## What / When / Why / How

- What: Clojure 交互式编程（REPL-first、架构完整性、数据驱动）
- When: 需要在 REPL 驱动下小步构建与验证，再落盘改动
- Why: 快速反馈、最小回归、保持纯函数与可测试性
- How: 找源→REPL 验证→交互开发→多例验证→文件修改→零警告/全测过

## Key Points

- 禁止权宜之计隐藏配置/基础设施问题，失败要清晰
- 数据优先：解构、名字空间关键字、扁平结构
- 逐步 REPL 评估替代 println
- 架构违规（副作用/不可测/全局原子）需重构
- 完成定义：架构完整、REPL 测过、零警告、测试全过

## Compact Map

- 查阅→评估当前→REPL 试探实现
- 多用例/边界→再落盘
- 结构化编辑与命名
- 失败路径与性能对比

## Example Questions (10+)

- 哪个命名空间与源文件需要先完整阅读？
- 当前行为如何在 REPL 中复现与测量？
- 有哪些副作用可推迟或封装到最后一环？
- 数据结构是否可简化并以解构表达？
- 错误信息能否更具可诊断性且无回避？
- 评估分步表达式代替 println 的方案？
- 变更前后的性能对比方法是什么？
- 测试数据如何在 REPL 中生成与复用？
- 哪些架构违规需要本次一并修复？
- 改动如何避免破坏可测试性？
- 完成后如何确保零警告与测试全过？

---
Source: d:\mycode\awesome-copilot\chatmodes\clojure-interactive-programming.chatmode.md
Generated: {{timestamp}}
