## What / When / Why / How

- What: C# MCP Server 专家（.NET DI、MCP 协议、工具/提示开发）
- When: 需要构建稳健、可测试、面向 LLM 的 MCP 服务器
- Why: 通过最佳实践（日志/错误/异步/DI）打造生产级质量
- How: 明确目标→依赖注入→工具/提示实现→日志/错误→示例/测试

## Key Points

- 包：ModelContextProtocol 系列（含 AspNetCore/Core）
- 日志：stderr, LogToStandardErrorThreshold=Trace
- 架构：Host.CreateApplicationBuilder + DI 生命周期
- 工具：注解 [McpServerToolType]/[McpServerTool]/[Description]
- 协议错误：McpProtocolException + McpErrorCode
- 友好：LLM 可用描述、简洁参数、JSON 可序列化

## Compact Map

- 需求→工具/提示设计
- DI/日志/异步/取消
- 安全与校验
- 代码示例与测试
- 性能与常见问题

## Example Questions (10+)

- 服务器目标与需要的工具能力是什么？
- 依赖注入的生命周期（Singleton/Scoped/Transient）如何划分？
- 如何配置标准错误日志与级别？
- 工具/参数的描述如何优化以便 LLM 使用？
- 协议错误如何分门别类并返回？
- 如何进行 stdio 传输调试与序列化问题排查？
- 需要哪些单元/集成测试来覆盖工具？
- 安全边界（文件/网络）如何限制与校验？
- 性能与内存优化点有哪些？
- 何时需要 AsSamplingChatClient？
- 版本/预发布包如何管理？

---
Source: d:\mycode\awesome-copilot\chatmodes\csharp-mcp-expert.chatmode.md
Generated: {{timestamp}}
