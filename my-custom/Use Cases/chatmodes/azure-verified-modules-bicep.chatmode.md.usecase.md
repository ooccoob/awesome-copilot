---
post_title: "azure-verified-modules-bicep.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "azure-verified-modules-bicep-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","azure","bicep","modules"]
ai_note: "Generated with AI assistance."
summary: "使用 Azure Verified Modules (Bicep) 的模块化基础设施示例与治理实践。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 演示如何在 Bicep 中使用并扩展 Azure Verified Modules，包含版本管理、合规性与引用策略。

## When

- 构建标准化、可复用的 IaC 组件库并在企业范围内共享时使用。

## Why

- 通过模块化与版本化减少重复工作并保证部署一致性与合规。

## How

- 提供模块引用、参数策略、模块测试与本地开发验证示例。

## Key points (英文+中文对照)

- Module versioning（模块版本管理）
- Parameter contract（参数契约）
- Compliance checks（合规检查）
- Local testing（本地测试）
- Module composition（模块组装）

## 使用场景

### 1. 模块封装与重用

- 用户故事：作为平台工程师，我要把常用网络/存储资源封装成可复用模块。
- 例 1：创建模块模板并在多个项目中引用。
- 例 2：模块兼容性测试与版本回滚示例。
- 例 3：模块文档与参数约束示例。
- 例 4：通过管道自动发布模块到企业 registry。
- 例 5：模块签名与信任策略示例。

## 原始文件

- [chatmodes/azure-verified-modules-bicep.chatmode.md](../../../chatmodes/azure-verified-modules-bicep.chatmode.md)
