## What/When/Why/How
- What: 技术文档本地化流程规范（Markdown→目标语言区域），目录/链接/校验与免责声明。
- When: 需要为仓库批量生成多语言版本并保持链接/行数一致性时。
- Why: 降低阅读门槛、统一产出质量并便于审校与溯源。
- How: 扫描 *.md→生成 localization/{{locale}} 下对应结构→修订内部链接→行数比对→追加免责声明。

## Key Points
- 目录：localization/{{locale}}；locale 采用 lang-region（ISO639-1 + ISO3166）。
- 链接：图片保留原路径；文档链接指向本地化副本（外部链接除外）。
- 覆盖：不漏任何段落或小节；逐行对照检查。
- 校验：完成后对比原文与译文行数；行数差异提示遗漏。
- 免责声明：在文末加入（本地化）免责声明并指向 issues 页面。
- 质量：统一术语，保留代码块语言标签与结构；不改动外链 URL。

## Compact Map
L10n
- Files → localization/{{locale}}
- Links: images original, docs localized
- Line parity check
- Disclaimer append

## Checklist
- [ ] 扫描并生成目标目录结构
- [ ] 更新内部文档链接为本地化路径
- [ ] 对比行数并修复缺失段落
- [ ] 文末追加本地化免责声明
- [ ] 多语言样例校验（en-us/zh-cn 等）

## Example Questions (≥10)
- 如何校验本地化文档与原文的行数一致性？
- 如何识别并重写仓库内相对链接以指向本地化版本？
- 代码块语言与内容在本地化时应如何处理？
- 图片链接与外链在本地化时的处理边界是什么？
- 如何生成 localization/zh-cn 下的镜像目录结构？
- 如何在 CI 中自动化行数比对与缺口提醒？
- 如何维护术语表并在翻译时统一用词？
- 在多仓联动时如何保持链接稳定？
- 免责声明如何本地化并指向 issues？
- 如何处理混合语言与不可译专有名词？

Source: d:\mycode\awesome-copilot\instructions\localization.instructions.md | Generated: 2025-10-17
