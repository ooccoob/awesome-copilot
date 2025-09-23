---
description: "Azure Verified Modules (AVM) 与 Terraform"
applyTo: "**/*.terraform, **/*.tf, **/*.tfvars, **/*.tfstate, **/*.tflint.hcl, **/*.tf.json, **/*.tfvars.json"
---

# Azure Verified Modules (AVM) Terraform

## 概述

Azure Verified Modules（AVM）是预构建、测试和验证的 Terraform 与 Bicep 模块，遵循 Azure 最佳实践。使用这些模块可自信地创建、更新或评审 Azure 基础设施即代码（IaC）。

## GitHub Copilot Agent 专用指引

**重要：** Copilot Agent 或 Coding Agent 在本仓库工作时，必须执行以下本地单元测试以通过 PR 校验，否则会导致 PR 校验失败：

```bash
./avm pre-commit
./avm tflint
./avm pr-check
```

这些命令必须在创建或更新 PR 前运行，以确保符合 AVM 标准，避免 CI/CD 流水线失败。详情见 [Azure Verified Modules 贡献文档](https://azure.github.io/Azure-Verified-Modules/contributing/terraform/testing/)。

**未运行上述测试将导致 PR 校验失败，无法合并。**

## 模块发现

### Terraform Registry

- 搜索 "avm" + 资源名
- 用 "Partner" 标签筛选官方 AVM 模块
- 示例：搜索 "avm storage account" → 筛选 Partner

### 官方 AVM 索引

- **Terraform 资源**：`https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-resource-modules/`
- **Terraform 模式**：`https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-pattern-modules/`
- **Bicep 资源**：`https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-resource-modules/`
- **Bicep 模式**：`https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-pattern-modules/`

## Terraform 模块用法

### 示例用法

1. 从模块文档复制示例代码
2. 将 `source = "../../"` 替换为 `source = "Azure/avm-res-{service}-{resource}/azurerm"`
3. 添加 `version = "~> 1.0"`（用最新可用版本）
4. 设置 `enable_telemetry = true`

### 从零开始

1. 复制模块文档中的 Provision Instructions
2. 配置必需与可选输入
3. 固定模块版本
4. 启用 telemetry

### 用法示例

```hcl
module "storage_account" {
  source  = "Azure/avm-res-storage-storageaccount/azurerm"
  version = "~> 0.1"

  enable_telemetry    = true
  location            = "East US"
  name                = "mystorageaccount"
  resource_group_name = "my-rg"
  # 其他配置...
}
```

## 命名规范

### 模块类型

- **资源模块**：`Azure/avm-res-{service}-{resource}/azurerm`
  - 示例：`Azure/avm-res-storage-storageaccount/azurerm`
- **模式模块**：`Azure/avm-ptn-{pattern}/azurerm`
  - 示例：`Azure/avm-ptn-aks-enterprise/azurerm`
- **工具模块**：`Azure/avm-utl-{utility}/azurerm`
  - 示例：`Azure/avm-utl-regions/azurerm`

### 服务命名

- 服务与资源用 kebab-case
- 遵循 Azure 服务命名（如 `storage-storageaccount`, `network-virtualnetwork`）

## 版本管理

### 查询可用版本

- 接口：`https://registry.terraform.io/v1/modules/Azure/{module}/azurerm/versions`
- 示例：`https://registry.terraform.io/v1/modules/Azure/avm-res-storage-storageaccount/azurerm/versions`

### 版本锁定最佳实践

- 用悲观约束：`version = "~> 1.0"`
- 生产环境锁定具体版本：`version = "1.2.3"`
- 升级前务必查阅 changelog

## 模块来源

### Terraform Registry

- **URL 模式**：`https://registry.terraform.io/modules/Azure/{module}/azurerm/latest`
- **示例**：`https://registry.terraform.io/modules/Azure/avm-res-storage-storageaccount/azurerm/latest`

### GitHub 仓库

- **URL 模式**：`https://github.com/Azure/terraform-azurerm-avm-{type}-{service}-{resource}`
- **示例**：
  - 资源：`https://github.com/Azure/terraform-azurerm-avm-res-storage-storageaccount`
  - 模式：`https://github.com/Azure/terraform-azurerm-avm-ptn-aks-enterprise`

## 开发最佳实践

### 模块用法

- **务必**锁定模块与 provider 版本
- **从官方示例开始**
- **实现前审查所有输入输出**
- **启用 telemetry：`enable_telemetry = true`**
- **用 AVM 工具模块实现通用模式**
- **遵循 AzureRM provider 要求**

### 代码质量

- **每次更改后运行 `terraform fmt`**
- **每次更改后运行 `terraform validate`**
- **变量命名有意义并加注释**
- **添加合适标签与元数据**
- **复杂配置需文档说明**

### 校验要求

PR 前务必：

```bash
terraform fmt -recursive
terraform validate
./avm pre-commit
./avm tflint
./avm pr-check
```

## 工具集成

### 可用工具

- **部署建议**：用 `azure_get_deployment_best_practices` 工具
- **服务文档**：用 `microsoft.docs.mcp` 获取 Azure 服务指引
- **Schema 信息**：用 `azure_get_schema_for_Bicep` 获取 Bicep 资源 schema

### Copilot 集成

1. 创建新资源前务必检查现有模块
2. 以官方示例为起点
3. 提交前运行所有校验
4. 文档化所有自定义或偏离示例的实现

## 常用模式

### 资源组模块

```hcl
module "resource_group" {
  source  = "Azure/avm-res-resources-resourcegroup/azurerm"
  version = "~> 0.1"
  enable_telemetry = true
  location         = var.location
  name            = var.resource_group_name
}
```

### 虚拟网络模块

```hcl
module "virtual_network" {
  source  = "Azure/avm-res-network-virtualnetwork/azurerm"
  version = "~> 0.1"
  enable_telemetry    = true
  location            = module.resource_group.location
  name                = var.vnet_name
  resource_group_name = module.resource_group.name
  address_space       = ["10.0.0.0/16"]
}
```

## 故障排查

### 常见问题

1. **版本冲突**：务必检查模块与 provider 兼容性
2. **依赖缺失**：确保所有依赖资源已创建
3. **校验失败**：提交前运行 AVM 校验工具
4. **文档问题**：始终参考最新模块文档

### 支持资源

- **AVM 文档**：`https://azure.github.io/Azure-Verified-Modules/`
- **GitHub Issues**：在具体模块仓库提 issue
- **社区**：Azure Terraform Provider GitHub 讨论区

## 合规清单

PR 前请确认：

- [ ] 模块版本已锁定
- [ ] 已启用 telemetry
- [ ] 代码已格式化（`terraform fmt`）
- [ ] 代码已校验（`terraform validate`）
- [ ] AVM pre-commit 校验通过（`./avm pre-commit`）
- [ ] TFLint 校验通过（`./avm tflint`）
- [ ] AVM PR 校验通过（`./avm pr-check`）
- [ ] 文档已更新
- [ ] 示例已测试可用

---

**免责声明**：本文档由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 本地化。如有错误或不当之处，欢迎通过 [issues](../../issues) 反馈。
