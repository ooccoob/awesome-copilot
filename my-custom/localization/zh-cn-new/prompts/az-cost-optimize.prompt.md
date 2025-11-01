---
mode: 'agent'
description: '分析应用中使用的Azure资源（IaC文件和/或目标资源组中的资源），优化成本 - 为识别的优化机会创建GitHub问题。'
---

# Azure 成本优化

此工作流分析基础架构即代码（IaC）文件和Azure资源，生成成本优化建议。它为每个优化机会创建单独的GitHub问题，并创建一个EPIC问题来协调实施，从而实现成本节约计划的高效跟踪和执行。

## 先决条件
- Azure MCP服务器已配置并身份验证
- GitHub MCP服务器已配置并身份验证
- 目标GitHub仓库已识别
- Azure资源已部署（IaC文件可选但有帮助）
- 在可用时，优先使用Azure MCP工具（`azmcp-*`）而不是直接Azure CLI

## 工作流步骤

### 步骤1：获取Azure最佳实践
**操作**：在分析之前检索成本优化最佳实践
**工具**：Azure MCP最佳实践工具
**流程**：
1. **加载最佳实践**：
   - 执行`azmcp-bestpractices-get`获取一些最新的Azure优化指南。这可能不会涵盖所有场景，但提供基础。
   - 尽可能使用这些实践来指导后续分析和建议
   - 在优化建议中引用最佳实践，无论是来自MCP工具输出还是通用Azure文档

### 步骤2：发现Azure基础架构
**操作**：动态发现和分析Azure资源和配置
**工具**：Azure MCP工具 + Azure CLI回退 + 本地文件系统访问
**流程**：
1. **资源发现**：
   - 执行`azmcp-subscription-list`查找可用订阅
   - 执行`azmcp-group-list --subscription <subscription-id>`查找资源组
   - 获取相关资源组中所有资源的列表：
     - 使用`az resource list --subscription <id> --resource-group <name>`
   - 对于每种资源类型，尽可能首先使用MCP工具，然后CLI回退：
     - `azmcp-cosmos-account-list --subscription <id>` - Cosmos DB账户
     - `azmcp-storage-account-list --subscription <id>` - 存储账户
     - `azmcp-monitor-workspace-list --subscription <id>` - Log Analytics工作区
     - `azmcp-keyvault-key-list` - 密钥保管库
     - `az webapp list` - Web应用（回退 - 无MCP工具可用）
     - `az appservice plan list` - 应用服务计划（回退）
     - `az functionapp list` - 函数应用（回退）
     - `az sql server list` - SQL服务器（回退）
     - `az redis list` - Redis缓存（回退）
     - 等等，其他资源类型依此类推

2. **IaC检测**：
   - 使用`file_search`扫描IaC文件："**/*.bicep", "**/*.tf", "**/main.json", "**/*template*.json"
   - 解析资源定义以了解预期配置
   - 与发现的资源进行比较以识别差异
   - 注意IaC文件的存在以便后续实施建议
   - 不要使用仓库中的任何其他文件，只使用IaC文件。使用其他文件是不允许的，因为它不是真实来源。
   - 如果没有找到IaC文件，则停止并向用户报告未找到IaC文件。

3. **配置分析**：
   - 提取每个资源的当前SKU、层级和设置
   - 识别资源关系和依赖项
   - 在可用时映射资源利用模式

### 步骤3：收集使用指标和验证当前成本
**操作**：收集利用数据并验证实际资源成本
**工具**：Azure MCP监控工具 + Azure CLI
**流程**：
1. **查找监控源**：
   - 使用`azmcp-monitor-workspace-list --subscription <id>`查找Log Analytics工作区
   - 使用`azmcp-monitor-table-list --subscription <id> --workspace <name> --table-type "CustomLog"`发现可用数据

