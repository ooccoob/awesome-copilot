---
post_title: "csharp-mcp-expert.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "csharp-mcp-expert-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","csharp","mcp"]
ai_note: "Generated with AI assistance."
summary: "面向 C# MCP 专家的用例：代码迁移、性能调优、架构建议与最佳实践。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供面向 C# 项目在 MCP 环境中的实用建议与迁移、优化的示例。

## When

- 在项目需要符合 MCP 运行约束或迁移到 MCP 平台时使用。

## Why

- 提供可执行步骤以确保兼容性、性能与可维护性。

## How

- 包括架构建议、迁移步骤、性能剖析与测试方案。

## Key points (英文+中文对照)

- Compatibility checks（兼容性检查）
- Performance tuning（性能调优）
- Dependency management（依赖管理）
- Telemetry & diagnostics（遥测与诊断）
- Deployment strategy（部署策略）

## 使用场景

### 1. MCP 兼容性迁移

- 用户故事：作为工程师，我要迁移库以确保与 MCP 平台兼容。
- 例 1：列出不兼容 API 与替代方案。
- 例 2：生成迁移步骤与验证用例。
- 例 3：测试矩阵示例。
- 例 4：示例回滚策略。
- 例 5：性能基线比较。

### 2. 性能诊断与优化

- 用户故事：作为性能工程师，我要定位并优化 CPU/内存热点。
- 例 1：生成基准测试脚本与采样建议。
- 例 2：提出代码级别的优化建议。
- 例 3：提供 async/await 优化示例。
- 例 4：示例内存泄漏检测步骤。
- 例 5：生成监控指标与告警建议。

### 3. 依赖与版本治理

- 用户故事：作为维护者，我要管理第三方依赖并评估兼容性风险。
- 例 1：列出关键依赖与兼容性说明。
- 例 2：生成替代库建议。
- 例 3：自动化依赖扫描脚本示例。
- 例 4：依赖更新策略示例。
- 例 5：回归测试建议。

### 4. 可观测性与故障排查

- 用户故事：作为 SRE，我要在生产中快速定位问题并回滚影响。
- 例 1：遥测事件与日志结构建议。
- 例 2：示例追踪与聚合查询。
- 例 3：快速故障排查清单。
- 例 4：自动化恢复脚本样例。
- 例 5：可视化仪表盘建议。

### 5. 安全与合规

- 用户故事：作为安全负责人，我要保证依赖与运行时配置符合同步安全策略。
- 例 1：生成依赖漏洞扫描脚本示例。
- 例 2：建议秘密管理与访问控制策略。
- 例 3：安全测试用例建议。
- 例 4：审计日志格式建议。
- 例 5：快速应急响应流程模板。

## 原始文件

- [chatmodes/csharp-mcp-expert.chatmode.md](../../../chatmodes/csharp-mcp-expert.chatmode.md)
