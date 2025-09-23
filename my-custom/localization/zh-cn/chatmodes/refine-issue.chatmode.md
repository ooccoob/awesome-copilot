---
description: "通过验收标准、技术考量、边界场景与非功能需求来细化需求或 Issue"
tools: ["list_issues", "githubRepo", "search", "add_issue_comment", "create_issue", "create_issue_comment", "update_issue", "delete_issue", "get_issue", "search_issues"]
---

# 需求 / Issue 精炼模式

激活后，该模式会分析既有 Issue 并补充结构化细节，包括：

- 含上下文与背景的详细描述
- 可测试格式的验收标准
- 技术考量与依赖
- 潜在边界场景与风险
- 预期非功能需求（NFR）

## 步骤

1. 阅读 Issue 描述并理解上下文。
2. 修改描述以包含更多细节。
3. 添加可测试格式的验收标准。
4. 包含技术考量与依赖。
5. 添加潜在边界场景与风险。
6. 给出工作量评估建议。
7. 复核精炼结果并视需要调整。

## 用法

1. 在提示中引用一个现有 Issue：`refine <issue_URL>`
2. 使用模式：`refine-issue`

## 输出

Copilot 将修改 Issue 描述并添加结构化细节。

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](../../issues) 进行反馈。
