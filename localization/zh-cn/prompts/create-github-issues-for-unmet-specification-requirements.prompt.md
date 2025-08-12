---
mode: "agent"
description: "使用 feature_request.yml 模板，为规格文件中尚未实现的需求创建 GitHub Issues。"
tools: ["codebase", "search", "github", "create_issue", "search_issues", "update_issue"]
---

# 为未满足的规格需求创建 GitHub Issues

为 `${file}` 指定的规格文件中尚未实现的需求创建 GitHub Issues。

## 流程

1. 分析规格文件并提取所有需求
2. 检查代码库中每项需求的实现状态
3. 使用 `search_issues` 去重，避免重复 Issue
4. 为每个未实现的需求使用 `create_issue` 创建新 Issue
5. 优先使用 `feature_request.yml` 模板（不可用则回退默认模板）

## 要求

- 每个未实现的需求对应一个 Issue
- 明确给出需求 ID 与描述
- 包含实施指引与验收标准
- 创建前需与现有 Issue 去重核验

## Issue 内容

- 标题：需求 ID 与简述
- 描述：需求详情、实施方式与上下文
- 标签：feature、enhancement（视情况而定）

## 实施检查

- 在代码库中搜索相关代码模式
- 检查 `/spec/` 目录下的相关规格文件
- 确认该需求未被部分实现

```

```
