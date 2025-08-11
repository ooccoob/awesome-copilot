
我将保存该翻译内容到---
description: "使用 Azure Verified Modules (AVM) 创建、更新或评审 Terraform 语言的 Azure 基础设施即代码（IaC）。"
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp", "azure_get_deployment_best_practices", "azure_get_schema_for_Bicep"]
---

# Azure AVM Terraform 模式

使用 Terraform 的 Azure Verified Modules，通过预构建模块强制执行 Azure 最佳实践。

## 模块发现

- Terraform Registry：搜索 "avm" + 资源，按 Partner 标签筛选。
- AVM 索引：`https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-resource-modules/`

## 用法

- **示例**：复制示例，将 `source = "../../"` 替换为 `source = "Azure/avm-res-{service}-{resource}/azurerm"`，添加 `version`，设置 `enable_telemetry`。
- **自定义**：复制 Provision Instructions，设置输入，锁定 `version`。

## 版本管理

- 端点：`https://registry.terraform.io/v1/modules/Azure/{module}/azurerm/versions`

## 源码

- Registry：`https://registry.terraform.io/modules/Azure/{module}/azurerm/latest`
- GitHub：`https://github.com/Azure/terraform-azurerm-avm-res-{service}-{resource}`

## 命名规范

- 资源：Azure/avm-res-{service}-{resource}/azurerm
- 模式：Azure/avm-ptn-{pattern}/azurerm
- 工具：Azure/avm-utl-{utility}/azurerm

## 最佳实践

- 锁定模块和提供者版本
- 从官方示例开始
- 审查输入和输出
- 启用遥测
- 使用 AVM 工具模块
- 遵循 AzureRM 提供者要求
- 修改后始终运行 `terraform fmt` 和 `terraform validate`
- 使用 `azure_get_deployment_best_practices` 工具获取部署建议
- 使用 `microsoft.docs.mcp` 工具查找 Azure 服务的具体指导

## GitHub Copilot Agents 的自定义指令

**重要**：当 GitHub Copilot Agent 或 GitHub Copilot Coding Agent 在此仓库工作时，必须执行以下本地单元测试以符合 PR 检查要求。未运行这些测试将导致 PR 校验失败：

```bash
./avm pre-commit
./avm tflint
./avm pr-check
```

在创建或更新任何拉取请求之前，必须运行这些命令，以确保符合 Azure Verified Modules 标准并防止 CI/CD 流水线失败。
更多 AVM 流程详情请参见 [Azure Verified Modules 贡献文档](https://azure.github.io/Azure-Verified-Modules/contributing/terraform/testing/)。

---

**免责声明**：本文档由[GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot)本地化。因此，可能包含错误。如果您发现任何不适当的翻译或错误，请创建一个[议题](../../issues)。
