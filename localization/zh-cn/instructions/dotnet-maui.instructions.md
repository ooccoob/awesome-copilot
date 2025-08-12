---
description: ".NET MAUI 组件与应用开发模式"
applyTo: "**/*.xaml, **/*.cs"
---

# .NET MAUI

## .NET MAUI 代码风格与结构

- 编写符合 .NET MAUI 和 C# 规范的高效代码。
- 遵循 .NET 及 .NET MAUI 约定。
- 小型组件可用内联函数，复杂逻辑应拆分到 code-behind 或服务类。
- UI 操作需用 async/await 保证非阻塞。

## 命名规范

- 组件名、方法名和公有成员用 PascalCase。
- 私有字段和局部变量用 camelCase。
- 接口名加前缀 "I"（如 IUserService）。

## .NET MAUI 及 .NET 通用建议

- 利用 .NET MAUI 内置生命周期方法（如 OnAppearing, OnDisappearing）。
- 有效使用数据绑定（{Binding}）。
- 组件与服务结构应遵循关注点分离。
- 始终使用最新 C# 版本（如 C# 13），充分利用 record、模式匹配、全局 using 等特性。

## 错误处理与校验

- 页面和 API 调用需有完善的错误处理。
- 后端用日志记录错误，前端可用 MAUI Community Toolkit 的 Logger 捕获 UI 层异常。
- 表单校验可用 FluentValidation 或 DataAnnotations。

## MAUI API 与性能优化

- 利用 MAUI 生命周期钩子（如 OnAppearing, OnDisappearing）。
- API 调用或可能阻塞 UI 的操作应使用异步方法（async/await）。
- 通过高效使用 OnPropertyChanged() 减少不必要的渲染。
- 用 BatchBegin()/BatchCommit() 控制批量渲染，避免无谓刷新。

## 缓存策略

- 频繁数据建议用内存缓存（IMemoryCache）。
- 大型应用需考虑分布式缓存（如 Redis、SQL Server Cache）。
- API 调用可缓存响应，减少重复请求，提升体验。

## 状态管理库

- 用依赖注入和 MAUI Community Toolkit 实现组件间状态共享。

## API 设计与集成

- 用 HttpClient 或其他服务访问外部 API 或后端。
- API 调用需 try-catch 错误处理，并在 UI 端友好提示。

## 测试与调试

- 组件与服务建议用 xUnit、NUnit 或 MSTest 测试。
- 依赖可用 Moq 或 NSubstitute mock。

## 安全与认证

- 需要时实现认证与授权，API 认证建议用 OAuth 或 JWT。
- 所有 Web 通信用 HTTPS，配置好 CORS。

## API 文档与 Swagger

- 后端 API 建议用 Swagger/OpenAPI 生成文档。
- 模型与 API 方法需有 XML 注释以增强 Swagger 文档。

---

> 本文档为自动翻译，仅供参考。如有歧义请以英文原文为准。

```instructions
---
description: '.NET MAUI 组件与应用模式'
applyTo: '**/*.xaml, **/*.cs'
---

# .NET MAUI

## .NET MAUI 代码风格与结构

- 编写符合规范且高效的 .NET MAUI 和 C# 代码。
- 遵循 .NET 及 .NET MAUI 的约定。
- 小型组件可用内联函数，复杂逻辑应拆分到 code-behind 或服务类。
- 适用时应使用 async/await，确保 UI 操作非阻塞。

## 命名规范

- 组件名、方法名和公有成员使用 PascalCase。
- 私有字段和局部变量使用 camelCase。
- 接口名以 "I" 前缀（如 IUserService）。

## .NET MAUI 及 .NET 专属指南

- 利用 .NET MAUI 内置的组件生命周期（如 OnAppearing, OnDisappearing）。
- 有效使用 {Binding} 进行数据绑定。
- 组件和服务结构应遵循关注点分离原则。
- 始终使用最新 C# 版本（如 C# 13 的 record、模式匹配、全局 using）。

## 错误处理与校验

- 为 .NET MAUI 页面和 API 调用实现适当的错误处理。
- 后端用日志跟踪错误，前端可用 MAUI Community Toolkit 的 Logger 捕获 UI 层错误。
- 表单校验建议用 FluentValidation 或 DataAnnotations。

## MAUI API 与性能优化

- 利用 MAUI 内置生命周期（如 OnAppearing, OnDisappearing）。
- API 调用或可能阻塞主线程的 UI 操作应使用异步（async/await）。
- 通过减少不必要的渲染和高效使用 OnPropertyChanged() 优化组件。
- 通过 BatchBegin() 和 BatchCommit() 控制渲染，避免无谓重渲。

## 缓存策略

- 对常用数据实现内存缓存，MAUI 应用可用 IMemoryCache。
- 大型应用需多用户共享状态时，考虑分布式缓存（如 Redis、SQL Server Cache）。
- 对不常变的数据缓存 API 响应，减少冗余调用，提升体验。

## 状态管理库

- 使用依赖注入和 .NET MAUI Community Toolkit 实现组件间状态共享。

## API 设计与集成

- 用 HttpClient 或其他服务与外部 API 或后端通信。
- API 调用用 try-catch 做错误处理，并在 UI 给予用户反馈。

## 测试与调试

- 用 xUnit、NUnit 或 MSTest 测试组件和服务。
- Mock 依赖可用 Moq 或 NSubstitute。

## 安全与认证

- 需要时在 MAUI 应用实现认证与授权，API 认证用 OAuth 或 JWT。
- 所有 Web 通信用 HTTPS，确保 CORS 策略正确。

## API 文档与 Swagger

- 后端 API 服务用 Swagger/OpenAPI 生成文档。
- 为模型和 API 方法添加 XML 注释，增强 Swagger 文档。

---

> 本文件为自动翻译，仅供参考。如有歧义请以英文原文为准。
```
