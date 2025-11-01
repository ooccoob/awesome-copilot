## What
- 目标：将 `${input:folder}` 下文件按 `${input:pattern}` 生成索引/表格，更新到 `${file}` 的指定区块或新增分节。
- 输出：简单列表/详细表格/按类型分组三选一；相对路径链接与描述。

## When
- 文档目录新增/大量变更，需集中索引时。
- README/目录页需要自动维护子文档列表时。

## Why
- 保持文档可发现性与一致性；减少手工维护成本。

## How
- 读取 `${file}` 识别现有“index/files/contents”等标题或注释标记区段。
- 列举 `${input:folder}` 下匹配文件，提取：名称/类型/首行说明/大小/修改时间（可选）。
- 选择最合适的三种结构之一并生成内容；若已有区段则替换，若无则新增。
- 校验：相对链接、Markdown 语法、排序（默认字母序）。

## Key Points
- 保留原文档层次与格式；处理特殊字符；相对路径。
- 可按文件类型分节；可增量更新或全量替换。

## Compact Map
- Scan file → Discover files → Structure table → Update section → Validate

## Example Questions (10+)
- 该 README 已有目录表格，如何无损替换其内容？
- 描述来自首行标题/注释，优先级与回退策略是什么？
- 需要按类型（.md/.js/.py）分组输出，如何排序？
- 表格太长时是否可折叠或拆分分节？
- 文件名包含空格/中文/括号时如何正确生成链接？
- 我想增加“最后修改时间/大小”两列，该如何取值与格式化？
- 如何只更新符合 pattern 的文件而不影响其他条目？
- 目录层级很深时是否可以仅索引一层并标注？
- 与自动化 pipeline 集成时如何避免冲突提交？
- 如何在 PR 中标注新增/移除的文件变化统计？
- 大文件/二进制文件是否应排除并标注原因？

---
Source: d:\mycode\awesome-copilot\prompts\update-markdown-file-index.prompt.md
Generated: 2025-10-17T00:00:00Z
