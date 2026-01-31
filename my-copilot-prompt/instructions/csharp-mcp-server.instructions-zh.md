---
描述：“使用 C# SDK 构建模型上下文协议 (MCP) 服务器的说明”
applyTo: '**/*.cs, **/*.csproj'
---

# C# MCP 服务器开发

## 使用说明

- 对于大多数项目，使用 **ModelContextProtocol** NuGet 包（预发行版）：`dotnet add package ModelContextProtocol --prerelease`
- 对基于 HTTP 的 MCP 服务器使用 **ModelContextProtocol.AspNetCore**
- 使用 **ModelContextProtocol.Core** 实现最小依赖（仅限客户端或低级服务器 API）
- 始终使用 `LogToStandardErrorThreshold = LogLevel.Trace` 配置日志记录到 stderr，以避免干扰 stdio 传输
- 在包含 MCP 工具的类上使用 `[McpServerToolType]` 属性
- 在方法上使用 `[McpServerTool]` 属性将它们公开为工具
- 使用 `System.ComponentModel` 中的 `[Description]` 属性来记录工具和参数
- 支持工具方法中的依赖注入 - 注入 `McpServer`、`HttpClient` 或其他服务作为参数
- 使用 `McpServer.AsSamplingChatClient()` 从工具内向客户端发出采样请求
- 在类上使用 `[McpServerPromptType]` 并在方法上使用 `[McpServerPrompt]` 来公开提示
- 对于 stdio 传输，在构建服务器时使用 `WithStdioServerTransport()`
- 使用 `WithToolsFromAssembly()` 自动发现并注册当前程序集中的所有工具
- 工具方法可以是同步的或异步的（返回 `Task` 或 `Task<T>`）
- 始终包含工具和参数的全面描述，以帮助法学硕士了解其目的
- 在异步工具中使用 `CancellationToken` 参数以获得正确的取消支持
- 返回简单类型（string、int等）或可以序列化为JSON的复杂对象
- 对于细粒度控制，请将 `McpServerOptions` 与自定义处理程序（例如 `ListToolsHandler` 和 `CallToolHandler`）结合使用
- 使用 `McpProtocolException` 来处理具有适当 `McpErrorCode` 值的协议级错误
- 使用来自同一 SDK 或任何兼容的 MCP 客户端的 `McpClient` 测试 MCP 服务器
- 使用 Microsoft.Extensions.Hosting 构建项目以进行正确的 DI 和生命周期管理

## 最佳实践

- 保持工具方法集中且单一目的
- 使用有意义的工具名称，清楚地表明其功能
- 提供详细说明，解释该工具的用途、期望的参数以及返回的内容
- 验证输入参数，并针对无效输入抛出 `McpProtocolException` 和 `McpErrorCode.InvalidParams`
- 使用结构化日志记录来帮助调试而不污染标准输出
- 使用 `[McpServerToolType]` 将相关工具组织成逻辑类
- 公开访问外部资源的工具时考虑安全隐患
- 使用内置 DI 容器来管理服务生命周期和依赖项
- 实施正确的错误处理并返回有意义的错误消息
- 在与法学硕士集成之前单独测试工具

## 常见模式

### 基本服务器设置
```csharp
var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(options => 
    options.LogToStandardErrorThreshold = LogLevel.Trace);
builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();
```

### 简单的工具
```csharp
[McpServerToolType]
public static class MyTools
{
    [McpServerTool, Description("Description of what the tool does")]
    public static string ToolName(
        [Description("Parameter description")] string param) => 
        $"Result: {param}";
}
```

### 具有依赖注入的工具
```csharp
[McpServerTool, Description("Fetches data from a URL")]
public static async Task<string> FetchData(
    HttpClient httpClient,
    [Description("The URL to fetch")] string url,
    CancellationToken cancellationToken) =>
    await httpClient.GetStringAsync(url, cancellationToken);
```

### 带采样的工具
```csharp
[McpServerTool, Description("Analyzes content using the client's LLM")]
public static async Task<string> Analyze(
    McpServer server,
    [Description("Content to analyze")] string content,
    CancellationToken cancellationToken)
{
    var messages = new ChatMessage[]
    {
        new(ChatRole.User, $"Analyze this: {content}")
    };
    return await server.AsSamplingChatClient()
        .GetResponseAsync(messages, cancellationToken: cancellationToken);
}
```
