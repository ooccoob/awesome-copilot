# Instructions for developing Power Platform custom connectors with Model Context Protocol (MCP) integration for Microsoft Copilot Studio - Instructions Mindmap

## 📊 摘要
Instructions for developing Power Platform custom connectors with Model Context Protocol (MCP) integration for Microsoft Copilot Studio

本指令提供了关于Instructions for developing Power Platform custom connectors with Model Context Protocol (MCP) integration for Microsoft Copilot Studio的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.{json,csx,md}`
- **技术栈**: 见文档详情
- **场景**: 开发和维护Instructions for developing Power Platform custom connectors with Model Context Protocol (MCP) integration for Microsoft Copilot Studio相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Always implement JSON-RPC 2.0 standard for MCP communication
- Use `x-ms-agentic-protocol: mcp-streamable-1.0` header for Copilot Studio compatibility
- Structure endpoints to support both standard REST operations and MCP tool invocation
- Transform responses to comply with Copilot Studio constraints (no reference types, single types only)
- Remove `$ref` and other reference types from JSON schemas as Copilot Studio cannot handle them
- Use single types instead of arrays of types in schema definitions
- Flatten `anyOf`/`oneOf` constructs to single schemas for Copilot Studio compatibility
- Ensure all tool input schemas are self-contained without external references

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
- Instructions for developing Power Platform custom connectors with Model Context Protocol (MCP) integration for Microsoft Copilot Studio
  - 适用范围
    - 文件类型: **/*.{json,csx,md}
  - 核心规则
    - Instructions
    - Additional Guidelines
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: power-platform-mcp-development.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:58
- 文件类型: Instructions (编程规范/最佳实践)
