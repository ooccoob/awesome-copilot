---
applyTo: '**.cs, **.csproj'
description: 'This file provides guidance on building C# applications using GitHub Copilot SDK.'
name: 'GitHub Copilot SDK C# Instructions'
---

## 核心原则

- SDK 处于技术预览阶段，可能会有重大更改
- 需要 .NET 10.0 或更高版本
- 需要安装 GitHub Copilot CLI 并位于 PATH 中
- 始终使用异步/等待模式
- 实现 IAsyncDisposable 以进行资源清理

## 安装

始终通过 NuGet 安装：
```bash
dotnet add package GitHub.Copilot.SDK
```

## 客户端初始化

### 基本客户端设置

```csharp
await using var client = new CopilotClient();
await client.StartAsync();
```

### 客户端配置选项

创建 CopilotClient 时，使用 `CopilotClientOptions`：

- `CliPath` - CLI 可执行文件的路径（默认值：路径中的“copilot”）
- `CliArgs` - 在 SDK 管理的标志之前添加额外参数
- `CliUrl` - 现有 CLI 服务器的 URL（例如“localhost:8080”）。提供后，客户端不会生成进程
- `Port` - 服务器端口（默认值：0 表示随机）
- `UseStdio` - 使用 stdio 传输而不是 TCP（默认值：true）
- `LogLevel` - 日志级别（默认值：“info”）
- `AutoStart` - 自动启动服务器（默认值：true）
- `AutoRestart` - 崩溃时自动重新启动（默认值：true）
- `Cwd` - CLI 进程的工作目录
- `Environment` - CLI 进程的环境变量
- `Logger` - 用于 SDK 日志记录的 ILogger 实例

### 手动服务器控制

对于显式控制：
```csharp
var client = new CopilotClient(new CopilotClientOptions { AutoStart = false });
await client.StartAsync();
// Use client...
await client.StopAsync();
```

当 `StopAsync()` 花费太长时间时，请使用 `ForceStopAsync()`。

## 会话管理

### 创建会话

使用 `SessionConfig` 进行配置：

```csharp
await using var session = await client.CreateSessionAsync(new SessionConfig
{
    Model = "gpt-5",
    Streaming = true,
    Tools = [...],
    SystemMessage = new SystemMessageConfig { ... },
    AvailableTools = ["tool1", "tool2"],
    ExcludedTools = ["tool3"],
    Provider = new ProviderConfig { ... }
});
```

### 会话配置选项

- `SessionId` - 自定义会话 ID
- `Model` - 型号名称（“gpt-5”、“claude-sonnet-4.5”等）
- `Tools` - 暴露给 CLI 的自定义工具
- `SystemMessage` - 系统消息定制
- `AvailableTools` - 工具名称白名单
- `ExcludedTools` - 工具名称阻止列表
- `Provider` - 自定义 API 提供程序配置 (BYOK)
- `Streaming` - 启用流响应块（默认值： false）

### 恢复会话

```csharp
var session = await client.ResumeSessionAsync(sessionId, new ResumeSessionConfig { ... });
```

### 会话操作

- `session.SessionId` - 获取会话标识符
- `session.SendAsync(new MessageOptions { Prompt = "...", Attachments = [...] })` - 发送消息
- `session.AbortAsync()` - 中止当前处理
- `session.GetMessagesAsync()` - 获取所有事件/消息
- `await session.DisposeAsync()` - 清理资源

## 事件处理

### 事件订阅模式

始终使用 TaskCompletionSource 来等待会话事件：

```csharp
var done = new TaskCompletionSource();

session.On(evt =>
{
    if (evt is AssistantMessageEvent msg)
    {
        Console.WriteLine(msg.Data.Content);
    }
    else if (evt is SessionIdleEvent)
    {
        done.SetResult();
    }
});

await session.SendAsync(new MessageOptions { Prompt = "..." });
await done.Task;
```

### 取消订阅活动

`On()` 方法返回一个 IDisposable：

```csharp
var subscription = session.On(evt => { /* handler */ });
// Later...
subscription.Dispose();
```

### 事件类型

使用模式匹配或开关表达式进行事件处理：

```csharp
session.On(evt =>
{
    switch (evt)
    {
        case UserMessageEvent userMsg:
            // Handle user message
            break;
        case AssistantMessageEvent assistantMsg:
            Console.WriteLine(assistantMsg.Data.Content);
            break;
        case ToolExecutionStartEvent toolStart:
            // Tool execution started
            break;
        case ToolExecutionCompleteEvent toolComplete:
            // Tool execution completed
            break;
        case SessionStartEvent start:
            // Session started
            break;
        case SessionIdleEvent idle:
            // Session is idle (processing complete)
            break;
        case SessionErrorEvent error:
            Console.WriteLine($"Error: {error.Data.Message}");
            break;
    }
});
```