2. **执行使用查询**：
   - 使用`azmcp-monitor-log-query`与这些预定义查询：
     - 查询："recent"用于最近的活动模式
     - 查询："errors"用于指示问题的错误级别日志
   - 对于自定义分析，使用KQL查询：
   ```kql
   // App服务的CPU利用率
   AppServiceAppLogs
   | where TimeGenerated > ago(7d)
   | summarize avg(CpuTime) by Resource, bin(TimeGenerated, 1h)

   // Cosmos DB RU消耗
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.DOCUMENTDB"
   | where TimeGenerated > ago(7d)
   | summarize avg(RequestCharge) by Resource

   // 存储账户访问模式
   StorageBlobLogs
   | where TimeGenerated > ago(7d)
   | summarize RequestCount=count() by AccountName, bin(TimeGenerated, 1d)
   ```

3. **计算基线指标**：
   - CPU/内存利用率平均值
   - 数据库吞吐量模式
   - 存储访问频率
   - 函数执行速率

4. **验证当前成本**：
   - 使用在步骤2中发现的SKU/层级配置
   - 在https://azure.microsoft.com/pricing/查找当前Azure定价或使用`az billing`命令
   - 文档：资源 → 当前SKU → 预估月度成本
   - 在继续建议之前计算现实的当前月度总成本

### 步骤4：生成成本优化建议
**操作**：分析资源以识别优化机会
**工具**：使用收集的数据进行本地分析
**流程**：
1. **基于找到的资源类型应用优化模式**：

   **计算优化**：
   - 应用服务计划：基于CPU/内存使用量调整大小
   - 函数应用：对于低使用量，Premium → Consumption计划
   - 虚拟机：缩小过大实例

   **数据库优化**：
   - Cosmos DB:
     - 对于可变工作负载，Provisioned → Serverless
     - 基于实际使用量调整RU/s大小
   - SQL数据库：基于DTU使用量调整服务层级大小

   **存储优化**：
   - 实施生命周期策略（热 → 冷 → 归档）
   - 合并冗余存储账户
   - 基于访问模式调整存储层级大小

   **基础架构优化**：
   - 删除未使用/冗余资源
   - 在有益的地方实施自动缩放
   - 调度非生产环境

2. **计算基于证据的节省**：
   - 当前验证成本 → 目标成本 = 节省
   - 记录当前和目标配置的定价来源

3. **为每个建议计算优先级分数**：
   ```
   优先级分数 = (价值分数 × 月度节省) / (风险分数 × 实施天数)

   高优先级：分数 > 20
   中优先级：分数 5-20
   低优先级：分数 < 5
   ```

4. **验证建议**：
   - 确保Azure CLI命令准确
   - 验证预估节省计算
   - 评估实施风险和先决条件
   - 确保所有节省计算都有支持证据

### 步骤5：用户确认
**操作**：在创建GitHub问题之前显示摘要并获得批准
**流程**：
1. **显示优化摘要**：
   ```
   🎯 Azure 成本优化摘要

   📊 分析结果：
   • 分析的总资源：X
   • 当前月度成本：$X
   • 潜在月度节省：$Y
   • 优化机会：Z
   • 高优先级项目：N

   🏆 建议：
   1. [资源]：[当前SKU] → [目标SKU] = $X/月节省 - [风险级别] | [实施工作量]
   2. [资源]：[当前配置] → [目标配置] = $Y/月节省 - [风险级别] | [实施工作量]
   3. [资源]：[当前配置] → [目标配置] = $Z/月节省 - [风险级别] | [实施工作量]
   ... 等等

   💡 这将创建：
   • Y个单独的GitHub问题（每个优化一个）
   • 1个EPIC问题来协调实施

   ❓ 继续创建GitHub问题？（y/n）
   ```

2. **等待用户确认**：只有在用户确认时才继续

