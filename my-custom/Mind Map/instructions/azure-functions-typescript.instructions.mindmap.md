# TypeScript patterns for Azure Functions - Instructions Mindmap

## 📊 摘要
TypeScript patterns for Azure Functions

本指令提供了关于TypeScript patterns for Azure Functions的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.ts, **/*.js, **/*.json`
- **技术栈**: TypeScript, Azure
- **场景**: 开发和维护TypeScript patterns for Azure Functions相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Generate modern TypeScript code for Node.js
- Use `async/await` for asynchronous code
- Whenever possible, use Node.js v20 built-in modules instead of external packages
- Always use Node.js async functions, like `node:fs/promises` instead of `fs` to avoid blocking the event loop
- Ask before adding any extra dependencies to the project
- The API is built using Azure Functions using `@azure/functions@4` package.
- Each endpoint should have its own function file, and use the following naming convention: `src/functions/<resource-name>-<http-verb>.ts`
- When making changes to the API, make sure to update the OpenAPI schema (if it exists) and `README.md` file accordingly.

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
- TypeScript patterns for Azure Functions
  - 适用范围
    - 文件类型: **/*.ts, **/*.js, **/*.json
    - 技术栈: TypeScript, Azure
  - 核心规则
    - Guidance for Code Generation
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: azure-functions-typescript.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:52
- 文件类型: Instructions (编程规范/最佳实践)
