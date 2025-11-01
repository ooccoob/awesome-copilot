---
post_title: "comment-code-generate-a-tutorial.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "comment-code-generate-a-tutorial-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "documentation"]
ai_note: "Generated with AI assistance."
summary: "Use cases for refactoring Python scripts with instructional comments and producing full README tutorials." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 将 Python 脚本重构为遵循 PEP 8 的教学项目，补充解释性注释并生成完整 README 教程。

## When

- 希望把原型脚本升级成面向初学者的学习资源。
- 准备分享代码给新人或社区，需要结构化说明文档。
- 对现有脚本进行重构与知识传承。

## Why

- 提升代码可读性与教学价值，降低学习门槛。
- 统一风格与命名，确保规范可复用。
- 通过 README 提供背景、运行步骤与示例，加速 onboarding。

## How

- 按 PEP 8 重构代码，重命名模糊变量或函数。
- 添加面向新手的注释，强调“为什么”与逻辑目的。
- 生成 README，覆盖项目简介、环境配置、运行方法、代码解析、示例用法与输出。

## Key points (英文+中文对照)

- Beginner-centric refactoring（面向初学者的重构）
- Instructional commenting style（教学型注释风格）
- PEP 8 compliance（遵循 PEP 8 规范）
- Tutorial README generation（生成教程式 README）
- Code clarity and pedagogy（兼顾清晰性与教学性）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. 内部培训脚本整理（Internal Training Upgrade）

- 用户故事：作为团队导师，我要将粗糙的工具脚本打磨成新人培训资料。
- 例 1："/comment-code-generate-a-tutorial 重构 `tools/data_cleaner.py` 并输出教学 README。"
- 例 2："/comment-code-generate-a-tutorial 增加解释性注释，说明每步数据处理的原因。"
- 例 3："/comment-code-generate-a-tutorial 在 README 中加入运行前提与依赖安装。"
- 例 4："/comment-code-generate-a-tutorial 展示典型输入输出示例帮助理解。"
- 例 5："/comment-code-generate-a-tutorial 通过示例强调常见错误与注意事项。"

### 2. 开源项目文档化（Open Source Polishing）

- 用户故事：作为开源维护者，我要提升项目可读性，吸引初学者参与。
- 例 1："/comment-code-generate-a-tutorial 对 `scripts/cli_tool.py` 做 PEP 8 重构与注释。"
- 例 2："/comment-code-generate-a-tutorial 在 README 写明贡献指南与示例。"
- 例 3："/comment-code-generate-a-tutorial 解释关键算法的设计思路。"
- 例 4："/comment-code-generate-a-tutorial 补充可选的 Sample Output 帮助验证运行结果。"
- 例 5："/comment-code-generate-a-tutorial 标注如何扩展脚本功能的建议。"

### 3. 数据科学教程制作（Data Science Tutorial）

- 用户故事：作为数据科学家，我要把分析脚本制作成教学材料给社区分享。
- 例 1："/comment-code-generate-a-tutorial 重构 `notebooks/export_to_script.py` 并解释每个步骤。"
- 例 2："/comment-code-generate-a-tutorial 在 README 中细分‘How It Works’解释数据管线。"
- 例 3："/comment-code-generate-a-tutorial 引导读者如何使用示例数据运行脚本。"
- 例 4："/comment-code-generate-a-tutorial 标出常见参数调整方法与效果。"
- 例 5："/comment-code-generate-a-tutorial 提供图表/输出截图的占位说明。"

### 4. 黑客松/比赛提交、展示优化（Hackathon Submission）

- 用户故事：作为参赛者，我要让评委快速理解项目逻辑与使用方式。
- 例 1："/comment-code-generate-a-tutorial 优化 hackathon 脚本结构并补充注释。"
- 例 2："/comment-code-generate-a-tutorial README 中写清安装、运行和展示流程。"
- 例 3："/comment-code-generate-a-tutorial 描述脚本的价值点与亮点代码。"
- 例 4："/comment-code-generate-a-tutorial 准备示例场景和测试数据说明。"
- 例 5："/comment-code-generate-a-tutorial 提醒评委如何复现并验证结果。"

### 5. 客户成功/支持团队交接（Customer Success Handoff）

- 用户故事：作为支持工程师，我要把自动化脚本整理成易懂文档，方便客户使用。
- 例 1："/comment-code-generate-a-tutorial 为客户部署脚本添加注释和操作指南。"
- 例 2："/comment-code-generate-a-tutorial README 中列出常见问题与 FAQ。"
- 例 3："/comment-code-generate-a-tutorial 强调敏感配置的处理方式与安全注意事项。"
- 例 4："/comment-code-generate-a-tutorial 加入示例命令行参数说明。"
- 例 5："/comment-code-generate-a-tutorial 指导客户如何自定义脚本功能。"

### 6. 教学课程素材制作（Course Material Creation）

- 用户故事：作为讲师，我要提供分步教程帮助学生理解 Python 实践。
- 例 1："/comment-code-generate-a-tutorial 将课堂案例脚本整理成教学版本。"
- 例 2："/comment-code-generate-a-tutorial 给出每个函数的教学注释与练习提示。"
- 例 3："/comment-code-generate-a-tutorial README 里安排教学目标与扩展任务。"
- 例 4："/comment-code-generate-a-tutorial 提供示例输出和验证方法。"
- 例 5："/comment-code-generate-a-tutorial 增加课程所需依赖和环境准备说明。"

## 原始文件

- [comment-code-generate-a-tutorial.prompt.md](../../prompts/comment-code-generate-a-tutorial.prompt.md)
