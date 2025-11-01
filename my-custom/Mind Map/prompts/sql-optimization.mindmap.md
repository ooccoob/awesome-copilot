## SQL Performance Optimization — Mind Map

### What
- 通用 SQL 性能优化助手：查询、索引、分页、聚合、批处理、监控。

### When
- 慢查询、吞吐下降、数据增长导致延迟、分页深度过大时。

### Why
- 可测量的响应改善、资源效率提升与成本控制。

### How
- 定位→执行计划→结构重写→索引策略→批/分页→监控→回归测试。

### Key Points (中/英)
- 执行计划/Explain
- 复合索引/Composite Index
- 覆盖索引/Covering
- 窗口函数/Window
- 游标分页/Cursor Pagination
- 批处理/Batch Ops
- 部分索引/Partial Index
- 监控/Monitoring

### Compact map
- Anti-patterns: SELECT *, 函数在 WHERE, 相关子查询, 大 OFFSET
- Techniques: JOIN 重写, 条件聚合, UNION ALL, 临时表
- Monitoring: slow log/pg_stat/sys.dm_exec

### Example Questions (≥10)
- 该查询的瓶颈来自扫描、排序还是连接？
- 合适的复合索引列序与包含列如何选择？
- 何时用 EXISTS/IN/JOIN 更优？
- 如何将 OFFSET 分页改为游标/时间游标？
- 相关子查询能否以窗口函数改写？
- 何时使用临时表/物化中间结果？
- 如何评估过度索引带来的写入成本？
- 不同数据库下的等价优化写法有哪些？
- 如何建立持续慢查询告警与基线？
- 优化收益如何度量并防止回归？

---
- Source: d:\mycode\awesome-copilot\prompts\sql-optimization.prompt.md
- Generated: 2025-10-17
