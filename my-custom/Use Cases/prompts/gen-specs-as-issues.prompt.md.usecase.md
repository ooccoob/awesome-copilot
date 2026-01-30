---
post_title: "gen-specs-as-issues.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "gen-specs-as-issues-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "github", "issues", "specification", "project-management"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Generate Specifications as Issues prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于将功能规范文档自动分解并生成为多个结构化的 GitHub Issues 的提示词。

## When

- 在功能规范或产品需求文档 (PRD) 编写完成后。
- 当需要将一个大的功能或 Epic 分解为更小的、可管理的开发任务时。
- 在项目规划或 Sprint 规划会议上，为开发团队分配工作时。

## Why

- 自动化从文档到任务列表的转换，极大地提高了项目管理的效率。
- 确保每个 Issue 都与规范中的特定部分相关联，保持需求的可追溯性。
- 生成的 Issues 格式统一，包含所有必要信息，便于开发人员理解和执行。

## How

- 使用 `/gen-specs-as-issues` 命令并提供你的规范文档。
- AI 将通读并理解文档的结构，识别出可以被分解为独立任务的各个部分（如不同的用户故事、功能点或技术组件）。
- 为每个识别出的任务生成一个 GitHub Issue，包含标题、描述（引用规范原文）、验收标准和建议的标签。

## Key points (英文+中文对照)

- Specification Decomposition (规范分解)
- Bulk Issue Generation (批量 Issue 生成)
- Task Granularity (任务粒度)
- Traceability Matrix (可追溯性矩阵)

## 使用场景

### 1. 将 PRD 分解为用户故事 (Decomposing a PRD into User Stories)

- **用户故事**: 作为一名产品负责人，我已经完成了一个关于“用户个人资料重构”的 PRD，现在需要将其中的每个用户故事都创建为一个 GitHub Issue。
- **例 1**: `/gen-specs-as-issues [selection=prd.md] 将这份 PRD 中的所有用户故事转换为独立的 GitHub Issues。`
- **例 2**: `/gen-specs-as-issues [selection=prd.md] 分析这份规范，并为每个一级标题下的功能点创建一个 Issue。`

### 2. 将技术设计文档转化为开发任务 (Turning a Technical Design Doc into Dev Tasks)

- **用户故事**: 作为一名软件架构师，我编写了一份详细的系统设计文档，现在需要为后端、前端和数据库团队创建各自的任务。
- **例 1**: `/gen-specs-as-issues [selection=tech_design.md] 根据这份技术设计，为所有 API 端点的实现创建 GitHub Issues，并打上 `backend` 标签。`
- **例 2**: `/gen-specs-as-issues [selection=tech_design.md] 为文档中描述的每个数据库表模式的更改创建一个 Issue。`

### 3. 创建测试用例的占位符 (Creating Placeholders for Test Cases)

- **用户故事**: 作为一名 QA 负责人，我希望根据功能规范，为每个功能点预先创建好测试任务的 Issue。
- **例 1**: `/gen-specs-as-issues [selection=spec.md] 为这份规范中的每个验收标准创建一个对应的测试任务 Issue，并打上 `qa` 和 `testing` 标签。`

### 4. 迁移计划的任务化 (Task-ifying a Migration Plan)

- **用户故事**: 作为一名 DevOps 工程师，我制定了一个从旧系统到新系统的详细迁移计划，现在需要将计划中的每一步都变成一个可跟踪的 Issue。
- **例 1**: `/gen-specs-as-issues [selection=migration_plan.md] 将这份迁移计划的每个阶段（如数据备份、数据迁移、DNS 切换）都转换为一个 GitHub Issue。`

## 原始文件

- [gen-specs-as-issues.prompt.md](../../prompts/gen-specs-as-issues.prompt.md)
