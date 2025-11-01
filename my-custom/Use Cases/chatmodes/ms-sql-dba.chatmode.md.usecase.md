---
post_title: "ms-sql-dba.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "ms-sql-dba-chatmode-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: ["use-cases","chatmode","database"]
tags: ["use-cases","sql","dba"]
ai_note: "Generated with AI assistance from chatmodes/ms-sql-dba.chatmode.md"
summary: "Use cases for MS SQL DBA assistant: performance tuning, backup strategies, query optimization, and migration guidance." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- A database administrator assistant focused on Microsoft SQL Server: performance troubleshooting, index recommendations, backup/restore guidance, and migration planning.

## When

- When DBAs and engineers need quick diagnostics, tuning suggestions, or migration checklists for SQL Server instances.

## Why

- To shorten troubleshooting cycles, provide consistent tuning advice, and codify migration best practices.

## How

- Accept metrics (wait stats, slow queries, index usage) and provide targeted recommendations.
- Generate scripts for index creation/maintenance, explain plans, and backup validation.
- Produce migration step lists and rollback plans.

## Key points (英文+中文对照)

- Index & query tuning（索引与查询调优）
- Backup and restore strategies（备份与恢复策略）
- Migration planning（迁移规划）

## 使用场景

### 1. Diagnose slow queries

- 用户故事：作为 DBA，我想快速定位并修复导致慢查询的根因。
- 例 1："[分析] 提供一个步骤清单，以收集执行计划和等待统计信息。"
- 例 2："[建议] 根据执行计划建议 3 个改进索引或查询重写的方案。"
- 例 3："[脚本] 生成查询分析脚本以便重复运行并记录差异。"
- 例 4："[验证] 提供性能验证步骤以确保更改未引入回归。"
- 例 5："[回滚] 生成回滚脚本与风险说明。"

### 2. Backup & DR verification

- 用户故事：作为运维工程师，我需要验证备份完整性并确保恢复路径可靠。
- 例 1："[检查] 生成自动化备份验证脚本并报告缺失项。"
- 例 2："[演练] 提供一次恢复演练的详细计划与检查点。"
- 例 3："[加密] 建议备份加密与存储策略。"
- 例 4："[合规] 生成满足合规审计要求的备份报告模板。"
- 例 5："[恢复] 生成多个恢复场景的步骤（时间点恢复、故障转移等）。"

### 3. Migration planning

- 用户故事：作为架构师，我想把本地 SQL Server 迁移到托管实例或云端并确保最小停机。
- 例 1："[评估] 生成迁移评估清单，涵盖兼容性、功能差异与性能预估。"
- 例 2："[步骤] 提供详细迁移流程与回滚点。"
- 例 3："[容量] 估算目标环境资源需求并给出优化建议。"
- 例 4："[测试] 生成迁移后验证测试清单与性能基线对比方法。"
- 例 5："[自动化] 生成迁移脚本的示例并说明安全注意点。"

## 原始文件

- ../../../../chatmodes/ms-sql-dba.chatmode.md
---
post_title: "ms-sql-dba.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "ms-sql-dba-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","mssql","dba"]
ai_note: "Generated with AI assistance."
summary: "MS SQL DBA 场景：性能调优、索引改进、备份与恢复策略示例。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 提供 MS SQL Server 日常运维、性能调优与灾备的实用用例。

## When

- 在性能瓶颈诊断、备份策略制定或架构优化时使用。

## Why

- 降低停机风险、提高查询性能并保证数据一致性。

## How

- 包括索引建议、执行计划分析、备份恢复演练与容量规划示例。

## Key points (英文+中文对照)

- Index tuning（索引调优）
- Execution plans（执行计划）
- Backup & restore（备份与恢复）
- High availability（高可用）
- Maintenance jobs（维护任务）

## 使用场景

### 1. 索引与查询优化

- 用户故事：作为 DBA，我要定位慢查询并提出索引改进建议。
- 例 1：分析执行计划并建议索引/重写查询。
- 例 2：示例创建覆盖索引的语句。
- 例 3：建议统计信息刷新策略。
- 例 4：示例查询重写以减少扫描。
- 例 5：生成回归测试用例以验证变更影响。

### 2. 备份策略设计

- 用户故事：作为运维，我要设计适合 RPO/RTO 的备份策略。
- 例 1：示例完整/差异/事务日志备份策略。
- 例 2：恢复演练脚本示例。
- 例 3：备份保留与合规性策略建议。
- 例 4：异地复制与容灾示例。
- 例 5：监控备份成功/失败的告警配置。

### 3. 高可用与复制

- 用户故事：作为架构师，我要部署 Always On/可用性组以保障可用性。
- 例 1：示例部署拓扑与配置要点。
- 例 2：故障转移策略与验证步骤。
- 例 3：读写分离策略建议。
- 例 4：监控与健康检查脚本示例。
- 例 5：性能影响评估建议。

### 4. 维护与自动化作业

- 用户故事：作为 DBA，我要自动化日常维护任务并预防问题。
- 例 1：索引重建/重组计划脚本。
- 例 2：清理历史数据与归档策略示例。
- 例 3：自动化统计信息维护脚本。
- 例 4：示例告警与自动化恢复流程。
- 例 5：容量规划模板。

### 5. 安全与合规

- 用户故事：作为安全负责人，我要确保数据库访问与审计满足合规要求。
- 例 1：示例最小权限用户策略。
- 例 2：审计日志配置示例。
- 例 3：敏感数据脱敏/加密建议。
- 例 4：访问审批与临时特权管理样例。
- 例 5：合规审计报告模板。

## 原始文件

- [chatmodes/ms-sql-dba.chatmode.md](../../../chatmodes/ms-sql-dba.chatmode.md)
