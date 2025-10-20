---
post_title: 'dotnet-best-practices.prompt.md Use Cases'
author1: 'github-copilot'
post_slug: 'dotnet-best-practices-prompt-use-cases'
microsoft_alias: 'copilot'
featured_image: ''
categories: []
tags: ['use-cases', '.net', 'csharp', 'best-practices', 'code-review']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for auditing and refactoring .NET/C# code to align with project-specific best practices, including architecture, DI, async patterns, testing, and AI integration.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

* 借助“.NET/C# Best Practices”提示词审查或重构代码，使其符合项目约定：架构模式、依赖注入、资源管理、异步、测试、配置、AI 集成、安全等。

## When

* 代码评审、遗留模块重构、引入新功能前的质量基线检查。
* 版本发布或迁移到 .NET 8/C#12 等新平台时。

## Why

* 标准化代码结构，提高可维护性与测试性。
* 降低 Bug 率与运行时风险，强化安全与性能。

## How

* 指定待检查范围（文件/项目/解决方案）。
* 按分类给出改进建议：文档、模式、依赖注入、资源、本地化、异步、测试、配置、AI、日志、安全、质量。
* 输出重构示例、验证步骤与后续行动。

## Key points (英文+中文对照)

* Enforce documentation standards（执行文档与命名标准）
* Apply architectural patterns（应用既定架构模式）
* Validate DI and lifetimes（校验依赖注入与生命周期）
* Ensure async correctness（确保异步调用正确）
* Strengthen testing and AI usage（强化测试与 AI 使用规范）

## 使用场景

### 1. 文档与命名空间治理（Documentation & Namespaces）

* 用户故事：作为代码审查者，我需要确保公共 API 有完整 XML 注释、命名空间满足 `{Core|Console|App|Service}.{Feature}` 约定。
* 例1："/dotnet-best-practices 检查 Application 层公共类缺失的 XML 文档并给出补全文本。"
* 例2："/dotnet-best-practices 列出命名空间不符合规则的类并提供重构建议。"
* 例3："/dotnet-best-practices 审查公共方法 XML 注释是否包含参数与返回值描述。"
* 例4："/dotnet-best-practices 生成缺失注释清单与责任人分配表。"
* 例5："/dotnet-best-practices 输出建议的文档模板及示例。"

### 2. 架构模式与依赖注入（Architecture & DI）

* 用户故事：作为架构师，我要验证命令处理、工厂模式、接口隔离等是否按约执行，并检查 DI 配置。
* 例1："/dotnet-best-practices 审核 CommandHandlers 继承关系并补齐泛型基类。"
* 例2："/dotnet-best-practices 检查构造函数注入 null 校验是否使用 ArgumentNullException。"
* 例3："/dotnet-best-practices 分析服务注册生命周期是否合理（Singleton/Scoped/Transient）。"
* 例4："/dotnet-best-practices 识别职责过大的接口，建议拆分并命名。"
* 例5："/dotnet-best-practices 为复杂对象创建添加 Factory 模式示例。"

### 3. 资源管理与本地化（Resources & Localization）

* 用户故事：作为国际化负责人，我要确保消息使用 ResourceManager、区分日志与错误资源文件，并进行空值防护。
* 例1："/dotnet-best-practices 检查是否存在硬编码字符串并迁移到资源文件。"
* 例2："/dotnet-best-practices 验证 `_resourceManager.GetString` 调用是否对缺失键做处理。"
* 例3："/dotnet-best-practices 审查日志/错误资源文件是否拆分并添加示例。"
* 例4："/dotnet-best-practices 输出资源命名规范与测试策略。"
* 例5："/dotnet-best-practices 列出未覆盖的语言键并建议优先级。"

### 4. 异步模式与性能（Async & Performance）

* 用户故事：作为性能工程师，我要确保 I/O 操作使用 async/await、正确返回 Task，并在需要时 ConfigureAwait(false)。
* 例1："/dotnet-best-practices 检测同步 I/O 方法并给出异步替代代码。"
* 例2："/dotnet-best-practices 校验 async 方法返回类型与异常处理是否规范。"
* 例3："/dotnet-best-practices 找出遗漏 ConfigureAwait(false) 的库调用并分析风险。"
* 例4："/dotnet-best-practices 对潜在死锁/阻塞调用给出修复建议。"
* 例5："/dotnet-best-practices 评估 C#12/.NET8 新特性是否可优化现有实现。"

### 5. 测试与质量保证（Testing & QA）

* 用户故事：作为测试负责人，我要确保 MSTest + FluentAssertions + Moq 的测试标准落地，并覆盖成功/失败场景。
* 例1："/dotnet-best-practices 审核单元测试是否遵循 AAA 模式并引用 FluentAssertions。"
* 例2："/dotnet-best-practices 生成缺失的失败路径测试列表。"
* 例3："/dotnet-best-practices 检查 null 参数验证是否有专门的测试。"
* 例4："/dotnet-best-practices 评估测试命名/目录结构与约定是否一致。"
* 例5："/dotnet-best-practices 输出测试覆盖率提升路线图。"

### 6. 配置、AI 集成与日志（Configuration, AI, Logging）

* 用户故事：作为平台工程师，我要验证配置绑定、语义内核集成与日志策略是否正确、安全。
* 例1："/dotnet-best-practices 检查 strongly-typed 配置类及数据注解是否齐全。"
* 例2："/dotnet-best-practices 审核 IConfiguration 绑定流程与 appsettings 后备值。"
* 例3："/dotnet-best-practices 对 Semantic Kernel 配置与模型注册进行合规性检查。"
* 例4："/dotnet-best-practices 分析日志是否结构化、包含上下文且避免敏感数据。"
* 例5："/dotnet-best-practices 识别未捕获的异常并建议 try-catch 与特定异常类型。"

## 原始文件

* [dotnet-best-practices.prompt.md](../../prompts/dotnet-best-practices.prompt.md)
