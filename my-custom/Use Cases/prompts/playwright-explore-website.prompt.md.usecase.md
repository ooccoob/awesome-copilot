---
post_title: "playwright-explore-website.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "playwright-explore-website-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "playwright", "testing", "automation", "web-scraping"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Playwright Explore Website prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于生成 Playwright 脚本的提示词，该脚本能够探索性地浏览网站、发现链接并与之交互，以了解网站的结构和功能。

## When

- 在开始为一个不熟悉的网站编写测试或爬虫之前。
- 当需要快速了解一个网站有哪些页面和关键功能时。
- 在进行探索性测试（Exploratory Testing）的自动化时。

## Why

- 自动发现网站的页面和链接，为后续的深入测试或数据抓取提供基础。
- 帮助理解单页应用（SPA）的路由和动态加载内容。
- 生成一个基础的站点地图或功能清单。

## How

- 使用 `/playwright-explore-website` 命令并提供起始 URL。
- AI 将生成一个 Playwright 脚本，该脚本会：
    1. 导航到起始 URL。
    2. 抓取页面上所有的 `<a>` 标签链接。
    3. 访问这些链接（通常会限制在同一个域名下）。
    4. 记录访问过的页面和发现的链接，可能会进行截图。
    5. （可选）对页面上的交互元素（如按钮、表单）进行基本交互。

## Key points (英文+中文对照)

- Web Crawling (网页爬取)
- Link Discovery (链接发现)
- Exploratory Testing (探索性测试)
- Site Mapping (站点地图绘制)

## 使用场景

### 1. 为测试自动化做准备 (Preparing for Test Automation)

- **用户故事**: 作为一名 QA 工程师，我即将为一个新的电子商务网站编写 E2E 测试。在开始之前，我需要了解网站的所有主要页面，如主页、产品列表页、产品详情页和购物车。
- **例 1**: `/playwright-explore-website URL: https://my-ecommerce-site.com。请生成一个脚本，从主页开始，发现并访问所有内部链接，并列出所有页面的标题。`
- **例 2**: `/playwright-explore-website URL: https://my-ecommerce-site.com。探索网站，并为每个页面进行截图。`

### 2. 了解单页应用 (SPA) 的结构 (Understanding the Structure of a Single-Page Application)

- **用户故事**: 作为一名前端开发人员，我正在接手一个复杂的 React 单页应用。我想快速了解它的所有路由和视图。
- **例 1**: `/playwright-explore-website URL: https://my-spa.com。探索这个 SPA，点击所有导航链接，并记录下 URL 的变化和每个视图的标题。`

### 3. 基础的网站健康检查 (Basic Website Health Check)

- **用户故事**: 作为一名网站管理员，我想快速检查网站上是否存在坏掉的链接。
- **例 1**: `/playwright-explore-website URL: https://my-blog.com。爬取整个网站，并报告所有返回 404 或其他错误状态码的链接。`

### 4. 为数据抓取做准备 (Preparing for Web Scraping)

- **用户故事**: 作为一名数据分析师，我需要从一个新闻网站上抓取所有文章的链接。
- **例 1**: `/playwright-explore-website URL: https://news-site.com。生成一个脚本，从主页开始，遍历所有分页，并收集所有指向文章页面的链接。`

## 原始文件

- [playwright-explore-website.prompt.md](../../prompts/playwright-explore-website.prompt.md)
