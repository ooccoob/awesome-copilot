## What/When/Why/How
- What: 使用 rmcp（Rust SDK）构建 MCP 服务器最佳实践
- When: 需要高性能/强类型的工具/资源/提示服务时
- Why: 利用 async/await + 类型系统 + 宏简化声明与校验
- How: ServerHandler/transport + #[tool]/router 宏 + 错误/日志/测试

## Key Points
- 依赖：rmcp/rmcp-macros/tokio/serde/schemars/anyhow/tracing
- 传输：Stdio/SSE/Streamable HTTP；Axum 集成；Ctrl+C 关闭
- 处理器：ServerHandler 实现 list/call；ToolRouter 分发
- 工具：#[tool] 参数 struct + JsonSchema；注解 destructive/read_only
- 提示/资源：list/get/read；mime/type/uri；分页与描述
- 错误：ErrorData 标准化；anyhow 上下文
- 状态：Arc<RwLock<T>> 共享；进度通知
- 测试：tokio::test 单测；集成测 server 交互
- 部署：release 构建/交叉编译；Docker 镜像

## Compact Map
- Handler: list/call/prompts/resources
- Transport: stdio | sse | http
- Macros: tool/tool_router/tool_handler
- Obs: tracing + structured logs

## Example Questions
1) 工具参数是否派生 Deserialize/JsonSchema？
2) 错误是否统一用 ErrorData 并带上下文？
3) 传输层是否按场景选择且支持中断？
4) 是否使用注解标明破坏性/只读/幂等提示？
5) 共享状态是否线程安全并避免竞争？
6) 是否提供进度通知以改善 UX？
7) 是否有覆盖率良好的单元/集成测试？
8) 是否使用 tracing 记录关键步骤与耗时？
9) 返回内容是否结构化（文本/图片等）并含 MIME？
10) Docker/跨平台发布是否配置完善？
11) 是否遵循 MCP 规范并验证兼容性？

Source: d:\mycode\awesome-copilot\instructions\rust-mcp-server.instructions.md | Generated: 2025-10-17
