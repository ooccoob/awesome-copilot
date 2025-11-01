---
post_title: "playwright-automation-fill-in-form.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "playwright-automation-fill-in-form-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "playwright", "testing", "automation", "forms"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Playwright Automation Fill-in Form prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于生成 Playwright 自动化脚本的提示词，该脚本能够自动填充和提交网页上的表单。

## When

- 在需要为网站的注册、登录、联系我们或任何其他表单编写端到端（E2E）测试时。
- 当需要自动化重复性的数据录入任务时。
- 在测试表单的验证逻辑和提交功能时。

## Why

- 快速生成可靠的 Playwright 脚本，节省手动编写测试代码的时间。
- 自动处理各种表单元素，如文本输入框、下拉菜单、复选框和单选按钮。
- 提高测试覆盖率，确保表单功能的健壮性。

## How

- 使用 `/playwright-automation-fill-in-form` 命令，提供要测试的网页 URL 和要填充的表单数据。
- AI 将分析网页的 HTML 结构，找到表单元素对应的定位器（selectors）。
- 生成一个 Playwright 测试脚本，该脚本会导航到指定页面，使用提供的数据填充表单，并触发表单提交。

## Key points (英文+中文对照)

- Form Automation (表单自动化)
- End-to-End Testing (E2E 测试)
- Element Locators (元素定位器)
- Data-Driven Testing (数据驱动测试)

## 使用场景

### 1. 测试用户注册表单 (Testing a User Registration Form)

- **用户故事**: 作为一名 QA 工程师，我需要验证我们网站的注册功能是否正常工作。
- **例 1**: `/playwright-automation-fill-in-form URL: https://example.com/register, 数据: { "username": "testuser", "password": "password123", "email": "test@example.com" }。请为这个注册表单生成 Playwright 测试脚本。`
- **例 2**: `/playwright-automation-fill-in-form URL: https://example.com/register。生成一个脚本，用随机生成的数据填充表单并提交。`

### 2. 自动化登录过程 (Automating the Login Process)

- **用户故事**: 作为一名开发人员，我需要在我的许多 E2E 测试的开头部分自动登录系统。
- **例 1**: `/playwright-automation-fill-in-form URL: https://example.com/login, 数据: { "username": "admin", "password": "supersecret" }。生成一个可重用的登录函数。`

### 3. 测试复杂的表单，包括下拉菜单和复选框 (Testing Complex Forms with Dropdowns and Checkboxes)

- **用户故事**: 作为一名测试自动化工程师，我需要测试一个包含多种类型输入的复杂设置页面。
- **例 1**: `/playwright-automation-fill-in-form URL: https://example.com/settings。表单数据包括选择国家（下拉菜单），并勾选“同意服务条款”（复选框）。`

### 4. 数据驱动的表单测试 (Data-Driven Form Testing)

- **用户故事**: 作为一名 SDET，我需要用多组不同的数据集（有效的、无效的、边界值）来测试同一个表单，以验证其验证逻辑。
- **例 1**: `/playwright-automation-fill-in-form URL: https://example.com/contact。请生成一个数据驱动的 Playwright 测试，从一个数组中读取多组联系人信息来填充和提交表单。`

## 原始文件

- [playwright-automation-fill-in-form.prompt.md](../../prompts/playwright-automation-fill-in-form.prompt.md)
