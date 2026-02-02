---
agent: agent
description: 'Generate a Playwright test based on a scenario using Playwright MCP'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'web/fetch', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'search/searchResults', 'runCommands/terminalLastCommand', 'runCommands/terminalSelection', 'testFailure', 'playwright/*']
model: 'Claude Sonnet 4.5'
---

# 使用 Playwright MCP 进行测试生成

您的目标是在完成所有规定的步骤后，根据提供的场景生成剧作家测试。

## 具体说明

- 给你一个场景，你需要为其生成一个剧作家测试。如果用户没有提供场景，您将要求他们提供一个。
- 在未完成所有规定步骤的情况下，请勿过早或仅根据场景生成测试代码。
- 请使用剧作家 MCP 提供的工具一一运行步骤。
- 仅在完成所有步骤后，才发出基于消息历史记录使用 `@playwright/test` 的 Playwright TypeScript 测试
- 将生成的测试文件保存在tests目录中
- 执行测试文件并迭代直至测试通过
