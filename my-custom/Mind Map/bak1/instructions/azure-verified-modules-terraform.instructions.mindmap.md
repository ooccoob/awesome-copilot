#  Azure Verified Modules (AVM) and Terraform - Instructions Mindmap

## 📊 摘要
 Azure Verified Modules (AVM) and Terraform

本指令提供了关于 Azure Verified Modules (AVM) and Terraform的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.terraform, **/*.tf, **/*.tfvars, **/*.tfstate, **/*.tflint.hcl, **/*.tf.json, **/*.tfvars.json`
- **技术栈**: Azure
- **场景**: 开发和维护 Azure Verified Modules (AVM) and Terraform相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Search for "avm" + resource name
- Filter by "Partner" tag to find official AVM modules
- Example: Search "avm storage account" → filter by Partner
- Terraform Resources**: `https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-resource-modules/`
- Terraform Patterns**: `https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-pattern-modules/`
- Bicep Resources**: `https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-resource-modules/`
- Bicep Patterns**: `https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-pattern-modules/`
- Resource Modules**: `Azure/avm-res-{service}-{resource}/azurerm`

### 代码质量标准
- 遵循行业标准编码规范
- 保持代码简洁可读
- 添加适当的注释和文档
- 进行充分的测试覆盖

## 📝 关键技术要点

### 项目配置
- 正确设置开发环境
- 配置必要的工具和依赖
- 遵循项目结构规范

### 实现标准
- 使用推荐的设计模式
- 遵循命名规范
- 注意性能和安全考虑

## 🗺️ 思维导图

```mindmap
-  Azure Verified Modules (AVM) and Terraform
  - 适用范围
    - 文件类型: **/*.terraform, **/*.tf, **/*.tfvars, **/*.tfstate, **/*.tflint.hcl, **/*.tf.json, **/*.tfvars.json
    - 技术栈: Azure
  - 核心规则
    - Overview
    - Custom Instructions for GitHub Copilot Agents
    - Module Discovery
    - Terraform Module Usage
    - Naming Conventions
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: azure-verified-modules-terraform.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:52
- 文件类型: Instructions (编程规范/最佳实践)
