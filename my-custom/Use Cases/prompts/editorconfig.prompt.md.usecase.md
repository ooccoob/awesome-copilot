---
post_title: "editorconfig.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "editorconfig-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "editorconfig", "code-style", "formatting"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the EditorConfig prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于生成或更新 `.editorconfig` 文件的提示词，帮助团队在不同的编辑器和 IDE 之间保持一致的编码风格。

## When

- 在创建新项目时，需要建立编码风格规范。
- 当团队成员使用不同的开发环境，导致代码格式不一致时。
- 在希望自动化代码格式化规则的执行时。

## Why

- 确保代码库的风格一致性，提高可读性。
- 减少因格式问题在代码审查中产生的噪音。
- 自动配置开发人员的编辑器，无需手动设置。

## How

- 使用 `/editorconfig` 命令并描述你的编码风格偏好。
- AI 将生成一个 `.editorconfig` 文件，其中包含针对不同文件类型的规则，如缩进样式、缩进大小、字符集等。
- 你可以将此文件放置在项目的根目录中，大多数现代编辑器会自动识别并应用这些规则。

## Key points (英文+中文对照)

- Code Style Consistency (代码风格一致性)
- Formatting Rules (格式化规则)
- Cross-Editor Configuration (跨编辑器配置)
- Readability (可读性)

## 使用场景

### 1. 为新项目创建 `.editorconfig` (Creating `.editorconfig` for a New Project)

- **用户故事**: 作为一名技术负责人，我正在启动一个新的 TypeScript 项目，我希望确保所有团队成员都使用相同的代码格式。
- **例 1**: `/editorconfig 为一个 TypeScript 项目创建一个 `.editorconfig` 文件。要求使用 2 个空格缩进，UTF-8 编码，并在文件末尾保留一个空行。`
- **例 2**: `/editorconfig 我需要一个适用于 Python 项目的 `.editorconfig`，遵循 PEP 8 风格指南。`

### 2. 统一现有项目的编码风格 (Unifying Code Style in an Existing Project)

- **用户故事**: 作为一名开发人员，我注意到我们的代码库中混合了制表符和空格，我想统一使用空格。
- **例 1**: `/editorconfig 生成一个 `.editorconfig` 文件，强制所有 `.js`, `.css`, 和 `.html` 文件都使用 4 个空格进行缩进。`

### 3. 基于多种语言的项目配置 (Configuration for a Polyglot Project)

- **用户故事**: 作为一名全栈开发人员，我的项目同时包含 Java 后端和 React 前端。我需要一个 `.editorconfig` 来处理这两种语言。
- **例 1**: `/editorconfig 创建一个 `.editorconfig`，为 `.java` 文件设置 4 个空格缩进，为 `.jsx` 和 `.tsx` 文件设置 2 个空格缩进。`

### 4. 与 Linter 和 Formatter 集成 (Integration with Linters and Formatters)

- **用户故事**: 作为一名 DevOps 工程师，我希望我们的 `.editorconfig` 文件能与 Prettier 和 ESLint 协同工作。
- **例 1**: `/editorconfig 生成一个与 Prettier 兼容的 `.editorconfig` 文件。`

## 原始文件

- [editorconfig.prompt.md](../../prompts/editorconfig.prompt.md)
