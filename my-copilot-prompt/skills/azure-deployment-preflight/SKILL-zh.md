---
名称：azure-部署-预检
描述：'对部署到 Azure 的 Bicep 执行全面的预检验证，包括模板语法验证、假设分析和权限检查。在部署到 Azure 之前使用此技能来预览更改、识别潜在问题并确保部署成功。当用户提及部署到 Azure、验证 Bicep 文件、检查部署权限、预览基础架构更改、运行假设或准备 azd 供应时激活。
---

# Azure 部署预检验证

此技能在执行前验证 Bicep 部署，支持 Azure CLI (`az`) 和 Azure Developer CLI (`azd`) 工作流。

## 何时使用此技能

- 将基础架构部署到 Azure 之前
- 准备或查看二头肌文件时
- 预览部署将进行的更改
- 验证权限是否足以进行部署
- 运行 `azd up`、`azd provision` 或 `az deployment` 命令之前

## 验证过程

按顺序执行以下步骤。即使上一步失败，也要继续下一步——在最终报告中捕获所有问题。

### 第 1 步：检测项目类型

通过检查项目指标来确定部署工作流程：

1. **检查 azd 项目**：在项目根目录中查找 `azure.yaml`
   - 如果找到 → 使用 **azd 工作流程**
   - 如果未找到 → 使用 **az CLI 工作流程**

2. **查找 Bicep 文件**：查找所有 `.bicep` 文件进行验证
   - 对于 azd 项目：首先检查 `infra/` 目录，然后检查项目根目录
   - 对于独立版：使用用户指定的文件或搜索公共位置（`infra/`、`deploy/`、项目根目录）

3. **自动检测参数文件**：对于每个 Bicep 文件，查找匹配的参数文件：
   - `<filename>.bicepparam` （二头肌参数 - 首选）
   - `<filename>.parameters.json`（JSON 参数）
   - `parameters.json` 或 `parameters/<env>.json` 在同一目录中

### 第 2 步：验证 Bicep 语法

在尝试部署验证之前运行 Bicep CLI 以检查模板语法：

```bash
bicep build <bicep-file> --stdout
```

**要捕捉什么：**
- 行号/列号的语法错误
- 警告信息
- 构建成功/失败状态

**如果未安装 Bicep CLI：**
- 请注意报告中的问题
- 继续执行步骤 3（Azure 将在假设过程中验证语法）

### 第 3 步：运行预检验证

根据步骤 1 中检测到的项目类型选择适当的验证。

#### 对于 azd 项目（azure.yaml 存在）

使用 `azd provision --preview` 验证部署：

```bash
azd provision --preview
```

如果指定了一个环境或者存在多个环境：
```bash
azd provision --preview --environment <env-name>
```

#### 对于独立二头肌（无 azure.yaml）

从 Bicep 文件的 `targetScope` 声明确定部署范围：

|目标范围|命令|
|--------------|---------|
| `resourceGroup`（默认）| __代码1__ |
| __代码0__ | __代码1__ |
| __代码0__ | __代码1__ |
| __代码0__ | __代码1__ |

**首先使用提供者验证级别运行：**

```bash
# Resource Group scope (most common)
az deployment group what-if \
  --resource-group <rg-name> \
  --template-file <bicep-file> \
  --parameters <param-file> \
  --validation-level Provider

# Subscription scope
az deployment sub what-if \
  --location <location> \
  --template-file <bicep-file> \
  --parameters <param-file> \
  --validation-level Provider

# Management Group scope
az deployment mg what-if \
  --location <location> \
  --management-group-id <mg-id> \
  --template-file <bicep-file> \
  --parameters <param-file> \
  --validation-level Provider

# Tenant scope
az deployment tenant what-if \
  --location <location> \
  --template-file <bicep-file> \
  --parameters <param-file> \
  --validation-level Provider
```

**后备策略：**

如果 `--validation-level Provider` 因权限错误 (RBAC) 失败，请使用 `ProviderNoRbac` 重试：

```bash
az deployment group what-if \
  --resource-group <rg-name> \
  --template-file <bicep-file> \
  --validation-level ProviderNoRbac
```

请注意报告中的后备方案 - 用户可能缺乏完整的部署权限。

### 第 4 步：捕获假设结果

解析假设输出以对资源更改进行分类：

|更改类型 |符号|意义|
|-------------|--------|---------|
|创建| __代码0__ |将创建新资源 |
|删除 | __代码0__ |资源将被删除 |
|修改| __代码0__ |资源属性将发生变化|
|没有改变| __代码0__ |资源不变|
|忽略| __代码0__ |资源未分析（达到限制）|
|部署 | __代码0__ |将部署资源（变化未知）|

对于已修改的资源，捕获特定的属性更改。

### 第5步：生成报告

在 **项目根目录** 中创建一个 Markdown 报告文件，名为：
- __代码0__

使用 [references/REPORT-TEMPLATE.md](references/REPORT-TEMPLATE-zh.md) 中的模板结构。

**报告部分：**
1. **摘要** - 总体状态、时间戳、已验证的文件、目标范围
2. **执行的工具** - 运行的命令、版本、使用的验证级别
3. **问题** - 所有错误和警告及其严重程度和补救措施
4. **假设结果** - 要创建/修改/删除/未更改的资源
5. **建议** - 可行的后续步骤

## 所需信息

在运行验证之前，收集：

|资讯|需要 |如何获取 |
|-------------|--------------|---------------|
|资源组| __代码0__ |询问用户或检查现有的 `.azure/` 配置 |
|订阅 |所有部署| `az account show` 或询问用户 |
|地点 |子/MG/租户范围 |询问用户或使用配置中的默认值 |
|环境 | azd项目| `azd env list` 或询问用户 |

如果缺少所需信息，请在继续之前提示用户。

## 错误处理

请参阅 [references/ERROR-HANDLING.md](references/ERROR-HANDLING-zh.md) 了解详细的错误处理指南。

**关键原则：** 即使发生错误也继续验证。在最终报告中记录所有问题。

|错误类型|行动|
|------------|--------|
|未登录 |报告中注明，建议使用 `az login` 或 `azd auth login` |
|权限被拒绝 |回退到 `ProviderNoRbac`，报告中的注释 |
|二头肌语法错误 |包含所有错误，继续其他文件 |
|工具未安装|请注意，在报告中，跳过该验证步骤 |
|找不到资源组 |报告中注释，建议创建它 |

## 工具要求

该技能使用以下工具：

- **Azure CLI** (`az`) - 建议 `--validation-level` 使用版本 2.76.0+
- **Azure 开发人员 CLI** (`azd`) - 适用于具有 `azure.yaml` 的项目
- **Bicep CLI** (`bicep`) - 用于语法验证
- **Azure MCP 工具** - 用于文档查找和最佳实践

开始前检查工具可用性：
```bash
az --version
azd version
bicep --version
```

## 示例工作流程

1. 用户：“在运行之前验证我的二头肌部署”
2. 代理检测到 `azure.yaml` → azd 项目
3. 代理找到 `infra/main.bicep` 和 `infra/main.bicepparam`
4. 代理运行 `bicep build infra/main.bicep --stdout`
5. 代理运行 `azd provision --preview`
6. 代理在项目根目录中生成 `preflight-report.md`
7. 代理向用户总结调查结果

## 参考文档

- [验证命令参考](references/VALIDATION-COMMANDS-zh.md)
- [报告模板](references/REPORT-TEMPLATE-zh.md)
- [错误处理指南](references/ERROR-HANDLING-zh.md)
