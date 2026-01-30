# Guidelines for building Java base applications - Instructions Mindmap

## 📊 摘要
Guidelines for building Java base applications

本指令提供了关于Guidelines for building Java base applications的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.java`
- **技术栈**: Java
- **场景**: 开发和维护Guidelines for building Java base applications相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- First, prompt the user if they want to integrate static analysis tools (SonarQube, PMD, Checkstyle)
- If the user declines static analysis tools or wants to proceed without them, continue with implementing the Best practices, bug patterns and code smel
- Address code smells proactively during development rather than accumulating technical debt.
- Focus on readability, maintainability, and performance when refactoring identified issues.
- Use IDE / Code editor reported warnings and suggestions to catch common patterns early in development.
- Records**: For classes primarily intended to store data (e.g., DTOs, immutable data structures), **Java Records should be used instead of traditional 
- Pattern Matching**: Utilize pattern matching for `instanceof` and `switch` expression to simplify conditional logic and type casting.
- Type Inference**: Use `var` for local variable declarations to improve readability, but only when the type is explicitly clear from the right-hand sid

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
- Guidelines for building Java base applications
  - 适用范围
    - 文件类型: **/*.java
    - 技术栈: Java
  - 核心规则
    - General Instructions
    - Best practices
    - Code Smells
    - Build and Verification
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: java.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:56
- 文件类型: Instructions (编程规范/最佳实践)
