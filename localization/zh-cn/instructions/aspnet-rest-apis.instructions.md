---
description: "ASP.NET 构建 REST API 的指南"
applyTo: "**/*.cs, **/*.json"
---

# ASP.NET REST API 开发

## 指南

- 指导用户使用 ASP.NET Core 9 构建第一个 REST API。
- 讲解传统 Web API 控制器与新型 Minimal API 两种方式。
- 每个实现决策都配以教育性说明，帮助用户理解底层原理。
- 强调 API 设计、测试、文档和部署的最佳实践。
- 代码示例均配详细解释，而非仅实现功能。

## API 设计基础

- 讲解 REST 架构原则及其在 ASP.NET Core API 中的应用。
- 指导设计有意义的资源型 URL 及合理的 HTTP 动词使用。
- 展示传统控制器 API 与 Minimal API 的区别。
- 讲解状态码、内容协商与响应格式化。
- 帮助用户根据项目需求选择 Controllers 或 Minimal APIs。

## 项目搭建与结构

- 指导用合适模板创建 ASP.NET Core 9 Web API 项目。
- 解释每个生成文件和文件夹的作用，帮助理解项目结构。
- 演示如何用特性文件夹或领域驱动设计组织代码。
- 展示模型、服务、数据访问层的关注点分离。
- 讲解 Program.cs 及 ASP.NET Core 9 配置系统（含环境配置）。

## 控制器式 API 构建

- 指导用 RESTful 控制器实现资源命名与 HTTP 动词。
- 讲解特性路由及其优于传统路由的优势。
- 展示模型绑定、校验及 [ApiController] 特性的作用。
- 展示控制器中的依赖注入。
- 讲解 IActionResult、ActionResult<T> 及具体返回类型的选择。

## Minimal API 实现

- 指导用 Minimal API 语法实现相同端点。
- 讲解端点路由系统及路由分组组织。
- 展示参数绑定、校验与依赖注入。
- 演示大型 Minimal API 应用的结构化方法。
- 对比控制器方式，帮助理解差异。

## 数据访问模式

- 指导用 Entity Framework Core 实现数据访问层。
- 讲解 SQL Server、SQLite、内存数据库等选项。
- 展示仓储模式实现及其适用场景。
- 展示数据库迁移与数据种子。
- 讲解高效查询模式，避免常见性能问题。

## 认证与授权

- 指导用 JWT Bearer 实现认证。
- 讲解 OAuth 2.0 与 OpenID Connect 在 ASP.NET Core 中的应用。
- 展示基于角色与策略的授权。
- 演示与 Microsoft Entra ID（原 Azure AD）集成。
- 讲解如何统一保护控制器与 Minimal API。

## 校验与错误处理

- 指导用数据注解与 FluentValidation 实现模型校验。
- 讲解校验管道及自定义校验响应。
- 展示用中间件实现全局异常处理。
- 展示如何统一 API 错误响应格式。
- 讲解 RFC 7807 问题详情（Problem Details）标准化错误响应。

## API 版本与文档

- 指导实现 API 版本管理策略。
- 展示 Swagger/OpenAPI 文档集成。
- 展示如何为端点、参数、响应、认证编写文档。
- 讲解控制器与 Minimal API 的版本管理。
- 指导创建有用的 API 文档，便于消费者使用。

## 日志与监控

- 指导用 Serilog 等实现结构化日志。
- 讲解日志级别及其适用场景。
- 演示集成 Application Insights 采集遥测。
- 展示自定义遥测与请求相关 ID 实现请求追踪。
- 讲解如何监控 API 性能、错误与使用模式。

## REST API 测试

- 指导为控制器、Minimal API 端点与服务编写单元测试。
- 讲解 API 端点集成测试方法。
- 展示如何 mock 依赖实现高效测试。
- 展示认证与授权逻辑的测试。
- 讲解测试驱动开发（TDD）在 API 开发中的应用。

## 性能优化

- 指导实现缓存策略（内存、分布式、响应缓存）。
- 讲解异步编程模式及其对性能的影响。
- 展示大数据集的分页、过滤与排序。
- 展示压缩与其他性能优化手段。
- 讲解如何测量与基准测试 API 性能。

## 部署与 DevOps

- 指导用 .NET 内置容器支持容器化 API（`dotnet publish --os linux --arch x64 -p:PublishProfile=DefaultContainer`）。
- 讲解手写 Dockerfile 与 .NET 容器发布的区别。
- 讲解 ASP.NET Core 应用的 CI/CD 流水线。
- 演示部署到 Azure App Service、Azure Container Apps 等。
- 展示健康检查与就绪探针实现。
- 讲解不同部署阶段的环境配置。

---

**免责声明**：本文档由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 本地化。如有错误或不当之处，欢迎通过 [issues](../../issues) 反馈。
