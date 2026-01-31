---
代理人：“代理人”
描述：“分析应用程序中使用的 Azure 资源（IaC 文件和/或目标 rg 中的资源）并优化成本 - 为已确定的优化创建 GitHub 问题。”
---

# Azure 成本优化

此工作流分析基础结构即代码 (IaC) 文件和 Azure 资源以生成成本优化建议。它为每个优化机会创建单独的 GitHub 问题，并创建一个 EPIC 问题来协调实施，从而实现成本节约计划的高效跟踪和执行。

## 先决条件
- Azure MCP 服务器已配置并经过身份验证
- GitHub MCP 服务器已配置并经过身份验证  
- 已确定目标 GitHub 存储库
- 部署的 Azure 资源（IaC 文件可选但很有帮助）
- 在可用时，优先使用 Azure MCP 工具 (`azmcp-*`)，而不是直接 Azure CLI

## 工作流程步骤

### 步骤 1：获取 Azure 最佳实践
**行动**：在分析之前检索成本优化最佳实践
**工具**：Azure MCP 最佳实践工具
**流程**：
1. **加载最佳实践**：
   - 执行 `azmcp-bestpractices-get` 获取一些最新的 Azure 优化指南。这可能无法涵盖所有​​场景，但提供了基础。
   - 使用这些实践尽可能为后续分析和建议提供信息
   - 参考优化建议中的最佳实践，来自 MCP 工具输出或一般 Azure 文档

### 第 2 步：发现 Azure 基础设施
**操作**：动态发现和分析 Azure 资源和配置
**工具**：Azure MCP 工具 + Azure CLI 回退 + 本地文件系统访问
**流程**：
1. **资源发现**：
   - 执行 `azmcp-subscription-list` 查找可用的订阅
   - 执行`azmcp-group-list --subscription <subscription-id>`查找资源组
   - 获取相关组中所有资源的列表：
     - 使用 `az resource list --subscription <id> --resource-group <name>`
   - 对于每种资源类型，如果可能的话，首先使用 MCP 工具，然后使用 CLI 回退：
     - `azmcp-cosmos-account-list --subscription <id>` - Cosmos DB 帐户
     - `azmcp-storage-account-list --subscription <id>` - 存储帐户  
     - `azmcp-monitor-workspace-list --subscription <id>` - Log Analytics 工作区
     - `azmcp-keyvault-key-list` - 密钥库
     - `az webapp list` - Web 应用程序（后备 - 没有可用的 MCP 工具）
     - `az appservice plan list` - 应用程序服务计划（后备）
     - `az functionapp list` - 功能应用程序（后备）
     - `az sql server list` - SQL Server（后备）
     - `az redis list` - Redis 缓存（后备）
     - ...其他资源类型依此类推

