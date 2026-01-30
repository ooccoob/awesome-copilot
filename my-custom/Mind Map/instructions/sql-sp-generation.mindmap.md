## What/When/Why/How
- What: SQL 与存储过程规范（命名/结构/安全/事务/风格）
- When: 设计表结构、编写查询与 SP 时
- Why: 一致性、可维护与安全防注入
- How: 统一命名 + 结构化查询 + 标准化 SP 头/参数/返回

## Key Points
- 架构：单数表/列；主键 id；created_at/updated_at
- 约束：主键/外键命名与级联；内联定义；引用父表 PK
- 风格：关键字大写；缩进分行；注释复杂逻辑
- 查询：显式列；限定表名/别名；尽量 JOIN；限制结果集
- SP 命名：usp_ 前缀 + PascalCase（GetProducts/GetProduct）
- 参数：@camelCase；必填在前；默认值；验证与注释
- SP 结构：头注释/标准错误码/列顺序一致/OUTPUT 状态/tmp_ 临时表
- 安全：参数化/预编译；避免动态 SQL；不含凭证
- 事务：显式 begin/commit；隔离级别；NOCOUNT；分批大操作

## Compact Map
- Schema: pk/fk + timestamps
- Query: columns + joins + limit
- SP: usp_* + params + header + output
- Sec/Tx: parameterize + error/iso + nocount

## Example Questions
1) 表/列命名是否单数且包含审计字段？
2) 外键是否内联且含 ON DELETE/UPDATE CASCADE？
3) 查询是否避免 SELECT * 并限定结果集？
4) 是否避免在索引列上使用函数？
5) 存储过程是否使用 usp_ 前缀与 PascalCase？
6) 参数是否有默认/验证并文档化？
7) 是否统一错误返回并含输出参数？
8) 所有查询是否参数化并避免动态 SQL？
9) 事务是否短小且设置合适隔离级别？
10) 批处理是否分批并使用 NOCOUNT？
11) 索引策略是否覆盖高频过滤/排序列？

Source: d:\mycode\awesome-copilot\instructions\sql-sp-generation.instructions.md | Generated: 2025-10-17
