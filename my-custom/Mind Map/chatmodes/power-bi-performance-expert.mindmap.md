## What / When / Why / How

- What: Power BI 性能专家（模型/查询/报表/容量）
- When: 加载慢、交互卡顿或容量紧张时
- Why: 系统化诊断与优化确保体验与成本
- How: 建基线→找瓶颈→针对优化→复测→持续监控

## Key Points

- 工具：Performance Analyzer、DAX Studio、Query Diagnostics、Fabric Metrics
- 模型：列/行裁剪、类型、聚合、增量刷新
- DirectQuery：索引/物化视图、简化度量、减少跨表
- 报表：视觉数量、交互、过滤策略、移动优化
- 容量：监控 CPU/内存/并发，合理调度刷新

## Compact Map

- 评估→诊断→优化
- 模型/查询/报表/容量
- 监控与回归

## Example Questions (10+)

- 基线指标与目标阈值是什么？
- 页面与视觉的主要慢点在哪里？
- 哪些列/表可裁剪或降粒度？
- DirectQuery 的索引与折叠情况？
- 报表首屏加载如何优化？
- 聚合表与缓存策略如何设计？
- 容量监控有哪些告警阈值？
- 网络/网关是否是瓶颈？
- 优化后的回归与验证流程？
- 用户体验的可量化改善如何体现？

---
Source: d:\mycode\awesome-copilot\chatmodes\power-bi-performance-expert.chatmode.md
Generated: {{timestamp}}
