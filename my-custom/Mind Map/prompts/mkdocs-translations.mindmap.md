## What
- 将 MkDocs 文档从 en/includes/en 批量翻译到指定目标语言，保持结构与格式，并更新 mkdocs.yml。

## When to use
- 需要为现有英文文档新增多语言版本并自动化处理全量文件。

## Why it matters
- 保持结构一致与引用路径正确，避免链接失效；分支与提交流程可控，提升文档协作质量。

## How (关键流程)
- 确认目标语言与 locale；新建分支 docs-translation-<lang>
- 列出 docs/docs/en 与 docs/docs/includes/en 全量文件
- 逐个翻译并镜像目录结构；更新 includes 路径引用
- 修改 mkdocs.yml：i18n.locale/nav/admonition translations
- 完成后核对源/目标文件数一致

## Example questions (≥10)
1. 目标语言为 pt-BR，请创建分支并给出需要翻译的文件清单统计表。
2. 翻译第一批 10 个文件并在末尾追加“Translated using GitHub Copilot and GPT-4o.”
3. 展示 includes 路径从 includes/en/... 到 includes/pt-BR/... 的自动替换规则。
4. 修改 mkdocs.yml，新增 i18n locale=pt-BR，并示例 nav_translations/admonition_translations。
5. 如何确保代码块、链接与元数据在翻译后保持不变？
6. 如果某些文件已存在目标语言版本，如何跳过并记录？
7. 提供中断恢复策略：如何从上次处理的文件继续。
8. 翻译完成后，生成源/目标文件数校验报告。
9. 给出提交规范（commit message 模板）与 PR 描述模板。
10. 如何在 CI 中校验未翻译或漏改的 includes 路径？

## Key points
- CN: 先列清单再翻译、镜像结构、引用更新、配置同步、数量校验
- EN: List-first, mirror structure, update includes, sync config, count verification

## Mind map (简要)
- 语言确认 → 分支 → 列表 → 翻译 → 引用更新 → 配置 →校验 → 提交

---
Source file: d:\mycode\awesome-copilot\prompts\mkdocs-translations.prompt.md
Generated: 2025-10-17T00:00:00Z