## 流式响应

### 启用流媒体

在 SessionConfig 中设置 `Streaming = true`：

```csharp
var session = await client.CreateSessionAsync(new SessionConfig
{
    Model = "gpt-5",
    Streaming = true
});
```

### 处理流媒体事件

处理增量事件（增量）和最终事件：

```csharp
var done = new TaskCompletionSource();

session.On(evt =>
{
    switch (evt)
    {
        case AssistantMessageDeltaEvent delta:
            // Incremental text chunk
            Console.Write(delta.Data.DeltaContent);
            break;
        case AssistantReasoningDeltaEvent reasoningDelta:
            // Incremental reasoning chunk (model-dependent)
            Console.Write(reasoningDelta.Data.DeltaContent);
            break;
        case AssistantMessageEvent msg:
            // Final complete message
            Console.WriteLine("\n--- Final ---");
            Console.WriteLine(msg.Data.Content);
            break;
        case AssistantReasoningEvent reasoning:
            // Final reasoning content
            Console.WriteLine("--- Reasoning ---");
            Console.WriteLine(reasoning.Data.Content);
            break;
        case SessionIdleEvent:
            done.SetResult();
            break;
    }
});

await session.SendAsync(new MessageOptions { Prompt = "Tell me a story" });
await done.Task;
```

注意：无论流设置如何，最终事件（`AssistantMessageEvent`、`AssistantReasoningEvent`）始终会发送。

## 定制工具

### 使用 AIFunctionFactory 定义工具

使用 `Microsoft.Extensions.AI.AIFunctionFactory.Create` 作为类型安全工具：

```csharp
using Microsoft.Extensions.AI;
using System.ComponentModel;

var session = await client.CreateSessionAsync(new SessionConfig
{
    Model = "gpt-5",
    Tools = [
        AIFunctionFactory.Create(
            async ([Description("Issue ID")] string id) => {
                var issue = await FetchIssueAsync(id);
                return issue;
            },
            "lookup_issue",
            "Fetch issue details from tracker"),
    ]
});
```

### 工具返回类型

- 返回任何 JSON 可序列化值（自动包装）
- 或者返回 `ToolResultAIContent` 包装 `ToolResultObject` 以完全控制元数据

### 工具执行流程

当 Copilot 调用工具时，客户端会自动：
1. 运行您的处理函数
2. 序列化返回值
3. 响应 CLI

## 系统消息定制

### 追加模式（默认 - 保留护栏）

```csharp
var session = await client.CreateSessionAsync(new SessionConfig
{
    Model = "gpt-5",
    SystemMessage = new SystemMessageConfig
    {
        Mode = SystemMessageMode.Append,
        Content = @"
<workflow_rules>
- Always check for security vulnerabilities
- Suggest performance improvements when applicable
</workflow_rules>
"
    }
});
```

### 更换模式（完全控制 - 移除护栏）

```csharp
var session = await client.CreateSessionAsync(new SessionConfig
{
    Model = "gpt-5",
    SystemMessage = new SystemMessageConfig
    {
        Mode = SystemMessageMode.Replace,
        Content = "You are a helpful assistant."
    }
});
```

## 文件附件

使用 `UserMessageDataAttachmentsItem` 将文件附加到消息：

```csharp
await session.SendAsync(new MessageOptions
{
    Prompt = "Analyze this file",
    Attachments = new List<UserMessageDataAttachmentsItem>
    {
        new UserMessageDataAttachmentsItem
        {
            Type = UserMessageDataAttachmentsItemType.File,
            Path = "/path/to/file.cs",
            DisplayName = "My File"
        }
    }
});
```

## 消息传递模式

使用 `MessageOptions` 中的 `Mode` 属性：

- `"enqueue"` - 等待处理的队列消息
- `"immediate"` - 立即处理消息

```csharp
await session.SendAsync(new MessageOptions
{
    Prompt = "...",
    Mode = "enqueue"
});
```

## 多次会议

会话是独立的并且可以同时运行：

```csharp
var session1 = await client.CreateSessionAsync(new SessionConfig { Model = "gpt-5" });
var session2 = await client.CreateSessionAsync(new SessionConfig { Model = "claude-sonnet-4.5" });

await session1.SendAsync(new MessageOptions { Prompt = "Hello from session 1" });
await session2.SendAsync(new MessageOptions { Prompt = "Hello from session 2" });
```

