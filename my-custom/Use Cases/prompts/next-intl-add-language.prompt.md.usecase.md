---
post_title: "next-intl-add-language.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "next-intl-add-language-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "nextjs", "internationalization", "i18n", "localization"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the next-intl Add Language prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于在 `next-intl`（一个 Next.js 国际化库）项目中添加新语言支持的自动化提示词。

## When

- 当需要将 Next.js 应用程序本地化到一种新的语言时。
- 在扩展产品的全球市场覆盖范围时。
- 当需要翻译现有的语言文件（如 `en.json`）到新的目标语言时。

## Why

- 自动化添加新语言的繁琐过程，包括创建新的 JSON 语言文件和更新配置文件。
- 利用 AI 翻译能力，快速生成新语言文件的初稿。
- 减少手动错误，确保所有必要的配置都已更新。

## How

- 使用 `/next-intl-add-language` 命令并指定要添加的新语言代码（如 `fr`, `de`, `ja`）。
- AI 将：
    1. 找到你的默认语言文件（例如 `messages/en.json`）。
    2. 将其内容翻译成你指定的新语言。
    3. 创建一个新的语言文件（例如 `messages/fr.json`）。
    4. （可选）更新 `next.config.js` 或相关配置文件以包含新的区域设置。

## Key points (英文+中文对照)

- Internationalization (i18n, 国际化)
- Localization (l10n, 本地化)
- Translation Automation (翻译自动化)
- Configuration Update (配置更新)

## 使用场景

### 1. 添加一种新的欧洲语言 (Adding a New European Language)

- **用户故事**: 作为一名前端开发人员，我们的产品需要支持法国市场，我需要为我们的 Next.js 应用添加法语支持。
- **例 1**: `/next-intl-add-language 添加法语（fr）。` -> AI 会找到 `en.json`，翻译内容，并创建 `fr.json`。
- **例 2**: `/next-intl-add-language 我需要支持德语（de）和西班牙语（es）。` -> AI 会依次创建 `de.json` 和 `es.json`。

### 2. 支持亚洲语言 (Supporting Asian Languages)

- **用户故事**: 作为一名项目经理，我们计划进入日本市场，需要将网站翻译成日语。
- **例 1**: `/next-intl-add-language 添加日语（ja）。`
- **例 2**: `/next-intl-add-language 为我们的应用添加韩语（ko）支持。`

### 3. 扩展到多语言环境 (Expanding to a Multilingual Environment)

- **用户故事**: 作为一名初创公司创始人，我希望从一开始就将我的应用设计为多语言的，以便快速扩展。
- **例 1**: `/next-intl-add-language 基于我的 `en.json` 文件，为我生成 `es.json`, `fr.json`, `de.json`, 和 `zh.json` 的翻译文件。`

### 4. 更新和同步翻译 (Updating and Syncing Translations)

- **用户故事**: 作为一名维护者，我们在 `en.json` 中添加了一些新的键，现在需要将这些新键同步并翻译到所有其他语言文件中。
- **例 1**: `/next-intl-add-language 我更新了 `en.json`，请检查 `fr.json` 和 `de.json`，并为它们添加缺失键的翻译。` (注意：此功能可能需要更高级的脚本，但提示词可以生成这个脚本)

## 原始文件

- [next-intl-add-language.prompt.md](../../prompts/next-intl-add-language.prompt.md)
