---
description: "该工作流帮助系统化识别缺失特性、确定优先级，并生成可实施的详细规格说明以便推进落地。"
---

# 产品经理助理：特性识别与规格说明

该工作流指导你用系统化方法识别缺失特性、进行优先级排序，并为实施创建详细的规格说明。

## 1. 项目理解阶段

- 查看项目结构以理解组织方式
- 阅读 README.md 与其他文档把握核心功能
- 通过以下内容识别当前实现状态：
  - 入口（CLI、API、UI 等）
  - 核心模块与功能
  - 测试用于理解期望行为
  - 任何占位（placeholder）实现

**引导问题：**

- 项目的核心目标是什么？
- 解决了哪些用户问题？
- 现有实现中有哪些模式？
- 文档中提到但未完善的特性有哪些？

## 2. 差距分析阶段

- 仅对比文档中宣称的能力与实际实现
- 识别缺乏真实功能的占位代码
- 查找文档提到但缺失的健壮实现
- 从用户旅程视角识别破损或缺失的步骤
- 优先关注核心功能（非“锦上添花”）

**输出：**

- 列出 5–7 个潜在缺失特性
- 对每项给出：
  - 当前实现状态
  - 文档引用
  - 缺失对用户体验的影响

## 3. 优先级阶段

- 为每个差距打分：

**评分矩阵（1–5）**

- 用户影响：有多少用户受益？
- 战略匹配：是否符合核心使命？
- 实施可行性：技术复杂度？
- 资源需求：开发投入？
- 风险等级：潜在负面影响？

**优先级 = (用户影响 × 战略匹配) / (实施投入 × 风险等级)**

**输出：**

- 按评分给出 Top 3 缺失特性，并提供：
  - 特性名称
  - 当前状态
  - 不实现的影响
  - 依赖关系

## 4. 规格说明阶段

- 为每个优先特性编写可执行的规格说明：
  - 以“简单优先”的理念开篇
  - 聚焦 MVP 功能
  - 关注开发者体验
  - 使规格便于实施

**每个规格包括：**

1. **概览与范围**：解决什么问题？包含与不包含什么？
2. **技术要求**：核心功能、用户接口（API/UI/CLI）、与现有代码集成点
3. **实现计划**：关键模块/文件、简要示例、数据结构与接口
4. **验收标准**：完成的定义、必须工作的功能、应通过的测试

## 5. 创建 GitHub Issue 阶段

- 为每份规格创建 Issue：
  - 清晰标题
  - 完整规格正文
  - 合适标签（enhancement/high-priority 等）
  - 必要处强调 MVP 哲学

**Issue 模板：**

# [Feature Name]

## Overview

[Brief description of the feature and its purpose]

## Scope

[What's included and what's explicitly excluded]

## Technical Requirements

[Specific technical needs and constraints]

## Implementation Plan

[Step-by-step approach with simple code examples]

## Acceptance Criteria

[Clear list of requirements to consider the feature complete]

## Priority

[Justification for prioritization]

## Dependencies

- **Blocks:** [List of issues blocked by this one]
- **Blocked by:** [List of issues this one depends on]

## Implementation Size

- **Estimated effort:** [Small/Medium/Large]
- **Sub-issues:** [Links to sub-issues if this is a parent issue]

## 5.5 工作拆分优化

- **独立性分析**

  - 识别真正独立的组件
  - 重构规格以最大化并行工作流
  - 明确边界，弱化耦合

- **依赖映射**

  - 为不可避免的依赖建立清晰层级
  - 用父子 Issue 切分整体特性
  - 显式记录 “blocked by/blocks” 关系

- **工作量均衡**
  - 将大特性拆分为 1–3 天可交付的子任务
  - 为每个子任务定义明确验收标准

**实施指引：**

- 使用 GitHub Issue 链接语法建立显式关系
- 使用标签标记依赖状态（如 “blocked”、“prerequisite”）
- 为每个 Issue 记录估算复杂度/投入，以利于计划

## 6. 终审阶段

- 汇总所有规格
- 标注特性之间的实现依赖
- 建议合理的实施顺序
- 备注潜在挑战或注意事项

请始终牢记：

- 偏好简单而非复杂
- 先构建可工作的最小版本
- 重视开发者体验
- 打好可扩展的基础
- 兼顾开源协作与贡献模式
