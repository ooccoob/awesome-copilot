## What / When / Why / How

- What: Blueprint Mode（结构化工作流 v39，严谨、复现、工具策略升级）
- When: 需要覆盖从分析→设计→计划→实现→验证的完整闭环
- Why: 以工程化准则和自反校验提升可靠性
- How: 选择工作流→多轮自检→阈值信心决策→最小更改→质量门禁

## Key Points

- 强化规范：SOLID/DRY/KISS/一致性
- 工具策略：并行只读、顺序依赖、避免交互式、prefer 集成工具
- 自反评分门槛（>8 全通过）→不足即返工
- Spartan 沟通与最终总结（Outstanding/Next/Status）

## Compact Map

- 分析→设计→计划→实现→验证
- 事实先行：读取/搜索/用例
- 自检评分→返工迭代
- 最终产物与后续步骤

## Example Questions (10+)

- 哪个工作流最贴切当前任务？
- 需要哪些事实与上下文阅读验证？
- 方案与既有代码风格/结构如何对齐？
- 最小变更集如何定义并验证？
- 质量门槛评分如何量化并记录？
- 潜在边界与失败模式有哪些？
- 如何在不影响外部行为的前提下重构？
- 产物如何做到可审查、可复现、可回滚？
- 结束时的状态/后续如何清晰呈现？
- 是否存在更简单等价实现？
- 如何控制工具调用成本与噪音？

---
Source: d:\mycode\awesome-copilot\chatmodes\blueprint-mode.chatmode.md
Generated: {{timestamp}}
