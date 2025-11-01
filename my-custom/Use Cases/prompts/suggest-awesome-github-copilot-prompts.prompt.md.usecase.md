---
post_title: "suggest-awesome-github-copilot-prompts.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "suggest-awesome-github-copilot-prompts-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "github-copilot", "prompts", "ideation"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Suggest Awesome GitHub Copilot Prompts prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个元提示词（meta-prompt），用于头脑风暴和构思新的、有用的 GitHub Copilot 提示词（Prompts）。

## When

- 当你有一个可以被 AI 自动化的任务，但不确定如何将其表述为一个好的提示词时。
- 在为 `awesome-copilot` 这样的社区仓库贡献新的提示词想法时。
- 在探索 AI 在软件开发生命周期中新的应用可能性时。

## Why

- 作为一个创意引擎，帮助社区发现和定义新的、有价值的 Copilot 用例。
- 帮助将一个高层次的想法（例如“我想让 AI 帮我重构代码”）具体化为一个可操作的、结构化的提示词定义。
- 促进 Copilot 提示词生态的丰富和创新。

## How

- 使用 `/suggest-awesome-github-copilot-prompts` 命令，并分享你希望 AI 帮助解决的任务或问题。
- AI 将与你一起探讨这个想法，并帮助你定义：
    - 提示词的名称（例如 `refactor-to-async-await.prompt.md`）。
    - 提示词的目的和使用场景。
    - 提示词的模式（`mode`）：是应该作为一个一次性的问答（`ask`）还是一个交互式的代理（`agent`）。
    - 提示词的核心指令和行为。
- （可选）为你生成一个 `.prompt.md` 文件的草稿。

## Key points (英文+中文对照)

- Prompt Ideation (提示词构思)
- Use Case Discovery (用例发现)
- Community Brainstorming (社区头脑风暴)
- Feature Prototyping (功能原型设计)

## 使用场景

### 1. 自动化常见的重构任务 (Automating Common Refactoring Tasks)

- **用户故事**: 作为一名 JavaScript 开发者，我经常需要将使用 Promise `.then()` 语法的旧代码重构为使用 `async/await`。
- **例 1**: `/suggest-awesome-github-copilot-prompts 我想要一个能自动将 Promise `.then()` 链重构为 `async/await` 的提示词。` -> AI 会帮你设计这个提示词，并建议它可以如何处理错误（`catch` -> `try/catch`）。

### 2. 生成特定类型的测试 (Generating Specific Types of Tests)

- **用户故事**: 作为一名 QA 工程师，我希望有一个提示词能专门为我的 API 端点生成集成测试。
- **例 1**: `/suggest-awesome-github-copilot-prompts 帮我设计一个提示词，它可以读取一个 OpenAPI 规范文件，并为其中的每个端点生成一个基本的 Jest/Supertest 集成测试。`

### 3. 创建项目脚手架或配置文件 (Creating Project Scaffolding or Config Files)

- **用户故事**: 作为一名 DevOps 工程师，我厌倦了每次都手动创建 `Dockerfile`。
- **例 1**: `/suggest-awesome-github-copilot-prompts 我想创建一个提示词，它能根据我的项目类型（如 Node.js, Python, Java）为我生成一个优化的、多阶段的 `Dockerfile`。`

### 4. 辅助学习和理解代码 (Aiding in Learning and Understanding Code)

- **用户故事**: 作为一名编程初学者，我经常对复杂的算法感到困惑。
- **例 1**: `/suggest-awesome-github-copilot-prompts 帮我构思一个“算法解释器”提示词。当我选中一段算法代码时，它应该能用简单的语言、伪代码和流程图来解释这个算法是如何工作的。`

## 原始文件

- [suggest-awesome-github-copilot-prompts.prompt.md](../../prompts/suggest-awesome-github-copilot-prompts.prompt.md)
