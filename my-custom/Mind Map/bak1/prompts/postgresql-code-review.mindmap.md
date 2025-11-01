# PostgreSQL Code Review Assistant - 思维导图

## 📋 文档摘要

**功能定位**：专注于 PostgreSQL 独有的最佳实践、反模式和质量标准的代码审查助手。

**适用场景**：需要对 PostgreSQL 相关 SQL、Schema、函数、扩展、安全等进行专项审查时。

**核心价值**：提升 JSONB、数组、自定义类型、分区、RLS 等特性利用率，避免常见性能与安全陷阱。

**使用指南**：结合清单和反模式，逐项检查代码是否充分利用 PostgreSQL 独特能力。

## 🎯 实际使用说明示例问题

- 如何优化 JSONB 查询和索引？
- 如何利用 GIN/GiST 索引提升数组/JSONB 性能？
- 如何设计自定义类型和约束？
- 如何实现行级安全（RLS）？
- 如何避免常见的 PostgreSQL 性能反模式？

## 📊 结构化要点(中英文对照)

- JSONB Best Practices (JSONB 最佳实践)
- Array Operations (数组操作)
- Schema Design (模式设计)
- Custom Types & Domains (自定义类型与域)
- Anti-Patterns (反模式)
- Extension Usage (扩展使用)
- Security & RLS (安全与行级安全)
- Code Quality Checklist (代码质量清单)

## 🗺️ 思维导图格式

- PostgreSQL 代码审查
  - JSONB 最佳实践
  - 数组操作
  - 模式设计
  - 自定义类型与域
  - 反模式
  - 扩展使用
  - 安全与 RLS
  - 代码质量清单

---
**源文件**: d:\mycode\awesome-copilot\prompts\postgresql-code-review.prompt.md
**生成时间**: 2025-10-17T00:00:00+08:00
