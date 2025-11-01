---
post_title: "semantic-kernel-dotnet — 用例"
post_slug: "semantic-kernel-dotnet-use-cases"
tags: ['chatmode','semantic-kernel','dotnet','usecase']
ai_note: '根据 chatmodes/semantic-kernel-dotnet.chatmode.md 生成的中文用例'
summary: '使用 Semantic Kernel (.NET) 构建基于语义检索与插件化技能代理的场景示例。'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

什么

- 利用 Microsoft Semantic Kernel (.NET) 框架构建技能（skills）、计划（planner）与提示管理的代理应用。

何时

- 当需要构建可组合的 LLM 驱动代理、将外部技能与语义检索结合，或在 .NET 环境中集成 LLM 服务时。

为什么

- Semantic Kernel 提供插件化与计划执行能力，有利于将复杂任务拆解为可组合技能并控制执行流程。

如何

- 提供用例描述、外部技能接口（HTTP/DB）、以及检索数据源；请求输出技能定义、示例 Prompt 与测试方法。

关键要点

- 将外部 I/O 与技能以隔离方式包装
- 设计可重入的计划与错误回退策略
- 衡量语义检索质量与提示工程稳定性

示例场景

1) 构建知识问答代理
- 示例提示："使用 semantic kernel 创建一个文档检索问答技能并集成到 ASP.NET 服务。"
- 预期產出：技能接口、检索管线与示例单元测试。

2) 多技能工作流
- 示例提示："实现一个多步骤订单处理代理，包含验证、发票生成与通知技能。"
- 预期產出：技能设计、计划器示例与错误处理策略。

3) 插件化外部 API 调用
- 示例提示："将外部 REST API 封装为技能并处理速率限制。"
- 预期產出：技能包装器、重试策略与鉴权说明。

4) 本地语义索引集成
- 示例提示："为内部文档构建语义索引并提升检索召回率。"
- 预期產出：索引策略、分片/更新方案与测试集。

5) 测试与监控
- 示例提示："为技能执行添加链路追踪与指标。"
- 预期產出：度量清单、告警阈值与日志结构化建议。

原始 chatmode: ../../../../chatmodes/semantic-kernel-dotnet.chatmode.md
