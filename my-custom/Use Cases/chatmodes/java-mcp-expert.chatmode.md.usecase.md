---
post_title: "java-mcp-expert.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "java-mcp-expert-chatmode-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: ["use-cases","chatmode"]
tags: ["use-cases","java","mcp","server"]
ai_note: "Generated with AI assistance from chatmodes/java-mcp-expert.chatmode.md"
summary: "Use cases for building Java MCP servers: server setup, tool/resource/prompt implementation, reactive patterns, and Spring Boot integration."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- Expert guidance for building Model Context Protocol (MCP) servers in Java, including server architecture, tool/resource/prompt development, reactive streams with Project Reactor, and Spring Boot integration.

## When

- When teams need to implement or improve a Java MCP server, integrate MCP into Spring Boot apps, or design tools/resources/prompts for MCP-based services.

## Why

- To create robust, observable, and production-ready MCP servers that handle streaming and request/response patterns correctly and scale with reactive design.

## How

- Use the official MCP Java SDK with McpServerBuilder; declare capabilities (tools/resources/prompts) explicitly.
- Prefer Reactor types (Mono/Flux) for async responses; use bounded elastic scheduler for blocking calls.
- Define tools with JSON Schema and validate inputs; return ToolResponse objects with structured content.
- Register transports (stdio, HTTP) and integrate with Spring Boot using a McpServerConfigurer bean.
- Add structured logging (SLF4J) and context propagation for observability and tracing.

## Key points (英文+中文对照)

- Reactive server idiom with Mono/Flux（使用 Mono/Flux 的响应式服务范式）
- Tool definitions using JSON Schema（使用 JSON Schema 定义工具输入与验证）
- Spring Boot integration via McpServerConfigurer（通过 McpServerConfigurer 与 Spring Boot 集成）

## 使用场景

### 1. 快速启动 MCP Java 服务

- 用户故事：作为后端工程师，我需要在本地快速搭建一个可运行的 MCP Java 服务来调试工具行为并进行端到端测试。
- 例 1："[创建项目骨架] 请为我生成 Maven/Gradle 依赖与最小可运行示例，包含 McpServerBuilder 配置。"
- 例 2："[配置 transport] 请给出启动 StdioServerTransport 的示例代码以及如何在 IDE 中调试。"
- 例 3："[注册工具] 请展示如何注册一个名为 'process' 的工具及其同步和异步处理示例。"
- 例 4："[运行测试] 请提供用于验证工具处理的单元测试示例（同步与 Reactor 测试）。"
- 例 5："[部署指南] 请给出本地到云端的部署注意事项与容器化建议。"

### 2. 构建并验证工具与输入 Schema

- 用户故事：作为工具开发者，我需要定义工具的输入 Schema 并确保在运行时正确校验与报错。
- 例 1："[定义 Schema] 请提供 JsonSchema 构建器的示例，包含必填字段与枚举校验。"
- 例 2："[参数校验] 请写出处理代码示例，演示接收参数并在校验失败时返回明确错误。"
- 例 3："[示例 Payload] 请给出 5 个有效/无效的请求示例用于测试。"
- 例 4："[错误策略] 请建议错误处理与重试策略（何时返回 error、何时重试）。"
- 例 5："[文档] 请生成工具的 README 段落，描述输入、输出与示例调用。"

### 3. 处理流式资源与订阅

- 用户故事：作为数据工程师，我需要在 MCP 中注册可订阅的资源并正确处理订阅生命周期与通知。
- 例 1："[资源注册] 请展示如何注册 Resource URI 与 read handler 的示例。"
- 例 2："[订阅管理] 请给出订阅/取消订阅的服务器端实现并记录订阅列表。"
- 例 3："[多内容响应] 请示例化如何在一个响应中同时返回文本与二进制数据。"
- 例 4："[通知] 请给出资源变更通知的实现示例并说明并发安全。"
- 例 5："[样例查询] 请提供资源采样与分页示例以供客户端展示。"

### 4. 与 Spring Boot 集成与配置

