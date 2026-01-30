---
post_title: "power-bi-data-modeling-expert.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "power-bi-data-modeling-expert-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "power-bi", "data-modeling", "star-schema", "performance", "security"]
ai_note: "Generated with AI assistance."
summary: "Power BI 数据建模专家模式：以星型模型为核心，聚焦关系设计、复合模型、增量刷新、性能与安全治理的端到端实践。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 基于微软官方建模最佳实践，提供 Power BI 模型设计与优化指导：星型模型、关系类型与过滤方向、复合模型与存储模式、数据缩减、RLS 安全等。

## When

- 新建或重构数据模型；从报表驱动表格转向维度建模；需要提升性能或降低内存占用；引入增量刷新与复合模型；落地行级安全时。

## Why

- 以规范化的星型模型和关系策略减少复杂度与性能瓶颈；通过数据缩减和复合模型平衡“性能/数据新鲜度”；用 RLS 与治理提升安全与可运维性。

## How

- 先用 `microsoft.docs.mcp` 查证最新官方建议；在回答中按“文档引用 → 技术概览 → 具体实现（示例）→ 最佳实践 → 下一步”的结构给出方案；优先星型建模，慎用多对多与双向过滤，确保一致的粒度与可折叠查询。

## Key points (英文+中文对照)

- Star schema first（优先星型模型）
- Proper relationships（正确的关系与过滤方向）
- Storage mode wisely（存储模式合理选型）
- Reduce before optimize（先做数据缩减）
- Secure by design（设计即安全：RLS）

## 使用场景

### 1. 绿地建模迁移（Greenfield star schema）

- 用户故事：作为数据建模者，我要从报表驱动表格迁移到星型模型，提升可维护性与性能。
- 例 1："根据业务度量与分析维度，列出候选事实表与维度表清单，并确定一致粒度。"
- 例 2："为维度表设计代理键，规划层级属性与隐藏技术列。"
- 例 3："为事实表保留数值度量与外键列，移除描述性文本列。"
- 例 4："输出一张关系图（文本描述），标注一对多方向与活动关系。"
- 例 5："列出需要保留为计算度量而非计算列的表达式。"

### 2. 关系设计与排障（Relationships & troubleshooting）

- 用户故事：作为模型工程师，我要正确设置基数与过滤方向，并能快速定位关系问题。
- 例 1："根据样本数据判断关系基数，默认一对多，避免不必要的多对多。"
- 例 2："仅在确需穿透过滤时使用双向过滤，给出替代方案（桥接表）。"
- 例 3："对不活跃关系示例，展示在度量中用 `USERELATIONSHIP` 激活的写法。"
- 例 4："提供孤立记录检查与参照完整性验证清单。"
- 例 5："给出减少循环关系与雪花膨胀的重构建议。"

### 3. 复合模型与存储模式（Composite models & storage modes）

- 用户故事：作为数据平台工程师，我需要同时满足历史聚合与实时明细的并存需求。
- 例 1："给出将维度表设置为 `Dual`，事实表历史分区 `Import` + 明细 `DirectQuery` 的组合方案。"
- 例 2："描述跨源关系的限制与测试要点，如何避免跨源计算放大。"
- 例 3："在 DQ 路径下，列出最小化双向过滤与避免复杂计算列的原则。"
- 例 4："生成冷热数据分层策略与切换阈值建议。"
- 例 5："输出监控指标（延迟/失败率/网关）与告警阈值参考。"

### 4. 增量刷新与数据缩减（Incremental refresh & reduction）

- 用户故事：作为性能负责人，我要在保证新鲜度的同时控制模型大小与刷新时间。
- 例 1："根据业务需求建议 `RangeStart/RangeEnd` 窗口与历史期保留策略。"
- 例 2："用可折叠查询的 Power Query 片段演示增量过滤，并说明禁用折叠的代价。"
- 例 3："列出列削减、类型优化与字典编码策略。"
- 例 4："设计按月聚合表 + 明细表的度量切换模式。"
- 例 5："产出刷新作业顺序与并发控制建议。"

### 5. 安全与治理（Security & governance）

- 用户故事：作为模型管理员，我要用行级安全控制访问范围，并满足审计合规。
- 例 1："列出基于邮件账户的动态 RLS 模式，示例 `LOOKUPVALUE` 过滤表达式。"
- 例 2："梳理敏感列的列级安全与脱敏策略。"
- 例 3："定义角色矩阵与层级授权映射，说明测试方法。"
- 例 4："提供数据血缘、变更审计与发布流程建议。"
- 例 5："在复合模型下评估 RLS 与 DQ 源的交互影响。"

## 原始文件

- [chatmodes/power-bi-data-modeling-expert.chatmode.md](../../../chatmodes/power-bi-data-modeling-expert.chatmode.md)
