## What / When / Why / How

- What: Semantic Kernel .NET 模式（创建/重构/解释 SK 代码）
- When: 构建 .NET AI 应用与 Agent，需跟随最新文档
- Why: SK 迭代快，需以官方文档/示例为准
- How: 必查 Docs/Samples→按插件/函数调用模式实现→记录与测试

## Key Points

- 工具：microsoft.docs.mcp；官方 repo 与 samples
- 模式：async/await；插件化；错误处理与日志
- 认证：DefaultAzureCredential 优先；Azure AI Foundry 优先
- 记忆/上下文：内置能力；保持最新包版本

## Compact Map

- 查阅→实现/重构→测试→对齐样例→记录

## Example Questions (10+)

- 目标使用场景对应哪类 SK 模式？
- 依赖与包版本如何选择？
- 插件/函数的注册与调用示例？
- 上下文/记忆如何管理？
- 错误处理与日志策略？
- Azure 服务集成与鉴权？
- 单测与端到端示例？
- 与现有代码的迁移路径？
- 性能/并发考虑？
- 文档引用与更新频率？

---
Source: d:\mycode\awesome-copilot\chatmodes\semantic-kernel-dotnet.chatmode.md
Generated: {{timestamp}}
