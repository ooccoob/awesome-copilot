---
mode: "agent"
description: "使用 feature_request.yml 模板，从规格文件创建功能需求的 GitHub Issue。"
tools: ["codebase", "search", "github", "create_issue", "search_issues", "update_issue"]
---

# 基于规格创建 GitHub Issue

为 `${file}` 所在的规格文件创建 GitHub Issue。

## 流程

1. 分析规格文件以提取需求
2. 使用 `search_issues` 检查已有 Issue
3. 使用 `create_issue` 创建新 Issue，或用 `update_issue` 更新已有 Issue
4. 优先使用 `feature_request.yml` 模板（若不可用则回退为默认模板）

## 要求

- 针对整份规格只创建一个 Issue
- 标题需能明确标识该规格
- 仅包含规格要求的改动
- 在创建前与现有 Issue 进行去重核验

## Issue 内容

- 标题：从规格中提取的功能名称
- 描述：问题背景、拟议方案与上下文
- 标签：feature、enhancement（视情况而定）

```

```
