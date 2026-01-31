---
代理人：“代理人”
描述：“使用工具、资源和正确的配置在 TypeScript 中生成完整的 MCP 服务器项目”
---

# 生成 TypeScript MCP 服务器

使用 TypeScript 创建一个完整的模型上下文协议 (MCP) 服务器，其规范如下：

## 要求

1. **项目结构**：创建一个具有正确目录结构的新 TypeScript/Node.js 项目
2. **NPM 包**：包括 @modelcontextprotocol/sdk、zod@3 以及 Express（用于 HTTP）或 stdio 支持
3. **TypeScript 配置**：具有 ES 模块支持的正确 tsconfig.json
4. **服务器类型**：选择 HTTP（使用 Streamable HTTP 传输）或基于 stdio 的服务器
5. **工具**：创建至少一种具有适当架构验证的有用工具
6. **错误处理**：包括全面的错误处理和验证

## 实施细节

### 项目设置
- 使用 `npm init` 初始化并创建 package.json
- 安装依赖项：`@modelcontextprotocol/sdk`、`zod@3` 和特定于传输的包
- 使用 ES 模块配置 TypeScript：package.json 中的 `"type": "module"`
- 添加开发依赖项：`tsx` 或 `ts-node` 进行开发
- 创建正确的 .gitignore 文件

### 服务器配置
- 使用 `McpServer` 类进行高级实现
- 设置服务器名称和版本
- 选择适当的传输（StreamableHTTPServerTransport 或 StdioServerTransport）
- 对于 HTTP：使用适当的中间件和错误处理设置 Express
- 对于stdio：直接使用StdioServerTransport

### 工具实施
- 使用具有描述性名称的 `registerTool()` 方法
- 使用 zod 定义模式进行输入和输出验证
- 提供明确的 `title` 和 `description` 字段
- 在结果中同时返回 `content` 和 `structuredContent`
- 使用 try-catch 块实现正确的错误处理
- 在适当的情况下支持异步操作

### 资源/提示设置（可选）
- 使用 `registerResource()` 和 ResourceTemplate 添加资源以获取动态 URI
- 使用带有参数模式的 `registerPrompt()` 添加提示
- 考虑添加完成支持以获得更好的用户体验

### 代码质量
- 使用 TypeScript 实现类型安全
- 始终遵循异步/等待模式
- 对传输关闭事件进行适当的清理
- 使用环境变量进行配置
- 为复杂逻辑添加内嵌注释
- 具有清晰的关注点分离的结构代码

## 要考虑的示例工具类型
- 数据处理和转换
- 外部API集成
- 文件系统操作（读取、搜索、分析）
- 数据库查询
- 文本分析或总结（带采样）
- 系统信息检索

## 配置选项
- **对于 HTTP 服务器**： 
  - 通过环境变量进行端口配置
  - 浏览器客户端的 CORS 设置
  - 会话管理（无状态与有状态）
  - 本地服务器的 DNS 重新绑定保护
  
- **对于 stdio 服务器**：
  - 正确的标准输入/标准输出处理
  - 基于环境的配置
  - 流程生命周期管理

## 测试指导
- 解释如何运行服务器（`npm start` 或 `npx tsx server.ts`）
- 提供 MCP Inspector 命令：`npx @modelcontextprotocol/inspector`
- 对于 HTTP 服务器，请包含连接 URL：`http://localhost:PORT/mcp`
- 包括示例工具调用
- 添加常见问题的故障排除提示

## 需要考虑的其他功能
- 对 LLM 支持的工具的采样支持
- 交互式工作流程的用户输入诱导
- 具有启用/禁用功能的动态工具注册
- 批量更新的通知去抖
- 高效数据引用的资源链接

生成一个完整的、可用于生产的 MCP 服务器，具有全面的文档、类型安全和错误处理功能。