2. **IaC 检测**：
   - 使用 `file_search` 扫描 IaC 文件：“**/*.bicep”、“**/*.tf”、“**/main.json”、“**/*template*.json”
   - 解析资源定义以了解预期的配置
   - 与发现的资源进行比较以识别差异
   - 请注意 IaC 文件的存在，以便稍后提出实施建议
   - 不要使用存储库中的任何其他文件，只能使用 IaC 文件。不允许使用其他文件，因为它不是事实来源。
   - 如果未找到 IaC 文件，则停止并向用户报告未找到 IaC 文件。

3. **配置分析**：
   - 提取每个资源的当前 SKU、层和设置
   - 识别资源关系和依赖关系
   - 绘制可用资源利用模式图

### 第 3 步：收集使用指标并验证当前成本
**行动**：收集利用率数据并验证实际资源成本
**工具**：Azure MCP 监视工具 + Azure CLI
**流程**：
1. **查找监控源**：
   - 使用 `azmcp-monitor-workspace-list --subscription <id>` 查找 Log Analytics 工作区
   - 使用 `azmcp-monitor-table-list --subscription <id> --workspace <name> --table-type "CustomLog"` 发现可用数据

2. **执行使用情况查询**：
   - 将 `azmcp-monitor-log-query` 与这些预定义查询一起使用：
     - 查询：“最近”最近的活动模式
     - 查询：指示问题的错误级别日志的“errors”
   - 对于自定义分析，请使用 KQL 查询：
   ```kql
   // CPU utilization for App Services
   AppServiceAppLogs
   | where TimeGenerated > ago(7d)
   | summarize avg(CpuTime) by Resource, bin(TimeGenerated, 1h)
   
   // Cosmos DB RU consumption  
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.DOCUMENTDB"
   | where TimeGenerated > ago(7d)
   | summarize avg(RequestCharge) by Resource
   
   // Storage account access patterns
   StorageBlobLogs
   | where TimeGenerated > ago(7d)
   | summarize RequestCount=count() by AccountName, bin(TimeGenerated, 1d)
   ```

3. **计算基线指标**：
   - CPU/内存利用率平均值
   - 数据库吞吐量模式
   - 存储访问频率
   - 函数执行率

4. **验证当前成本**： 
   - 使用步骤 2 中发现的 SKU/层配置
   - 在 https://azure.microsoft.com/pricing/ 查找当前的 Azure 定价或使用 `az billing` 命令
   - 文档：资源 → 当前 SKU → 预计每月成本
   - 在继续提出建议之前计算实际的当前每月总数

### 第 4 步：生成成本优化建议
**行动**：分析资源以识别优化机会
**工具**：使用收集的数据进行本地分析
**流程**：
1. **根据找到的资源类型应用优化模式**：
   
   **计算优化**：
   - 应用服务计划：根据 CPU/内存使用情况调整大小
   - 功能应用：高级版 → 低使用率的消费计划
   - 虚拟机：缩小超大实例
   
   **数据库优化**：
   - 宇宙数据库： 
     - 针对可变工作负载配置 → 无服务器
     - 根据实际使用情况调整 RU/s 大小
   - SQL 数据库：根据 DTU 使用情况调整适当大小的服务层
   
   **存储优化**：
   - 实施生命周期策略（热→冷→存档）
   - 整合冗余存储帐户
   - 根据访问模式调整适当大小的存储层
   
   **基础设施优化**：
   - 删除未使用/冗余的资源
   - 在有利的情况下实施自动缩放
   - 安排非生产环境

2. **计算基于证据的节省**： 
   - 当前验证的成本 → 目标成本 = 节省的成本
   - 记录当前配置和目标配置的定价来源

3. **计算每项建议的优先级分数**：
   ```
   Priority Score = (Value Score × Monthly Savings) / (Risk Score × Implementation Days)
   
   High Priority: Score > 20
   Medium Priority: Score 5-20
   Low Priority: Score < 5
   ```

4. **验证建议**：
   - 确保 Azure CLI 命令准确
   - 验证预计节省的计算结果
   - 评估实施风险和先决条件
   - 确保所有节省计算都有支持证据

### 第五步：用户确认
**操作**：在创建 GitHub 问题之前提供摘要并获得批准
**流程**：
1. **显示优化总结**：
   ```
   🎯 Azure Cost Optimization Summary
   
   📊 Analysis Results:
   • Total Resources Analyzed: X
   • Current Monthly Cost: $X 
   • Potential Monthly Savings: $Y 
   • Optimization Opportunities: Z
   • High Priority Items: N
   
   🏆 Recommendations:
   1. [Resource]: [Current SKU] → [Target SKU] = $X/month savings - [Risk Level] | [Implementation Effort]
   2. [Resource]: [Current Config] → [Target Config] = $Y/month savings - [Risk Level] | [Implementation Effort]
   3. [Resource]: [Current Config] → [Target Config] = $Z/month savings - [Risk Level] | [Implementation Effort]
   ... and so on
   
   💡 This will create:
   • Y individual GitHub issues (one per optimization)
   • 1 EPIC issue to coordinate implementation
   
   ❓ Proceed with creating GitHub issues? (y/n)
   ```

2. **等待用户确认**：仅在用户确认后才继续

### 第 6 步：创建单独的优化问题
**操作**：为每个优化机会创建单独的 GitHub 问题。将它们标记为“成本优化”（绿色）、“天蓝色”（蓝色）。
**所需的 MCP 工具**：每个建议的 `create_issue`
**流程**：
1. **使用此模板创建单独的问题**：

   **标题格式**：`[COST-OPT] [Resource Type] - [Brief Description] - $X/month savings`
   
   **正文模板**：
   ```markdown
   ## 💰 Cost Optimization: [Brief Title]
   
   **Monthly Savings**: $X | **Risk Level**: [Low/Medium/High] | **Implementation Effort**: X days
   
   ### 📋 Description
   [Clear explanation of the optimization and why it's needed]
   
   ### 🔧 Implementation
   
   **IaC Files Detected**: [Yes/No - based on file_search results]
   
   ```bash
   # 如果找到 IaC 文件：显示 IaC 修改 + 部署
   # 文件：基础设施/bicep/modules/app-service.bicep
   # 更改：sku.name：'S3' → 'B2'
   az 部署组创建 --resource-group [rg] --template-file 基础架构/bicep/main.bicep
   
   # 如果没有 IaC 文件：直接 Azure CLI 命令 + 警告
   # ⚠️ 未找到 IaC 文件。如果它们存在于其他地方，请修改它们。
   az appservice 计划更新 --name [计划] --sku B2
   ```
   
   ### 📊 Evidence
   - Current Configuration: [details]
   - Usage Pattern: [evidence from monitoring data]
   - Cost Impact: $X/month → $Y/month
   - Best Practice Alignment: [reference to Azure best practices if applicable]
   
   ### ✅ Validation Steps
   - [ ] Test in non-production environment
   - [ ] Verify no performance degradation
   - [ ] Confirm cost reduction in Azure Cost Management
   - [ ] Update monitoring and alerts if needed
   
   ### ⚠️ Risks & Considerations
   - [Risk 1 and mitigation]
   - [Risk 2 and mitigation]
   
   **Priority Score**: X | **Value**: X/10 | **Risk**: X/10
   ```

### 第 7 步：创建 EPIC 协调问题
**操作**：创建主问题来跟踪所有优化工作。将其标记为“成本优化”（绿色）、“天蓝色”（蓝色）和“史诗”（紫色）。
**所需的 MCP 工具**：EPIC 的 `create_issue`
**关于美人鱼图的注意事项**：确保您验证美人鱼语法是否正确，并在创建图表时考虑可访问性指南（样式、颜色等）。
**流程**：
1. **创建史诗问题**：

   **标题**：`[EPIC] Azure Cost Optimization Initiative - $X/month potential savings`
   
   **正文模板**：
   ```markdown
   # 🎯 Azure Cost Optimization EPIC
   
   **Total Potential Savings**: $X/month | **Implementation Timeline**: X weeks
   
   ## 📊 Executive Summary
   - **Resources Analyzed**: X
   - **Optimization Opportunities**: Y  
   - **Total Monthly Savings Potential**: $X
   - **High Priority Items**: N
   
   ## 🏗️ Current Architecture Overview
   
   ```mermaid
   图TB
       子图“资源组：[名称]”
           [生成的架构图显示当前资源和成本]
       结束
   ```
   
   ## 📋 Implementation Tracking
   
   ### 🚀 High Priority (Implement First)
   - [ ] #[issue-number]: [Title] - $X/month savings
   - [ ] #[issue-number]: [Title] - $X/month savings
   
   ### ⚡ Medium Priority 
   - [ ] #[issue-number]: [Title] - $X/month savings
   - [ ] #[issue-number]: [Title] - $X/month savings
   
   ### 🔄 Low Priority (Nice to Have)
   - [ ] #[issue-number]: [Title] - $X/month savings
   
   ## 📈 Progress Tracking
   - **Completed**: 0 of Y optimizations
   - **Savings Realized**: $0 of $X/month
   - **Implementation Status**: Not Started
   
   ## 🎯 Success Criteria
   - [ ] All high-priority optimizations implemented
   - [ ] >80% of estimated savings realized
   - [ ] No performance degradation observed
   - [ ] Cost monitoring dashboard updated
   
   ## 📝 Notes
   - Review and update this EPIC as issues are completed
   - Monitor actual vs. estimated savings
   - Consider scheduling regular cost optimization reviews
   ```

## 错误处理
- **成本验证**：如果节省估算缺乏支持证据或看起来与 Azure 定价不一致，请在继续之前重新验证配置和定价来源
- **Azure 身份验证失败**：提供手动 Azure CLI 设置步骤
- **未找到资源**：创建有关 Azure 资源部署的信息问题
- **GitHub 创建失败**：将格式化建议输出到控制台
- **使用数据不足**：注意限制并仅提供基于配置的建议

## 成功标准
- ✅ 根据实际资源配置和 Azure 定价验证所有成本估算
- ✅ 为每个优化创建的单独问题（可跟踪和可分配）
- ✅ EPIC问题提供全面的协调和跟踪
- ✅ 所有建议都包含特定的可执行 Azure CLI 命令
- ✅ 优先评分可实现以投资回报率为中心的实施
- ✅ 架构图准确表示当前状态
- ✅ 用户确认可防止产生不必要的问题
