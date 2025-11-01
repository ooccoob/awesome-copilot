---
post_title: "powershell.instructions.md Use Cases"
author1: "github-copilot"
post_slug: "powershell-instructions-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "powershell", "cmdlet-development", "scripting", "best-practices"]
ai_note: "Generated with AI assistance."
summary: "PowerShell cmdlet 开发指导原则的使用场景，包括命名约定、参数设计、管道处理、错误处理、文档编写和完整实现等核心功能和最佳实践"
post_date: "2025-10-27"
---

<!-- markdownlint-disable MD041 -->

## What

- 一套完整的 PowerShell cmdlet 开发指导规范，涵盖命名约定、参数设计、管道处理、错误处理、文档编写和安全机制等最佳实践

## When

- 开发 PowerShell 模块和 cmdlet 时
- 创建可重用的 PowerShell 脚本时
- 需要建立团队 PowerShell 开发标准时
- 进行 PowerShell 代码审查和优化时

## Why

- 确保生成的 PowerShell 代码符合微软官方标准
- 提高脚本的可读性、可维护性和可重用性
- 建立安全的脚本执行和错误处理机制
- 提升 cmdlet 的自动化友好性和管道兼容性

## How

- 遵循 PowerShell 官方的 Verb-Noun 命名约定
- 使用 PascalCase 进行命名，避免别名
- 实现完整的参数设计和类型验证
- 建立标准的管道输入输出机制
- 使用 ShouldProcess 和标准错误处理
- 提供完整的基于注释的帮助文档

## Key points (英文+中文对照)

- Verb-Noun Naming Conventions（动词-名词命名约定）
- Parameter Design and Validation（参数设计与验证）
- Pipeline Input and Output Handling（管道输入输出处理）
- Error Handling and Safety Mechanisms（错误处理与安全机制）
- Comment-Based Help Documentation（基于注释的帮助文档）

## 使用场景

### 1. 命名约定与代码风格规范

- 用户故事：作为 PowerShell 开发者，我需要遵循标准的命名约定和代码风格，确保生成的 cmdlet 具有一致性和可读性。
- 例 1："[提供函数概念] 请帮我创建一个符合 Verb-Noun 格式的函数名称，使用 PascalCase。"
- 例 2："[提供变量定义] 请帮我将变量名改为有意义的 PascalCase 命名。"
- 例 3："请帮我将代码中的别名替换为完整的 cmdlet 名称和参数。"
- 例 4："[提供现有脚本] 请帮我检查并修正代码是否符合 PowerShell 命名标准。"
- 例 5："请为我创建团队 PowerShell 命名约定的检查清单和工具。"

### 2. 参数设计与类型管理

- 用户故事：作为 cmdlet 设计者，我需要为函数设计清晰的参数，包含适当的类型验证和约束。
- 例 1："[提供函数需求] 请帮我设计参数列表，包含 Mandatory 和可选参数的标记。"
- 例 2："[提供参数类型需求] 请帮我使用 ValidateSet 为参数添加选项验证。"
- 例 3："请帮我将布尔标志转换为 [switch] 类型的参数。"
- 例 4："[提供复杂参数] 请帮我设计数组参数的验证和类型检查。"
- 例 5："请帮我为 cmdlet 添加参数别名和文档说明。"

### 3. 管道输入输出处理

- 用户故事：作为脚本开发者，我需要实现标准的管道支持，确保 cmdlet 能够与其他 PowerShell 命令流畅协作。
- 例 1："[提供函数需求] 请帮我实现 ValueFromPipeline 参数绑定。"
- 例 2："[提供对象处理需求] 请帮我添加 ValueFromPipelineByPropertyName 支持。"
- 例 3："请帮我实现 Begin/Process/End 块以支持管道流处理。"
- 例 4："[提供输出需求] 请帮我设计 PassThru 模式用于返回修改的对象。"
- 例 5："请帮我将格式化输出改为返回 PSCustomObject 对象。"

### 4. 错误处理与安全机制

- 用户故事：作为系统管理员，我需要建立安全的脚本执行机制，确保用户操作的安全性和可控性。
- 例 1："[提供系统修改需求] 请帮我为函数添加 SupportsShouldProcess 支持。"
- 例 2："[提供危险操作] 请帮我实现 ShouldProcess 确认机制和适当的 ConfirmImpact。"
- 例 3："请帮我使用 try/catch 块实现完整的错误处理。"
- 例 4："[提供错误场景] 请帮我创建有意义的错误消息和 ErrorRecord 对象。"
- 例 5："请帮我为函数添加适当的 Write-Verbose、Write-Warning 和 Write-Error。"

### 5. 文档编写与代码注释

- 用户故事：作为技术文档作者，我需要为 PowerShell 函数创建完整的基于注释的帮助文档。
- 例 1："[提供函数实现] 请帮我添加完整的基于注释的帮助，包含 .SYNOPSIS 和 .DESCRIPTION。"
- 例 2："[提供函数参数] 请帮我为每个参数添加 .PARAMETER 说明。"
- 例 3："请帮我为函数添加 .EXAMPLE 节，展示实际使用场景。"
- 例 4："[提供输出类型] 请帮我添加 .OUTPUTS 节说明返回对象类型。"
- 例 5："请帮我创建函数的 .NOTES 节和相关的使用注意事项。"

### 6. 完整 cmdlet 实现与优化

- 用户故事：作为高级 PowerShell 开发者，我需要创建完整的、生产就绪的 cmdlet 实现，包含所有标准特性。
- 例 1："[提供业务需求] 请帮我创建一个完整的 cmdlet，实现 Get/Set/New/Remove 模式。"
- 例 2："[提供现有实现] 请帮我将脚本重构为符合高级函数标准的格式。"
- 例 3："请帮我为 cmdlet 添加完整的验证、错误处理和文档。"
- 例 4："[提供模块需求] 请帮我创建符合模块标准的 PowerShell 脚本文件。"
- 例 5："请帮我优化现有代码以提升性能和可维护性。"

## 原始文件

- [powershell.instructions.md](../../instructions/powershell.instructions.md)