## 自带密钥 (BYOK)

通过 `ProviderConfig` 使用自定义 API 提供程序：

```csharp
var session = await client.CreateSessionAsync(new SessionConfig
{
    Provider = new ProviderConfig
    {
        Type = "openai",
        BaseUrl = "https://api.openai.com/v1",
        ApiKey = "your-api-key"
    }
});
```

## 会话生命周期管理

### 上市会议

```csharp
var sessions = await client.ListSessionsAsync();
foreach (var metadata in sessions)
{
    Console.WriteLine($"Session: {metadata.SessionId}");
}
```

### 删除会话

```csharp
await client.DeleteSessionAsync(sessionId);
```

### 检查连接状态

```csharp
var state = client.State;
```

## 错误处理

### 标准异常处理

```csharp
try
{
    var session = await client.CreateSessionAsync();
    await session.SendAsync(new MessageOptions { Prompt = "Hello" });
}
catch (StreamJsonRpc.RemoteInvocationException ex)
{
    Console.Error.WriteLine($"JSON-RPC Error: {ex.Message}");
}
catch (Exception ex)
{
    Console.Error.WriteLine($"Error: {ex.Message}");
}
```

### 会话错误事件

监视 `SessionErrorEvent` 的运行时错误：

```csharp
session.On(evt =>
{
    if (evt is SessionErrorEvent error)
    {
        Console.Error.WriteLine($"Session Error: {error.Data.Message}");
    }
});
```

## 连接测试

使用 PingAsync 验证服务器连接：

```csharp
var response = await client.PingAsync("test message");
```

## 资源清理

### 使用自动清理

始终使用 `await using` 进行自动处置：

```csharp
await using var client = new CopilotClient();
await using var session = await client.CreateSessionAsync();
// Resources automatically cleaned up
```

### 手动清理

如果不使用 `await using`：

```csharp
var client = new CopilotClient();
try
{
    await client.StartAsync();
    // Use client...
}
finally
{
    await client.StopAsync();
}
```

## 最佳实践

1. **始终对 CopilotClient 和 CopilotSession 使用 `await using`**
2. **使用TaskCompletionSource**等待SessionIdleEvent
3. **处理 SessionErrorEvent** 以实现强大的错误处理
4. **使用模式匹配**（开关表达式）进行事件处理
5. **启用流式传输**以在交互场景中获得更好的用户体验
6. **使用 AIFunctionFactory** 进行类型安全工具定义
7. **不再需要时处置事件订阅**
8. **使用 SystemMessageMode.Append** 保留安全护栏
9. **提供描述性工具名称和描述**以更好地理解模型
10. **启用流式传输时处理增量事件和最终事件**

## 常见模式

### 简单的查询-响应

```csharp
await using var client = new CopilotClient();
await client.StartAsync();

await using var session = await client.CreateSessionAsync(new SessionConfig
{
    Model = "gpt-5"
});

var done = new TaskCompletionSource();

session.On(evt =>
{
    if (evt is AssistantMessageEvent msg)
    {
        Console.WriteLine(msg.Data.Content);
    }
    else if (evt is SessionIdleEvent)
    {
        done.SetResult();
    }
});

await session.SendAsync(new MessageOptions { Prompt = "What is 2+2?" });
await done.Task;
```

### 多轮对话

```csharp
await using var session = await client.CreateSessionAsync();

async Task SendAndWait(string prompt)
{
    var done = new TaskCompletionSource();
    var subscription = session.On(evt =>
    {
        if (evt is AssistantMessageEvent msg)
        {
            Console.WriteLine(msg.Data.Content);
        }
        else if (evt is SessionIdleEvent)
        {
            done.SetResult();
        }
    });

    await session.SendAsync(new MessageOptions { Prompt = prompt });
    await done.Task;
    subscription.Dispose();
}

await SendAndWait("What is the capital of France?");
await SendAndWait("What is its population?");
```

### 具有复杂返回类型的工具

```csharp
var session = await client.CreateSessionAsync(new SessionConfig
{
    Tools = [
        AIFunctionFactory.Create(
            ([Description("User ID")] string userId) => {
                return new {
                    Id = userId,
                    Name = "John Doe",
                    Email = "john@example.com",
                    Role = "Developer"
                };
            },
            "get_user",
            "Retrieve user information")
    ]
});
```

