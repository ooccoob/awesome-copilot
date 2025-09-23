---
mode: agent
description: '使用 Playwright MCP 进行网站探索以支持测试'
tools: ['changes', 'codebase', 'editFiles', 'fetch', 'findTestFiles', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'playwright']
model: 'Claude Sonnet 4'
---

# 网站探索用于测试

你的目标是探索网站并识别关键功能。

## 具体指令

1. 使用 Playwright MCP Server 访问提供的 URL。若未提供 URL，请要求用户提供。
2. 识别并交互 3–5 个核心特性或用户流程。
3. 记录用户交互、相关 UI 元素（及其定位器）与期望结果。
4. 任务结束后关闭浏览器上下文。
5. 提供一份简明的发现总结。
6. 基于探索结果提出并生成测试用例。
