---
post_title: "javascript-typescript-jest.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "javascript-typescript-jest-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "javascript", "typescript", "testing", "jest"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the JavaScript/TypeScript Jest prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个专门用于为 JavaScript 和 TypeScript 代码生成单元测试和集成测试的提示词，主要使用 Jest 测试框架。

## When

- 在为函数、组件或模块编写测试时。
- 当需要模拟依赖、测试异步代码或验证 UI 组件的渲染时。
- 在前端或 Node.js 项目中实施测试策略时。

## Why

- 自动生成符合 Jest API 和最佳实践的测试代码，提高开发速度。
- 帮助开发者覆盖各种测试场景，包括边缘情况和错误处理。
- 促进项目代码的质量和可维护性。

## How

- 使用 `/javascript-typescript-jest` 命令并提供你想要测试的代码文件。
- AI 将分析代码，并为导出的函数、类或 React 组件生成 `describe` 和 `it`/`test` 测试块。
- 生成的测试将利用 Jest 的模拟（mocking）、断言（assertions）和快照测试（snapshot testing）等功能。

## Key points (英文+中文对照)

- Unit Testing (单元测试)
- Mocking Dependencies (模拟依赖)
- Asynchronous Testing (异步测试)
- Snapshot Testing (快照测试)

## 使用场景

### 1. 测试纯函数 (Testing Pure Functions)

- **用户故事**: 作为一名前端开发人员，我编写了一个用于格式化日期的工具函数，现在需要为它编写单元测试。
- **例 1**: `/javascript-typescript-jest [selection=formatDate.js] 为这个 `formatDate` 函数生成 Jest 测试，覆盖有效的日期、无效的日期和不同的格式选项。`
- **例 2**: `/javascript-typescript-jest [selection=calculator.ts] 为这个计算器模块中的所有导出函数编写单元测试。`

### 2. 测试 React 组件 (Testing React Components)

- **用户故事**: 作为一名 React 开发人员，我创建了一个新的 `Button` 组件，需要验证它的渲染和交互行为。
- **例 1**: `/javascript-typescript-jest [selection=Button.tsx] 使用 React Testing Library 和 Jest 为这个 `Button` 组件生成测试。测试应包括：组件是否正确渲染，以及点击时 `onClick` 回调是否被调用。`
- **例 2**: `/javascript-typescript-jest [selection=UserProfile.tsx] 为这个组件创建一个快照测试，以确保其 UI 不会意外改变。`

### 3. 测试异步代码 (Testing Asynchronous Code)

- **用户故事**: 作为一名 Node.js 开发人员，我有一个从 API 获取数据的异步函数，需要测试它的成功和失败情况。
- **例 1**: `/javascript-typescript-jest [selection=fetchUser.ts] 为这个 `fetchUser` 函数编写测试。使用 `jest.mock` 来模拟 `axios`，并测试成功获取用户数据和 API 返回错误两种场景。`
- **例 2**: `/javascript-typescript-jest 给我一个使用 `async/await` 和 `resolves/rejects` 来测试 Promise 的 Jest 示例。`

### 4. 模拟模块或函数 (Mocking Modules or Functions)

- **用户故事**: 作为一名工程师，我需要测试一个依赖于第三方库或内部模块的函数，但我不想在测试中实际调用它们。
- **例 1**: `/javascript-typescript-jest [selection=auth.js] `auth.js` 中的 `login` 函数依赖于一个 `apiClient` 模块。请编写 `login` 函数的测试，并完全模拟 `apiClient` 模块。`

## 原始文件

- [javascript-typescript-jest.prompt.md](../../prompts/javascript-typescript-jest.prompt.md)
