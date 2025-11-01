## What
- 目标：使用官方 Swift MCP SDK 生成含工具/资源/提示与测试的完整 MCP 服务器工程。
- 产物：Package.swift、Sources/**（Server/Tools/Resources/Prompts）、Tests/**、README。

## When
- 需要在 Apple 生态或跨端环境提供 MCP 能力时。
- 期望用 Swift 并发、结构化日志、优雅停机与可测试性。

## Why
- 原生并发/Actor 易于写出稳健高性能服务。
- 规范工程骨架降低运维与集成成本（Claude Desktop/Inspector）。

## How
- Server.capabilities: prompts/resources/tools listChanged/subscribe。
- 工具：ListTools/CallTool（greet/calculate 示例）。
- 资源：List/Read/Subscribe/Unsubscribe；Actor 保存订阅状态。
- 提示：ListPrompts/GetPrompt（code-review 示例）。
- ServiceLifecycle 统一运行与优雅关停；swift-log 统一日志级别。

## Key Points
- SDK: modelcontextprotocol/swift-sdk；日志：swift-log；生命周期：swift-service-lifecycle。
- 线程安全：Actor 状态；错误处理：MCPError。
- 测试覆盖工具处理分支与异常（除零等）。

## Compact Map
- Project
  - Package.swift 依赖/平台
  - Sources/* 分层
  - Tests/* 覆盖
- Server
  - 注册工具/资源/提示
  - 传输：StdioTransport
- Ops
  - 日志/关停/配置

## Example Questions (10+)
- 如何把传输从 stdio 换成自定义 Socket/HTTP？
- 想增加异步外部 API 工具，如何编写 zod/Schema 等价校验？
- 多资源订阅广播如何做去抖与批量推送？
- 工具返回 structuredContent 的推荐结构是什么？
- 如何为工具执行链路增加请求 ID 与指标？
- 资源内容较大时的分页/分片策略如何设计？
- 如何将日志等级通过环境变量配置并在运行期热更新？
- 单测如何模拟 CallTool.Params 复杂入参与错误分支？
- 如何封装通用错误映射为 MCPError 并带上下文？
- 如何为 prompts 增加多语言与动态参数？
- 在 CI 中如何执行 swift test 并输出 JUnit 报告？

---
Source: d:\mycode\awesome-copilot\prompts\swift-mcp-server-generator.prompt.md
Generated: 2025-10-17T00:00:00Z
