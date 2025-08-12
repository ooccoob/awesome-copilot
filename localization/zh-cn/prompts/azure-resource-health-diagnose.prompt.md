---
mode: "agent"
description: "分析 Azure 资源健康状况，基于日志与遥测诊断问题，并为识别到的问题制定修复计划。"
---

# Azure 资源健康与问题诊断

该工作流针对特定 Azure 资源：评估其健康状态，使用日志与遥测诊断潜在问题，并为发现的问题制定完整的修复计划。

## 前置条件

- 已配置并完成身份验证的 Azure MCP 服务器
- 已确定目标 Azure 资源（名称，及可选的资源组/订阅）
- 资源必须已部署并运行，以便产生日志/遥测
- 当可用时优先使用 Azure MCP 工具（`azmcp-*`），仅在必要时回退到 Azure CLI

## 工作流步骤

### 步骤 1：获取 Azure 最佳实践

**动作**：检索诊断与故障排查最佳实践
**工具**：Azure MCP 最佳实践工具
**流程**：

1. 加载最佳实践：
   - 运行 Azure 最佳实践工具获取诊断指南
   - 关注健康监控、日志分析与问题解决模式
   - 在诊断方法与修复建议中引用这些实践

### 步骤 2：资源发现与识别

**动作**：定位并识别目标 Azure 资源
**工具**：Azure MCP 工具 + Azure CLI 回退
**流程**：

1. 资源查找：

   - 仅提供资源名时：使用 `azmcp-subscription-list` 跨订阅搜索
   - 使用 `az resource list --name <resource-name>` 查找匹配资源
   - 若匹配项过多，提示用户指定订阅/资源组
   - 收集资源详情：
     - 资源类型与当前状态
     - 所在区域、标签与配置
     - 关联服务与依赖

2. 资源类型检测：
   - 识别资源类型以确定合适的诊断方法：
     - Web/Function 应用：应用日志、性能指标、依赖跟踪
     - 虚拟机：系统日志、性能计数器、启动诊断
     - Cosmos DB：请求指标、限流、分区统计
     - 存储账户：访问日志、性能指标、可用性
     - SQL 数据库：查询性能、连接日志、资源使用
     - Application Insights：应用遥测、异常、依赖
     - Key Vault：访问日志、证书状态、密钥/机密使用
     - Service Bus：消息指标、死信队列、吞吐

### 步骤 3：健康状态评估

**动作**：评估当前资源健康与可用性
**工具**：Azure MCP 监控工具 + Azure CLI
**流程**：

1. 基本健康检查：

   - 检查资源置备状态与运行状态
   - 验证服务可用性与响应能力
   - 回顾近期部署或配置更改
   - 评估当前资源利用率（CPU、内存、存储等）

2. 服务特定健康指标：
   - Web 应用：HTTP 状态码、响应时长、可用性
   - 数据库：连接成功率、查询性能、死锁
   - 存储：可用性百分比、请求成功率、时延
   - 虚拟机：启动诊断、来宾 OS 指标、网络连通性
   - Functions：执行成功率、时长、错误频次

### 步骤 4：日志与遥测分析

**动作**：分析日志与遥测以识别问题与模式
**工具**：Azure MCP 监控工具（用于 Log Analytics 查询）
**流程**：

1. 定位监控源：

   - 使用 `azmcp-monitor-workspace-list` 识别 Log Analytics 工作区
   - 定位与资源关联的 Application Insights 实例
   - 使用 `azmcp-monitor-table-list` 确认相关日志表

