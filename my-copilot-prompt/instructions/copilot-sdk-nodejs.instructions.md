---
applyTo: "**.ts, **.js, package.json"
description: "This file provides guidance on building Node.js/TypeScript applications using GitHub Copilot SDK."
name: "GitHub Copilot SDK Node.js Instructions"
---

## 核心原则

- SDK 处于技术预览阶段，可能会有重大更改
- 需要 Node.js 18.0 或更高版本
- 需要安装 GitHub Copilot CLI 并位于 PATH 中
- 使用 TypeScript 构建以确保类型安全
- 始终使用异步/等待模式
- 提供完整的 TypeScript 类型定义

## 安装

始终通过 npm/pnpm/yarn 安装：

```bash
npm install @github/copilot-sdk
# or
pnpm add @github/copilot-sdk
# or
yarn add @github/copilot-sdk
```

## 客户端初始化

### 基本客户端设置

```typescript
import { CopilotClient } from "@github/copilot-sdk";

const client = new CopilotClient();
await client.start();
// Use client...
await client.stop();
```

### 客户端配置选项

创建 CopilotClient 时，使用 `CopilotClientOptions`：

- `cliPath` - CLI 可执行文件的路径（默认值：路径中的“copilot”）
- `cliArgs` - 在 SDK 管理的标志之前添加额外参数 (string[])
- `cliUrl` - 现有 CLI 服务器的 URL（例如“localhost:8080”）。提供后，客户端不会生成进程
- `port` - 服务器端口（默认值：0 表示随机）
- `useStdio` - 使用 stdio 传输而不是 TCP（默认值：true）
- `logLevel` - 日志级别（默认值：“调试”）
- `autoStart` - 自动启动服务器（默认值：true）
- `autoRestart` - 崩溃时自动重新启动（默认值：true）
- `cwd` - CLI 进程的工作目录（默认值：process.cwd()）
- `env` - CLI 进程的环境变量（默认值：process.env）

### 手动服务器控制

对于显式控制：

```typescript
const client = new CopilotClient({ autoStart: false });
await client.start();
// Use client...
await client.stop();
```

当 `stop()` 花费太长时间时，请使用 `forceStop()`。

## 会话管理

### 创建会话

使用 `SessionConfig` 进行配置：

```typescript
const session = await client.createSession({
    model: "gpt-5",
    streaming: true,
    tools: [...],
    systemMessage: { ... },
    availableTools: ["tool1", "tool2"],
    excludedTools: ["tool3"],
    provider: { ... }
});
```

### 会话配置选项

- `sessionId` - 自定义会话 ID（字符串）
- `model` - 型号名称（“gpt-5”、“claude-sonnet-4.5”等）
- `tools` - 暴露给 CLI 的自定义工具 (Tool[])
- `systemMessage` - 系统消息定制（SystemMessageConfig）
- `availableTools` - 工具名称允许列表（字符串[]）
- `excludedTools` - 工具名称阻止列表（字符串[]）
- `provider` - 自定义 API 提供程序配置 (BYOK) (ProviderConfig)
- `streaming` - 启用流响应块（布尔值）
- `mcpServers` - MCP 服务器配置 (MCPServerConfig[])
- `customAgents` - 自定义代理配置 (CustomAgentConfig[])
- `configDir` - 配置目录覆盖（字符串）
- `skillDirectories` - 技能目录（字符串[]）
- `disabledSkills` - 禁用技能（字符串[]）
- `onPermissionRequest` - 权限请求处理程序（PermissionHandler）

### 恢复会话

```typescript
const session = await client.resumeSession("session-id", {
  tools: [myNewTool],
});
```

### 会话操作

- `session.sessionId` - 获取会话标识符（字符串）
- `await session.send({ prompt: "...", attachments: [...] })` - 发送消息，返回 Promise<string>
- `await session.sendAndWait({ prompt: "..." }, timeout)` - 发送并等待空闲，返回 Promise<AssistantMessageEvent |空>
- `await session.abort()` - 中止当前处理
- `await session.getMessages()` - 获取所有事件/消息，返回 Promise<SessionEvent[]>
- `await session.destroy()` - 清理会话

