## Interactive Programming Nudge — Mind Map

### What
- 提醒代理以“交互式程序员”方式工作：以系统（REPL）为真相源，边探索边修改。

### When
- 具备 REPL/实时运行环境（Clojure 等）时；需要快速验证与迭代时。

### Why
- 用最短反馈回路理解系统真实行为，减少臆测与无效重构。

### How
- 简述评估内容→小步执行→汇报要点（而非吐出大段执行结果）→结构化编辑→维护待办。

### Key Points (中/英)
- 评估/Evaluate
- 探索/Explore
- 小步提交/Small Steps
- 结构化编辑/Structural Editing
- 真实来源/Source of Truth
- 待办/Todo hygiene

### Compact map
- REPL: run → observe → summarize
- Edit: structural, reversible, minimal
- Communicate: concise deltas, intent, next step
- Track: keep TODO list fresh

### Example Questions (≥10)
- 在有 REPL 的项目里，哪些操作值得先用 REPL 探索而非直接改文件？
- 我如何用“简述评估内容”的方式报告一次大规模评估？
- 避免粘贴长执行输出的最佳做法有哪些？
- 结构化编辑和普通文本编辑的边界与收益？
- 如何将 REPL 实验固化为最小可逆提交？
- 交互式探索时如何管理临时代码与清理策略？
- 何时该从 REPL 切回测试驱动的提交节奏？
- 沟通中“delta-first”的最佳表达模板是？
- 如何将 REPL 发现转化为具体 TODO 与后续 PR 计划？
- 失败实验应如何被记录以便未来复用或规避？

---
- Source: d:\mycode\awesome-copilot\prompts\remember-interactive-programming.prompt.md
- Generated: 2025-10-17