2. 执行诊断查询：
   通过 `azmcp-monitor-log-query`，基于资源类型使用针对性的 KQL：

   通用错误分析：

   ```kql
   // 最近错误与异常
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

   性能分析：

   ```kql
   // 性能退化模式
   | where TimeGenerated > ago(7d)
   | where ObjectName == "Processor" and CounterName == "% Processor Time"
   | where avg_CounterValue > 80
   ```

   应用特定查询：

   // Application Insights - 失败请求
   requests
   **免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot) 本地化生成，因此可能包含错误。若发现不当或错误翻译，请创建一个[问题](https://github.com/ooccoob/datafill/issues)。
   | where timestamp > ago(24h)
   | where success == false
   | summarize FailureCount=count() by resultCode, bin(timestamp, 1h)
   | order by timestamp desc

   // 数据库 - 连接失败
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.SQL"
   | where Category == "SQLSecurityAuditEvents"
   | where action_name_s == "CONNECTION_FAILED"
   | summarize ConnectionFailures=count() by bin(TimeGenerated, 1h)

   ```

   ```

3. 模式识别：
   - 识别重复出现的错误模式或异常
   - 将错误与部署时间或配置更改进行关联
   - 分析性能趋势与退化模式
   - 检查依赖故障或外部服务问题

### 步骤 5：问题分类与根因分析

**动作**：对识别的问题分类并确定根因
**流程**：

1. 问题分类：

   - 严重：服务不可用、数据丢失、安全事件
   - 高：性能退化、间歇性故障、高错误率
   - 中：警告、次优配置、轻微性能问题
   - 低：信息性告警、优化机会

2. 根因分析：

   - 配置问题：设置错误、缺失依赖
   - 资源约束：CPU/内存/磁盘限制、限流
   - 网络问题：连通性、DNS 解析、防火墙
   - 应用问题：代码缺陷、内存泄漏、低效查询
   - 外部依赖：第三方服务故障、API 限额
   - 安全问题：身份验证失败、证书过期

3. 影响评估：
   - 评估业务影响与受影响用户/系统
   - 评估数据完整性与安全影响
   - 评估恢复时间目标与优先级

### 步骤 6：制定修复计划

**动作**：创建全面的修复计划来处理识别的问题
**流程**：

1. 立即动作（严重问题）：

   - 应急修复以恢复服务可用性
   - 临时措施以减轻影响
   - 对复杂问题的升级流程

2. 短期修复（高/中问题）：

   - 配置调整与资源扩缩
   - 应用更新与补丁
   - 监控与告警改进

3. 长期改进（所有问题）：

   - 面向更高韧性的架构变更
   - 预防性措施与监控增强
   - 文档与流程改进

4. 实施步骤：
   - 带有具体 Azure CLI 命令的优先级行动清单
   - 测试与验证过程
   - 每项变更的回滚计划
   - 用于验证修复效果的监控

### 步骤 7：用户确认与报告生成

**动作**：展示发现并获取修复动作批准
**流程**：

1. 显示健康评估摘要：

   ```
   🏥 Azure 资源健康评估

   📊 资源概览：
   • 资源：[名称]（[类型]）
   • 状态：[Healthy/Warning/Critical]
   • 区域：[Region]
   • 最近分析时间：[Timestamp]

   🚨 识别的问题：
   • 严重：X 个需立即处理
   • 高：Y 个影响性能/可靠性
   • 中：Z 个优化项
   • 低：N 个信息项

   🔍 重点问题：
   1. [问题类型]：[描述] - 影响：[高/中/低]
   2. [问题类型]：[描述] - 影响：[高/中/低]
   3. [问题类型]：[描述] - 影响：[高/中/低]

   🛠️ 修复计划：
   • 立即动作：X 项
   • 短期修复：Y 项
   • 长期改进：Z 项
   • 预计完成时间：[时间]

   ❓是否继续生成详细修复计划？(y/n)
   ```

2. 生成详细报告：

   ````markdown
   # Azure 资源健康报告：[资源名称]

   **生成时间**：[Timestamp]
   **资源**：[完整资源 ID]
   **总体健康**：[状态 + 颜色指示]

   ## 🔍 执行摘要

   [健康状态与关键发现的简述]

   ## 📈 健康指标

   - 可用性：近 24h 为 X%
   - 性能：[平均响应时间/吞吐]
   - 错误率：近 24h 为 X%
   - 资源使用：CPU/内存/存储百分比

   ## 🚨 识别的问题

   ### 严重问题

   - [问题 1]：[描述]
     - 根因：[…]
     - 影响：[…]
     - 立即动作：[…]

   ### 高优先问题

   - [问题 2]：[描述]
     - 根因：[…]
     - 影响：[…]
     - 建议修复：[…]

   ## 🛠️ 修复计划

   ### 阶段 1：立即动作（0–2 小时）

   ```bash
   # 用于恢复服务的关键修复
   [Azure CLI 命令 + 说明]
   ```
   ````

   ### 阶段 2：短期修复（2–24 小时）

   ```bash
   # 提升性能与可靠性
   [Azure CLI 命令 + 说明]
   ```

   ### 阶段 3：长期改进（1–4 周）

   ```bash
   # 架构性与预防性措施
   [Azure CLI 命令 + 配置变更]
   ```

   ## 📊 监控建议

   - 建议告警：[…]
   - 仪表板：[…]
   - 定期健康检查：[…]

   ## ✅ 验证步骤

   - [ ] 通过日志验证问题已解决
   - [ ] 确认性能改善
   - [ ] 测试应用功能
   - [ ] 更新监控与告警
   - [ ] 记录复盘结论

   ## 📝 预防措施

   - [预防建议]
   - [流程改进]
   - [监控增强]

   ```

   ```

## 错误处理

- 未找到资源：给出资源名/位置的指定指引
- 身份验证问题：指导完成 Azure 身份验证设置
- 权限不足：列出访问所需的 RBAC 角色
- 无日志可用：建议启用诊断设置并等待数据
- 查询超时：将分析拆分为更小的时间窗口
- 服务特定限制：提供带限制说明的通用健康评估

## 成功标准

- ✅ 准确评估资源健康状态
- ✅ 识别并分类所有重要问题
- ✅ 主要问题完成根因分析
- ✅ 提供可执行的修复计划与具体步骤
- ✅ 包含监控与预防建议
- ✅ 按业务影响清晰排序问题
- ✅ 实施步骤包含验证与回滚

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 本地化生成，因此可能包含错误。若发现不当或错误翻译，请创建一个[问题](../../issues)。
