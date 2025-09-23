---
mode: agent
description: '使用 Playwright MCP 基于场景生成测试'
tools: ['changes', 'codebase', 'editFiles', 'fetch', 'findTestFiles', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'playwright']
model: 'Claude Sonnet 4'
---

# 使用 Playwright MCP 生成测试

你的目标是在完成所有规定步骤后，基于提供的场景生成一个 Playwright 测试。

## 具体指令

- 你会得到一个场景，需要据此生成 Playwright 测试。如果用户未提供场景，请先要求其提供。
- 不要过早生成测试代码，也不要仅基于场景生成代码，必须先完成所有规定步骤。
- 使用 Playwright MCP 提供的工具逐步执行步骤。
- 仅在所有步骤都完成后，输出一个使用 `@playwright/test` 的 TypeScript 测试，并基于消息历史生成。
- 将生成的测试文件保存在 tests 目录下。
- 执行该测试文件并反复迭代直到测试通过。
