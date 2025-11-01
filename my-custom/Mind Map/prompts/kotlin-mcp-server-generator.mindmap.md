## What
- 生成一个基于 Kotlin 的 MCP 服务器项目骨架（Gradle/Ktor/Kotlin SDK），含工具注册、传输、配置、测试与文档。

## When to use
- 需要快速搭建可扩展的 Kotlin MCP 服务，供 IDE/代理工具通过 JSON-RPC 或 stdio/SSE 连接调用。

## Why it matters
- 统一模板可减少脚手架时间；内置类型安全与错误处理，降低接入成本并提升稳定性与可测试性。

## How (关键流程)
- 项目结构：Gradle KTS + src/main/kotlin + tools/ + config/
- 依赖：io.modelcontextprotocol:kotlin-sdk、Ktor、kotlinx-serialization、coroutines、logging
- 启动：Main.kt 使用 StdioServerTransport（或扩展 SSE/Ktor）
- 能力：ServerCapabilities 声明 tools/resources/prompts；tools 以 JSON Schema 定义输入输出
- 工具注册：tools/ToolRegistry.registerTools() 聚合注册
- 配置：data class Config + env 读取
- 测试：kotlin.test + kotlinx-coroutines-test

## Example questions (≥10)
1. 请生成含 Stdio 与 SSE 的双传输 Kotlin MCP 服务模板，并解释如何在 Ktor 中挂载 /mcp。
2. 为工具 tool1 定义输入 JSON Schema（必填 string param1、可选 int param2）并实现参数校验与结果封装。
3. 如何在 ServerOptions 中启用 resources.listChanged 与 prompts.listChanged？示例代码给我。
4. 给出使用 kotlin-logging + logback 的最小日志配置与示例日志调用。
5. 增加一个返回结构化 JSON 的工具，并提供单元测试（含协程测试器）。
6. 如何把环境变量（SERVER_NAME、VERSION）注入到 Config 并在 Main.kt 打印启动横幅？
7. 演示在工具内部抛出业务异常并转换为 MCP 友好错误响应的做法。
8. 提供多模块化结构建议：server、tools、resources 子包如何解耦与依赖。
9. 生成 GitHub Actions 构建发布 workflow，发布 fatJar，并在 README 中添加使用说明。
10. 给出“开发/生产”两种日志级别与 JVM 参数示例，如何通过 Gradle 参数切换环境。

## Key points (要点)
- CN: 类型安全、协程、JSON Schema、工具注册统一、传输可扩展、日志与测试内置
- EN: Type-safe tools, coroutines, JSON schemas, unified tool registry, extensible transports, logging/tests baked-in

## Mind map (简要)
- 目标: Kotlin MCP Server
  - 架构: Gradle/Ktor/SDK
  - 传输: stdio | SSE
  - 能力: tools/resources/prompts
  - 工具: JSON Schema + 校验
  - 配置: data class + env
  - 测试: coroutines-test
  - 文档/CI: README + Actions

---
Source file: d:\mycode\awesome-copilot\prompts\kotlin-mcp-server-generator.prompt.md
Generated: 2025-10-17T00:00:00Z
