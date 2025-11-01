## What
- 基于给定场景，用 Playwright MCP 按步骤执行后再生成 TypeScript 测试文件并运行直至通过。

## When to use
- 已有清晰用户场景，希望沉淀为可维护的自动化测试并验证稳定性。

## Why it matters
- 避免“先写代码后调试”的反模式；以事实步骤驱动产生可靠的测试。

## How (关键流程)
- 若未提供场景则先询问 → 按工具逐步执行并记录 → 完成后生成 @playwright/test 代码 → 保存到 tests → 运行并迭代至通过

## Example questions (≥10)
1. 场景：用户登录后搜索商品并加入购物车，请按步骤执行并最终生成 TS 测试。
2. 生成的测试放在 tests/e2e/cart.spec.ts，并使用 test.use({ baseURL }) 配置。
3. 将动态等待封装为 helper，提高稳定性并复用。
4. 失败后自动截图与保存视频，并在报告中附链接。
5. 使用数据驱动写法，为不同用户/商品参数化。
6. 区分 setup 与 test 的职责（如登录前置）并使用 test.step 标注。
7. 在 CI 中运行的最小配置与并发建议是什么？
8. 如何断言网络响应状态与关键字段？
9. 生成可重跑的重试策略与超时配置。
10. 当定位器频繁变动，建议引入 testId 与选择器策略迁移方案。

## Key points
- CN: 步骤先行、稳健等待、证据留存、参数化、CI 运行
- EN: Step-first, robust waits, artifacts, parametrization, CI-ready

## Mind map (简要)
- 场景 → 执行记录 → 生成代码 → 保存运行 → 迭代通过

---
Source file: d:\mycode\awesome-copilot\prompts\playwright-generate-test.prompt.md
Generated: 2025-10-17T00:00:00Z
