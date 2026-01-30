---
post_title: "create-readme.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-readme-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "documentation", "readme", "github"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Create README prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于根据项目信息自动生成结构化 `README.md` 文件的提示词。

## When

- 在创建新项目时。
- 当需要为现有项目改进或创建一个 `README` 文件时。
- 在希望标准化组织内所有项目的 `README` 格式时。

## Why

- 快速生成一个内容全面、格式清晰的 `README` 文件，为项目提供一个专业的门面。
- 确保 `README` 包含所有关键信息，如项目描述、安装指南、使用方法和贡献方式。
- 节省开发人员手动编写文档的时间。

## How

- 使用 `/create-readme` 命令并提供关于项目的一些基本信息（如项目名称、描述、使用的技术等）。
- AI 将根据你提供的信息和标准的 `README` 模板，生成一个完整的 Markdown 文件。
- 你可以审查、编辑并保存生成的 `README.md` 文件到你的项目根目录。

## Key points (英文+中文对照)

- README Generation (README 生成)
- Project Documentation (项目文档)
- Onboarding (新成员上手)
- Standardization (标准化)

## 使用场景

### 1. 新项目的快速启动 (Quick Start for New Projects)

- **用户故事**: 作为一名独立开发者，我刚刚创建了一个新的开源库，需要快速为它创建一个 `README` 文件。
- **例 1**: `/create-readme 我的项目是一个名为 'React-Easy-State' 的 React 状态管理库。请为它生成一个 README。`
- **例 2**: `/create-readme 为我的新 Python CLI 工具生成一个 README，它需要安装说明和基本用法示例。`

### 2. 改进现有项目的文档 (Improving Documentation for Existing Projects)

- **用户故事**: 作为一名项目维护者，我注意到我们项目的 `README` 文件已经过时且信息不全。我需要一个更好的版本。
- **例 1**: `/create-readme [selection=project_summary.txt] 根据这份项目摘要，为我们的项目重写 README，增加“功能”和“贡献指南”部分。`

### 3. 公司内部项目的标准化 (Standardizing Internal Company Projects)

- **用户故事**: 作为一名工程经理，我希望我们公司的所有内部项目都有一个统一的 `README` 格式，以便于内部共享和维护。
- **例 1**: `/create-readme 使用我们公司的标准 README 模板，为这个名为 'Internal-Auth-Service' 的项目生成文档。`

### 4. 为编程作业创建 README (Creating a README for a School Project)

- **用户故事**: 作为一名学生，我需要为我的计算机科学课程作业提交一个 `README` 文件，解释我的项目是如何工作的。
- **例 1**: `/create-readme 我的作业是一个用 Java 实现的排序算法可视化工具。请帮我创建一个 README，描述项目目标和如何运行它。`

## 原始文件

- [create-readme.prompt.md](../../prompts/create-readme.prompt.md)
