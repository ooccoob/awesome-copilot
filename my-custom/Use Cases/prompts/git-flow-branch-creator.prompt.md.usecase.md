---
post_title: "git-flow-branch-creator.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "git-flow-branch-creator-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "git", "git-flow", "branching", "automation"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Git Flow Branch Creator prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于根据 Git Flow 工作流约定自动创建和切换到新分支的提示词。

## When

- 在开始开发新功能、修复错误或准备发布时。
- 当团队采用 Git Flow 作为其分支策略时。
- 在希望简化和标准化分支创建过程时。

## Why

- 自动化分支命名和创建，减少手动输入错误。
- 确保所有分支都遵循一致的命名约定（如 `feature/`, `bugfix/`, `release/`）。
- 提高开发工作流的效率。

## How

- 使用 `/git-flow-branch-creator` 命令并描述你将要开始的工作。
- AI 将根据你的描述确定分支类型（feature, bugfix, hotfix, release）和分支名称。
- 生成并执行 `git checkout -b <branch-name>` 命令，为你创建并切换到新分支。

## Key points (英文+中文对照)

- Git Flow (Git 工作流)
- Branching Strategy (分支策略)
- Naming Conventions (命名约定)
- Workflow Automation (工作流自动化)

## 使用场景

### 1. 开始一个新功能开发 (Starting a New Feature)

- **用户故事**: 作为一名开发人员，我将要开始开发一个新的“用户登录”功能。
- **例 1**: `/git-flow-branch-creator 我要开始做用户登录功能了。` -> AI 执行 `git checkout -b feature/user-login`
- **例 2**: `/git-flow-branch-creator 从 issue #123 开始创建一个新功能分支。` -> AI 执行 `git checkout -b feature/issue-123-some-description`

### 2. 修复一个 Bug (Fixing a Bug)

- **用户故事**: 作为一名工程师，我需要修复一个在 `develop` 分支上发现的 bug。
- **例 1**: `/git-flow-branch-creator 修复一个导致表单无法提交的 bug。` -> AI 执行 `git checkout -b bugfix/form-submission-error`
- **例 2**: `/git-flow-branch-creator 我要处理 bug #456。` -> AI 执行 `git checkout -b bugfix/456-fix-null-pointer`

### 3. 进行紧急线上修复 (Making a Hotfix)

- **用户故事**: 作为一名运维工程师，我需要紧急修复一个在生产环境 (`main` 分支) 发现的严重问题。
- **例 1**: `/git-flow-branch-creator 紧急修复线上支付失败的问题。` -> AI 从 `main` 分支创建并执行 `git checkout -b hotfix/payment-gateway-failure`

### 4. 准备一个新版本发布 (Preparing a New Release)

- **用户故事**: 作为一名发布经理，我需要开始准备 `v1.2.0` 版本的发布工作。
- **例 1**: `/git-flow-branch-creator 准备发布 1.2.0 版本。` -> AI 从 `develop` 分支创建并执行 `git checkout -b release/1.2.0`

## 原始文件

- [git-flow-branch-creator.prompt.md](../../prompts/git-flow-branch-creator.prompt.md)
