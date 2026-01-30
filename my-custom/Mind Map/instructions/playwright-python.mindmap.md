## What/When/Why/How
- What: Playwright Python 编写稳健端到端测试的简明要点与清单
- When: 新建/重构 UI 测试、定位 flaky、建立团队规范与模板时
- Why: 降低 flaky、提升可维护性与可读性、加速调试与定位
- How: 以角色定位器与 web-first 断言为核心，靠 Pytest fixtures 组织、少等待多校验、保持可读结构

## Key Points
- 选择定位器：优先 get_by_role/get_by_label/get_by_text（可访问性优先）
- 断言策略：expect(page|locator).to_have_* 系列，避免硬等待与盲等
- 超时与等待：依赖自动等待，禁用 sleep，必要时缩小作用域设置 timeout
- 结构：tests/ + test_*.py；函数签名注入 page: Page；复用前置用 Pytest fixtures
- 组织：test.describe/类分组、语义化用例名、最小可读步骤
- 稳定性：去除随机依赖；解耦网络波动；减少跨测试状态耦合
- 可维护性：封装常用选择器与步骤；页面对象或轻量 helper；统一错误截图/视频
- 可观测性：trace、screenshot、console、network 日志按需开启；失败自动保留

## Compact Map
- Imports: from playwright.sync_api import Page, expect
- Setup: fixture 导航; page.goto(baseUrl)
- Locators: role/label/text > css/xpath；减少 nth 依赖
- Assertions: to_have_title/url/text/count/value; 避免只校验可见
- Patterns: 分层封装（Page Object/Helper）、数据驱动、idempotent 前置
- CI: 并行、重试、仅重跑失败、HTML 报告、失败保留 trace

## Example Questions
1) 当前用例的断言是否具体且 web-first（能自动重试）？
2) 哪些等待仍是硬等待，能否用 expect 或 locator.wait_for 替代？
3) 定位器是否优先基于角色/可达性而非脆弱的 CSS？
4) 失败时是否自动生成 trace.zip 与截图便于复盘？
5) 基线导航与登录是否用 fixture 复用且幂等？
6) 用例是否可以独立运行且互不依赖共享状态？
7) 是否为易变元素（toast、动画）设置了更稳健的断言策略？
8) CI 是否开启并行、重试与仅重跑失败以降低 flake 成本？
9) 数据准备与清理是否最小化并可重复？
10) 页面对象/Helper 是否把多步交互压缩为单一语义动作？
11) 是否将 baseURL、超时、headless、video/trace 策略集中配置？

Source: d:\mycode\awesome-copilot\instructions\playwright-python.instructions.md | Generated: 2025-10-17
