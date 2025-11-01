---
description: '使用Azure验证模块（AVM）创建、更新或审查Azure IaC Bicep。'
tools: ['changes', 'codebase', 'edit/editFiles', 'extensions', 'fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI', 'microsoft.docs.mcp', 'azure_get_deployment_best_practices', 'azure_get_schema_for_Bicep']
---
# Azure AVM Bicep模式

使用Azure验证模块进行Bicep开发，通过预构建模块强制执行Azure最佳实践。

## 发现模块

- AVM索引：`https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-resource-modules/`
- GitHub：`https://github.com/Azure/bicep-registry-modules/tree/main/avm/`

## 使用方法

- **示例**：从模块文档复制，更新参数，固定版本
- **注册表**：引用`br/public:avm/res/{service}/{resource}:{version}`

## 版本控制

- MCR端点：`https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list`
- 固定到特定版本标签

## 来源

- GitHub：`https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`
- 注册表：`br/public:avm/res/{service}/{resource}:{version}`

## 命名约定

- 资源：avm/res/{service}/{resource}
- 模式：avm/ptn/{pattern}
- 实用程序：avm/utl/{utility}

## 最佳实践

- 在可用时总是使用AVM模块
- 固定模块版本
- 从官方示例开始
- 审查模块参数和输出
- 进行更改后总是运行`bicep lint`
- 使用`azure_get_deployment_best_practices`工具获取部署指导
- 使用`azure_get_schema_for_Bicep`工具进行模式验证
- 使用`microsoft.docs.mcp`工具查找Azure服务特定指导