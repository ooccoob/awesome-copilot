---
post_title: "create-llms.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-llms-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "llm", "ai", "development"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Create LLMs prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于创建和配置大型语言模型（LLM）相关组件的提示词。

## When

- 在开发需要与 LLM 交互的应用程序时。
- 当需要定义 LLM 的行为、集成外部工具或设置响应格式时。
- 在构建多代理系统（multi-agent systems）时。

## Why

- 简化创建和管理 LLM 配置的复杂性。
- 提供一个结构化的方法来定义 LLM 的功能和约束。
- 促进可重用和模块化的 LLM 组件的开发。

## How

- 使用 `/create-llms` 命令并描述你需要的 LLM 的功能。
- AI 将生成一个配置文件或代码片段，用于定义 LLM 的代理、工具和模型参数。
- 你可以将生成的配置集成到你的应用程序中。

## Key points (英文+中文对照)

- LLM Configuration (LLM 配置)
- Agent Definition (代理定义)
- Tool Integration (工具集成)
- Multi-Agent Systems (多代理系统)

## 使用场景

### 1. 创建一个简单的问答机器人 (Creating a Simple Q&A Bot)

- **用户故事**: 作为一名开发人员，我需要创建一个能回答关于我们产品基本问题的聊天机器人。
- **例 1**: `/create-llms 创建一个问答 LLM，使用我们的产品文档作为知识库。`
- **例 2**: `/create-llms 我需要一个 LLM，它可以从提供的文本中提取关键信息并回答问题。`

### 2. 集成外部 API 的代理 (Agent with External API Integration)

- **用户故事**: 作为一名 AI 工程师，我正在构建一个可以查询天气预报的代理。
- **例 1**: `/create-llms 创建一个 LLM 代理，它可以调用天气 API 并根据用户的位置返回当前天气。`
- **例 2**: `/create-llms 我需要一个集成了日历 API 的 LLM，以便用户可以查询和安排会议。`

### 3. 构建一个多代理协作系统 (Building a Multi-Agent Collaborative System)

- **用户故事**: 作为一名研究员，我正在探索如何让多个 AI 代理协同解决一个复杂问题，例如软件开发。
- **例 1**: `/create-llms 创建一个多代理系统，其中包含一个“产品经理”代理、一个“开发人员”代理和一个“测试人员”代理，用于模拟软件开发流程。`
- **例 2**: `/create-llms 设计一个包含“规划者”和“执行者”两个代理的系统，用于完成多步骤任务。`

### 4. 定义具有特定角色的 LLM (Defining an LLM with a Specific Persona)

- **用户故事**: 作为一名内容创作者，我希望创建一个具有特定写作风格（例如，莎士比亚风格）的 LLM 来帮助我写作。
- **例 1**: `/create-llms 创建一个角色为“海盗”的 LLM，它的回答都将使用海盗的口吻。`

## 原始文件

- [create-llms.prompt.md](../../prompts/create-llms.prompt.md)
