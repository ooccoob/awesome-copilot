## What/When/Why/How
- What: 基于 Python MCP SDK 的服务器开发规范（FastMCP/装饰器/类型）
- When: 新建/扩展 MCP 工具、资源、提示服务时
- Why: 通过强类型与结构化输出提高可用性与兼容性
- How: FastMCP + @mcp.tool/resource/prompt + Pydantic/TypedDict 返回

## Key Points
- 依赖：uv 管理；mcp[cli]；FastMCP 初始化与 run(transport)
- 类型：参数/返回全量 type hints；Pydantic/TypedDict/dataclass
- 上下文：ctx.debug/info/warning/error；report_progress；elicit 输入
- 资源：@mcp.resource 模板 + URI；图片/图标 MIME 类型
- 提示：@mcp.prompt 返回 Message 序列；支持参数
- 传输：stdio/streamable-http；Starlette/FastAPI 挂载；CORS 暴露头
- 生命周期：lifespan 上下文；工具访问 shared 资源
- 日志：stderr 输出避免干扰 stdio；错误处理

## Compact Map
- Decorators: tool/resource/prompt
- Transport: stdio | streamable-http
- Context: logs/progress/elicit/sampling
- Models: BaseModel/TypedDict → JSON schema

## Example Questions
1) 工具参数/返回是否完整类型注解并可生成模式？
2) 复杂输出是否使用 Pydantic 模型而非裸 dict？
3) 是否使用 ctx.report_progress 提供长任务进度？
4) stdio 模式下日志是否仅写 stderr？
5) HTTP 模式是否配置 CORS 并暴露会话头？
6) 资源/提示是否可分页列出并带描述？
7) FastMCP 生命周期是否正确释放共享资源？
8) 调用失败时是否返回清晰错误并附上下文？
9) 是否提供本地 dev 安装与集成测试脚本？
10) 是否最小化依赖并锁定版本范围？
11) 是否考虑安全边界（FS/网络访问白名单）？

Source: d:\mycode\awesome-copilot\instructions\python-mcp-server.instructions.md | Generated: 2025-10-17