## 事件处理

### 事件订阅模式

始终使用 async/await 或 Promises 来等待会话事件：

```typescript
await new Promise<void>((resolve) => {
  session.on((event) => {
    if (event.type === "assistant.message") {
      console.log(event.data.content);
    } else if (event.type === "session.idle") {
      resolve();
    }
  });

  session.send({ prompt: "..." });
});
```

### 取消订阅活动

`on()` 方法返回一个取消订阅的函数：

```typescript
const unsubscribe = session.on((event) => {
  // handler
});
// Later...
unsubscribe();
```

### 事件类型

使用带有类型保护的可区分联合来进行事件处理：

```typescript
session.on((event) => {
  switch (event.type) {
    case "user.message":
      // Handle user message
      break;
    case "assistant.message":
      console.log(event.data.content);
      break;
    case "tool.executionStart":
      // Tool execution started
      break;
    case "tool.executionComplete":
      // Tool execution completed
      break;
    case "session.start":
      // Session started
      break;
    case "session.idle":
      // Session is idle (processing complete)
      break;
    case "session.error":
      console.error(`Error: ${event.data.message}`);
      break;
  }
});
```

## 流式响应

### 启用流媒体

在 SessionConfig 中设置 `streaming: true`：

```typescript
const session = await client.createSession({
  model: "gpt-5",
  streaming: true,
});
```

### 处理流媒体事件

处理增量事件（增量）和最终事件：

```typescript
await new Promise<void>((resolve) => {
  session.on((event) => {
    switch (event.type) {
      case "assistant.message.delta":
        // Incremental text chunk
        process.stdout.write(event.data.deltaContent);
        break;
      case "assistant.reasoning.delta":
        // Incremental reasoning chunk (model-dependent)
        process.stdout.write(event.data.deltaContent);
        break;
      case "assistant.message":
        // Final complete message
        console.log("\n--- Final ---");
        console.log(event.data.content);
        break;
      case "assistant.reasoning":
        // Final reasoning content
        console.log("--- Reasoning ---");
        console.log(event.data.content);
        break;
      case "session.idle":
        resolve();
        break;
    }
  });

  session.send({ prompt: "Tell me a story" });
});
```

注意：无论流设置如何，最终事件（`assistant.message`、`assistant.reasoning`）始终会发送。

## 定制工具

### 使用defineTool定义工具

使用 `defineTool` 进行类型安全工具定义：

```typescript
import { defineTool } from "@github/copilot-sdk";

const session = await client.createSession({
  model: "gpt-5",
  tools: [
    defineTool({
      name: "lookup_issue",
      description: "Fetch issue details from tracker",
      parameters: {
        type: "object",
        properties: {
          id: { type: "string", description: "Issue ID" },
        },
        required: ["id"],
      },
      handler: async (args) => {
        const issue = await fetchIssue(args.id);
        return issue;
      },
    }),
  ],
});
```

### 使用 Zod 作为参数

SDK 支持参数的 Zod 架构：

```typescript
import { z } from "zod";

const session = await client.createSession({
  tools: [
    defineTool({
      name: "get_weather",
      description: "Get weather for a location",
      parameters: z.object({
        location: z.string().describe("City name"),
        units: z.enum(["celsius", "fahrenheit"]).optional(),
      }),
      handler: async (args) => {
        return { temperature: 72, units: args.units || "fahrenheit" };
      },
    }),
  ],
});
```

### 工具返回类型

- 返回任何 JSON 可序列化值（自动包装）
- 或者返回 `ToolResultObject` 以完全控制元数据：

```typescript
{
    textResultForLlm: string;  // Result shown to LLM
    resultType: "success" | "failure";
    error?: string;  // Internal error (not shown to LLM)
    toolTelemetry?: Record<string, unknown>;
}
```

### 工具执行流程

当 Copilot 调用工具时，客户端会自动：

1. 运行您的处理函数
2. 序列化返回值
3. 响应 CLI

## 系统消息定制

### 追加模式（默认 - 保留护栏）

