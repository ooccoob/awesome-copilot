---
post_title: "code-tour — 用例"
post_slug: "code-tour-use-cases"
tags: ['chatmode','code-tour','onboarding','usecase']
ai_note: '根据 chatmodes/code-tour.chatmode.md 生成的中文用例'
summary: '创建引导代码浏览、团队入门与文档化重点片段的场景示例与模板。'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

什么

- 帮助工程师创建交互式代码导览（code tour），用于新成员入门、复杂模块说明或审计要点展示。

何时

- 在团队上新、代码重构后或准备演示/审计时使用。

为什么

- 结构化的代码导览能让读者快速掌握关键路径、依赖与注意事项，提升知识传递效率。

如何

- 提供代码库路径与目标受众，要求输出分步导览（每步包含文件、行号、注释与要点），并可导出为 IDE 支持的 tour 文件格式。

关键要点 (EN / ZH)

- EN: Step-by-step walkthrough; context per snippet; exportable tour format.
- ZH: 分步导览；每步包含上下文与要点；支持导出为 IDE 导览格式。

示例场景

1) 新成员入门路线
- 示例提示："为服务 A 生成一份 10 步的新成员入门 code tour，覆盖启动流程、关键模块与测试位置。"
- 预期产出：10 步导览、每步建议注释与阅读时间。

2) 复杂算法讲解
- 示例提示："为排序模块生成导览，解释主要函数、复杂度与边界条件。"
- 预期产出：导览步骤、关键代码注释与示例输入输出。

3) 发布审查导览
- 示例提示："生成审查导览突出潜在风险点（并发/资源泄露/错误处理）。"
- 预期产出：风险点列表与参考修复建议。

4) 生成 IDE 可导入文件
- 示例提示："输出可被 VS Code CodeTour 扩展导入的 JSON 格式文件样本。"
- 预期产出：可直接导入的 tour JSON 示例。

5) 文档化关键变更点
- 示例提示："为 PR 生成一个短导览，指出改动位置与向后兼容性说明。"
- 预期产出：PR 导览与兼容性评估。

原始 chatmode: ../../../../chatmodes/code-tour.chatmode.md
---
post_title: "code-tour.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "code-tour-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases","code-tour","developer-experience"]
ai_note: "Generated with AI assistance."
summary: "Code Tour 用例：自动生成代码导航、注释建议与 onboarding 流程示例。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 使用 Code Tour 驱动的交互式代码导航与文档化示例。

## When

- 在新成员入职、代码审查或大型仓库导航时使用。

## Why

- 降低学习曲线，提高代码发现效率，并保持知识在代码库中的可随时间演化的文档。

## How

- 生成按模块/路径组织的 tour 步骤、清晰注释与任务链接。

## Key points (英文+中文对照)

- Guided walkthroughs（引导式讲解）
- Contextual notes（上下文注释）
- Onboarding flows（入职流程）
- Review-focused tours（审查导向的 tour）
- Linkable tasks（可链接任务）

## 使用场景

### 1. 新成员入职导航

- 用户故事：作为团队负责人，我要为新成员生成模块级别的学习路径。
- 例 1：从高层架构开始的 tour。
- 例 2：重点代码路径与依赖说明。
- 例 3：集成运行/测试步骤说明。
- 例 4：安全与合规点提示。
- 例 5：建议阅读顺序与练习任务。

### 2. 代码审查预览

- 用户故事：作为 reviewer，我要快速定位变更相关上下文与关键点。
- 例 1：为 PR 自动生成变更要点 tour。
- 例 2：列出潜在风险点与测试建议。
- 例 3：引用相关设计文档。
- 例 4：示例修复建议与重构提示。
- 例 5：导出审查摘要。

### 3. 架构文档嵌入

- 用户故事：作为架构师，我要把设计决策以 tour 形式嵌入代码库。
- 例 1：记录关键接口与调用链。
- 例 2：说明兼容性契约与约束。
- 例 3：列出演进建议与替代方案。
- 例 4：关联 ADR。
- 例 5：提供示例使用流程。

### 4. 教学与演练任务

- 用户故事：作为导师，我要为任务创建练习用的 tour。
- 例 1：任务目标与预期输出说明。
- 例 2：步骤化练习指导。
- 例 3：测试验证点与断言示例。
- 例 4：集成自动评估脚本建议。
- 例 5：记录常见错误与修复建议。

### 5. 文档审计与维护

- 用户故事：作为文档负责人，我要发现过时 tour 并提供更新建议。
- 例 1：检测失效链接与文件路径。
- 例 2：标记需要重写的上下文段落。
- 例 3：生成更新任务并分配维护者。
- 例 4：自动化测试 tour 的可执行性。
- 例 5：维护版本历史与变更记录。

## 原始文件

- [chatmodes/code-tour.chatmode.md](../../../chatmodes/code-tour.chatmode.md)
