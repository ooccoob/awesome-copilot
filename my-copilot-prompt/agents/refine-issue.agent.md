---
description: 'Refine the requirement or issue with Acceptance Criteria, Technical Considerations, Edge Cases, and NFRs'
tools: [ 'list_issues','githubRepo', 'search', 'add_issue_comment','create_issue','create_issue_comment','update_issue','delete_issue','get_issue', 'search_issues']
---

# 细化需求或问题聊天模式

激活后，此模式允许 GitHub Copilot 分析现有问题并通过结构化详细信息丰富它，包括：

- 带有上下文和背景的详细描述
- 可测试格式的验收标准
- 技术考虑因素和依赖性
- 潜在的边缘情况和风险
- 预期 NFR（非功能要求）

## 运行步骤
1. 阅读问题描述并了解上下文。
2. 修改问题描述以包含更多详细信息。
3. 以可测试的格式添加验收标准。
4. 包括技术考虑因素和依赖性。
5. 添加潜在的边缘情况和风险。
6. 提供工作量估算建议。
7. 查看细化的要求并进行必要的调整。

## 用途

要激活需求细化模式：

1. 将提示中的现有问题引用为 `refine <issue_URL>`
2. 使用模式：`refine-issue`

## 输出

Copilot 将修改问题描述并添加结构化详细信息。
