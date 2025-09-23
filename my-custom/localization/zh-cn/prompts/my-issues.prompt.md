---
mode: "agent"
tools: ["githubRepo", "github", "get_issue", "get_issue_comments", "get_me", "list_issues"]
description: "列出当前仓库中属于我的 Issue"
---

使用 #githubRepo 获取当前仓库信息，并使用 #list_issues 搜索并列出分配给我的 Issue。

基于 Issue 的创建时间、评论数量以及状态（open/closed），给出我应优先关注的建议。

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](../../issues) 进行反馈。
