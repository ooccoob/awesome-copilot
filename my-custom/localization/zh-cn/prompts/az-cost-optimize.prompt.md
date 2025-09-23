---
mode: "agent"
description: "分析应用使用的 Azure 资源（IaC 文件和/或目标资源组中的资源）并优化成本——为识别到的优化项分别创建 GitHub Issue。"
---

# Azure 成本优化

该工作流会分析基础设施即代码（IaC）文件与 Azure 资源，产生成本优化建议。它会为每个优化机会创建一个独立的 GitHub Issue，并创建一个用于统筹实施的 EPIC Issue，便于高效跟踪与执行节省举措。

## 前置条件

- 已配置并完成身份验证的 Azure MCP 服务器
- 已配置并完成身份验证的 GitHub MCP 服务器
- 已确定目标 GitHub 仓库
- 已部署的 Azure 资源（存在 IaC 文件更佳，但不是必须）
- 当可用时优先使用 Azure MCP 工具（`azmcp-*`），仅在必要时回退到 Azure CLI

## 工作流步骤

### 步骤 1：获取 Azure 最佳实践

**动作**：在分析前检索成本优化最佳实践
**工具**：Azure MCP 最佳实践工具
**流程**：

1. 加载最佳实践：
   - 执行 `azmcp-bestpractices-get` 以获取部分最新的 Azure 优化指南。该结果可能不覆盖全部场景，但可作为基础。
   - 在后续分析与建议中尽可能参考这些实践
   - 在优化建议中引用最佳实践来源，可来自 MCP 工具输出或 Azure 官方文档

### 步骤 2：发现 Azure 基础设施

**动作**：动态发现并分析 Azure 资源与配置
**工具**：Azure MCP 工具 + Azure CLI 回退 + 本地文件系统访问
**流程**：

1. 资源发现：

   - 执行 `azmcp-subscription-list` 查找可用订阅
   - 执行 `azmcp-group-list --subscription <subscription-id>` 查找资源组
   - 获取相关资源组内的所有资源列表：
     - 使用 `az resource list --subscription <id> --resource-group <name>`
   - 按资源类型优先使用 MCP 工具，其次 CLI 回退，例如：
     - `azmcp-cosmos-account-list --subscription <id>`：Cosmos DB 账户
     - `azmcp-storage-account-list --subscription <id>`：存储账户
     - `azmcp-monitor-workspace-list --subscription <id>`：Log Analytics 工作区
     - `azmcp-keyvault-key-list`：Key Vault
     - `az webapp list`：Web App（回退——无 MCP 工具）
     - `az appservice plan list`：App Service 计划（回退）
     - `az functionapp list`：Function App（回退）
     - `az sql server list`：SQL Server（回退）
     - `az redis list`：Redis（回退）
     - …其他资源类型依此类推

2. IaC 检测：

   - 使用 `file_search` 扫描 IaC 文件："**/\*.bicep"、"**/*.tf"、"**/main.json"、"**/*template\*.json"
   - 解析资源定义以理解期望配置
   - 与已发现资源对比以识别差异
   - 记录 IaC 文件的存在情况，以便后续实施建议
   - 不要使用仓库中的其他文件，仅限 IaC 文件。其他文件不被视为真实来源。
   - 如果未发现 IaC 文件，则停止并向用户报告“未找到 IaC 文件”。

3. 配置分析：
   - 提取每个资源的当前 SKU、层级与关键设置
   - 识别资源关系与依赖
   - 在可用范围内映射资源使用模式

### 步骤 3：收集使用指标并校验当前成本

**动作**：收集利用率数据并核验实际成本
**工具**：Azure MCP 监控工具 + Azure CLI
**流程**：

1. 定位监控源：

   - 使用 `azmcp-monitor-workspace-list --subscription <id>` 查找 Log Analytics 工作区
   - 使用 `azmcp-monitor-table-list --subscription <id> --workspace <name> --table-type "CustomLog"` 发现场景相关的数据

