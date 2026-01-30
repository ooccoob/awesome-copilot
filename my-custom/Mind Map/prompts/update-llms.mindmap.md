## What
- 目标：依据 https://llmstxt.org/ 规范，更新仓库根目录 llms.txt 以反映文档/规格与结构变化。
- 范围：项目名、摘要引用块、H2 分区下的文件链接列表（文档/规格/示例/配置/Optional）。

## When
- 文档结构发生变化、新增/迁移/删除文件时。
- 版本发布或重大模块/规范调整后。

## Why
- 让 LLM 快速定位关键信息，提高回答质量与上下文相关性。
- 保持机器/人类双可读，降低索引与导航成本。

## How
- 分析：读取现有 llms.txt 与规范页面 → 盘点仓库结构变化 → 发现新增/移除/迁移文档。
- 计划：决定需新增的链接与描述、需移除或更新的条目、必要的分区重组。
- 执行：仅在仓库根写入/更新 llms.txt，保证相对路径有效、格式合规（H1/引用块/H2 列表）。
- 校验：链接有效性、规范合规性、语言清晰度与结构一致性。

## Key Points
- 链接格式：[name](relative-url): optional description
- 分区建议：Documentation/Specifications/Examples/Configuration/Optional。
- 排序：按字母或逻辑顺序；避免冗余与实现细节。

## Compact Map
- Review current → Scan repo → Plan changes → Update file → Validate

## Example Questions (10+)
- 我们新增了 /doc 与 /spec，llms.txt 需要增加哪些关键条目？
- 如何为多模块（后端/前端）同时组织分区？
- 规范要求的 H1/引用块/H2 的最小集是什么？
- 链接描述写多长最合适、如何避免冗余？
- 已删除或移动的文件如何在 llms.txt 中更新到新路径？
- Optional 区放哪些“可省略”的文档更合适？
- 如何在 CI 中校验链接有效性与规范格式？
- 如果仓库多语言文档并行，如何表达语言维度？
- 如何确保 llms.txt 对 LLM 友好且对人类也清晰？
- 变更较大时是否需要在 PR 中附差异摘要？
- 如何避免把实现细节/生成产物写入 llms.txt？

---
Source: d:\mycode\awesome-copilot\prompts\update-llms.prompt.md
Generated: 2025-10-17T00:00:00Z
