## What / When / Why / How

- What: TDD Green（最小实现使测试通过，按 Issue 需求）
- When: 已有失败测试，需尽快变绿
- Why: 快速验证需求，避免过度设计
- How: 重读 Issue→跑失败测试→最小改动→全套测试→仅更新进度

## Key Points

- 范围：只做当前 Issue 范围；最小可行
- 策略：硬编码→条件→提取方法；简单集合优先
- 纪律：不改测试（理想上）；避免超范围改动

## Compact Map

- 需求→失败→最小实现→全绿→记录

## Example Questions (10+)

- Issue 的验收标准与边界案例？
- 首个失败测试的最小实现路径？
- 有无引入额外复杂度？
- 现有用例是否仍全部通过？
- 需要哪些硬编码或临时实现？
- 何处可待后续重构？
- 与其他模块的影响？
- 进度如何同步到 Issue？
- 是否需要新增测试来三角化？
- 回滚策略？

---
Source: d:\mycode\awesome-copilot\chatmodes\tdd-green.chatmode.md
Generated: {{timestamp}}
