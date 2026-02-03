---
agent: 'agent'
description: 'Analyze Azure resource health, diagnose issues from logs and telemetry, and create a remediation plan for identified problems.'
---

# Azure 资源运行状况和问题诊断

此工作流分析特定的 Azure 资源以评估其运行状况，使用日志和遥测数据诊断潜在问题，并针对发现的任何问题制定全面的修复计划。

## 先决条件
- Azure MCP 服务器已配置并经过身份验证
- 已识别的目标 Azure 资源（名称和可选的资源组/订阅）
- 必须部署并运行资源才能生成日志/遥测数据
- 在可用时，优先使用 Azure MCP 工具 (`azmcp-*`)，而不是直接 Azure CLI

## 工作流程步骤

### 步骤 1：获取 Azure 最佳实践
**操作**：检索诊断和故障排除最佳实践
**工具**：Azure MCP 最佳实践工具
**流程**：
1. **加载最佳实践**：
   - 执行 Azure 最佳实践工具来获取诊断指南
   - 专注于健康监控、日志分析和问题解决模式
   - 使用这些实践来告知诊断方法和补救建议

### 第 2 步：资源发现和识别
**操作**：找到并识别目标 Azure 资源
**工具**：Azure MCP 工具 + Azure CLI 后备
**流程**：
1. **资源查找**：
   - 如果仅提供资源名称：使用 `azmcp-subscription-list` 跨订阅搜索
   - 使用 `az resource list --name <resource-name>` 查找匹配的资源
   - 如果找到多个匹配项，则提示用户指定订阅/资源组
   - 收集详细的资源信息：
     - 资源类型和现状
     - 位置、标签和配置
     - 关联服务和依赖项

2. **资源类型检测**：
   - 确定资源类型以确定适当的诊断方法：
     - **Web 应用程序/功能应用程序**：应用程序日志、性能指标、依赖项跟踪
     - **虚拟机**：系统日志、性能计数器、启动诊断
     - **Cosmos DB**：请求指标、限制、分区统计信息
     - **存储帐户**：访问日志、性能指标、可用性
     - **SQL 数据库**：查询性能、连接日志、资源利用率
     - **应用程序洞察**：应用程序遥测、异常、依赖项
     - **Key Vault**：访问日志、证书状态、秘密使用情况
     - **服务总线**：消息指标、死信队列、吞吐量

### 第三步：健康状况评估
**行动**：评估当前资源的运行状况和可用性
**工具**：Azure MCP 监视工具 + Azure CLI
**流程**：
1. **基本健康检查**：
   - 检查资源配置状态和运行状态
   - 验证服务可用性和响应能力
   - 查看最近的部署或配置更改
   - 评估当前资源利用率（CPU、内存、存储等）

2. **特定服务的健康指标**：
   - **Web 应用程序**：HTTP 响应代码、响应时间、正常运行时间
   - **数据库**：连接成功率、查询性能、死锁
   - **存储**：可用性百分比、请求成功率、延迟
   - **虚拟机**：启动诊断、来宾操作系统指标、网络连接
   - **功能**：执行成功率、持续时间、错误频率

### 第 4 步：日志和遥测分析
**操作**：分析日志和遥测以识别问题和模式
**工具**：用于 Log Analytics 查询的 Azure MCP 监视工具
**流程**：
1. **查找监控源**：
   - 使用 `azmcp-monitor-workspace-list` 标识 Log Analytics 工作区
   - 找到与资源关联的 Application Insights 实例
   - 使用 `azmcp-monitor-table-list` 识别相关日志表

2. **执行诊断查询**：
   根据资源类型将 `azmcp-monitor-log-query` 与目标 KQL 查询结合使用：

   **一般错误分析**：
   ```kql
   // Recent errors and exceptions
   union isfuzzy=true 
       AzureDiagnostics,
       AppServiceHTTPLogs,
       AppServiceAppLogs,
       AzureActivity
   | where TimeGenerated > ago(24h)
   | where Level == "Error" or ResultType != "Success"
   | summarize ErrorCount=count() by Resource, ResultType, bin(TimeGenerated, 1h)
   | order by TimeGenerated desc
   ```

   **性能分析**：
   ```kql
   // Performance degradation patterns
   Perf
   | where TimeGenerated > ago(7d)
   | where ObjectName == "Processor" and CounterName == "% Processor Time"
   | summarize avg(CounterValue) by Computer, bin(TimeGenerated, 1h)
   | where avg_CounterValue > 80
   ```

   **特定于应用程序的查询**：
   ```kql
   // Application Insights - Failed requests
   requests
   | where timestamp > ago(24h)
   | where success == false
   | summarize FailureCount=count() by resultCode, bin(timestamp, 1h)
   | order by timestamp desc
   
   // Database - Connection failures
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.SQL"
   | where Category == "SQLSecurityAuditEvents"
   | where action_name_s == "CONNECTION_FAILED"
   | summarize ConnectionFailures=count() by bin(TimeGenerated, 1h)
   ```

3. **模式识别**：
   - 识别重复出现的错误模式或异常
   - 将错误与部署时间或配置更改相关联
   - 分析性能趋势和退化模式
   - 查找依赖项故障或外部服务问题

### 第 5 步：问题分类和根本原因分析
**行动**：对已发现的问题进行分类并确定根本原因
**流程**：
1. **问题分类**：
   - **严重**：服务不可用、数据丢失、安全漏洞
   - **高**：性能下降、间歇性故障、高错误率
   - **中**：警告、次优配置、轻微性能问题
   - **低**：信息警报、优化机会

