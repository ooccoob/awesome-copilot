---
description: "构建 C# 应用程序的指南"
applyTo: "**/*.cs"
---

# C# 开发

## C# 指南

- 始终使用最新版本的 C#，目前为 C# 13。
- 为每个函数编写清晰简明的注释。

## 通用指南

- 仅在有高度信心时才对代码变更提出建议。
- 编写易于维护的代码，并注释设计决策原因。
- 处理边界情况并编写清晰的异常处理。
- 对于库或外部依赖，在注释中说明其用途和目的。

## 命名规范

- 组件名、方法名和公共成员使用 PascalCase。
- 私有字段和局部变量使用 camelCase。
- 接口名以 "I" 开头（如 IUserService）。

## 格式化

- 应用 `.editorconfig` 中定义的代码格式风格。
- 优先使用文件作用域命名空间声明和单行 using 指令。
- 在任何代码块（如 `if`、`for`、`while`、`foreach`、`using`、`try` 等）的大括号前插入换行。
- 方法的最终 return 语句应单独成行。
- 尽可能使用模式匹配和 switch 表达式。
- 使用 `nameof` 替代字符串字面量引用成员名。
- 为所有公共 API 创建 XML 文档注释，必要时包含 `<example>` 和 `<code>`。

## 项目设置与结构

- 指导用户使用合适模板创建新 .NET 项目。
- 解释每个生成文件和文件夹的用途，帮助理解项目结构。
- 演示如何用特性文件夹或领域驱动设计组织代码。
- 展示模型、服务和数据访问层的关注点分离。
- 讲解 ASP.NET Core 9 中 Program.cs 和配置系统，包括环境特定设置。

## 可空引用类型

- 声明变量时默认非空，并在入口处检查 `null`。
- 始终用 `is null` 或 `is not null`，不要用 `== null` 或 `!= null`。
- 信任 C# 的空注解，类型系统已保证非空时无需额外检查。

## 数据访问模式

- 指导用 Entity Framework Core 实现数据访问层。
- 讲解开发和生产环境下 SQL Server、SQLite、内存数据库等选项。
- 演示仓储模式实现及其适用场景。
- 展示数据库迁移和数据填充的实现。
- 讲解高效查询模式，避免常见性能问题。

## 认证与授权

- 指导用 JWT Bearer 实现认证。
- 讲解 OAuth 2.0 和 OpenID Connect 在 ASP.NET Core 中的应用。
- 展示基于角色和策略的授权实现。
- 演示与 Microsoft Entra ID（原 Azure AD）集成。
- 讲解如何统一保护控制器和 Minimal API。

## 校验与错误处理

- 指导用数据注解和 FluentValidation 实现模型校验。
- 讲解校验管道及自定义校验响应。
- 演示用中间件实现全局异常处理。
- 展示如何创建一致的 API 错误响应。
- 讲解 RFC 7807 问题详情标准化错误响应实现。

## API 版本管理与文档

- 指导实现和讲解 API 版本管理策略。
- 演示用 Swagger/OpenAPI 生成文档。
- 展示如何为端点、参数、响应和认证编写文档。
- 讲解控制器和 Minimal API 的版本管理。
- 指导创建有助于使用者的 API 文档。

## 日志与监控

- 指导用 Serilog 或其他提供程序实现结构化日志。
- 讲解日志级别及其适用场景。
- 演示与 Application Insights 集成收集遥测。
- 展示如何实现自定义遥测和请求跟踪相关 ID。
- 讲解如何监控 API 性能、错误和使用模式。

## 测试

- 始终为应用关键路径编写测试用例。
- 指导创建单元测试。
- 不要添加 "Act"、"Arrange" 或 "Assert" 注释。
- 测试方法名和大小写应与现有风格一致。
- 讲解 API 端点集成测试方法。
- 演示如何 mock 依赖实现高效测试。
- 展示认证与授权逻辑的测试方法。
- 讲解测试驱动开发在 API 开发中的应用。

## 性能优化

- 指导实现缓存策略（内存、分布式、响应缓存）。
- 讲解异步编程模式及其对 API 性能的意义。
- 演示大数据集的分页、过滤和排序。
- 展示压缩和其他性能优化方法。
- 讲解如何测量和基准测试 API 性能。

## 部署与 DevOps

- 指导用 .NET 内置容器支持容器化 API（`dotnet publish --os linux --arch x64 -p:PublishProfile=DefaultContainer`）。
- 讲解手动 Dockerfile 与 .NET 容器发布的区别。
- 讲解 .NET 应用的 CI/CD 流水线。
- 演示部署到 Azure App Service、Azure Container Apps 或其他托管选项。
- 展示健康检查和就绪探针实现。
- 讲解不同部署阶段的环境特定配置。

---

**免责声明**：本文档由[GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot)本地化。因此，可能包含错误。如果您发现任何不适当的翻译或错误，请创建一个[议题](../../issues)。
