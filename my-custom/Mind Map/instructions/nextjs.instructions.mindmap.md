# Nextjs - Instructions Mindmap

## 📊 摘要
Nextjs的开发指南和最佳实践

本指令提供了关于Nextjs的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**`
- **技术栈**: TypeScript, React
- **场景**: 开发和维护Nextjs相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Use the `app/` directory** (App Router) for all new projects. Prefer it over the legacy `pages/` directory.
- Top-level folders:
- Colocation:** Place files (components, styles, tests) near where they are used, but avoid deeply nested structures.
- Route Groups:** Use parentheses (e.g., `(admin)`) to group routes without affecting the URL path.
- Private Folders:** Prefix with `_` (e.g., `_internal`) to opt out of routing and signal implementation details.
- Feature Folders:** For large apps, group by feature (e.g., `app/dashboard/`, `app/auth/`).
- Use `src/`** (optional): Place all source code in `src/` to separate from config files.
- If you need to use a Client Component (e.g., a component that uses hooks, browser APIs, or client-only libraries) inside a Server Component, you must:

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
- Nextjs
  - 适用范围
    - 文件类型: **
    - 技术栈: TypeScript, React
  - 核心规则
    - 1. Project Structure & Organization
    - 2.1. Server and Client Component Integration (App Router)
    - 2. Component Best Practices
    - 3. Naming Conventions (General)
    - 4. API Routes (Route Handlers)
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: nextjs.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:57
- 文件类型: Instructions (编程规范/最佳实践)
