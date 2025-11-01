## What / When / Why / How

- What: Swift MCP 服务器专家（官方 Swift SDK + 现代并发）
- When: 构建生产级、并发安全的 MCP 服务器
- Why: Actor 隔离 + async/await 保证正确性与性能
- How: Server/Transport/Handlers→工具/资源/提示→状态 Actor→日志/错误→测试

## Key Points

- 传输：Stdio/HTTP/Network/InMemory；ServiceLifecycle 优雅关停
- 工具：Value 构建 JSON Schema；CallTool 处理
- 资源：ReadResource/订阅/变更通知；多内容响应
- 并发：Actor 隔离；任务组；取消与错误传播
- 日志：swift-log；调试等级

## Compact Map

- 依赖→Server→Handlers→Transport→Actor 状态→测试/部署

## Example Questions (10+)

- 工具参数 Schema 如何用 Value 定义？
- 资源订阅与变更通知的实现？
- 传输选型与部署拓扑？
- Actor 状态模型与并发场景？
- 错误处理与返回约定？
- 初始化 Hook 与客户端能力协商？
- 日志/指标与调试策略？
- 平台支持与条件编译？
- 异步测试与样例？
- 性能优化与背压策略？

---
Source: d:\mycode\awesome-copilot\chatmodes\swift-mcp-expert.chatmode.md
Generated: {{timestamp}}
