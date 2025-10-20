---
post_title: "update-llms.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "update-llms-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "llm", "ai", "agents", "configuration"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Update LLMs prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于修改和更新现有大型语言模型（LLM）代理或其配置的提示词。

## When

- 当需要向现有 AI 代理添加新功能、工具或知识时。
- 在需要调整代理的行为、角色或响应风格时。
- 在对多代理系统进行迭代开发和调试时。

## Why

- 提供一种便捷的方式来动态地修改代理配置，而无需从头开始重新生成。
- 简化了对复杂代理系统进行微调和实验的过程。
- 确保代理的配置与不断变化的需求保持同步。

## How

- 使用 `/update-llms` 命令，并提供现有的 LLM 代理配置文件以及你想要进行的修改描述。
- AI 将解析你的修改请求，并将其应用到现有的配置上。
- 例如，你可以要求它“添加一个新的工具”、“更改模型的温度参数”或“修改系统的初始提示”。
- 生成一个更新后的配置文件，你可以用它来重新加载你的代理。

## Key points (英文+中文对照)

- Agent Configuration (代理配置)
- Dynamic Update (动态更新)
- Iterative Development (迭代开发)
- Fine-tuning (微调)

## 使用场景

### 1. 为代理添加新工具 (Adding a New Tool to an Agent)

- **用户故事**: 作为一名 AI 开发者，我有一个可以查询天气的代理，现在我想让它也能搜索互联网。
- **例 1**: `/update-llms [selection=weather_agent.json] 这是我的天气代理的配置。请为它添加一个名为 `search_web` 的新工具。`
- **例 2**: `/update-llms [selection=my_agent.yml] 为这个代理添加一个可以执行 Python 代码的工具。`

### 2. 调整代理的行为参数 (Adjusting Agent's Behavior Parameters)

- **用户故事**: 作为一名提示词工程师，我觉得我的代理生成的响应不够有创意。我想通过调整 `temperature` 参数来让它更大胆一些。
- **例 1**: `/update-llms [selection=creative_writer_agent.json] 将这个代理的 OpenAI 模型参数中的 `temperature` 值从 0.5 修改为 0.9。`

### 3. 修改代理的系统提示或角色 (Modifying Agent's System Prompt or Persona)

- **用户故事**: 作为一名内容创作者，我有一个“专业作家”代理，但我现在希望它的写作风格更偏向于非正式的博客风格。
- **例 1**: `/update-llms [selection=writer_agent.json] 修改这个代理的系统提示，告诉它“你的写作风格应该像一个友好、知识渊博的博主，多使用第一人称和非正式的语言”。`

### 4. 在多代理系统中修改交互规则 (Modifying Interaction Rules in a Multi-Agent System)

- **用户故事**: 作为一名研究员，我有一个包含“经理”和“员工”代理的系统。目前，“员工”只能响应“经理”。我想修改规则，允许“员工”之间也可以互相通信。
- **例 1**: `/update-llms [selection=multi_agent_config.yml] 更新这个多代理系统的配置，允许所有 `employee` 类型的代理之间进行通信。`

## 原始文件

- [update-llms.prompt.md](../../prompts/update-llms.prompt.md)
