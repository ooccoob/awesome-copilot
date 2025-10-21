---
post_title: "csharp-dotnet-janitor.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "csharp-dotnet-janitor-chatmode-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","csharp","dotnet","janitor"]
ai_note: "Generated with AI assistance."
summary: "针对 C#/.NET 项目进行清理、现代化和性能/可维护性改进的用例集合。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 针对 C#/.NET 代码库的例行重构、清理与现代化建议与操作提示。

## When

- 在代码存在大量陈旧用法、编译警告或性能问题时使用。

## Why

- 降低技术债务、提高可维护性与运行效率，确保代码遵循现代 C# 最佳实践。

## How

- 识别并替换过时 API、移除未使用成员、引入 nullable 引用类型并改善测试覆盖。

## Key points (英文+中文对照)

- Modernize APIs（现代化 API）
- Remove dead code（移除无效代码）
- Improve test coverage（提升测试覆盖率）

## 使用场景

### 1. 代码现代化

- 用户故事：作为维护工程师，我要把旧代码迁移到更现代的写法以提升可读性和性能。
- 例 1："请识别项目中可安全替换为 pattern matching 的用例并给出修改示例。"
- 例 2："请列出应替换的已弃用 API，并给出推荐替代方案。"
- 例 3："请提供将指定文件迁移到 nullable reference types 的步骤清单。"
- 例 4："请建议 LINQ 优化以降低内存分配。"
- 例 5："生成一个小型迁移计划（每次提交的变更点与测试要求）。"

### 2. 清理与风格一致性

- 用户故事：作为代码审查员，我要去除无用引用并统一命名以减少噪声。
- 例 1："扫描并列出未使用的 using/imports 并提供修复指令。"
- 例 2："检查命名不合规项并给出重命名建议。"
- 例 3："指出可合并或抽象的重复逻辑并建议重构。"
- 例 4："提供可在 CI 中运行的静态分析配置示例。"
- 例 5："生成一份提交前检查清单用于 PR 质量控制。"

### 3. 性能与内存优化

- 用户故事：作为性能工程师，我要识别热点并给出低侵入性的优化建议。
- 例 1："发现高分配点并给出使用 Span<T>/Memory<T> 的替代建议。"
- 例 2："识别可使用 StringBuilder 的频繁字符串拼接处并改写。"
- 例 3："给出 async/await 的正确用法以避免线程阻塞。"
- 例 4："建议针对关键路径的基准测试方法与示例代码。"
- 例 5："列出可能的内存泄漏源并提供排查步骤。"

### 4. 测试覆盖与质量把控

- 用户故事：作为 QA 负责人，我希望提升关键公共 API 的单元与集成测试覆盖。
- 例 1："请为指定类生成单元测试用例模板（使用 Arrange/Act/Assert）。"
- 例 2："指出缺失的边界条件测试并给出示例输入。"
- 例 3："生成用于 CI 的测试运行脚本与失败响应策略。"
- 例 4："建议使用 FluentAssertions 的断言示例以提高可读性。"
- 例 5："列出集成测试场景并给出环境准备建议。"

## 原始文件

- ../../chatmodes/csharp-dotnet-janitor.chatmode.md
---
post_title: "csharp-dotnet-janitor.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "csharp-dotnet-janitor-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","csharp","dotnet","janitor"]
ai_note: "Generated with AI assistance."
summary: "C#/.NET 清理和重构助手用例：代码整理、依赖清理、性能与安全检查示例。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供 .NET 项目代码清理、重构与静态检查的具体用例与快速修复示例。

## When

- 在代码倾斜、升级或准备发布前进行代码清理与依赖优化时使用。

## Why

- 保持代码库整洁、减少技术债务并提升可维护性与性能。

## How

- 包括自动重构建议、依赖去除、API 升级路径与性能热点定位示例。

## Key points (英文+中文对照)

- Remove dead code（移除死代码）
- Fix obsolete APIs（修复弃用 API）
- Dependency cleanup（依赖清理）
- Performance hotspots（性能热点）
- Security fixes（安全修复）

## 使用场景

### 1. 移除未使用代码

- 用户故事：作为开发者，我要识别并删除未使用的类/方法以减少混淆。
- 例 1：列出未被引用的 public/internal 类型示例。
- 例 2：提供 Roslyn 分析器规则与修复建议。
- 例 3：生成批量删除脚本前的安全检查清单。
- 例 4：示例单元测试保留策略。
- 例 5：变更日志模板示例。

### 2. 依赖升级与精简

- 用户故事：作为构建工程师，我要升级库版本并移除不再需要的依赖。
- 例 1：生成依赖树与冲突分析示例。
- 例 2：自动化迁移替代代码示例。
- 例 3：回滚策略与版本锁定建议。
- 例 4：安全修复补丁优先级建议。
- 例 5：CI/CD 中的依赖扫描示例。

### 3. 性能剖析与热点优化

- 用户故事：作为性能工程师，我要定位 CPU/内存热点并建议修复。
- 例 1：示例诊断采样与热点分析脚本。
- 例 2：建议使用 ValueTask/Span 等低分配 API 示例。
- 例 3：示例异步并发模型改进建议。
- 例 4：GC 调优建议示例。
- 例 5：负载测试与基准对比模板。

### 4. 安全修复与静态分析

- 用户故事：作为安全工程师，我要在发布前修补明显的安全风险。
- 例 1：示例静态分析器规则与修复建议。
- 例 2：敏感信息检测与脱敏建议。
- 例 3：示例依赖漏洞修复流程。
- 例 4：权限最小化检查样例。
- 例 5：自动化安全回归测试示例。

### 5. 发布前代码质量门禁

- 用户故事：作为发布经理，我要确保代码满足最低质量指标后才发布。
- 例 1：设置质量阈值（覆盖率/复杂度/漏洞数）的示例。
- 例 2：生成合并请求检查列表示例。
- 例 3：示例自动化修复与人工复审流程。
- 例 4：失败回滚与快速回退示例。
- 例 5：质量报告模板示例。

## 原始文件

- [chatmodes/csharp-dotnet-janitor.chatmode.md](../../../chatmodes/csharp-dotnet-janitor.chatmode.md)
