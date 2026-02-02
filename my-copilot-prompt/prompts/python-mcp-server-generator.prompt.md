---
agent: 'agent'
description: 'Generate a complete MCP server project in Python with tools, resources, and proper configuration'
---

# 生成Python MCP服务器

使用 Python 创建一个完整的模型上下文协议 (MCP) 服务器，其规范如下：

## 要求

1. **项目结构**：使用 uv 创建一个具有正确结构的新 Python 项目
2. **依赖项**：包含带有 uv 的 mcp[cli] 包
3. **传输类型**：选择 stdio（用于本地）或 Streamable-http（用于远程）
4. **工具**：创建至少一种具有正确类型提示的有用工具
5. **错误处理**：包括全面的错误处理和验证

## 实施细节

### 项目设置
- 使用 `uv init project-name` 初始化
- 添加MCP SDK：`uv add "mcp[cli]"`
- 创建主服务器文件（例如 `server.py`）
- 为 Python 项目添加 `.gitignore`
- 使用 `if __name__ == "__main__"` 配置直接执行

### 服务器配置
- 使用 `mcp.server.fastmcp` 中的 `FastMCP` 类
- 设置服务器名称和可选说明
- 选择传输：stdio（默认）或streamable-http
- 对于 HTTP：可选择配置主机、端口和无状态模式

### 工具实施
- 在函数上使用 `@mcp.tool()` 装饰器
- 始终包含类型提示 - 它们自动生成模式
- 编写清晰的文档字符串 - 它们成为工具描述
- 使用 Pydantic 模型或 TypedDicts 进行结构化输出
- 支持 I/O 密集型任务的异步操作
- 包括正确的错误处理

### 资源/提示设置（可选）
- 使用 `@mcp.resource()` 装饰器添加资源
- 使用动态资源的 URI 模板：`"resource://{param}"`
- 使用 `@mcp.prompt()` 装饰器添加提示
- 从提示中返回字符串或消息列表

### 代码质量
- 对所有函数参数和返回值使用类型提示
- 编写工具、资源和提示的文档字符串
- 遵循 PEP 8 风格指南
- 使用 async/await 进行异步操作
- 实施上下文管理器以进行资源清理
- 为复杂逻辑添加内嵌注释

## 要考虑的示例工具类型
- 数据处理和转换
- 文件系统操作（读取、分析、搜索）
- 外部API集成
- 数据库查询
- 文本分析或生成（带采样）
- 系统信息检索
- 数学或科学计算

## 配置选项
- **对于 stdio 服务器**：
  - 简单直接执行
  - 使用 `uv run mcp dev server.py` 进行测试
  - 安装到克劳德：`uv run mcp install server.py`
  
- **对于 HTTP 服务器**：
  - 通过环境变量进行端口配置
  - 用于可扩展性的无状态模式：`stateless_http=True`
  - JSON响应模式：`json_response=True`
  - 浏览器客户端的 CORS 配置
  - 安装到现有的 ASGI 服务器 (Starlette/FastAPI)

## 测试指导
- 解释一下如何运行服务器：
  - 标准输入输出：`python server.py` 或 `uv run server.py`
  - HTTP：`python server.py` 然后连接到 `http://localhost:PORT/mcp`
- 使用 MCP Inspector 进行测试：`uv run mcp dev server.py`
- 安装到 Claude 桌面：`uv run mcp install server.py`
- 包括示例工具调用
- 添加故障排除提示

## 需要考虑的其他功能
- 日志记录、进度和通知的上下文使用
- AI 驱动工具的 LLM 采样
- 交互式工作流程的用户输入诱导
- 共享资源（数据库、连接）的生命周期管理
- 使用 Pydantic 模型进行结构化输出
- UI显示的图标
- 使用 Image 类处理图像
- 完成支持以获得更好的用户体验

## 最佳实践
- 到处使用类型提示 - 它们不是可选的
- 尽可能返回结构化数据
- 记录到 stderr（或使用上下文日志记录）以避免 stdout 污染
- 正确清理资源
- 尽早验证输入
- 提供清晰的错误消息
- 在 LLM 集成之前独立测试工具

生成一个完整的、可用于生产的 MCP 服务器，具有类型安全、正确的错误处理和全面的文档。
