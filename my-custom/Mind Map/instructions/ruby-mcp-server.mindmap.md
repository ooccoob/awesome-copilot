## What/When/Why/How
- What: 使用 Ruby MCP SDK 构建 MCP 服务器（工具/资源/提示/传输）
- When: 需快速提供强类型工具与结构化输出时
- Why: 简洁声明（类或块）+ 输入/输出 schema + 注解增强
- How: gem 'mcp' + 定义 Tool/Resource/Prompt + stdio/HTTP/streamable

## Key Points
- 工具：类式或块式；input_schema/output_schema；annotations（只读/幂等）
- 资源：注册资源/模板；read 处理器按 URI 返回 MIME
- 提示：类或块；参数/消息模板；描述
- 传输：Stdio/HTTP/Streamable；Rails 控制器集成
- 上下文：server_context 传 user_id/request_id 等
- 监控：exception_reporter + instrumentation 回调
- 通知：工具/提示/资源列表变更通知
- 客户端：HTTP 传输 + 列表/调用

## Compact Map
- Tools: schema + annotations + response
- Resources: uri + mime + read_handler
- Prompts: args + messages
- Transport: stdio/http/streamable

## Example Questions
1) 工具是否定义了输入/输出 schema 并验证？
2) 是否使用 annotations 标注只读/幂等等语义？
3) 资源 read 是否返回正确 MIME 与内容？
4) 提示的 messages 是否结构化且含描述？
5) HTTP 集成是否处理鉴权与限流？
6) exception_reporter 是否接入告警平台？
7) instrumentation 是否记录方法名/耗时/错误？
8) 是否在变更后发送列表通知给客户端？
9) server_context 是否最小化且无敏感明文？
10) 是否提供最小客户端示例与集成测试？
11) 协议版本/兼容性是否可配置并已验证？

Source: d:\mycode\awesome-copilot\instructions\ruby-mcp-server.instructions.md | Generated: 2025-10-17
