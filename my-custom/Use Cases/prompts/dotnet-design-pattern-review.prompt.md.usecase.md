---
post_title: 'dotnet-design-pattern-review.prompt.md Use Cases'
author1: 'github-copilot'
post_slug: 'dotnet-design-pattern-review-prompt-use-cases'
microsoft_alias: 'copilot'
featured_image: ''
categories: []
tags: ['use-cases', '.net', 'design-patterns', 'code-review']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for reviewing .NET/C# codebases with a focus on command, factory, provider, repository, and resource patterns.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

* 利用“.NET/C# Design Pattern Review”提示词审阅选定代码，识别模式应用、缺陷与改进建议，覆盖命令、工厂、依赖注入、资源、仓储等核心实践。

## When

* 拉取请求、架构评审、重构前诊断或技术债梳理时。
* 想验证团队是否遵循既定模式与命名空间准则时。

## Why

* 统一代码风格与架构模式，提升可维护性、可测试性与可扩展性。
* 发现潜在性能、安全、可用性问题并输出可执行修复建议。

## How

* 提供 `${selection}`（文件/目录/项目），让提示词生成模式分析、缺失项、示例代码与操作步骤。
* 覆盖命名空间、依赖注入、资源管理、异步模式、测试可行性等方面。

## Key points (英文+中文对照)

* Pattern compliance checks（检查关键设计模式）
* Namespace & layering review（审视命名空间与分层）
* Async and DI hygiene（关注异步与依赖注入卫生）
* Resource & localization usage（资源与本地化实践）
* Actionable remediation steps（输出可执行改进建议）

## 使用场景

### 1. 命令模式与处理器审查（Command Handlers）

* 用户故事：作为架构师，我要确认命令处理器层使用泛型基类、统一错误处理并遵循命名规则。
* 例1："/dotnet-design-pattern-review [selection=App/Commands] 检查 CommandHandler&lt;TOptions&gt; 是否实现共用验证逻辑。"
* 例2："/dotnet-design-pattern-review [selection=Core/Handlers] 识别缺少 ICommandHandler 接口实现的类。"
* 例3："/dotnet-design-pattern-review [selection=Service/Commands] 建议在 SetupCommand 中统一注册依赖。"
* 例4："/dotnet-design-pattern-review [selection=Console/Program.cs] 校验命令入口是否遵循 host.SetupCommand 模式。"
* 例5："/dotnet-design-pattern-review [selection=App/Commands] 输出命令失败处理与日志策略改进建议。"

### 2. 工厂、依赖注入与生命周期（Factories & DI）

* 用户故事：作为平台工程师，我要确认工厂方法与服务注册一致，依赖注入使用主构造函数与空值守护。
* 例1："/dotnet-design-pattern-review [selection=Core/Factories] 审查工厂是否依赖 ServiceProvider 并负责资源释放。"
* 例2："/dotnet-design-pattern-review [selection=App/Startup.cs] 检查注册生命周期是否符合设计（Singleton/Scoped/Transient）。"
* 例3："/dotnet-design-pattern-review [selection=Service/Implementations] 建议为构造函数参数增加 ArgumentNullException。"
* 例4："/dotnet-design-pattern-review [selection=Core/Factories] 分析复杂对象构建流程并给出抽象改进。"
* 例5："/dotnet-design-pattern-review [selection=App/Extensions] 识别未使用主构造函数的类并提供重构示例。"

### 3. 仓储与提供者实现（Repository & Provider）

* 用户故事：作为数据层负责人，我要审查异步仓储、外部服务 Provider 是否抽象良好且安全。
* 例1："/dotnet-design-pattern-review [selection=Infrastructure/Repositories] 检查接口是否返回 Task/Task&lt;T&gt; 与正确 async/await。"
* 例2："/dotnet-design-pattern-review [selection=Infrastructure/Providers] 评估外部服务 Provider 对配置和异常处理的封装。"
* 例3："/dotnet-design-pattern-review [selection=Infrastructure/DataAccess] 指出未使用参数化查询的代码。"
* 例4："/dotnet-design-pattern-review [selection=Core/Providers] 建议抽象复用（缓存、重试、退避）策略。"
* 例5："/dotnet-design-pattern-review [selection=Tests/Providers] 检查是否具备接口化以支持 Mock。"

### 4. 资源管理与本地化（Resources & Localization）

* 用户故事：作为国际化负责人，我要确保 LogMessages/ ErrorMessages 分离、ResourceManager 使用规范。
* 例1："/dotnet-design-pattern-review [selection=App/Resources] 检查是否存在硬编码字符串需迁移至资源文件。"
* 例2："/dotnet-design-pattern-review [selection=Core/Localization] 评估 ResourceManager 获取字符串的空值处理。"
* 例3："/dotnet-design-pattern-review [selection=App/Logging] 建议为日志与错误信息拆分 .resx。"
* 例4："/dotnet-design-pattern-review [selection=Infrastructure/Localization] 输出资源命名与文化回退策略。"
* 例5："/dotnet-design-pattern-review [selection=Tests/Localization] 确认测试用例覆盖主要资源键。"

### 5. 架构、文档与可测试性（Architecture & Quality）

* 用户故事：作为评审者，我要检查命名空间、SOLID、测试可行性与文档是否符合团队标准。
* 例1："/dotnet-design-pattern-review [selection=Core] 验证命名空间是否遵循 {Core|Console|App|Service}.{Feature}。"
* 例2："/dotnet-design-pattern-review [selection=Service] 识别 SRP 或接口隔离违规点并提供重构建议。"
* 例3："/dotnet-design-pattern-review [selection=App] 审核异步调用是否缺乏 ConfigureAwait(false) 或存在阻塞。"
* 例4："/dotnet-design-pattern-review [selection=App] 输出 XML 文档缺失列表与示例注释。"
* 例5："/dotnet-design-pattern-review [selection=Tests] 评估单元测试是否符合 AAA 模式并覆盖关键路径。"

## 原始文件

* [dotnet-design-pattern-review.prompt.md](../../prompts/dotnet-design-pattern-review.prompt.md)
