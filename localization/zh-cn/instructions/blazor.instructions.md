---
description: "Blazor 组件与应用开发模式"
applyTo: "**/*.razor, **/*.razor.cs, **/*.razor.css"
---

## Blazor 代码风格与结构

- 编写地道高效的 Blazor 与 C# 代码
- 遵循 .NET 与 Blazor 规范
- 合理使用 Razor 组件实现组件化 UI
- 小型组件可用内联函数，复杂逻辑应拆分到 code-behind 或服务类
- 适用场景下统一用 async/await，确保 UI 非阻塞

## 命名规范

- 组件名、方法名、公有成员用 PascalCase
- 私有字段与局部变量用 camelCase
- 接口名加前缀 "I"（如 IUserService）

## Blazor 与 .NET 专项建议

- 利用 Blazor 内置生命周期（如 OnInitializedAsync, OnParametersSetAsync）
- 有效使用 @bind 实现数据绑定
- 服务注入用 Blazor 的依赖注入机制
- 组件与服务结构遵循关注点分离
- 始终用最新 C# 版本（如 C# 13 的 record、模式匹配、全局 using 等）

## 错误处理与校验

- Blazor 页面与 API 调用需实现健壮的错误处理
- 后端用日志跟踪错误，前端可用 ErrorBoundary 捕获 UI 级错误
- 表单校验用 FluentValidation 或 DataAnnotations

## Blazor API 与性能优化

- 根据项目需求合理选择 Blazor Server 或 WebAssembly
- API 调用与 UI 可能阻塞主线程的操作均用 async/await
- 优化 Razor 组件，减少不必要的渲染，合理用 StateHasChanged()
- 用 ShouldRender() 控制渲染，避免无谓重渲
- 事件处理用 EventCallbacks，传递最小必要数据

## 缓存策略

- Blazor Server 推荐用 IMemoryCache 实现内存缓存
- Blazor WebAssembly 可用 localStorage 或 sessionStorage 缓存应用状态
- 大型应用需共享状态可用分布式缓存（如 Redis、SQL Server Cache）
- API 调用结果可缓存，避免重复请求，提升体验

## 状态管理库

- 跨组件状态共享用 Blazor 内置 Cascading Parameters 与 EventCallbacks
- 复杂应用可用 Fluxor、BlazorState 等库实现高级状态管理
- Blazor WebAssembly 客户端状态持久化可用 Blazored.LocalStorage 或 Blazored.SessionStorage
- Blazor Server 端用 Scoped Services 与 StateContainer 模式管理会话内状态，减少重渲

## API 设计与集成

- 用 HttpClient 或其他服务与后端/外部 API 通信
- API 调用用 try-catch 错误处理，UI 需合理反馈

## Visual Studio 测试与调试

- 单元与集成测试均在 Visual Studio Enterprise 完成
- 组件与服务测试可用 xUnit、NUnit 或 MSTest
- Mock 依赖推荐用 Moq 或 NSubstitute
- UI 问题用浏览器开发者工具与 Visual Studio 调试工具定位
- 性能分析与优化用 Visual Studio 诊断工具

## 安全与认证

- 需认证时用 ASP.NET Identity 或 JWT 实现认证与授权
- 所有 Web 通信用 HTTPS，配置合理 CORS 策略

## API 文档与 Swagger

- 后端 API 文档用 Swagger/OpenAPI
- 模型与 API 方法加 XML 注释，提升 Swagger 文档质量

---

**免责声明**：本文档由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 本地化。如有错误或不当之处，欢迎通过 [issues](../../issues) 反馈。
