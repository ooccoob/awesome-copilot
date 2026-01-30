---
description: 'Azure验证模块（AVM）和Terraform'
applyTo: '**/*.terraform, **/*.tf, **/*.tfvars, **/*.tfstate, **/*.tflint.hcl, **/*.tf.json, **/*.tfvars.json'
---

# Azure验证模块（AVM）Terraform

## 概述

Azure验证模块（AVM）是预构建、测试和验证的Terraform和Bicep模块，遵循Azure最佳实践。使用这些模块自信地创建、更新或审查Azure基础设施即代码（IaC）。

## GitHub Copilot代理的自定义指令

**重要**：当GitHub Copilot代理或GitHub Copilot编码代理在此仓库上工作时，必须执行以下本地单元测试以符合PR检查。未能运行这些测试将导致PR验证失败：

```bash
./avm pre-commit
./avm tflint
./avm pr-check
```

这些命令必须在创建或更新任何拉取请求之前运行，以确保符合Azure验证模块标准并防止CI/CD管道失败。
有关AVM流程的更多详细信息可在[Azure验证模块贡献文档](https://azure.github.io/Azure-Verified-Modules/contributing/terraform/testing/)中找到。

**未能运行这些测试将导致PR验证失败并阻止成功合并。**

## 模块发现

### Terraform注册表

- 搜索"avm" + 资源名称
- 按"合作伙伴"标签筛选以查找官方AVM模块
- 示例：搜索"avm storage account" → 按合作伙伴筛选

### 官方AVM索引

- **Terraform资源**：`https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-resource-modules/`
- **Terraform模式**：`https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-pattern-modules/`
- **Bicep资源**：`https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-resource-modules/`
- **Bicep模式**：`https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-pattern-modules/`

## Terraform模块使用

### 从示例

1. 从模块文档复制示例代码
2. 将`source = "../../"`替换为`source = "Azure/avm-res-{service}-{resource}/azurerm"`
3. 添加`version = "~> 1.0"`（使用最新可用版本）
4. 设置`enable_telemetry = true`

### 从头开始

1. 从模块文档复制配置说明
2. 配置必需和可选输入
3. 固定模块版本
4. 启用遥测

### 使用示例

```hcl
module "storage_account" {
  source  = "Azure/avm-res-storage-storageaccount/azurerm"
  version = "~> 0.1"

  enable_telemetry    = true
  location            = "East US"
  name                = "mystorageaccount"
  resource_group_name = "my-rg"

  # 附加配置...
}
```

## 命名约定

### 模块类型

- **资源模块**：`Azure/avm-res-{service}-{resource}/azurerm`
  - 示例：`Azure/avm-res-storage-storageaccount/azurerm`
- **模式模块**：`Azure/avm-ptn-{pattern}/azurerm`
  - 示例：`Azure/avm-ptn-aks-enterprise/azurerm`
- **实用工具模块**：`Azure/avm-utl-{utility}/azurerm`
  - 示例：`Azure/avm-utl-regions/azurerm`

### 服务命名

- 对服务和资源使用kebab-case
- 遵循Azure服务名称（例如`storage-storageaccount`、`network-virtualnetwork`）

## 版本管理

### 检查可用版本

- 端点：`https://registry.terraform.io/v1/modules/Azure/{module}/azurerm/versions`
- 示例：`https://registry.terraform.io/v1/modules/Azure/avm-res-storage-storageaccount/azurerm/versions`

### 版本固定最佳实践

- 使用悲观版本约束：`version = "~> 1.0"`
- 为生产环境固定到特定版本：`version = "1.2.3"`
- 升级前始终审查变更日志

## 模块源

### Terraform注册表

- **URL模式**：`https://registry.terraform.io/modules/Azure/{module}/azurerm/latest`
- **示例**：`https://registry.terraform.io/modules/Azure/avm-res-storage-storageaccount/azurerm/latest`

### GitHub仓库

- **URL模式**：`https://github.com/Azure/terraform-azurerm-avm-{type}-{service}-{resource}`
- **示例**：
  - 资源：`https://github.com/Azure/terraform-azurerm-avm-res-storage-storageaccount`
  - 模式：`https://github.com/Azure/terraform-azurerm-avm-ptn-aks-enterprise`

## 开发最佳实践

### 模块使用

- ✅ **始终**固定模块和提供程序版本
- ✅ **从**模块文档的官方示例开始
- ✅ **实施前**审查所有输入和输出
- ✅ **启用**遥测：`enable_telemetry = true`
- ✅ **使用**AVM实用工具模块处理常见模式
- ✅ **遵循**AzureRM提供程序要求和约束

### 代码质量

- ✅ **进行更改后**始终运行`terraform fmt`
- ✅ **进行更改后**始终运行`terraform validate`
- ✅ **使用**有意义的变量名和描述
- ✅ **添加**适当的标签和元数据
- ✅ **记录**复杂配置

### 验证要求

在创建或更新任何拉取请求之前：

```bash
# 格式化代码
terraform fmt -recursive

# 验证语法
terraform validate

# AVM特定验证（必需）
./avm pre-commit
./avm tflint
./avm pr-check
```

## 工具集成

### 使用可用工具

- **部署指导**：使用`azure_get_deployment_best_practices`工具
- **服务文档**：使用`microsoft.docs.mcp`工具获取Azure服务特定指导
- **模式信息**：使用`azure_get_schema_for_Bicep`获取Bicep资源

### GitHub Copilot集成

使用AVM仓库时：

1. 在创建新资源之前始终检查现有模块
2. 使用官方示例作为起点
3. 提交前运行所有验证测试
4. 记录任何自定义或与示例的偏差

## 常见模式

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

## 故障排除

### 常见问题

1. **版本冲突**：始终检查模块和提供程序版本之间的兼容性
2. **缺少依赖关系**：确保首先创建所有必需的资源
3. **验证失败**：提交前运行AVM验证工具
4. **文档**：始终参考最新的模块文档

### 支持资源

- **AVM文档**：`https://azure.github.io/Azure-Verified-Modules/`
- **GitHub问题**：在特定模块的GitHub仓库中报告问题
- **社区**：Azure Terraform提供程序GitHub讨论

## 合规性清单

在提交任何AVM相关代码之前：

- [ ] 模块版本已固定
- [ ] 遥测已启用
- [ ] 代码已格式化（`terraform fmt`）
- [ ] 代码已验证（`terraform validate`）
- [ ] AVM预提交检查通过（`./avm pre-commit`）
- [ ] TFLint检查通过（`./avm tflint`）
- [ ] AVM PR检查通过（`./avm pr-check`）
- [ ] 文档已更新
- [ ] 示例已测试并正常工作