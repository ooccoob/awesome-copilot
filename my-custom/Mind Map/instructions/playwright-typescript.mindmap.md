## What/When/Why/How
- What: Playwright TypeScript 端到端测试实践速览与落地清单
- When: 新建测试体系、治理 flaky、高质量回归与并行加速
- Why: 更稳、更快、更可读、可观测、可维护
- How: 角色定位器 + web-first 断言 + 语义化步骤 + 并行与重试 + CI 报告

## Key Points
- 入口：import { test, expect } from '@playwright/test'
- 结构：tests/*.spec.ts；test.describe 分组；beforeEach 导航/登录
- 定位：getByRole/getByLabel/getByText 优先；减少 nth 依赖；test.step 包装
- 断言：await expect(locator).toHaveText/URL/Count 等，少用仅可见断言
- 等待：避免硬等待；利用 auto-wait；仅在必要时局部延长 timeout
- 复用：Page Object/Helper 封装多步；数据工厂与种子；幂等前置
- 观测：trace/screenshot/video/console/network 失败保留；HTML 报告
- CI：--project 多浏览器；并行/重试/仅重跑失败；分片执行；快照基线

## Compact Map
- Config: baseURL, retries, use: { trace, video, screenshot }
- Steps: test.step("行为") 包裹关键交互，提升报告可读性
- Locators: by role/label/text、has/hasText 组合提升稳健性
- Snapshots: toHaveScreenshot/ARIA snapshots 校验结构而非像素
- Patterns: 数据驱动、幂等化、隔离状态、idempotent 清理
- Perf: 并行度、网络拦截、mock、分层断言减少 flake

## Example Questions
1) 断言是否具体而稳定（文本/URL/计数）而非仅可见？
2) 失败时是否有 trace/video/screenshot 以支持定位？
3) 是否通过 test.step 输出语义化步骤，报告可读？
4) baseURL、retries、项目矩阵是否在配置集中管理？
5) 选择器是否基于可访问性而非脆弱 CSS？
6) 是否将登录/导航封装在 beforeEach 或 fixture？
7) 用例是否无共享状态、可并行运行？
8) 慢/易变模块是否通过 mock 拆除外部脆弱性？
9) 快照是否用于结构（ARIA）与关键视图而非全部像素？
10) CI 是否启用分片与仅重跑失败以提高吞吐？
11) flaky 是否通过重试与稳定化策略（超时、定位器）降低？

Source: d:\mycode\awesome-copilot\instructions\playwright-typescript.instructions.md | Generated: 2025-10-17
