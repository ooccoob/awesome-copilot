---
适用于：'*'
描述：“具有 HTTP SSE 传输开发标准和说明的 Quarkus 和 MCP 服务器”
---
# Quarkus MCP 服务器

使用 Java 21、Quarkus 和 HTTP SSE 传输构建 MCP 服务器。

## 堆栈

- Java 21 与 Quarkus 框架
- MCP 服务器扩展：`mcp-server-sse`
- 用于依赖注入的 CDI
- MCP 端点：`http://localhost:8080/mcp/sse`

## 快速入门

```bash
quarkus create app --no-code -x rest-client-jackson,qute,mcp-server-sse your-domain-mcp-server
```

## 结构

- 使用标准 Java 命名约定（PascalCase 类、camelCase 方法）
- 组织在包中：`model`、`repository`、`service`、`mcp`
- 将记录类型用于不可变数据模型
- 不可变数据的状态管理必须由存储库层管理
- 为公共方法添加 Javadoc

## MCP 工具

- 必须是 `@ApplicationScoped` CDI beans 中的公共方法
- 使用 `@Tool(name="tool_name", description="clear description")`
- 从不返回 `null` - 而是返回错误消息
- 始终验证参数并优雅地处理错误

## 建筑

- 单独关注点：MCP 工具 → 服务层 → 存储库
- 使用 `@Inject` 进行依赖注入
- 使数据操作线程安全
- 使用 `Optional<T>` 避免空指针异常

## 常见问题

- 不要将业务逻辑放在 MCP 工具中（使用服务层）
- 不要从工具中抛出异常（返回错误字符串）
- 不要忘记验证输入参数
- 使用边缘情况进行测试（空、空输入）
