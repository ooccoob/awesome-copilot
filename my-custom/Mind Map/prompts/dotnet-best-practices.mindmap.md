## 文档综述（What/When/Why/How）

- What：.NET/C# 项目最佳实践清单（结构/模式/DI/资源/异步/测试/配置/AI/日志/性能/质量）

- When：对现有代码进行专项审查与整改时

- Why：统一约定，提升可维护性/性能/安全与可测试性

- How：按专题检查与修正（XML 注释、命名空间、主构造器、命令处理器、资源管理、本地化、MSTest+FluentAssertions、SK 集成等）

## 示例提问（Examples）

- “为该服务添加主构造器 DI 与参数空校验，并补齐 XML 注释”

- “按资源管理器拆分日志/错误消息到 .resx，并接入结构化日志”

## 结构化要点（CN/EN）

- 设计/Design：Command/Factory/ISegregation

- DI：构造注入/生命周期/可测试性

- 本地化/I18n：ResourceManager 分离

- 异步/Async：Task/ConfigureAwait/异常

- 测试/Testing：MSTest + Fluent

- 配置/Config：强类型 + 校验

- AI 集成/SK：Kernel 配置

## 中文思维导图

- 文档与结构
- 模式与架构
- 依赖注入
- 资源与本地化
- 异步与错误
- 测试与配置
- 日志与性能

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\dotnet-best-practices.prompt.md

- 生成时间：2025-10-17
