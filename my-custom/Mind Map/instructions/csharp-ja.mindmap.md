## C# 指南（日文版要点）

- What: 面向 C# 应用开发的统一实践与风格（含 ASP.NET Core、EF Core、认证/鉴权、测试、部署运维）。
- When: 新建/评审 .NET 项目、实现 API、接入数据访问与认证、上线与监控时。
- Why: 提升可维护性与一致性，减少异常与性能坑，保障文档与安全合规。
- How: 采用最新 C# 特性、清晰注释、规范命名/格式、分层与模板、统一验证与错误处理、日志监控与测试覆盖。

### 关键要点
- 命名与格式: Public/类型/方法用 PascalCase；私有字段/局部变量 camelCase；接口前缀 I；文件作用域 namespace 与单行 using（推荐）。
- 可空与空值: 使用 is null / is not null；入口做 null 检查；依赖 NRT 做静态保证，避免重复检查。
- 数据访问: EF Core + 迁移/种子；Repository 模式按需；分页/AsNoTracking/只取必要列；防 N+1。
- 认证鉴权: JWT Bearer；OAuth2/OIDC；基于角色与策略；统一保护 Controller 与 Minimal API；可集成 Entra ID。
- 校验与错误: DataAnnotations + FluentValidation；全局异常中间件；Problem Details(RFC7807)。
- 文档与版本: OpenAPI/Swagger 完整注释与示例；支持 API 版本化策略。
- 日志与监控: 结构化日志（Serilog 等）；遥测/相关 ID；性能、错误与使用模式监控。
- 测试: 关键路径必测；单测/集成/鉴权用例；遵循现有命名风格；TDD 可选。
- 性能优化: 缓存（内存/分布式/响应缓存）；异步化；分页/过滤/排序；压缩；基准与度量。
- 部署与 DevOps: 内置容器发布或 Dockerfile；CI/CD；Azure（App Service/Container Apps）；健康检查与多环境配置。

### Compact Map
- Style -> 命名/格式/注释
- Data -> EF Core/迁移/性能
- Auth -> JWT/OIDC/策略
- Errors -> Middleware/ProblemDetails
- Docs -> Swagger/版本化
- Logs -> Serilog/Telemetry/Correlation
- Tests -> 单测/集成/TDD
- Perf -> 缓存/异步/分页
- DevOps -> 容器/CI/CD/健康检查

### 示例问题（开发者）
1) 在 Minimal API 中统一返回 RFC7807 的最佳做法？
2) EF Core 分页列表如何避免 N+1 并保持可测试性？
3) DataAnnotations 与 FluentValidation 组合的验证流水线怎么设计？
4) 如何同时保护 Controller 与 Minimal API 的 JWT 验证？
5) 使用 Entra ID 时多租户配置要点是什么？
6) Serilog 如何注入 CorrelationId 并在分布式调用链传递？
7) Swagger 中如何为多版本 API 暴露不同的分组与示例？
8) 高并发下的缓存穿透与击穿应对策略？
9) ASP.NET Core 9 Program.cs 常见配置的环境分层方式？
10) 集成测试里如何 Mock 鉴权与外部依赖？

Source: d:\mycode\awesome-copilot\instructions\csharp-ja.instructions.md | Generated: 2025-10-17T00:00:00Z
