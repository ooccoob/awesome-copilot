## What / When / Why / How

- What: Semantic Kernel Python 模式（创建/重构/解释基于 SK 的 Python 代码）
- When: 需要用 Python 版本 SK 构建 AI 应用/Agent
- Why: SK 迭代快，必须对齐官方文档与示例最佳实践
- How: 必查 Docs/Repo/Samples→遵循插件/函数调用模式→异步优先→记录与测试

## Key Points

- 官方资源：Docs、Python repo 与 samples；优先 Azure AI Foundry 集成
- 模式：async 优先；插件化（functions/plugins）与调用约定
- 认证：DefaultAzureCredential 优先；日志与错误处理规范
- 记忆/上下文：SK 内置记忆与上下文管理
- 工具：microsoft.docs.mcp 获取最新教程与示例

## Compact Map

- 查阅→实现/重构→测试→对齐样例→文档化

## Example Questions (10+)

- 目标场景对应哪种 SK Python 模式（Planner/Orchestration/Agent）？
- 依赖与包版本如何锁定并保持兼容？
- 插件/函数的注册、发现与调用流程示例？
- 上下文与记忆如何持久化与隔离？
- 错误处理与日志策略的推荐做法？
- Azure 服务对接与凭据管理？
- 单测/集成测试如何组织？
- 与既有代码的迁移路径与兼容策略？
- 性能与并发注意事项？
- 文档引用与示例更新节奏？

---
Source: d:\mycode\awesome-copilot\chatmodes\semantic-kernel-python.chatmode.md
Generated: {{timestamp}}
