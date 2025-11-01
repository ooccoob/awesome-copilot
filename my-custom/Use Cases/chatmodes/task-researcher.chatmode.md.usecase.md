---
post_title: "task-researcher.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "task-researcher-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "task-researcher"]
ai_note: "Generated with AI assistance."
summary: "任务研究专家模式：只做深度研究、只在 research 目录写文档、证据优先与去重更新。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 专注研究与证据留痕的模式，创建/更新 ./.copilot-tracking/research/ 下的研究文件，绝不改动源代码。

## When

- 计划生成前研究缺失/不充分；需要权衡多种方案并收敛到唯一推荐路线时。

## Why

- 保障结论来源可靠、可追溯、可验证；避免假设驱动与重复信息；为计划与实现阶段提供稳固依据。

## How

- 使用 codebase/search/usages/fetch/githubRepo 等工具；以研究模板记录“文件分析/外部研究/关键发现/推荐方案”；发现即记录、过时即删除；消除重复并合并条目；用日期前缀命名。

## Key points (英文+中文对照)

- Evidence before opinion.（证据先于结论）
- Consolidate, don’t duplicate.（合并而非重复）
- Remove outdated info.（移除过时信息）
- Single recommended approach.（收敛为单一推荐）
- Research-only writes.（仅在 research 写入）

## 使用场景

### 1. 研究立项与范围界定（Scope and planning）

- 用户故事：作为研究者，我要定义研究范围、问题清单与工具栈，并初始化研究文件。
- 例 1："创建 YYYYMMDD-topic-research.md，填充模板骨架。"
- 例 2："列出研究问题与成功标准。"
- 例 3："为每个问题选择工具并说明理由。"
- 例 4："初始化 External Resources 区域。"
- 例 5："将研究任务写入 Todo 并标注优先级。"

### 2. 递归查证与合并（Recursive validation & consolidation）

- 用户故事：作为研究者，我要递归查证并把重复与过时信息清理合并。
- 例 1："对新术语执行二次/三次搜索。"
- 例 2："将类似发现合并到单一条目，并删除重复。"
- 例 3："对比多源证据并标注版本/日期。"
- 例 4："把被否定的路线放入 ‘Decision Trail’。"
- 例 5："持续更新研究文件的关键发现。"

### 3. 示例与配置沉淀（Examples and configurations）

- 用户故事：作为工程师，我希望研究包含完整示例与配置片段以便快速验证。
- 例 1："添加可运行的最小代码示例与来源。"
- 例 2："记录必要的配置样例与格式。"
- 例 3："将边界与限制纳入 Technical Requirements。"
- 例 4："补充 API/Schema 引用。"
- 例 5："对实验结果做时间戳与结论说明。"

### 4. 收敛与交接（Convergence and handoff）

- 用户故事：作为协调者，我要把研究收敛为唯一建议并准备交接给规划/实现。
- 例 1："将单一推荐方案写入 Recommended Approach。"
- 例 2："把关键证据列表与链接汇总到 External Resources。"
- 例 3："输出实现目标/关键任务/依赖/成功标准。"
- 例 4："标记研究状态为 Verified/Updated。"
- 例 5："给出下一步计划建议。"

## 原始文件

- chatmodes/task-researcher.chatmode.md
