---
description: '使用 C# SDK 构建模型上下文协议 (MCP) 服务器的指令'
applyTo: '**/*.cs, **/*.csproj'
---

# C# MCP 服务器开发

## 指令

- 对大多数项目使用 **ModelContextProtocol** NuGet 包（预览版）：`dotnet add package ModelContextProtocol --prerelease`
- 对基于 HTTP 的 MCP 服务器使用 **ModelContextProtocol.AspNetCore**
- 对最小依赖项（仅客户端或低级服务器 API）使用 **ModelContextProtocol.Core**
- 始终配置日志记录到 stderr，使用 `LogToStandardErrorThreshold = LogLevel.Trace` 以避免干扰 stdio 传输
- 在包含 MCP 工具的类上使用 `[McpServerToolType]` 属性
- 在方法上使用 `[McpServerTool]` 属性将它们公开为工具
- 使用 `System.ComponentModel` 中的 `[Description]` 属性来记录工具和参数
- 支持工具方法中的依赖注入 - 注入 `McpServer`、`HttpClient` 或其他服务作为参数
- 使用 `McpServer.AsSamplingChatClient()` 从工具内向客户端发回采样请求
- 在类上使用 `[McpServerPromptType]`、在方法上使用 `[McpServerPrompt]` 来公开提示
- 对于 stdio 传输，构建服务器时使用 `WithStdioServerTransport()`
- 使用 `WithToolsFromAssembly()` 自动发现和注册当前程序集中的所有工具
- 工具方法可以是同步或异步的（返回 `Task` 或 `Task<T>`）
- 始终包含工具和参数的全面描述，以帮助 LLM 理解其用途
- 在异步工具中使用 `CancellationToken` 参数以实现适当的取消支持
- 返回简单类型（string、int 等）或可以序列化为 JSON 的复杂对象
- 对于细粒度控制，使用带有自定义处理器的 `McpServerOptions`，如 `ListToolsHandler` 和 `CallToolHandler`
- 对协议级错误使用 `McpProtocolException` 并带有适当的 `McpErrorCode` 值
- 使用来自同一 SDK 的 `McpClient` 或任何兼容的 MCP 客户端测试 MCP 服务器
- 使用 Microsoft.Extensions.Hosting 构建项目以实现适当的 DI 和生命周期管理

## 最佳实践

- 保持工具方法专注和单一目的
- 使用清晰表明其功能的有意义的工具名称
- 提供详细描述，解释工具的功能、期望的参数和返回的内容
- 验证输入参数并对无效输入抛出带有 `McpErrorCode.InvalidParams` 的 `McpProtocolException`
- 使用结构化日志记录以帮助调试而不污染 stdout
- 使用 `[McpServerToolType]` 将相关工具组织到逻辑类中
- 在暴露访问外部资源的工具时考虑安全影响
- 使用内置 DI 容器管理服务生命周期和依赖项
- 实现适当的错误处理并返回有意义的错误消息
- 在与 LLM 集成之前单独测试工具

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

### 简单工具
```csharp
[McpServerToolType]
public static class MyTools
{
    [McpServerTool, Description("工具功能的描述")]
    public static string ToolName(
        [Description("参数描述")] string param) =>
        $"结果: {param}";
}
```

### 带依赖注入的工具
```csharp
[McpServerTool, Description("从 URL 获取数据")]
public static async Task<string> FetchData(
    HttpClient httpClient,
    [Description("要获取的 URL")] string url,
    CancellationToken cancellationToken) =>
    await httpClient.GetStringAsync(url, cancellationToken);
```

### 带采样的工具
```csharp
[McpServerTool, Description("使用客户端的 LLM 分析内容")]
public static async Task<string> Analyze(
    McpServer server,
    [Description("要分析的内容")] string content,
    CancellationToken cancellationToken)
{
    var messages = new ChatMessage[]
    {
        new(ChatRole.User, $"分析这个: {content}")
    };
    return await server.AsSamplingChatClient()
        .GetResponseAsync(messages, cancellationToken: cancellationToken);
}
```