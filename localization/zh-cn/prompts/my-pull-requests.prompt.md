---
mode: "agent"
tools: ["githubRepo", "github", "get_me", "get_pull_request", "get_pull_request_comments", "get_pull_request_diff", "get_pull_request_files", "get_pull_request_reviews", "get_pull_request_status", "list_pull_requests", "request_copilot_review"]
description: "列出当前仓库中属于我的 Pull Request"
---

使用 #githubRepo 获取当前仓库信息，并使用 #list_pull_requests 搜索并列出分配给我的 PR。

描述每个 PR 的目的与细节。

若某个 PR 正在等待他人评审，请在结果中予以强调。

若该 PR 存在检查失败，请描述失败项并给出可能的修复建议。

若尚未进行 Copilot 评审，可提示是否使用 #request_copilot_review 发起评审。

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](../../issues) 进行反馈。
