## What
- 使用 @modelcontextprotocol/sdk 构建 TypeScript MCP 服务器：McpServer/Server、传输、工具/资源/提示、zod 校验、采样与提示补全

## When
- 需要以 stdio 或 HTTP 方式提供 LLM 可调用的工具/资源/提示时

## Why
- 统一协议、结构化输入输出、良好兼容 MCP Inspector 与多客户端

## How
- 依赖
  - @modelcontextprotocol/sdk, zod；按路径导入 server/mcp、server/stdio、server/streamableHttp 等
- 核心对象
  - 推荐 registerTool/registerResource/registerPrompt（带 title/description）；content + structuredContent
- 传输
  - StdioServerTransport 本地集成；StreamableHTTPServerTransport(Express)；每请求新实例避免 ID 冲突
  - 会话：sessionIdGenerator；DNS 反绑定保护；CORS 暴露 Mcp-Session-Id
- 资源
  - ResourceTemplate('scheme://{id}') 动态 URI；listChanged 通知与 enable/disable/update/remove
- 交互增强
  - completable() 提示补全；createMessage 采样；elicitInput 请求额外输入
  - debouncedNotificationMethods 降噪
- 错误/安全
  - try/catch→isError；结构化日志；谨慎暴露文件/网络；传输关闭时清理
- 测试
  - npx @modelcontextprotocol/inspector 验证

## Key Points
- Tool/Resource/Prompt 都应有清晰标题与类型
- 使用 zod 明确定义输入/输出

## Compact Map
- Server: McpServer/Server
- Transport: stdio/http
- Tool: schema+结果
- Resource: 模板+动态
- Prompt: args+messages
- UX: completable/notifications
- 安全: CORS/DNS/清理

## Example Questions
1) 何时选 McpServer vs 低层 Server？
2) 如何设计 zod 输入/输出 schema？
3) 如何在 HTTP 模式下避免请求 ID 冲突？
4) structuredContent 与 content 的取舍？
5) 如何给资源列表发 listChanged 通知？
6) completable 如何提供动态补全？
7) 采样 createMessage 的适用场景？
8) 如何处理 CORS 与 Session ID 暴露？
9) 传输关闭时资源如何清理？
10) Inspector 验证有哪些常见错误？
11) 如何实现动态资源 URI 参数解析？

Source: d:\mycode\awesome-copilot\instructions\typescript-mcp-server.instructions.md | Generated: 2025-10-17
