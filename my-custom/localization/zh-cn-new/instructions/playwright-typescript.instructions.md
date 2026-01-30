---
description: 'Playwright 测试生成指令'
applyTo: '**'
---

## 测试编写指南

### 代码质量标准
- **定位器**：优先使用面向用户的、基于角色的定位器（`getByRole`、`getByLabel`、`getByText` 等）以提高弹性和可访问性。使用 `test.step()` 对交互进行分组并提高测试可读性和报告。
- **断言**：使用自动重试的网页优先断言。这些断言以 `await` 关键字开始（例如：`await expect(locator).toHaveText()`）。除非专门测试可见性变化，否则避免使用 `expect(locator).toBeVisible()`。
- **超时**：依赖 Playwright 内置的自动等待机制。避免硬编码等待或增加默认超时时间。
- **清晰性**：使用清楚说明意图的描述性测试和步骤标题。仅添加注释来解释复杂逻辑或非显而易见的交互。


### 测试结构
- **导入**：以 `import { test, expect } from '@playwright/test';` 开始。
- **组织**：将功能的相关测试分组在 `test.describe()` 块下。
- **钩子**：使用 `beforeEach` 进行 `describe` 块中所有测试共有的设置操作（例如：导航到页面）。
- **标题**：遵循清晰的命名约定，如 `功能 - 特定操作或场景`。


### 文件组织
- **位置**：将所有测试文件存储在 `tests/` 目录中。
- **命名**：使用约定 `<feature-or-page>.spec.ts`（例如：`login.spec.ts`、`search.spec.ts`）。
- **范围**：每个主要应用程序功能或页面目标是一个测试文件。

### 断言最佳实践
- **UI 结构**：使用 `toMatchAriaSnapshot` 验证组件的可访问性树结构。这提供了全面且可访问的快照。
- **元素计数**：使用 `toHaveCount` 断言定位器找到的元素数量。
- **文本内容**：使用 `toHaveText` 进行精确文本匹配，使用 `toContainText` 进行部分匹配。
- **导航**：使用 `toHaveURL` 验证操作后的页面 URL。


## 示例测试结构

```typescript
import { test, expect } from '@playwright/test';

test.describe('电影搜索功能', () => {
  test.beforeEach(async ({ page }) => {
    // 在每个测试之前导航到应用程序
    await page.goto('https://debs-obrien.github.io/playwright-movies-app');
  });

  test('按标题搜索电影', async ({ page }) => {
    await test.step('激活并执行搜索', async () => {
      await page.getByRole('search').click();
      const searchInput = page.getByRole('textbox', { name: 'Search Input' });
      await searchInput.fill('Garfield');
      await searchInput.press('Enter');
    });

    await test.step('验证搜索结果', async () => {
      // 验证搜索结果的可访问性树
      await expect(page.getByRole('main')).toMatchAriaSnapshot(`
        - main:
          - heading "Garfield" [level=1]
          - heading "search results" [level=2]
          - list "movies":
            - listitem "movie":
              - link "poster of The Garfield Movie The Garfield Movie rating":
                - /url: /playwright-movies-app/movie?id=tt5779228&page=1
                - img "poster of The Garfield Movie"
                - heading "The Garfield Movie" [level=2]
      `);
    });
  });
});
```

## 测试执行策略

1. **初始运行**：使用 `npx playwright test --project=chromium` 执行测试
2. **调试失败**：分析测试失败并识别根本原因
3. **迭代**：根据需要优化定位器、断言或测试逻辑
4. **验证**：确保测试持续通过并覆盖预期功能
5. **报告**：提供关于测试结果和发现的任何问题的反馈

## 质量检查清单

在最终确定测试之前，确保：
- [ ] 所有定位器都是可访问且具体的，避免严格模式违规
- [ ] 测试逻辑分组并遵循清晰结构
- [ ] 断言是有意义的并反映用户期望
- [ ] 测试遵循一致的命名约定
- [ ] 代码格式正确并有注释