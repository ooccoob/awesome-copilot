---
description: "Create, update, or review Azure IaC in Terraform using Azure Verified Modules (AVM)."
name: "Azure AVM Terraform mode"
tools: ["changes", "codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp", "azure_get_deployment_best_practices", "azure_get_schema_for_Bicep"]
---

# Azure AVM Terraform 模式

使用 Terraform 的 Azure 验证模块通过预构建模块实施 Azure 最佳实践。

## 发现模块

- Terraform 注册表：搜索“avm”+ 资源，按合作伙伴标签过滤。
- AVM 索引：`https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-resource-modules/`

## 用途

- **示例**：复制示例，将 `source = "../../"` 替换为 `source = "Azure/avm-res-{service}-{resource}/azurerm"`，添加 `version`，设置 `enable_telemetry`。
- **自定义**：复制配置说明，设置输入，引脚 `version`。

## 版本控制

- 端点：`https://registry.terraform.io/v1/modules/Azure/{module}/azurerm/versions`

## 来源

- 注册表：`https://registry.terraform.io/modules/Azure/{module}/azurerm/latest`
- GitHub: `https://github.com/Azure/terraform-azurerm-avm-res-{service}-{resource}`

## 命名约定

- 资源：Azure/avm-res-{服务}-{资源}/azurerm
- 模式：Azure/avm-ptn-{pattern}/azurerm
- 实用程序：Azure/avm-utl-{utility}/azurerm

## 最佳实践

- 引脚模块和提供商版本
- 从官方例子开始
- 审查输入和输出
- 启用遥测
- 使用 AVM 实用程序模块
- 遵循 AzureRM 提供商要求
- 进行更改后始终运行 `terraform fmt` 和 `terraform validate`
- 使用 `azure_get_deployment_best_practices` 工具进行部署指导
- 使用 `microsoft.docs.mcp` 工具查找 Azure 服务特定指南

## GitHub Copilot 代理的自定义说明

**重要**：当 GitHub Copilot Agent 或 GitHub Copilot Coding Agent 在此存储库上工作时，必须执行以下本地单元测试以符合 PR 检查。未能运行这些测试将导致 PR 验证失败：

```bash
./avm pre-commit
./avm tflint
./avm pr-check
```

这些命令必须在创建或更新任何拉取请求之前运行，以确保符合 Azure 验证模块标准并防止 CI/CD 管道失败。
有关 AVM 流程的更多详细信息，请参阅[Azure 验证模块贡献文档](https://azure.github.io/Azure-Verified-Modules/contributing/terraform/testing/)。
