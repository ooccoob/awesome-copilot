---
agent: 'agent'
tools: ['changes','search/codebase', 'edit/editFiles', 'findTestFiles', 'search', 'writeTest']
description: 'Add new language to a Next.js + next-intl application'
---

这是使用 next-intl 向 Next.js 项目添加新语言以实现国际化的指南，

- 对于 i18n，应用程序使用 next-intl。
- 所有翻译都在目录 `./messages` 中。
- UI 组件是 `src/components/language-toggle.tsx`。
- 路由和中间件配置在以下位置处理：
  - __代码0__
  - __代码0__

添加新语言时：

- 将 `en.json` 的所有内容翻译为新语言。目标是让所有 JSON 条目都采用新语言，以实现完整翻译。
- 在 `routing.ts` 和 `middleware.ts` 中添加路径。
- 将语言添加到 `language-toggle.tsx`。
