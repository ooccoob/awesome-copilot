---
post_title: "postgresql-optimization.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "postgresql-optimization-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "postgresql", "sql", "database", "performance", "optimization"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the PostgreSQL Optimization prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个专门用于优化 PostgreSQL 查询和数据库性能的提示词。

## When

- 当遇到数据库查询缓慢、CPU 或 I/O 使用率过高的问题时。
- 在进行数据库性能调优和容量规划时。
- 当需要深入理解查询执行计划并找出瓶颈时。

## Why

- 提供针对性的、可操作的 PostgreSQL 性能优化建议。
- 帮助用户理解 `EXPLAIN ANALYZE` 的输出，并据此进行优化。
- 涵盖了从查询重写、索引优化到服务器配置调整等多个层面的优化技巧。

## How

- 使用 `/postgresql-optimization` 命令，并提供慢查询的 SQL 语句及其 `EXPLAIN ANALYZE` 的输出。
- AI 将分析执行计划，识别出成本最高的操作、不准确的行数估计或低效的操作（如全表扫描）。
- 生成一份详细的优化报告，建议如何修改查询、创建什么索引，或者调整哪些 PostgreSQL 配置参数。

## Key points (英文+中文对照)

- Query Optimization (查询优化)
- Index Tuning (索引调优)
- Execution Plan Analysis (执行计划分析)
- Performance Tuning (性能调优)

## 使用场景

### 1. 分析和优化慢查询 (Analyzing and Optimizing a Slow Query)

- **用户故事**: 作为一名应用开发者，我有一个查询花费了超过 5 秒钟才返回结果，我需要找出原因并优化它。
- **例 1**: `/postgresql-optimization [selection=slow_query_with_plan.txt] 这是我的慢查询和它的 `EXPLAIN ANALYZE` 计划。请帮我分析瓶颈在哪里，并提供优化建议。`
- **例 2**: `/postgresql-optimization [selection=slow_query_with_plan.txt] 执行计划显示了一个全表扫描（Seq Scan），我应该创建一个什么样的索引来避免它？`

### 2. 索引建议 (Index Recommendation)

- **用户故事**: 作为一名数据库管理员，我希望为我们应用中最常执行的一组查询推荐最佳的索引策略。
- **例 1**: `/postgresql-optimization [selection=queries.sql] 这是我们系统中的一组核心查询。请分析它们，并为 `users` 和 `orders` 表推荐合适的索引。`
- **例 2**: `/postgresql-optimization 我应该创建一个 B-tree 索引还是一个 GIN 索引？我的查询条件是 `WHERE tags @> ARRAY['tag1']`。`

### 3. 数据库配置调优 (Database Configuration Tuning)

- **用户故事**: 作为一名运维工程师，我刚刚将我们的 PostgreSQL 服务器升级到了更大的硬件，我需要调整配置以充分利用新资源。
- **例 1**: `/postgresql-optimization 我的服务器有 64GB 内存。请为我的 `postgresql.conf` 文件推荐合适的 `shared_buffers`, `work_mem`, 和 `effective_cache_size` 的值。`

### 4. 理解复杂的执行计划 (Understanding a Complex Execution Plan)

- **用户故事**: 作为一名初级 DBA，我面对一个非常复杂的查询计划，里面有各种节点，如 Hash Join, Nested Loop, Bitmap Heap Scan，我需要帮助来理解它。
- **例 1**: `/postgresql-optimization [selection=complex_plan.txt] 请逐行解释这个执行计划的每个节点都在做什么。`

## 原始文件

- [postgresql-optimization.prompt.md](../../prompts/postgresql-optimization.prompt.md)
