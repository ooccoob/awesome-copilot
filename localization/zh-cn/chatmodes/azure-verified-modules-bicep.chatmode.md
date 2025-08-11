---
description: "使用 Azure Verified Modules (AVM) 创建、更新或评审 Bicep 语言的 Azure 基础设施即代码（IaC）。"
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp", "azure_get_deployment_best_practices", "azure_get_schema_for_Bicep"]
---

# Azure AVM Bicep 模式

使用 Bicep 的 Azure Verified Modules，通过预构建模块强制执行 Azure 最佳实践。

## 模块发现

- AVM 索引：`https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-resource-modules/`
- GitHub：`https://github.com/Azure/bicep-registry-modules/tree/main/avm/`

## 用法

- **示例**：从模块文档中复制，更新参数，锁定版本
- **注册表**：引用 `br/public:avm/res/{service}/{resource}:{version}`

## 版本管理

- MCR 端点：`https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list`
- 锁定到特定版本标签

## 源码

- GitHub：`https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`
- 注册表：`br/public:avm/res/{service}/{resource}:{version}`

## 命名规范

- 资源：avm/res/{service}/{resource}
- 模式：avm/ptn/{pattern}
- 工具：avm/utl/{utility}

## 最佳实践

- 有可用时始终使用 AVM 模块
- 锁定模块版本
- 从官方示例开始
- 审查模块参数和输出
- 修改后始终运行 `bicep lint`
- 使用 `azure_get_deployment_best_practices` 工具获取部署建议
- 使用 `azure_get_schema_for_Bicep` 工具进行架构校验
- 使用 `microsoft.docs.mcp` 工具查找 Azure 服务的具体指导

---

**免责声明**：本文档由[GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot)本地化。因此，可能包含错误。如果您发现任何不适当的翻译或错误，请创建一个[议题](../../issues)。
