---
post_title: "implementation-plan.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "implementation-plan-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "implementation-plan"]
ai_note: "Generated with AI assistance."
summary: "面向 AI/人协同的、可执行实现计划生成：阶段化、机器可解析、零歧义。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 生成面向自动化执行的实现计划，包含阶段/任务/校验与依赖，严格遵循模板与命名约束。

## When

- 需要以 AI-to-AI 方式交接；多人并行实施；要求可追踪、可度量、可自动验证的任务清单时。

## Why

- 通过确定性语言与结构化约束，减少理解偏差，提升复用与自动化可执行性。

## How

- 遵循固定 Front matter 与章节；采用 REQ/TASK/GOAL/DEP/TEST 等前缀；放置到 /plan/ 目录，文件名按 purpose 前缀；严禁占位符残留；每任务需有完成标准与可验证步骤。

## Key points (英文+中文对照)

- Deterministic language.（确定性语言）
- Machine-parseable plans.（可被机器解析）
- Independent phases.（相互独立的阶段）
- Explicit dependencies.（显式依赖）
- Validation criteria.（可验证标准）

## 使用场景

### 1. 新功能落地计划（Feature implementation plan）

- 用户故事：作为开发负责人，我要把新功能拆解为阶段化任务并可由代理执行。
- 例 1："生成 feature-user-onboarding-1.md，含两个阶段与各自 `TASK-*`。"
- 例 2："为每个任务给出完成标记与日期栏位。"
- 例 3："将依赖库与环境前置条件写入 Dependencies。"
- 例 4："为关键任务补充自动验证步骤。"
- 例 5："输出与规范/研究的交叉引用。"

### 2. 重构与迁移（Refactor/migration）

- 用户故事：作为维护者，我要约束重构范围并确保不停机迁移可执行。
- 例 1："生成 refactor-auth-module-1.md，任务不可跨阶段依赖。"
- 例 2："把风险与回滚策略写为独立任务。"
- 例 3："定义不修改行为的验证标准。"
- 例 4："列出接口稳定性与兼容性要求。"
- 例 5："把测试覆盖率阈值纳入验证。"

### 3. 多人并行（Parallelizable execution）

- 用户故事：作为项目经理，我需要任务具备并行性与明确边界。
- 例 1："将 I/O 无关的任务并列到同一阶段。"
- 例 2："在任务描述中写明文件路径与函数名。"
- 例 3："给出共享工件与接口契约。"
- 例 4："补充冲突解决与合并策略。"
- 例 5："用状态徽章体现当前状态。"

### 4. 自动化代理协作（Agent-to-agent handoff）

- 用户故事：作为自动化平台，我要把计划直接喂给执行代理并获得可核对的结果。

- 例 1："为每个任务添加可编程的执行步骤与校验脚本引用。"
- 例 2："确保不依赖外部隐性上下文。"
- 例 3："将配置与常量显式列出。"
- 例 4："输出一键执行与分阶段停靠选项。"
- 例 5："提供完成后摘要与链接清单。"

### 5. 与规范/研究对齐（Alignment with spec/research）

- 用户故事：作为评审者，我希望计划与规范/研究严格对齐且可追溯来源。
- 例 1："在计划中引用 `spec-*` 与 `research-*` 的具体文件名。"
- 例 2："把约束与风险映射到具体 TASK。"
- 例 3："将验证标准对应到 Acceptance Criteria。"
- 例 4："在完成标准中加入覆盖率/性能阈值。"
- 例 5："显式标记外部依赖的准备状态。"

## 原始文件

- chatmodes/implementation-plan.chatmode.md
