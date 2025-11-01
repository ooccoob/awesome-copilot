---
mode: 'agent'
description: '生成完整的Python MCP服务器项目，包含工具、资源和正确的配置'
---

# 生成Python MCP服务器

创建一个完整的模型上下文协议（MCP）Python服务器，具体要求如下：

## 要求

1. **项目结构**：使用uv创建具有正确结构的新Python项目
2. **依赖**：使用uv包含mcp[cli]包
3. **传输类型**：在stdio（本地）或streamable-http（远程）之间选择
4. **工具**：创建至少一个具有正确类型提示的有用工具
5. **错误处理**：包含全面的错误处理和验证

## 实现细节

### 项目设置
- 使用`uv init project-name`初始化
- 添加MCP SDK：`uv add "mcp[cli]"`
- 创建主服务器文件（例如`server.py`）
- 为Python项目添加`.gitignore`
- 配置直接执行，使用`if __name__ == "__main__"`

### 服务器配置
- 使用`mcp.server.fastmcp`中的`FastMCP`类
- 设置服务器名称和可选指令
- 选择传输：stdio（默认）或streamable-http
- 对于HTTP：可选地配置主机、端口和无状态模式

### 工具实现
- 在函数上使用`@mcp.tool()`装饰器
- 始终包含类型提示——它们自动生成模式
- 编写清晰的文档字符串——它们成为工具描述
- 使用Pydantic模型或TypedDicts进行结构化输出
- 支持I/O绑定任务的异步操作
- 包含正确的错误处理

### 资源/提示设置（可选）
- 使用`@mcp.resource()`装饰器添加资源
- 为动态资源使用URI模板：`"resource://{param}"`
- 使用`@mcp.prompt()`装饰器添加提示
- 从提示返回字符串或消息列表

### 代码质量
- 为所有函数参数和返回使用类型提示
- 为工具、资源和提示编写文档字符串
- 遵循PEP 8风格指南
- 对异步操作使用async/await
- 实现上下文管理器进行资源清理
- 为复杂逻辑添加内联注释

## 示例工具类型考虑
- 数据处理和转换
- 文件系统操作（读取、分析、搜索）
- 外部API集成
- 数据库查询
- 文本分析或生成（使用采样）
- 系统信息检索
- 数学或科学计算

## 配置选项

- **对于stdio服务器**：
  - 简单直接执行
  - 使用`uv run mcp dev server.py`测试
  - 安装到Claude：`uv run mcp install server.py`

- **对于HTTP服务器**：
  - 通过环境变量配置端口
  - 可扩展的无状态模式：`stateless_http=True`
  - JSON响应模式：`json_response=True`
  - 为浏览器客户端配置CORS
  - 挂载到现有ASGI服务器（Starlette/FastAPI）

## 测试指导
- 解释如何运行服务器：
  - stdio：`python server.py`或`uv run server.py`
  - HTTP：`python server.py`然后连接到`http://localhost:PORT/mcp`
- 使用MCP Inspector测试：`uv run mcp dev server.py`
- 安装到Claude Desktop：`uv run mcp install server.py`
- 包含示例工具调用
- 添加故障排除提示

## 需要考虑的附加功能
- 上下文使用，用于日志记录、进度和通知
- LLM采样，用于AI驱动的工具
- 用户输入引出，用于交互式工作流
- 共享资源的生命周期管理（数据库、连接）
- 使用Pydantic模型的结构化输出
- 用于UI显示的图标
- 使用Image类处理图像
- 更好用户体验的完成支持

## 最佳实践
- 到处使用类型提示——它们不是可选的
- 尽可能返回结构化数据
- 记录到stderr（或使用上下文日志记录）以避免stdout污染
- 正确清理资源
- 尽早验证输入
- 提供清晰的错误消息
- 在LLM集成之前独立测试工具

生成一个完整的、生产就绪的MCP服务器，具有类型安全、正确的错误处理和全面的文档。