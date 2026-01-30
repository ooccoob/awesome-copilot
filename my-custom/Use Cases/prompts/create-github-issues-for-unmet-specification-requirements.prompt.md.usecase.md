---
post_title: "create-github-issues-for-unmet-specification-requirements.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-github-issues-for-unmet-specification-requirements-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "github", "issues", "project-management", "gap-analysis"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Create GitHub Issues for Unmet Specification Requirements prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于比较实施计划或现有代码与功能规范，识别未满足的需求，并为这些差距创建 GitHub Issues 的提示词。

## When

- 在开发周期中进行差距分析时。
- 在代码审查或测试阶段发现功能缺失时。
- 当需要确保最终产品完全符合最初的设计规范时。

## Why

- 自动识别规范与实现之间的差距，防止需求遗漏。
- 为每个未满足的需求创建明确的、可操作的 Issue，便于跟踪和修复。
- 提高产品的完整性和质量。

## How

- 使用 `/create-github-issues-for-unmet-specification-requirements` 命令，并同时提供功能规范和实施计划（或代码摘要）。
- AI 将进行比较，找出实施计划中未覆盖或未完全满足的规范要求。
- 为每个发现的差距生成一个 GitHub Issue，详细说明缺失的功能。

## Key points (英文+中文对照)

- Gap Analysis (差距分析)
- Requirement Traceability (需求可追溯性)
- Quality Assurance (质量保证)
- Automated Issue Creation (自动化 Issue 创建)

## 使用场景

### 1. 实施计划与规范的对齐检查 (Aligning Implementation Plan with Specification)

- **用户故事**: 作为一名产品经理，在开发开始之前，我需要确保技术团队的实施计划完全覆盖了我的产品需求文档 (PRD) 中的所有要求。
- **例 1**: `/create-github-issues-for-unmet-specification-requirements [specification=prd.md] [implementation=plan.md] 比较 PRD 和实施计划，为计划中遗漏的任何功能点创建 GitHub Issues。`
- **例 2**: `/create-github-issues-for-unmet-specification-requirements [specification=prd.md] [implementation=plan.md] 检查实施计划是否包含了 PRD 中所有的非功能性需求，如性能和安全性要求。`

### 2. 代码审查期间的功能完整性检查 (Feature Completeness Check During Code Review)

- **用户故事**: 作为一名技术负责人，在审查一个新功能的拉取请求时，我需要验证它是否实现了规范中的所有验收标准。
- **例 1**: `/create-github-issues-for-unmet-specification-requirements [specification=feature_spec.md] [implementation=code_summary.txt] 将此代码摘要与功能规范进行比较，为未实现的验收标准创建 Issues。`

### 3. 测试阶段发现的需求差距 (Identifying Requirement Gaps in Testing Phase)

- **用户故事**: 作为一名 QA 工程师，我发现当前版本缺少规范中定义的几个次要功能。我需要为这些缺失的功能创建错误报告。
- **例 1**: `/create-github-issues-for-unmet-specification-requirements [specification=spec.md] [implementation=test_results.md] 根据这份测试报告和原始规范，为所有失败或未覆盖的测试用例（代表未满足的需求）创建 Issues。`

### 4. 项目审计和合规性验证 (Project Audit and Compliance Verification)

- **用户故事**: 作为一名项目审计员，我需要验证已完成的项目是否满足所有合同中规定的要求。
- **例 1**: `/create-github-issues-for-unmet-specification-requirements [specification=contract_requirements.md] [implementation=final_product_docs.md] 比较合同要求和最终产品文档，为任何不匹配项创建需要整改的 Issues。`

## 原始文件

- [create-github-issues-for-unmet-specification-requirements.prompt.md](../../prompts/create-github-issues-for-unmet-specification-requirements.prompt.md)
