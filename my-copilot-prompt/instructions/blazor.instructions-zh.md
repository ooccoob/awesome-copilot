---
描述：“Blazor 组件和应用程序模式”
applyTo: '**/*.razor, **/*.razor.cs, **/*.razor.css'
---

## Blazor 代码风格和结构

- 编写惯用且高效的 Blazor 和 C# 代码。
- 遵循 .NET 和 Blazor 约定。
- 适当使用 Razor 组件进行基于组件的 UI 开发。
- 更喜欢较小组件的内联函数，但将复杂的逻辑分离到代码隐藏或服务类中。
- 应在适用的情况下使用 Async/await 以确保非阻塞 UI 操作。

## 命名约定

- 组件名称、方法名称和公共成员遵循 PascalCase。
- 对私有字段和局部变量使用驼峰命名法。
- 在接口名称前加上“I”前缀（例如 IUserService）。

## Blazor 和 .NET 特定指南

- 利用 Blazor 的组件生命周期内置功能（例如 OnInitializedAsync、OnParametersSetAsync）。
- 通过@bind 有效地使用数据绑定。
- 利用 Blazor 中的服务的依赖注入。
- 按照关注点分离构建 Blazor 组件和服务。
- 始终使用最新版本的 C#，目前使用 C# 13 功能，例如记录类型、模式匹配和全局使用。

## 错误处理和验证

- 对 Blazor 页面和 API 调用实施正确的错误处理。
- 在后端使用日志记录进行错误跟踪，并考虑使用 ErrorBoundary 等工具捕获 Blazor 中的 UI 级别错误。
- 在表单中使用 FluentValidation 或 DataAnnotations 实现验证。

## Blazor API 和性能优化

- 根据项目要求优化使用 Blazor 服务器端或 WebAssembly。
- 对可能阻塞主线程的 API 调用或 UI 操作使用异步方法 (async/await)。
- 通过减少不必要的渲染并有效使用 StateHasChanged() 来优化 Razor 组件。
- 除非必要，否则可以通过避免重新渲染来最小化组件渲染树，并在适当的情况下使用 ShouldRender() 。
- 使用 EventCallbacks 有效地处理用户交互，在触发事件时仅传递最少的数据。

## 缓存策略

- 对常用数据实施内存缓存，尤其是 Blazor Server 应用程序。使用 IMemoryCache 实现轻量级缓存解决方案。
- 对于 Blazor WebAssembly，利用 localStorage 或 sessionStorage 缓存用户会话之间的应用程序状态。
- 对于需要跨多个用户或客户端共享状态的大型应用程序，请考虑分布式缓存策略（例如 Redis 或 SQL Server 缓存）。
- 通过存储响应来缓存 API 调用，以避免数据不太可能发生变化时的冗余调用，从而改善用户体验。

## 状态管理库

- 使用 Blazor 的内置级联参数和事件回调来跨组件共享基本状态。
- 当应用程序变得越来越复杂时，使用 Fluxor 或 BlazorState 等库实施高级状态管理解决方案。
- 对于 Blazor WebAssembly 中的客户端状态持久性，请考虑使用 Blazored.LocalStorage 或 Blazored.SessionStorage 来维护页面重新加载之间的状态。
- 对于服务器端 Blazor，使用 Scoped Services 和 StateContainer 模式来管理用户会话中的状态，同时最大限度地减少重新渲染。

## API设计与集成

- 使用 HttpClient 或其他适当的服务与外部 API 或您自己的后端进行通信。
- 使用 try-catch 实现 API 调用的错误处理，并在 UI 中提供正确的用户反馈。

## 在 Visual Studio 中测试和调试

- 所有单元测试和集成测试都应在 Visual Studio Enterprise 中完成。
- 使用 xUnit、NUnit 或 MSTest 测试 Blazor 组件和服务。
- 在测试期间使用 Moq 或 NSubstitute 模拟依赖关系。
- 使用浏览器开发人员工具和 Visual Studio 的后端和服务器端问题调试工具来调试 Blazor UI 问题。
- 对于性能分析和优化，请依靠 Visual Studio 的诊断工具。

## 安全与认证

- 必要时使用 ASP.NET Identity 或 JWT 令牌进行 API 身份验证，在 Blazor 应用程序中实现身份验证和授权。
- 对所有 Web 通信使用 HTTPS，并确保实施正确的 CORS 策略。

## API 文档和 Swagger

- 使用 Swagger/OpenAPI 获取后端 API 服务的 API 文档。
- 确保模型和 API 方法的 XML 文档，以增强 Swagger 文档。
