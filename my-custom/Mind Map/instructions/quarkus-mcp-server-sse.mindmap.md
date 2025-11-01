## What/When/Why/How
- What: 基于 Quarkus 的 MCP 服务器（HTTP SSE 传输）规范
- When: 构建工具/资源/提示能力并通过 SSE 暴露时
- Why: 强类型、高性能与云原生可运维
- How: CDI + @Tool 注解 + 分层（tool→service→repo）+ SSE 端点

## Key Points
- 栈：Java21/Quarkus/CDI；mcp-server-sse 扩展；端点 /mcp/sse
- 分层：ApplicationScoped 工具仅做编排；业务在 Service
- 参数/返回：不可返回 null；校验入参；清晰错误
- 线程安全：服务层无共享可变或使用并发安全结构
- 命名/结构：PascalCase 类、camelCase 方法；包：model/repo/service/mcp
- Javadoc：公共方法文档与示例
- 常见陷阱：在工具中写业务；抛出未处理异常；未覆盖边界

## Compact Map
- Endpoint: /mcp/sse
- Tools: @Tool(name, description)
- Arch: tool→service→repo
- Errors: return error text, not null

## Example Questions
1) 工具是否仅编排且不含复杂业务？
2) SSE 端点是否稳定（断线重连/心跳）？
3) 入参校验是否完备并具错误消息？
4) 是否避免返回 null，使用错误对象/文本？
5) 共享状态是否线程安全或避免共享？
6) 包结构与命名是否一致可读？
7) 是否提供集成测试覆盖边界与异常？
8) 是否记录结构化日志便于排障？
9) 是否有示例 Javadoc 便于使用者？
10) 发布镜像/原生构建是否验证通过？
11) 是否定义幂等/只读工具语义（注解/约定）？

Source: d:\mycode\awesome-copilot\instructions\quarkus-mcp-server-sse.instructions.md | Generated: 2025-10-17
