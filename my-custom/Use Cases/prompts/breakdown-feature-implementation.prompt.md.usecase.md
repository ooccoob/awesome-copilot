---
post_title: "breakdown-feature-implementation.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "breakdown-feature-implementation-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "implementation-planning"]
ai_note: "Generated with AI assistance."
summary: "Use cases for producing detailed feature implementation plans aligned with Epoch monorepo architecture."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 生成覆盖前后端、数据与部署的 Feature 实施计划，包含架构、接口、数据模型与安全性能细节。

## When

- Feature PRD 已完成，需要详细技术执行方案。
- 架构师、Tech Lead 规划跨层实现流程时。
- 准备技术评审、开发排期或迭代拆分。

## Why

- 统一理解实现路径、架构边界与依赖。
- 输出可直接指导开发的步骤、图表与规格。
- 降低跨团队沟通成本，确保质量与可扩展性。

## How

- 解析 PRD，撰写 Markdown 实施计划，保存到 `/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`。
- 按 Epoch monorepo 结构涵盖前端 apps、后端 services、共享 packages。
- 生成架构图（Mermaid）、数据模型、API 设计、部署与安全策略。
- 聚焦可执行细节，必要时使用伪代码，不直接生成生产代码。

## Key points (英文+中文对照)

- End-to-end implementation planning（端到端实施规划）
- Architecture visualization（架构可视化）
- Data & API specification（数据与 API 规格）
- Frontend component hierarchy（前端组件层级）
- Security & performance guardrails（安全与性能护栏）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. 大型 SaaS 核心特性落地（Core Feature Delivery）

- 用户故事：作为 Tech Lead，我要将“企业计费中心”PRD 转化为可执行实施方案。
- 例 1："/breakdown-feature-implementation [selection=docs/prd/billing.md] 生成端到端实施计划并绘制系统架构图。"
- 例 2："/breakdown-feature-implementation 请补充前端与 tRPC API 的交互流程。"
- 例 3："/breakdown-feature-implementation 输出数据库 ER 图与索引策略。"
- 例 4："/breakdown-feature-implementation 说明部署拓扑与扩展方案。"
- 例 5："/breakdown-feature-implementation 梳理安全、性能与缓存策略。"

### 2. 多团队协作拆分（Cross-team Alignment）

- 用户故事：作为项目经理，我要明确前端、后端、基础设施各团队的工作内容与依赖。
- 例 1："/breakdown-feature-implementation 按团队拆分实施计划并标注交付物。"
- 例 2："/breakdown-feature-implementation 生成 Mermaids 展示层间交互，方便同步。"
- 例 3："/breakdown-feature-implementation 指出 packages 复用与新建策略。"
- 例 4："/breakdown-feature-implementation 列出关键集成点与测试边界。"
- 例 5："/breakdown-feature-implementation 制定上线前检查清单。"

### 3. 架构评审准备（Architecture Review Deck）

- 用户故事：作为架构师，我要汇总实施计划用于评审，并验证架构符合规范。
- 例 1："/breakdown-feature-implementation 汇总关键组件与数据流供评审使用。"
- 例 2："/breakdown-feature-implementation 列出技术栈选择及其合理性。"
- 例 3："/breakdown-feature-implementation 补充风险、依赖与缓解措施。"
- 例 4："/breakdown-feature-implementation 生成 API 规范与错误处理策略。"
- 例 5："/breakdown-feature-implementation 给出可扩展性与性能考量。"

### 4. 技术债与重构实施（Refactor Execution）

- 用户故事：作为平台工程师，我要规划重构或技术债特性的实施细节。
- 例 1："/breakdown-feature-implementation 描述重构后系统架构与数据迁移策略。"
- 例 2："/breakdown-feature-implementation 列出替换旧模块所需的步骤与时间点。"
- 例 3："/breakdown-feature-implementation 规划渐进迁移的部署与回滚方案。"
- 例 4："/breakdown-feature-implementation 补充监控与告警需求。"
- 例 5："/breakdown-feature-implementation 说明测试策略与验收标准。"

### 5. 客户定制功能交付（Customer Customization）

- 用户故事：作为交付工程师，我要针对客户需求编写实现计划，确保与主线代码一致。
- 例 1："/breakdown-feature-implementation 根据定制 PRD 输出实现路线与风险。"
- 例 2："/breakdown-feature-implementation 规划 packages 内需扩展的模块。"
- 例 3："/breakdown-feature-implementation 给出第三方集成与数据处理方案。"
- 例 4："/breakdown-feature-implementation 说明权限、审计与合规要求。"
- 例 5："/breakdown-feature-implementation 制定交付后回归和验收计划。"

### 6. 新人培训与知识传承（Onboarding & Knowledge Transfer）

- 用户故事：作为资深工程师，我要把成熟的实施流程转为模板，帮助新人快速掌握。
- 例 1："/breakdown-feature-implementation 用样板 PRD 生成标准实施计划教学资料。"
- 例 2："/breakdown-feature-implementation 强调 Monorepo 目录结构与职责划分。"
- 例 3："/breakdown-feature-implementation 列出常见陷阱与回避策略。"
- 例 4："/breakdown-feature-implementation 设计练习任务的实施计划蓝本。"
- 例 5："/breakdown-feature-implementation 输出 QA 与验收流程，方便培训。"

## 原始文件

- [breakdown-feature-implementation.prompt.md](../../prompts/breakdown-feature-implementation.prompt.md)
