## What/When/Why/How
- What: 规格驱动工作流 v1（文档为真源 + 6 阶段循环）
- When: 执行从需求→设计→实现→验证→复盘→交接的端到端任务时
- Why: 降低歧义、可追踪、可验证、可移交
- How: requirements.md/design.md/tasks.md + 6 阶段严格执行

## Key Points
- 文档：EARS 需求；设计含架构/接口/模型；tasks 可执行
- 6 阶段：Analyze→Design→Implement→Validate→Reflect→Handoff
- 关键约束：阶段前置检查通过方可推进；错误需回溯
- 质量：错误矩阵、测试策略、性能验证、跟踪日志
- 技债：决策记录/影响/审查；自动化创建与优先级
- 报告：行动日志/压缩决策记录；PR 打包材料
- 故障处理：重分析/重设计/重计划/重试/升级

## Compact Map
- Docs: req/design/tasks
- Loop: A-D-I-V-R-H
- QA: tests/perf/traces
- Debt: records/issues/prioritize

## Example Questions
1) 是否已用 EARS 定义清晰可测的需求？
2) 设计文档是否覆盖架构/接口/模型与错误矩阵？
3) 进入实现前是否完成计划与风险评估？
4) 每个增量是否有验证与文档证据？
5) 失败是否经根因分析并更新设计/计划？
6) 覆盖率/复杂度/可维护指标是否纳入度量？
7) 决策是否记录并设定复审时间点？
8) 技债项是否建档、估算与排序？
9) 交接包是否包含摘要/日志/验证链接？
10) 故障处理是否遵循回溯与重试协议？
11) 是否禁止在前置未完成时越级推进？

Source: d:\mycode\awesome-copilot\instructions\spec-driven-workflow-v1.instructions.md | Generated: 2025-10-17
