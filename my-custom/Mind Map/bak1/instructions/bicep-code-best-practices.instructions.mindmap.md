# Infrastructure as Code with Bicep - Instructions Mindmap

## 📊 摘要
Infrastructure as Code with Bicep

本指令提供了关于Infrastructure as Code with Bicep的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.bicep`
- **技术栈**: 见文档详情
- **场景**: 开发和维护Infrastructure as Code with Bicep相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- When writing Bicep code, use lowerCamelCase for all names (variables, parameters, resources)
- Use resource type descriptive symbolic names (e.g., 'storageAccount' not 'storageAccountName')
- Avoid using 'name' in a symbolic name as it represents the resource, not the resource's name
- Avoid distinguishing variables and parameters by the use of suffixes
- Always declare parameters at the top of files with @description decorators
- Use latest stable API versions for all resources
- Use descriptive @description decorators for all parameters
- Specify minimum and maximum character length for naming parameters

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
- Infrastructure as Code with Bicep
  - 适用范围
    - 文件类型: **/*.bicep
  - 核心规则
    - Naming Conventions
    - Structure and Declaration
    - Parameters
    - Variables
    - Resource References
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: bicep-code-best-practices.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:52
- 文件类型: Instructions (编程规范/最佳实践)
