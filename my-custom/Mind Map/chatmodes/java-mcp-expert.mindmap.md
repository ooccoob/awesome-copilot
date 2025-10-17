## What / When / Why / How

- What: Java MCP Server 专家（JVM/协议/并发/测试）
- When: 以 Java 实现生产级 MCP 服务器
- Why: 借助 JVM 生态与并发模型构建稳健服务
- How: 需求→工具/提示→序列化→并发/超时→日志/错误→测试

## Key Points

- 传输：stdio/WebSocket；JSON-RPC
- 并发：Executor/CompletableFuture；超时/取消
- 序列化：Jackson/Gson；记录类型
- 错误：分类/重试/退避
- 测试：JUnit/Mockito/Testcontainers

## Compact Map

- API/工具设计
- 并发资源控制
- 错误与可观测
- 测试与基准
- 部署与版本

## Example Questions (10+)

- 工具的输入输出应如何建模？
- 如何避免线程泄漏与阻塞？
- JSON 序列化的兼容性策略？
- 错误分类与重试策略如何定义？
- 端到端测试如何搭建？
- 如何记录与过滤敏感日志？
- 性能基线与压测场景？
- 配置与密钥管理方式？
- 与 IDE/扩展的集成约束？
- 版本发布与兼容策略？

---
Source: d:\mycode\awesome-copilot\chatmodes\java-mcp-expert.chatmode.md
Generated: {{timestamp}}
