---
applyTo: "playwright-typescript.instructions.md"
---

<!-- 本文件为自动翻译，供参考。请结合实际需求进行校对和完善。-->

# Playwright TypeScript 测试编写指南

## 代码质量标准

- **定位器**：优先使用用户可见、基于角色的定位器（如 `getByRole`、`getByLabel`、`getByText` 等），提升测试的健壮性和可访问性。用 `test.step()` 分组交互，提升可读性和报告质量。
- **断言**：使用自动重试的 web-first 断言（如 `await expect(locator).toHaveText()`）。除非专门测试可见性变化，否则避免 `expect(locator).toBeVisible()`。
- **超时**：依赖 Playwright 内置自动等待机制，避免硬编码等待或调整默认超时。
- **清晰性**：测试和步骤标题应清晰表达意图。仅对复杂逻辑或非显而易见的交互添加注释。

## 测试结构

- **导入**：统一使用 `import { test, expect } from '@playwright/test';`。
- **组织**：相关测试用 `test.describe()` 分组。
- **钩子**：用 `beforeEach` 做通用前置操作（如页面跳转）。
- **命名**：测试和步骤命名规范，表达具体场景。

## 文件组织

- **位置**：所有测试文件放在 `tests/` 目录。
- **命名**：采用 `<feature-or-page>.spec.ts`（如 `login.spec.ts`）。
- **范围**：每个主要功能或页面一个测试文件。

## 断言最佳实践

- **结构**：用 `toMatchAriaSnapshot` 验证组件可访问性树。
- **元素数量**：用 `toHaveCount` 断言元素数量。
- **文本内容**：用 `toHaveText` 精确匹配，用 `toContainText` 部分匹配。
- **导航**：用 `toHaveURL` 验证跳转。

## 测试执行策略

1. **初次运行**：用 `npx playwright test --project=chromium` 执行全部测试。
2. **调试失败**：分析失败原因并修正。
3. **迭代**：优化定位器、断言或逻辑。
4. **验证**：确保测试稳定通过。
5. **报告**：输出测试结果和发现的问题。

## 质量检查清单

- [ ] 定位器可访问且具体，避免 strict mode 违规
- [ ] 测试分组合理、结构清晰
- [ ] 断言有意义且符合用户预期
- [ ] 命名规范统一
- [ ] 代码格式规范，注释适当

---

免责声明：本翻译仅供参考，具体实践请结合实际项目需求和最新官方文档。
