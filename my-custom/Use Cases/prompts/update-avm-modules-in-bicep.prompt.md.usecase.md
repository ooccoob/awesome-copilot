---
post_title: "update-avm-modules-in-bicep.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "update-avm-modules-in-bicep-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "azure", "bicep", "avm", "iac"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Update AVM Modules in Bicep prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于在 Bicep 文件中自动检查和更新 Azure Verified Modules (AVM) 引用的提示词。

## When

- 在维护使用 Bicep 编写的基础设施即代码 (IaC) 时。
- 当需要确保你的 Bicep 模块引用的是最新、最安全的 AVM 版本时。
- 在进行定期的依赖项更新和安全扫描时。

## Why

- 自动化检查和更新 AVM 模块版本的过程，节省手动查找和替换的时间。
- 帮助你的基础设施代码跟上 AVM 的最新功能和安全修复。
- 减少因使用过时模块而可能引入的配置错误或安全漏洞。

## How

- 使用 `/update-avm-modules-in-bicep` 命令，并可以指定要检查的 Bicep 文件。
- AI 将：
    1. 扫描指定的 Bicep 文件，找出所有引用 AVM 的 `module` 声明。
    2. 检查每个引用的模块版本。
    3. 查询 AVM 的模块注册表（如 Bicep Public Registry）以获取最新版本。
    4. 如果发现有可用的新版本，它会建议更新，并可以自动应用更改。

## Key points (英文+中文对照)

- Dependency Management (依赖管理)
- Infrastructure as Code (IaC, 基础设施即代码)
- Version Update (版本更新)
- Azure Verified Modules (AVM, Azure 验证模块)

## 使用场景

### 1. 定期更新项目中的所有 AVM 模块 (Regularly Updating All AVM Modules in a Project)

- **用户故事**: 作为一名 DevOps 工程师，我希望每周检查一次我们项目中所有的 Bicep 文件，并更新所有 AVM 模块到最新版本。
- **例 1**: `/update-avm-modules-in-bicep 检查当前工作区中所有 `.bicep` 文件的 AVM 模块引用，并更新到最新版本。`
- **例 2**: `/update-avm-modules-in-bicep [selection=main.bicep] 只更新这个 `main.bicep` 文件中的模块。`

### 2. 检查特定模块的更新 (Checking for Updates to a Specific Module)

- **用户故事**: 作为一名云工程师，我听说 AVM 的 `network/virtual-network` 模块最近有一次重要的安全更新，我需要检查我的项目是否正在使用最新版本。
- **例 1**: `/update-avm-modules-in-bicep 检查我的项目中所有对 `br/public:avm/res/network/virtual-network` 模块的引用，并告诉我是否有可用的更新。`

### 3. 在 CI/CD 流水线中集成更新检查 (Integrating Update Checks into a CI/CD Pipeline)

- **用户故事**: 作为一名平台工程师，我希望在我们的 CI 流水线中添加一个步骤，如果发现有任何过时的 AVM 模块，就让构建失败。
- **例 1**: `/update-avm-modules-in-bicep 创建一个脚本，用于在 CI 环境中检查 AVM 模块更新。如果存在过时模块，则以非零状态码退出。` (提示词可以生成这个检查脚本)

### 4. 了解新版本的变更内容 (Understanding Changes in a New Version)

- **用户故事**: 作为一名谨慎的开发人员，在更新一个主要的 AVM 模块版本之前，我希望了解新版本有哪些重大变更（breaking changes）。
- **例 1**: `/update-avm-modules-in-bicep `storage/storage-account` 模块有一个新的主版本更新。请告诉我从 v1.x 更新到 v2.0 有哪些主要变化和需要注意的事项。`

## 原始文件

- [update-avm-modules-in-bicep.prompt.md](../../prompts/update-avm-modules-in-bicep.prompt.md)