2. **根本原因分析**：
   - **配置问题**：设置不正确，缺少依赖项
   - **资源限制**：CPU/内存/磁盘限制、限制
   - **网络问题**：连接问题、DNS 解析、防火墙规则
   - **应用程序问题**：代码错误、内存泄漏、低效查询
   - **外部依赖**：第三方服务故障、API 限制
   - **安全问题**：身份验证失败、证书过期

3. **影响评估**：
   - 确定业务影响和受影响的用户/系统
   - 评估数据完整性和安全影响
   - 评估恢复时间目标和优先事项

### 第 6 步：生成补救计划
**行动**：制定全面的计划来解决已识别的问题
**流程**：
1. **立即采取行动**（关键问题）：
   - 紧急修复以恢复服务可用性
   - 减轻影响的临时解决办法
   - 复杂问题的升级程序

2. **短期修复**（高/中问题）：
   - 配置调整和资源扩展
   - 应用程序更新和补丁
   - 监控和警报改进

3. **长期改进**（所有问题）：
   - 架构变化以提高弹性
   - 预防措施和加强监测
   - 文档和流程改进

4. **实施步骤**：
   - 使用特定 Azure CLI 命令确定操作项目的优先级
   - 测试和验证程序
   - 每次变更的回滚计划
   - 监控以验证问题解决情况

### 第7步：用户确认和报告生成
**行动**：提出调查结果并获得补救行动的批准
**流程**：
1. **显示健康评估摘要**：
   ```
   🏥 Azure Resource Health Assessment
   
   📊 Resource Overview:
   • Resource: [Name] ([Type])
   • Status: [Healthy/Warning/Critical]
   • Location: [Region]
   • Last Analyzed: [Timestamp]
   
   🚨 Issues Identified:
   • Critical: X issues requiring immediate attention
   • High: Y issues affecting performance/reliability  
   • Medium: Z issues for optimization
   • Low: N informational items
   
   🔍 Top Issues:
   1. [Issue Type]: [Description] - Impact: [High/Medium/Low]
   2. [Issue Type]: [Description] - Impact: [High/Medium/Low]
   3. [Issue Type]: [Description] - Impact: [High/Medium/Low]
   
   🛠️ Remediation Plan:
   • Immediate Actions: X items
   • Short-term Fixes: Y items  
   • Long-term Improvements: Z items
   • Estimated Resolution Time: [Timeline]
   
   ❓ Proceed with detailed remediation plan? (y/n)
   ```

2. **生成详细报告**：
   ```markdown
   # Azure Resource Health Report: [Resource Name]
   
   **Generated**: [Timestamp]  
   **Resource**: [Full Resource ID]  
   **Overall Health**: [Status with color indicator]
   
   ## 🔍 Executive Summary
   [Brief overview of health status and key findings]
   
   ## 📊 Health Metrics
   - **Availability**: X% over last 24h
   - **Performance**: [Average response time/throughput]
   - **Error Rate**: X% over last 24h
   - **Resource Utilization**: [CPU/Memory/Storage percentages]
   
   ## 🚨 Issues Identified
   
   ### Critical Issues
   - **[Issue 1]**: [Description]
     - **Root Cause**: [Analysis]
     - **Impact**: [Business impact]
     - **Immediate Action**: [Required steps]
   
   ### High Priority Issues  
   - **[Issue 2]**: [Description]
     - **Root Cause**: [Analysis]
     - **Impact**: [Performance/reliability impact]
     - **Recommended Fix**: [Solution steps]
   
   ## 🛠️ Remediation Plan
   
   ### Phase 1: Immediate Actions (0-2 hours)
   ```bash
   # 恢复服务的关键修复
   [Azure CLI 命令及说明]
   ```
   
   ### Phase 2: Short-term Fixes (2-24 hours)
   ```bash
   # 性能和可靠性改进
   [Azure CLI 命令及说明]
   ```
   
   ### Phase 3: Long-term Improvements (1-4 weeks)
   ```bash
   # 建筑和预防措施
   [Azure CLI 命令和配置更改]
   ```
   
   ## 📈 Monitoring Recommendations
   - **Alerts to Configure**: [List of recommended alerts]
   - **Dashboards to Create**: [Monitoring dashboard suggestions]
   - **Regular Health Checks**: [Recommended frequency and scope]
   
   ## ✅ Validation Steps
   - [ ] Verify issue resolution through logs
   - [ ] Confirm performance improvements
   - [ ] Test application functionality
   - [ ] Update monitoring and alerting
   - [ ] Document lessons learned
   
   ## 📝 Prevention Measures
   - [Recommendations to prevent similar issues]
   - [Process improvements]
   - [Monitoring enhancements]
   ```

## 错误处理
- **找不到资源**：提供有关资源名称/位置规范的指导
- **身份验证问题**：指导用户完成 Azure 身份验证设置
- **权限不足**：列出资源访问所需的 RBAC 角色
- **没有可用日志**：建议启用诊断设置并等待数据
- **查询超时**：将分析分解为更小的时间窗口
- **特定于服务的问题**：提供一般健康评估，但注明了限制

## 成功标准
- ✅ 准确评估资源健康状况
- ✅ 已识别并分类的所有重大问题
- ✅ 完成主要问题的根本原因分析
- ✅ 提供具体步骤的可行补救计划
- ✅ 包括监测和预防建议
- ✅ 按业务影响明确问题的优先级
- ✅ 实施步骤包括验证和回滚程序
