---
mode: 'agent'
tools: ['changes','codebase', 'edit/editFiles', 'findTestFiles', 'search', 'writeTest']
description: '向Next.js + next-intl应用程序添加新语言'
---

这是使用next-intl向Next.js项目添加新语言的指南，

- 对于i18n，应用程序使用next-intl。
- 所有翻译都在`./messages`目录中。
- UI组件是`src/components/language-toggle.tsx`。
- 路由和中间件配置在以下文件中处理：
  - `src/i18n/routing.ts`
  - `src/middleware.ts`

添加新语言时：

- 将`en.json`的所有内容翻译为新语言。目标是为完整翻译，在新语言中拥有所有JSON条目。
- 在`routing.ts`和`middleware.ts`中添加路径。
- 将语言添加到`language-toggle.tsx`。