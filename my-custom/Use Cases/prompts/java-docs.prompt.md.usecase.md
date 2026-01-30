---
post_title: 'java-docs.prompt.md Use Cases'
author1: 'github-copilot'
post_slug: 'java-docs-prompt-use-cases'
microsoft_alias: 'copilot'
featured_image: ''
categories: []
tags: ['use-cases', 'java', 'documentation', 'javadoc', 'md-guides']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for generating and maintaining Java documentation, including Javadoc, API guides, and architecture references.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

* 利用“Java 文档”提示词，为类/接口/模块生成高质量文档：Javadoc、API 指南、示例、架构图与变更日志。

## When

* 新增或重构模块后，需要补齐/刷新文档时。
* 发布版本前进行 API 冻结与说明更新时。
* 代码评审要求提升可读性与可维护性时。

## Why

* 高质量文档降低认知负担，提升协作效率与交付质量。
* 文档即契约，有助于测试、自动化与合规审计。

## How

* 从源码提取公共 API 与关键注释，形成 Javadoc 与 MD 文档。
* 以“输入/输出/错误模式”为主线编写使用指南与示例。
* 自动生成变更记录与迁移指南，覆盖破坏性变更与替代方案。

## Key points (英文+中文对照)

* Clear API contracts（清晰的 API 契约）
* Examples first（示例优先，先跑通后解释）
* Error handling and edge cases（错误处理与边界条件）
* Versioning and changelogs（版本与变更记录）
* Architecture context（架构上下文与约束）

## 使用场景

### 1. 生成 Javadoc（类与接口）

* 用户故事：作为开发者，我要为公共类补齐 Javadoc，明确职责、参数、返回与异常。
* 例1："/java-docs 为 UserService 接口生成 Javadoc，包括线程安全说明。"
* 例2："/java-docs 为 OrderController 的每个端点添加 @param/@return 描述。"
* 例3："/java-docs 为枚举 PaymentStatus 添加语义解释与示例。"
* 例4："/java-docs 为 Util 类补充‘不建议实例化’与示例代码。"
* 例5："/java-docs 为异常类 BizException 添加使用建议与错误码约定。"

### 2. API 使用指南（MD 文档）

* 用户故事：作为集成方，我需要快速理解如何调用接口、需要哪些依赖与配置。
* 例1："/java-docs 生成‘快速开始’文档，含依赖、配置、初始化代码。"
* 例2："/java-docs 提供 ‘Happy Path + 失败重试’示例。"
* 例3："/java-docs 说明超时/重试/幂等策略，列出默认值与覆盖方式。"
* 例4："/java-docs 输出‘常见错误与排查’章节。"
* 例5："/java-docs 给出 ‘生产部署建议’与安全注意事项。"

### 3. 变更与迁移（Changelog/Migration）

* 用户故事：作为维护者，我要记录破坏性变更并提供迁移方案与脚本样例。
* 例1："/java-docs 生成从 v1 到 v2 的迁移指南，标注废弃 API 与替代。"
* 例2："/java-docs 输出 changelog 模板（Added/Changed/Deprecated/Removed/Fixed/Security）。"
* 例3："/java-docs 生成‘兼容适配层’示例代码。"
* 例4："/java-docs 对数据库变更生成 DDL 差异示例与回滚思路。"
* 例5："/java-docs 列出需要更新的配置项与默认值调整。"

### 4. 架构与上下文（Architecture Overview）

* 用户故事：作为架构师，我需要出具模块的上下文、依赖与数据流，以便团队理解边界。
* 例1："/java-docs 输出 C4 Container 与 Component 级别的概览图（Mermaid）。"
* 例2："/java-docs 标注与外部系统的集成点与协议。"
* 例3："/java-docs 列举关键 NFR 与设计权衡（延迟/吞吐/一致性）。"
* 例4："/java-docs 给出典型时序图与失败路径。"
* 例5："/java-docs 说明数据模型与索引策略选择。"

### 5. 质量与评审（Docs Lint/Review）

* 用户故事：作为评审者，我需要检查文档质量并给出修订建议。
* 例1："/java-docs 运行文档质量检查清单（术语一致、链接有效、示例可执行）。"
* 例2："/java-docs 标注歧义与不一致的段落并给出替代表述。"
* 例3："/java-docs 检查代码示例是否可编译并符合最佳实践。"
* 例4："/java-docs 输出‘缺失章节’与‘建议补充’列表。"
* 例5："/java-docs 生成评审意见汇总与优先级排序。"

## 原始文件

* [java-docs.prompt.md](../../prompts/java-docs.prompt.md)
