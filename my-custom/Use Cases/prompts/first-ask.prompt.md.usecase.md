---
post_title: "first-ask.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "first-ask-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "prompt-engineering", "clarification"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the First Ask prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个初始提问提示词，用于在用户提供模糊或不完整的请求时，主动进行澄清和收集更多信息。

## When

- 当用户第一次提出请求，但请求内容不够具体时。
- 在开始执行任何复杂任务之前，需要确保对目标有清晰的理解。
- 当 AI 需要引导用户提供更多上下文时。

## Why

- 避免因误解用户意图而产生错误的输出。
- 提高首次交互的成功率，减少来回沟通的次数。
- 建立一个更具协作性和引导性的对话模式。

## How

- 当用户的初始请求缺乏细节时，内部调用 `/first-ask`。
- AI 会分析用户的请求，并生成一系列澄清性问题，以探寻用户的真实目标、约束和期望的输出格式。
- 用户回答这些问题后，AI 将使用这些新信息来更好地完成原始请求。

## Key points (英文+中文对照)

- Clarification Questions (澄清性问题)
- Requirement Gathering (需求收集)
- Goal Alignment (目标对齐)
- Interactive Dialogue (交互式对话)

## 使用场景

### 1. 模糊的编码请求 (Vague Coding Request)

- **用户故事**: 用户说：“帮我写个脚本。”
- **AI (使用 /first-ask)**: “当然，我很乐意。为了更好地帮助你，你能告诉我这个脚本需要做什么吗？它将用于什么语言（比如 Python, Bash）？它需要处理任何输入文件或数据吗？你期望的输出是什么？”
- **例 1**: 用户输入 `/first-ask 我需要一个脚本。` -> AI 提出澄清问题。

### 2. 不完整的文档请求 (Incomplete Documentation Request)

- **用户故事**: 用户说：“为我的项目写文档。”
- **AI (使用 /first-ask)**: “好的。为了生成最好的文档，你能提供一些关于你项目的信息吗？比如，项目是做什么的？它的主要功能有哪些？目标读者是谁（是其他开发者还是最终用户）？”
- **例 2**: 用户输入 `/first-ask 写文档。` -> AI 引导用户提供项目细节。

### 3. 宽泛的设计问题 (Broad Design Question)

- **用户故事**: 用户说：“给我设计一个数据库。”
- **AI (使用 /first-ask)**: “这是一个很好的起点。为了设计一个适合你需求的数据库，我们需要考虑几个方面。这个数据库将用于什么类型的应用（例如，电子商务、社交媒体）？主要的数据实体有哪些（例如，用户、产品、订单）？你预期的访问模式是怎样的（读多写少，还是写多读少）？”
- **例 3**: 用户输入 `/first-ask 设计数据库。` -> AI 开始需求分析过程。

### 4. 寻求建议 (Seeking Advice)

- **用户故事**: 用户说：“我应该用什么技术？”
- **AI (使用 /first-ask)**: “选择正确的技术很重要。为了给你最好的建议，你能告诉我你正在构建什么类型的项目吗？你和你的团队对哪些技术已经有经验了？项目有什么特别的需求，比如性能、可伸缩性或预算限制吗？”
- **例 4**: 用户输入 `/first-ask 推荐技术栈。` -> AI 了解项目背景。

## 原始文件

- [first-ask.prompt.md](../../prompts/first-ask.prompt.md)
