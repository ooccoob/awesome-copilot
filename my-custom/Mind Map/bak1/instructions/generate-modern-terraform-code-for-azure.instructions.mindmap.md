# Guidelines for generating modern Terraform code for Azure - Instructions Mindmap

## 📊 摘要
Guidelines for generating modern Terraform code for Azure

本指令提供了关于Guidelines for generating modern Terraform code for Azure的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.tf`
- **技术栈**: Azure
- **场景**: 开发和维护Guidelines for generating modern Terraform code for Azure相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Use `main.tf` for resources
- Use `variables.tf` for inputs
- Use `outputs.tf` for outputs
- Follow consistent naming conventions and formatting (`terraform fmt`)
- Create a module with its own variables/outputs
- Reference it rather than duplicating code
- This promotes reuse and consistency
- Parameterize** all configurable values using variables with types and descriptions

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
- Guidelines for generating modern Terraform code for Azure
  - 适用范围
    - 文件类型: **/*.tf
    - 技术栈: Azure
  - 核心规则
    - 1. Use Latest Terraform and Providers
    - 2. Organize Code Cleanly
    - 3. Encapsulate in Modules
    - 4. Leverage Variables and Outputs
    - 5. Provider Selection (AzureRM vs AzAPI)
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: generate-modern-terraform-code-for-azure.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:55
- 文件类型: Instructions (编程规范/最佳实践)
