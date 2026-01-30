---
mode: 'agent'
description: '生成一个完整的C# MCP服务器项目，包含工具、提示和正确的配置'
---

# 生成 C# MCP 服务器

创建一个完整的模型上下文协议（MCP）C# 服务器，具体要求如下：

## 要求

1. **项目结构**：创建一个具有正确目录结构的新C#控制台应用程序
2. **NuGet包**：包含ModelContextProtocol（预发布版）和Microsoft.Extensions.Hosting
3. **日志配置**：将所有日志配置到stderr，避免干扰stdio传输
4. **服务器设置**：使用Host构建器模式和正确的DI配置
5. **工具**：创建至少一个具有正确属性和描述的有用工具
6. **错误处理**：包含正确的错误处理和验证

## 实现细节

### 基本项目设置
- 使用.NET 8.0或更高版本
- 创建控制台应用程序
- 使用--prerelease标志添加必要的NuGet包
- 将日志配置到stderr

### 服务器配置
- 使用`Host.CreateApplicationBuilder`进行DI和生命周期管理
- 配置`AddMcpServer()`使用stdio传输
- 使用`WithToolsFromAssembly()`进行自动工具发现
- 确保服务器使用`RunAsync()`运行

### 工具实现
- 在工具类上使用`[McpServerToolType]`属性
- 在工具方法上使用`[McpServerTool]`属性
- 为工具和参数添加`[Description]`属性
- 在适当的地方支持异步操作
- 包含正确的参数验证

### 代码质量
- 遵循C#命名约定
- 包含XML文档注释
- 使用可空引用类型
- 使用McpProtocolException实现正确的错误处理
- 使用结构化日志进行调试

## 示例工具类型考虑
- 文件操作（读取、写入、搜索）
- 数据处理（转换、验证、分析）
- 外部API集成（HTTP请求）
- 系统操作（执行命令、检查状态）
- 数据库操作（查询、更新）

## 测试指导
- 解释如何运行服务器
- 提供使用MCP客户端测试的示例命令
- 包含故障排除提示

生成一个完整的、生产就绪的MCP服务器，包含全面的文档和错误处理。