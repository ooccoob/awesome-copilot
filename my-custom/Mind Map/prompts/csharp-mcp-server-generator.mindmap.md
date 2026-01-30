## 文档综述（What/When/Why/How）

- What：生成 C# MCP Server 的完整项目（.NET 8+、工具/日志/DI/错误处理）

- When：需要以标准结构快速创建可运行的 MCP 服务并内置至少一个工具时

- Why：统一项目结构、依赖与质控，便于客户端对接与调试

- How：控制台项目 + 预发布包 + Host/DI + AddMcpServer(stdio) + WithToolsFromAssembly + 结构化日志(stderr) + 异常处理

## 示例提问（Examples）

- “创建含文件工具的 MCP Server，所有日志到 stderr，使用可空引用与 XML 注释”

- “给出运行与客户端测试示例及常见排障”

## 结构化要点（CN/EN）

- 依赖/Packages：ModelContextProtocol(pre) + Hosting

- 启动/Host：HostBuilder + DI + RunAsync

- 工具/Tools：特性标注 + 参数校验 + 异步

- 质量/Quality：命名/注释/错误/日志

## 中文思维导图

- 项目结构
  - 控制台 + 目录
- 依赖配置
  - NuGet 预发布
- 服务器搭建
  - stdio 传输
- 工具实现
  - 描述/参数/校验
- 测试文档
  - 运行/调试

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\csharp-mcp-server-generator.prompt.md

- 生成时间：2025-10-17
