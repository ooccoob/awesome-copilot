## What/When/Why/How
- What: 基于官方 Kotlin MCP SDK 构建 MCP 服务器（工具/资源/提示、协程、Ktor 传输、多平台）。
- When: 以 Kotlin/JVM 或 KMP 交付 LLM 工具端点与资源访问时。
- Why: 类型安全、协程友好的异步模型、便捷的 Stdio 与 SSE/HTTP 集成。
- How: 声明 Server + Capabilities → addTool/addResource/addPrompt → 选择传输（Stdio/Ktor）→ 测试。

## Key Points
- Server：Implementation/ServerOptions/Capabilities；描述信息与能力。
- Tools：输入 JSON Schema（kotlinx.serialization 或手写 JsonObject）；CallToolRequest/Result。
- Resources：ReadResourceRequest/Result，TextResourceContents；notifyResourceListChanged。
- Prompts：GetPromptRequest/Result，PromptMessage/Role。
- 传输：StdioServerTransport；Ktor mcp{} SSE 集成。
- 协程：suspend 处理器；coroutineScope/async 并行；超时与错误处理。
- 构建：Gradle Kotlin DSL；kotlinx-serialization/coroutines；KMP 支持。
- 日志：kotlin-logging；结构化上下文。

## Compact Map
Kotlin MCP
- Server/Capabilities
- Tools/Resource/Prompt
- Transport: stdio | Ktor SSE
- Coroutines: suspend/async
- JSON schema: kotlinx.serialization
- KMP 支持

## Checklist
- [ ] 工具输入严格校验与清晰错误信息
- [ ] 协程并行受控 + 超时
- [ ] 资源订阅/变更通知
- [ ] Ktor 路由最小可用示例
- [ ] 单元测试使用 runTest

## Example Questions (≥10)
- 如何为工具构建类型安全的输入 Schema？
- suspend 处理器里并发查询的最佳实践是什么？
- 如何在资源更新时通知客户端 listChanged？
- Stdio 与 SSE/HTTP 的取舍点？
- 如何在多平台项目中共享协议层代码？
- 如何组织错误返回与异常日志？
- 如何在 Gradle 中配置 serialization/coroutines？
- 如何对工具进行单元测试并断言内容输出？
- Ktor 集成需要注意哪些依赖与版本匹配？
- 如何在 Dev 与 Prod 中分别配置传输与日志级别？

Source: d:\mycode\awesome-copilot\instructions\kotlin-mcp-server.instructions.md | Generated: 2025-10-17
