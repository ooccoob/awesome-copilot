## What / When / Why / How
- What: 使用 TypeScript（Node 20）开发 Azure Functions 的规范（@azure/functions v4）。
- When: 生成/修改函数端点、I/O 绑定、依赖与 API 文档时。
- Why: 现代异步、最小依赖、可维护与一致命名。
- How: async/await；优先 node:* 内置模块（fs/promises 等）；按资源-动词命名；OpenAPI/README 同步。

## Key points
- 代码：ESM/TS 现代写法；类型完善；顶层 await 避免；始终非阻塞 I/O。
- 目录：每个端点单文件：src/functions/<resource>-<verb>.ts。
- 运行时：@azure/functions@4；掌握 Context、Request/Response、触发器与绑定（HTTP/Timer/Queue 等）。
- 依赖：新增第三方包需先征询；优先内置 Node 20 模块。
- 文档：更新 OpenAPI schema 与 README；守一致性与示例。
- 错误：集中处理与统一响应格式；日志结构化；冷启动考虑。
- 测试：本地/集成测试；模拟触发器与绑定；环境变量隔离。

## Compact map
- 命名: resource-verb
- I/O: async fs/promises
- 运行: v4 触发器/绑定
- 文档: OpenAPI/README
- 依赖: 内置优先

## Example questions (10+)
- 如何为 HTTP 触发器定义强类型请求/响应模型？
- 绑定（Queue/Blob）在 TS 下的类型与错误处理策略？
- 何时需要中间层（服务/仓储）而不把逻辑塞进函数？
- Node 20 原生特性替代哪些常见第三方包？
- OpenAPI 如何与函数描述自动/半自动同步？
- 函数冷启动与连接池最佳实践？
- 本地调试时如何注入环境变量与隔离机密？
- 统一错误响应与日志相关 ID 的实现方式？
- 端点命名冲突与重构策略？
- 并发与重试配置对幂等性的影响？

—
Source: d:\mycode\awesome-copilot\instructions\azure-functions-typescript.instructions.md | Generated: {{timestamp}}
