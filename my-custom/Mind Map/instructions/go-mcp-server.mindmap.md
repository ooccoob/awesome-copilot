## What/When/Why/How
- What: 使用 modelcontextprotocol/go-sdk 实现 Go MCP 服务器的最佳实践
- When: 新建/扩展 MCP 服务器、编写工具/资源/提示、配置传输
- Why: 标准化能力注册、类型安全 I/O、稳定传输与优雅退出
- How: mcp.NewServer + Options/Capabilities，AddTool/AddResource/AddPrompt，Stdio/HTTP 传输，context 与错误处理

## Key Points
- Server: mcp.NewServer(Implementation, Options)
- Tool: 结构化输入/输出（json/jsonschema tag），类型安全处理器
- Resource: AddResource + ReadResource 回调返回 TextResourceContents
- Prompt: AddPrompt + 输入参数声明 + 消息模板
- Transport: Stdio（默认桌面）、HTTP（需要地址/TLS）
- Context: 取消/超时检查；尽早返回
- 错误: 标准 error 包装与 %w 传播
- 选项: Capabilities.Tools/Resources.Subscribe/Prompts
- 测试: 标准 testing；表驱动

## Compact Map
NewServer→Tools→Resources→Prompts→Transport→Context→Errors→Options→Testing

## Example Questions (10+)
1) 最小可运行的 Stdio MCP 服务器骨架
2) 写一个 search 工具（带输入/输出结构体与 jsonschema 标签）
3) 注册文件资源并实现 ReadResourceResult 返回文本
4) 定义 analyze 提示模板并声明必填参数
5) 将传输从 Stdio 切换到 HTTP 并监听 8080
6) 在工具中正确处理 context 取消与超时
7) 统一错误包装并附加上下文（%w）
8) 配置 Resources.Subscribe=true 的示例
9) 为工具编写单元测试（表驱动）
10) 使用 slog 记录调用入参/出参但避免敏感信息

Source: d:\mycode\awesome-copilot\instructions\go-mcp-server.instructions.md | Generated: 2025-10-17T00:00:00Z
