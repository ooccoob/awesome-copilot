# 验证命令参考

本参考记录了用于 Azure 部署预检验证的所有命令。

## Azure 开发人员 CLI (azd)

### azd 规定--预览

无需部署即可预览 azd 项目的基础架构更改。

```bash
azd provision --preview [options]
```

**选项：**
|选项 |描述 |
|--------|-------------|
| __代码0__，__代码1__ |要使用的环境名称 |
| __代码0__ |接受默认值而不提示 |
| __代码0__ |启用调试日志记录 |
| __代码0__ |设置工作目录|

**示例：**

```bash
# Preview with default environment
azd provision --preview

# Preview specific environment
azd provision --preview --environment dev

# Preview without prompts (CI/CD)
azd provision --preview --no-prompt
```

**输出：** 显示将创建、修改或删除的资源。

### azd 身份验证登录

向 Azure 进行身份验证以执行 azd 操作。

```bash
azd auth login [options]
```

**选项：**
|选项 |描述 |
|--------|-------------|
| __代码0__ |无需登录即可查看登录状态 |
| __代码0__ |使用设备代码流程|
| __代码0__ |指定租户 |
| __代码0__ |服务主体客户端 ID |

### azd 环境列表

列出可用的环境。

```bash
azd env list
```

---

## Azure CLI (az)

### az 部署组假设

预览资源组部署的更改。

```bash
az deployment group what-if \
  --resource-group <rg-name> \
  --template-file <bicep-file> \
  [options]
```

**所需参数：**
|参数|描述 |
|-----------|-------------|
| __代码0__，__代码1__ |目标资源组名称 |
| __代码0__，__代码1__ |二头肌文件的路径 |

**可选参数：**
|参数|描述 |
|-----------|-------------|
| __代码0__，__代码1__ |参数文件或内联值 |
| __代码0__ | `Provider`（默认）、`ProviderNoRbac` 或 `Template` |
| __代码0__ | `FullResourcePayloads`（默认）或 `ResourceIdOnly` |
| __代码0__ |输出原始 JSON 用于解析 |
| __代码0__，__代码1__ |部署名称 |
| __代码0__ |从输出中排除特定的更改类型 |

**验证级别：**
|水平|描述 |使用案例|
|-------|-------------|----------|
| __代码0__ |通过 RBAC 检查进行全面验证 |默认，最彻底|
| __代码0__ |完全验证，仅限读取权限 |当缺乏部署权限时 |
| __代码0__ |仅静态语法验证 |快速语法检查 |

**示例：**

```bash
# Basic what-if
az deployment group what-if \
  --resource-group my-rg \
  --template-file main.bicep

# With parameters and full validation
az deployment group what-if \
  --resource-group my-rg \
  --template-file main.bicep \
  --parameters main.bicepparam \
  --validation-level Provider

# Fallback without RBAC checks
az deployment group what-if \
  --resource-group my-rg \
  --template-file main.bicep \
  --validation-level ProviderNoRbac

# JSON output for parsing
az deployment group what-if \
  --resource-group my-rg \
  --template-file main.bicep \
  --no-pretty-print
```

### az 部署子假设

预览订阅级别部署的更改。

```bash
az deployment sub what-if \
  --location <location> \
  --template-file <bicep-file> \
  [options]
```

**所需参数：**
|参数|描述 |
|-----------|-------------|
| __代码0__，__代码1__ |部署元数据的位置 |
| __代码0__，__代码1__ |二头肌文件的路径 |

**示例：**

```bash
az deployment sub what-if \
  --location eastus \
  --template-file main.bicep \
  --parameters main.bicepparam \
  --validation-level Provider
```

### az 部署 mg 假设

预览管理组部署的更改。

```bash
az deployment mg what-if \
  --location <location> \
  --management-group-id <mg-id> \
  --template-file <bicep-file> \
  [options]
```

**所需参数：**
|参数|描述 |
|-----------|-------------|
| __代码0__，__代码1__ |部署元数据的位置 |
| __代码0__，__代码1__ |目标管理组 ID |
| __代码0__，__代码1__ |二头肌文件的路径 |