- 用户故事：作为后端架构师，我希望通过 Spring Boot 自动装配 MCP 服务并在应用启动时注册能力。
- 例 1："[配置类] 请生成 McpServerConfigurer 的 Spring Bean 配置示例。"
- 例 2："[Properties] 请列出可配置项（端口、transport、启用 capability 的开关）并给出 application.yml 示例。"
- 例 3："[健康检查] 请说明如何在 Actuator 中暴露 MCP 服务健康状态。"
- 例 4："[安全] 请给出建议的认证/授权方案（仅接口设计层面，不包含实现秘钥）。"
- 例 5："[高可用] 请建议部署架构以保证高可用与可伸缩性。"

### 5. 测试、监控与可观察性

- 用户故事：作为运维工程师，我需要监控 MCP 服务器的处理延迟、错误率与订阅数量，以便快速定位问题。
- 例 1："[指标] 请列出关键 Prometheus 指标与采集点示例。"
- 例 2："[日志] 请给出结构化日志示例并说明在哪些点记录关键信息。"
- 例 3："[追踪] 请说明如何在 Reactor 上下文中传播追踪 ID 并示例化代码。"
- 例 4："[压测] 请给出负载测试场景与期望瓶颈指标。"
- 例 5："[告警] 请列出需告警的事件并建议阈值范围（初始建议）。"

## 原始文件

- ../../../../chatmodes/java-mcp-expert.chatmode.md
---
post_title: 'java-mcp-expert — Use Cases'
post_slug: 'java-mcp-expert-use-cases'
tags: ['chatmode','java','mcp','usecase']
ai_note: 'Generated from chatmodes/java-mcp-expert.chatmode.md'
summary: 'Use cases for the Java MCP expert chatmode: code reviews, migration guidance, performance tuning, and design patterns suited for enterprise Java applications.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

What
====
A chatmode tuned to provide Java/MCP specific advice: code patterns, migration recipes, debugging steps, test strategies, and performance tuning for enterprise Java codebases.

When
====
When developers need step-by-step Java implementation guidance, code review commentary, or migration strategies to modernize Java services in an MCP context.

Why
===
To accelerate Java development while keeping to platform conventions, maintainability, and performance trade-offs specific to the MCP ecosystem.

How
===
Feed code snippets, stack traces, configuration files, or feature descriptions and ask for concrete actionable outputs: refactor plan, test cases, fixed snippets, or benchmarks.

Key Points (EN)
- Practical Java idioms and anti-pattern detection
- Clear migration or modernization steps
- Performance tuning and hotspot analysis

要点 (ZH)
- 指导 Java 常用惯用法并识别反模式
- 提供清晰的迁移/现代化步骤
- 性能调优与热点分析

Scenarios
---------

1) Code review suggestions
- Prompt: "Review this Java method for thread-safety and performance: [insert snippet]. Provide fixes and tests." 
- Expected output: list of issues, refactored snippet, unit test outline, and complexity analysis.

2) Migration from legacy framework
- Prompt: "Plan migration of a Spring MVC app to Spring Boot with minimal downtime. Database: MySQL. Size: 30 microservices." 
- Expected output: migration phases, backward-compat API plan, CI/CD changes, and database migration approach.

3) Memory leak diagnosis
- Prompt: "Heap grows over time in service X; garbage collector logs attached. Suggest likely causes and investigative steps." 
- Expected output: probable causes, instrumentation steps (jmap/jstack), sampling recommendations, and patch plan.

4) Performance tuning
- Prompt: "Service sees high GC pause times. Provide GC tuning recommendations, metrics to monitor, and safe rolling restart plan." 
- Expected output: GC config suggestions, monitoring charts to target, and incremental rollout plan.

5) Secure coding checklist
- Prompt: "Audit this login flow for security vulnerabilities and recommend fixes." 
- Expected output: list of vulnerabilities, code-level fixes, and automated tests to assert security behavior.

Original chatmode: ../../../../chatmodes/java-mcp-expert.chatmode.md
