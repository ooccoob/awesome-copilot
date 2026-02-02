---
agent: 'agent'
description: 'Create GitHub Issues for unimplemented requirements from specification files using feature_request.yml template.'
tools: ['search/codebase', 'search', 'github', 'create_issue', 'search_issues', 'update_issue']
---
# 针对未满足的规范要求创建 GitHub 问题

针对 `${file}` 规范中未实现的要求创建 GitHub 问题。

## 工艺流程

1. 分析规格文件以提取所有需求
2. 检查每个需求的代码库实施状态
3. 使用 `search_issues` 搜索现有问题以避免重复
4. 使用 `create_issue` 根据未实现的需求创建新问题
5. 使用 `feature_request.yml` 模板（回退到默认值）

## 要求

- 规范中每个未实现的要求都会出现一个问题
- 清晰的需求 ID 和描述映射
- 包括实施指南和验收标准
- 创建前验证现有问题

## 发行内容

- 标题：需求 ID 和简要说明
- 描述：详细需求、实现方法、背景
- 标签：功能、增强（视情况而定）

## 实施检查

- 在代码库中搜索相关代码模式
- 查看`/spec/`目录下相关规范文件
- 验证要求未部分实现
