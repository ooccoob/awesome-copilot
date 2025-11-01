---
mode: "agent"
description: "Read a  chatmode.md, extract best practices, generate MECE scenarios with user stories and 5+ imperative examples each, and write <source>.usecase.md to the specified folder."
tools: ["codebase", "search", "editFiles", "changes"]
---

## 用例说明文档生成器（Use Case Builder）

读取指定的提示词 .md 文件，提炼最佳实践，使用 MECE 方法划分“使用场景”，并为每个场景写出“用户故事 + 不少于 5 条祈使句示例”。输出一份可直接复制复用的 `<源文件名>.usecase.md` 文档，并自动保存到指定目录。

## 输入

- sourceMdPath：源 .md 文件的绝对或相对路径（例如：`d:\mycode\awesome-copilot\my-custom\prompts\java-springboot.prompt.md`）。
- optional.selection：用户当前选择的一段代码或片段（可为空，用于示例措辞）。
- optional.mindmapPath：同主题的思维导图/摘要 .md（若存在，用于提取 Key points）。

## 任务要求

- 阅读 `sourceMdPath` 内容，严格按其“最佳实践/能力边界/使用建议”生成“使用场景”清单，采用 MECE 分类，避免重叠与遗漏。
- 每个“使用场景”包含：
  - 用户故事（第一人称角色 + 目标 + 价值）。
  - 示例（不少于 5 条），使用祈使句，贴近日常 AI 协作口吻。格式建议：
    - `"[选择一段代码|提供一个 md] 请根据[当前选择/提供的文件]，帮我 <具体动作> ..."`
  - 示例内容必须严格对齐源文件能力（不得超出源文件建议的范围）。
- 文档中必须包含固定版块：What / When / Why / How、Key points（英中对照）、使用场景、原始文件（链接）。
- 如存在思维导图（如 `java-springboot.mindmap.md`），优先从其中的 Key points 提取 3–5 条“英文+中文对照”；否则从源文件纲要提炼。
- 语言：中文为主；Key points 提供英中对照。
- Markdown 合规：使用 `##/###` 标题；标题与列表/代码块上下留空行；示例可直接复制。

## 输出文件命名与位置（强制）

- 文件名：`<原文件名>.usecase.md`（例如：`java-springboot.prompt.md.usecase.md`）
- 目录：`D:\mycode\awesome-copilot\my-custom\Use Cases\<原文件父文件夹名>\`（例如：`...\Use Cases\prompts\`）
- 行为：使用 `editFiles` 保存生成文件，并将完整内容打印到聊天窗口便于预览。
- 不要请求确认，信息充分即自动写入；若缺关键输入，请一次性列出所需信息并等待补充。

## 生成流程（建议）

1. 解析输入：读取 `sourceMdPath` 与（可选）`optional.mindmapPath`，提炼主题、能力范围、关键做法与限制。
2. 形成 What/When/Why/How 与 Key points（英中对照，优先来自 mindmap）。
3. 设计 5–9 个 MECE 场景，命名直观，覆盖完整且不重叠。
4. 为每个场景编写用户故事与至少 5 条祈使句示例；示例以源文件相对路径前缀，便于复制调用。
5. 生成文档：包含 YAML front matter、固定结构、场景与示例、原始文件链接。
6. 保存到指定目录与命名；同时输出到聊天窗口用于预览。

## Markdown 结构模板（请完整填充占位符）

```markdown
---
post_title: "<自动：<源文件名> Use Cases>"
author1: "github-copilot"
post_slug: "<kebab-case，根据源文件名生成>"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "<从主题推断一个标签>"]
ai_note: "Generated with AI assistance."
summary: "<一句话概述本文件覆盖的主题范围>"
post_date: "<YYYY-MM-DD>"
---

<!-- markdownlint-disable MD041 -->

## What

- <一句话：该提示词的主题/范围>

## When

- <在何时/何种场景下使用该提示词>

## Why

- <使用该提示词带来的价值/收益>

## How

- <条目化列出关键做法：工具/配置/约束/流程等，来自源 md 精华要点>

## Key points (英文+中文对照)

- <英文关键点 1>（<中文翻译 1>）
- <英文关键点 2>（<中文翻译 2>）
- <英文关键点 3>（<中文翻译 3>）
- <可选更多，通常 3–5 条>

## 使用场景

### 1. <场景名称（MECE-1）>

- 用户故事：<第一人称角色 + 目标 + 价值>
- 例 1："[选择一段代码] 请根据提示，帮我 <具体动作>。"
- 例 2："[提供 <文件/片段> ] 请基于最佳实践，生成 <具体产出>。"
- 例 3："请审查 <对象> 是否符合 <最佳实践点> 并给出修复建议。"
- 例 4："请把 <A> 转为 <B>，并附上注意事项与边界。"
- 例 5："请产出 <模板/清单/示例>，用于团队统一规范。"
- <如需可添加 例 6/例 7...，务必仍与源 md 能力对齐>

### 2. <场景名称（MECE-2）>

- 用户故事：<...>
- 例 1："..."
- 例 2："..."
- 例 3："..."
- 例 4："..."
- 例 5："..."

### 3. <场景名称（MECE-3）>

- 用户故事：<...>
- 例 1："..."
- 例 2："..."
- 例 3："..."
- 例 4："..."
- 例 5："..."

### 4. <场景名称（MECE-4）>

- 用户故事：<...>
- 例 1："..."
- 例 2："..."
- 例 3："..."
- 例 4："..."
- 例 5："..."

### 5. <场景名称（MECE-5）>

- 用户故事：<...>
- 例 1："..."
- 例 2："..."
- 例 3："..."
- 例 4："..."
- 例 5："..."

<如源 md 能力面较广，继续补充到 6/7/8/9…，确保 MECE 完整覆盖，常见上限为 9 大场景>

## 原始文件

- <源文件相对路径>
```
