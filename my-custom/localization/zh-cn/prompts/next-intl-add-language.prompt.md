---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "findTestFiles", "search", "writeTest"]
description: "为 Next.js + next-intl 应用新增一种语言"
---

这是一个在使用 next-intl 做国际化的 Next.js 项目中新增语言的指南：

- i18n 使用 next-intl。
- 所有翻译位于 `./messages` 目录。
- UI 语言切换组件：`src/components/language-toggle.tsx`。
- 路由与中间件配置位于：
  - `src/i18n/routing.ts`
  - `src/middleware.ts`

新增语言时：

- 将 `en.json` 的所有内容翻译为新语言，保证所有 JSON 条目均有对应翻译。
- 在 `routing.ts` 与 `middleware.ts` 中添加新语言路径。
- 在 `language-toggle.tsx` 中加入新语言选项。

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](../../issues) 进行反馈。
