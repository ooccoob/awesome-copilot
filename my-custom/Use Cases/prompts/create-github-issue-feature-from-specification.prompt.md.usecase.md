---
post_title: "create-github-issue-feature-from-specification.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-github-issue-feature-from-specification-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "github", "issues", "project-management", "specification"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Create GitHub Issue from Specification prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于从功能规范文档中创建结构化的 GitHub Issue 的提示词。

## When

- 在功能规范已经编写完成并审查通过后。
- 当需要将一个大的功能拆解成可管理的任务并分配给团队成员时。
- 在项目管理工具中跟踪开发进度时。

## Why

- 确保每个 GitHub Issue 都包含所有必要的信息，如用户故事、验收标准和技术要求。
- 自动化创建过程，节省时间并减少手动复制粘贴的错误。
- 保持项目积压（backlog）的清晰和一致性。

## How

- 使用 `/create-github-issue-feature-from-specification` 命令并提供功能规范。
- AI 将解析规范并生成一个或多个格式化的 GitHub Issue，包含标题、正文（用户故事、验收标准等）、标签和可能的负责人。
- 你可以在创建实际的 Issue 之前审查和编辑生成的内容。

## Key points (英文+中文对照)

- Issue Creation (Issue 创建)
- Specification Breakdown (规范分解)
- Project Tracking (项目跟踪)
- Task Management (任务管理)

## 使用场景

### 1. 从产品需求文档 (PRD) 创建功能 Issue (Creating Feature Issues from a PRD)

- **用户故事**: 作为一名产品经理，我已经完成了一个新功能的 PRD，现在需要为开发团队创建对应的 GitHub Issues。
- **例 1**: `/create-github-issue-feature-from-specification [selection=new_feature_prd.md] 从这份 PRD 中为用户登录功能创建一个 GitHub Issue。`
- **例 2**: `/create-github-issue-feature-from-specification [selection=new_feature_prd.md] 将这份 PRD 中的每个主要部分都转换成一个独立的 GitHub Issue。`

### 2. 将技术设计文档分解为任务 (Breaking Down Technical Design Docs into Tasks)

- **用户故事**: 作为一名技术负责人，我编写了一份技术设计文档，现在需要将其分解为具体的开发任务。
- **例 1**: `/create-github-issue-feature-from-specification [selection=tech_design.md] 为数据库模式更改创建一个 GitHub Issue。`
- **例 2**: `/create-github-issue-feature-from-specification [selection=tech_design.md] 为 API 端点实现创建一系列的 GitHub Issues。`

### 3. 导入用户故事 (Importing User Stories)

- **用户故事**: 作为一名 Scrum Master，我需要将用户故事从我们的 wiki 页面导入到 GitHub Issues 中，以便进行 Sprint 规划。
- **例 1**: `/create-github-issue-feature-from-specification [selection=user_stories.txt] 将这些用户故事列表转换为 GitHub Issues。`

### 4. 错误报告的标准化 (Standardizing Bug Reports)

- **用户故事**: 作为一名 QA 工程师，我希望确保所有的错误报告都遵循一个标准的格式。
- **例 1**: `/create-github-issue-feature-from-specification [selection=bug_report_template.md] 使用这个模板，并根据我提供的重现步骤和预期结果创建一个 GitHub Issue。`

## 原始文件

- [create-github-issue-feature-from-specification.prompt.md](../../prompts/create-github-issue-feature-from-specification.prompt.md)
