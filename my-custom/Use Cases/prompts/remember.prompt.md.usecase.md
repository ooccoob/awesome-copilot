---
post_title: "remember.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "remember-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "memory", "context", "personalization"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Remember prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个通用的提示词，用于让 Copilot “记住”或“学习”一段特定的信息，以便在后续的对话或代码生成中加以利用。

## When

- 当你需要 Copilot 了解并遵循特定的项目约定、个人偏好或上下文信息时。
- 在希望 Copilot 能在当前会话中持续使用某个事实、代码片段或指令时。
- 在进行需要跨多轮对话保持上下文的任务时。

## Why

- 增强 Copilot 的上下文感知能力，使其提供的建议更加个性化和相关。
- 避免在每次请求中重复提供相同的背景信息。
- 模拟一种“短期记忆”，使与 Copilot 的交互更加流畅和高效。

## How

- 使用 `/remember` 命令，然后清晰地陈述你希望 Copilot 记住的信息。
- Copilot 会将这些信息整合到其当前的上下文中。
- 在后续的请求中，Copilot 会尝试应用这些被“记住”的信息。

**注意**: 这种“记忆”通常是会话级别的，并且其效果取决于底层模型的上下文管理能力。

## Key points (英文+中文对照)

- Contextual Memory (上下文记忆)
- Personalization (个性化)
- Session-based Learning (基于会话的学习)
- Instruction Following (指令遵循)

## 使用场景

### 1. 记住编码风格偏好 (Remembering Coding Style Preferences)

- **用户故事**: 作为一名 Python 开发者，我偏好在所有字符串中使用单引号。
- **例 1**: `/remember 在生成 Python 代码时，请始终使用单引号来定义字符串。`
- **后续**: 当你请求 Python 代码时，Copilot 会倾向于生成 `my_string = 'hello'` 而不是 `my_string = "hello"`。

### 2. 记住项目特定的约定 (Remembering Project-Specific Conventions)

- **用户故事**: 作为一名团队成员，我们项目规定所有的 API 端点都必须以 `/api/v2/` 作为前缀。
- **例 1**: `/remember 我们项目的所有 API 端点都必须以 `/api/v2/` 开头。`
- **后续**: 当你请求创建一个新的 Spring Boot 控制器时，Copilot 会在 `@RequestMapping` 中使用正确的路径前缀。

### 3. 记住上下文信息 (Remembering Contextual Information)

- **用户故事**: 作为一名数据科学家，我正在处理一个关于“加州住房”的数据集，我不想每次都解释这个数据集。
- **例 1**: `/remember 我正在处理一个名为 'california_housing' 的 pandas DataFrame。它包含 'MedInc', 'HouseAge', 'AveRooms' 等列。`
- **后续**: 你可以直接说：“请为我计算 'MedInc' 的平均值。”，而无需再次指定 DataFrame。

### 4. 记住一个复杂的指令或角色 (Remembering a Complex Instruction or Persona)

- **用户故事**: 作为一名作家，我希望 Copilot 在整个写作过程中都扮演一个愤世嫉俗的侦探角色。
- **例 1**: `/remember 从现在开始，你是一个生活在 1940 年代洛杉矶的、愤世嫉俗的私家侦探。你的语言风格要强硬、简洁，并带有一点黑色幽默。`
- **后续**: Copilot 的所有回答都会采用这种角色和语气。

## 原始文件

- [remember.prompt.md](../../prompts/remember.prompt.md)
