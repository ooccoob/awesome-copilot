## What
- 生成基于官方 MCP Java SDK 的完整服务器工程（Maven/Gradle），含 Reactive Streams、工具/资源/提示处理器与测试。

## When
- 需要 Java 生态可运行、带日志与测试的 MCP 服务脚手架时。

## Why
- 标准化结构与能力，便于接入与持续集成。

## How
- 结构：pom/gradle + src/main(java/resources) + test
- 能力：工具/资源/提示定义与处理器；Stdio 传输
- 异步：Reactor；优雅停机；SLF4J 日志
- 测试：同步封装测试调用；异常分支覆盖

## Key points (CN)
- 明确 capabilities（tools/resources/prompts）
- 工具参数校验与错误响应
- Shade/应用入口与配置

## Key points (EN)
- Reactive handlers; stdio transport
- Validation + error responses
- Tests for tools and edge cases

## Example questions
- “生成 greet/calculate 工具与对应测试？”
- “如何在 README 中说明在 Claude Desktop 集成？”

## 思维导图（要点）
- 结构/依赖
- 工具/资源/提示
- 异步/日志/停机
- 测试/打包/运行

—
- Source: d:\mycode\awesome-copilot\prompts\java-mcp-server-generator.prompt.md
- Generated: 2025-10-17
