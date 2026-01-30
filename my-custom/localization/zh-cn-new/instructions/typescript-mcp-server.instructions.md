---
description: '使用 TypeScript SDK 构建模型上下文协议 (MCP) 服务器的指令'
applyTo: '**/*.ts, **/*.js, **/package.json'
---

# TypeScript MCP 服务器开发

## 指令

- 使用 **@modelcontextprotocol/sdk** npm 包：`npm install @modelcontextprotocol/sdk`
- 从特定路径导入：`@modelcontextprotocol/sdk/server/mcp.js`、`@modelcontextprotocol/sdk/server/stdio.js` 等
- 使用 `McpServer` 类进行高级服务器实现，具有自动协议处理
- 使用 `Server` 类进行低级控制，带有手动请求处理器
- 使用 **zod** 进行输入/输出模式验证：`npm install zod@3`
- 始终为工具、资源和提示提供 `title` 字段以获得更好的 UI 显示
- 使用 `registerTool()`、`registerResource()` 和 `registerPrompt()` 方法（推荐而非旧版 API）
- 使用 zod 定义模式：`{ inputSchema: { param: z.string() }, outputSchema: { result: z.string() } }`
- 从工具返回 `content`（用于显示）和 `structuredContent`（用于结构化数据）
- 对于 HTTP 服务器，使用带有 Express 或类似框架的 `StreamableHTTPServerTransport`
- 对于本地集成，使用 `StdioServerTransport` 进行基于 stdio 的通信
- 为每个请求创建新的传输实例以防止请求 ID 冲突（无状态模式）
- 使用带有 `sessionIdGenerator` 的会话管理进行有状态服务器
- 为本地服务器启用 DNS 重新绑定保护：`enableDnsRebindingProtection: true`
- 配置 CORS 标头并为基于浏览器的客户端暴露 `Mcp-Session-Id`
- 使用带有 URI 参数的 `ResourceTemplate` 进行动态资源：`new ResourceTemplate('resource://{param}', { list: undefined })`
- 使用来自 `@modelcontextprotocol/sdk/server/completable.js` 的 `completable()` 包装器支持补全以获得更好的用户体验
- 使用 `server.server.createMessage()` 实现采样，从客户端请求 LLM 补全
- 使用 `server.server.elicitInput()` 在工具执行期间请求额外的用户输入
- 为批量更新启用通知防抖：`debouncedNotificationMethods: ['notifications/tools/list_changed']`
- 动态更新：在注册项目上调用 `.enable()`、`.disable()`、`.update()` 或 `.remove()` 来发出 `listChanged` 通知
- 使用来自 `@modelcontextprotocol/sdk/shared/metadataUtils.js` 的 `getDisplayName()` 进行 UI 显示名称
- 使用 MCP Inspector 测试服务器：`npx @modelcontextprotocol/inspector`

## 最佳实践

- 保持工具实现专注于单一职责
- 为 LLM 理解提供清晰、描述性的标题和描述
- 为所有参数和返回值使用适当的 TypeScript 类型
- 使用 try-catch 块实现全面的错误处理
- 在工具结果中返回 `isError: true` 用于错误条件
- 对所有异步操作使用 async/await
- 正确关闭数据库连接并清理资源
- 在处理前验证输入参数
- 使用结构化日志记录进行调试，而不污染 stdout/stderr
- 在暴露文件系统或网络访问时考虑安全影响
- 在传输关闭事件上实现适当的资源清理
- 使用环境变量进行配置（端口、API 密钥等）
- 清楚地记录工具功能和限制
- 使用多个客户端测试以确保兼容性

## 常见模式

### 基本服务器设置（HTTP）
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

### 基本服务器设置（stdio）
```typescript
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new McpServer({
    name: 'my-server',
    version: '1.0.0'
});

// ... 注册工具、资源、提示 ...

const transport = new StdioServerTransport();
await server.connect(transport);
```

### 简单工具
```typescript
import { z } from 'zod';

server.registerTool(
    'calculate',
    {
        title: '计算器',
        description: '执行基本计算',
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
    new ResourceTemplate('users/{userId}', { list: undefined }),
    {
        title: '用户配置文件',
        description: '获取用户配置文件数据'
    },
    async (uri, { userId }) => ({
        contents: [{
            uri: uri.href,
            text: `用户 ${userId} 数据在这里`
        }]
    })
);
```

### 带采样的工具
```typescript
server.registerTool(
    'summarize',
    {
        title: '文本摘要器',
        description: '使用 LLM 摘要文本',
        inputSchema: { text: z.string() },
        outputSchema: { summary: z.string() }
    },
    async ({ text }) => {
        const response = await server.server.createMessage({
            messages: [{
                role: 'user',
                content: { type: 'text', text: `摘要：${text}` }
            }],
            maxTokens: 500
        });

        const summary = response.content.type === 'text' ?
            response.content.text : '无法摘要';
        const output = { summary };
        return {
            content: [{ type: 'text', text: JSON.stringify(output) }],
            structuredContent: output
        };
    }
);
```

### 带补全的提示
```typescript
import { completable } from '@modelcontextprotocol/sdk/server/completable.js';

server.registerPrompt(
    'review',
    {
        title: '代码审查',
        description: '以特定焦点审查代码',
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
                text: `审查这个 ${language} 代码：\n\n${code}`
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
        title: '风险操作',
        description: '可能失败的操作',
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
                content: [{ type: 'text', text: `错误：${error.message}` }],
                isError: true
            };
        }
    }
);
```