### az 部署租户假设

预览租户级部署的更改。

```bash
az deployment tenant what-if \
  --location <location> \
  --template-file <bicep-file> \
  [options]
```

**所需参数：**
|参数|描述 |
|-----------|-------------|
| __代码0__，__代码1__ |部署元数据的位置 |
| __代码0__，__代码1__ |二头肌文件的路径 |

### 登录

向 Azure CLI 进行身份验证。

```bash
az login [options]
```

**选项：**
|选项 |描述 |
|--------|-------------|
| __代码0__，__代码1__ |租户 ID 或域 |
| __代码0__ |使用设备代码流程|
| __代码0__ |以服务主体身份登录 |

### az 帐户显示

显示当前订阅上下文。

```bash
az account show
```

### az 组存在

检查资源组是否存在。

```bash
az group exists --name <rg-name>
```

---

## 二头肌 CLI

### 二头肌构建

将 Bicep 编译为 ARM JSON 并验证语法。

```bash
bicep build <bicep-file> [options]
```

**选项：**
|选项 |描述 |
|--------|-------------|
| __代码0__ |输出到 stdout 而不是文件 |
| __代码0__ |输出目录|
| __代码0__ |输出文件路径 |
| __代码0__ |跳过模块恢复 |

**示例：**

```bash
# Validate syntax (output to stdout, no file created)
bicep build main.bicep --stdout > /dev/null

# Build to specific directory
bicep build main.bicep --outdir ./build

# Validate multiple files
for f in *.bicep; do bicep build "$f" --stdout; done
```

**错误输出格式：**
```
/path/to/file.bicep(22,51) : Error BCP064: Found unexpected tokens in interpolated expression.
/path/to/file.bicep(22,51) : Error BCP004: The string at this location is not terminated.
```

格式：`<file>(<line>,<column>) : <severity> <code>: <message>`

### 二头肌——版本

检查 Bicep CLI 版本。

```bash
bicep --version
```

---

## 参数文件检测

### 二头肌参数 (.bicepparam)

现代二头肌参数文件（推荐）：

```bicep
using './main.bicep'

param location = 'eastus'
param environment = 'dev'
param tags = {
  environment: 'dev'
  project: 'myapp'
}
```

**检测模式：** `<template-name>.bicepparam`

### JSON 参数 (.parameters.json)

传统ARM参数文件：

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "location": { "value": "eastus" },
    "environment": { "value": "dev" }
  }
}
```

**检测模式：**
- __代码0__
- __代码0__
- __代码0__

### 在命令中使用参数

```bash
# Bicep parameters file
az deployment group what-if \
  --resource-group my-rg \
  --template-file main.bicep \
  --parameters main.bicepparam

# JSON parameters file
az deployment group what-if \
  --resource-group my-rg \
  --template-file main.bicep \
  --parameters @parameters.json

# Inline parameter overrides
az deployment group what-if \
  --resource-group my-rg \
  --template-file main.bicep \
  --parameters main.bicepparam \
  --parameters location=westus
```

---

## 确定部署范围

检查 Bicep 文件的 `targetScope` 声明：

```bicep
// Resource Group (default if not specified)
targetScope = 'resourceGroup'

// Subscription
targetScope = 'subscription'

// Management Group
targetScope = 'managementGroup'

// Tenant
targetScope = 'tenant'
```

**范围到命令映射：**

|目标范围 |命令|所需参数 |
|-------------|---------|---------------------|
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__ |
| __代码0__ | __代码1__ | __代码2__，__代码3__ |
| __代码0__ | __代码1__ | __代码2__ |

---

## 版本要求

|工具|最低版本 |推荐版本 |主要特点|
|------|-----------------|---------------------|--------------|
| Azure CLI | 2.14.0 | 2.14.0 2.76.0+ | `--validation-level` 开关 |
| Azure 开发人员 CLI | 1.0.0 |最新 | `--preview` 标志 |
|二头肌 CLI | 0.4.0 |最新 |最佳错误消息 |

**检查版本：**
```bash
az --version
azd version
bicep --version
```
