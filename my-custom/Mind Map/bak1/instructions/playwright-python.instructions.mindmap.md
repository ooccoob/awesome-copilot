# Playwright Python AI test generation instructions based on official documentation. - Instructions Mindmap

## 📊 摘要
Playwright Python AI test generation instructions based on official documentation.

本指令提供了关于Playwright Python AI test generation instructions based on official documentation.的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**`
- **技术栈**: Python
- **场景**: 开发和维护Playwright Python AI test generation instructions based on official documentation.相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Locators**: Prioritize user-facing, role-based locators (get_by_role, get_by_label, get_by_text) for resilience and accessibility.
- Timeouts**: Rely on Playwright's built-in auto-waiting mechanisms. Avoid hard-coded waits or increased default timeouts.
- Imports**: Every test file should begin with from playwright.sync_api import Page, expect.
- Fixtures**: Use the page: Page fixture as an argument in your test functions to interact with the browser page.
- Setup**: Place navigation steps like page.goto() at the beginning of each test function. For setup actions shared across multiple tests, use standard 
- Location**: Store test files in a dedicated tests/ directory or follow the existing project structure.
- Naming**: Test files must follow the test_<feature-or-page>.py naming convention to be discovered by Pytest.
- Scope**: Aim for one test file per major application feature or page.

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
- Playwright Python AI test generation instructions based on official documentation.
  - 适用范围
    - 文件类型: **
    - 技术栈: Python
  - 核心规则
    - Test Writing Guidelines
    - Assertion Best Practices
    - Example
    - Test Execution Strategy
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: playwright-python.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:58
- 文件类型: Instructions (编程规范/最佳实践)
