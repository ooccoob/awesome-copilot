---
description: 'Instructions for building Model Context Protocol (MCP) servers using the TypeScript SDK'
applyTo: '**/*.ts, **/*.js, **/package.json'
---

# TypeScript MCP 服务器开发

## 使用说明

- 使用 **@modelcontextprotocol/sdk** npm 包：`npm install @modelcontextprotocol/sdk`
- 从特定路径导入：`@modelcontextprotocol/sdk/server/mcp.js`、`@modelcontextprotocol/sdk/server/stdio.js` 等。
- 使用 `McpServer` 类进行具有自动协议处理的高级服务器实现
- 使用 `Server` 类通过手动请求处理程序进行低级控制
- 使用 **zod** 进行输入/输出模式验证：`npm install zod@3`
- 始终为工具、资源和提示提供 `title` 字段，以实现更好的 UI 显示
- 使用 `registerTool()`、`registerResource()` 和 `registerPrompt()` 方法（推荐使用较旧的 API）
- 使用 zod 定义模式：`{ inputSchema: { param: z.string() }, outputSchema: { result: z.string() } }`
- 从工具返回 `content` （用于显示）和 `structuredContent` （用于结构化数据）
- 对于 HTTP 服务器，将 `StreamableHTTPServerTransport` 与 Express 或类似框架一起使用
- 对于本地集成，请使用 `StdioServerTransport` 进行基于 stdio 的通信
- 每个请求创建新的传输实例以防止请求 ID 冲突（无状态模式）
- 将会话管理与 `sessionIdGenerator` 用于有状态服务器
- 为本地服务器启用 DNS 重新绑定保护：`enableDnsRebindingProtection: true`
- 配置 CORS 标头并为基于浏览器的客户端公开 `Mcp-Session-Id`
- 对带有 URI 参数的动态资源使用 `ResourceTemplate`：`new ResourceTemplate('resource://{param}', { list: undefined })`
- 使用 `@modelcontextprotocol/sdk/server/completable.js` 中的 `completable()` 包装器支持补全以获得更好的用户体验
- 使用 `server.server.createMessage()` 实施抽样，以请求客户完成 LLM
- 使用 `server.server.elicitInput()` 在工具执行期间请求额外的用户输入
- 为批量更新启用通知去抖：`debouncedNotificationMethods: ['notifications/tools/list_changed']`
- 动态更新：在已注册的项目上调用 `.enable()`、`.disable()`、`.update()` 或 `.remove()` 以发出 `listChanged` 通知
- 使用 `@modelcontextprotocol/sdk/shared/metadataUtils.js` 中的 `getDisplayName()` 作为 UI 显示名称
- 使用 MCP Inspector 测试服务器：`npx @modelcontextprotocol/inspector`

## 最佳实践

- 让工具实现专注于单一职责
- 提供清晰、描述性的标题和描述，以帮助 LLM 理解
- 对所有参数和返回值使用正确的 TypeScript 类型
- 使用 try-catch 块实现全面的错误处理
- 在错误条件的工具结果中返回 `isError: true`
- 对所有异步操作使用 async/await
- 正确关闭数据库连接并清理资源
- 处理前验证输入参数
- 使用结构化日志记录进行调试，而不会污染 stdout/stderr
- 公开文件系统或网络访问时考虑安全隐患
- 对传输关闭事件实施适当的资源清理
- 使用环境变量进行配置（端口、API 密钥等）
- 清楚地记录工具的功能和限制
- 与多个客户端进行测试以确保兼容性

## 常见模式

### 基本服务器设置 (HTTP)
```typescript
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import express from 'express';

const server = new McpServer({
    name: 'my-server',
    version: '1.0.0'
});

const app = express();
app.use(express.json());

app.post('/mcp', async (req, res) => {
    const transport = new StreamableHTTPServerTransport({
        sessionIdGenerator: undefined,
        enableJsonResponse: true
    });
    
    res.on('close', () => transport.close());
    
    await server.connect(transport);
    await transport.handleRequest(req, res, req.body);
});

app.listen(3000);
```

### 基本服务器设置 (stdio)
```typescript
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new McpServer({
    name: 'my-server',
    version: '1.0.0'
});

// ... register tools, resources, prompts ...

const transport = new StdioServerTransport();
await server.connect(transport);
```

### 简单的工具
```typescript
import { z } from 'zod';

server.registerTool(
    'calculate',
    {
        title: 'Calculator',
        description: 'Perform basic calculations',
        inputSchema: { a: z.number(), b: z.number(), op: z.enum(['+', '-', '*', '/']) },
        outputSchema: { result: z.number() }
    },
    async ({ a, b, op }) => {
        const result = op === '+' ? a + b : op === '-' ? a - b : 
                      op === '*' ? a * b : a / b;
        const output = { result };
        return {
            content: [{ type: 'text', text: JSON.stringify(output) }],
            structuredContent: output
        };
    }
);
```

### 动态资源
```typescript
import { ResourceTemplate } from '@modelcontextprotocol/sdk/server/mcp.js';

server.registerResource(
    'user',
    new ResourceTemplate('users://{userId}', { list: undefined }),
    {
        title: 'User Profile',
        description: 'Fetch user profile data'
    },
    async (uri, { userId }) => ({
        contents: [{
            uri: uri.href,
            text: `User ${userId} data here`
        }]
    })
);
```

### 带采样的工具
```typescript
server.registerTool(
    'summarize',
    {
        title: 'Text Summarizer',
        description: 'Summarize text using LLM',
        inputSchema: { text: z.string() },
        outputSchema: { summary: z.string() }
    },
    async ({ text }) => {
        const response = await server.server.createMessage({
            messages: [{
                role: 'user',
                content: { type: 'text', text: `Summarize: ${text}` }
            }],
            maxTokens: 500
        });
        
        const summary = response.content.type === 'text' ? 
            response.content.text : 'Unable to summarize';
        const output = { summary };
        return {
            content: [{ type: 'text', text: JSON.stringify(output) }],
            structuredContent: output
        };
    }
);
```

### 提示完成
```typescript
import { completable } from '@modelcontextprotocol/sdk/server/completable.js';

server.registerPrompt(
    'review',
    {
        title: 'Code Review',
        description: 'Review code with specific focus',
        argsSchema: {
            language: completable(z.string(), value => 
                ['typescript', 'python', 'javascript', 'java']
                    .filter(l => l.startsWith(value))
            ),
            code: z.string()
        }
    },
    ({ language, code }) => ({
        messages: [{
            role: 'user',
            content: {
                type: 'text',
                text: `Review this ${language} code:\n\n${code}`
            }
        }]
    })
);
```

### 错误处理
```typescript
server.registerTool(
    'risky-operation',
    {
        title: 'Risky Operation',
        description: 'An operation that might fail',
        inputSchema: { input: z.string() },
        outputSchema: { result: z.string() }
    },
    async ({ input }) => {
        try {
            const result = await performRiskyOperation(input);
            const output = { result };
            return {
                content: [{ type: 'text', text: JSON.stringify(output) }],
                structuredContent: output
            };
        } catch (err: unknown) {
            const error = err as Error;
            return {
                content: [{ type: 'text', text: `Error: ${error.message}` }],
                isError: true
            };
        }
    }
);
```
