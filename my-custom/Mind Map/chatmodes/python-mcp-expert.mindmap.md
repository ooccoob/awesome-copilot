## What / When / Why / How

- What: Python MCP 服务器专家（mcp/FastMCP/stdio/HTTP）
- When: 需要构建类型安全、可维护的 MCP 服务器
- Why: 类型完善、结构化输出与健壮错误处理
- How: FastMCP 为默认；装饰器声明 tool/resource/prompt；完善类型与文档

## Key Points

- 类型优先：Pydantic/TypedDict；完整注释/返回结构
- 传输：stdio/streamable-http；Starlette/FastAPI 挂载
- 上下文：Context 日志/进度/采样/elicitation
- 测试：uv run mcp dev/ install；MCP Inspector
- 安全：CORS/认证/异常处理；stateless_http 可扩展

## Compact Map

- 需求→FastMCP→装饰器→结构化返回→传输→测试/部署

## Example Questions (10+)

- 使用 stdio 还是 HTTP？是否需要无状态？
- 工具/资源/提示的参数与模式？
- Pydantic 模型与字段校验如何定义？
- 何处需要 ctx.logging/progress/sampling？
- 错误语义与返回结构如何统一？
- Starlette/FastAPI 的挂载与 CORS？
- 测试路径与本地/集成验证？
- 版本/依赖与升级策略？
- 端到端示例与目录结构？
- 生产可观测性与限流？

---
Source: d:\mycode\awesome-copilot\chatmodes\python-mcp-expert.chatmode.md
Generated: {{timestamp}}
