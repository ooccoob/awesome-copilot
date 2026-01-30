---
description: '使用Azure验证模块（AVM）创建、更新或审查Azure IaC Terraform。'
tools: ['changes', 'codebase', 'edit/editFiles', 'extensions', 'fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI', 'microsoft.docs.mcp', 'azure_get_deployment_best_practices', 'azure_get_schema_for_Bicep']
---

# Azure AVM Terraform模式

使用Azure验证模块进行Terraform开发，通过预构建模块强制执行Azure最佳实践。

## 发现模块

- Terraform注册表：搜索"avm" + 资源，按合作伙伴标签过滤。
- AVM索引：`https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-resource-modules/`

## 使用方法

- **示例**：复制示例，将`source = "../..//"`替换为`source = "Azure/avm-res-{service}-{resource}/azurerm"`，添加`version`，设置`enable_telemetry`。
- **自定义**：复制配置说明，设置输入，固定`version`。

## 版本控制

- 端点：`https://registry.terraform.io/v1/modules/Azure/{module}/azurerm/versions`

## 来源

- 注册表：`https://registry.terraform.io/modules/Azure/{module}/azurerm/latest`
- GitHub：`https://github.com/Azure/terraform-azurerm-avm-res-{service}-{resource}`

## 命名约定

- 资源：Azure/avm-res-{service}-{resource}/azurerm
- 模式：Azure/avm-ptn-{pattern}/azurerm
- 实用程序：Azure/avm-utl-{utility}/azurerm

## 最佳实践

- 固定模块和提供商版本
- 从官方示例开始
- 审查输入和输出
- 启用遥测
- 使用AVM实用程序模块
- 遵循AzureRM提供商要求
- 进行更改后总是运行`terraform fmt`和`terraform validate`
- 使用`azure_get_deployment_best_practices`工具获取部署指导
- 使用`microsoft.docs.mcp`工具查找Azure服务特定指导

## GitHub Copilot代理的自定义指令

**重要**：当GitHub Copilot代理或GitHub Copilot编码代理在此存储库上工作时，必须执行以下本地单元测试以符合PR检查。未能运行这些测试将导致PR验证失败：

```bash
./avm pre-commit
./avm tflint
./avm pr-check
```

这些命令必须在创建或更新任何拉取请求之前运行，以确保符合Azure验证模块标准并防止CI/CD管道失败。
有关AVM流程的更多详细信息可以在[Azure验证模块贡献文档](https://azure.github.io/Azure-Verified-Modules/contributing/terraform/testing/)中找到。