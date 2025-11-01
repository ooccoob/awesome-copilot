## SQL Code Review — Mind Map

### What
- 面向多数据库的通用 SQL 代码审查：安全、性能、可维护、架构设计。

### When
- 上线前评审、性能回归、规范统一或疑似注入与越权风险时。

### Why
- 提升质量与安全基线，降低隐患与成本。

### How
- 安全→性能→风格→模式→DB 特性→测试校验→输出整改清单与评分。

### Key Points (中/英)
- 注入/Injection
- 权限/Access Control
- 索引/Indexing
- 连接/Joins
- 聚合/Aggregation
- 风格/Style
- 规范/Naming
- 约束/Constraints

### Compact map
- Security: 参数化/最小权限/敏感列
- Performance: 结构/索引/JOIN/窗口
- Quality: 风格/命名/注释
- Schema: 规范化/数据类型/约束
- DB-specific: PG/MySQL/SQLServer/Oracle
- Output: issues + scores + top actions

### Example Questions (≥10)
- 哪些语句有字符串拼接构造的动态 SQL 风险？
- 角色/模式/对象权限是否最小化？
- SELECT * 是否可替换为显式列并覆盖索引？
- 连接条件是否完整避免笛卡尔积？
- WHERE 函数调用能否改为范围以启用索引？
- 聚合/窗口是否正确避免相关子查询？
- 命名与风格是否一致且可读？
- 约束/默认值是否合理，是否有负值/NULL 异常？
- 跨数据库差异（时区/函数/分页）如何兼容？
- 优先整改清单的前三项是什么？

---
- Source: d:\mycode\awesome-copilot\prompts\sql-code-review.prompt.md
- Generated: 2025-10-17
