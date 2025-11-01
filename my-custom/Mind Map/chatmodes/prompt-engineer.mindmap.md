## What / When / Why / How

- What: Prompt Engineer（把输入当“提示”来分析并重写）
- When: 需要系统化评审与输出改进后的系统提示
- Why: 通过<reasoning>结构化评估→输出最终提示
- How: 先在<reasoning>中评分/优先级/结论→再给完整系统提示

## Key Points

- 任何输入都当待改进提示；不直接完成任务
- 必须先输出 <reasoning> 段并按清单评估
- 最终仅输出“完整系统提示”正文（无额外说明）
- 结构：任务描述→细节→步骤→输出格式→示例→备注

## Compact Map

- 评估→重写→结构化→可测可执行

## Example Questions (10+)

- 输入提示的核心目标与受众是谁？
- 需要的输出格式最合适为何种？
- 是否需要 Few-shot 示例与占位符？
- 推理顺序与结论顺序是否需要反转？
- 需要哪些约束与成功标准？
- 哪些冗余/冲突需要去除？
- 版本/上下文依赖要如何说明？
- 如何确保安全与防注入？
- 如何测评改写后的稳定性？
- 与现有工作流如何集成？

---
Source: d:\mycode\awesome-copilot\chatmodes\prompt-engineer.chatmode.md
Generated: {{timestamp}}
