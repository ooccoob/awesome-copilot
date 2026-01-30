---
post_title: "documentation-writer.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "documentation-writer-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "documentation", "writing", "technical-writing"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Documentation Writer prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个通用的技术文档撰写提示词，可以根据给定的主题、代码或功能描述生成清晰、准确的文档。

## When

- 在需要为软件、API 或流程编写任何类型的技术文档时。
- 当开发人员需要帮助将技术概念转化为易于理解的文字时。
- 在创建教程、指南、API 参考或发行说明时。

## Why

- 提高文档撰写的效率和质量。
- 确保文档的风格、语气和术语在整个项目中保持一致。
- 帮助非专业作者（如开发人员）写出专业水平的文档。

## How

- 使用 `/documentation-writer` 命令，并提供你要文档化的主题、目标受众和任何相关的上下文或代码。
- AI 将生成一段结构良好、语言清晰的文档草稿。
- 你可以要求 AI 对草稿进行修改，例如“让它更简洁”、“为初学者解释这个概念”或“添加一个代码示例”。

## Key points (英文+中文对照)

- Technical Writing (技术写作)
- Content Generation (内容生成)
- Audience Awareness (受众意识)
- Clarity and Conciseness (清晰与简洁)

## 使用场景

### 1. 撰写 API 参考文档 (Writing API Reference Documentation)

- **用户故事**: 作为一名后端开发人员，我需要为我新创建的 `/widgets` API 端点编写文档。
- **例 1**: `/documentation-writer [selection=api_code.js] 为这个 API 端点编写文档，包括它的用途、参数、返回值和可能的错误代码。目标受众是前端开发人员。`
- **例 2**: `/documentation-writer 解释一下我们 API 的身份验证机制（OAuth 2.0），并提供一个获取访问令牌的示例。`

### 2. 创建用户指南或教程 (Creating User Guides or Tutorials)

- **用户故事**: 作为一名产品经理，我需要为我们的新功能“项目模板”编写一个分步教程。
- **例 1**: `/documentation-writer 编写一个教程，指导用户如何使用我们的项目模板功能创建一个新项目。`
- **例 2**: `/documentation-writer [selection=ui_screenshots] 根据这些 UI 截图，为我们的应用编写一个快速入门指南。`

### 3. 解释复杂的架构或概念 (Explaining Complex Architecture or Concepts)

- **用户故事**: 作为一名软件架构师，我需要向新团队成员解释我们系统的微服务架构。
- **例 1**: `/documentation-writer 撰写一篇文档，解释我们系统的事件驱动架构，包括消息队列和事件消费者的作用。`
- **例 2**: `/documentation-writer 用一个简单的比喻来解释什么是 Kubernetes。`

### 4. 撰写发行说明 (Writing Release Notes)

- **用户故事**: 作为一名发布经理，我需要为我们即将发布的 2.0 版本撰写发行说明。
- **例 1**: `/documentation-writer [selection=commit_logs.txt] 根据这些提交日志，为我们的 2.0 版本生成发行说明，重点突出新功能和重要的错误修复。`

## 原始文件

- [documentation-writer.prompt.md](../../prompts/documentation-writer.prompt.md)
