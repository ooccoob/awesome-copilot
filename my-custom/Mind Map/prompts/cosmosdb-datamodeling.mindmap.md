## Azure Cosmos DB NoSQL 数据建模专家系统（思维导图）

- What
  - 引导式采集应用访问模式、规模、地理分布与一致性需求
  - 产出：cosmosdb_requirements.md 与 cosmosdb_data_model.md 两份工件
  - 方法论：基于聚合建模、访问相关性、标识关系、容器合并评审
- When
  - 启动新系统/重构关系型到 NoSQL
  - 出现跨分区高频查询或热分区/写入瓶颈
  - 全球多活/一致性与成本需权衡
- Why
  - 消除不必要的跨分区查询，降低 RU 成本
  - 明确聚合边界与分区键，避免热键与存储/索引膨胀
  - 提前量化成本（RU/存储/区域），做可预期的容量规划
- How
  - 访问模式清单：为每个 Pattern 记录 RPS(峰值/均值)、SLO、一致性、结果大小
  - 聚合判定：按共同访问比例与尺寸/更新频率选择 单文档/同容器多文档/分容器
  - 分区键设计：高基数、均匀分布，可考虑写分片与层级分区键（HPK）
  - 索引策略：仅索引被查询属性；必要时加复合索引；排除无用路径
  - 成本评估：读/写 RU × 频率 + 跨分区 2.5 RU × 物理分区数；按月估算
  - 大规模写入：数据分箱/分块（chunk）+ 写分片；避免时间热点
  - 全局分布：一致性级别/冲突解决/故障切换策略

- Key Points (CN/EN)
  - 聚合导向 Aggregates over entities
  - 标识关系 Identifying relationship
  - 多文档同容器 Multi-document container
  - 单文档聚合 Single-document aggregate
  - 层级分区键 Hierarchical Partition Keys (HPK)
  - 写分片 Write sharding
  - 稀疏索引 Sparse/selective indexing
  - 事务边界 ACID-in-partition

- Example Questions (≥10)
  1) 最高/平均 RPS 的前5个访问模式分别是什么？各自 SLO？
  2) 哪些父子关系满足“标识关系”，可用 parent_id 作为分区键？
  3) 哪些查询经常需要联取两类实体？其共同访问比例是多少？
  4) 预估主实体文档大小分布（P50/P95/Max），会触及 2MB 限制吗？
  5) 预计总数据量与留存期？按 50GB/物理分区估算需多少物理分区？
  6) 哪些查询必须跨分区？是否能通过建模/索引降为单分区？
  7) 哪些字段需要复合索引（排序+过滤）？排除哪些路径降写入 RU？
  8) 是否存在热门键/顺序键（如今天日期）导致写热点？如何写分片？
  9) 全局分布是否需要多写区域？一致性选择与冲突策略为何？
  10) 读/写月度成本估算分别是多少？不同设计方案对比如何？

- Compact Mind Map
  - 访问模式→聚合判定→分区键→索引→成本→分布
  - 特殊场景：批量写→分箱；高并发→写分片；层次查询→HPK

- Source: prompts/cosmosdb-datamodeling.prompt.md
- Generated: 2025-10-17
