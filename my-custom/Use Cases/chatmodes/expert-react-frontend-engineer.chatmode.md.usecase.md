---
post_title: "expert-react-frontend-engineer.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "expert-react-frontend-engineer-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","react","frontend"]
ai_note: "Generated with AI assistance."
summary: "React 前端专家：组件设计、性能优化、状态管理与测试的可执行用例集合。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供 React（含 TypeScript）项目中组件设计、性能调优、无障碍、状态管理与测试策略的可执行示例。

## When

- 新建页面、优化渲染性能、引入全局状态或增加测试覆盖时使用。

## Why

- 保持组件可维护性、避免不必要的重渲染并保证良好的用户体验与可访问性。

## How

- 给出组件拆分原则、memo/Hooks 优化示例、性能测量方法和 Jest/RTL 的测试模版。

## Key points (英文+中文对照)

- Component design（组件设计）
- Performance optimization（性能优化）
- Accessibility（无障碍）
- State management（状态管理）
- Testing & CI（测试与 CI）

## 使用场景

### 1. 组件拆分与复用

- 用户故事：作为前端工程师，我需要设计高复用的组件库。
- 例 1："提供按钮/输入/表单的通用组件示例和 API 约定。"
- 例 2："示例如何抽离渲染逻辑与展示逻辑。"
- 例 3："组件文档模板（props/示例/edge cases）。"
- 例 4："设计 variant 与主题适配的建议。"
- 例 5："如何保证组件的可测试性。"

### 2. 渲染性能优化

- 用户故事：作为性能工程师，我要减少不必要的重渲染并降低首屏时间。
- 例 1："使用 React.memo 与 useCallback 的场景与误区。"
- 例 2："分片渲染/虚拟化（react-window）示例。"
- 例 3："懒加载与代码分割建议（路由级与组件级）。"
- 例 4："首屏渲染性能测量与 Lighthouse 指标解读。"
- 例 5："减少 bundle size 的策略（tree-shaking、按需加载）。"

### 3. 无障碍（A11y）

- 用户故事：作为产品经理，我需要页面满足基本无障碍要求。
- 例 1："表单/控件的键盘导航与 ARIA 示例。"
- 例 2："色彩对比检查提示与修正建议。"
- 例 3："屏幕阅读器测试建议与示例。"
- 例 4："可访问性回归测试策略。"
- 例 5："无障碍审核清单（必做项）。"

### 4. 状态管理选择

- 用户故事：作为工程师，我要在复杂场景选择合适状态管理工具。
- 例 1："何时使用 Context + reducer vs Redux vs Zustand 的决策树。"
- 例 2："示例缓存策略与离线支持要点。"
- 例 3："避免过度 lift state 的重构示例。"
- 例 4："同步与异步状态边界建议。"
- 例 5："跨页面状态持久化与版本迁移指南。"

### 5. 测试与 CI 集成

- 用户故事：作为 QA/DevOps，我要保证回归可控并且 PR 自动验证。
- 例 1："Jest + Testing Library 的组件测试模版。"
- 例 2："端到端（Playwright）测试场景与数据准备策略。"
- 例 3："性能回归在 CI 中的最小化执行样例。"
- 例 4："静态检查（ESLint/TypeScript）配置示例。"
- 例 5："PR 模板与自动化检查建议。"

## 原始文件

- [chatmodes/expert-react-frontend-engineer.chatmode.md](../../../chatmodes/expert-react-frontend-engineer.chatmode.md)
