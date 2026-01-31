---
名称： 微软文档
描述：查询 Microsoft 官方文档以了解概念、查找教程并了解服务的工作原理。用于 Azure、.NET、Microsoft 365、Windows、Power Platform 和所有 Microsoft 技术。从 learn.microsoft.com 和其他 Microsoft 官方网站获取准确的最新信息 — 体系结构概述、快速入门、配置指南、限制和最佳实践。
兼容性：需要 Microsoft Learn MCP 服务器 (https://learn.microsoft.com/api/mcp)
---

# 微软文档

## 工具

|工具|用于 |
|------|---------|
| __代码0__ |查找文档——概念、指南、教程、配置 |
| __代码0__ |获取整页内容（当搜索摘录不够时）|

## 何时使用

- **理解概念** — “Cosmos DB 分区如何工作？”
- **学习服务** —“Azure Functions 概述”、“容器应用架构”
- **查找教程** —“快速入门”、“入门”、“分步”
- **配置选项** — “应用服务配置设置”
- **限制和配额** —“Azure OpenAI 速率限制”、“服务总线配额”
- **最佳实践** —“Azure 安全最佳实践”

## 查询有效性

好的查询是具体的：

```
# ❌ Too broad
"Azure Functions"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"Container Apps scaling rules KEDA"
```

包括上下文：
- **版本**（相关时）（`.NET 8`、`EF Core 8`）
- **任务意图**（`quickstart`、`tutorial`、`overview`、`limits`）
- **平台** 用于多平台文档（`Linux`、`Windows`）

## 何时获取整页

搜索后获取：
- **教程** — 需要完整的分步说明
- **配置指南** — 需要列出所有选项
- **深入研究** - 用户想要全面的覆盖范围
- **搜索摘录被截断** - 需要完整的上下文

## 为什么使用这个

- **准确性** - 实时文档，而不是可能过时的训练数据
- **完整性** — 教程包含所有步骤，而不是片段
- **权威** — Microsoft 官方文档
