---
mode: 'agent'
description: '使用feature_request.yml模板从规范文件为未实现的需求创建GitHub Issues。'
tools: ['codebase', 'search', 'github', 'create_issue', 'search_issues', 'update_issue']
---

# 为未满足的规范需求创建GitHub Issues

为`${file}`处规范中未实现的需求创建GitHub Issues。

## 流程

1. 分析规范文件以提取所有需求
2. 检查每个需求的代码库实现状态
3. 使用`search_issues`搜索现有问题以避免重复
4. 使用`create_issue`为每个未实现需求创建新问题
5. 使用`feature_request.yml`模板（回退到默认）

## 要求

- 为规范中每个未实现需求创建一个问题
- 清晰的需求ID和描述映射
- 包含实现指导和验收标准
- 创建前验证现有问题

## 问题内容

- 标题：需求ID和简要描述
- 描述：详细需求、实现方法和上下文
- 标签：feature、enhancement（根据需要）

## 实现检查

- 搜索代码库中的相关代码模式
- 检查`/spec/`目录中的相关规范文件
- 验证需求没有部分实现