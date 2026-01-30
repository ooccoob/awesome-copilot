## What
- 使用 Swift MCP SDK 构建 MCP 服务器的实践：工具/资源/提示、传输、并发 Actor、错误处理、包管理

## When
- 需要在 Apple 生态中实现本地/远程可交互的 MCP Server（stdio/HTTP/SSE）

## Why
- 类型安全并发模型、结构化协议处理、良好日志与生命周期管理

## How
- 服务端骨架
  - Server(name, version, capabilities)；withMethodHandler 注册 List/CallTool、List/ReadResource、List/GetPrompt 等
  - 初始化钩子：start(transport) { clientInfo, capabilities 校验 }
- 工具
  - 使用 Value(JSON Schema) 定义参数；CallTool 中解析/校验；isError 标识错误
- 资源
  - ListResources 与 ReadResource 返回 contents；订阅 ResourceSubscribe 追踪订阅集合
- 提示
  - ListPrompts/GetPrompt 产出描述与对话消息
- 传输
  - StdioTransport 本地子进程；HTTPClientTransport(streaming=true) 远程
- 并发/状态
  - 使用 actor 管理 ServerState（订阅/缓存）确保线程安全
- 错误/日志
  - 抛 MCPError 或捕获并包装 isError；swift-log 结构化日志
- 包管理
  - Package.swift 依赖 MCP SDK 与 swift-log；使用 ServiceLifecycle 做优雅关闭
- 模式
  - 批量请求 withBatch；严格模式 Client(configuration: .strict)；内容类型 text/image/resource

## Key Points
- 强类型 JSON Schema(Value)
- 每个 handler 都要进行输入校验与错误分支
- 传输关闭时清理资源

## Compact Map
- Server: capabilities/handlers/init
- Tools: List/Call + schema + error
- Resources: list/read/subscribe
- Prompts: list/get
- Transport: stdio/http
- Concurrency: actor state
- Logging: swift-log
- Lifecycle: ServiceLifecycle

## Example Questions
1) 如何为工具定义 JSON Schema 并做强类型解析？
2) 如何在 CallTool 中区分业务错误与系统错误？
3) 何时选择 StdioTransport 而非 HTTP？
4) 如何通过 actor 管理订阅集合避免竞态？
5) 如何实现初始化钩子校验客户端并拒绝？
6) 如何实现资源的订阅与通知？
7) 如何配置严格客户端并快速失败？
8) 如何组织批量请求并收集结果？
9) 如何优雅关闭并释放传输/资源？
10) 如何为不同内容类型构造返回？
11) Package.swift 最低平台与依赖如何设置？

Source: d:\mycode\awesome-copilot\instructions\swift-mcp-server.instructions.md | Generated: 2025-10-17
