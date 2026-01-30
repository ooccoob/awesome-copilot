---
post_title: "clojure-add-to-memory.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "clojure-add-to-memory-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "knowledge-management"]
ai_note: "Generated with AI assistance."
summary: "Use cases for updating Clojure memory instructions with lessons learned, gotchas, and best practices." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 将近期的错误、经验转化为 `clojure-memory.instructions.md` 中的可执行指南与示例。

## When

- 遇到 Clojure 项目中的错误、惯用法失误或 REPL 体验问题，需要固化成记忆。
- 希望持续完善团队的 Clojure AI 协作说明与避坑指南。

## Why

- 避免重复踩坑，提升后续 AI/开发者的工作效率与准确性。
- 维持规范化的知识库，强化数据/函数式思维方式。

## How

- 读取 `clojure-memory.instructions.md`，理解当前结构与内容。
- 分类错误/经验（常见坑、增强、最佳实践、流程改进），补充 ❌/✅ 示例与原因。
- 保持条目简洁、可执行，必要时新增章节或优化排序。

## Key points (英文+中文对照)

- Continuous memory curation（持续维护记忆）
- Mistake-to-guideline conversion（将错误转换为指南）
- Actionable code examples（提供可执行代码示例）
- Structured knowledge organization（结构化组织知识）
- Functional mindset reinforcement（强化函数式思维）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. 新发现的常见错误记录（Gotcha Capture）

- 用户故事：作为 Clojure 教练，我要把刚发生的括号错误整理到记忆文档中，提醒后续 AI 避免。
- 例 1："/clojure-add-to-memory 总结今天遇到的 `(def foo { :a 1 :b 2 )` 括号不匹配问题，并给出正确示例。"
- 例 2："/clojure-add-to-memory 记录 namespace 命名大小写错误的 ❌/✅ 示例。"
- 例 3："/clojure-add-to-memory 添加 REPL 使用中的 load-file 与 evaluate 区别。"
- 例 4："/clojure-add-to-memory 补充常见 destructuring 误用与正确写法。"
- 例 5："/clojure-add-to-memory 将 map/list 区分错误归类为“常见坑”。"

### 2. 现有章节增强（Section Enhancement）

- 用户故事：作为维护者，我要扩展现有“文件编辑”章节，纳入新的流程改进建议。
- 例 1："/clojure-add-to-memory 为现有文件操作章节补充 VS Code 使用注意事项。"
- 例 2："/clojure-add-to-memory 添加关于 use/require 差异的解释与示例。"
- 例 3："/clojure-add-to-memory 更新 lint/build 流程中的提示与工具链。"
- 例 4："/clojure-add-to-memory 增加测试命名约定的提醒。"
- 例 5："/clojure-add-to-memory 强调保存后运行 `lein test` 的流程。"

### 3. 新增最佳实践条目（Best Practice Addition）

- 用户故事：作为团队成员，我要把项目中总结的高频实用技巧写入记忆，便于复用。
- 例 1："/clojure-add-to-memory 总结线程宏 `->` 与 `->>` 的选择心得。"
- 例 2："/clojure-add-to-memory 添加数据驱动测试的示例与建议。"
- 例 3："/clojure-add-to-memory 记录不可变数据结构操作的推荐模式。"
- 例 4："/clojure-add-to-memory 写入配置管理与环境变量处理经验。"
- 例 5："/clojure-add-to-memory 总结 transducer 的性能优化场景。"

### 4. 流程改进与回顾（Process Improvement）

- 用户故事：作为流程负责人，我要记录每次事故复盘的改进措施，保持记忆同步。
- 例 1："/clojure-add-to-memory 记录部署事故复盘中的改进步骤。"
- 例 2："/clojure-add-to-memory 添加 pre-commit 检查清单的执行建议。"
- 例 3："/clojure-add-to-memory 将 pair-programming 问题转为流程提醒。"
- 例 4："/clojure-add-to-memory 记录代码评审中的常见指摘点。"
- 例 5："/clojure-add-to-memory 添加自动化测试缺失导致回滚的教训与预防。"

### 5. 新成员培训资料（Onboarding Aid）

- 用户故事：作为团队导师，我要把常见问题整理进记忆文档，帮助新人快速上手。
- 例 1："/clojure-add-to-memory 整理入门常见 pitfall 与示例。"
- 例 2："/clojure-add-to-memory 记录 REPL 驱动开发的最佳流程。"
- 例 3："/clojure-add-to-memory 添加常用项目脚本与命令的说明。"
- 例 4："/clojure-add-to-memory 提供命名与文件结构规范。"
- 例 5："/clojure-add-to-memory 说明如何定位常见异常栈与处理方式。"

### 6. 指令模板与升级（Instruction Template Evolution）

- 用户故事：作为知识库管理员，我要定期重构指令模板，使内容清晰可维护。
- 例 1："/clojure-add-to-memory 重新组织章节标题与排序。"
- 例 2："/clojure-add-to-memory 为每条指导加入 WHY 说明。"
- 例 3："/clojure-add-to-memory 补充目录、索引与跳转链接。"
- 例 4："/clojure-add-to-memory 更新表格/代码块格式，提高可读性。"
- 例 5："/clojure-add-to-memory 将旧内容标记为 deprecated 并说明替代方案。"

## 原始文件

- [clojure-add-to-memory.prompt.md](../../prompts/clojure-add-to-memory.prompt.md)
