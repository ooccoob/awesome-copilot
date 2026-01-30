---
post_title: 'mkdocs-translations.prompt.md Use Cases'
author1: 'github-copilot'
post_slug: 'mkdocs-translations-prompt-use-cases'
microsoft_alias: 'copilot'
featured_image: ''
categories: []
tags: ['use-cases', 'mkdocs', 'i18n', 'docs', 'translation']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for translating MkDocs documentation to a target locale with folder mirroring, include path updates, and mkdocs.yml i18n config updates.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

* 将 MkDocs 文档从 docs/docs/en 与 docs/docs/includes/en 翻译到目标语言，保持目录结构与 Markdown 格式，并更新 i18n 配置。

## When

* 需要为现有 MkDocs 文档新增目标语言版本时。
* 建立多语言站点、验证本地化工作流或准备国际发布版本时。
* 希望标准化翻译步骤与产物路径，并一次性完成所有文件翻译时。

## Why

* 快速建立一致的多语言文档集，降低人工遗漏与结构偏差风险。
* 通过自动化流程保证目录镜像与链接正确，减少运维与编辑成本。
* 将翻译流程固化为可重复执行的流水线步骤。

## How

* 先确认目标语言与 locale 代码（如 es、fr、pt-BR、ko）。
* 构建目标语言目录：docs/docs/<locale> 与 docs/docs/includes/<locale>，完整镜像 en 目录结构。
* 翻译每个文件，保留原 Markdown 格式与文件名；末尾追加“Translated using GitHub Copilot and GPT-4o.”
* 更新 include 引用路径中的语言段（如 includes/en/... → includes/es/...）。
* 修改 mkdocs.yml：新增 i18n locale，完善 nav/admonition 翻译映射。
* 全量核对：翻译文件数量必须与源文件数一致。

## Key points (英文+中文对照)

* Preserve folder structure and formatting（保留目录结构与 Markdown 格式）
* Process all files automatically without prompts（自动化全量处理，无需交互确认）
* Update include paths to new locale（更新 include 路径为目标语言）
* Add locale to mkdocs.yml i18n plugin（在 mkdocs.yml 中新增 locale 配置）
* Append translation attribution line（在文件末尾追加翻译归因行）

## 使用场景

### 1. 启动与清点（文件清单与工单）

* 用户故事：作为文档维护者，我希望获取待翻译文件清单，确保目录镜像完整、可追踪。
* 例1："/mkdocs-translations 请列出 docs/docs/en 全量文件与子目录清单。"
* 例2："/mkdocs-translations 请列出 docs/docs/includes/en 全量文件与子目录清单。"
* 例3："/mkdocs-translations [目标语言=es] 请对比源与目标的文件数量差异，生成缺失列表。"
* 例4："/mkdocs-translations [目标语言=fr] 请生成翻译任务表（路径、类型、预计耗时）。"
* 例5："/mkdocs-translations [目标语言=pt-BR] 请输出翻译批次计划与分配建议。"

### 2. 批量镜像与翻译（主体文档）

* 用户故事：作为翻译执行者，我希望自动镜像目录并逐一翻译所有文档，避免遗漏或错放。
* 例1："/mkdocs-translations [locale=es] 请在 docs/docs/es 镜像 en 目录并翻译所有文件。"
* 例2："/mkdocs-translations [locale=fr] 请在每个翻译文件末尾追加翻译归因行。"
* 例3："/mkdocs-translations [locale=ko] 请保持标题/代码块/链接原样格式，仅翻译正文。"
* 例4："/mkdocs-translations [locale=pt-BR] 请在完成后核对翻译文件总数与源文件一致。"
* 例5："/mkdocs-translations [locale=es] 请对未翻译的残留文件生成告警清单。"

### 3. 处理 includes 与路径替换

* 用户故事：作为技术写作人员，我需要同步翻译 includes 并修正引用路径，确保站点构建无报错。
* 例1："/mkdocs-translations [locale=es] 请在 docs/docs/includes/es 镜像 en 子目录并翻译所有 includes。"
* 例2："/mkdocs-translations [locale=fr] 请替换文内 include 路径为 includes/fr/... 并逐条校验。"
* 例3："/mkdocs-translations [locale=ko] 请输出所有被替换的 include 路径变更表。"
* 例4："/mkdocs-translations [locale=pt-BR] 请扫描链接与图片路径，确认未误伤英文路径。"
* 例5："/mkdocs-translations [locale=es] 请对 includes 变更进行一次性回归检查。"

### 4. 更新 mkdocs.yml（i18n 配置）

* 用户故事：作为站点管理员，我希望在 mkdocs.yml 中新增 locale 并完善导航/提示语翻译，保证切换语言正常。
* 例1："/mkdocs-translations [locale=fr] 请在 mkdocs.yml 的 i18n 插件中新增 locale=fr。"
* 例2："/mkdocs-translations [locale=es] 请补充 nav_translations 与 admonition_translations 映射。"
* 例3："/mkdocs-translations [locale=pt-BR] 请输出需要人工确认的 UI 文案项列表。"
* 例4："/mkdocs-translations [locale=ko] 请校验 i18n 配置是否与目录结构匹配。"
* 例5："/mkdocs-translations [locale=fr] 请生成一次 mkdocs build 的预检查指引。"

### 5. 质量核对与验收（收尾）

* 用户故事：作为审核者，我需要对翻译产物进行一致性审查并输出差异报告，确保上线质量。
* 例1："/mkdocs-translations [locale=es] 请对源/目标文件进行标题与段落数量对比。"
* 例2："/mkdocs-translations [locale=fr] 请抽样检查代码块是否被误翻或包裹。"
* 例3："/mkdocs-translations [locale=ko] 请扫描是否包含未替换的 includes/en/ 路径。"
* 例4："/mkdocs-translations [locale=pt-BR] 请输出未翻与机翻痕迹的高风险清单。"
* 例5："/mkdocs-translations [locale=es] 请生成最终验收报告与后续维护建议。"

## 原始文件

* [mkdocs-translations.prompt.md](../../prompts/mkdocs-translations.prompt.md)
