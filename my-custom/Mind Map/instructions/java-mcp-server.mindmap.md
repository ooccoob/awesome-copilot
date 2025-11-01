## What/When/Why/How
- What: 使用官方 Java MCP SDK 构建 MCP Server（工具/资源/提示，Reactive Streams）。
- When: 需要为 LLM/代理提供工具调用、资源读取/订阅、Prompt 模板等协议化能力时。
- Why: 标准化对接、类型安全 JSON Schema、良好异步与可观测性支持、Spring 生态集成。
- How: 引入依赖→构建 Server → 注册 tools/resources/prompts → 选择传输 → 编写处理器与测试。

## Key Points
- 依赖：io.modelcontextprotocol.sdk:mcp 与可选 mcp-spring-boot-starter。
- 传输：stdio、本地 Servlet/HTTP、（可）SSE；生命周期与优雅停机。
- 工具：定义 JSON Schema、返回 ToolResponse；校验输入、超时/重试、错误分类。
- 资源：list/read/subscribe 处理器；推送 listChanged；缓存与订阅管理。
- 提示：prompt 列表/get；参数化消息模板。
- Reactive：Mono/Flux，boundedElastic 处理阻塞；Context 传播 traceId。
- 测试：同步 API（toSyncServer）便于断言；Jackson 自定义序列化。
- 观测：SLF4J 日志；异常只记录一次；分类错误返回。

## Compact Map
Server
- Capabilities: tools/resources/prompts
- Transport: stdio | servlet
- Handlers: tool/resource/prompt
- Reactive: Mono/Flux + Schedulers
- Spring: Starter + @Component Handler
- JSON Schema: fluent builder
- Error: Validation vs Unexpected
- Lifecycle: start/stop + hook

## Checklist
- [ ] 为每个 tool 定义严格输入Schema并验证
- [ ] 阻塞调用放 boundedElastic，设超时
- [ ] Resource 缓存与订阅去重
- [ ] 结构化日志 + traceId 传递
- [ ] 同步API编写最小可测用例
- [ ] 优雅停机释放资源

## Example Questions (≥10)
- 如何为工具定义 JSON Schema 并在处理器中做输入校验？
- 何时使用 Mono/Flux 与哪些场景需要 boundedElastic？
- 如何实现资源订阅与 listChanged 通知？
- 在 Spring Boot 中如何以 Bean 形式注册工具处理器？
- ToolResponse 如何返回多内容类型（文本/图片/资源）？
- 如何在 Reactor 上下文中传播 traceId？
- 同步 API 如何用于单元测试最小闭环？
- 服务器优雅停机的通用做法有哪些？
- 如何封装通用错误处理并区分校验与系统异常？
- Stdio 与 Servlet 传输选择的权衡是什么？

Source: d:\mycode\awesome-copilot\instructions\java-mcp-server.instructions.md | Generated: 2025-10-17
