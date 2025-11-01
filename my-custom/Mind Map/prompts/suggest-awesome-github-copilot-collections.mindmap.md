## Suggest Awesome Copilot Collections — Mind Map

### What
- 基于仓库与会话上下文，推荐 awesome-copilot 集合（prompts/instructions/chatmodes），并支持按需安装。

### When
- 需要系统性增强某类能力（测试/云/架构）并批量引入资产时。

### Why
- 以集合为单位补齐流程短板，控制重复与一致性。

### How
- 抓取集合清单→扫描本地资产→解析前言→语境匹配→资产重叠度分析→推荐与安装预览。

### Key Points (中/英)
- 集合/Collection
- 资产/Assets
- 去重/Overlap
- 相关性/Relevance
- 安装/Install (opt-in)
- 用法/Usage Guidance

### Compact map
- Inputs: README.collections + local prompts/instructions/chatmodes
- Process: fetch → inventory → compare → suggest → preview install
- Output: 推荐表（项数、重叠、理由、价值）

### Example Questions (≥10)
- 如何计算集合与本地资产的“实质重叠度”？
- 为什么推荐该集合，对当前仓库有什么直接价值？
- 安装前如何给出“将要写入”的目录与清单预览？
- 对于重叠项如何安全跳过或标注来源？
- 集合内不同资产类型的落盘目录规则是什么？
- 失败项（抓取/权限）如何报告与重试？
- 安装后如何产出使用指南与示例？
- 如何保持与上游集合的同步与差异化维护？
- 多集合并装的冲突与优先级策略？
- 如何在 CI 中校验格式/前言与命名规范？

---
- Source: d:\mycode\awesome-copilot\prompts\suggest-awesome-github-copilot-collections.prompt.md
- Generated: 2025-10-17
