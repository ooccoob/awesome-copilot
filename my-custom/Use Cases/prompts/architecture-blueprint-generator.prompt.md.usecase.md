---
post_title: "architecture-blueprint-generator.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "architecture-blueprint-generator-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "architecture"]
ai_note: "Generated with AI assistance."
summary: "Use cases for producing comprehensive architecture blueprints from existing codebases with automated analysis, visualization, and governance guidance."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 生成详尽的 `Project_Architecture_Blueprint.md`，自动分析代码架构、可视化组件关系并输出可扩展的治理蓝图。

## When

- 需要快速了解遗留系统或新接手项目的真实架构。
- 规划重构、迁移或扩展方案时评估现状与风险。
- 建立统一的架构文档、图谱与演进指引。

## Why

- 自动化梳理技术栈与模式，减少人工调研误差。
- 输出多层级图表、模式说明与演进建议，确保团队共识。
- 为扩展、治理、审计提供权威依据。

## How

- 配置技术栈、架构模式、图表类型、细节层级、是否包含示例/决策记录等变量。
- 解析目录结构、依赖、命名约束，识别架构边界与层次规则。
- 生成跨层组件说明、数据架构、跨领域通用能力与治理策略。
- 可选输出代码示例、ADR、蓝图流程，确保持续演进。

## Key points (英文+中文对照)

- Architecture detection automation（自动化识别架构与技术栈）
- Layered dependency mapping（梳理分层依赖关系）
- Diagram-driven communication（通过图表传达架构）
- Cross-cutting concern catalog（覆盖跨领域通用能力）
- Extension governance guidance（提供扩展与治理指引）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. 遗留系统架构盘点（Legacy Audit）

- 用户故事：作为企业架构师，我要对遗留系统进行快速盘点，厘清真实分层、组件交互与技术债，支撑重构路线规划。
- 例 1："/architecture-blueprint-generator [selection=src] 生成当前系统的分层与组件交互图，指出架构违规点。"
- 例 2："/architecture-blueprint-generator 请梳理遗留系统的跨域调用与数据流，并输出治理建议。"
- 例 3："/architecture-blueprint-generator [selection=src/Modules] 识别存在的混合架构模式并说明成因。"
- 例 4："/architecture-blueprint-generator 生成跨层依赖清单，标注循环引用与风险模块。"
- 例 5："/architecture-blueprint-generator 输出遗留系统扩展限制与推荐的演进路径。"

### 2. 新成员项目交接（Onboarding Briefing）

- 用户故事：作为技术负责人，我要为新成员提供可视化的项目架构指南，确保快速理解模块职责与交互协议。
- 例 1："/architecture-blueprint-generator 生成面向新成员的高层架构概览与核心组件说明。"
- 例 2："/architecture-blueprint-generator [selection=docs/deployment] 转化部署结构为图表并说明关键依赖。"
- 例 3："/architecture-blueprint-generator 输出各层职责及团队边界，帮助新人匹配联系人。"
- 例 4："/architecture-blueprint-generator 请提供常见扩展点与插件机制说明，便于新功能接入。"
- 例 5："/architecture-blueprint-generator 制作 FAQ 与更新建议，提醒新成员常见陷阱。"

### 3. 架构评审与守护（Architecture Review）

- 用户故事：作为架构委员会成员，我要定期评审系统实现是否符合既定模式，并制定自动化守护策略。
- 例 1："/architecture-blueprint-generator [selection=src] 检查实现是否遵循 Clean Architecture 分层规则。"
- 例 2："/architecture-blueprint-generator 输出服务通信协议、同步/异步模式与容错策略。"
- 例 3："/architecture-blueprint-generator 提供跨领域能力（安全、日志、配置）实现现状与差距。"
- 例 4："/architecture-blueprint-generator [selection=src/Core] 识别依赖注入模式与改进建议。"
- 例 5："/architecture-blueprint-generator 生成架构守护建议，包括自动化校验与评审节奏。"

### 4. 重构/迁移路线规划（Refactor Roadmapping）

- 用户故事：作为解决方案架构师，我要评估当前架构的风险点，制定分阶段重构或云迁移路线。
- 例 1："/architecture-blueprint-generator [selection=src] 输出关键组件的演进与扩展策略。"
- 例 2："/architecture-blueprint-generator 提供数据架构与缓存策略图谱，辅助迁移评估。"
- 例 3："/architecture-blueprint-generator 识别可抽离的微服务候选并标注依赖。"
- 例 4："/architecture-blueprint-generator 生成重构优先级与潜在影响分析。"
- 例 5："/architecture-blueprint-generator 提供迁移过程中需要维护的架构守护 checklist。"

### 5. 持续交付与治理（Continuous Governance）

- 用户故事：作为平台负责人，我要确保架构文档常新，落地自动化校验与 ADR，避免架构偏移。
- 例 1："/architecture-blueprint-generator 生成最新的架构蓝图并附带治理流程建议。"
- 例 2："/architecture-blueprint-generator [selection=src] 输出跨环境部署拓扑与配置策略。"
- 例 3："/architecture-blueprint-generator 提取关键 ADR，梳理决策背景与影响。"
- 例 4："/architecture-blueprint-generator 制定自动化守护脚本需覆盖的检查项。"
- 例 5："/architecture-blueprint-generator 生成未来演进蓝图与维护节奏提醒。"

### 6. 多技术栈整合（Polyglot Integration）

- 用户故事：作为集成架构师，我要理解多技术栈系统间的协作方式，确保扩展时不破坏边界。
- 例 1："/architecture-blueprint-generator [selection=src] 列出每个技术栈的专属架构模式与治理要点。"
- 例 2："/architecture-blueprint-generator 识别多栈间的数据流向、转换与契约。"
- 例 3："/architecture-blueprint-generator 输出跨技术栈的依赖与集成风险。"
- 例 4："/architecture-blueprint-generator 提供统一扩展模板，指导新增服务如何接入。"
- 例 5："/architecture-blueprint-generator 制定多栈协作下的测试与部署策略建议。"

## 原始文件

- [architecture-blueprint-generator.prompt.md](../../prompts/architecture-blueprint-generator.prompt.md)
