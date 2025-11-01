# Playwright test generation instructions - Instructions Mindmap

## 📊 摘要
Playwright test generation instructions

本指令提供了关于Playwright test generation instructions的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**`
- **技术栈**: TypeScript
- **场景**: 开发和维护Playwright test generation instructions相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Timeouts**: Rely on Playwright's built-in auto-waiting mechanisms. Avoid hard-coded waits or increased default timeouts.
- Clarity**: Use descriptive test and step titles that clearly state the intent. Add comments only to explain complex logic or non-obvious interactions.
- Imports**: Start with `import { test, expect } from '@playwright/test';`.
- Organization**: Group related tests for a feature under a `test.describe()` block.
- Hooks**: Use `beforeEach` for setup actions common to all tests in a `describe` block (e.g., navigating to a page).
- Titles**: Follow a clear naming convention, such as `Feature - Specific action or scenario`.
- Location**: Store all test files in the `tests/` directory.
- Naming**: Use the convention `<feature-or-page>.spec.ts` (e.g., `login.spec.ts`, `search.spec.ts`).

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
- Playwright test generation instructions
  - 适用范围
    - 文件类型: **
    - 技术栈: TypeScript
  - 核心规则
    - Test Writing Guidelines
    - Example Test Structure
    - Test Execution Strategy
    - Quality Checklist
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: playwright-typescript.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:58
- 文件类型: Instructions (编程规范/最佳实践)
