---
applyTo: "quarkus-mcp-server-sse.instructions.md"
---

<!-- 本文件为自动翻译，供参考。请结合实际需求进行校对和完善。-->

# Quarkus MCP Server（SSE）开发规范

## 技术栈

- Java 21 + Quarkus 框架
- MCP Server 扩展：`mcp-server-sse`
- CDI 依赖注入
- MCP 端点：`http://localhost:8080/mcp/sse`

## 快速开始

```bash
quarkus create app --no-code -x rest-client-jackson,qute,mcp-server-sse your-domain-mcp-server
```

## 结构规范

- Java 命名规范（类 PascalCase，方法 camelCase）
- 包结构：`model`、`repository`、`service`、`mcp`
- 不变数据模型用 Record 类型
- 状态管理由 repository 层负责
- 公共方法需加 Javadoc

## MCP 工具开发

- 必须为 `@ApplicationScoped` CDI bean 的 public 方法
- 用 `@Tool(name, description)` 注解
- 禁止返回 null，出错时返回错误信息
- 必须校验参数，优雅处理异常

## 架构建议

- 关注分层：MCP 工具 → Service 层 → Repository
- 用 `@Inject` 注入依赖
- 数据操作需线程安全
- 用 Optional<T> 避免空指针

## 常见问题

- 业务逻辑不要写在 MCP 工具，放在 service 层
- 工具方法禁止抛异常，返回错误字符串
- 必须校验所有输入参数
- 测试需覆盖边界情况（null、空等）

---

免责声明：本翻译仅供参考，具体实践请结合实际项目需求和最新官方文档。
