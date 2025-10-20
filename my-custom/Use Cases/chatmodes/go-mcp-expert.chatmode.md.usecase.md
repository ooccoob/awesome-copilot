---
post_title: "go-mcp-expert.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "go-mcp-expert-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","go","mcp"]
ai_note: "Generated with AI assistance."
summary: "Go MCP 专家用例：面向后端服务的 Go 代码实践、模块化、并发模式与性能调优的可执行场景。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供面向 Go 的微服务与库开发最佳实践：项目布局、依赖管理、并发模式、测试与 benchmark 示例。

## When

- 新建 Go 服务、重构性能关键路径或准备代码审查/性能优化时使用。

## Why

- 提供一致的工程实践，减少常见并发错误（竞态）、提高可测性并改进上线质量与性能。

## How

- 给出模板化项目结构、示例代码片段（worker pool、context 用法）、单元测试/基准测试脚本与常见问题排查清单。

## Key points (英文+中文对照)

- Module & dependency management（模块与依赖管理）
- Context cancellation（Context 取消）
- Concurrency patterns（并发模式）
- Profiling & benchmarking（分析与基准）
- Error handling & observability（错误处理与可观测性）

## 使用场景

### 1. 项目启动模版

- 用户故事：作为工程师，我需要一个可复制的 Go 服务模版来快速启动项目。
- 例 1："提供模块化目录结构与 go.mod 范例。"
- 例 2："示例 main.go 启动流程与优雅停机实现。"
- 例 3："Dockerfile 与 multi-stage 构建示例。"
- 例 4："CI 基本流水线（lint/test/build/publish）示例。"
- 例 5："安全依赖扫描与依赖版本管理策略。"

### 2. 并发与协程池

- 用户故事：作为性能工程师，我要实现稳定的 worker-pool 以降低内存峰值。
- 例 1："示例 worker pool 实现与负载控制。"
- 例 2："使用 context 进行超时/取消的最佳实践。"
- 例 3："避免 goroutine 泄漏的检测与修复方法。"
- 例 4："并发数据结构的线程安全用法示例。"
- 例 5："性能监控点与指标示例（goroutine count/allocs）。"

### 3. 性能剖析与调优

- 用户故事：作为 SRE，我需要快速定位 CPU/内存热点。
- 例 1："pprof CPU/heap 快速定位流程。"
- 例 2："benchmark 测试样例与比较报告。"
- 例 3："减少内存分配与对象重用示例。"
- 例 4："锁竞争检测与优化策略。"
- 例 5："生产剖析的安全与采样建议。"

### 4. 测试与契约

- 用户故事：作为 QA，我要服务遵循契约并能做端到端测试。
- 例 1："示例 mock/测试替身与 table-driven 单元测试。"
- 例 2："契约测试（Pact/自定义）集成示例。"
- 例 3："集成测试容器化（Testcontainers/Localstack 等）。"
- 例 4："稳定化 flaky 测试的策略。"
- 例 5："CI 中的测试分层与并行运行示例。"

### 5. 可观察性与错误处理

- 用户故事：作为运维，我需要高质量的日志与追踪以便快速定位问题。
- 例 1："示例 structured logging（带 traceId）的实现。"
- 例 2："在出口点注入度量并导出 Prometheus。"
- 例 3："错误包装与语义日志策略示例。"
- 例 4："链路追踪（Opentelemetry）接入指南。"
- 例 5："异常率告警与自动化响应建议。"

## 原始文件

- [chatmodes/go-mcp-expert.chatmode.md](../../../chatmodes/go-mcp-expert.chatmode.md)
