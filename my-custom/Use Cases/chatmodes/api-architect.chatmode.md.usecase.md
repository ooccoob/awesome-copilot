---
post_title: "api-architect — 用例"
post_slug: "api-architect-use-cases"
tags: ['chatmode','api','architecture','usecase']
ai_note: '根据 chatmodes/api-architect.chatmode.md 生成的中文用例'
summary: '设计 API（REST/GraphQL）、版本策略、安全与性能考量的实战场景与交付产物示例。'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

什么

- 协助架构师与后端工程师设计 API 接口、数据契约、错误模型与非功能需求。

何时

- 在定义外部/内部服务契约、API 重构或对外开放平台设计阶段。

为什么

- 清晰的 API 设计能减少集成成本、提高可维护性并降低破坏性变更风险。

如何

- 提供业务用例、数据模型与期望的调用模式；请求输出包括接口列表、示例请求/响应、错误码、版本与迁移策略。

关键要点 (EN / ZH)

- EN: Contract-first design; versioning; error conventions; pagination and rate limiting.
- ZH: 先契约设计；版本管理；错误规范；分页与限流。

示例场景

1) 设计 RESTful 用户服务
- 示例提示："为用户管理设计 REST API，包括分页、过滤、软删除与错误模型。"
- 预期产出：路径列表、示例请求/响应、HTTP 状态与错误体规范。

2) GraphQL schema 设计
- 示例提示："为电商目录设计 GraphQL schema，包含聚合查询与性能保护建议。"
- 预期产出：schema 草案、resolver 建议与复杂度限制策略。

3) 版本迁移计划
- 示例提示："把 v1 API 平滑迁移到 v2 的计划，列出兼容策略与迁移窗口。"
- 预期产出：迁移步骤、退回策略与通信模板。

4) 安全与配额策略
- 示例提示："建议 API 的鉴权方案（OAuth2/JWT）与速率限制策略。"
- 预期产出：鉴权流程图、速率限制与异常处理建议。

5) API 文档与 SDK 生成流程
- 示例提示："为该 API 生成 OpenAPI 规范与自动化 SDK 生成建议。"
- 预期产出：OpenAPI 草案、生成命令示例与 CI 流程片段。

原始 chatmode: ../../../../chatmodes/api-architect.chatmode.md
---
post_title: "api-architect.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "api-architect-chatmode-md"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "api-architecture"]
ai_note: "Generated with AI assistance."
summary: "API 架构师模式：在开发者说“generate”前收集关键输入，随后产出分层且具备韧性的端到端联通实现与测试。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 作为 API 架构向导：先收集必填输入（语言、端点、方法）及可选韧性需求，待开发者说“generate”后生成分层完备实现与测试。

## When

- 新建或重构到外部服务的调用链路，需要统一分层与韧性策略时。
- 需要从零到一快速产出可运行样例并可扩展时。
- 需要将非功能性（限流/熔断/退避/隔离）纳入一致的架构层时。

## Why

- 通过 service/manager/resilience 明确职责边界，提升可测试性与可维护性。
- 以“先信息后生成”的流程避免错误假设，提高一次成功率。
- 统一采用流行韧性框架，减少重复造轮子与隐性缺陷。

## How

- 初始阶段仅枚举并收集：语言、端点、REST 方法、DTO（可选）、韧性需求、测试范围。
- 开发者说“generate”后：输出三层完整代码（无模板/无省略句），并提供测试用例。
- 遵循关注点分离、全实现无占位、代码优先于注释的原则。

## Key points (英文+中文对照)

- Gather inputs first（先收集信息再生成）
- Three-layer architecture（三层分离：service/manager/resilience）
- Full working code only（输出完整可运行代码）
- Built-in resilience（内置韧性：熔断/限流/退避/隔离）
- Test-ready design（可测试的设计与样例）

## 使用场景

### 1. 从零设计外部 API 连接

- 用户故事：作为集成开发者，我需要在未知条件下快速形成能跑通的端到端调用。
- 例 1："[提供端点 URL] 请列出需要我补充的必填项与可选韧性项。"
- 例 2："[提供语言] 请推荐对应流行的韧性库并说明选择理由。"
- 例 3："[提供初步 DTO] 请补全字段与序列化策略并对齐错误码。"
- 例 4："[提供 REST 方法] 开发者说 generate 后，请生成三层完整实现与测试。"
- 例 5："[提供鉴权方式] 请集成到 service 层并保证可替换性。"

### 2. 将韧性策略纳入架构

- 用户故事：作为架构师，我要把熔断、限流、退避与舱壁并入统一层，避免散落各处。
- 例 1："[提供 SLA] 请映射到超时/重试/退避配置并说明默认值。"
- 例 2："[提供失败模式] 请设计熔断与半开恢复策略。"
- 例 3："[提供吞吐目标] 请给出限流策略与队列/丢弃选择。"
- 例 4："[提供依赖隔离需求] 请加入 Bulkhead 并展示并发配置。"
- 例 5："[提供降级策略] 请在 manager 层实现 fallback 与观测点。"

### 3. 可测试与可替换的接口设计

- 用户故事：作为测试工程师，我需要针对 service/manager/resilience 编写分层测试。
- 例 1："[提供接口定义] 请给出单测与集成测试样板。"
- 例 2："[提供 mock 需求] 请生成基于接口的 mock 与契约测试。"
- 例 3："[提供边界条件] 请补充错误码/超时/重试用例。"
- 例 4："[提供负载建模] 请输出并发与限流下的行为验证。"
- 例 5："[提供 CI 管道] 请集成构建与报告步骤。"

### 4. 迁移与重构到统一分层

- 用户故事：作为维护者，我要把历史散落的 HTTP 调用迁移到统一分层并提升韧性。
- 例 1："[提供调用分布] 请生成迁移路线图与批次划分。"
- 例 2："[提供旧代码片段] 请重构为三层结构并标明可复用部分。"
- 例 3："[提供依赖冲突] 请建议升级/替换路径与风险点。"
- 例 4："[提供配置项] 请输出集中化配置方案与缺省值。"
- 例 5："[提供监控基线] 请映射到指标/日志/追踪注入点。"

### 5. 生成与交付

- 用户故事：作为交付负责人，我需要把生成的代码与测试快速纳入仓库。
- 例 1："[提供模块路径] 开发者说 generate 后，请创建对应目录与文件。"
- 例 2："[提供依赖管理] 请输出需要新增的依赖与版本建议。"
- 例 3："[提供代码规范] 请保证命名与风格符合现有约定。"
- 例 4："[提供运行说明] 请生成 README 片段与使用示例。"
- 例 5："[提供变更计划] 请列出回滚与灰度策略。"

## 原始文件

- [chatmodes/api-architect.chatmode.md](../../../chatmodes/api-architect.chatmode.md)
