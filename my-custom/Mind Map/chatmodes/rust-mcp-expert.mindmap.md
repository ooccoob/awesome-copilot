## What / When / Why / How

- What: Rust MCP 服务器专家（rmcp SDK + tokio）
- When: 构建高性能、类型安全的 MCP 服务器
- Why: 宏/类型驱动的工具与处理器，可靠传输与错误语义
- How: 工具宏/路由/处理器→传输（stdio/SSE/HTTP）→状态与错误→测试/部署

## Key Points

- 宏：#[tool]/#[tool_router]/#[tool_handler]
- 类型：Serde/JsonSchema；Parameters<T>
- 传输：Stdio/SSE/Streamable HTTP（Axum）
- 状态：Arc<RwLock<..>>；锁粒度/并发
- 错误：ErrorData/anyhow；Result 语义

## Compact Map

- 工具/路由→传输→资源/提示→状态→错误→测试/部署

## Example Questions (10+)

- 工具参数与 JsonSchema 如何定义？
- 传输与部署拓扑选择？
- 状态共享与锁竞争如何优化？
- 协议错误与应用错误分层？
- 单测/集成测试覆盖面？
- 性能热点与度量？
- 跨平台构建与容器化？
- 宏使用的可维护性？
- 资源/提示的实现与分页？
- 鉴权/限流/可观测性？

---
Source: d:\mycode\awesome-copilot\chatmodes\rust-mcp-expert.chatmode.md
Generated: {{timestamp}}
