---
post_title: "create-specification.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-specification-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "specification", "project-management", "requirements"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Create Specification prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于将高层次的功能想法或需求转化为详细、结构化的功能规范文档的提示词。

## When

- 在项目规划阶段，需要将模糊的想法具体化时。
- 在编写产品需求文档 (PRD) 或技术设计文档之前。
- 当需要为开发团队提供清晰、无歧义的功能要求时。

## Why

- 确保所有利益相关者对功能有共同的理解。
- 为设计、开发和测试工作提供一个坚实的基础。
- 减少由于需求不明确而导致的返工和误解。

## How

- 使用 `/create-specification` 命令并描述你想要实现的功能。
- AI 将引导你完成一系列问题，以收集关于用户故事、验收标准、非功能性需求和潜在约束的详细信息。
- 最终，AI 会生成一个完整的规范文档，你可以将其用作进一步讨论和开发的基础。

## Key points (英文+中文对照)

- Requirement Elicitation (需求获取)
- Specification Document (规范文档)
- User Stories (用户故事)
- Acceptance Criteria (验收标准)

## 使用场景

### 1. 将产品想法转化为规范 (Turning a Product Idea into a Specification)

- **用户故事**: 作为一名产品经理，我有一个关于“用户个人资料页面”的新功能的想法，需要将其 fleshed out 为一个完整的规范。
- **例 1**: `/create-specification 我想创建一个用户个人资料页面，用户可以在上面编辑他们的姓名、头像和简介。`
- **例 2**: `/create-specification 帮我为一个新的“购物车”功能创建规范，包括添加商品、删除商品和查看总价的功能。`

### 2. 定义 API 的技术规范 (Defining a Technical Specification for an API)

- **用户故事**: 作为一名后端工程师，我需要为一个新的 RESTful API 设计技术规范。
- **例 1**: `/create-specification 我需要为 `/users/{id}` 端点创建一个规范，它应该支持 GET, PUT, 和 DELETE 方法。`
- **例 2**: `/create-specification 为一个新的身份验证服务创建技术规范，包括 JWT 的生成和验证流程。`

### 3. 编写非功能性需求 (Writing Non-Functional Requirements)

- **用户故事**: 作为一名系统架构师，我需要确保我们的新功能满足性能、安全性和可扩展性要求。
- **例 1**: `/create-specification 为我们的新服务定义非功能性需求，要求其在 99.9% 的时间内可用，并且平均响应时间低于 200ms。`

### 4. 澄清模糊的需求 (Clarifying Ambiguous Requirements)

- **用户故事**: 作为一名业务分析师，我收到了一个来自客户的模糊需求：“我们希望网站更‘现代’”。我需要将其转化为具体、可衡量的规范。
- **例 1**: `/create-specification 客户希望网站更“现代”。请帮我通过提问的方式，将这个需求具体化为关于响应式设计、加载速度和 UI 风格的规范。`

## 原始文件

- [create-specification.prompt.md](../../prompts/create-specification.prompt.md)
