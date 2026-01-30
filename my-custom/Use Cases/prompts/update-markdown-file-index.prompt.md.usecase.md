---
post_title: "update-markdown-file-index.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "update-markdown-file-index-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "markdown", "documentation", "automation", "indexing"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Update Markdown File Index prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于自动扫描指定目录下的 Markdown 文件，并生成或更新一个索引文件（如 `README.md` 或 `SUMMARY.md`）的提示词。

## When

- 在维护一个包含许多 Markdown 文件的文档项目、知识库或个人笔记时。
- 当添加、删除或重命名文件后，需要更新目录或导航文件时。
- 在使用 MkDocs, GitBook, VuePress 等静态网站生成器时，需要保持 `SUMMARY.md` 文件同步。

## Why

- 自动化创建和维护索引文件的过程，避免手动操作的遗漏和错误。
- 确保文档的导航结构始终与文件系统的实际结构保持一致。
- 提高大型文档项目的可维护性。

## How

- 使用 `/update-markdown-file-index` 命令，并可以指定要扫描的目录和要更新的索引文件。
- AI 将：
    1. 递归地扫描指定目录下的所有 `.md` 文件。
    2. 提取每个文件的标题（通常是文件内的第一个 H1 标题）。
    3. 按照文件系统的层级结构，生成一个格式化的 Markdown 列表。
    4. 将这个列表插入或更新到指定的索引文件中。

## Key points (英文+中文对照)

- Index Generation (索引生成)
- Documentation Automation (文档自动化)
- Table of Contents (目录)
- File System Sync (文件系统同步)

## 使用场景

### 1. 为项目文档生成 `README.md` 目录 (Generating a README.md Index for Project Docs)

- **用户故事**: 作为一名开源项目维护者，我希望在我的 `docs` 目录下的 `README.md` 文件中，有一个能自动更新的、指向所有文档页面的链接列表。
- **例 1**: `/update-markdown-file-index 扫描 `docs` 目录，并在 `docs/README.md` 中生成一个文件索引。`

### 2. 维护 MkDocs 的 `SUMMARY.md` (Maintaining `SUMMARY.md` for MkDocs)

- **用户故事**: 作为一名技术作家，我使用 MkDocs 来构建我们的产品文档。我每次添加新页面时，都必须手动更新 `SUMMARY.md` 文件，这很繁琐。
- **例 1**: `/update-markdown-file-index 扫描 `docs` 目录下的所有 Markdown 文件，并更新根目录下的 `SUMMARY.md` 文件，以匹配 MkDocs 的格式。`

### 3. 创建个人知识库的索引 (Creating an Index for a Personal Knowledge Base)

- **用户故事**: 作为一名学生，我用一个文件夹来存放我所有的 Markdown 学习笔记。我希望有一个主文件能让我快速导航到任何一篇笔记。
- **例 1**: `/update-markdown-file-index 扫描我的 `MyNotes` 文件夹，并在 `MyNotes/Index.md` 中创建一个按子文件夹组织的笔记索引。`

### 4. 自动更新博客文章列表 (Auto-updating a Blog Post List)

- **用户故事**: 作为一名博主，我将我的每篇博客文章都保存为一个 Markdown 文件。我希望我的主页上能有一个自动更新的文章列表。
- **例 1**: `/update-markdown-file-index 扫描 `_posts` 目录，并在 `index.md` 中生成一个按文件名（日期）倒序排列的文章列表。`

## 原始文件

- [update-markdown-file-index.prompt.md](../../prompts/update-markdown-file-index.prompt.md)