### 步骤6：创建单独的优化问题
**操作**：为每个优化机会创建单独的GitHub问题。用"cost-optimization"（绿色）、"azure"（蓝色）标记它们。
**所需MCP工具**：为每个建议使用`create_issue`
**流程**：
1. **使用此模板创建单独问题**：

   **标题格式**：`[COST-OPT] [资源类型] - [简要描述] - $X/月节省`

   **正文模板**：
   ```markdown
   ## 💰 成本优化：[简要标题]

   **月度节省**：$X | **风险级别**：[低/中/高] | **实施工作量**：X天

   ### 📋 描述
   [优化的清晰解释以及为什么需要它]

   ### 🔧 实施

   **检测到IaC文件**：[是/否 - 基于file_search结果]

   ```bash
   # 如果找到IaC文件：显示IaC修改 + 部署
   # 文件：infrastructure/bicep/modules/app-service.bicep
   # 更改：sku.name: 'S3' → 'B2'
   az deployment group create --resource-group [rg] --template-file infrastructure/bicep/main.bicep

   # 如果没有IaC文件：直接Azure CLI命令 + 警告
   # ⚠️ 未找到IaC文件。如果它们存在于别处，请修改那些文件。
   az appservice plan update --name [plan] --sku B2
   ```

   ### 📊 证据
   - 当前配置：[详情]
   - 使用模式：[来自监控数据的证据]
   - 成本影响：$X/月 → $Y/月
   - 最佳实践对齐：[如果适用，引用Azure最佳实践]

   ### ✅ 验证步骤
   - [ ] 在非生产环境中测试
   - [ ] 验证没有性能下降
   - [ ] 在Azure成本管理中确认成本降低
   - [ ] 如果需要，更新监控和警报

   ### ⚠️ 风险和考虑因素
   - [风险1和缓解措施]
   - [风险2和缓解措施]

   **优先级分数**：X | **价值**：X/10 | **风险**：X/10
   ```

### 步骤7：创建EPIC协调问题
**操作**：创建主问题来跟踪所有优化工作。用"cost-optimization"（绿色）、"azure"（蓝色）和"epic"（紫色）标记它。
**所需MCP工具**：为EPIC使用`create_issue`
**关于mermaid图的说明**：确保验证mermaid语法正确，并在考虑可访问性指南（样式、颜色等）的情况下创建图表。
**流程**：
1. **创建EPIC问题**：

   **标题**：`[EPIC] Azure成本优化计划 - $X/月潜在节省`

   **正文模板**：
   ```markdown
   # 🎯 Azure 成本优化 EPIC

   **总潜在节省**：$X/月 | **实施时间线**：X周

   ## 📊 执行摘要
   - **分析的资源**：X
   - **优化机会**：Y
   - **总月度节省潜力**：$X
   - **高优先级项目**：N

   ## 🏗️ 当前架构概览

   ```mermaid
   graph TB
       subgraph "资源组：[名称]"
           [生成的架构图显示当前资源和成本]
       end
   ```

   ## 📋 实施跟踪

   ### 🚀 高优先级（首先实施）
   - [ ] #[问题编号]：[标题] - $X/月节省
   - [ ] #[问题编号]：[标题] - $X/月节省

   ### ⚡ 中优先级
   - [ ] #[问题编号]：[标题] - $X/月节省
   - [ ] #[问题编号]：[标题] - $X/月节省

   ### 🔄 低优先级（有也不错）
   - [ ] #[问题编号]：[标题] - $X/月节省

   ## 📈 进度跟踪
   - **已完成**：Y个优化中的0个
   - **实现节省**：$X/月中的$0
   - **实施状态**：未开始

   ## 🎯 成功标准
   - [ ] 所有高优先级优化已实施
   - [ ] >80%的预估节省已实现
   - [ ] 未观察到性能下降
   - [ ] 成本监控仪表板已更新

   ## 📝 备注
   - 在问题完成时审查和更新此EPIC
   - 监控实际与预估节省
   - 考虑安排定期成本优化审查
   ```

## 错误处理
- **成本验证**：如果节省估算缺乏支持证据或与Azure定价不一致，在继续之前重新验证配置和定价来源
- **Azure身份验证失败**：提供手动Azure CLI设置步骤
- **未找到资源**：创建关于Azure资源部署的信息问题
- **GitHub创建失败**：向控制台输出格式化建议
- **使用数据不足**：注意限制，仅提供基于配置的建议

## 成功标准
- ✅ 所有成本估算都根据实际资源配置和Azure定价进行了验证
- ✅ 为每个优化创建了单独问题（可跟踪和可分配）
- ✅ EPIC问题提供全面的协调和跟踪
- ✅ 所有建议都包括具体的、可执行的Azure CLI命令
- ✅ 优先级评分支持以ROI为重点的实施
- ✅ 架构图准确表示当前状态
- ✅ 用户确认防止不想要的问题创建