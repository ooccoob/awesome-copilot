## Rust MCP Server Generator — Mind Map

### What
- 基于 rmcp 官方 SDK 生成具工具/提示/资源/测试的完整 Rust MCP 服务器脚手架。

### When
- 需要高性能、强类型、可测试的 MCP 服务端起步工程时。

### Why
- 统一项目结构与依赖，减少样板；保障可维护与扩展性。

### How
- 询问参数→生成 Cargo.toml/src/**/*/tests→使用 rmcp-macros 定义工具→实现 handler/state → 配置 transports 与日志。

### Key Points (中/英)
- 工具/Tools (macros)
- 状态/State (Arc/RwLock)
- 处理器/Handler (async)
- 传输/Transport (stdio/http)
- 测试/Tests (tokio)
- 日志/Tracing

### Compact map
- src: main.rs, handler.rs, state.rs, tools/, prompts/, resources/
- features: http 可选
- tests: integration_test.rs
- dependencies: rmcp, tokio, serde, tracing

### Example Questions (≥10)
- 如何选择 stdio/SSE/HTTP 传输并抽象切换？
- 工具参数类型为何需 JsonSchema？
- 如何在 handler 中优雅路由与错误处理？
- 共享状态在并发下的正确用法？
- 集成测试如何模拟调用与断言结果？
- 分层（tools/prompts/resources）如何保持清晰边界？
- 日志与诊断（tracing）最佳粒度建议？
- features 与可选依赖如何组织？
- 性能与内存占用的常见陷阱？
- 与客户端（如 Claude）集成的配置示例？

---
- Source: d:\mycode\awesome-copilot\prompts\rust-mcp-server-generator.prompt.md
- Generated: 2025-10-17