2. 执行使用分析查询：

   - 使用 `azmcp-monitor-log-query` 执行预定义查询：
     - Query: "recent"：最近活动模式
     - Query: "errors"：错误级日志以指示问题
   - 如需自定义分析，使用如下 KQL 查询：

   ```kql
   // App Service CPU 使用
   AppServiceAppLogs
   | where TimeGenerated > ago(7d)
   | summarize avg(CpuTime) by Resource, bin(TimeGenerated, 1h)

   // Cosmos DB RU 消耗
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.DOCUMENTDB"
   | where TimeGenerated > ago(7d)
   | summarize avg(RequestCharge) by Resource

   // 存储账户访问模式
   StorageBlobLogs
   | where TimeGenerated > ago(7d)
   | summarize RequestCount=count() by AccountName, bin(TimeGenerated, 1d)
   ```

3. 计算基线指标：

   - CPU/内存利用率均值
   - 数据库吞吐模式
   - 存储访问频率
   - 函数执行频次

4. 校验当前成本：
   - 使用第 2 步发现的 SKU/层级配置作为基础
   - 在 https://azure.microsoft.com/pricing/ 查询价格或使用 `az billing` 命令
   - 记录：资源 → 当前 SKU → 估算月度成本
   - 在提出建议前，先计算现实的当前月度总成本

### 步骤 4：生成成本优化建议

**动作**：基于资源分析识别优化机会
**工具**：基于已收集数据的本地分析
**流程**：

1. 按资源类型应用优化模式：

   计算优化：

   - App Service 计划：依据 CPU/内存使用做适配降配
   - Function App：低使用量从 Premium → Consumption 计划
   - 虚拟机：缩小过大规格实例

   数据库优化：

   - Cosmos DB：
     - Provisioned → Serverless 以适应波动负载
     - 根据实际使用调小 RU/s
   - SQL 数据库：依据 DTU 使用率降配服务层级

   存储优化：

   - 实施生命周期策略（Hot → Cool → Archive）
   - 合并冗余存储账户
   - 依据访问模式匹配存储层级

   基础设施优化：

   - 移除未使用/冗余资源
   - 在收益合适时启用自动伸缩
   - 为非生产环境设置定时关闭

2. 计算基于证据的节省：

   - 当前经校验的成本 → 目标成本 = 节省
   - 为当前与目标配置的定价来源提供引用

3. 为每条建议计算优先级分：

   ```
   Priority Score = (Value Score × Monthly Savings) / (Risk Score × Implementation Days)

   高优先级：Score > 20
   中优先级：Score 5–20
   低优先级：Score < 5
   ```

4. 校验建议：
   - 确认 Azure CLI 命令准确
   - 核对节省估算
   - 评估实施风险与前置条件
   - 确保所有节省计算均有证据支持

### 步骤 5：用户确认

**动作**：在创建 GitHub Issue 之前展示摘要并征求确认
**流程**：

1. 显示优化摘要：

   ```
   🎯 Azure 成本优化摘要

   📊 分析结果：
   • 已分析资源总数：X
   • 当前月度成本：$X
   • 潜在月度节省：$Y
   • 优化机会：Z
   • 高优先级项：N

   🏆 建议：
   1. [资源]：[当前 SKU] → [目标 SKU] = 每月节省 $X —— [风险等级] | [实施工作量]
   2. [资源]：[当前配置] → [目标配置] = 每月节省 $Y —— [风险等级] | [实施工作量]
   3. [资源]：[当前配置] → [目标配置] = 每月节省 $Z —— [风险等级] | [实施工作量]
   ... 以此类推

   💡 将创建：
   • Y 个独立 GitHub Issue（每个优化一条）
   • 1 个 EPIC Issue 用于统筹实施

   ❓是否继续创建 GitHub Issues？(y/n)
   ```

2. 等待用户确认：仅在用户确认后继续

### 步骤 6：创建独立优化 Issues

**动作**：为每个优化机会创建独立的 GitHub Issue。为其添加标签：“cost-optimization”（绿色）、“azure”（蓝色）。
**所需 MCP 工具**：对每条建议调用 `create_issue`
**流程**：

