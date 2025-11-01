## What
- 目标：用 TypeScript 生成完整 MCP 服务器（工具/资源/可选 prompts/传输/配置/测试指引）。
- 依赖：@modelcontextprotocol/sdk、zod@3、Express(HTTP) 或 stdio 传输、tsx/ts-node（开发）。

## When
- 需要快速搭建可观测、可维护、类型安全的 MCP 服务端时。
- 需要 HTTP/stdio 两种运行模式（二选一）。

## Why
- TS 类型系统 + zod 保障输入输出契约；便于 Inspector/客户端调试。
- 规范化工程骨架与错误处理，降低集成风险。

## How
- 项目：npm init、package.json type=module、tsconfig（ESM）。
- 传输：StreamableHTTPServerTransport + Express 中间件 或 StdioServerTransport。
- 工具：registerTool + zod schema；返回 content 与 structuredContent；try/catch 错误处理。
- 资源/提示：registerResource/registerPrompt（可选），支持模板/参数补全。
- 质量：async/await、一致清理、环境变量配置、模块化分层。

## Key Points
- 提供示例工具类型：数据处理、外部 API、文件系统、数据库、文本分析等。
- HTTP 需 CORS/会话策略、DNS 重绑定防护；stdio 需生命周期钩子。
- 提供运行、Inspector 连接、问题排查文档与示例调用。

## Compact Map
- Setup: deps + tsconfig + scripts
- Server: McpServer + transport
- Tools: zod schema + error handling
- Optional: resources/prompts
- QA: config/env/logging/cleanup

## Example Questions (10+)
- 如何在 HTTP 与 stdio 两种传输间切换与抽象？
- registerTool 的输入/输出 zod 应如何组织与复用？
- 如何实现异步外部 API 工具并增加超时与重试？
- structuredContent 的推荐数据结构是什么？
- Express 版本的中间件顺序与错误处理最佳实践？
- 如何优雅关闭并确保未完成请求处理完毕？
- 单元测试如何模拟 transport 事件与工具调用？
- 如何为资源注册模板 URI 与参数校验？
- 生产环境 CORS/安全与本地调试的差异化配置？
- Inspector 无法连接的常见原因与排查步骤？
- 如何实现动态工具开关与通知去抖？

---
Source: d:\mycode\awesome-copilot\prompts\typescript-mcp-server-generator.prompt.md
Generated: 2025-10-17T00:00:00Z
