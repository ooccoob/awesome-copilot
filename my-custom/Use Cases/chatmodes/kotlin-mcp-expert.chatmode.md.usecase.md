---
post_title: "kotlin-mcp-expert.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "kotlin-mcp-expert-chatmode-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: ["use-cases","chatmode"]
tags: ["use-cases","kotlin","mcp","server"]
ai_note: "Generated with AI assistance from chatmodes/kotlin-mcp-expert.chatmode.md"
summary: "Use cases for building Kotlin MCP servers: idiomatic Kotlin patterns, coroutines, Ktor transports, serialization, and testing." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- Expert guidance for building Model Context Protocol (MCP) servers in Kotlin: coroutine patterns, Ktor transports, kotlinx.serialization, and multiplatform considerations.

## When

- When Kotlin teams need runnable examples, coroutine-based tool handlers, or guidance on multiplatform & Ktor integration for MCP servers.

## Why

- To produce idiomatic, type-safe, and testable MCP servers using Kotlin features while ensuring interoperability with MCP tooling.

## How

- Use the official Kotlin SDK and prefer suspending handlers for tool/resource implementations.
- Use Ktor for HTTP/SSE transports and kotlinx.serialization for schema and payload handling.
- Favor structured concurrency and runTest for coroutine-based testing.

## Key points (英文+中文对照)

- Idiomatic Kotlin with coroutines（使用协程的惯用 Kotlin 编码风格）
- Ktor transports and multiplatform considerations（Ktor 传输与多平台兼容性考虑）
- kotlinx.serialization-based schemas（基于 kotlinx.serialization 的 schema 与序列化）

## 使用场景

### 1. 使用协程实现工具处理

- 用户故事：作为 Kotlin 开发者，我希望使用 suspending handler 实现工具逻辑并保持高并发性能。
- 例 1："[定义工具] 请提供使用 suspending 函数的工具注册示例和参数校验样例。"
- 例 2："[并发处理] 请示例化如何使用 coroutineScope/async 并行处理多个子请求。"
- 例 3："[阻塞调用] 请说明在协程中调用阻塞 IO 时如何切换到适当的调度器。"
- 例 4："[错误处理] 请提供协程内异常传播与 fallback 策略示例。"
- 例 5："[测试] 请给出 runTest 下的工具单元测试示例。"

### 2. Ktor Transport 集成

- 用户故事：作为后端工程师，我需要在 Ktor 上暴露 MCP 的 HTTP/SSE 传输并保证请求路由正确。
- 例 1："[配置] 请生成 Ktor module 的示例，用于注册 MCP HTTP transport。"
- 例 2："[SSE] 请示例化如何在 Ktor 中实现 SSE 推送给订阅客户端。"
- 例 3："[安全] 请建议在 Ktor 层面的基本鉴权与速率限制策略。"
- 例 4："[部署] 请给出 Ktor + Docker 的部署示例与健康检查配置。"
- 例 5："[日志] 请说明如何集成结构化日志与Tracing。"

### 3. JSON Schema 与序列化

- 用户故事：作为库维护者，我要定义可移植的 schema 并通过 kotlinx.serialization 进行序列化/反序列化。
- 例 1："[schema] 请示例化 buildJsonObject 与 kotlinx.serialization 的混合用法。"
- 例 2："[字段校验] 请提供校验失败时的友好错误返回示例。"
- 例 3："[向后兼容] 请列出 schema 进化的实践要点。"
- 例 4："[示例数据] 请生成 5 个示例请求 payload 用于测试。"
- 例 5："[工具文档] 请生成 schema 文档段落以便输出到 README。"

### 4. 多平台/构建配置