1. 使用如下模板创建独立 Issue：

   标题格式：`[COST-OPT] [资源类型] - [简要描述] - $X/月节省`

   正文模板：

   ````markdown
   ## 💰 成本优化：[简短标题]

   **月度节省**：$X | **风险等级**：[低/中/高] | **实施工作量**：X 天

   ### 📋 描述

   [对优化项的清晰解释及必要性]

   ### 🔧 实施

   **是否检测到 IaC 文件**：[是/否 —— 基于 file_search 结果]

   ```bash
   # 若存在 IaC：展示 IaC 修改 + 部署
   # 文件：infrastructure/bicep/modules/app-service.bicep
   # 变更：sku.name: 'S3' → 'B2'
   az deployment group create --resource-group [rg] --template-file infrastructure/bicep/main.bicep

   # 若不存在 IaC：使用直接 Azure CLI 并给出警告
   # ⚠️ 未找到 IaC 文件。若其存在于其他位置，请优先修改 IaC。
   az appservice plan update --name [plan] --sku B2
   ```
   ````

   ### 📈 证据

   - 当前配置：[详情]
   - 使用模式：[来自监控的数据证据]
   - 成本影响：$X/月 → $Y/月
   - 最佳实践对齐：[如适用则引用 Azure 最佳实践]

   ### ✅ 验证步骤

   - [ ] 在非生产环境验证
   - [ ] 确认无性能退化
   - [ ] 在 Azure 成本管理中确认成本下降
   - [ ] 必要时更新监控与告警

   ### ⚠️ 风险与注意事项

   - [风险 1 及缓解]
   - [风险 2 及缓解]

   **Priority Score**：X | **Value**：X/10 | **Risk**：X/10

   ```

   ```

### 步骤 7：创建 EPIC 统筹 Issue

**动作**：创建用于跟踪全部优化工作的主 Issue。为其添加标签：“cost-optimization”（绿色）、“azure”（蓝色）、“epic”（紫色）。
**所需 MCP 工具**：`create_issue`（EPIC）
**关于 mermaid 图**：务必校验 mermaid 语法正确，并在可访问性方面考虑样式与配色。
**流程**：

1. 创建 EPIC Issue：

   标题：`[EPIC] Azure 成本优化计划 - 潜在节省 $X/月`

   正文模板：

   ````markdown
   # 🎯 Azure 成本优化 EPIC

   **潜在总节省**：$X/月 | **实施周期**：X 周

   ## 📊 管理者摘要

   - **已分析资源数**：X
   - **优化机会**：Y
   - **潜在月度节省总额**：$X
   - **高优先级项**：N

   ## 🏗️ 当前架构概览

   ```mermaid
   graph TB
   	 subgraph "资源组：[name]"
   		  [Generated architecture diagram showing current resources and costs]
   	 end
   ```
   ````

   ## 📎 实施跟踪

   ### 🚀 高优先（优先实施）

   - [ ] #[issue-number]：[标题] - $X/月节省
   - [ ] #[issue-number]：[标题] - $X/月节省

   ### ⚡ 中优先

   - [ ] #[issue-number]：[标题] - $X/月节省
   - [ ] #[issue-number]：[标题] - $X/月节省

   ### 🔄 低优先（可择机）

   - [ ] #[issue-number]：[标题] - $X/月节省

   ## 📈 进度追踪

   - **已完成**：Y 个优化中的 0 个
   - **已实现节省**：$0 / $X/月
   - **实施状态**：未开始

   ## ✅ 成功标准

   - [ ] 完成全部高优先级优化
   - [ ] 实现 >80% 的预估节省
   - [ ] 无性能退化
   - [ ] 成本监控仪表盘已更新

   ## 📝 备注

   - 随着子 Issue 完成，更新该 EPIC
   - 关注实际节省与预估的偏差
   - 建议定期开展成本优化复盘

   ```

   ```

## 错误处理

- 成本校验：若节省估算缺乏证据或与 Azure 定价不一致，先重新核验配置与定价来源再推进
- Azure 身份验证失败：提供手动 Azure CLI 配置步骤
- 未发现资源：创建信息性 Issue 说明 Azure 资源部署情况
- GitHub 创建失败：将格式化的建议输出到控制台
- 使用数据不足：仅提供基于配置的建议并标注限制

## 成功标准

- ✅ 所有成本估算已与实际配置与 Azure 定价进行核验
- ✅ 为每条优化创建可跟踪、可分配的独立 Issue
- ✅ EPIC Issue 提供完善的统筹与跟踪
- ✅ 所有建议包含可直接执行的 Azure CLI 命令
- ✅ 以优先级评分引导 ROI 优先实施
- ✅ 架构图准确反映当前状态
- ✅ 用户确认后才会创建 Issues

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 本地化生成，因此可能包含错误。若发现不当或错误翻译，请创建一个[问题](../../issues)。
