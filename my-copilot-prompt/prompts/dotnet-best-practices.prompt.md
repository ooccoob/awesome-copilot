---
agent: 'agent'
description: 'Ensure .NET/C# code meets best practices for the solution/project.'
---
# .NET/C# 最佳实践

您的任务是确保 ${selection} 中的 .NET/C# 代码符合特定于该解决方案/项目的最佳实践。这包括：

## 文档和结构

- 为所有公共类、接口、方法和属性创建全面的 XML 文档注释
- 在XML注释中包含参数描述和返回值描述
- 遵循既定的命名空间结构：{Core|Console|App|Service}.{Feature}

## 设计模式与架构

- 使用主要构造函数语法进行依赖项注入（例如，`public class MyClass(IDependency dependency)`）
- 使用通用基类（例如 `CommandHandler<TOptions>`）实现命令处理程序模式
- 使用具有明确命名约定的接口隔离（接口前缀带有“I”）
- 遵循工厂模式来创建复杂的对象。

## 依赖注入和服务

- 通过 ArgumentNullException 使用构造函数依赖注入和 null 检查
- 注册具有适当生命周期的服务（Singleton、Scoped、Transient）
- 使用 Microsoft.Extensions.DependencyInjection 模式
- 实现可测试性服务接口

## 资源管理和本地化

- 使用 ResourceManager 获取本地化消息和错误字符串
- 单独的 LogMessages 和 ErrorMessages 资源文件
- 通过 `_resourceManager.GetString("MessageKey")` 访问资源

## 异步/等待模式

- 对所有 I/O 操作和长时间运行的任务使用 async/await
- 从异步方法返回 Task 或 Task<T>
- 在适当的情况下使用ConfigureAwait(false)
- 正确处理异步异常

## 检测标准

- 使用 MSTest 框架和 FluentAssertions 进行断言
- 遵循 AAA 模式（安排、行动、断言）
- 使用 Moq 来模拟依赖项
- 测试成功和失败场景
- 包括空参数验证测试

## 配置与设置

- 使用带有数据注释的强类型配置类
- 实现验证属性（必需、NotEmptyOrWhitespace）
- 使用 IConfiguration 绑定进行设置
- 支持appsettings.json配置文件

## 语义内核与人工智能集成

- 使用 Microsoft.SemanticKernel 进行 AI 操作
- 实施正确的内核配置和服务注册
- 处理 AI 模型设置（ChatCompletion、Embedding 等）
- 使用结构化输出模式实现可靠的 AI 响应

## 错误处理和日志记录

- 通过 Microsoft.Extensions.Logging 使用结构化日志记录
- 包括具有有意义上下文的范围日志记录
- 使用描述性消息引发特定异常
- 对预期的失败场景使用 try-catch 块

## 性能与安全

- 在适用的情况下使用 C# 12+ 功能和 .NET 8 优化
- 实施适当的输入验证和清理
- 使用参数化查询进行数据库操作
- 遵循 AI/ML 操作的安全编码实践

## 代码质量

- 确保遵守 SOLID 原则
- 通过基类和实用程序避免代码重复
- 使用反映领域概念的有意义的名称
- 保持方法的重点和凝聚力
- 实施适当的资源处置模式
