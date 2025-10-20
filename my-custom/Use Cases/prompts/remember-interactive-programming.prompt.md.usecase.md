---
post_title: "remember-interactive-programming.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "remember-interactive-programming-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "clojure", "joyride", "interactive-programming", "memory"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Remember Interactive Programming prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于在 Joyride（一个 VS Code 的 ClojureScript 交互式编程环境）会话中动态地将信息“记住”（即存储到内存中）的提示词。

## When

- 在进行交互式编程或探索性编码时，需要临时存储和引用数据、函数或配置。
- 当需要跨多个 Joyride 命令或评估步骤共享状态时。
- 在构建需要上下文记忆的复杂 Joyride 脚本时。

## Why

- 提供了一种轻量级的方式来在交互式会话中维护状态，而无需创建临时文件或修改全局变量。
- 使得构建更复杂的、有状态的 Joyride 工作流成为可能。
- 提高了交互式编程的灵活性和能力。

## How

- 使用 `/remember-interactive-programming` 命令，并提供你想要记住的键和值。
- AI 将生成并执行一个 Joyride ClojureScript 片段，该片段使用 Joyride 的内存（memory）或状态管理功能来存储数据。
- 例如，它可能会执行 `(swap! joyride.core/!memory assoc :my-key "my-value")`。
- 在后续的命令中，你可以引用这个被记住的值。

## Key points (英文+中文对照)

- Interactive Programming (交互式编程)
- State Management (状态管理)
- In-Memory Storage (内存存储)
- Joyride Scripting (Joyride 脚本)

## 使用场景

### 1. 存储 API 密钥或配置 (Storing API Keys or Configuration)

- **用户故事**: 作为一名开发人员，我在一个 Joyride 会话中需要多次使用一个 API 密钥，但我不想每次都复制粘贴它。
- **例 1**: `/remember-interactive-programming 将我的 API 密钥 'supersecret' 存储在 `:api-key` 下。` -> AI 执行代码将密钥存入内存。
- **后续**: 在另一个 Joyride 脚本中，你可以通过 `(:api-key @joyride.core/!memory)` 来获取它。

### 2. 缓存 API 调用的结果 (Caching the Result of an API Call)

- **用户故事**: 作为一名数据分析师，我调用了一个耗时的 API 来获取数据，我希望在当前会话中缓存这个结果，以便后续的分析可以快速进行。
- **例 1**: `/remember-interactive-programming [selection=api_result.json] 将这个选中的 JSON 数据记住为 `:user-data`。`

### 3. 在多步骤工作流中传递状态 (Passing State in a Multi-Step Workflow)

- **用户故事**: 作为一名自动化工程师，我正在构建一个多步骤的 Joyride 脚本，用于设置一个新项目。第一步是获取用户输入项目名称，后续步骤需要使用这个名称。
- **例 1 (Step 1)**: `/remember-interactive-programming (let [project-name (vscode/window.showInputBox "Enter project name")] (remember :project-name project-name))`
- **例 2 (Step 2)**: `(let [project-name (recall :project-name)] (create-folder project-name))` (这里 `recall` 是一个假设的辅助函数)

### 4. 动态定义和重用函数 (Dynamically Defining and Reusing Functions)

- **用户故事**: 作为一名 Clojure 爱好者，我喜欢在 REPL 中动态地定义和测试小函数。
- **例 1**: `/remember-interactive-programming 将这个函数 `(fn [x] (* x x))` 记住为 `:square-fn`。`
- **后续**: `((recall :square-fn) 5)` -> 应该返回 25。

## 原始文件

- [remember-interactive-programming.prompt.md](../../prompts/remember-interactive-programming.prompt.md)
