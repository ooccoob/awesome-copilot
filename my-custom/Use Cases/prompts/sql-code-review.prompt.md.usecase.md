---
post_title: "sql-code-review.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "sql-code-review-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "sql", "database", "code-review", "performance"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the SQL Code Review prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个通用的 SQL 代码审查提示词，用于分析和改进 SQL 查询、存储过程和数据库模式定义，支持多种 SQL 方言（如 PostgreSQL, MySQL, SQL Server）。

## When

- 在将任何 SQL 代码部署到生产环境之前。
- 当需要确保跨不同数据库系统的 SQL 代码的质量和性能时。
- 在团队中建立和执行 SQL 编码标准时。

## Why

- 提供一个自动化的第一道防线，捕捉常见的 SQL 错误和反模式。
- 帮助开发者编写更高效、更安全、更易于维护的 SQL 代码。
- 作为一个学习工具，帮助开发者了解特定 SQL 方言的最佳实践。

## How

- 使用 `/sql-code-review` 命令，并提供你想要审查的 SQL 代码。你可以选择性地指定 SQL 的方言。
- AI 将检查代码的语法、逻辑、性能和安全性。
- 生成一份审查报告，指出潜在问题并提供具体的修改建议。

## Key points (英文+中文对照)

- SQL Best Practices (SQL 最佳实践)
- Query Performance (查询性能)
- Code Readability (代码可读性)
- Security (安全性)

## 使用场景

### 1. 审查跨数据库的查询 (Reviewing a Cross-Database Query)

- **用户故事**: 作为一名全栈开发人员，我编写了一个应该同时在 PostgreSQL 和 MySQL 上运行的查询，我需要确保它的兼容性和性能。
- **例 1**: `/sql-code-review [selection=my_query.sql] 审查这个 SQL 查询。请同时考虑 PostgreSQL 和 MySQL 的最佳实践。`

### 2. 优化数据仓库的 ETL 查询 (Optimizing an ETL Query for a Data Warehouse)

- **用户故事**: 作为一名数据工程师，我有一个复杂的 SQL Server 查询用于我们的 ETL 过程，它运行得非常慢。
- **例 1**: `/sql-code-review [selection=etl_query.sql] 审查这个用于 SQL Server 的 ETL 查询。重点关注其性能，并建议如何优化其中的 `JOIN` 和聚合操作。`

### 3. 检查新表的定义 (Checking a New Table Definition)

- **用户故事**: 作为一名初级开发人员，我为我们的 Oracle 数据库设计了一个新表，我不确定我的数据类型选择是否最佳。
- **例 1**: `/sql-code-review [selection=create_table.sql] 审查这个 Oracle DDL 脚本。评估 `VARCHAR2` 和 `NUMBER` 的使用是否恰当，并检查是否缺少任何约束。`

### 4. 确保代码风格一致性 (Ensuring Code Style Consistency)

- **用户故事**: 作为一名团队负责人，我希望团队的所有 SQL 代码都遵循统一的格式，例如关键字大写，统一使用四个空格缩进。
- **例 1**: `/sql-code-review [selection=messy_query.sql] 审查并重写这个查询，使其符合我们的编码规范：关键字大写，所有连接词（JOIN, WHERE）都换行。`

## 原始文件

- [sql-code-review.prompt.md](../../prompts/sql-code-review.prompt.md)
