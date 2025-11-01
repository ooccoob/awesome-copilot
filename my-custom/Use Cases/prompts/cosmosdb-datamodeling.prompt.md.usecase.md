---
post_title: "cosmosdb-datamodeling.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "cosmosdb-datamodeling-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "azure", "cosmosdb", "datamodeling"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Cosmos DB Data Modeling prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于指导 Cosmos DB 数据建模的提示词，帮助用户根据其领域模型和访问模式设计最佳的数据模型。

## When

- 在开始一个新的使用 Cosmos DB 的项目时。
- 当需要为现有应用程序设计新的数据模型时。
- 当遇到性能问题并怀疑数据模型是瓶颈时。

## Why

- 确保数据模型能够高效地支持应用程序的查询和访问模式。
- 帮助开发人员理解 Cosmos DB 的数据建模最佳实践，如嵌入、引用和分区。
- 减少由于数据模型设计不当而导致的后期重构成本。

## How

- 使用 `/cosmosdb-datamodeling` 命令并提供领域模型、访问模式和非功能性需求。
- AI 将分析输入并提供一个或多个建议的数据模型方案。
- 每个方案都会解释其优缺点以及适用的场景。

## Key points (英文+中文对照)

- Data Modeling (数据建模)
- Access Patterns (访问模式)
- Partitioning Strategy (分区策略)
- Embedding vs. Referencing (嵌入与引用)

## 使用场景

### 1. 新项目的初始数据模型设计 (Initial Data Model Design for New Projects)

- **用户故事**: 作为一名后端开发人员，我正在为一个新的电子商务应用设计数据模型，该应用将使用 Cosmos DB。我需要一个能够支持产品目录、订单和用户配置文件的模型。
- **例 1**: `/cosmosdb-datamodeling [selection=ecommerce_domain.json] 基于这些领域实体和访问模式，为我设计一个 Cosmos DB 数据模型。`
- **例 2**: `/cosmosdb-datamodeling 我需要一个支持高读写吞吐量的社交媒体应用的数据模型。`

### 2. 现有模型的性能优化 (Performance Optimization for Existing Models)

- **用户故事**: 作为一名数据库管理员，我发现我们的 Cosmos DB 查询延迟很高。我怀疑是数据模型的问题，并希望得到优化建议。
- **例 1**: `/cosmosdb-datamodeling [selection=current_model.json] 这是我们当前的模型和遇到的性能问题，请提供优化建议。`
- **例 2**: `/cosmosdb-datamodeling 我们的分区键选择似乎不合理，导致了热点分区。请帮我重新设计分区策略。`

### 3. 从关系数据库迁移 (Migration from Relational Databases)

- **用户故事**: 作为一名解决方案架构师，我正在计划将一个现有的 SQL Server 数据库迁移到 Cosmos DB。我需要帮助将关系模型转换为 NoSQL 模型。
- **例 1**: `/cosmosdb-datamodeling [selection=sql_schema.sql] 请将这个 SQL 模式转换为一个优化的 Cosmos DB 数据模型。`
- **例 2**: `/cosmosdb-datamodeling 如何处理 SQL 中的多对多关系在 Cosmos DB 中的建模？`

### 4. 学习和培训 (Learning and Training)

- **用户故事**: 作为一名初级开发人员，我想学习如何在 Cosmos DB 中为不同的场景进行数据建模。
- **例 1**: `/cosmosdb-datamodeling 为一个物联网场景设计一个数据模型，其中包含设备遥测数据。`
- **例 2**: `/cosmosdb-datamodeling 解释一下在什么情况下应该使用嵌入而不是引用。`

## 原始文件

- [cosmosdb-datamodeling.prompt.md](../../prompts/cosmosdb-datamodeling.prompt.md)
