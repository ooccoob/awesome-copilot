---
post_title: "sql-optimization.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "sql-optimization-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "sql", "database", "performance", "optimization"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the SQL Optimization prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个通用的 SQL 性能优化提示词，旨在分析慢查询并提供具体的改进建议，支持多种数据库系统。

## When

- 当应用程序的数据库交互成为性能瓶颈时。
- 在需要对特定的、已知的慢查询进行深度分析和重写时。
- 在进行数据库性能审计或准备容量扩展时。

## Why

- 提供基于查询执行计划的、数据驱动的优化建议。
- 帮助开发者和 DBA 理解查询缓慢的根本原因，而不仅仅是表面现象。
- 教授高级的 SQL 优化技术，如索引策略、查询重写和利用特定数据库的功能。

## How

- 使用 `/sql-optimization` 命令，并提供慢查询的 SQL 语句。
- **强烈建议**同时提供该查询的 `EXPLAIN` 或 `EXPLAIN ANALYZE` 计划，这将极大地提高优化建议的准确性。
- AI 将分析查询的逻辑和执行计划，找出瓶颈所在（如全表扫描、错误的连接顺序、昂贵的排序等）。
- 生成一份详细的报告，包含一或多个优化方案，例如：
    - 创建或修改索引。
    - 重写查询（例如，改变 JOIN 类型，使用子查询或 CTE）。
    - 调整数据库配置。

## Key points (英文+中文对照)

- Query Tuning (查询调优)
- Indexing Strategy (索引策略)
- Execution Plan (执行计划)
- Performance Bottleneck (性能瓶颈)

## 使用场景

### 1. 优化带有多个 JOIN 的复杂查询 (Optimizing a Complex Query with Multiple Joins)

- **用户故事**: 作为一名数据分析师，我有一个查询需要连接五个表，它几乎无法在合理的时间内运行完毕。
- **例 1**: `/sql-optimization [selection=complex_query_with_plan.txt] 这是我的 SQL Server 查询及其执行计划。请帮我分析为什么它这么慢，并告诉我如何优化 JOIN 的顺序或类型。`

### 2. 解决全表扫描问题 (Addressing a Full Table Scan Issue)

- **用户故事**: 作为一名应用开发者，我从监控工具中得知，我的一个查询正在对一个有数百万行记录的表进行全表扫描。
- **例 1**: `/sql-optimization [selection=query_with_seqscan.txt] 这是我的 PostgreSQL 查询和它的 `EXPLAIN` 计划。请告诉我应该在 `WHERE` 子句的哪个列上创建索引来避免全表扫描。`
- **例 2**: `/sql-optimization 我已经在一个列上创建了索引，但查询规划器仍然没有使用它。这是我的查询和计划，请帮我分析原因。`

### 3. 重写使用相关子查询的查询 (Rewriting a Query with Correlated Subqueries)

- **用户故事**: 作为一名数据库开发人员，我听说相关子查询通常性能不佳，我想将我的一个查询重写为使用 `JOIN` 或 `LATERAL JOIN`。
- **例 1**: `/sql-optimization [selection=correlated_subquery.sql] 请将这个使用相关子查询的 MySQL 查询重写为一个更高效的等效查询。`

### 4. 学习如何阅读执行计划 (Learning How to Read Execution Plans)

- **用户故事**: 作为一名初级 DBA，我想学习如何解读不同数据库的执行计划。
- **例 1**: `/sql-optimization [selection=oracle_plan.txt] 这是 Oracle 数据库的一个执行计划。请向我解释 `HASH JOIN` 和 `NESTED LOOPS` 在这里分别代表什么，以及它们的成本（cost）是如何计算的。`

## 原始文件

- [sql-optimization.prompt.md](../../prompts/sql-optimization.prompt.md)
