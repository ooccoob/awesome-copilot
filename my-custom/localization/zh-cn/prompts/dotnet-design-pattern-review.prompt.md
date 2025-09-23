---
mode: "agent"
description: "审查 C#/.NET 代码中的设计模式实现并提出改进建议。"
---

# .NET/C# 设计模式评审

审查 ${selection} 中的 C#/.NET 代码的设计模式实现情况，为该解决方案/项目提出改进建议。不要直接修改代码，只提供评审意见。

## 必备设计模式

- **命令模式（Command Pattern）**：通用基类（`CommandHandler<TOptions>`）、`ICommandHandler<TOptions>` 接口、`CommandHandlerOptions` 继承、静态 `SetupCommand(IHost host)` 方法
- **工厂模式（Factory Pattern）**：复杂对象创建与服务提供者集成
- **依赖注入（DI）**：主构造函数语法、`ArgumentNullException` 空检查、接口抽象、合适的服务生命周期
- **仓储模式（Repository Pattern）**：异步数据访问接口、对连接等资源的提供者抽象
- **提供者模式（Provider Pattern）**：外部服务（数据库、AI 等）抽象、清晰契约与配置处理
- **资源模式（Resource Pattern）**：使用 ResourceManager 管理本地化消息，拆分 .resx（LogMessages、ErrorMessages）

## 评审清单

- **设计模式**：识别已用模式。Command Handler、Factory、Provider、Repository 是否正确实现？是否缺少有益模式？
- **架构**：是否遵循命名空间约定（`{Core|Console|App|Service}.{Feature}`）？Core/Console 分层是否清晰？模块化与可读性如何？
- **.NET 最佳实践**：主构造函数、async/await 与 Task 返回、ResourceManager 使用、结构化日志、强类型配置是否到位？
- **GoF 模式**：Command、Factory、Template Method、Strategy 等是否合理落地？
- **SOLID 原则**：是否存在 SRP/OCP/LSP/ISP/DIP 违规？
- **性能**：async/await 使用是否合理，资源释放是否正确，`ConfigureAwait(false)`、并行化机会？
- **可维护性**：关注关注点分离、一致的错误处理、正确的配置用法？
- **可测试性**：依赖是否抽象为接口、组件可 Mock、异步可测试性、AAA 模式兼容？
- **安全**：输入校验、凭据安全、参数化查询、安全的异常处理？
- **文档**：公共 API 的 XML 注释、参数/返回说明、资源文件组织？
- **代码清晰度**：领域含义命名、通过模式表达意图、结构自解释？
- **整洁代码**：风格一致、方法/类规模适中、复杂度可控、消除重复？

## 改进重点

- **命令处理器**：在基类做参数与状态校验、统一错误处理、妥善资源管理
- **工厂**：依赖配置、与 ServiceProvider 集成、释放模式
- **提供者**：连接管理、异步模式、异常处理与日志
- **配置**：数据注解与验证属性、安全处理敏感配置
- **AI/ML 集成**：Semantic Kernel 使用模式、结构化输出、模型配置

请提供具体、可执行的改进建议，确保与项目架构和 .NET 最佳实践保持一致。
