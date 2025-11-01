## What / When / Why / How

- What: Go MCP Server 专家（协议/工具/并发/测试）
- When: 需要以 Go 实现高质量 MCP 服务器
- Why: 利用 Go 并发/内存模型与生态实现稳健服务
- How: 需求→工具/提示→并发安全→错误/日志→测试/示例

## Key Points

- 协议：JSON-RPC/stdio/WebSocket
- 并发：context/errgroup/通道；超时与取消
- 结构：package 划分、接口与依赖注入
- 可靠性：错误包装、重试/退避、限流
- 测试：table-driven、race detector、bench

## Compact Map

- API/工具设计
- 并发与资源控制
- 错误与可观测
- 测试与基准
- 部署与版本

## Example Questions (10+)

- 工具与提示的接口如何对 LLM 友好？
- 如何组织并发与取消，避免泄漏？
- 错误类型与上下文信息如何包装？
- 需要哪些限流/熔断与重试策略？
- 标准 I/O 与 WS 的选择与调试手段？
- 如何进行端到端与竞态检测？
- 序列化性能与内存分配如何优化？
- 配置/密钥如何安全加载？
- 日志与指标如何暴露？
- 模块化与版本策略如何制定？

---
Source: d:\mycode\awesome-copilot\chatmodes\go-mcp-expert.chatmode.md
Generated: {{timestamp}}
