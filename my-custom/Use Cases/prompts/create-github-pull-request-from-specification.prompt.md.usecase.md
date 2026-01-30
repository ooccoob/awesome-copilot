---
post_title: "create-github-pull-request-from-specification.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-github-pull-request-from-specification-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "github", "pull-request", "automation", "specification"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Create GitHub Pull Request from Specification prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于根据功能规范和代码更改自动生成 GitHub 拉取请求 (Pull Request, PR) 描述的提示词。

## When

- 当开发人员完成一个功能的编码并准备提交代码进行审查时。
- 当需要确保 PR 描述清晰、完整，并与相关的功能规范和 Issues 关联时。
- 在希望标准化团队的 PR 模板和流程时。

## Why

- 自动生成详细的 PR 描述，节省开发人员的时间。
- 确保审查者拥有审查代码所需的所有上下文信息，如功能目标、变更摘要和相关的 Issues。
- 提高代码审查的效率和质量。

## How

- 使用 `/create-github-pull-request-from-specification` 命令，并提供功能规范、相关的 GitHub Issues 链接以及代码更改的摘要（或 `git diff`）。
- AI 将生成一个格式化的 PR 描述，包括标题、变更摘要、如何测试、关联的 Issues 等。
- 开发人员可以将生成的描述复制到 GitHub 的 PR 创建页面。

## Key points (英文+中文对照)

- Pull Request Automation (拉取请求自动化)
- Code Review Context (代码审查上下文)
- Developer Productivity (开发人员生产力)
- Standardized Workflow (标准化工作流)

## 使用场景

### 1. 创建功能开发的 PR (Creating a PR for Feature Development)

- **用户故事**: 作为一名开发人员，我已经完成了一个新功能的开发，现在需要创建一个 PR 来合并我的代码。我希望 PR 描述能自动填充所有相关信息。
- **例 1**: `/create-github-pull-request-from-specification [specification=feature_spec.md] [issues=#123] [diff=git_diff.txt] 根据这份规范、关联的 Issue 和代码 diff，为我生成一个 PR 描述。`
- **例 2**: `/create-github-pull-request-from-specification [specification=feature_spec.md] 生成一个 PR 描述，总结我所做的更改，并链接到原始规范。`

### 2. 提交错误修复的 PR (Submitting a PR for a Bug Fix)

- **用户故事**: 作为一名工程师，我修复了一个紧急的 bug，需要快速创建一个清晰的 PR 以便审查和合并。
- **例 1**: `/create-github-pull-request-from-specification [specification=bug_report.md] [issues=#456] [diff=git_diff.txt] 为这个 bug 修复生成一个 PR 描述，解释问题的原因和我的解决方案。`

### 3. 标准化 PR 模板 (Standardizing PR Templates)

- **用户故事**: 作为一名技术负责人，我希望团队的所有 PR 都遵循相同的格式，以确保一致性和可读性。
- **例 1**: `/create-github-pull-request-from-specification [specification=template.md] 使用我们的团队 PR 模板，并根据我提供的功能信息填充内容。`

### 4. 自动化版本发布的 PR (Automating PRs for Release Versioning)

- **用户故事**: 作为一名发布经理，我需要创建一个 PR，将 `develop` 分支的更改合并到 `main` 分支以进行新版本发布。
- **例 1**: `/create-github-pull-request-from-specification [specification=release_notes.md] [diff=git_diff_develop_main.txt] 生成一个版本发布 PR 的描述，其中包含版本说明和自上次发布以来的所有代码更改摘要。`

## 原始文件

- [create-github-pull-request-from-specification.prompt.md](../../prompts/create-github-pull-request-from-specification.prompt.md)
