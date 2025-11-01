## PostgreSQL 代码评审助手（思维导图）

- What
  - 面向 PostgreSQL 特性的代码评审：JSONB/数组/自定义类型/Schema/触发器/扩展/RLS
  - 输出具体修改建议与示例 SQL/DDL；关注安全、性能与可维护性
- When
  - 合并 PR 前的数据库变更评审
  - 发现慢 SQL、索引缺失、类型不当、约束不足
  - 需要落地 RLS 与权限最小化
- Why
  - 用好 PG 专属能力（GIN/GiST、JSONB、FTS、域/枚举）获得更高性价比
  - 通过约束/类型/索引设计提升质量与性能
- How
  - JSONB：使用 @>、? 运算与 GIN 索引；必要时 CHECK 约束保障结构
  - 数组：ANY/&&/array_ops + GIN；聚合用 array_agg/unnest
  - 模式设计：CITEXT、TIMESTAMPTZ、域/ENUM；约束与表达式/部分索引
  - 函数/触发器：仅在必要处触发；使用 CURRENT_TIMESTAMP；WHEN 过滤
  - 扩展：uuid-ossp/pgcrypto/pg_trgm/btree_gin 依需要启用
  - 安全：启用 RLS；精细化 GRANT；参数化查询

- Key Points (CN/EN)
  - JSONB + GIN, arrays + GIN
  - Partial/Expression/Covering indexes
  - CITEXT/TIMESTAMPTZ/ENUM/DOMAIN
  - Row Level Security (RLS)
  - pg_stat_statements 与 EXPLAIN (ANALYZE)

- Example Questions (≥10)
  1) 这些 JSONB 查询能改为 @> 或 path 运算并配套 GIN 吗？
  2) 哪些数组查询可用 GIN 与 operators（ANY/&&）优化？
  3) 哪些列适合改为 CITEXT/ENUM/DOMAIN 并增加 CHECK？
  4) 是否存在可改为部分/表达式/覆盖索引的场景？
  5) 时间类型是否统一为 TIMESTAMPTZ？
  6) 触发器是否加 WHEN 条件减少无谓执行？
  7) 是否启用并审查 RLS 策略？
  8) 权限是否最小化，序列 USAGE 是否单独授予？
  9) 是否使用 pg_stat_statements 定位最慢 TOP10 查询？
  10) 是否存在反模式：LIKE 于 JSON、OFFSET 深翻页、未参数化？

- Compact Mind Map
  - Schema→类型/约束→索引→查询→函数/触发器→扩展→安全

- Source: prompts/postgresql-code-review.prompt.md
- Generated: 2025-10-17
