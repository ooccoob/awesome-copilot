---
post_title: "create-agentsmd.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-agentsmd-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "agent-documentation"]
ai_note: "Generated with AI assistance."
summary: "Use cases for generating actionable AGENTS.md files that equip AI agents with project-specific workflows and standards." 
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 生成位于仓库根目录的 `AGENTS.md`，提供 AI 代理快速上手所需的技术背景、命令与流程。

## When

- 项目需要为 Copilot、Cursor 等代理提供详细运行指南。
- README.md 面向人类读者，需额外编写 agent 专用文档。
- 多团队协作、上线交接或开源发布前。

## Why

- 降低 AI 代理进入项目的学习成本。
- 确保自动化工具遵循实际工作流与安全约束。
- 提供标准化的命令、测试、部署与调试指引。

## How

- 分析项目结构、脚本、CI/CD 与依赖，提炼可执行命令。
- 组织成项目概述、安装、开发、测试、代码风格、构建部署等章节。
- 可根据需要增加安全、Monorepo、PR、故障排查等扩展内容。

## Key points (英文+中文对照)

- Agent-centric documentation（面向代理的文档）
- Actionable workflows and commands（可执行的工作流与命令）
- Architecture and tooling clarity（架构与工具说明）
- Testing and quality alignment（测试与质量对齐）
- Security and governance awareness（安全与治理意识）

## 使用场景

**文件名:取源文件相对路径，然后读取文件名，不包含 .prompt.md，例如 my-custom\\my-prompt\\my-api-create.prompt.md 生成的文件名为 my-api-create**

### 1. 新项目初始化（Project Kickoff）

- 用户故事：作为技术负责人，我要为新仓库创建 AGENTS.md，让代理了解全流程。
- 例 1："/create-agentsmd [selection=repo-root] 生成包含安装、启动、测试命令的 AGENTS.md。"
- 例 2："/create-agentsmd 强调关键框架版本与配置文件位置。"
- 例 3："/create-agentsmd 加入环境变量与 secrets 管理方式。"
- 例 4："/create-agentsmd 说明构建、部署、CI/CD 步骤。"
- 例 5："/create-agentsmd 提供常见问题和调试技巧。"

### 2. Monorepo 指南建设（Monorepo Navigation）

- 用户故事：作为平台团队，我要帮助代理在 Monorepo 中快速定位包与命令。
- 例 1："/create-agentsmd 描述 packages 子目录的结构与跨包依赖。"
- 例 2："/create-agentsmd 列出特定包的安装、构建、测试命令。"
- 例 3："/create-agentsmd 指出如何使用脚本或工具在包之间跳转。"
- 例 4："/create-agentsmd 说明 turbo/nx 等任务调度器的用法。"
- 例 5："/create-agentsmd 提供子项目 AGENTS.md 的链接与定位策略。"

### 3. 外部协作与交接（External Collaboration）

- 用户故事：作为项目经理，我要把项目交给外包团队并保证他们跟随既定流程。
- 例 1："/create-agentsmd 记录 PR 流程、标题格式与必跑命令。"
- 例 2："/create-agentsmd 提醒所有提交需通过 Lint、测试与安全扫描。"
- 例 3："/create-agentsmd 写明代码风格与命名规范。"
- 例 4："/create-agentsmd 说明敏感信息与配置文件处理方式。"
- 例 5："/create-agentsmd 指出沟通渠道及变更审批流程。"

### 4. 运维与部署自动化（Ops & Deployment Enablement）

- 用户故事：作为 DevOps，我要让代理掌握部署流水线与应急操作。
- 例 1："/create-agentsmd 汇总打包命令、构建输出位置与环境要求。"
- 例 2："/create-agentsmd 描述 CI/CD workflow 触发条件与必备变量。"
- 例 3："/create-agentsmd 提供 rollback、热修复与监控指引。"
- 例 4："/create-agentsmd 记录部署前后验证步骤。"
- 例 5："/create-agentsmd 列出日志、调试与性能优化策略。"

### 5. 安全与合规（Security & Compliance）

- 用户故事：作为安全负责人，我要确保代理遵守安全策略与审计要求。
- 例 1："/create-agentsmd 标注 secrets 管理、凭证轮换与禁止提交项。"
- 例 2："/create-agentsmd 说明安全测试命令、依赖扫描和报告提交流程。"
- 例 3："/create-agentsmd 描述账户权限、审核与审批链。"
- 例 4："/create-agentsmd 写明处理敏感数据的流程与注意事项。"
- 例 5："/create-agentsmd 提供合规检查清单与监管要求链接。"

### 6. 教学与知识共享（Education & Enablement）

- 用户故事：作为文档负责人，我要把 AGENTS.md 作为教学资料，帮助团队了解项目全貌。
- 例 1："/create-agentsmd 梳理项目目标、模块拆分与关键架构图。"
- 例 2："/create-agentsmd 在各章节添加 WHY/注意事项，帮助理解。"
- 例 3："/create-agentsmd 提供常见工作流（如添加新模块、修复 bug）。"
- 例 4："/create-agentsmd 链接 README、设计文档、API 规范。"
- 例 5："/create-agentsmd 记录学习资源与内部工具指南。"

## 原始文件

- [create-agentsmd.prompt.md](../../prompts/create-agentsmd.prompt.md)
