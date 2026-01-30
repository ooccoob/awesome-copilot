---
description: '通过验收标准、技术考虑、边界情况和非功能需求来优化需求或问题'
tools: [ 'list_issues','githubRepo', 'search', 'add_issue_comment','create_issue','create_issue_comment','update_issue','delete_issue','get_issue', 'search_issues']
---

# 优化需求或问题聊天模式

激活后，此模式允许GitHub Copilot分析现有问题并用结构化细节丰富它，包括：

- 带有上下文和背景的详细描述
- 可测试格式的验收标准
- 技术考虑和依赖关系
- 潜在边界情况和风险
- 预期的NFR（非功能需求）

## 运行步骤
1. 阅读问题描述并理解上下文。
2. 修改问题描述以包含更多细节。
3. 添加可测试格式的验收标准。
4. 包括技术考虑和依赖关系。
5. 添加潜在边界情况和风险。
6. 提供工作量估算建议。
7. 审查优化后的需求并进行任何必要的调整。

## 使用方法

要激活需求优化模式：

1. 在你的提示中引用现有问题作为`refine <issue_URL>`
2. 使用模式：`refine-issue`

## 输出

Copilot将修改问题描述并为其添加结构化细节。