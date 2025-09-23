---
mode: "agent"
description: "确保 ${selection} 中的 .NET/C# 代码符合该解决方案/项目的最佳实践。"
---

# .NET/C# 最佳实践

你的任务是确保 ${selection} 中的 .NET/C# 代码符合本解决方案/项目的最佳实践要求。这包括：

## 文档与结构

- 为所有公有类型、接口、方法、属性编写完整的 XML 文档注释
- 在 XML 注释中包含参数与返回值说明
- 遵循既定命名空间结构：{Core|Console|App|Service}.{Feature}

## 设计模式与架构

- 使用主构造函数语法进行依赖注入（例如 `public class MyClass(IDependency dependency)`）
- 采用命令处理器（Command Handler）模式与通用基类（如 `CommandHandler<TOptions>`）
- 接口分离原则，接口命名以 I 前缀
- 复杂对象创建遵循工厂模式

## 依赖注入与服务

- 构造函数注入并进行空值校验（`ArgumentNullException`）
- 按生命周期注册服务（Singleton/Scoped/Transient）
- 使用 Microsoft.Extensions.DependencyInjection 模式
- 通过接口抽象提升可测试性

## 资源管理与本地化

- 使用 ResourceManager 管理本地化消息与错误字符串
- 区分 LogMessages 与 ErrorMessages 资源文件
- 通过 `_resourceManager.GetString("MessageKey")` 访问资源

## Async/Await 模式

- 对所有 I/O 与长耗时任务使用 async/await
- 异步方法返回 Task 或 Task<T>
- 适当场景使用 `ConfigureAwait(false)`
- 正确处理异步异常

## 测试标准

- 使用 MSTest，断言建议采用 FluentAssertions
- 遵循 AAA（Arrange, Act, Assert）
- 使用 Moq 对依赖进行 Mock
- 同时覆盖成功与失败路径
- 包含空参数验证类测试

## 配置与设置

- 使用强类型配置类并添加数据注解
- 使用验证属性（如 Required、NotEmptyOrWhitespace）
- 使用 IConfiguration 进行配置绑定
- 支持 appsettings.json 配置文件

## Semantic Kernel 与 AI 集成

- 使用 Microsoft.SemanticKernel 处理 AI 操作
- 实现内核配置与服务注册
- 处理模型设置（ChatCompletion、Embedding 等）
- 使用结构化输出模式，提升响应可靠性

## 错误处理与日志

- 使用 Microsoft.Extensions.Logging 进行结构化日志
- 使用作用域日志提供上下文
- 抛出具体异常并提供清晰消息
- 对可预期失败场景使用 try-catch

## 性能与安全

- 在适用处使用 C# 12+ 与 .NET 8 优化
- 实施输入校验与清理
- 数据库操作使用参数化查询（防注入）
- 遵循安全编码实践（含 AI/ML 操作）

## 代码质量

- 遵循 SOLID 原则
- 避免重复，通过基类/工具类复用
- 命名应表达领域含义
- 保持方法内聚、聚焦
- 正确释放资源（IDisposable/AsyncDisposable）

```

```
