---
description: '使用 Python SDK 构建模型上下文协议 (MCP) 服务器的指令'
applyTo: '**/*.py, **/pyproject.toml, **/requirements.txt'
---

# Python MCP 服务器开发

## 指令

- 使用 **uv** 进行项目管理：`uv init mcp-server-demo` 和 `uv add "mcp[cli]"`
- 从 `mcp.server.fastmcp` 导入 FastMCP：`from mcp.server.fastmcp import FastMCP`
- 使用 `@mcp.tool()`、`@mcp.resource()` 和 `@mcp.prompt()` 装饰器进行注册
- 类型提示是必需的 - 它们用于模式生成和验证
- 对结构化输出使用 Pydantic 模型、TypedDicts 或数据类
- 当返回类型兼容时，工具自动返回结构化输出
- 对于 stdio 传输，使用 `mcp.run()` 或 `mcp.run(transport="stdio")`
- 对于 HTTP 服务器，使用 `mcp.run(transport="streamable-http")` 或挂载到 Starlette/FastAPI
- 在工具/资源中使用 `Context` 参数访问 MCP 功能：`ctx: Context`
- 使用 `await ctx.debug()`、`await ctx.info()`、`await ctx.warning()`、`await ctx.error()` 发送日志
- 使用 `await ctx.report_progress(progress, total, message)` 报告进度
- 使用 `await ctx.elicit(message, schema)` 请求用户输入
- 使用 `await ctx.session.create_message(messages, max_tokens)` 进行 LLM 采样
- 使用 `Icon(src="path", mimeType="image/png")` 为服务器、工具、资源、提示配置图标
- 使用 `Image` 类进行自动图像处理：`return Image(data=bytes, format="png")`
- 使用 URI 模式定义资源模板：`@mcp.resource("greeting://{name}")`
- 通过接受部分值并返回建议来实现完成支持
- 对启动/关闭使用共享资源的生命周期上下文管理器
- 通过 `ctx.request_context.lifespan_context` 在工具中访问生命周期上下文
- 对于无状态 HTTP 服务器，在 FastMCP 初始化中设置 `stateless_http=True`
- 为现代客户端启用 JSON 响应：`json_response=True`
- 使用以下方式测试服务器：`uv run mcp dev server.py`（Inspector）或 `uv run mcp install server.py`（Claude Desktop）
- 在 Starlette 中使用不同路径挂载多个服务器：`Mount("/path", mcp.streamable_http_app())`
- 为浏览器客户端配置 CORS：暴露 `Mcp-Session-Id` 标头
- 当 FastMCP 不足时，使用低级 Server 类以获得最大控制

## 最佳实践

- 始终使用类型提示 - 它们驱动模式生成和验证
- 返回 Pydantic 模型或 TypedDicts 以获得结构化工具输出
- 保持工具函数专注于单一职责
- 提供清晰的文档字符串 - 它们成为工具描述
- 使用带有类型提示的描述性参数名称
- 使用 Pydantic Field 描述验证输入
- 使用 try-except 块实施适当的错误处理
- 对 I/O 绑定操作使用异步函数
- 在生命周期上下文管理器中清理资源
- 记录到 stderr 以避免干扰 stdio 传输（使用 stdio 时）
- 对配置使用环境变量
- 在 LLM 集成之前独立测试工具
- 在暴露文件系统或网络访问时考虑安全性
- 对机器可读数据使用结构化输出
- 为向后兼容性提供内容和结构化数据

## 常见模式

### 基本服务器设置（stdio）
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool()
def calculate(a: int, b: int, op: str) -> int:
    """执行计算"""
    if op == "add":
        return a + b
    return a - b

if __name__ == "__main__":
    mcp.run()  # 默认 stdio
```

### HTTP 服务器
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My HTTP Server")

@mcp.tool()
def hello(name: str = "World") -> str:
    """问候某人"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

### 带结构化输出的工具
```python
from pydantic import BaseModel, Field

class WeatherData(BaseModel):
    temperature: float = Field(description="摄氏温度")
    condition: str
    humidity: float

@mcp.tool()
def get_weather(city: str) -> WeatherData:
    """获取城市天气"""
    return WeatherData(
        temperature=22.5,
        condition="sunny",
        humidity=65.0
    )
```

### 动态资源
```python
@mcp.resource("users://{user_id}")
def get_user(user_id: str) -> str:
    """获取用户配置文件数据"""
    return f"User {user_id} profile data"
```

### 带上下文的工具
```python
from mcp.server.fastmcp import Context
from mcp.server.session import ServerSession

@mcp.tool()
async def process_data(
    data: str,
    ctx: Context[ServerSession, None]
) -> str:
    """处理数据并记录日志"""
    await ctx.info(f"Processing: {data}")
    await ctx.report_progress(0.5, 1.0, "Halfway done")
    return f"Processed: {data}"
```

### 带采样的工具
```python
from mcp.server.fastmcp import Context
from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

@mcp.tool()
async def summarize(
    text: str,
    ctx: Context[ServerSession, None]
) -> str:
    """使用 LLM 总结文本"""
    result = await ctx.session.create_message(
        messages=[SamplingMessage(
            role="user",
            content=TextContent(type="text", text=f"Summarize: {text}")
        )],
        max_tokens=100
    )
    return result.content.text if result.content.type == "text" else ""
```

### 生命周期管理
```python
from contextlib import asynccontextmanager
from dataclasses import dataclass
from mcp.server.fastmcp import FastMCP, Context

@dataclass
class AppContext:
    db: Database

@asynccontextmanager
async def app_lifespan(server: FastMCP):
    db = await Database.connect()
    try:
        yield AppContext(db=db)
    finally:
        await db.disconnect()

mcp = FastMCP("My App", lifespan=app_lifespan)

@mcp.tool()
def query(sql: str, ctx: Context) -> str:
    """查询数据库"""
    db = ctx.request_context.lifespan_context.db
    return db.execute(sql)
```

### 带消息的提示
```python
from mcp.server.fastmcp.prompts import base

@mcp.prompt(title="Code Review")
def review_code(code: str) -> list[base.Message]:
    """创建代码审查提示"""
    return [
        base.UserMessage("Review this code:"),
        base.UserMessage(code),
        base.AssistantMessage("I'll review the code for you.")
    ]
```

### 错误处理
```python
@mcp.tool()
async def risky_operation(input: str) -> str:
    """可能失败的操作"""
    try:
        result = await perform_operation(input)
        return f"Success: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
```