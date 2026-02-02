---
name: azure-resource-visualizer
description: Analyze Azure resource groups and generate detailed Mermaid architecture diagrams showing the relationships between individual resources. Use this skill when the user asks for a diagram of their Azure resources or help in understanding how the resources relate to each other.
license: Complete terms in LICENSE.txt
metadata:
  author: Tom Meschter (tom.meschter@microsoft.com)
---

# Azure 资源可视化工具 - 架构图生成器

用户可能会寻求帮助来理解各个资源如何组合在一起，或者创建一个图表来显示它们的关系。您的任务是检查 Azure 资源组，了解它们的结构和关系，并生成清晰说明架构的全面美人鱼图。

## 核心职责

1. **资源组发现**：未指定时列出可用的资源组
2. **深度资源分析**：检查所有资源、其配置和相互依赖关系
3. **关系映射**：识别并记录资源之间的所有连接
4. **图表生成**：创建详细、准确的美人鱼图
5. **文档创建**：生成带有嵌入图表的清晰 Markdown 文件

## 工作流程

### 步骤1：资源组选择

如果用户未指定资源组：

1. 使用您的工具查询可用的资源组。如果您没有可用的工具，请使用 `az`。
2. 显示资源组的编号列表及其位置
3. 要求用户按编号或名称选择一个
4. 等待用户响应后再继续

如果指定了资源组，请验证其存在并继续。

### 第 2 步：资源发现与分析

拥有资源组后：

1. **使用 Azure MCP 工具或 `az` 查询资源组中的所有资源**。
2. **分析每个资源**类型并捕获：
   - 资源名称和类型
   - SKU/等级信息
   - 地点/地区
   - 关键配置属性
   - 网络设置（VNet、子网、专用终结点）
   - 身份和访问（托管身份、RBAC）
   - 依赖关系和连接

3. **通过识别来映射关系**：
   - **网络连接**：VNet 对等、子网分配、NSG 规则、专用终结点
   - **数据流**：应用程序 → 数据库、功能 → 存储、API 管理 → 后端
   - **身份**：连接到资源的托管身份
   - **配置**：指向 Key Vault 的应用程序设置、连接字符串
   - **依赖关系**：父子关系，所需资源

### 第三步：构建图表

使用 `graph TB` （从上到下）或 `graph LR` （从左到右）格式创建 **详细的美人鱼图**：

**图表结构指南：**

```mermaid
graph TB
    %% Use subgraphs to group related resources
    subgraph "Resource Group: [name]"
        subgraph "Network Layer"
            VNET[Virtual Network<br/>10.0.0.0/16]
            SUBNET1[Subnet: web<br/>10.0.1.0/24]
            SUBNET2[Subnet: data<br/>10.0.2.0/24]
            NSG[Network Security Group]
        end
        
        subgraph "Compute Layer"
            APP[App Service<br/>Plan: P1v2]
            FUNC[Function App<br/>Runtime: .NET 8]
        end
        
        subgraph "Data Layer"
            SQL[Azure SQL Database<br/>DTU: S1]
            STORAGE[Storage Account<br/>Type: Standard LRS]
        end
        
        subgraph "Security & Identity"
            KV[Key Vault]
            MI[Managed Identity]
        end
    end
    
    %% Define relationships with descriptive labels
    APP -->|"HTTPS requests"| FUNC
    FUNC -->|"SQL connection"| SQL
    FUNC -->|"Blob/Queue access"| STORAGE
    APP -->|"Uses identity"| MI
    MI -->|"Access secrets"| KV
    VNET --> SUBNET1
    VNET --> SUBNET2
    SUBNET1 --> APP
    SUBNET2 --> SQL
    NSG -->|"Rules applied to"| SUBNET1
```

**关键图要求：**

- **按层或目的分组**：网络、计算、数据、安全、监控
- **包含详细信息**：SKU、层级、节点标签中的重要设置（使用 `<br/>` 进行换行）
- **标记所有连接**：描述资源之间的流动（数据、身份、网络）
- **使用有意义的节点 ID**：有意义的缩写（APP、FUNC、SQL、KV）
- **视觉层次结构**：逻辑分组的子图
- **连接类型**：
  - `-->` 用于数据流或依赖关系
  - `-.->` 用于可选/条件连接
  - `==>` 用于关键/主要路径

**资源类型示例：**
- 应用服务：包括计划层（B1、S1、P1v2）
- 功能：包括运行时（.NET、Python、Node）
- 数据库：包括层（基本、标准、高级）
- 存储：包括冗余（LRS、GRS、ZRS）
- VNet：包括地址空间
- 子网：包括地址范围

### 第 4 步：创建文件

使用 [template-architecture.md](./assets/template-architecture-zh.md) 作为模板并创建一个名为 `[resource-group-name]-architecture.md` 的 Markdown 文件，其中包含：

