---
post_title: "task-planner.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "task-planner-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "task-planner"]
ai_note: "Generated with AI assistance."
summary: "任务规划器模式：以研究为前置、三文件输出（plan/details/prompt）、按模板与命名规范落地。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 在已验证研究的基础上，生成可执行的任务计划与细节文件，并产出实现提示文件供代理执行。

## When

- 任何实施前置环节：当研究文件已在 ./.copilot-tracking/research/ 下完备，且需要分解为可执行任务时。

## Why

- 以“研究→计划→实现”的链路降低返工，确保输出落在证据与项目规范之内，并具备可追溯性。

## How

- 先校验研究是否存在且完备；缺失则调用 task-researcher；随后在 ./.copilot-tracking/plans/、details/、prompts/ 下分别生成 3 个文件；严格模板、命名和行号引用；仅在这些目录写入。

## Key points (英文+中文对照)

- Research first, always.（研究优先且强制）
- Three files per task.（每个任务三文件）
- Accurate cross-references.（交叉引用准确）
- Template compliance.（严格模板合规）
- Minimal surface writes.（仅写入跟踪目录）

## 使用场景

### 1. 研究校验与兜底（Research validation & fallback）

- 用户故事：作为计划者，我需要在计划前强制校验研究，若缺失则自动触发研究模式。
- 例 1："检查 ./.copilot-tracking/research/ 是否存在当日 research 文件。"
- 例 2："若不满足模板字段，调用 task-researcher 更新研究。"
- 例 3："研究完备后再进入计划生成流程。"
- 例 4："将研究的关键发现引用到计划 ‘Research Summary’。"
- 例 5："把研究不足之处列为计划的依赖与风险。"

### 2. 计划清单生成（Plan checklist generation）

- 用户故事：作为执行者，我需要一个可勾选的阶段与任务清单，以及跨文件的行号引用。
- 例 1："在 plans 目录生成 YYYYMMDD-task-plan.instructions.md。"
- 例 2："每个任务附带 details 文件的行号引用。"
- 例 3："列出工具与前置条件依赖。"
- 例 4："标注可并行与互斥任务。"
- 例 5："输出成功标准可被脚本校验。"

### 3. 细节文件编制（Details authoring）

- 用户故事：作为工程师，我需要将每个任务的具体操作、文件路径与验证标准写入 details 文件。
- 例 1："在 details 目录生成 YYYYMMDD-task-details.md。"
- 例 2："把研究文件具体行段落映射到操作步骤。"
- 例 3："为每个步骤定义可验证的完成标准。"
- 例 4："列出需要修改/创建的文件路径。"
- 例 5："标注依赖关系与前置任务。"

### 4. 实现提示文件（Implementation prompt）

- 用户故事：作为自动化代理，我需要一个实现提示文件来指导逐步执行与阶段停靠。
- 例 1："在 prompts 目录生成 implement-*.prompt.md。"
- 例 2："添加阶段/任务停靠变量以支持逐步执行。"
- 例 3："加入清理步骤与变更摘要输出。"
- 例 4："提供计划与细节文件的链接便于跳转。"
- 例 5："实现完毕后尝试删除实现提示文件。"

### 5. 多任务并行与优先级（Parallel tasks & priority）

- 用户故事：作为项目经理，我希望对多任务按依赖排序，基础先行，避免阻塞。
- 例 1："按研究中的依赖关系排序计划。"
- 例 2："将基础设施/公共模块放在第一阶段。"
- 例 3："将特性任务并行化分配到不同执行代理。"
- 例 4："在清单中标注完成状态和日期。"
- 例 5："输出准备情况报告（Ready for Implementation）。"

## 原始文件

- chatmodes/task-planner.chatmode.md
