---
post_title: "postgresql-code-review.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "postgresql-code-review-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "postgresql", "sql", "database", "code-review"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the PostgreSQL Code Review prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于审查 PostgreSQL SQL 代码（包括查询、函数、存储过程和表结构定义）的提示词，旨在发现潜在问题并提出改进建议。

## When

- 在将新的 SQL 代码合并到主分支之前。
- 当需要优化现有查询或数据库对象的性能时。
- 在学习和推广 PostgreSQL 最佳实践时。

## Why

- 自动识别常见的 SQL 反模式、性能陷阱和安全漏洞。
- 提供具体的优化建议，如添加索引、重写查询或改进数据类型。
- 提高数据库代码的质量、性能和可维护性。

## How

- 使用 `/postgresql-code-review` 命令并提供你想要审查的 SQL 代码。
- AI 将从性能、可读性、可维护性和安全性等多个维度分析代码。
- 生成一份详细的审查报告，其中包含发现的问题和具体的改进建议。

## Key points (英文+中文对照)

- SQL Code Review (SQL 代码审查)
- Performance Optimization (性能优化)
- Best Practices (最佳实践)
- Security Vulnerabilities (安全漏洞)

## 使用场景

### 1. 审查新的 DDL（数据定义语言）脚本 (Reviewing New DDL Scripts)

- **用户故事**: 作为一名数据库管理员（DBA），我需要审查开发人员提交的用于创建新表的 DDL 脚本。
- **例 1**: `/postgresql-code-review [selection=create_tables.sql] 审查这个 DDL 脚本。检查数据类型的选择是否合理，是否缺少必要的主键、外键或约束。`
- **例 2**: `/postgresql-code-review [selection=create_tables.sql] 分析这个表结构定义，并建议可能需要的索引。`

### 2. 优化慢查询 (Optimizing Slow Queries)

- **用户故事**: 作为一名后端开发人员，我发现一个报告页面的加载速度非常慢，我怀疑是后端的 SQL 查询有问题。
- **例 1**: `/postgresql-code-review [selection=slow_query.sql] 审查这个慢查询。分析其执行计划，并提出优化建议。`
- **例 2**: `/postgresql-code-review [selection=slow_query.sql] 这个查询中使用了多个 JOIN，有没有办法重写它以提高性能？`

### 3. 检查存储过程和函数的逻辑 (Checking Logic in Stored Procedures and Functions)

- **用户故事**: 作为一名数据库开发人员，我编写了一个复杂的 PostgreSQL 函数，需要确保其逻辑正确且高效。
- **例 1**: `/postgresql-code-review [selection=my_function.sql] 审查这个 PL/pgSQL 函数的逻辑。检查是否存在潜在的 bug、性能问题或不必要的复杂性。`
- **例 2**: `/postgresql-code-review [selection=my_function.sql] 这个函数中有很多循环，有没有办法用基于集合的操作来替代它们？`

### 4. 识别安全风险 (Identifying Security Risks)

- **用户故事**: 作为一名安全工程师，我需要确保我们的数据库代码没有 SQL 注入的风险。
- **例 1**: `/postgresql-code-review [selection=dynamic_query.sql] 审查这个使用了动态 SQL 的函数，检查是否存在 SQL 注入漏洞。`

## 原始文件

- [postgresql-code-review.prompt.md](../../prompts/postgresql-code-review.prompt.md)
