---
post_title: "expert-dotnet-software-engineer.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "expert-dotnet-software-engineer-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","dotnet","csharp"]
ai_note: "Generated with AI assistance."
summary: ".NET 专家：包含依赖注入、并发、性能剖析与部署的实战用例集合。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供 .NET（C#）后端的架构与编码用例：依赖注入、异步模式、性能剖析、诊断与云部署示例。

## When

- 新建/重构 .NET 服务、进行性能调优或准备迁移至云平台时使用。

## Why

- 避免常见反模式（同步阻塞、错误的 DI 使用）、提升可维护性并降低生产故障率。

## How

- 提供代码片段（IServiceCollection 扩展、async/await 模式）、profiling 指南（dotnet-trace/PerfView）与部署脚本示例。

## Key points (英文+中文对照)

- Dependency injection（依赖注入）
- Async patterns（异步模式）
- Profiling & diagnostics（性能与诊断）
- Secure coding（安全编码）
- Cloud-native deployment（云原生部署）

## 使用场景

### 1. 依赖注入与模块化

- 用户故事：作为开发者，我需要组织服务注册与生命周期。
- 例 1："示例 IServiceCollection 扩展方法和模块化注册。"
- 例 2："Scoped/Singleton 的典型陷阱与正确使用示例。"
- 例 3："按业务边界拆分服务与接口示例。"
- 例 4："配置与选项绑定示例（IOptions）。"
- 例 5："测试时替换依赖的最佳实践。"

### 2. 并发与异步模式

- 用户故事：作为性能工程师，我要优化异步 IO 与并发吞吐。
- 例 1："正确使用 async/await 与避免同步阻塞示例。"
- 例 2："Channel/TaskPool 的使用场景示例。"
- 例 3："线程池饱和检测与缓解措施。"
- 例 4："并发数据结构的使用建议。"
- 例 5："超时与取消链的实现示例。"

### 3. 性能剖析与调优

- 用户故事：作为 SRE，我需要定位 CPU/GC/IO 瓶颈。
- 例 1："dotnet-trace 与 PerfView 的常用命令与解读。"
- 例 2："降低 GC 压力的内存分配优化示例。"
- 例 3："热路径内联与 JIT 优化建议。"
- 例 4："数据库访问的批量/参数化优化示例。"
- 例 5："在容器中正确收集指标与日志的建议。"

### 4. 安全与编码规范

- 用户故事：作为安全工程师，我要减少常见漏洞并保证代码质量。
- 例 1："输入校验与 API 防护示例。"
- 例 2："敏感配置通过 Key Vault 注入示例。"
- 例 3："依赖库漏洞扫描与更新策略。"
- 例 4："日志脱敏与合规注意事项。"
- 例 5："认证/授权最佳实践（JWT/Policy-based）。"

### 5. 部署与运维

- 用户故事：作为 DevOps，我要可靠地部署并回滚服务。
- 例 1："示例 Helm/ARM 模板与 YAML 部署策略。"
- 例 2："健康检查与就绪探针配置示例。"
- 例 3："蓝绿/滚动发布示例与回滚步骤。"
- 例 4："自动化迁移与数据库版本控制示例。"
- 例 5："部署后性能基线验证清单。"

## 原始文件

- [chatmodes/expert-dotnet-software-engineer.chatmode.md](../../../chatmodes/expert-dotnet-software-engineer.chatmode.md)
