---
post_title: 'breakdown-epic-arch.prompt.md Use Cases'
author1: 'github-copilot'
post_slug: 'breakdown-epic-arch-prompt-use-cases'
microsoft_alias: 'copilot'
featured_image: ''
categories: []
tags: ['use-cases', 'architecture', 'epic', 'mermaid', 'ddd', 'nextjs', 'turborepo', 'trpc', 'docker', 'saas']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for generating Epic Architecture Specifications: overview, layered Mermaid diagrams, features & enablers, tech stack, value, and t-shirt sizing with deployment considerations.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

- 基于 Epic PRD 生成高层技术架构说明书：架构综述、分层架构图（Mermaid）、高层特性与技术使能、技术栈、技术价值评估与 T-Shirt 估算，并按规范落盘。

## When

- 拿到 Epic PRD，需要在开发前进行跨团队对齐与方案规划时。
- 进入里程碑的架构评审阶段，需固定统一输出物规范时。
- 需要兼顾自托管与 SaaS 两种部署形态进行差异分析时。

## Why

- 降低不确定性，统一技术蓝图与交付边界，支撑估算与排期。
- 保障模块化与可扩展性，兼容多部署形态，便于持续演进。
- 让研发、产品、运维对同一架构产物达成共识。

## How

- 采用领域驱动架构（Domain-driven architecture）进行模块化与边界划分。
- 全面容器化（Docker）各服务，规划自托管与 SaaS 部署差异。
- 应用栈：TypeScript/Next.js（App Router）；单仓：Turborepo。
- 接口层：tRPC（类型安全 API）；认证：Stack Auth。
- 产出 Mermaid 架构图：用户层、应用层、服务层、数据层、基础设施层；同步/异步路径均标注。
- 交付格式：Markdown 保存到 `/docs/ways-of-work/plan/{epic-name}/arch.md`。
- 输出不写真实代码（如需仅给伪代码），重点在架构与流程。

## Key points (英文+中文对照)

- Domain-driven architecture; modular and scalable（领域驱动架构；模块化与可扩展）
- Self-hosted and SaaS deployment support（同时支持自托管与 SaaS 部署）
- Docker containerization for all services（全服务容器化）
- TypeScript/Next.js App Router; Turborepo monorepo（TypeScript/Next.js App Router；Turborepo 单仓）
- tRPC for type-safe APIs; Stack Auth for authentication（tRPC 类型安全 API；Stack Auth 认证）

## 使用场景

### 1. 从 PRD 快速产出架构综述（Overview）

- 用户故事：作为资深架构师，我希望基于 PRD 快速形成高层技术方案综述，便于团队对齐目标与边界。
- 例1："/breakdown-epic-arch [提供 Epic PRD.md] 请提炼架构综述，明确关键组件与交互路径。"
- 例2："/breakdown-epic-arch [提供功能列表] 请将功能聚类为领域模块，并说明边界与依赖。"
- 例3："/breakdown-epic-arch [提供风险清单] 请在综述中标注高风险区域与缓解策略。"
- 例4："/breakdown-epic-arch 请给出综述中的关键假设与前置条件，便于评审确认。"
- 例5："/breakdown-epic-arch 请输出适合领导层阅读的 1 段摘要（不含代码）。"

### 2. 绘制分层系统架构图（Mermaid）

- 用户故事：作为方案设计者，我需要可读性强的分层架构图，展示用户/应用/服务/数据/基础设施层及同步与异步流程。
- 例1："/breakdown-epic-arch [提供关键服务清单] 请生成包含五层结构的 Mermaid 架构图（含子图 subgraphs）。"
- 例2："/breakdown-epic-arch 请在图中标注同步请求路径与异步处理流（消息/任务）。"
- 例3："/breakdown-epic-arch 请为外部 API 集成、缓存、向量库、主数据库分别着色并加图例。"
- 例4："/breakdown-epic-arch [提供部署形态约束] 请分别给出自托管与 SaaS 两种部署变体图。"
- 例5："/breakdown-epic-arch 请在图中标注认证（Stack Auth）与鉴权流转的关键节点。"

### 3. 梳理高层特性与技术使能（Features & Enablers）

