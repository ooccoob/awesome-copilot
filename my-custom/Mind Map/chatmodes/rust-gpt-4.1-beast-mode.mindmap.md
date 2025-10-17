## What / When / Why / How

- What: Rust Beast Mode（端到端问题求解 + 强制网络检索）
- When: 需要彻底、验证充分、可运行的 Rust 方案
- Why: 通过递归检索/计划/实现/测试确保完备
- How: 工具前置声明→严格工作流→清单化 ToDo→持续测试与迭代

## Key Points

- 强制使用 fetch_webpage（Google/Bing/官方文档）
- 工作流：理解→调查→计划→实现→调试→测试→回归
- 反模式清单：clone/unwrap/unsafe/过度抽象/全局可变等
- 要求：每步前解释、一旦声明就执行；直到完成

## Compact Map

- 检索→分析→计划→实现→测试→验证

## Example Questions (10+)

- 目标问题的精确定义与成功标准？
- 依赖与版本的最新权威用法？
- 代码库结构与关键模块位置？
- 风险与边界条件有哪些？
- 计划步骤的可验证产出？
- 常见反模式如何避免？
- 测试覆盖与基准如何设计？
- 需要哪些命令与工具链？
- 何处需要并发/异步？
- 出错与回滚策略？

---
Source: d:\mycode\awesome-copilot\chatmodes\rust-gpt-4.1-beast-mode.chatmode.md
Generated: {{timestamp}}
