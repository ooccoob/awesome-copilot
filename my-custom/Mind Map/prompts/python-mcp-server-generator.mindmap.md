## Python MCP 服务器生成器（思维导图）

- What
  - 使用 uv + mcp[cli] 生成可运行的 Python MCP 服务器（工具/资源/提示可选）
- When
  - 快速搭建本地/HTTP（streamable-http）可接入的 MCP 服务
- Why
  - 类型安全、错误处理完备、结构清晰、易于接入客户端
- How
  - 项目：uv init；uv add "mcp[cli]"；server.py 主文件
  - 传输：stdio 或 streamable-http（端口/无状态/JSON 响应）
  - 服务器：FastMCP；名称、说明；主入口 if __name__ == '__main__'
  - 工具：@mcp.tool 注解 + 完整类型提示与文档；Pydantic/TypedDict 输出
  - 资源/提示：@mcp.resource/@mcp.prompt（可选）；URI 模板与 Message 列表
  - 质量：PEP8、类型注解、async/await、上下文日志、资源清理
  - 测试：uv run mcp dev/install；示例调用与排障

- Key Points (CN/EN)
  - FastMCP; stdio/HTTP
  - Type hints; Pydantic
  - Tools/Resources/Prompts
  - MCP Inspector/Claude install

- Example Questions (≥10)
  1) 选择 stdio 还是 streamable-http？是否需要无状态/JSON 返回？
  2) 需要哪些工具（功能）及其输入输出 Schema？
  3) 是否需要资源/提示，资源 URI 模板如何设计？
  4) I/O 边界与异常分类/消息结构？
  5) 是否需要并发与异步 I/O（外部 API/文件）？
  6) 结构化输出是否采用 Pydantic/TypedDict？
  7) 运行/调试/安装到客户端的命令序列？
  8) 日志输出如何避免污染 stdout？
  9) 共享资源生命周期如何管理？
  10) 示例用例与回归测试如何编写？

- Compact Mind Map
  - 项目→传输→服务器→工具→资源→质量→测试

- Source: prompts/python-mcp-server-generator.prompt.md
- Generated: 2025-10-17