- 用户故事：作为技术负责人，我希望明确高层特性与所需技术使能，以指导后续分解与排期。
- 例1："/breakdown-epic-arch [提供 PRD 章节] 请列出高层特性清单，并对齐技术使能（新服务/库/基础设施）。"
- 例2："/breakdown-epic-arch 请为每个特性标注依赖的服务与跨组件交互。"
- 例3："/breakdown-epic-arch 请识别需要的后台任务、工作流（如 n8n）与触发条件。"
- 例4："/breakdown-epic-arch 请输出可观测性/日志/审计等横向使能建议。"
- 例5："/breakdown-epic-arch 请将使能项按优先级与复杂度分层，形成落地顺序建议。"

### 4. 技术栈与非功能约束（部署/扩展/安全）

- 用户故事：作为架构评审者，我需要技术栈选择与非功能约束（性能/可用性/安全/合规）的清晰说明。
- 例1："/breakdown-epic-arch 请确认技术栈：TypeScript/Next.js(App Router)/tRPC/Turborepo/Stack Auth，并说明选型理由与替代方案。"
- 例2："/breakdown-epic-arch 请给出数据库/缓存/向量库的建议（PostgreSQL/Redis/Qdrant）与场景说明。"
- 例3："/breakdown-epic-arch 请输出容器化（Docker）与镜像构建建议，包含本地与 CI/CD 流程要点。"
- 例4："/breakdown-epic-arch 请梳理自托管与 SaaS 在网络、密钥管理、数据驻留上的差异点。"
- 例5："/breakdown-epic-arch 请列出安全与合规注意事项（认证、授权、日志、隐私）。"

### 5. 技术价值评估与 T-Shirt 估算（Value & Sizing）

- 用户故事：作为计划负责人，我需要面向价值的评估与粗粒度 T-Shirt 估算，支撑排期与资源配置。
- 例1："/breakdown-epic-arch [提供价值维度] 请输出技术价值（高/中/低）并简述依据。"
- 例2："/breakdown-epic-arch 请标注主要复杂度与不确定性来源，并给出缓解建议。"
- 例3："/breakdown-epic-arch 请给出各模块的 T-Shirt 估算（S/M/L/XL）和关键假设。"
- 例4："/breakdown-epic-arch 请将估算与部署形态（自托管/SaaS）差异相关联。"
- 例5："/breakdown-epic-arch 请输出可选切片交付路径（里程碑划分建议）。"

### 6. 交付落盘与路径规范（Delivery & Pathing）

- 用户故事：作为过程管理员，我需要确保产物命名、路径与结构合规，便于查阅与复用。
- 例1："/breakdown-epic-arch [提供 epic 名称] 请生成最终文档，并保存到 `/docs/ways-of-work/plan/{epic-name}/arch.md`。"
- 例2："/breakdown-epic-arch 请校验文档结构是否包含所有必须章节并给出缺失清单。"
- 例3："/breakdown-epic-arch 请在文末附上假设/未决问题/TODO 列表，便于后续追踪。"
- 例4："/breakdown-epic-arch 请输出评审清单（检查点）用于走查架构说明书质量。"
- 例5："/breakdown-epic-arch 请根据规范生成 PR 描述模板，便于归档与评审。"

### 7. 多部署与合规差异化方案（Self-hosted vs SaaS）

- 用户故事：作为平台架构师，我需要对比自托管与 SaaS 在架构、运维与合规方面的差异并形成双轨方案。
- 例1："/breakdown-epic-arch 请输出自托管与 SaaS 部署差异表（网络、Secrets、数据驻留）。"
- 例2："/breakdown-epic-arch 请为多租户/单租户场景提供架构差异建议与风险点。"
- 例3："/breakdown-epic-arch 请生成 SaaS 多区域部署示意（路由/数据同步/故障转移）。"
- 例4："/breakdown-epic-arch 请列出合规要求映射（如审计、日志保留、数据删除流程）。"
- 例5："/breakdown-epic-arch 请补充针对出口合规/外部 API 的风险与缓解策略。"

## 原始文件

- [breakdown-epic-arch.prompt.md](../../prompts/breakdown-epic-arch.prompt.md)
