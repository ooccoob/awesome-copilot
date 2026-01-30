---
mode: agent
description: '使用Playwright MCP进行网站探索测试'
tools: ['changes', 'codebase', 'edit/editFiles', 'fetch', 'findTestFiles', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'playwright']
model: 'Claude Sonnet 4'
---

# 网站测试探索

您的目标是探索网站并识别关键功能。

## 具体指令

1. 使用Playwright MCP服务器导航到提供的URL。如果没有提供URL，请用户提供一个。
2. 识别并与3-5个核心功能或用户流程交互。
3. 记录用户交互、相关UI元素（及其定位器）和预期结果。
4. 完成后关闭浏览器上下文。
5. 提供您发现的简明摘要。
6. 基于探索提议并生成测试用例。