- 用户故事：作为工程负责人，我希望在 Gradle Kotlin DSL 下配置多平台构建并在 JVM 与 wasm 目标都支持 MCP。
- 例 1："[gradle] 请生成 Kotlin Multiplatform 的 build.gradle.kts 示例，包含 JVM 与 JS/wasm 目标。"
- 例 2："[依赖管理] 请说明如何管理跨平台依赖与序列化插件。"
- 例 3："[CI] 请示例化在 CI 中运行多平台测试的步骤。"
- 例 4："[发布] 请说明如何发布到私有 Maven 仓库。"
- 例 5："[兼容性] 请列出常见平台陷阱与规避方法。"

### 5. 调试与性能分析

- 用户故事：作为运维人员，我需要定位协程泄漏与性能瓶颈并制定修复方案。
- 例 1："[分析] 请列出常用的协程泄漏诊断方法与采样策略。"
- 例 2："[压力测试] 请给出压力测试用例与期望的吞吐/延迟目标。"
- 例 3："[监控] 请列出需导出的指标与示例 Prometheus 指标。"
- 例 4："[追踪] 请示例化如何在 CoroutineContext 中传播 tracing 信息。"
- 例 5："[回滚] 请给出当新版本引入性能下降时的回滚策略。"

## 原始文件

- ../../../../chatmodes/kotlin-mcp-expert.chatmode.md
---
post_title: "kotlin-mcp-expert.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "kotlin-mcp-expert-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","kotlin","mcp"]
ai_note: "Generated with AI assistance."
summary: "Kotlin MCP 专家用例：迁移、协程性能与平台集成示例。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供 Kotlin 应用在 MCP 平台上迁移、性能优化与协程管理的用例。

## When

- 在迁移或性能优化、协程问题诊断时使用。

## Why

- 确保并发性能与平台兼容性，提高运行效率。

## How

- 包括协程调优、依赖管理与可观测性集成示例。

## Key points (英文+中文对照)

- Coroutines tuning（协程调优）
- Dependency management（依赖管理）
- Platform integration（平台集成）
- Performance profiling（性能剖析）
- Observability（可观测性）

## 使用场景

### 1. 协程与并发优化

- 用户故事：作为开发者，我要调优协程以减少阻塞与提升吞吐。
- 例 1：示例 dispatcher 与线程池选择建议。
- 例 2：协程泄漏检测与修复示例。
- 例 3：性能基准测试脚本示例。
- 例 4：示例异常处理与超时策略。
- 例 5：并发边界与退避策略建议。

### 2. 平台容器化与启动优化

- 用户故事：作为 SRE，我要优化容器启动与资源使用。
- 例 1：生成轻量化镜像示例。
- 例 2：示例启动探针与资源限制配置。
- 例 3：JVM 参数与内存管理建议。
- 例 4：冷启动优化策略。
- 例 5：示例健康检查脚本。

### 3. 依赖管理与版本兼容

- 用户故事：作为构建工程师，我要确保多模块项目的依赖兼容。
- 例 1：依赖冲突检测与替代建议。
- 例 2：升级兼容性测试矩阵。
- 例 3：生成 CI 依赖扫描示例。
- 例 4：回滚策略与回退计划。
- 例 5：依赖安全扫描样例。

### 4. 可观测性与追踪

- 用户故事：作为运维，我要在生产中追踪异步调用链。
- 例 1：集成 tracing 与 span 语义设计。
- 例 2：示例日志上下文与 correlation id 策略。
- 例 3：性能告警与异常聚合示例。
- 例 4：端到端请求追踪示例。
- 例 5：示例仪表盘查询。

### 5. 平台迁移与兼容性验证

- 用户故事：作为迁移工程师，我要验证 Kotlin 服务在 MCP 的运行兼容性。
- 例 1：生成迁移验证清单与测试用例。
- 例 2：性能基准与资源配置建议。
- 例 3：示例管道与自动化演练脚本。
- 例 4：回退与故障恢复策略。
- 例 5：生成迁移报告模板。

## 原始文件

- [chatmodes/kotlin-mcp-expert.chatmode.md](../../../chatmodes/kotlin-mcp-expert.chatmode.md)