```typescript
const session = await client.createSession({
  model: "gpt-5",
  systemMessage: {
    mode: "append",
    content: `
<workflow_rules>
- Always check for security vulnerabilities
- Suggest performance improvements when applicable
</workflow_rules>
`,
  },
});
```

### 更换模式（完全控制 - 移除护栏）

```typescript
const session = await client.createSession({
  model: "gpt-5",
  systemMessage: {
    mode: "replace",
    content: "You are a helpful assistant.",
  },
});
```

## 文件附件

将文件附加到消息：

```typescript
await session.send({
  prompt: "Analyze this file",
  attachments: [
    {
      type: "file",
      path: "/path/to/file.ts",
      displayName: "My File",
    },
  ],
});
```

## 消息传递模式

在消息选项中使用 `mode` 属性：

- `"enqueue"` - 等待处理的队列消息
- `"immediate"` - 立即处理消息

```typescript
await session.send({
  prompt: "...",
  mode: "enqueue",
});
```

## 多次会议

会话是独立的并且可以同时运行：

```typescript
const session1 = await client.createSession({ model: "gpt-5" });
const session2 = await client.createSession({ model: "claude-sonnet-4.5" });

await Promise.all([
  session1.send({ prompt: "Hello from session 1" }),
  session2.send({ prompt: "Hello from session 2" }),
]);
```

## 自带密钥 (BYOK)

通过 `provider` 使用自定义 API 提供程序：

```typescript
const session = await client.createSession({
  provider: {
    type: "openai",
    baseUrl: "https://api.openai.com/v1",
    apiKey: "your-api-key",
  },
});
```

## 会话生命周期管理

### 上市会议

```typescript
const sessions = await client.listSessions();
for (const metadata of sessions) {
  console.log(`${metadata.sessionId}: ${metadata.summary}`);
}
```

### 删除会话

```typescript
await client.deleteSession(sessionId);
```

### 获取最后一个会话 ID

```typescript
const lastId = await client.getLastSessionId();
if (lastId) {
  const session = await client.resumeSession(lastId);
}
```

### 检查连接状态

```typescript
const state = client.getState();
// Returns: "disconnected" | "connecting" | "connected" | "error"
```

## 错误处理

### 标准异常处理

```typescript
try {
  const session = await client.createSession();
  await session.send({ prompt: "Hello" });
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```

### 会话错误事件

监视 `session.error` 事件类型的运行时错误：

```typescript
session.on((event) => {
  if (event.type === "session.error") {
    console.error(`Session Error: ${event.data.message}`);
  }
});
```

## 连接测试

使用 ping 验证服务器连接：

```typescript
const response = await client.ping("health check");
console.log(`Server responded at ${new Date(response.timestamp)}`);
```

## 资源清理

### 使用 Try-Finally 自动清理

始终在finally块中使用try-finally或cleanup：

```typescript
const client = new CopilotClient();
try {
  await client.start();
  const session = await client.createSession();
  try {
    // Use session...
  } finally {
    await session.destroy();
  }
} finally {
  await client.stop();
}
```

### 清理函数模式

```typescript
async function withClient<T>(
  fn: (client: CopilotClient) => Promise<T>,
): Promise<T> {
  const client = new CopilotClient();
  try {
    await client.start();
    return await fn(client);
  } finally {
    await client.stop();
  }
}

async function withSession<T>(
  client: CopilotClient,
  fn: (session: CopilotSession) => Promise<T>,
): Promise<T> {
  const session = await client.createSession();
  try {
    return await fn(session);
  } finally {
    await session.destroy();
  }
}

// Usage
await withClient(async (client) => {
  await withSession(client, async (session) => {
    await session.send({ prompt: "Hello!" });
  });
});
```

## 最佳实践

1. **始终使用 try-finally** 进行资源清理
2. **使用 Promises** 等待 session.idle 事件
3. **处理 session.error** 事件以实现强大的错误处理
4. **使用类型保护或 switch 语句**进行事件处理
5. **启用流式传输**以在交互场景中获得更好的用户体验
6. **使用defineTool**进行类型安全的工具定义
7. **使用 Zod 架构**进行运行时参数验证
8. **不再需要时处置事件订阅**
9. **使用带有模式：“append”的 systemMessage** 来保护安全护栏
10. **启用流式传输时处理增量事件和最终事件**
11. **利用 TypeScript 类型**实现编译时安全

