---
post_title: "bicep-plan.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "bicep-plan-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","bicep","infra-as-code"]
ai_note: "Generated with AI assistance."
summary: "Bicep plan 用例：基础设施描述、参数化与部署验证场景。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供 Bicep 模板规划、参数化与预览部署结果（plan）的用例集合。

## When

- 在撰写基础设施模板、进行变更审查或生成部署预览时使用。

## Why

- 确保基础设施变更是可重现、可审计并且具有最小影响范围。

## How

- 包括生成 plan 的命令、示例参数文件、变更影响评估与回滚建议。

## Key points (英文+中文对照)

- Parameterization（参数化）
- Idempotency（幂等性）
- Preview & validation（预览与校验）
- Impact analysis（影响分析）
- Rollback planning（回退计划）

## 使用场景

### 1. 变更预览（Change Preview）

- 用户故事：作为平台工程师，我要在合并前预览 Bicep 变更的影响。
- 例 1：生成 plan 并列出将修改/创建/删除的资源。
- 例 2：比较不同参数组合的计划差异。
- 例 3：自动化在 PR 中附带 plan 输出的示例脚本。
- 例 4：策略为有风险变更触发人工审查。
- 例 5：记录 plan 输出以便审计。

### 2. 参数化部署

- 用户故事：作为 DevOps，我要使用环境参数重复部署相同模板到不同订阅/环境。
- 例 1：参数文件示例与 secrets 管理建议。
- 例 2：区域/规模/命名约定的参数化示例。
- 例 3：示例验证脚本，确保参数满足策略。
- 例 4：参数变更影响回归测试示例。
- 例 5：参数模板版本化示例。

### 3. 影响评估与审批

- 用户故事：作为变更经理，我要在部署前评估变更风险与影响范围。
- 例 1：自动生成变更清单与受影响资源树示例。
- 例 2：触发基于影响范围的审批流程示例。
- 例 3：示例 tag/label 策略以标识关键资源。
- 例 4：示例回退触发条件。
- 例 5：生成变更记录并归档示例。

### 4. 合规与策略校验

- 用户故事：作为安全合规工程师，我要验证模板是否符合组织策略。
- 例 1：示例 Azure Policy 与 Bicep 中的条件性注释。
- 例 2：示例自动化校验步骤在 CI 中运行。
- 例 3：策略违规时的阻断/告警示例。
- 例 4：示例策略报表导出。
- 例 5：合规审计中使用的 plan 片段示例。

### 5. 回退与恢复演练

- 用户故事：作为 SRE，我需要确保变更可快速回退且可恢复。
- 例 1：示例回退 playbook。
- 例 2：生成并保存先前成功部署的状态描述用于回退。
- 例 3：演练回退策略与验证脚本示例。
- 例 4：资源删除场景的安全检查示例。
- 例 5：回退后验证一致性示例。

## 原始文件

- [chatmodes/bicep-plan.chatmode.md](../../../chatmodes/bicep-plan.chatmode.md)
