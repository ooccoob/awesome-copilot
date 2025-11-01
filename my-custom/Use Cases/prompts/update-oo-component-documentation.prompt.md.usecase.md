---
post_title: "update-oo-component-documentation.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "update-oo-component-documentation-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "documentation", "object-oriented", "refactoring"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Update Object-Oriented Component Documentation prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于在面向对象（Object-Oriented, OO）组件的代码发生变化后，智能地更新其对应文档的提示词。

## When

- 在重构代码，例如更改了方法签名（参数、返回类型）之后。
- 当为现有类添加了新方法或属性时。
- 在修改了方法的内部实现，导致其行为或目的发生变化时。

## Why

- 确保代码和文档之间的同步，防止文档过时。
- 自动化更新文档的过程，减少开发人员在重构后手动修改注释的负担。
- 维护高质量、准确的文档，这对于团队协作和代码库的长期健康至关重要。

## How

- 使用 `/update-oo-component-documentation` 命令，并提供被修改的 OO 组件的代码（包括其旧的文档注释）。
- AI 将：
    1. 比较代码的当前状态和其文档注释。
    2. 识别出不一致的地方（例如，文档中的参数名与代码中的不匹配）。
    3. 分析代码的变更，理解其新的行为或签名。
    4. 生成更新后的文档注释，以准确反映代码的当前状态。

## Key points (英文+中文对照)

- Documentation Sync (文档同步)
- Refactoring Support (重构支持)
- Code-Doc Consistency (代码与文档一致性)
- Maintenance Automation (维护自动化)

## 使用场景

### 1. 方法签名变更后更新文档 (Updating Docs After Method Signature Change)

- **用户故事**: 作为一名 Java 开发人员，我将一个 `findUser(String name)` 方法重构为了 `findUser(String firstName, String lastName)`。我需要更新它的 Javadoc。
- **例 1**: `/update-oo-component-documentation [selection=UserService.java] 我修改了 `findUser` 方法的签名。请分析新的签名并更新其 Javadoc，特别是 `@param` 标签。`

### 2. 为新添加的方法生成文档 (Generating Docs for a New Method)

- **用户故事**: 作为一名 Python 开发者，我为一个现有的 `DataProcessor` 类添加了一个新的公共方法 `export_to_csv`。我需要为这个新方法添加文档字符串（docstring）。
- **例 1**: `/update-oo-component-documentation [selection=DataProcessor.py] 我在这个类里添加了 `export_to_csv` 方法。请为它生成一个符合 Google 风格的 docstring，并将其插入到现有文档中。`

### 3. 在方法逻辑改变后重写文档 (Rewriting Docs After Logic Change)

- **用户故事**: 作为一名 C# 工程师，我重写了一个 `CalculatePrice` 方法的实现，它现在会考虑会员折扣。我需要更新它的 XML 文档注释来反映这个新的业务逻辑。
- **例 1**: `/update-oo-component-documentation [selection=PriceCalculator.cs] `CalculatePrice` 方法的逻辑已经改变，现在它会应用会员折扣。请更新它的文档摘要（`<summary>`)，以解释这个新行为。`

### 4. 保持接口和实现类的文档同步 (Keeping Docs for Interface and Implementation in Sync)

- **用户故事**: 作为一名团队负责人，我更新了一个 `IRepository` 接口，添加了一个新方法。我需要确保所有实现这个接口的类都更新了它们的文档。
- **例 1**: `/update-oo-component-documentation [selection=SqlRepository.cs] `IRepository` 接口已经更新。请检查 `SqlRepository` 类，并为新实现的接口方法生成文档。`

## 原始文件

- [update-oo-component-documentation.prompt.md](../../prompts/update-oo-component-documentation.prompt.md)