## 常见模式

### 简单的查询-响应

```typescript
import { CopilotClient } from "@github/copilot-sdk";

const client = new CopilotClient();
try {
  await client.start();

  const session = await client.createSession({ model: "gpt-5" });
  try {
    await new Promise<void>((resolve) => {
      session.on((event) => {
        if (event.type === "assistant.message") {
          console.log(event.data.content);
        } else if (event.type === "session.idle") {
          resolve();
        }
      });

      session.send({ prompt: "What is 2+2?" });
    });
  } finally {
    await session.destroy();
  }
} finally {
  await client.stop();
}
```

### 多轮对话

```typescript
const session = await client.createSession();

async function sendAndWait(prompt: string): Promise<void> {
  await new Promise<void>((resolve, reject) => {
    const unsubscribe = session.on((event) => {
      if (event.type === "assistant.message") {
        console.log(event.data.content);
      } else if (event.type === "session.idle") {
        unsubscribe();
        resolve();
      } else if (event.type === "session.error") {
        unsubscribe();
        reject(new Error(event.data.message));
      }
    });

    session.send({ prompt });
  });
}

await sendAndWait("What is the capital of France?");
await sendAndWait("What is its population?");
```

### 发送并等待助手

```typescript
// Use built-in sendAndWait for simpler synchronous interaction
const response = await session.sendAndWait({ prompt: "What is 2+2?" }, 60000);

if (response) {
  console.log(response.data.content);
}
```

### 具有类型安全参数的工具

```typescript
import { z } from "zod";
import { defineTool } from "@github/copilot-sdk";

interface UserInfo {
  id: string;
  name: string;
  email: string;
  role: string;
}

const session = await client.createSession({
  tools: [
    defineTool({
      name: "get_user",
      description: "Retrieve user information",
      parameters: z.object({
        userId: z.string().describe("User ID"),
      }),
      handler: async (args): Promise<UserInfo> => {
        return {
          id: args.userId,
          name: "John Doe",
          email: "john@example.com",
          role: "Developer",
        };
      },
    }),
  ],
});
```

### 流媒体取得进展

```typescript
let currentMessage = "";

const unsubscribe = session.on((event) => {
  if (event.type === "assistant.message.delta") {
    currentMessage += event.data.deltaContent;
    process.stdout.write(event.data.deltaContent);
  } else if (event.type === "assistant.message") {
    console.log("\n\n=== Complete ===");
    console.log(`Total length: ${event.data.content.length} chars`);
  } else if (event.type === "session.idle") {
    unsubscribe();
  }
});

await session.send({ prompt: "Write a long story" });
```

### 错误恢复

```typescript
session.on((event) => {
  if (event.type === "session.error") {
    console.error("Session error:", event.data.message);
    // Optionally retry or handle error
  }
});

try {
  await session.send({ prompt: "risky operation" });
} catch (error) {
  // Handle send errors
  console.error("Failed to send:", error);
}
```

## TypeScript 特定的功能

### 类型推断

```typescript
import type { SessionEvent, AssistantMessageEvent } from "@github/copilot-sdk";

session.on((event: SessionEvent) => {
  if (event.type === "assistant.message") {
    // TypeScript knows event is AssistantMessageEvent here
    const content: string = event.data.content;
  }
});
```

### 通用助手

```typescript
async function waitForEvent<T extends SessionEvent["type"]>(
  session: CopilotSession,
  eventType: T,
): Promise<Extract<SessionEvent, { type: T }>> {
  return new Promise((resolve) => {
    const unsubscribe = session.on((event) => {
      if (event.type === eventType) {
        unsubscribe();
        resolve(event as Extract<SessionEvent, { type: T }>);
      }
    });
  });
}

// Usage
const message = await waitForEvent(session, "assistant.message");
console.log(message.data.content);
```
