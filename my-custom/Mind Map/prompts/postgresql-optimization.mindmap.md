## PostgreSQL 优化助手（思维导图）

- What
  - PostgreSQL 专属能力与优化：JSONB、数组、窗口函数、全文检索、扩展
  - 查询/索引/存储/连接与内存/监控的系统性优化建议
- When
  - 慢查询、CPU/IO 占用高、连接爆炸、表/索引膨胀
  - 新特性引入与数据模型重构前
- Why
  - 充分利用 PG 的高阶特性实现性价比最优
  - 以可观测性驱动改造，避免盲目调参
- How
  - 查询分析：EXPLAIN (ANALYZE, BUFFERS)；pg_stat_statements 排序
  - 索引策略：复合/部分/表达式/覆盖；为 JSONB/数组建 GIN/GiST
  - 存储：数据类型压缩；去除无用列；分区与冷热分层
  - 连接与内存：连接池（pgbouncer）；shared_buffers/work_mem/maintenance_work_mem
  - 监控与维护：VACUUM/ANALYZE；索引使用率与膨胀；日志阈值
  - 扩展：uuid-ossp/pgcrypto/unaccent/pg_trgm/btree_gin

- Key Points (CN/EN)
  - EXPLAIN/pg_stat_statements
  - Composite/Partial/Expression/INCLUDE Index
  - JSONB/Array + GIN
  - FTS, Window functions
  - Partitioning, Vacuum/Analyze

- Example Questions (≥10)
  1) 最慢 TOP10 查询与其计划（FE/SE 比例）分别是什么？
  2) 哪些查询是全表扫，缺少合适索引/统计信息？
  3) 哪些索引长期 idx_scan=0 可下线？
  4) 是否有可改为部分索引或表达式索引的过滤模式？
  5) JSONB/数组查询是否启用 GIN/GiST 并使用 @>/ANY/&&？
  6) OFFSET 深分页能否改为游标/键集分页？
  7) DirectQuery/联邦场景是否需要聚合表/物化视图？
  8) 连接池与 max_connections 是否合理？
  9) autovacuum、统计信息与日志阈值设置是否合适？
  10) 是否存在超高基数字段导致压缩差并拖慢联接？

- Compact Mind Map
  - 观测→定位→索引/查询→存储/分区→连接/内存→扩展→维护

- Source: prompts/postgresql-optimization.prompt.md
- Generated: 2025-10-17
