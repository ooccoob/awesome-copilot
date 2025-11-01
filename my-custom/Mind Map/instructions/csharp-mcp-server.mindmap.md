## C# MCP 服务器开发要点

- What: 使用 C# SDK 构建 MCP 服务器（stdio/HTTP 传输）、工具与提示暴露、依赖注入与日志、错误模型。
- When: 实现面向 LLM 的工具/提示服务、组装最小服务器并注册程序集工具时。
- Why: 以标准协议向 LLM 暴露能力，便于测试、扩展与运维。
- How: HostBuilder + AddMcpServer + WithStdioServerTransport/WithToolsFromAssembly；用特性声明工具/提示；结构化日志输出到 stderr。

### 关键要点
- 包选择: ModelContextProtocol(.AspNetCore/.Core)。
- 传输: 首选 stdio（避免 stdout 干扰，日志写 stderr）；HTTP 选 AspNetCore 包。
- 工具暴露: [McpServerToolType] 标注类；[McpServerTool] 标注方法；[Description] 说明工具与参数；支持同步/Task/Task<T>。
- 依赖注入: 方法参数可注入 McpServer/HttpClient/自定义服务；支持 CancellationToken。
- 取样/回调: server.AsSamplingChatClient() 可向客户端发起采样请求。
- 提示暴露: [McpServerPromptType]/[McpServerPrompt]。
- 发现与注册: WithToolsFromAssembly() 自动发现当前程序集工具。
- 错误: 抛出 McpProtocolException 并带 McpErrorCode（如 InvalidParams）。
- 测试: 使用同 SDK 的 McpClient 或其他兼容客户端。

### 常用样例（概念）
- 基础服务: Host.CreateApplicationBuilder → AddMcpServer → WithStdioServerTransport → WithToolsFromAssembly → RunAsync。
- 简单工具: [McpServerTool] string Echo([Description] string input) => $"Echo: {input}"。
- DI 工具: 注入 HttpClient 获取远程内容；支持取消。
- 采样工具: 注入 McpServer，调用 AsSamplingChatClient().GetResponseAsync。

### 示例问题
1) 如何确保日志不干扰 stdio 通道？
2) 工具参数的可选/必填应如何描述？
3) 如何在工具中安全地发起回调采样请求？
4) 多程序集工具注册的组织方式？
5) HTTP 与 stdio 传输的选择与权衡？
6) 自定义 McpServerOptions/Handlers 的适用场景？
7) 如何编写集成测试覆盖工具调用成功/失败路径？
8) McpProtocolException 与业务异常如何区分？
9) 序列化复杂返回对象的注意事项？
10) 大量工具类型下的发现/装配性能优化？

Source: d:\mycode\awesome-copilot\instructions\csharp-mcp-server.instructions.md | Generated: 2025-10-17T00:00:00Z
