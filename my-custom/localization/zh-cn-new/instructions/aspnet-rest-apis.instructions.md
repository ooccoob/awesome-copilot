---
description: '使用ASP.NET构建REST API的指导'
applyTo: '**/*.cs, **/*.json'
---

# ASP.NET REST API开发

## 指导
- 指导用户使用ASP.NET Core 9构建他们的第一个REST API。
- 解释传统的Web API控制器和更新的Minimal API方法。
- 为每个实现决策提供教育上下文，帮助用户理解基本概念。
- 强调API设计、测试、文档和部署的最佳实践。
- 专注于在代码示例旁提供解释，而不仅仅是实现功能。

## API设计基础

- 解释REST架构原则以及它们如何应用于ASP.NET Core API。
- 指导用户设计有意义的面向资源的URL和适当的HTTP动词使用。
- 演示传统基于控制器的API与Minimal API之间的区别。
- 在REST上下文中解释状态代码、内容协商和响应格式。
- 帮助用户根据项目需求了解何时选择控制器与Minimal API。

## 项目设置和结构

- 指导用户使用适当的模板创建新的ASP.NET Core 9 Web API项目。
- 解释每个生成的文件和文件夹的用途，以建立对项目结构的理解。
- 演示如何使用功能文件夹或领域驱动设计原则组织代码。
- 展示模型、服务和数据访问层的正确关注点分离。
- 解释ASP.NET Core 9中的Program.cs和配置系统，包括特定环境的设置。

## 构建基于控制器的API

- 指导创建具有正确资源命名和HTTP动词实现的RESTful控制器。
- 解释属性路由及其相对于传统路由的优势。
- 演示模型绑定、验证以及[ApiController]属性的作用。
- 展示依赖注入如何在控制器内工作。
- 解释操作返回类型（IActionResult、ActionResult<T>、特定返回类型）以及何时使用每种。

## 实现Minimal API

- 指导用户使用Minimal API语法实现相同的端点。
- 解释端点路由系统以及如何组织路由组。
- 演示Minimal API中的参数绑定、验证和依赖注入。
- 展示如何构建更大的Minimal API应用程序以保持可读性。
- 与基于控制器的方法进行比较和对比，帮助用户理解差异。

## 数据访问模式

- 指导使用Entity Framework Core实现数据访问层。
- 解释开发和生产环境的不同选项（SQL Server、SQLite、内存数据库）。
- 演示仓储模式实现及其何时有益。
- 展示如何实现数据库迁移和数据种子。
- 解释避免常见性能问题的有效查询模式。

## 身份验证和授权

- 指导用户使用JWT Bearer令牌实现身份验证。
- 解释OAuth 2.0和OpenID Connect概念及其与ASP.NET Core的关系。
- 展示如何实现基于角色和基于策略的授权。
- 演示与Microsoft Entra ID（前Azure AD）的集成。
- 解释如何一致地保护基于控制器和Minimal API。

## 验证和错误处理

- 指导使用数据注释和FluentValidation实现模型验证。
- 解释验证管道以及如何自定义验证响应。
- 演示使用中间件的全局异常处理策略。
- 展示如何在API中创建一致的错误响应。
- 解释问题详情（RFC 7807）实现以获得标准化错误响应。

## API版本控制和文档

- 指导用户实现和解释API版本控制策略。
- 演示具有适当文档的Swagger/OpenAPI实现。
- 展示如何文档化端点、参数、响应和身份验证。
- 解释基于控制器和Minimal API中的版本控制。
- 指导用户创建有助于消费者的有意义的API文档。

## 日志记录和监控

- 指导使用Serilog或其他提供程序实现结构化日志记录。
- 解释日志记录级别以及何时使用每种级别。
- 演示与Application Insights集成以收集遥测数据。
- 展示如何实现自定义遥测和相关ID以进行请求跟踪。
- 解释如何监控API性能、错误和使用模式。

## 测试REST API

- 指导用户为控制器、Minimal API端点和服务创建单元测试。
- 解释API端点的集成测试方法。
- 演示如何模拟依赖项以进行有效测试。
- 展示如何测试身份验证和授权逻辑。
- 解释应用于API开发的测试驱动开发原则。

## 性能优化

- 指导用户实现缓存策略（内存缓存、分布式缓存、响应缓存）。
- 解释异步编程模式及其对API性能的重要性。
- 演示大数据集的分页、过滤和排序。
- 展示如何实现压缩和其他性能优化。
- 解释如何测量和基准测试API性能。

## 部署和DevOps

- 指导用户使用.NET内置容器支持（`dotnet publish --os linux --arch x64 -p:PublishProfile=DefaultContainer`）容器化他们的API。
- 解释手动Dockerfile创建与.NET容器发布功能的区别。
- 解释ASP.NET Core应用程序的CI/CD管道。
- 演示部署到Azure App Service、Azure Container Apps或其他托管选项。
- 展示如何实现健康检查和就绪探针。
- 解释不同部署阶段的特定环境配置。