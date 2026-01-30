---
post_title: "create-github-issues-feature-from-implementation-plan.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-github-issues-feature-from-implementation-plan-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "github", "issues", "project-management", "implementation-plan"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Create GitHub Issues from Implementation Plan prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于从实施计划中批量创建 GitHub Issues 的提示词，将计划中的每个步骤或任务转换为一个独立的 Issue。

## When

- 在实施计划已经制定并获得批准后。
- 当需要将详细的实施步骤分配给开发团队并进行跟踪时。
- 在敏捷开发流程中，为下一个 Sprint 准备工作项时。

## Why

- 自动化从计划到可执行任务的转换过程，提高效率。
- 确保每个 Issue 都与实施计划中的特定部分直接对应，便于跟踪进度。
- 保持 GitHub Issues 与项目计划的一致性。

## How

- 使用 `/create-github-issues-feature-from-implementation-plan` 命令并提供实施计划文档。
- AI 将解析计划，为其中的每个主要任务或步骤创建一个结构化的 GitHub Issue。
- 生成的 Issues 将包含标题、描述（链接回实施计划的相应部分）和建议的标签。

## Key points (英文+中文对照)

- Bulk Issue Creation (批量 Issue 创建)
- Plan to Action (从计划到行动)
- Traceability (可追溯性)
- Agile Workflow (敏捷工作流)

## 使用场景

### 1. 将技术实施计划转化为开发任务 (Converting a Technical Implementation Plan into Dev Tasks)

- **用户故事**: 作为一名软件架构师，我已经完成了一个新微服务的实施计划，现在需要将其分解为开发团队可以领取的具体任务。
- **例 1**: `/create-github-issues-feature-from-implementation-plan [selection=microservice_plan.md] 根据这份实施计划，为每个阶段（如模型定义、API 实现、测试）创建 GitHub Issues。`
- **例 2**: `/create-github-issues-feature-from-implementation-plan [selection=microservice_plan.md] 为计划中的所有数据库迁移任务创建 GitHub Issues。`

### 2. 项目重构的任务分解 (Task Breakdown for a Project Refactoring)

- **用户故事**: 作为一名高级工程师，我正在领导一个大型代码库的重构工作，并制定了详细的计划。我需要将计划中的每一步都变成一个 Issue。
- **例 1**: `/create-github-issues-feature-from-implementation-plan [selection=refactoring_plan.md] 为重构计划中的每个模块创建一个 GitHub Issue。`
- **例 2**: `/create-github-issues-feature-from-implementation-plan [selection=refactoring_plan.md] 将计划中的“更新依赖项”部分转换为一个 Issue，并标记为 `chore`。`

### 3. 为 Sprint 填充 Backlog (Populating the Backlog for a Sprint)

- **用户故事**: 作为一名 Scrum Master，我们需要为即将到来的 Sprint 准备工作。我已经有了一个包含本 Sprint 要完成的功能的实施计划。
- **例 1**: `/create-github-issues-feature-from-implementation-plan [selection=sprint_plan.md] 从这份 Sprint 计划中为所有后端任务创建 GitHub Issues。`

### 4. 基础设施即代码 (IaC) 的部署计划 (Deployment Plan for Infrastructure as Code)

- **用户故事**: 作为一名 DevOps 工程师，我编写了一个使用 Terraform 部署新基础设施的计划，现在需要为每个步骤创建跟踪任务。
- **例 1**: `/create-github-issues-feature-from-implementation-plan [selection=iac_plan.md] 为计划中的“配置网络”和“创建虚拟机”步骤创建 GitHub Issues。`

## 原始文件

- [create-github-issues-feature-from-implementation-plan.prompt.md](../../prompts/create-github-issues-feature-from-implementation-plan.prompt.md)
