---
post_title: "playwright-generate-test.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "playwright-generate-test-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "playwright", "testing", "automation", "test-generation"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Playwright Generate Test prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个通用的 Playwright 测试生成提示词，可以根据用户的自然语言描述来创建端到端（E2E）测试脚本。

## When

- 当需要为特定的用户流程或功能编写自动化测试时。
- 在希望将手动测试用例转换为自动化脚本时。
- 在快速原型设计或验证某个特定功能的行为时。

## Why

- 将自然语言的需求直接转换为可执行的测试代码，极大地降低了编写 E2E测试的门槛。
- 提高了测试脚本的编写效率，使开发和 QA 团队能更快地获得反馈。
- 能够处理复杂的用户交互，如点击、输入、等待元素出现等。

## How

- 使用 `/playwright-generate-test` 命令并用自然语言描述你想要测试的用户场景。
- AI 将把你的描述分解为一系列 Playwright 动作和断言。
- 生成一个完整的 Playwright 测试文件，你可以直接运行它来验证你的应用。

## Key points (英文+中文对照)

- Natural Language to Code (自然语言转代码)
- Test Case Automation (测试用例自动化)
- User Journey Testing (用户旅程测试)
- Behavior-Driven Development (BDD, 行为驱动开发)

## 使用场景

### 1. 测试一个完整的用户购买流程 (Testing a Full User Purchase Flow)

- **用户故事**: 作为一名电商网站的 QA 工程师，我需要验证用户从浏览商品到成功下单的整个流程。
- **例 1**: `/playwright-generate-test 生成一个测试，模拟用户访问我们的网站，搜索“笔记本电脑”，将第一个结果添加到购物车，然后进入结算页面，填写送货信息并确认下单。`
- **例 2**: `/playwright-generate-test 创建一个测试，验证用户登录后，可以从他们的订单历史记录中查看最近的订单详情。`

### 2. 将手动测试用例转换为自动化脚本 (Converting a Manual Test Case to an Automated Script)

- **用户故事**: 作为一名测试人员，我有一个手动的测试用例文档，我希望将其自动化。
- **例 1**: `/playwright-generate-test [selection=manual_test_case.txt] 根据这份手动测试用例，生成一个 Playwright 自动化脚本。`

### 3. 验证 UI 元素的行为 (Verifying UI Element Behavior)

- **用户故事**: 作为一名前端开发人员，我需要确保我新开发的交互式图表在用户悬停时能正确显示工具提示（tooltip）。
- **例 1**: `/playwright-generate-test 创建一个测试，导航到图表页面，将鼠标悬停在第一个数据点上，并断言出现的工具提示中包含正确的文本。`
- **例 2**: `/playwright-generate-test 生成一个测试，验证当用户在输入框中输入少于3个字符时，会显示一个错误消息。`

### 4. BDD 风格的测试 (BDD-Style Testing)

- **用户故事**: 作为一名遵循 BDD 实践的开发人员，我希望用 Gherkin 风格的语言来描述我的测试。
- **例 1**: `/playwright-generate-test Given 我在登录页面，When 我输入有效的用户名和密码并点击登录，Then 我应该被重定向到仪表盘页面。`

## 原始文件

- [playwright-generate-test.prompt.md](../../prompts/playwright-generate-test.prompt.md)
