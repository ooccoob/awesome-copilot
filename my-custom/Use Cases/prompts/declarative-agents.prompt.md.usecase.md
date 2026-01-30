---
post_title: "declarative-agents.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "declarative-agents-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "ai", "agents", "declarative-programming"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Declarative Agents prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于以声明式方式定义和编排 AI 代理（Agent）行为的提示词。

## When

- 在构建需要多个 AI 代理协作完成任务的系统时。
- 当希望通过定义“什么”（What）而不是“如何”（How）来指定代理的目标和能力时。
- 在设计和模拟复杂的代理交互和工作流时。

## Why

- 简化多代理系统的设计和实现，使开发者能专注于业务逻辑而非底层的控制流。
- 提高代理行为的可预测性和可维护性。
- 促进代理组件的模块化和重用。

## How

- 使用 `/declarative-agents` 命令并以声明式语言（如 YAML 或 JSON）描述代理、它们的角色、工具和交互规则。
- AI 将解析这个声明，并生成实现该代理系统所需的代码骨架或配置文件。
- 你可以进一步完善生成的代码，将其集成到你的应用程序中。

## Key points (英文+中文对照)

- Declarative Programming (声明式编程)
- AI Agents (AI 代理)
- Multi-Agent Systems (多代理系统)
- Orchestration (编排)

## 使用场景

### 1. 定义一个客户服务代理团队 (Defining a Customer Service Agent Team)

- **用户故事**: 作为一名 AI 应用开发者，我需要创建一个自动化的客户服务系统，其中包含一个用于初步分类问题的一线代理，以及多个处理特定问题的专家代理。
- **例 1**: `/declarative-agents [selection=customer_service_agents.yml] 根据这个 YAML 文件，生成一个多代理客户服务系统的实现代码。`
- **例 2**: `/declarative-agents 我需要一个声明式的定义，描述一个“路由代理”，它可以根据用户的问题将对话转接给“技术支持代理”或“账单代理”。`

### 2. 编排一个软件开发工作流 (Orchestrating a Software Development Workflow)

- **用户故事**: 作为一名研究员，我正在模拟一个由 AI 代理组成的虚拟软件开发团队。
- **例 1**: `/declarative-agents 定义一个包含“产品经理代理”、“程序员代理”和“QA 代理”的系统。产品经理负责创建需求，程序员负责编写代码，QA 负责测试。`
- **例 2**: `/declarative-agents [selection=dev_team.json] 将这个 JSON 定义的代理团队转换为可执行的 Python 代码。`

### 3. 创建一个内容创作流水线 (Creating a Content Creation Pipeline)

- **用户故事**: 作为一名内容策略师，我希望自动化我们的博客文章创作流程。
- **例 1**: `/declarative-agents 设计一个内容创作流水线，其中“研究员代理”负责收集信息，“作家代理”负责撰写初稿，“编辑代理”负责校对和润色。`

### 4. 模拟经济或社会系统 (Simulating Economic or Social Systems)

- **用户故事**: 作为一名社会科学家，我希望使用代理来模拟市场中的买家和卖家的行为。
- **例 1**: `/declarative-agents 定义一个包含多个“消费者代理”和“生产者代理”的市场模型。每个代理都有自己的目标（如最大化利润或效用）和行为规则。`

## 原始文件

- [declarative-agents.prompt.md](../../prompts/declarative-agents.prompt.md)
