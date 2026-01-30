---
mode: agent
description: '使用Playwright MCP基于场景生成Playwright测试'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'fetch', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'search/searchResults', 'runCommands/terminalLastCommand', 'runCommands/terminalSelection', 'testFailure', 'playwright/*']
model: 'Claude Sonnet 4.5'
---

# 使用Playwright MCP生成测试

您的目标是在完成所有规定步骤后，根据提供的场景生成Playwright测试。

## 具体说明

- 您得到一个场景，需要为其生成一个playwright测试。如果用户没有提供场景，您将要求他们提供一个。
- 不要在完成所有规定步骤之前过早生成测试代码或仅基于场景生成。
- 确实使用Playwright MCP提供的工具逐步运行步骤。
- 只有在所有步骤完成后，根据消息历史发出使用`@playwright/test`的Playwright TypeScript测试。
- 将生成的测试文件保存在tests目录中
- 执行测试文件并迭代直到测试通过