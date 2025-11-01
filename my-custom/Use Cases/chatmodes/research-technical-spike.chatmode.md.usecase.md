---
post_title: "research-technical-spike.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "research-technical-spike-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "technical-spike"]
ai_note: "Generated with AI assistance."
summary: "技术 Spike 研究模式的系统化用例：递归研究、证据留痕、活体文档与 Todo 协同。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 以“工具驱动 + 递归深挖 + 实证验证”为核心的技术 Spike 研究工作流。

## When

- 在选型、未知技术验证、复杂集成调研、迁移路径探索、性能/安全评估等场景中。

## Why

- 防止“一眼定论”与信息片面，确保研究可复查、可追踪、可复现，形成对实现直接可用的证据链。

## How

- 研究开始即建立 Todo；使用 search/fetch/githubRepo/extensions 等工具递归跟进线索；重要发现即时写回 Spike；权限相关操作先征求许可；对实现想法用最小实验验证并记录失败结论。

## Key points (英文+中文对照)

- Obsessive, recursive research.（痴迷且递归的研究法）
- Evidence as you go.（发现即记录证据）
- Living spike document.（Spike 文档持续演进）
- Minimal experiments first.（先做最小化验证）
- Todo-driven tracking.（以待办驱动追踪）

## 使用场景

### 1. 选型与对比（Technology evaluation）

- 用户故事：作为架构师，我需要在多个技术路线间做证据化选择，并能向团队复盘取舍。
- 例 1："建立对比表，填入来源可追溯的性能/维护/生态证据，并给出推荐结论。"
- 例 2："用 #fetch 拉取官方基准/限制，标注版本与日期。"
- 例 3："通过 #githubRepo 寻找生产级实现，提炼常见架构与坑点。"
- 例 4："把被淘汰的方案与原因记录到 ‘Decision Trail’。"
- 例 5："生成 3 个‘最小验证实验’，各自列出期望与停机准则。"

### 2. 集成可行性验证（Integration feasibility）

- 用户故事：作为开发者，我要在上线前确认第三方集成的 API/鉴权/速率限制在我方约束内可行。
- 例 1："用 #fetch 获取官方 API 速率限制，并在 Spike 标注实际边界。"
- 例 2："通过 #search 找到鉴权失败的常见原因与规避方法。"
- 例 3："以最小样例创建 PoC，记录命令、输出与失败原因。"
- 例 4："把 PoC 结果写入 ‘Prototype/Testing Notes’，并关联外部资源。"
- 例 5："基于证据给出‘继续/终止/替代’明确建议。"

### 3. 性能与容量探索（Performance and capacity）

- 用户故事：作为性能工程师，我需要基于事实的容量估算与瓶颈定位方法论。
- 例 1："设计最小压测脚本与数据集，并记录指标与波动范围。"
- 例 2："通过 #githubRepo 找到相同技术栈的容量经验，交叉验证趋势。"
- 例 3："拉链式递进实验：先锁定单变量，再扩展组合变量。"
- 例 4："失败实验同样记录，追踪到配置/版本/依赖。"
- 例 5："总结可复用的性能优化 checklist。"

### 4. 安全与合规调研（Security and compliance）

- 用户故事：作为安全负责人，我要在实现前确认关键安全约束、组件许可与数据路径。
- 例 1："列出与场景相关的 OWASP/合规要点，并给出验证方法。"
- 例 2："对三方库做许可证与 CVE 粗筛，标注潜在阻断因素。"
- 例 3："整理鉴权/加密/密钥管理的可选方案与权衡。"
- 例 4："调查审计/日志留存要求，列出落地策略。"
- 例 5："将所有安全前置条件纳入 Todo 并持续跟踪。"

### 5. 研究到计划的交接（Research-to-plan handoff）

- 用户故事：作为团队协调者，我需要把研究结果转交给计划/实现同学，无缝继续。
- 例 1："在 Spike 中提供 ‘Recommended Approach’ 的单一选择，删除弃用路线。"
- 例 2："把关键证据与链接整理为 ‘External Resources’ 清单。"
- 例 3："输出实现所需的前置条件、依赖与明确边界。"
- 例 4："生成一页‘研究亮点’供评审会快速浏览。"
- 例 5："将 Todo 清单与完成状态一并交接。"

## 原始文件

- chatmodes/research-technical-spike.chatmode.md
