---
description: 'Blazor 组件和应用程序模式'
applyTo: '**/*.razor, **/*.razor.cs, **/*.razor.css'
---

## Blazor 代码风格和结构

- 编写地道且高效的 Blazor 和 C# 代码。
- 遵循 .NET 和 Blazor 约定。
- 适当使用 Razor 组件进行基于组件的 UI 开发。
- 对于较小的组件首选内联函数，但将复杂逻辑分离到代码隐藏或服务类中。
- 在适用的地方使用 Async/await 以确保非阻塞 UI 操作。

## 命名约定

- 组件名称、方法名称和公共成员使用 PascalCase（帕斯卡命名法）。
- 私有字段和局部变量使用 camelCase（驼峰命名法）。
- 接口名称前缀为 "I"（例如，IUserService）。

## Blazor 和 .NET 特定指导原则

- 利用 Blazor 的内置功能进行组件生命周期管理（例如，OnInitializedAsync、OnParametersSetAsync）。
- 有效地使用 @bind 进行数据绑定。
- 在 Blazor 中利用依赖注入来获取服务。
- 遵循关注点分离原则构建 Blazor 组件和服务。
- 始终使用最新版本的 C#，目前使用 C# 13 特性，如记录类型、模式匹配和全局 using。

## 错误处理和验证

- 为 Blazor 页面和 API 调用实施适当的错误处理。
- 在后端使用日志记录进行错误跟踪，并考虑使用 ErrorBoundary 等工具在 Blazor 中捕获 UI 级别的错误。
- 在表单中使用 FluentValidation 或 DataAnnotations 实施验证。

## Blazor API 和性能优化

- 根据项目需求最优地使用 Blazor 服务端或 WebAssembly。
- 对可能阻塞主线程的 API 调用或 UI 操作使用异步方法（async/await）。
- 通过减少不必要的渲染和高效使用 StateHasChanged() 来优化 Razor 组件。
- 通过避免不必要的重新渲染来最小化组件渲染树，在适当的地方使用 ShouldRender()。
- 使用 EventCallbacks 高效处理用户交互，触发事件时仅传递最小数据。

## 缓存策略

- 对频繁使用的数据实施内存缓存，特别是对于 Blazor Server 应用程序。使用 IMemoryCache 进行轻量级缓存解决方案。
- 对于 Blazor WebAssembly，利用 localStorage 或 sessionStorage 在用户会话之间缓存应用程序状态。
- 对于需要在多个用户或客户端之间共享状态的大型应用程序，考虑分布式缓存策略（如 Redis 或 SQL Server 缓存）。
- 通过存储响应来缓存 API 调用，避免在数据不太可能发生变化时进行冗余调用，从而改善用户体验。

## 状态管理库

- 使用 Blazor 内置的级联参数和 EventCallbacks 在组件间进行基本状态共享。
- 当应用程序复杂度增长时，使用 Fluxor 或 BlazorState 等库实施高级状态管理解决方案。
- 对于 Blazor WebAssembly 中的客户端状态持久化，考虑使用 Blazored.LocalStorage 或 Blazored.SessionStorage 在页面重新加载之间维护状态。
- 对于服务端 Blazor，使用作用域服务和 StateContainer 模式来管理用户会话内的状态，同时最小化重新渲染。

## API 设计和集成

- 使用 HttpClient 或其他适当的服务与外部 API 或您自己的后端通信。
- 使用 try-catch 为 API 调用实施错误处理，并在 UI 中提供适当的用户反馈。

## Visual Studio 中的测试和调试

- 所有单元测试和集成测试都应该在 Visual Studio Enterprise 中进行。
- 使用 xUnit、NUnit 或 MSTest 测试 Blazor 组件和服务。
- 在测试期间使用 Moq 或 NSubstitute 模拟依赖项。
- 使用浏览器开发工具调试 Blazor UI 问题，使用 Visual Studio 的调试工具调试后端和服务端问题。
- 对于性能分析和优化，依赖 Visual Studio 的诊断工具。

## 安全和身份验证

- 在 Blazor 应用程序中实施身份验证和授权，使用 ASP.NET Identity 或 JWT 令牌进行 API 身份验证。
- 对所有 Web 通信使用 HTTPS，并确保实施了适当的 CORS 策略。

## API 文档和 Swagger

- 为您的后端 API 服务使用 Swagger/OpenAPI 进行 API 文档。
- 确保为模型和 API 方法提供 XML 文档以增强 Swagger 文档。