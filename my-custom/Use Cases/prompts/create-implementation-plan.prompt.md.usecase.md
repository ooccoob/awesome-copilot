---
post_title: 'create-implementation-plan.prompt.md Use Cases'
author1: 'github-copilot'
post_slug: 'create-implementation-plan-prompt-use-cases'
microsoft_alias: 'copilot'
featured_image: ''
categories: []
tags: ['use-cases', 'implementation-plan', 'project-management', 'automation']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for generating deterministic, AI-ready implementation plans with structured phases, tasks, and validation gates.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

* 使用“Create Implementation Plan”提示词，为任意工作项生成机器可执行的实施计划，包含阶段划分、任务表、校验与元数据。

## When

* 新功能、重构、升级、基础设施调整或流程建设需要明确执行蓝图时。
* 需要由 AI 或多团队并行执行的分布式任务时。

## Why

* 保证计划结构标准化、可解析、无歧义，便于自动化执行与审计。
* 使得责任、依赖与验证点明确，降低沟通与协作成本。

## How

* 提供 PlanPurpose/上下文，按模板生成包含前言、需求、分阶段任务、依赖、测试、风险等章节的 Markdown。
* 遵守命名规范 `[purpose]-[component]-[version].md`，并写入 `/plan/` 目录。
* 为每个任务设置唯一 ID、可并行性说明、完成标准与自动验证条件。

## Key points (英文+中文对照)

* Deterministic structure（结构确定且可解析）
* Phase-based execution（按阶段组织执行）
* Machine-verified criteria（提供机器可验证标准）
* Explicit dependencies（显式声明依赖与顺序）
* Versioned deliverables（版本化交付物管理）

## 使用场景

### 1. 需求梳理与范围界定（Scope & Requirements）

* 用户故事：作为产品/架构负责人，我要确认计划输入清单、范围和约束，确保计划覆盖业务和技术需求。
* 例1："/create-implementation-plan [PlanPurpose=feature-customer-portal] 请列出前置需求与限制，映射到 REQ-/CON-/SEC- IDs。"
* 例2："/create-implementation-plan [PlanPurpose=refactor-auth-module] 汇总安全要求与兼容性约束，补充 SEC-/PAT- 条目。"
* 例3："/create-implementation-plan [PlanPurpose=upgrade-payment-gateway] 输出法规与合规模块，标注 PCI/DSS 影响。"
* 例4："/create-implementation-plan [PlanPurpose=process-ai-handoff] 定义 AI-to-AI 协作前提与交付标准。"
* 例5："/create-implementation-plan [PlanPurpose=data-warehouse-sync] 生成数据质量与同步频率要求列表。"

### 2. 阶段划分与任务模板（Phases & Tasks）

* 用户故事：作为交付经理，我要得到按阶段拆分的任务表，每个任务都带唯一 ID、描述、依赖、完成标记列。
* 例1："/create-implementation-plan [PlanPurpose=feature-notification-service] 为 Phase 1 列出 TASK-001~TASK-00X，附完成判据。"
* 例2："/create-implementation-plan [PlanPurpose=refactor-reporting] 添加并行任务说明，标注可并行执行与依赖链。"
* 例3："/create-implementation-plan [PlanPurpose=infrastructure-aks-upgrade] 生成多阶段表格，每阶段含 GOAL-XXX 与任务表。"
* 例4："/create-implementation-plan [PlanPurpose=design-mobile-app-shell] 在任务描述中引用具体文件路径与模块。"
* 例5："/create-implementation-plan [PlanPurpose=process-release-readiness] 输出任务完成列默认空白，预留审核签名。"

### 3. 自动化与校验（Automation & Validation）

* 用户故事：作为平台工程师，我要确保计划包含可编程验证点、CI/CD 集成与质量门控。
* 例1："/create-implementation-plan [PlanPurpose=architecture-edge-gateway] 添加验证列，指出自动化脚本或检查命令。"
* 例2："/create-implementation-plan [PlanPurpose=feature-ai-assistant] 写明模型评估指标与自动测试策略。"
* 例3："/create-implementation-plan [PlanPurpose=upgrade-dependency-tree] 记录版本锁定、回滚步骤与形式验证任务。"
* 例4："/create-implementation-plan [PlanPurpose=data-analytics-pipeline] 指定数据对账与质量校验流程。"
* 例5："/create-implementation-plan [PlanPurpose=process-onboarding] 添加 checklist 与自动触发的 GitHub Actions。"

### 4. 治理与追踪（Governance & Tracking）

* 用户故事：作为 PMO，我要跟踪版本、状态、变更记录，并确保计划可复用与审查。
* 例1："/create-implementation-plan [PlanPurpose=feature-customer-portal] 更新 front matter 状态为 Planned 并生成状态徽章。"
* 例2："/create-implementation-plan [PlanPurpose=refactor-auth-module] 添加 tags 字段补充 `architecture`, `security`。"
* 例3："/create-implementation-plan [PlanPurpose=process-ai-handoff] 指定 owner 与 last_updated 用于审计。"
* 例4："/create-implementation-plan [PlanPurpose=infrastructure-aks-upgrade] 添加版本号与变更记录小节。"
* 例5："/create-implementation-plan [PlanPurpose=feature-notification-service] 输出 Related Specifications 列表供后续查阅。"

### 5. 风险、依赖与交付确认（Risks & Sign-off）

* 用户故事：作为风险控制负责人，我要在计划中看到依赖、风险、缓解策略与验收流程，确保可顺利执行与收尾。
* 例1："/create-implementation-plan [PlanPurpose=upgrade-payment-gateway] 标注关键外部依赖与 SLA 要求。"
* 例2："/create-implementation-plan [PlanPurpose=data-warehouse-sync] 列出 RISK-/ASSUMPTION- 项并提供缓解措施。"
* 例3："/create-implementation-plan [PlanPurpose=feature-ai-assistant] 说明测试计划与覆盖率门槛。"
* 例4："/create-implementation-plan [PlanPurpose=refactor-reporting] 补充验收标准与签核流程。"
* 例5："/create-implementation-plan [PlanPurpose=architecture-edge-gateway] 输出备用路径/回滚策略与触发条件。"

## 原始文件

* [create-implementation-plan.prompt.md](../../prompts/create-implementation-plan.prompt.md)
