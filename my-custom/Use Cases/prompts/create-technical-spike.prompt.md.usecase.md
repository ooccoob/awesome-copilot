---
post_title: "create-technical-spike.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-technical-spike-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "agile", "scrum", "spike", "research"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Create Technical Spike prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于定义和构建技术预研（Technical Spike）任务的提示词，帮助团队探索未知技术、评估解决方案或降低风险。

## When

- 当团队面临技术不确定性，无法准确估算某个用户故事的工作量时。
- 在采用新技术、新框架或新库之前。
- 当需要评估不同技术方案的可行性时。

## Why

- 为技术预研提供一个结构化的框架，确保研究有明确的目标、范围和交付物。
- 帮助团队将大的不确定性分解为小的、有时间限制的研究任务。
- 使研究结果可见、可衡量，并为后续的开发决策提供依据。

## How

- 使用 `/create-technical-spike` 命令并描述需要研究的技术问题或不确定性。
- AI 将引导你定义 Spike 的目标、要回答的关键问题、时间盒（timebox）、以及预期的交付物（如原型代码、文档、决策矩阵等）。
- 生成一个结构化的 Spike 用户故事或任务，可以添加到你的项目积压（backlog）中。

## Key points (英文+中文对照)

- Technical Spike (技术预研)
- Risk Reduction (风险降低)
- Feasibility Study (可行性研究)
- Timeboxing (时间盒)

## 使用场景

### 1. 评估新技术或库 (Evaluating a New Technology or Library)

- **用户故事**: 作为一名开发团队成员，我们需要为我们的下一个项目选择一个前端框架。我们正在考虑 React 和 Vue，需要进行一次 Spike 来评估它们。
- **例 1**: `/create-technical-spike 创建一个 Spike，目标是比较 React 和 Vue 在我们的项目场景下的优缺点。交付物应包括一个简单的原型和一个决策矩阵。`
- **例 2**: `/create-technical-spike 我们需要研究一个新的图形数据库 Neo4j，看它是否适合我们的社交网络功能。`

### 2. 探索解决方案以降低风险 (Exploring Solutions to Reduce Risk)

- **用户故事**: 作为一名架构师，我不确定我们当前的架构能否支持预期的双十一流量。我需要一个 Spike 来进行性能测试和压力测试。
- **例 1**: `/create-technical-spike 创建一个 Spike，以确定我们现有的支付网关集成方案能否处理每秒 1000 次的并发请求。`
- **例 2**: `/create-technical-spike 我们需要研究如何将第三方身份验证服务（如 Auth0）集成到我们的应用中。`

### 3. 理解复杂系统的行为 (Understanding a Complex System's Behavior)

- **用户故事**: 作为一名后端工程师，我需要与一个我们不熟悉的、文档不全的旧版 API 集成。我需要一个 Spike 来探索它的行为和限制。
- **例 1**: `/create-technical-spike 创建一个 Spike，目标是找出旧版订单 API 的所有可用端点和数据格式。`

### 4. 为复杂的用户故事提供估算依据 (Enabling Estimation for a Complex User Story)

- **用户故事**: 作为一名 Scrum Master，团队无法为一个关于“实现实时协作编辑”的用户故事进行估算，因为它包含太多的未知数。
- **例 1**: `/create-technical-spike 创建一个 Spike，研究实现实时协作编辑所需的技术（如 WebSockets, CRDTs），并为原始用户故事的实现提供一个粗略的估算。`

## 原始文件

- [create-technical-spike.prompt.md](../../prompts/create-technical-spike.prompt.md)
