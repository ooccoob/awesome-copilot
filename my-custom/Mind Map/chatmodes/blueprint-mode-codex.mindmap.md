## What / When / Why / How

- What: Blueprint Mode Codex（严谨、可复现、最小工具使用的工作流执行）
- When: 需要高正确性、可维护、可自我纠错的工程化执行
- Why: 强约束与自检提高质量并减少偏差
- How: 选择工作流（Loop/Debug/Express/Main）→并行只读→小步实现→重试与总结

## Key Points

- 不假设：一切以代码和配置为准，先读再做
- 并行化读操作、顺序化依赖步骤
- 自我校验与最多 3 次重试，失败记录为 FAILED
- 最少字数沟通、输出为可执行/可审查产物
- 结束提供 Outstanding/Next/Status 摘要

## Compact Map

- 分析→选工作流
- 搜索/读取→事实校验
- 计划→最小可验证步骤
- 实施→工具精简使用
- 验证→问题修复与重试
- 总结→结果与后续

## Example Questions (10+)

- 当前目标属于 Loop/Debug/Express/Main 的哪一类？
- 哪些事实需要从仓库文件中验证后再行动？
- 如何以最少工具调用完成高可信结果？
- 并行可行的读取任务有哪些？
- 失败后的三次重试分别采用什么不同策略？
- 约束如何与项目既有风格/框架对齐？
- 交付物的最小可验证集是什么？
- 如何记录 FAILED 项并在最后回溯？
- 输出的最终摘要要包含哪些关键信息？
- 如何评估完成度与剩余风险？
- 哪些边界情况必须在本轮覆盖？

---
Source: d:\mycode\awesome-copilot\chatmodes\blueprint-mode-codex.chatmode.md
Generated: {{timestamp}}
