---
post_title: "suggest-awesome-github-copilot-instructions.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "suggest-awesome-github-copilot-instructions-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "github-copilot", "custom-instructions", "ideation"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Suggest Awesome GitHub Copilot Instructions prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于构思和创建新的 GitHub Copilot 自定义指令（Custom Instructions）的提示词。

## When

- 当你希望 Copilot 在特定文件类型或项目中遵循特定规则或风格时。
- 在需要微调 Copilot 的行为以更好地适应个人或团队的编码习惯时。
- 在为 `awesome-copilot` 这样的社区项目贡献新的、可重用的指令时。

## Why

- 帮助用户将他们的编码偏好或项目要求形式化为 Copilot 可以理解的指令。
- 激发关于如何通过指令来增强 Copilot 能力的新想法。
- 简化创建 `.instructions.md` 文件的过程。

## How

- 使用 `/suggest-awesome-github-copilot-instructions` 命令，并描述你希望 Copilot 遵循的规则或行为。
- AI 将帮助你将这个想法转化为一个结构化的指令，包括指令的描述和应用的范围（`applyTo`）。
- （可选）为你生成一个 `.instructions.md` 文件的完整草稿。

## Key points (英文+中文对照)

- Behavior Tuning (行为微调)
- Rule Enforcement (规则执行)
- Style Guidance (风格指导)
- Contextual Configuration (上下文配置)

## 使用场景

### 1. 强制执行编码风格 (Enforcing a Coding Style)

- **用户故事**: 作为一名 Python 开发者，我希望我所有的函数定义都包含类型提示（type hints）。
- **例 1**: `/suggest-awesome-github-copilot-instructions 我想创建一个指令，要求 Copilot 在生成任何 Python 函数时都必须添加类型提示。` -> AI 会帮你生成一个指令，应用到 `**.py` 文件，并描述这个要求。

### 2. 遵循框架的最佳实践 (Following Framework Best Practices)

- **用户故事**: 作为一名 Angular 开发者，我希望 Copilot 生成的组件总是遵循“关注点分离”的原则，将模板放在 `.html` 文件，样式放在 `.scss` 文件。
- **例 1**: `/suggest-awesome-github-copilot-instructions 帮我创建一个指令，当在 `.ts` 文件中生成 Angular 组件时，提醒我不要使用内联模板（inline template）或内联样式（inline styles）。`

### 3. 推广内部 API 或库的使用 (Promoting Internal APIs or Libraries)

- **用户故事**: 作为一名平台团队的成员，我们公司有一个自研的日志库 `my-corp-logger`，我希望所有新代码都用它来代替 `console.log`。
- **例 1**: `/suggest-awesome-github-copilot-instructions 我想创建一个指令，在所有的 JavaScript/TypeScript 文件中，如果 Copilot 要生成日志输出，它应该优先使用 `my-corp-logger`。`

### 4. 添加特定的注释或元数据 (Adding Specific Comments or Metadata)

- **用户故事**: 作为一名开源项目维护者，我要求每个新文件的头部都必须包含一个许可证声明的注释。
- **例 1**: `/suggest-awesome-github-copilot-instructions 帮我创建一个指令，在创建任何新文件时，自动在文件顶部插入我们的 MIT 许可证注释头。`

## 原始文件

- [suggest-awesome-github-copilot-instructions.prompt.md](../../prompts/suggest-awesome-github-copilot-instructions.prompt.md)
