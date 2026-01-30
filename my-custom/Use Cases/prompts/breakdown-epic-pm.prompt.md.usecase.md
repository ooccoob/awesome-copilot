---
post_title: "breakdown-epic-pm.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "breakdown-epic-pm-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "product-management"]
ai_note: "Generated with AI assistance."
summary: "Use cases for producing epic-level PRDs that drive technical architecture workstreams."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 生成 Epic 级产品需求文档（PRD），为工程团队和架构设计提供权威输入。

## When

- 规划新 Epic 时，需要清晰阐述目标、用户旅程与业务需求。
- 希望建立工程实现与业务价值之间的单一事实源。
- 准备与架构/工程团队对齐前置需求。

## Why

- 将高层想法落地为结构化 PRD，减少理解偏差。
- 明确功能与非功能需求、成功指标、范围边界。
- 支撑后续技术架构、计划排期与资源评估。

## How

- 扮演资深产品经理，读取用户的 Epic 描述并补充缺失信息。
- 采用标准 PRD 结构：名称、目标、用户、旅程、需求、指标、范围、价值。
- 输出 Markdown，保存至 `/docs/ways-of-work/plan/{epic-name}/epic.md`。
- 信息不足时主动提问澄清，确保完整性。

## Key points (英文+中文对照)

- Epic-level clarity（抓住 Epic 级别清晰度）
- Persona-driven journeys（以画像驱动旅程设计）
- Functional & non-functional coverage（同时覆盖功能与非功能）
- Scope guarding（明确范围与排除项）
- Value articulation（阐述业务价值）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. 新产品线立项（New Product Line Initiation）

- 用户故事：作为产品总监，我要把高层商业构想转化为 Epic PRD，支撑架构团队评估。
- 例 1："/breakdown-epic-pm 请将‘跨境支付结算’构想整理为完整 Epic PRD 并指出关键指标。"
- 例 2："/breakdown-epic-pm 依据现有调研，补充用户画像与旅程描述。"
- 例 3："/breakdown-epic-pm 如果缺信息，先提问后再生成 PRD。"
- 例 4："/breakdown-epic-pm 输出功能/非功能需求，并标注技术约束。"
- 例 5："/breakdown-epic-pm 说明不在范围的特性，防止后续需求蔓延。"

### 2. 架构对齐前置（Pre-Architecture Alignment）

- 用户故事：作为解决方案架构师，我需要完整 PRD 以规划技术方案。
- 例 1："/breakdown-epic-pm 将‘统一身份平台’需求转为 PRD，突出安全与性能指标。"
- 例 2："/breakdown-epic-pm 请强调与现有系统的边界与集成假设。"
- 例 3："/breakdown-epic-pm 添加关键 API 旅程与跨团队协作点。"
- 例 4："/breakdown-epic-pm 出具可量化 KPI，方便后续验证。"
- 例 5："/breakdown-epic-pm 说明业务价值等级并给出理由。"

### 3. 投资评审准备（Investment Review）

- 用户故事：作为产品运营，我要准备高质量 PRD 供投资委员会评估。
- 例 1："/breakdown-epic-pm 将‘会员增长引擎’想法整理成标准 PRD。"
- 例 2："/breakdown-epic-pm 请量化收益指标与目标达成时机。"
- 例 3："/breakdown-epic-pm 展示用户旅程对关键痛点的改善。"
- 例 4："/breakdown-epic-pm 标注非功能需求，尤其合规与隐私。"
- 例 5："/breakdown-epic-pm 列出超出范围的高级功能说明。"

### 4. 多团队协作规划（Cross-Team Planning）

- 用户故事：作为项目经理，我要让后端、前端、设计等团队统一理解 Epic 目标。
- 例 1："/breakdown-epic-pm 梳理‘智能客服’Epic 的用户旅程与团队分工。"
- 例 2："/breakdown-epic-pm 将功能需求分组，对应负责团队。"
- 例 3："/breakdown-epic-pm 补充关键依赖与风险提示。"
- 例 4："/breakdown-epic-pm 明确验收标准与 KPI，方便跟踪。"
- 例 5："/breakdown-epic-pm 指出后续迭代可考虑的扩展项。"

### 5. 技术债与演进梳理（Tech Debt Evolution）

- 用户故事：作为平台 PO，我要规划解决技术债的 Epic，让团队有明确方向。
- 例 1："/breakdown-epic-pm 生成‘支付风控重构’Epic PRD，强调性能目标。"
- 例 2："/breakdown-epic-pm 描述现有痛点与预期解决方案。"
- 例 3："/breakdown-epic-pm 明确非功能指标，如 SLA、审计要求。"
- 例 4："/breakdown-epic-pm 标注明确不在范围的遗留系统。"
- 例 5："/breakdown-epic-pm 估算业务价值并说明收益来源。"

### 6. 客户定制/伙伴共建（Customer Co-creation）

- 用户故事：作为合作伙伴 PM，我要将客户需求转为内部 PRD，确保交付一致。
- 例 1："/breakdown-epic-pm 将客户提出的‘多租户报表’诉求转成标准 PRD。"
- 例 2："/breakdown-epic-pm 完善用户旅程并标注合作方责任。"
- 例 3："/breakdown-epic-pm 在 PRD 中明确 SLA 与合规条款。"
- 例 4："/breakdown-epic-pm 写出成功指标与验收条件。"
- 例 5："/breakdown-epic-pm 指出不包含的特性，防止需求扩张。"

## 原始文件

- [breakdown-epic-pm.prompt.md](../../prompts/breakdown-epic-pm.prompt.md)