1. **标头**：资源组名称、订阅、区域
2. **摘要**：架构的简要概述（2-3 段）
3. **资源清单**：列出所有资源及其类型和关键属性的表格
4. **架构图**：完整的美人鱼图
5. **关系详情**：关键连接和数据流的说明
6. **注释**：任何重要的观察结果、潜在问题或建议

## 操作指南

### 质量标准

- **准确性**：在包含在图表中之前验证所有资源详细信息
- **完整性**：不遗漏资源；包括资源组中的所有内容
- **清晰度**：使用清晰的描述性标签和逻辑分组
- **详细级别**：包括对架构理解很重要的配置详细信息
- **关系**：显示所有重要的联系，而不仅仅是明显的联系

### 工具使用模式

1. **Azure MCP 搜索**： 
   - 使用 `intent="list resource groups"` 发现资源组
   - 使用 `intent="list resources in group"` 和组名来获取所有资源
   - 使用 `intent="get resource details"` 进行单个资源分析
   - 当您需要特定的 Azure 操作时，请使用 `command` 参数

2. **文件创建**：
   - 始终在工作区根目录或 `docs/` 文件夹（如果存在）中创建
   - 使用清晰的描述性文件名：`[rg-name]-architecture.md`
   - 确保 Mermaid 语法有效（输出前在心里测试语法）

3. **终端（需要时）**：
   - 使用 Azure CLI 进行 MCP 无法提供的复杂查询
   - 示例：`az resource list --resource-group <name> --output json`
   - 示例：`az network vnet show --resource-group <name> --name <vnet-name>`

### 约束和边界

**始终这样做：**
- ✅ 如果未指定则列出资源组
- ✅ 等待用户选择后再继续
- ✅ 分析群组中的所有资源
- ✅ 创建详细、准确的图表
- ✅ 在节点标签中包含配置详细信息
- ✅ 使用子图对资源进行逻辑分组
- ✅ 对所有连接进行描述性标记
- ✅ 创建带有图表的完整 Markdown 文件

**永远不要这样做：**
- ❌ 跳过资源，因为它们看起来不重要
- ❌ 在没有验证的情况下对资源关系做出假设
- ❌ 创建不完整或占位图
- ❌ 省略影响架构的配置细节
- ❌ 不确认资源组选择而继续
- ❌ 生成无效的 Mermaid 语法
- ❌ 修改或删除Azure资源（只读分析）

### 边缘情况和错误处理

- **未找到资源**：通知用户并验证资源组名称
- **权限问题**：解释缺少什么并建议检查 RBAC
- **复杂架构（50+资源）**：考虑按层创建多个图表
- **跨资源组依赖关系**：在图表注释中注意外部依赖关系
- **没有明确关系的资源**：“其他资源”部分中的分组

## 输出格式规范

### 美人鱼图语法
- 使用 `graph TB` （从上到下）进行垂直布局
- 使用 `graph LR` （从左到右）进行水平布局（更适合宽架构）
- 子图语法：`subgraph "Descriptive Name"`
- 节点语法：`ID["Display Name<br/>Details"]`
- 连接语法：`SOURCE -->|"Label"| TARGET`

### 降价结构
- 使用 H1 作为主标题
- 主要部分使用 H2
- 使用 H3 作为小节
- 使用表格进行资源清单
- 使用项目符号列表作为注释和建议
- 对图表使用带有 `mermaid` 语言标记的代码块

## 交互示例

**用户**：“分析我的生产资源组”

**代理**：
1. 列出订阅中的所有资源组
2. 要求用户选择：“哪个资源组？1) rg-prod-app, 2) rg-dev-app, 3) rg-shared”
3. 用户选择：“1”
4. 查询rg-prod-app中所有资源
5. 分析：应用服务、函数应用、SQL 数据库、存储帐户、Key Vault、VNet、NSG
6. 识别关系：应用程序 → 功能、功能 → SQL、功能 → 存储、全部 → Key Vault
7. 创建带有子图的详细美人鱼图
8. 生成带有完整文档的 `rg-prod-app-architecture.md`
9. 显示：“在 rg-prod-app-architecture.md 中创建了架构图。找到了具有 8 个关键关系的 7 个资源。”

## 成功标准

成功的分析包括：
- ✅ 已识别有效的资源组
- ✅ 发现和分析的所有资源
- ✅ 映射所有重要关系
- ✅ 详细的美人鱼图和适当的分组
- ✅ 创建完整的 Markdown 文件
- ✅ 清晰、可操作的文档
- ✅ 正确渲染的有效 Mermaid 语法
- ✅ 专业、架构师级别的输出

您的目标是提供对 Azure 架构的清晰度和洞察力，通过出色的可视化使复杂的资源关系易于理解。
