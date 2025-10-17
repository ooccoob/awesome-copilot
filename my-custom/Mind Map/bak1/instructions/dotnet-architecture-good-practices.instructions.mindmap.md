# DDD and .NET architecture guidelines - Instructions Mindmap

## 📊 摘要
DDD and .NET architecture guidelines

本指令提供了关于DDD and .NET architecture guidelines的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.cs,**/*.csproj,**/Program.cs,**/*.razor`
- **技术栈**: C#, .NET
- **场景**: 开发和维护DDD and .NET architecture guidelines相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Ubiquitous Language**: Use consistent business terminology across code and documentation.
- Bounded Contexts**: Clear service boundaries with well-defined responsibilities.
- Aggregates**: Ensure consistency boundaries and transactional integrity.
- Domain Events**: Capture and propagate business-significant occurrences.
- Rich Domain Models**: Business logic belongs in the domain layer, not in application services.
- Single Responsibility Principle (SRP)**: A class should have only one reason to change.
- Open/Closed Principle (OCP)**: Software entities should be open for extension but closed for modification.
- Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types.

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
- DDD and .NET architecture guidelines
  - 适用范围
    - 文件类型: **/*.cs,**/*.csproj,**/Program.cs,**/*.razor
    - 技术栈: C#, .NET
  - 核心规则
    - MANDATORY THINKING PROCESS
    - Core Principles
    - DDD & .NET Standards
    - Implementation Guidelines
    - Testing Guidelines
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: dotnet-architecture-good-practices.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:54
- 文件类型: Instructions (编程规范/最佳实践)
