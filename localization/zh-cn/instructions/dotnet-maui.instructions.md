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
