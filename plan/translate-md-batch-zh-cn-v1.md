---
goal: instructions、chatmodes、prompts 目录未翻译 Markdown 文档批量本地化到 zh-cn
version: 1.0
date_created: 2025-08-11
status: 'In progress'
tags: [localization, translation, markdown]
---

# Introduction

![Status: In progress](https://img.shields.io/badge/status-In%20progress-yellow)

本计划旨在将 `instructions`、`chatmodes`、`prompts` 目录下所有尚未翻译为简体中文的 Markdown 文档，批量翻译并存放到 `localization/zh-cn` 对应目录结构下。已翻译文件无需重复处理。

## 1. Requirements & Constraints

- **REQ-001**: 必须遍历 instructions、chatmodes、prompts 目录下所有 .md 文件。
- **REQ-002**: 仅对未在 localization/zh-cn/ 下存在的同名文件进行翻译。
- **REQ-003**: 翻译内容需完整、准确，结构与原文一致。
- **REQ-004**: 所有图片、文档链接按规范处理。
- **REQ-005**: 结尾添加本地化免责声明（中文）。
- **CON-001**: 不得遗漏任何段落、标题、代码块。
- **CON-002**: 不得重复翻译已存在的文件。
- **GUD-001**: 参考 localization.instructions.md 规范。

## 2. Implementation Steps

| Phase | Task ID | Description | File Path | Validation |
|-------|---------|-------------|-----------|------------|
| 1 | TASK-001 | 遍历 instructions 目录，收集未翻译 .md 文件 | instructions/ | 生成待翻译文件清单 |
| 1 | TASK-002 | 遍历 chatmodes 目录，收集未翻译 .md 文件 | chatmodes/ | 生成待翻译文件清单 |
| 1 | TASK-003 | 遍历 prompts 目录，收集未翻译 .md 文件 | prompts/ | 生成待翻译文件清单 |
| 2 | TASK-004 | 对每个待翻译文件进行全文翻译 | localization/zh-cn/ | 译文与原文行数、结构一致 |
| 2 | TASK-005 | 检查并修正所有文档链接、图片链接 | localization/zh-cn/ | 链接指向本地化或原始资源 |
| 2 | TASK-006 | 添加本地化免责声明（中文） | localization/zh-cn/ | 免责声明存在且为中文 |
| 3 | TASK-007 | 校验所有译文完整性与准确性 | localization/zh-cn/ | 行数、段落、结构与原文一致 |
| 3 | TASK-008 | 生成翻译完成报告 | plan/ | 报告内容准确 |

## 3. Alternatives

- **ALT-001**: 全量覆盖翻译（不区分已翻译与否）——低效，易覆盖人工修订内容。
- **ALT-002**: 仅人工逐个指定文件翻译——效率低，易遗漏。

## 4. Dependencies

- **DEP-001**: localization.instructions.md 规范文件
- **DEP-002**: 原始 instructions、chatmodes、prompts 目录下的 .md 文件

## 5. Files

- **FILE-001**: instructions/*.md
- **FILE-002**: chatmodes/*.md
- **FILE-003**: prompts/*.md
- **FILE-004**: localization/zh-cn/instructions/*.md
- **FILE-005**: localization/zh-cn/chatmodes/*.md
- **FILE-006**: localization/zh-cn/prompts/*.md
- **FILE-007**: plan/translate-md-batch-zh-cn-v1.md

## 6. Testing

- **TEST-001**: 检查所有待翻译文件均已生成对应 zh-cn 译文
- **TEST-002**: 校验译文与原文行数、结构、段落一致
- **TEST-003**: 检查免责声明存在且为中文

## 7. Risks & Assumptions

- **RISK-001**: 目录结构或文件名变动导致遗漏
- **ASSUMPTION-001**: localization/zh-cn/ 下所有同名文件均为已翻译，无需重复处理

## 8. Related Specifications / Further Reading

- [localization.instructions.md](../instructions/localization.instructions.md)

## 9. Execution Status (滚动状态)

**当前状态**：

已完成：
	- Batch 1：chatmodes 3 + prompts 2 翻译 & QA（reports/prompts-translation-batch1.md）
	- Prompts 全量 inventory 建立（plan/prompts-translation-inventory.md）
	- Batching 策略文件（plan/prompts-translation-batches.md）
	- Batch 2：prompts 5 个翻译 & QA（reports/prompts-translation-batch2.md）

当前阶段聚焦：prompts（71 个目标文件中的 7 个已完成）
进度（prompts 范围）：7 / 71 = 9.86%
剩余：64 prompts 待翻译；instructions、其余 chatmodes 将在 prompts 完成后恢复执行

### 里程碑

- Batch 1：前 5 个（混合）翻译与 QA ✅
- Batch 2：prompts Batch 2 (5) ✅
- 下一个里程碑：Batch 3（计划增加规模至 8–10 prompts）

### 后续行动（Next Actions）

1. 规划 Batch 3（扩大至 8–10 prompts）
2. 选择 Batch 3 文件并记录到 batches 文件
3. 执行 Batch 3 翻译与 QA
4. （可选）开发结构对比自动化脚本

### 质量保证记录

前两批零结构差异；front matter 与 disclaimer 均符合规范。

### 指标计划

- 下一批增加到 8–10 文件
- 保持每批产出 QA + 累计进度刷新

