## What / When / Why / How

- What: TypeScript MCP 服务器专家（@modelcontextprotocol/sdk）
- When: 需要创建/调试/优化基于 TS 的 MCP 服务器
- Why: 类型安全、可维护、对 LLM 友好
- How: 选传输(HTTP/stdio)→定义工具/资源/提示→zod 校验→错误处理→测试

## Key Points

- ESModule 导入：@modelcontextprotocol/sdk/server/mcp.js
- zod 定义输入/输出；工具需 title、content+structuredContent
- 资源：ResourceTemplate/动态 URI；ResourceLink 优化
- HTTP：CORS、Mcp-Session-Id 暴露、DNS Rebinding 保护
- 采样/引导：createMessage/elicitInput；completable 参数补全
- 测试：npx @modelcontextprotocol/inspector

## Compact Map

- 需求→传输→工具/资源→校验→错误→测试→部署

## Example Questions (10+)

- 该服务的工具与参数 Schema？
- 传输选型与安全配置？
- 如何返回 structuredContent 供二次利用？
- 资源订阅与更新通知？
- 交互式 elicitation 流程？
- HTTP 会话管理与清理？
- 类型推断与运行时校验？
- 调试常见问题与日志？
- Inspector 的测试流程？
- 部署环境变量与配置？

---
Source: d:\mycode\awesome-copilot\chatmodes\typescript-mcp-expert.chatmode.md
Generated: {{timestamp}}
