## What / When / Why / How

- What: 任务规划器（研究先行→三文件输出：计划/细节/实现提示）
- When: 有经过验证的研究材料后输出可执行计划
- Why: 以证据驱动计划，分离研究/计划/实现
- How: 校验研究→生成 plans/details/prompts 三文件→严格命名/引用行号

## Key Points

- 研究门禁：不合格即调用 task-researcher 先补齐
- 文件：plans/*.instructions.md、details/*.md、prompts/*.md
- 协议：模板占位 {{}}；行号引用保持同步；只在 .copilot-tracking 下写
- 输出：会话仅状态更新，不展示全文

## Compact Map

- 校研→分支创建→三文生成→校验引用→准备实施

## Example Questions (10+)

- 研究文件是否完备？缺口在哪里？
- 任务的目标、依赖与成功标准？
- 分阶段清单如何编排可并行/可验证？
- 细节文件与研究的行号映射？
- 实施提示如何引用计划？
- 失败与回滚路径？
- 质量门与检查点？
- 跨任务依赖与优先级？
- 命名与目录是否符合规范？
- 何时触发研究更新循环？

---
Source: d:\mycode\awesome-copilot\chatmodes\task-planner.chatmode.md
Generated: {{timestamp}}
