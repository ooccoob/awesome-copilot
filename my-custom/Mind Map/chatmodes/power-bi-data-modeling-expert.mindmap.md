## What / When / Why / How

- What: Power BI 数据建模专家（星型模型、关系、性能）
- When: 需要高性能、可维护的数据模型设计
- Why: 通过维度建模与最佳实践提升可用性与速度
- How: 先查 MS Docs→星型设计→关系/存储模式→性能/安全→验证

## Key Points

- 星型：事实/维度分离；一致粒度；外键/度量清晰
- 关系：一对多为主；双向谨慎；桥接表处理 M2M
- 存储：Import/DirectQuery/Composite；Dual 用于维度
- 性能：列/行裁剪、类型优化、禁用 Auto Date/Time
- 安全：RLS/CLS；治理与血缘

## Compact Map

- 需求→星型→关系→存储
- 优化→验证→安全

## Example Questions (10+)

- 模型的事实表与维度表边界如何划分？
- 关系基数与方向如何设置最优？
- 哪些维度应使用 Dual 模式？
- 需要的行/列裁剪策略？
- 自带日期表是否禁用并替换为自定义？
- DirectQuery 的索引与查询折叠策略？
- 何处使用聚合表提升性能？
- RLS 规则如何定义与验证？
- 复用的度量库如何组织？
- 模型验证与性能回归如何执行？

---
Source: d:\mycode\awesome-copilot\chatmodes\power-bi-data-modeling-expert.chatmode.md
Generated: {{timestamp}}
