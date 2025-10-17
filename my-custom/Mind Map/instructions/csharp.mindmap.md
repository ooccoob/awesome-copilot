## C# 开发通用指南（英文版要点）

- What: C# 13+ 语法/风格、工程结构、EF Core、认证/鉴权、验证与错误、版本/文档、日志监控、测试、性能与 DevOps。
- When: 新建 .NET 项、实现 API、接入数据访问与身份、安全上线与运维时。
- Why: 统一标准、降低缺陷、提升可维护性与可观测性。
- How: 采用现代 C# 特性、清晰注释、命名/格式一致；分层与 DDD/特性目录；统一校验与异常；结构化日志与遥测；覆盖关键测试；容器化与 CI/CD。

### 关键要点（提要）
- 命名/格式/注释：PascalCase/camelCase；nameof；XML 文档含 <example>/<code>；文件作用域 namespace。
- 可空：入口 null 检查；is null 判式；信任 NRT。
- 数据：EF Core + 迁移/种子；仓储可选；分页/AsNoTracking；查询优化。
- 认证：JWT/OIDC/Entra ID；角色/策略；统一保护 Controller/Minimal API。
- 验证/错误：DataAnnotations + FluentValidation；中间件异常；Problem Details。
- 文档/版本：Swagger/OpenAPI；多版本分组。
- 日志/监控：Serilog/AI；相关 ID；遥测监控性能与错误。
- 测试：单测/集成/鉴权；TDD 可选；关键路径覆盖。
- 性能：缓存/异步/分页/压缩/基准。
- DevOps：容器发布/手写 Dockerfile；CI/CD；健康检查；多环境配置。

### Compact Map
Style→Null→Data→Auth→Errors→Docs→Logs→Tests→Perf→DevOps

### 示例问题
1) ASP.NET Core 9 中如何组织 Program.cs 与多环境配置？
2) 统一返回 RFC7807 的最佳落地方式？
3) EF Core 查询如何在性能与可维护性间取舍？
4) JWT 与 OIDC 同时启用的策略写法？
5) Swagger 示例如何对齐 XML 文档注释？
6) 结构化日志的字段规范与脱敏策略？
7) 集成测试中如何 Mock 外部服务与鉴权？
8) 分布式缓存与本地缓存的选型与失效策略？
9) 使用内置容器发布与自定义 Dockerfile 的权衡？
10) 在 CI/CD 中如何做蓝绿/金丝雀发布？

Source: d:\mycode\awesome-copilot\instructions\csharp.instructions.md | Generated: 2025-10-17T00:00:00Z
