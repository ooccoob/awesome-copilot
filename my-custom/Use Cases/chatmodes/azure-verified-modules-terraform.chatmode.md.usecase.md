---
post_title: "azure-verified-modules-terraform.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "azure-verified-modules-terraform-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","azure","terraform","modules"]
ai_note: "Generated with AI assistance."
summary: "使用 Terraform 管理 Azure Verified Modules 的实践：提供模块治理、状态管理与工作流示例。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 展示如何采用 Terraform 管理与消费 Azure Verified Modules，并处理状态、远程后端与模块重用的挑战。

## When

- 企业采用 Terraform 作为 IaC 工具并希望复用验证模块时使用。

## Why

- 保证模块版本兼容、状态一致性与团队协作效率。

## How

- 包含模块封装、依赖管理、远程状态后端（Storage Account/Consul）与构建管道示例。

## Key points (英文+中文对照)

- Remote state（远程状态）
- Module registry（模块注册）
- Drift detection（漂移检测）
- Policy as Code（策略即代码）
- Workspace strategy（工作区策略）

## 使用场景

### 1. 模块注册与消费

- 用户故事：作为 DevOps，我要在 terraform registry 中管理共享模块并保证向后兼容。
- 例 1：模块版本化与依赖声明示例。
- 例 2：迁移远程状态到新的后端示例。
- 例 3：模块审计与策略检查流水线。
- 例 4：多团队共享模块的权限治理示例。
- 例 5：模块回滚与回退策略示例。

## 原始文件

- [chatmodes/azure-verified-modules-terraform.chatmode.md](../../../chatmodes/azure-verified-modules-terraform.chatmode.md)
