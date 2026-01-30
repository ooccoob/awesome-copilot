## C# 指南（韩文版要点）

- What: C# 代码风格、命名、格式化、语言特性、安全、性能与异常处理准则。
- When: 编写/评审 C# 源码、引入异步与 LINQ、设计异常与日志策略时。
- Why: 统一规范、提高可读性与安全性，减少错误与性能损耗。
- How: 依照表格化命名与格式规则；恰当使用 async/await、LINQ、表达式成员与 NRT；严格异常边界与输入校验。

### 关键要点
- 命名: 接口 I 前缀；公开成员 PascalCase；私有字段使用 _camelCase 或 camelCase；泛型形参 TKey/TValue。
- 格式: 4 空格缩进；所有控制流使用花括号；逻辑块间空行；尽量避免多语句单行；`nameof` 代替字符串字面值。
- 语言特性: 异步 I/O 使用 async/await + ConfigureAwait；LINQ 表达清晰查询；表达式成员简化只读属性；启用（或遵循）可空注解。
- 异常: 只捕获可处理的具体异常；避免以异常作控制流；统一错误响应。
- 性能: 字符串拼接用 StringBuilder；EF Core 读用 AsNoTracking；避免不必要的装箱与分配。
- 安全: 参数校验、防注入、密钥不硬编码，使用 Secret Manager/Key Vault。

### Compact Map
- Naming -> 接口/成员/字段/泛型
- Formatting -> 缩进/花括号/空行
- Language -> async/LINQ/expr members/NRT
- Exceptions -> 具体捕获/非流程控制
- Perf -> StringBuilder/AsNoTracking
- Security -> 校验/密钥管理

### 示例问题
1) 何时应使用 ConfigureAwait(false)？
2) LINQ 查询如何避免在数据库端生成低效 SQL？
3) 统一错误响应的最佳实践有哪些？
4) 如何在库代码里避免 sync-over-async 死锁？
5) 表达式成员在何种场景下更具可读性？
6) 如何为可空注解配置项目级规则？
7) 捕获异常的粒度如何拿捏（策略示例）？
8) EF Core 查询中的投影与跟踪策略选择？
9) nameof 与字符串字面量的取舍原则？
10) 密钥与连接串如何接入安全存储？

Source: d:\mycode\awesome-copilot\instructions\csharp-ko.instructions.md | Generated: 2025-10-17T00:00:00Z
