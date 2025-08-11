# Prompts 本地化批次 1 质量摘要

批次范围：5 个文件（chatmodes 3, prompts 2）

| 序号 | 源文件 | 目标文件 | 前言(front matter) 校验 | 结构元素(标题/代码块/表格) | 链接保留 | 状态 |
|------|--------|----------|--------------------------|----------------------------|-----------|------|
| 1 | chatmodes/wg-code-sentinel.chatmode.md | localization/zh-cn/chatmodes/wg-code-sentinel.chatmode.md | OK | OK | N/A | ✅ |
| 2 | chatmodes/wg-code-alchemist.chatmode.md | localization/zh-cn/chatmodes/wg-code-alchemist.chatmode.md | OK | OK | N/A | ✅ |
| 3 | chatmodes/voidbeast-gpt41enhanced.chatmode.md | localization/zh-cn/chatmodes/voidbeast-gpt41enhanced.chatmode.md | OK | OK | N/A | ✅ |
| 4 | prompts/update-specification.prompt.md | localization/zh-cn/prompts/update-specification.prompt.md | OK | OK | 保持 | ✅ |
| 5 | prompts/update-oo-component-documentation.prompt.md | localization/zh-cn/prompts/update-oo-component-documentation.prompt.md | OK | OK | 保持 | ✅ |

## 自动/半自动校验说明

- Front matter 字段与顺序：保持；仅 description 翻译
- 标题层级：与源一致（# / ## / 列表结构匹配）
- 代码块：全部保留（模板示例 / mermaid 占位 / 语言标记）
- 列表与强调：数量与层级一一对应
- 链接：/spec/ 模板链接保持；无需重写的内部锚点
- 外部 URL：无

## 差异与裁剪说明

无语义遗漏；必要专有名（SOLID, Clean Code, PLAN MODE 等）保留并提供语境化中文表达。

## 后续改进计划

1. 引入脚本化结构对比（统计：标题计数 / 代码块计数 / 表格计数）
2. 链接重写自动化（后续涉及跨文档本地化引用时）
3. 生成累计进度总览（356 总量 → 已完成 5 ≈ 1.40%）

---

若发现问题或需调整术语一致性，请记录于后续批次 QA。
