---
description: 'Azure Verified Modules (AVM) and Bicep'
applyTo: '**/*.bicep, **/*.bicepparam'
---

# Azure 验证模块 (AVM) 二头肌

## 概述

Azure 验证模块 (AVM) 是预先构建、测试和验证的 Bicep 模块，遵循 Azure 最佳实践。使用这些模块可以自信地创建、更新或查看 Azure 基础结构即代码 (IaC)。

## 模块发现

### 二头肌公共登记处

- 搜索模块：`br/public:avm/res/{service}/{resource}:{version}`
- 浏览可用模块：`https://github.com/Azure/bicep-registry-modules/tree/main/avm/res`
- 示例：`br/public:avm/res/storage/storage-account:0.30.0`

### 官方 AVM 指数

- **二头肌资源模块**：`https://raw.githubusercontent.com/Azure/Azure-Verified-Modules/refs/heads/main/docs/static/module-indexes/BicepResourceModules.csv`
- **二头肌模式模块**：`https://raw.githubusercontent.com/Azure/Azure-Verified-Modules/refs/heads/main/docs/static/module-indexes/BicepPatternModules.csv`

### 模块文档

- **GitHub 存储库**：`https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`
- **自述文件**：每个模块都包含带有示例的综合文档

## 模块使用

### 来自示例

1. 查看 `https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}` 中的模块自述文件
2. 从模块文档复制示例代码
3. 使用 `br/public:avm/res/{service}/{resource}:{version}` 的参考模块
4. 配置必需和可选参数

### 用法示例

```bicep
module storageAccount 'br/public:avm/res/storage/storage-account:0.30.0' = {
  name: 'storage-account-deployment'
  scope: resourceGroup()
  params: {
    name: storageAccountName
    location: location
    skuName: 'Standard_LRS'
    tags: tags
  }
}
```

### 当 AVM 模块不可用时

如果资源类型不存在 AVM 模块，请使用具有最新稳定 API 版本的本机 Bicep 资源声明。

## 命名约定

### 模块参考

- **资源模块**：`br/public:avm/res/{service}/{resource}:{version}`
- **模式模块**：`br/public:avm/ptn/{pattern}:{version}`
- 示例：`br/public:avm/res/network/virtual-network:0.7.2`

### 符号名称

- 所有名称（变量、参数、资源、模块）均使用小驼峰命名法
- 使用资源类型描述性名称（例如 `storageAccount` 而不是 `storageAccountName`）
- 避免在符号名称中使用“名称”后缀，因为它们代表资源，而不是资源的名称
- 避免通过后缀区分变量和参数

## 版本管理

### 版本固定最佳实践

- 始终固定到特定模块版本：`:{version}`
- 使用语义版本控制（例如 `:0.30.0`）
- 升级前查看模块变更日志
- 先在非生产环境测试版本升级

## 开发最佳实践

### 模块发现和使用

- ✅ **始终**在创建原始资源之前检查现有的 AVM 模块
- ✅ **在实施之前查看**模块文档和示例
- ✅ **明确固定**模块版本
- ✅ **使用**模块中可用的类型（从模块导入类型）
- ✅ **优先** AVM 模块而不是原始资源声明

### 代码结构

- ✅ **使用 `@sys.description()` 装饰器在文件顶部声明**参数
- ✅ **指定** `@minLength()` 和 `@maxLength()` 来命名参数
- ✅ **谨慎使用** `@allowed()` 装饰器以避免阻止有效部署
- ✅ **设置**对于测试环境安全的默认值（低成本 SKU）
- ✅ **使用**变量进行复杂表达式，而不是嵌入资源属性中
- ✅ **利用** `loadJsonContent()` 作为外部配置文件

### 资源参考

- ✅ **使用**符号名称作为引用（例如 `storageAccount.id`）而不是 `reference()` 或 `resourceId()`
- ✅ **通过符号名称创建**依赖项，而不是显式的 `dependsOn`
- ✅ **使用** `existing` 关键字从其他资源访问属性
- ✅ 通过点表示法**访问**模块输出（例如，`storageAccount.outputs.resourceId`）

### 资源命名

- ✅ **使用** `uniqueString()` 以及有意义的前缀来获得唯一名称
- ✅ **添加**前缀，因为某些资源不允许名称以数字开头
- ✅ **尊重**特定于资源的命名约束（长度、字符）

### 儿童资源

- ✅ **避免**子资源的过度嵌套
- ✅ **使用** `parent` 属性或嵌套而不是手动构造名称

### 安全性

- ❌ **永远不要** 在输出中包含秘密或密钥
- ✅ **直接在输出中使用**资源属性（例如，`storageAccount.outputs.primaryBlobEndpoint`）
- ✅ **尽可能启用**托管身份
- ✅ 启用网络隔离时**禁用**公共访问

### 类型

- ✅ **从模块导入**类型（如果可用）：`import { deploymentType } from './module.bicep'`
- ✅ **使用**用户定义的类型来处理复杂的参数结构
- ✅ **利用**变量的类型推断

### 文档

- ✅ **包含**对复杂逻辑有帮助的 `//` 注释
- ✅ **对所有参数使用** `@sys.description()` 并提供清晰的解释
- ✅ **记录**非显而易见的设计决策

## 验证要求

### 构建验证（强制）

对 Bicep 文件进行任何更改后，运行以下命令以确保所有文件成功构建：

```shell
# Ensure Bicep CLI is up to date
az bicep upgrade

# Build and validate changed Bicep files
az bicep build --file main.bicep
```

### 二头肌参数文件

- ✅ 修改 `*.bicep` 文件时，**始终**更新随附的 `*.bicepparam` 文件
- ✅ **验证**参数文件与当前参数定义匹配
- ✅ 在提交之前使用参数文件**测试**部署

## 工具集成

### 使用可用的工具

- **架构信息**：使用 `azure_get_schema_for_Bicep` 作为资源架构
- **部署指南**：使用 `azure_get_deployment_best_practices` 工具
- **服务文档**：使用 `microsoft.docs.mcp` 获取特定于 Azure 服务的指南

### GitHub Copilot 集成

使用二头肌时：

1. 创建资源之前检查现有 AVM 模块
2. 使用官方模块示例作为起点
3. 所有更改后运行 `az bicep build`
4. 更新随附的 `.bicepparam` 文件
5. 记录自定义或与示例的偏差

## 故障排除

### 常见问题

1. **模块版本**：始终在模块参考中指定准确的版本
2. **缺少依赖项**：确保在依赖模块之前创建资源
3. **验证失败**：运行 `az bicep build` 来识别语法/类型错误
4. **参数文件**：确保参数更改时更新 `.bicepparam` 文件

### 支持资源

- **AVM 文档**：`https://azure.github.io/Azure-Verified-Modules/`
- **二头肌注册表**：`https://github.com/Azure/bicep-registry-modules`
- **二头肌文档**：`https://learn.microsoft.com/azure/azure-resource-manager/bicep/`
- **最佳实践**：`https://learn.microsoft.com/azure/azure-resource-manager/bicep/best-practices`

## 合规检查表

在提交任何二头肌代码之前：

- [ ] 在可用的情况下使用 AVM 模块
- [ ] 模块版本已固定
- [ ] 代码构建成功 (`az bicep build`)
- [ ] 更新了随附的 `.bicepparam` 文件
- [ ] `@sys.description()` 所有参数
- [ ] 用于引用的符号名称
- [ ] 输出中没有秘密
- [ ] 在适当的情况下导入/定义的类型
- [ ] 为复杂逻辑添加注释
- [ ] 遵循小驼峰命名约定
