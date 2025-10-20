---
post_title: "ef-core.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "ef-core-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "dotnet", "csharp", "entity-framework-core", "database"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the EF Core prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个专门用于解答和生成与 Entity Framework Core (EF Core) 相关的代码和配置的提示词。

## When

- 在使用 .NET 和 C# 开发需要与数据库交互的应用程序时。
- 当遇到关于数据建模、查询、迁移或性能优化的问题时。
- 在学习或教授 EF Core 时。

## Why

- 提供快速、准确的 EF Core 代码示例和解决方案。
- 帮助开发人员解决常见的 EF Core 问题，提高开发效率。
- 推广 EF Core 的最佳实践。

## How

- 使用 `/ef-core` 命令并提出你的问题或需求。
- AI 将提供相关的代码片段、`DbContext` 配置、LINQ 查询或 `dotnet ef` 命令行指令。
- 你可以复制代码并根据你的项目进行调整。

## Key points (英文+中文对照)

- Data Access (数据访问)
- LINQ Queries (LINQ 查询)
- Database Migrations (数据库迁移)
- Performance Tuning (性能调优)

## 使用场景

### 1. 数据建模和 `DbContext` 配置 (Data Modeling and `DbContext` Configuration)

- **用户故事**: 作为一名 .NET 开发人员，我正在设计我的领域模型，并需要配置它们在数据库中的映射关系。
- **例 1**: `/ef-core 如何在 EF Core 中配置一对多关系？`
- **例 2**: `/ef-core [selection=User.cs] 为这个 `User` 实体生成 Fluent API 配置，将表名映射为 `AppUsers`。`
- **例 3**: `/ef-core 帮我配置一个使用值转换器（Value Converter）将 `enum` 存储为字符串的属性。`

### 2. 编写复杂的 LINQ 查询 (Writing Complex LINQ Queries)

- **用户故事**: 作为一名后端工程师，我需要编写一个复杂的查询来从数据库中检索数据。
- **例 1**: `/ef-core 如何使用 EF Core 编写一个包含 `Include` 和 `ThenInclude` 的查询来加载关联数据？`
- **例 2**: `/ef-core 给我一个使用 `GroupBy` 和 `Select` 进行数据聚合的 LINQ 查询示例。`
- **例 3**: `/ef-core 如何在 EF Core 中执行原始 SQL 查询？`

### 3. 数据库迁移 (Database Migrations)

- **用户故事**: 作为一名开发人员，我已经修改了我的数据模型，现在需要将这些更改应用到数据库中。
- **例 1**: `/ef-core 生成一个 `dotnet ef migrations add` 命令来创建一个名为 `AddUserEmail` 的新迁移。`
- **例 2**: `/ef-core 如何回滚到上一个数据库迁移？`

### 4. 性能优化 (Performance Optimization)

- **用户故事**: 作为一名数据库管理员，我发现我们的应用数据库查询很慢，需要进行优化。
- **例 1**: `/ef-core 解释一下 EF Core 中的 `AsNoTracking()` 是什么以及何时使用它。`
- **例 2**: `/ef-core 如何在 EF Core 中解决 N+1 查询问题？`
- **例 3**: `/ef-core 给我一些优化 EF Core 查询性能的最佳实践。`

## 原始文件

- [ef-core.prompt.md](../../prompts/ef-core.prompt.md)
