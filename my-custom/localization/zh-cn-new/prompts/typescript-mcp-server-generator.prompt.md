---
mode: 'agent'
description: '生成完整的TypeScript MCP服务器项目，包含工具、资源和正确的配置'
---

# 生成TypeScript MCP服务器

创建一个完整的TypeScript模型上下文协议（MCP）服务器，具体要求如下：

## 要求

1. **项目结构**：创建具有正确目录结构的新TypeScript/Node.js项目
2. **NPM包**：包含@modelcontextprotocol/sdk、zod@3和express（用于HTTP）或stdio支持
3. **TypeScript配置**：带有ES模块支持的正确tsconfig.json
4. **服务器类型**：在HTTP（使用Streamable HTTP传输）或基于stdio的服务器之间选择
5. **工具**：创建至少一个具有正确模式验证的有用工具
6. **错误处理**：包含全面的错误处理和验证

## 实现细节

### 项目设置
- 使用`npm init`初始化并创建package.json
- 安装依赖：`@modelcontextprotocol/sdk`、`zod@3`和传输特定包
- 配置带有ES模块的TypeScript：在package.json中`"type": "module"`
- 添加开发依赖：`tsx`或`ts-node`用于开发
- 创建正确的.gitignore文件

### 服务器配置
- 使用`McpServer`类进行高级实现
- 设置服务器名称和版本
- 选择适当的传输（StreamableHTTPServerTransport或StdioServerTransport）
- 对于HTTP：设置带有正确中间件和错误处理的Express
- 对于stdio：直接使用StdioServerTransport

### 工具实现
- 使用`registerTool()`方法和描述性名称
- 使用zod定义输入和输出验证的模式
- 提供清晰的`title`和`description`字段
- 在结果中返回`content`和`structuredContent`
- 使用try-catch块实现正确的错误处理
- 在适当的地方支持异步操作

### 资源/提示设置（可选）
- 使用`registerResource()`添加资源，并为动态URI使用ResourceTemplate
- 使用参数模式使用`registerPrompt()`添加提示
- 考虑添加完成支持以获得更好的用户体验

### 代码质量
- 使用TypeScript实现类型安全
- 一致地遵循async/await模式
- 在传输关闭事件上实现正确的清理
- 使用环境变量进行配置
- 为复杂逻辑添加内联注释
- 使用清晰的关注点分离结构化代码

## 示例工具类型考虑
- 数据处理和转换
- 外部API集成
- 文件系统操作（读取、搜索、分析）
- 数据库查询
- 文本分析或摘要（使用采样）
- 系统信息检索

## 配置选项

- **对于HTTP服务器**：
  - 通过环境变量配置端口
  - 为浏览器客户端设置CORS
  - 会话管理（无状态vs有状态）
  - 为本地服务器提供DNS重绑定保护

- **对于stdio服务器**：
  - 正确的stdin/stdout处理
  - 基于环境的配置
  - 进程生命周期管理

## 测试指导
- 解释如何运行服务器（`npm start`或`npx tsx server.ts`）
- 提供MCP Inspector命令：`npx @modelcontextprotocol/inspector`
- 对于HTTP服务器，包含连接URL：`http://localhost:PORT/mcp`
- 包含示例工具调用
- 为常见问题添加故障排除提示

## 需要考虑的附加功能
- 为LLM驱动的工具提供采样支持
- 为交互式工作流提供用户输入引出
- 具有启用/禁用功能的动态工具注册
- 为批量更新提供通知防抖
- 为高效数据引用提供资源链接

生成一个完整的、生产就绪的MCP服务器，具有全面的文档、类型安全和错误处理。