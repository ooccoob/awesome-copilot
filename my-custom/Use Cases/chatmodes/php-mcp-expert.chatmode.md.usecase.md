---
post_title: "php-mcp-expert.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "php-mcp-expert-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","php","mcp"]
ai_note: "Generated with AI assistance."
summary: "PHP MCP 专家用例：性能、依赖管理与安全实践示例。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供 PHP 应用在 MCP 环境中的迁移、性能与安全建议。

## When

- 在迁移到托管平台或需要提升性能与安全时使用。

## Why

- 提高稳定性、减少依赖冲突并保证运行安全。

## How

- 包括性能剖析、缓存策略与安全加固示例。

## Key points (英文+中文对照)

- Opcode caching（Opcode 缓存）
- Dependency management（依赖管理）
- Secure configuration（安全配置）
- Performance tuning（性能调优）
- Observability（可观测性）

## 使用场景

### 1. 性能优化

- 用户故事：作为开发者，我要优化 PHP 服务的响应延迟与并发性能。
- 例 1：配置与评估 opcode 缓存（如 Opcache）。
- 例 2：应用级缓存示例（Redis）与缓存失效策略。
- 例 3：数据库查询优化建议。
- 例 4：示例负载测试脚本。
- 例 5：生成性能回归报告。

### 2. 依赖治理

- 用户故事：作为构建工程师，我要管理 composer 依赖并避免冲突。
- 例 1：依赖锁定与审计脚本示例。
- 例 2：替代方案与兼容性建议。
- 例 3：CI 中的依赖扫描示例。
- 例 4：升级策略与回滚示例。
- 例 5：生成依赖风险评估。

### 3. 安全加固

- 用户故事：作为安全工程师，我要减少常见的 Web 漏洞风险。
- 例 1：输入校验与输出转义示例。
- 例 2：会话管理与 CSRF/ XSS 防护建议。
- 例 3：敏感配置与密钥管理示例。
- 例 4：依赖漏洞扫描与修复流程。
- 例 5：示例安全测试用例。

### 4. 可观测性

- 用户故事：作为 SRE，我要在生产中收集关键指标并快速定位问题。
- 例 1：建议采集的 APM 指标与日志格式。
- 例 2：示例 tracing 与分布式追踪集成。
- 例 3：告警规则与阈值建议。
- 例 4：示例错误恢复脚本。
- 例 5：生成可操作的运行手册。

### 5. 平台迁移准备

- 用户故事：作为迁移工程师，我要把 PHP 服务迁移到 MCP 平台并确保兼容性。
- 例 1：列出平台差异与需调整的配置。
- 例 2：生成迁移演练脚本与回滚步骤。
- 例 3：测试矩阵与兼容性验证。
- 例 4：示例 CI/CD pipeline 调整。
- 例 5：生成迁移报告模板。

## 原始文件

- [chatmodes/php-mcp-expert.chatmode.md](../../../chatmodes/php-mcp-expert.chatmode.md)
