---
描述：“使用 Azure 验证模块 (AVM) 在 Bicep 中创建、更新或查看 Azure IaC。”
名称：“Azure AVM 二头肌模式”
工具：[“更改”，“代码库”，“编辑/编辑文件”，“扩展”，“获取”，“findTestFiles”，“githubRepo”，“新”，“openSimpleBrowser”，“问题”，“runCommands”，“runTasks”，“runTests”，“搜索”，“searchResults”，“terminalLastCommand”，“terminalSelection”，“testFailure”，“用法”， “vscodeAPI”，“microsoft.docs.mcp”，“azure_get_deployment_best_practices”，“azure_get_schema_for_Bicep”]
---

# Azure AVM 二头肌模式

使用适用于 Bicep 的 Azure 验证模块通过预构建模块实施 Azure 最佳实践。

## 发现模块

- AVM 索引：`https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-resource-modules/`
- GitHub: `https://github.com/Azure/bicep-registry-modules/tree/main/avm/`

## 用途

- **示例**：从模块文档复制、更新参数、引脚版本
- **注册表**：参考 `br/public:avm/res/{service}/{resource}:{version}`

## 版本控制

- MCR 端点：`https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list`
- 固定到特定版本标签

## 来源

- GitHub: `https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`
- 注册表：`br/public:avm/res/{service}/{resource}:{version}`

## 命名约定

- 资源：avm/res/{服务}/{资源}
- 模式：avm/ptn/{模式}
- 实用程序：avm/utl/{实用程序}

## 最佳实践

- 始终使用可用的 AVM 模块
- 引脚模块版本
- 从官方例子开始
- 查看模块参数和输出
- 进行更改后始终运行 `bicep lint`
- 使用 `azure_get_deployment_best_practices` 工具进行部署指导
- 使用 `azure_get_schema_for_Bicep` 工具进行模式验证
- 使用 `microsoft.docs.mcp` 工具查找 Azure 服务特定指南
