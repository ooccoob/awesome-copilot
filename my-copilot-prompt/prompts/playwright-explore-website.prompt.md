---
agent: agent
description: 'Website exploration for testing using Playwright MCP'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'web/fetch', 'findTestFiles', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'search/searchResults', 'runCommands/terminalLastCommand', 'runCommands/terminalSelection', 'testFailure', 'playwright']
model: 'Claude Sonnet 4'
---

# 网站探索测试

您的目标是探索网站并确定关键功能。

## 具体说明

1. 使用 Playwright MCP 服务器导航到提供的 URL。如果未提供 URL，请要求用户提供 URL。
2. 识别 3-5 个核心功能或用户流程并与之交互。
3. 记录用户交互、相关 UI 元素（及其定位器）和预期结果。
4. 完成后关闭浏览器上下文。
5. 简要总结您的发现。
6. 根据探索提出并生成测试用例。
