## What
- 生成基于官方 go-sdk 的完整 MCP 服务器工程：模块布局、依赖、传输、工具与资源、测试与文档。

## When
- 需要可运行、可扩展且结构规范的 Go MCP 服务脚手架时。

## Why
- 降低接入门槛，统一结构与最佳实践，便于二次扩展与测试。

## How
- 结构：go.mod/main.go/tools/resources/config/README/tests
- 能力：Stdio Transport；注册 2–3 个工具（强类型输入输出）
- 健壮性：context 取消、错误处理、优雅退出、日志
- 文档与测试：README 用法/配置；至少一项工具测试

## Key points (CN)
- 类型安全（JSON Schema 标签）；工具单一职责
- main.go 最小化，逻辑入包；可扩展注册表
- 配置走 env；日志结构化

## Key points (EN)
- Proper module layout; typed tools; stdio transport
- Context-aware error handling; graceful shutdown
- Docs + tests included; minimal main

## Example questions
- “生成包含 greet/calc 工具的基础 MCP 服务骨架？”
- “如何按 env 覆盖服务名与版本？”

## 思维导图（要点）
- 结构/依赖
- 工具/资源/提示
- 错误/上下文/退出
- 文档/测试/配置

—
- Source: d:\mycode\awesome-copilot\prompts\go-mcp-server-generator.prompt.md
- Generated: 2025-10-17
