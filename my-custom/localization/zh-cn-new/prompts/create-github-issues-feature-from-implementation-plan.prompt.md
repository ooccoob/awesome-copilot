---
mode: 'agent'
description: '使用feature_request.yml或chore_request.yml模板从实施计划阶段创建GitHub Issues。'
tools: ['codebase', 'search', 'github', 'create_issue', 'search_issues', 'update_issue']
---

# 从实施计划创建GitHub Issue

为`${file}`处的实施计划创建GitHub Issues。

## 流程

1. 分析计划文件以识别阶段
2. 使用`search_issues`检查现有问题
3. 使用`create_issue`为每个阶段创建新问题或使用`update_issue`更新现有问题
4. 使用`feature_request.yml`或`chore_request.yml`模板（回退到默认）

## 要求

- 为每个实施阶段创建一个问题
- 清晰、结构化的标题和描述
- 仅包含计划所需的更改
- 创建前验证现有问题

## 问题内容

- 标题：实施计划中的阶段名称
- 描述：阶段详情、需求和上下文
- 标签：适用于问题类型（feature/chore）