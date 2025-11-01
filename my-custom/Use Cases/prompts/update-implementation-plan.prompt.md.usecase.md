---
post_title: "update-implementation-plan.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "update-implementation-plan-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "project-management", "implementation-plan", "agile"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Update Implementation Plan prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于根据新的需求、反馈或技术发现来更新现有实施计划的提示词。

## When

- 在项目开发过程中，当功能规范发生变更时。
- 在技术预研（Spike）或原型设计之后，需要将新的发现整合到计划中时。
- 在代码审查或测试中发现了未预见的问题，需要调整计划来解决它们时。

## Why

- 保持实施计划与项目的当前状态和目标同步，使其成为一个“活的文档”。
- 确保所有团队成员都了解最新的计划变更和任务调整。
- 自动化更新过程，减少手动编辑文档的繁琐工作。

## How

- 使用 `/update-implementation-plan` 命令，并提供现有的实施计划以及需要进行的变更描述。
- AI 将分析变更请求，并智能地修改实施计划的相应部分。例如，它可以添加新任务、修改现有任务的描述或估算、或重新排序任务。
- 生成一个更新后的实施计划文档，你可以审查这些变更。

## Key points (英文+中文对照)

- Living Document (活文档)
- Change Management (变更管理)
- Plan Adaptation (计划适应)
- Continuous Planning (持续规划)

## 使用场景

### 1. 根据变更的功能规范更新计划 (Updating Plan Based on Changed Specifications)

- **用户故事**: 作为一名技术负责人，产品经理刚刚更新了功能规范，在用户个人资料页面增加了一个“上传头像”的功能。我需要将这个新任务添加到我们的实施计划中。
- **例 1**: `/update-implementation-plan [selection=implementation_plan.md] 这是我们当前的实施计划。请根据最新的规范，在“前端”部分添加一个关于“实现头像上传 UI”的任务，并在“后端”部分添加一个“处理头像上传和存储”的任务。`

### 2. 将技术预研的结果整合进计划 (Incorporating Findings from a Technical Spike)

- **用户故事**: 作为一名开发人员，我刚刚完成了一个关于支付网关的技术预研。我们决定使用 Stripe 而不是 PayPal。我需要更新实施计划以反映这一决策。
- **例 1**: `/update-implementation-plan [selection=implementation_plan.md] 更新实施计划，将所有与“PayPal 集成”相关的任务替换为“Stripe 集成”任务，并根据 Stripe 的 API 更新任务描述。`

### 3. 响应测试中发现的问题 (Responding to Issues Found in Testing)

- **用户故事**: 作为一名 QA 工程师，我们发现了一个严重的性能问题，需要后端团队优化数据库查询。我需要将这个紧急任务添加到当前的实施计划中。
- **例 1**: `/update-implementation-plan [selection=implementation_plan.md] 在实施计划的开头添加一个高优先级的任务：“优化`get_user_posts`查询以解决 N+1 问题”。`

### 4. 重新排定任务优先级 (Re-prioritizing Tasks)

- **用户故事**: 作为一名项目经理，由于市场变化，我们需要优先交付“分享到社交媒体”功能。我需要调整实施计划的优先级。
- **例 1**: `/update-implementation-plan [selection=implementation_plan.md] 将与“分享到社交媒体”功能相关的所有任务移动到计划的最前面，并将其余任务向后顺延。`

## 原始文件

- [update-implementation-plan.prompt.md](../../prompts/update-implementation-plan.prompt.md)
