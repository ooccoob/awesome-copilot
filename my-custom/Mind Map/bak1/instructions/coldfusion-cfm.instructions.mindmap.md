# ColdFusion cfm files and application patterns - Instructions Mindmap

## 📊 摘要
ColdFusion cfm files and application patterns

本指令提供了关于ColdFusion cfm files and application patterns的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.cfm`
- **技术栈**: 见文档详情
- **场景**: 开发和维护ColdFusion cfm files and application patterns相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Use CFScript where possible for cleaner syntax.
- Avoid using deprecated tags and functions.
- Follow consistent naming conventions for variables and components.
- Use `cfqueryparam` to prevent SQL injection.
- Escape CSS hash symbols inside <cfoutput> blocks using ##
- When using HTMX inside <cfoutput> blocks, escape hash symbols (#) by using double hashes (##) to prevent unintended variable interpolation.
- If you are in a HTMX target file then make sure the top line is: <cfsetting showDebugOutput = "false">
- Use `Application.cfc` for application settings and request handling.

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
- ColdFusion cfm files and application patterns
  - 适用范围
    - 文件类型: **/*.cfm
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: coldfusion-cfm.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:53
- 文件类型: Instructions (编程规范/最佳实践)
