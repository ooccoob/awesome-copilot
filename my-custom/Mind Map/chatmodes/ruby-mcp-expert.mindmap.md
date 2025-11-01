## What / When / Why / How

- What: Ruby MCP 服务器专家（官方 Ruby SDK + 可与 Rails 集成）
- When: 需要实现生产级、结构化可用的 MCP 服务器
- Why: 强类型 schema、工具/资源/提示装配与健壮错误处理
- How: 服务器/工具/资源/提示类组织；传输（stdio/HTTP/SSE）；测试

## Key Points

- 工具：MCP::Tool；input/output_schema；annotations；is_error
- 资源：resources_read_handler；URI 模板
- 集成：Rails 控制器；异常上报与埋点
- 返回：结构化内容 + 文本

## Compact Map

- Gem 依赖→Server→Tool/Prompt/Resource→Transport→Rails/监控

## Example Questions (10+)

- 工具输入/输出 schema 如何定义与验证？
- 错误与异常的协议化表达？
- 资源 URI 模板与读取策略？
- Rails 控制器集成与授权？
- SSE/HTTP 的部署与伸缩？
- 结构化内容与文本的组合策略？
- 仪表与告警方案？
- 测试（金字塔）策略？
- 自定义 JSON-RPC 方法场景？
- 版本管理与升级路径？

---
Source: d:\mycode\awesome-copilot\chatmodes\ruby-mcp-expert.chatmode.md
Generated: {{timestamp}}
