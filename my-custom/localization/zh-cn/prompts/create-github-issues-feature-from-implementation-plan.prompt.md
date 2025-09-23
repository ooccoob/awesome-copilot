---
mode: "agent"
description: "使用 feature_request.yml 或 chore_request.yml 模板，从实施计划的各阶段创建对应的 GitHub Issues。"
tools: ["codebase", "search", "github", "create_issue", "search_issues", "update_issue"]
---

# 基于实施计划创建 GitHub Issues

为 `${file}` 所在的实施计划创建对应的 GitHub Issues。

## 流程

1. 分析计划文件以识别阶段（phases）
2. 使用 `search_issues` 检查已有 Issue
3. 每个阶段创建一个新 Issue（`create_issue`），或用 `update_issue` 更新已有 Issue
4. 使用 `feature_request.yml` 或 `chore_request.yml` 模板（不可用时回退为默认模板）

## 要求

- 每个实施阶段对应一个 Issue
- 标题与描述需清晰、结构化
- 仅包含计划要求的改动
- 在创建前与现有 Issue 进行去重核验

## Issue 内容

- 标题：来自实施计划的阶段名称
- 描述：阶段细节、要求与上下文
- 标签：根据 Issue 类型选择合适标签（feature/chore）

```

```
