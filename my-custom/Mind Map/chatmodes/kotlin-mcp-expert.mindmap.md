## What / When / Why / How

- What: Kotlin MCP Server 专家（协程/结构化并发/类型安全）
- When: 以 Kotlin 构建类型安全与并发友好服务器
- Why: 借助协程与 DSL 提升可读性与可靠性
- How: 协程上下文→结构化并发→序列化→错误/日志→测试

## Key Points

- 协程：scope/supervisor/job；超时/取消
- 序列化：kotlinx.serialization/Jackson
- 设计：sealed class/Result/Either
- 测试：runTest/flows/挂起函数
- 平台：JVM/Native；Ktor/Netty

## Compact Map

- API 设计与类型建模
- 并发与资源控制
- 错误与重试
- 测试与基准
- 部署与版本

## Example Questions (10+)

- 协程作用域与取消传播如何设计？
- 挂起 API 的错误如何表达与恢复？
- 序列化策略如何兼容进化？
- Flow/Channel 何时选用？
- 测试中如何控制时间与调度器？
- 配置与密钥如何注入？
- Ktor/Netty 的选择依据？
- 性能与内存基线？
- 端到端示例与契约测试？
- 构建与发布策略？

---
Source: d:\mycode\awesome-copilot\chatmodes\kotlin-mcp-expert.chatmode.md
Generated: {{timestamp}}
