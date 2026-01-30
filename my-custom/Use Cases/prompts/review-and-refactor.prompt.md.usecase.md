---
post_title: "review-and-refactor.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "review-and-refactor-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "code-review", "refactoring", "code-quality"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Review and Refactor prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于自动审查和重构代码的提示词，旨在提高代码质量、可读性和性能。

## When

- 在编写完一段代码后，希望对其进行改进时。
- 在进行代码审查（Code Review）时，需要一个“AI 审查员”提供初步反馈。
- 当接手一个旧的或复杂的代码库，并希望逐步改善它时。

## Why

- 自动识别代码中的“坏味道”（code smells），如重复代码、过长的方法、复杂的条件逻辑等。
- 提供具体的、可操作的重构建议，并能直接生成重构后的代码。
- 帮助开发者学习和应用编码最佳实践和设计模式。

## How

- 使用 `/review-and-refactor` 命令并选中你想要审查和重构的代码。
- AI 将分析代码，并从以下几个方面提出改进建议：
    - **可读性**: 改进变量命名，简化逻辑。
    - **性能**: 识别低效的算法或操作。
    - **可维护性**: 提取方法，减少重复。
    - **最佳实践**: 应用语言或框架的最佳实践。
- AI 会提供一份审查报告，并给出重构后的代码版本供你选择。

## Key points (英文+中文对照)

- Code Review (代码审查)
- Refactoring (重构)
- Code Quality (代码质量)
- Best Practices (最佳实践)

## 使用场景

### 1. 改进一个复杂的函数 (Improving a Complex Function)

- **用户故事**: 作为一名开发人员，我写了一个非常长的函数，里面有多个嵌套的 `if-else` 语句。我想让它变得更清晰、更易于维护。
- **例 1**: `/review-and-refactor [selection=my_complex_function.js] 审查并重构这个函数。尝试使用策略模式或提取方法来简化它。`
- **例 2**: `/review-and-refactor [selection=my_complex_function.js] 这个函数的圈复杂度太高了，请帮我降低它。`

### 2. 优化性能敏感的代码 (Optimizing Performance-Sensitive Code)

- **用户故事**: 作为一名游戏开发者，我的一段渲染循环代码运行得很慢，影响了游戏的帧率。
- **例 1**: `/review-and-refactor [selection=render_loop.cpp] 审查这段 C++ 代码的性能。检查是否存在不必要的内存分配或低效的循环。`
- **例 2**: `/review-and-refactor [selection=data_processing.py] 这个 Python 脚本处理大量数据时非常慢，请帮我找到瓶颈并进行优化，比如使用 NumPy 或并行处理。`

### 3. 现代化遗留代码 (Modernizing Legacy Code)

- **用户故事**: 作为一名维护工程师，我正在处理一个使用旧版 Java 编写的项目。我想将一些代码更新为使用 Java 8+ 的特性，如 Streams 和 Lambdas。
- **例 1**: `/review-and-refactor [selection=old_java_code.java] 将这个使用 for 循环和匿名内部类的代码重构为使用 Java Stream API。`

### 4. 作为自动化的代码审查者 (As an Automated Code Reviewer)

- **用户故事**: 作为一名技术负责人，我希望在团队成员提交 PR 之前，能有一个工具帮助他们发现并修复一些基本问题。
- **例 1**: `/review-and-refactor [selection=entire_file.ts] 对这个文件进行一次完整的代码审查，检查是否遵循了我们团队的编码规范。`

## 原始文件

- [review-and-refactor.prompt.md](../../prompts/review-and-refactor.prompt.md)
