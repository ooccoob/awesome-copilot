---
post_title: "create-github-action-workflow-specification.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-github-action-workflow-specification-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "github", "actions", "cicd", "specification"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Create GitHub Action Workflow Specification prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于生成 GitHub Action 工作流规范的提示词，该规范详细描述了 CI/CD 流程的触发器、作业、步骤和依赖项。

## When

- 在为项目设置新的 CI/CD 流程时。
- 当需要将现有的构建和部署流程自动化时。
- 在团队中标准化工作流的最佳实践时。

## Why

- 确保工作流的设计清晰、完整且易于理解。
- 促进团队成员之间的协作和代码审查。
- 作为自动化脚本实现的基础，减少手动错误。

## How

- 使用 `/create-github-action-workflow-specification` 命令并描述你的 CI/CD 需求。
- AI 将生成一个详细的工作流规范，包括触发事件、环境变量、作业和步骤。
- 你可以根据需要审查和修改此规范，然后用它来创建实际的 `.github/workflows/your-workflow.yml` 文件。

## Key points (英文+中文对照)

- Workflow Specification (工作流规范)
- Continuous Integration (持续集成)
- Continuous Deployment (持续部署)
- Triggers and Jobs (触发器和作业)

## 使用场景

### 1. 新项目的 CI/CD 设置 (CI/CD Setup for New Projects)

- **用户故事**: 作为一名 DevOps 工程师，我需要为一个新的 Node.js 项目设置一个 CI 工作流，该工作流在每次推送到 `main` 分支时运行测试和 linting。
- **例 1**: `/create-github-action-workflow-specification [selection=project_requirements.md] 为这个 Node.js 项目创建一个 CI 工作流规范，包括安装依赖、运行测试和 linting。`
- **例 2**: `/create-github-action-workflow-specification 我需要一个在每次创建拉取请求时触发的 GitHub Action 工作流规范。`

### 2. 部署到云服务 (Deployment to Cloud Services)

- **用户故事**: 作为一名开发人员，我希望自动化将我的 Web 应用部署到 Azure App Service 的过程。
- **例 1**: `/create-github-action-workflow-specification 创建一个工作流规范，用于在代码合并到 `main` 分支后，构建 Docker 镜像并将其部署到 Azure App Service。`
- **例 2**: `/create-github-action-workflow-specification 我需要一个规范，用于将静态网站部署到 GitHub Pages。`

### 3. 发布包到仓库 (Publishing Packages to a Registry)

- **用户故事**: 作为一名库作者，我希望在创建新的 Git 标签时，自动将我的 npm 包发布到 npmjs.com。
- **例 1**: `/create-github-action-workflow-specification 创建一个工作流规范，用于在打上 `v*.*.*` 格式的标签时，将 npm 包发布到公共仓库。`
- **例 2**: `/create-github-action-workflow-specification 我需要一个规范，用于将 Python 包发布到 PyPI。`

### 4. 复杂的多阶段工作流 (Complex Multi-Stage Workflows)

- **用户故事**: 作为一名技术负责人，我需要设计一个多阶段的 CI/CD 流程，包括构建、测试、阶段性部署和生产部署，并需要审批步骤。
- **例 1**: `/create-github-action-workflow-specification 设计一个包含构建、单元测试、集成测试和手动审批后部署到生产环境的工作流规范。`

## 原始文件

- [create-github-action-workflow-specification.prompt.md](../../prompts/create-github-action-workflow-specification.prompt.md)
