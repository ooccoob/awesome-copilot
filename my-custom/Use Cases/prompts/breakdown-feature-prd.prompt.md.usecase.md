---
post_title: "breakdown-feature-prd.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "breakdown-feature-prd-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "product-management"]
ai_note: "Generated with AI assistance."
summary: "Use cases for producing feature-level PRDs derived from epics with clear requirements, personas, and acceptance tests."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 生成 Feature 级 PRD，继承 Epic 背景并详细描述用户故事、需求与验收标准。

## When

- 从 Epic 下拆出新功能或使能项，需要细化需求。
- 规划跨团队协作或技术规格前的需求对齐。
- 准备评审、排期或验收标准时。

## Why

- 保证功能目标、需求与范围清晰，减少歧义。
- 提供工程团队迭代、测试、验收的单一事实源。
- 建立功能与业务价值的明确关联。

## How

- 读取用户提供的 Feature 描述与上层 Epic 背景。
- 输出 Markdown PRD，包含名称、目标、用户故事、需求、验收标准、范围、链接。
- 文件保存至 `/docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md`。
- 信息不足时提出澄清问题后再生成。

## Key points (英文+中文对照)

- Feature-level clarity（明确 Feature 目标）
- Persona-specific stories（围绕画像编写用户故事）
- Functional/non-functional balance（兼顾功能与非功能需求）
- Acceptance-driven validation（以验收标准驱动验证）
- Scope discipline（强调范围控制）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. Epic 子功能拆解（Epic Breakdown）

- 用户故事：作为产品经理，我要把“智能推荐”Epic 的子功能转化为可执行 PRD。
- 例 1："/breakdown-feature-prd [selection=docs/epic/recommendation.md] 根据子功能描述生成 PRD。"
- 例 2："/breakdown-feature-prd 自动引用 Epic 链接并补充用户画像。"
- 例 3："/breakdown-feature-prd 为主要场景写出用户故事与验收标准。"
- 例 4："/breakdown-feature-prd 明确功能/非功能需求并标注依赖。"
- 例 5："/breakdown-feature-prd 标出超出范围项，防止 scope creep。"

### 2. 研发迭代规划（Iteration Planning）

- 用户故事：作为交付经理，我要把即将迭代的功能编写成 PRD，支持排期与估算。
- 例 1："/breakdown-feature-prd 将‘多渠道通知’需求整理成 PRD 模板。"
- 例 2："/breakdown-feature-prd 列出各项验收标准，供 QA 编写测试用例。"
- 例 3："/breakdown-feature-prd 补充非功能需求（性能、安全、易用性）。"
- 例 4："/breakdown-feature-prd 说明关键依赖与与外部系统链接。"
- 例 5："/breakdown-feature-prd 标注业务价值等级与预期指标。"

### 3. 客户共创需求（Customer Co-creation）

- 用户故事：作为伙伴 PM，我要将客户定制功能需求转为内部标准 PRD。
- 例 1："/breakdown-feature-prd 整理客户提供的需求文档并补全缺口。"
- 例 2："/breakdown-feature-prd 将客户痛点映射到用户故事与验收标准。"
- 例 3："/breakdown-feature-prd 明确非功能约束（合规、SLA）。"
- 例 4："/breakdown-feature-prd 指出不在范围的个性化请求。"
- 例 5："/breakdown-feature-prd 生成链接方便关联到 Epic 与架构文档。"

### 4. 技术债或优化项需求化（Tech Debt PRDization）

- 用户故事：作为平台 PO，我要把技术债改进需求写成 PRD，让团队清楚验收标准。
- 例 1："/breakdown-feature-prd 描述‘日志系统升级’的业务问题与解决方案。"
- 例 2："/breakdown-feature-prd 补充非功能需求如性能、可靠性指标。"
- 例 3："/breakdown-feature-prd 写出用户故事覆盖主流程与边界场景。"
- 例 4："/breakdown-feature-prd 提供验收标准与测试清单。"
- 例 5："/breakdown-feature-prd 指出范围外的相关系统。"

### 5. 跨团队协同同步（Cross-team Alignment）

- 用户故事：作为解决方案经理，我要用 PRD 向设计、研发、运营同步目标与细节。
- 例 1："/breakdown-feature-prd 将会议纪要转化为标准 PRD 并分发。"
- 例 2："/breakdown-feature-prd 添加用户旅程补充设计需求。"
- 例 3："/breakdown-feature-prd 列出接口、权限与数据需求供工程参考。"
- 例 4："/breakdown-feature-prd 提供验收 checklist，支持运营上线。"
- 例 5："/breakdown-feature-prd 指定版本保存路径 `/docs/ways-of-work/plan/...`。"

### 6. 验收与回顾准备（Acceptance & Retro）

- 用户故事：作为 QA，我要确保 Feature 在上线前有清晰的验收标准与范围说明。
- 例 1："/breakdown-feature-prd 提取用户故事并附加验收条款。"
- 例 2："/breakdown-feature-prd 检查非功能需求是否覆盖安全、性能。"
- 例 3："/breakdown-feature-prd 指出边界场景和例外处理。"
- 例 4："/breakdown-feature-prd 将验收标准转为 Given/When/Then 格式。"
- 例 5："/breakdown-feature-prd 标记上线回顾时需要验证的指标。"

## 原始文件

- [breakdown-feature-prd.prompt.md](../../prompts/breakdown-feature-prd.prompt.md)
