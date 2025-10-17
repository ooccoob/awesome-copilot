## What / When / Why / How
- What: 使用 ASP.NET Core 9 构建 REST API（控制器 vs Minimal API）及其全生命周期实践。
- When: 新建服务/迁移 API/引入鉴权/版本/日志/部署流水线时。
- Why: 清晰资源建模、可测试、可观测、可演进。
- How: 语义化路由与状态码；模型绑定/校验；EF Core 数据访问；JWT/OIDC；版本化+Swagger；Serilog+AI；测试与容器化部署。

## Key points
- 设计：REST 资源路径/HTTP 动词/内容协商/状态码；控制器与 Minimal API 的取舍与分组路由。
- 项目结构：特性文件夹/DDD；Program.cs 启动与配置（环境）。
- 控制器：属性路由；[ApiController]；DI；返回类型 IActionResult/ActionResult<T>/具体类型选择。
- Minimal API：端点/路由组；参数绑定与验证；组织大型应用保持可读。
- 数据：EF Core（SQL/SQLite/InMemory）；仓储可选；迁移/种子；高效查询避免陷阱。
- 安全：JWT Bearer；OAuth2/OIDC；策略与角色；与 Entra ID 集成；控制器与 Minimal API 一致加固。
- 错误：数据注解/FluentValidation；全局异常中间件；ProblemDetails(RFC7807)。
- 文档：API Versioning；Swagger/OpenAPI 全面注释与授权说明。
- 观察：Serilog 结构化日志；Application Insights；相关 ID；性能监控。
- 测试：单元/集成/模拟依赖；鉴权逻辑测试；TDD。 
- DevOps：容器化（dotnet publish DefaultContainer vs Dockerfile）；CI/CD；健康检查；环境配置。

## Compact map
- 设计/路由/状态码
- 控制器 vs Minimal
- EF Core/迁移
- JWT/OIDC/策略
- 异常/ProblemDetails
- 版本/Swagger
- 日志/遥测
- 测试/CI/CD/容器

## Example questions (10+)
- Minimal API 如何组织路由组并共享过滤/中间件？
- 何时选择 ActionResult<T> 而不是 IActionResult？
- EF Core 查询优化与跟踪/不跟踪的取舍？
- 全局异常处理中如何标准化 ProblemDetails？
- 如何为多版本 API 同时生成 Swagger？
- Entra ID 与本地 JWT 配置差异与多环境切换？
- FluentValidation 如何接入 Minimal API 参数校验？
- 集成测试如何模拟 JWT 并测试授权策略？
- DefaultContainer 发布与自定义 Dockerfile 的权衡？
- 分层结构（服务/仓储）对小项目是否过度设计？
- Application Insights 中如何做端到端相关性？

—
Source: d:\mycode\awesome-copilot\instructions\aspnet-rest-apis.instructions.md | Generated: {{timestamp}}
