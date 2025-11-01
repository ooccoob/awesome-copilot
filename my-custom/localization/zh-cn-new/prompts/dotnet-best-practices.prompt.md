---
mode: 'agent'
description: '确保.NET/C#代码符合解决方案/项目的最佳实践。'
---
# .NET/C#最佳实践

您的任务是确保${selection}中的.NET/C#代码符合此解决方案/项目特定的最佳实践。这包括：

## 文档和结构

- 为所有公共类、接口、方法和属性创建全面的XML文档注释
- 在XML注释中包含参数描述和返回值描述
- 遵循已建立的命名空间结构：{Core|Console|App|Service}.{Feature}

## 设计模式和架构

- 对依赖注入使用主构造函数语法（例如，`public class MyClass(IDependency dependency)`）
- 使用泛型基类实现命令处理器模式（例如，`CommandHandler<TOptions>`）
- 使用接口隔离和清晰的命名约定（接口前缀为'I'）
- 对复杂对象创建遵循工厂模式。

## 依赖注入和服务

- 使用构造函数依赖注入并通过ArgumentNullException进行null检查
- 使用适当生命周期（Singleton、Scoped、Transient）注册服务
- 使用Microsoft.Extensions.DependencyInjection模式
- 为可测试性实现服务接口

## 资源管理和本地化

- 使用ResourceManager进行本地化消息和错误字符串
- 分离LogMessages和ErrorMessages资源文件
- 通过`_resourceManager.GetString("MessageKey")`访问资源

## 异步/等待模式

- 对所有I/O操作和长时间运行的任务使用async/await
- 从异步方法返回Task或Task<T>
- 在适当时使用ConfigureAwait(false)
- 正确处理异步异常

## 测试标准

- 使用MSTest框架配合FluentAssertions进行断言
- 遵循AAA模式（Arrange、Act、Assert）
- 使用Moq模拟依赖项
- 测试成功和失败场景
- 包括null参数验证测试

## 配置和设置

- 使用带数据注解的强类型配置类
- 实现验证属性（Required、NotEmptyOrWhitespace）
- 对设置使用IConfiguration绑定
- 支持appsettings.json配置文件

## 语义内核和AI集成

- 使用Microsoft.SemanticKernel进行AI操作
- 实现正确的内核配置和服务注册
- 处理AI模型设置（ChatCompletion、Embedding等）
- 使用结构化输出模式获得可靠的AI响应

## 错误处理和日志记录

- 使用Microsoft.Extensions.Logging进行结构化日志记录
- 包含有意义上下文的作用域日志记录
- 抛出具有描述性消息的特定异常
- 对预期失败场景使用try-catch块

## 性能和安全

- 在适用时使用C# 12+功能和.NET 8优化
- 实现适当的输入验证和清理
- 对数据库操作使用参数化查询
- 对AI/ML操作遵循安全编码实践

## 代码质量

- 确保SOLID原则合规
- 通过基类和工具避免代码重复
- 使用反映领域概念的有意义名称
- 保持方法专注和内聚
- 为资源实现适当的释放模式