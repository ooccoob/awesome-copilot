## What
- 将领域 memory.instructions.md 中“成熟经验”合并进对应 instructions.md，去冗余且不丢知识。

## When to use
- 领域知识在 memory 文件中沉淀较多，需要固化到主指令文件并清理重复部分。

## Why it matters
- 统一入口便于检索与复用；减少知识漂移；维持高质量、可扫描的最终指令。

## How (关键流程)
- 解析命令与作用域（global/workspace）→ 读取 memory 与指令
- 提案阶段：列出候选记忆块与落位位置，等待用户“go”批准
- 质量标准：0 知识丢失、最小冗余、最大可扫描性
- 合并迭代：起草→对照质量条→精修→达标
- 落盘：更新指令文件（含 frontmatter）、合并 applyTo 模式、清理已合并记忆

## Example questions (≥10)
1. 解析“/memory-merger >prompt-engineering ws”，并给出两端文件的实际路径。
2. 扫描 memory 文件，列出 5 条候选合并项，标注建议插入到 instructions 的哪个章节。
3. 给出 10/10 质量标准的检查清单，并据此评估当前合并草案差距。
4. 生成首版合并草案，并高亮潜在冗余或冲突段。
5. 合并 applyTo 通配规则时，如何去重并保持更宽覆盖？示例。
6. 若 memory 中存在与现有指令相反的建议，如何决策与记录取舍？
7. 清理 memory 文件时如何保留未合并条目与后续待评估清单？
8. 产出一次性 diff 视图，便于用户审阅与回滚。
9. 编写自动化检查：确保 frontmatter 与描述字段完整且非空。
10. 当用户输入 domain 拼写错误时，如何基于目录 glob 提示可能匹配项？

## Key points
- CN: 显式审批、质量门槛、无损合并、去重、路径与范围正确
- EN: Explicit approval, quality bar, lossless merge, dedup, correct paths/scopes

## Mind map (简要)
- 输入解析 → 文件定位 → 候选提案 → 质量标准 → 合并草案 → 文件更新 → 清理残留

---
Source file: d:\mycode\awesome-copilot\prompts\memory-merger.prompt.md
Generated: 2025-10-17T00:00:00Z
