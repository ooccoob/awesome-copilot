---
description: "Azure Functions 的 TypeScript 编码模式"
applyTo: "**/*.ts, **/*.js, **/*.json"
---

## 代码生成指引

- 生成现代 TypeScript 代码，适用于 Node.js
- 异步代码统一使用 `async/await`
- 优先使用 Node.js v20 内置模块，避免不必要的第三方依赖
- 所有异步操作应使用 Node.js 的 async 函数，如 `node:fs/promises`，避免阻塞事件循环
- 添加新依赖前需征询意见，避免随意引入包
- API 基于 Azure Functions，使用 `@azure/functions@4` 包实现
- 每个端点应有独立的函数文件，命名规范为：`src/functions/<resource-name>-<http-verb>.ts`
- 如对 API 做出更改，务必同步更新 OpenAPI schema（如有）及 `README.md`

---

**免责声明**：本文档由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 本地化。如有错误或不当之处，欢迎通过 [issues](../../issues) 反馈。
