---
agent: 'agent'
description: 'Generate a complete MCP server project in C# with tools, prompts, and proper configuration'
---

# 生成 C# MCP 服务器

使用 C# 创建一个完整的模型上下文协议 (MCP) 服务器，其规范如下：

## 要求

1. **项目结构**：创建一个具有正确目录结构的新 C# 控制台应用程序
2. **NuGet 包**：包括 ModelContextProtocol（预发行版）和 Microsoft.Extensions.Hosting
3. **日志配置**：将所有日志配置到 stderr 以避免干扰 stdio 传输
4. **服务器设置**：使用具有正确 DI 配置的主机构建器模式
5. **工具**：创建至少一种具有适当属性和描述的有用工具
6. **错误处理**：包括正确的错误处理和验证

## 实施细节

### 基本项目设置
- 使用.NET 8.0或更高版本
- 创建控制台应用程序
- 使用 --prerelease 标志添加必要的 NuGet 包
- 配置日志记录到 stderr

### 服务器配置
- 使用 `Host.CreateApplicationBuilder` 进行 DI 和生命周期管理
- 使用 stdio 传输配置 `AddMcpServer()`
- 使用 `WithToolsFromAssembly()` 进行自动工具发现
- 确保服务器以 `RunAsync()` 运行

### 工具实施
- 在工具类上使用 `[McpServerToolType]` 属性
- 在工具方法上使用 `[McpServerTool]` 属性
- 将 `[Description]` 属性添加到工具和参数
- 在适当的情况下支持异步操作
- 包括适当的参数验证

### 代码质量
- 遵循 C# 命名约定
- 包含 XML 文档注释
- 使用可为空的引用类型
- 使用 McpProtocolException 实施正确的错误处理
- 使用结构化日志记录进行调试

## 要考虑的示例工具类型
- 文件操作（读、写、搜索）
- 数据处理（转换、验证、分析）
- 外部 API 集成（HTTP 请求）
- 系统操作（执行命令、检查状态）
- 数据库操作（查询、更新）

## 测试指导
- 解释如何运行服务器
- 提供示例命令以使用 MCP 客户端进行测试
- 包括故障排除提示

生成一个完整的、可用于生产的 MCP 服务器，具有全面的文档和错误处理功能。
