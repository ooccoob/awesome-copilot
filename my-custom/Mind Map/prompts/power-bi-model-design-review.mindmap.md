## Power BI 数据模型设计评审（思维导图）

- What
  - 评审星型模型、关系、存储模式、可扩展性与治理
- When
  - 上线前健康检查；性能异常与可维护性问题
- Why
  - 降低模型体积与刷新/查询时延，提升可靠性与治理
- How
  - 架构：事实/维度分离、粒度一致、桥表/多对多合理化
  - 关系：基数/滤向/完整性；隐藏外键；避免环路
  - 存储：Import/DirectQuery/Composite/Dual/Hybrid 策略
  - 性能：聚合表/压缩/去冗余/减少计算列
  - 治理：文档/命名/安全（RLS）/变更与发布流程

- Key Points (CN/EN)
  - Star schema; Dual storage
  - Aggregations; Relationship cardinality
  - RLS; Documentation

- Example Questions (≥10)
  1) 事实表粒度是否统一？是否存在混合粒度导致的错误聚合？
  2) 有哪些多对多关系，是否可以通过桥表解决？
  3) 哪些维度可设置为 Dual 以优化复用？
  4) 模型膨胀的主要来源（高基数文本/计算列）是什么？
  5) 刷新/查询慢的首要瓶颈与可行的聚合策略？
  6) 哪些列/表可移除或下推到源头预处理？
  7) 关系是否需要双向？能否改单向并用度量实现？
  8) 是否具备一致的命名与文档？
  9) RLS 设计是否正确且通过性能验证？
  10) 变更发布与回滚策略是否完善？

- Compact Mind Map
  - 架构→关系→存储→性能→治理

- Source: prompts/power-bi-model-design-review.prompt.md
- Generated: 2025-10-17
