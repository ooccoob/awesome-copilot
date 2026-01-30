---
post_title: "generate-custom-instructions-from-codebase.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "generate-custom-instructions-from-codebase-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "prompt-engineering", "custom-instructions", "context-awareness"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Generate Custom Instructions from Codebase prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于分析代码库并自动生成 Copilot 自定义指令（Custom Instructions）的提示词。

## When

- 在开始在一个新的或不熟悉的代码库中工作时。
- 当希望 Copilot 的建议能更好地适应项目的特定编码风格、框架和约定。
- 在为团队或组织创建共享的 Copilot 配置时。

## Why

- 使 Copilot 能够提供更具上下文感知和项目特色的代码建议。
- 减少手动编写和维护自定义指令的工作量。
- 帮助新团队成员快速让他们的 Copilot 适应项目规范。

## How

- 使用 `/generate-custom-instructions-from-codebase` 命令。
- AI 将扫描你的工作区，分析文件类型、使用的框架、库、编码风格（如命名约定、注释风格）和项目结构。
- 基于分析结果，AI 会生成一组 `.instructions.md` 文件，你可以审查并应用这些指令来指导 Copilot 的行为。

## Key points (英文+中文对照)

- Contextual Awareness (上下文感知)
- Codebase Analysis (代码库分析)
- Style Adaptation (风格适应)
- Automated Configuration (自动化配置)

## 使用场景

### 1. 适应特定框架和库 (Adapting to Specific Frameworks and Libraries)

- **用户故事**: 作为一名前端开发人员，我加入了一个使用 Vue 3 和 Pinia 的项目。我希望 Copilot 能生成符合这些技术最佳实践的代码。
- **例 1**: `/generate-custom-instructions-from-codebase 分析我的项目，并生成指令，使 Copilot 优先使用 Composition API 和 Pinia stores。`
- **例 2**: `/generate-custom-instructions-from-codebase 我的项目是一个使用 Django 和 Django REST Framework 的后端。请生成指令，确保 Copilot 生成的代码遵循 Django 的模式。`

### 2. 遵循项目的编码规范 (Following Project's Coding Conventions)

- **用户故事**: 作为一名团队成员，我需要确保我提交的代码遵循团队严格的命名约定和注释标准。
- **例 1**: `/generate-custom-instructions-from-codebase 分析我们的 Python 代码库，并生成指令，强制所有私有方法都以单下划线开头。`
- **例 2**: `/generate-custom-instructions-from-codebase 请生成指令，要求 Copilot 在每个函数上方都添加 TSDoc 格式的注释。`

### 3. 理解项目结构和导入路径 (Understanding Project Structure and Import Paths)

- **用户故事**: 作为一名维护者，我们的项目有复杂的目录结构和自定义的模块别名。我希望 Copilot 能正确处理导入语句。
- **例 1**: `/generate-custom-instructions-from-codebase 分析我们的 `tsconfig.json` 和项目结构，生成指令以正确使用路径别名（如 `@/components`）。`

### 4. 推广内部库和组件的使用 (Promoting Use of Internal Libraries and Components)

- **用户故事**: 作为一名平台工程师，我希望鼓励团队成员使用我们公司内部的 UI 组件库，而不是第三方的。
- **例 1**: `/generate-custom-instructions-from-codebase 分析我们的代码，并生成指令，当需要一个按钮时，优先建议使用我们的 `InternalButton` 组件。`

## 原始文件

- [generate-custom-instructions-from-codebase.prompt.md](../../prompts/generate-custom-instructions-from-codebase.prompt.md)
