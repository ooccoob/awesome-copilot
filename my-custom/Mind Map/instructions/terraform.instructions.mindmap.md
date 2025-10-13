# Terraform Conventions and Guidelines - Instructions Mindmap

## 📊 摘要
Terraform Conventions and Guidelines

本指令提供了关于Terraform Conventions and Guidelines的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.tf`
- **技术栈**: 见文档详情
- **场景**: 开发和维护Terraform Conventions and Guidelines相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Use Terraform to provision and manage infrastructure.
- Use version control for your Terraform configurations.
- Always use the latest stable version of Terraform and its providers.
- Store sensitive information in a secure manner, such as using AWS Secrets Manager or SSM Parameter Store.
- Use AWS environment variables to reference values stored in AWS Secrets Manager or SSM Parameter Store.
- Never commit sensitive information such as AWS credentials, API keys, passwords, certificates, or Terraform state to version control.
- Always mark sensitive variables as `sensitive = true` in your Terraform configurations.
- Use IAM roles and policies to control access to resources.

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
- Terraform Conventions and Guidelines
  - 适用范围
    - 文件类型: **/*.tf
  - 核心规则
    - General Instructions
    - Security
    - Modularity
    - Maintainability
    - Style and Formatting
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: terraform.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:58:00
- 文件类型: Instructions (编程规范/最佳实践)
