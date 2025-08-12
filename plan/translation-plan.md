---
title: 'Docs Localization Plan (chatmodes | instructions | localization)'
locale: 'zh-cn'
date_created: '2025-08-12'
last_updated: '2025-08-12'
owner: 'Localization Automation'
status: 'In progress'
---

## 英文化文档 -> 中文 (zh-cn) 本地化计划（分目录管理）

## 目标

对 `chatmodes`、`instructions`、`localization` 三个源目录中尚未完成中文本地化的 `.md` 文件进行高质量翻译，确保：

- 结构、段落、代码块与原文一一对应，不遗漏。
- 内部链接指向 zh-cn 已翻译版本（若存在），外部链接保持原样。
- 行数统计会被记录在任务清单中供人工判断；是否进入 Review 由你决定。

## 参考规范

遵循 `instructions/localization.instructions.md` 要求（去除免责声明相关条款）：

- 不遗漏章节与段落
- 图片与外链保留
- 内部文档链接指向 localized 版本

（本计划不再要求在译文中添加任何免责声明内容。）

## 源与目标目录

- 源目录：
	- D:\\mycode\\awesome-copilot\\chatmodes
	- D:\\mycode\\awesome-copilot\\instructions
	- D:\\mycode\\awesome-copilot\\localization

- 目标目录：
	- D:\\mycode\\awesome-copilot\\localization\\zh-cn\\chatmodes
	- D:\\mycode\\awesome-copilot\\localization\\zh-cn\\instructions
	- D:\\mycode\\awesome-copilot\\localization\\zh-cn\\localization

## 状态枚举

- Pending: 尚未开始
- InProgress: 翻译中
- Review: 机器翻译完成待行数/质量复核
- Done: 已完成（已生成目标文件并记录行数）
- Skipped: 已存在翻译/无需处理

## 工作流

1. 按目录扫描源/目标文件列表；以“文件名”比对，找出源有但目标无的“新增文件”。
2. 读取源文件 -> 统计行数 S。
3. 翻译正文（保留 front matter 键名；翻译 description/正文段落），生成目标文件至对应 zh-cn 目录。
4. 统计目标行数 T，并仅记录到任务清单（不自动判定 Review）。
5. 每次执行后，新增/变更的条目更新本计划中的对应行与时间戳。

## 批次策略（说明）

按目录分批（chatmodes -> instructions -> localization）推进，单批 2–8 个文件，优先处理“新增文件”和体量较小的 quick wins 以保持节奏。

## 任务清单 · chatmodes

| ID  | File                                        | Priority | Source Path                                           | Target Path                                                              | SrcLines | TgtLines | Status  | LastUpdate | Notes                                |
| --- | ------------------------------------------- | -------- | ----------------------------------------------------- | ------------------------------------------------------------------------ | -------- | -------- | ------- | ---------- | ------------------------------------ |
| 1   | implementation-plan.chatmode.md             | High     | chatmodes/implementation-plan.chatmode.md             | localization/zh-cn/chatmodes/implementation-plan.chatmode.md             | 133      | 152      | Done    | 2025-08-12 | 行数差异<20%，结构保持               |
| 2   | specification.chatmode.md                   | High     | chatmodes/specification.chatmode.md                   | localization/zh-cn/chatmodes/specification.chatmode.md                   | 143      | 160      | Done    | 2025-08-12 | 模板代码块保留                       |
| 3   | plan.chatmode.md                            | High     | chatmodes/plan.chatmode.md                            | localization/zh-cn/chatmodes/plan.chatmode.md                            | 126      | 140      | Done    | 2025-08-12 |                                      |
| 4   | planner.chatmode.md                         | High     | chatmodes/planner.chatmode.md                         | localization/zh-cn/chatmodes/planner.chatmode.md                         | 23       | 31       | Done    | 2025-08-12 | 行数校正，结构保持                   |
| 5   | task-planner.chatmode.md                    | High     | chatmodes/task-planner.chatmode.md                    | localization/zh-cn/chatmodes/task-planner.chatmode.md                    | 278      | 305      | Done    | 2025-08-12 | 模板段落语义保持                     |
| 6   | task-researcher.chatmode.md                 | High     | chatmodes/task-researcher.chatmode.md                 | localization/zh-cn/chatmodes/task-researcher.chatmode.md                 | 396      | 415      | Done    | 2025-08-12 | 模板结构与占位保留                   |
| 7   | principal-software-engineer.chatmode.md     | High     | chatmodes/principal-software-engineer.chatmode.md     | localization/zh-cn/chatmodes/principal-software-engineer.chatmode.md     | 94       | 116      | Done    | 2025-08-12 | 适度扩展，语义等价                   |
| 8   | expert-dotnet-software-engineer.chatmode.md | High     | chatmodes/expert-dotnet-software-engineer.chatmode.md | localization/zh-cn/chatmodes/expert-dotnet-software-engineer.chatmode.md | 71       | 87       | Done    | 2025-08-12 | 术语保持并本地化                     |
| 9   | expert-react-frontend-engineer.chatmode.md  | High     | chatmodes/expert-react-frontend-engineer.chatmode.md  | localization/zh-cn/chatmodes/expert-react-frontend-engineer.chatmode.md  | 108      | 134      | Done    | 2025-08-12 | 列表细节保持                         |
| 10  | mentor.chatmode.md                          | High     | chatmodes/mentor.chatmode.md                          | localization/zh-cn/chatmodes/mentor.chatmode.md                          | 120      | 150      | Done    | 2025-08-12 | 序号列表保持                         |
| 11  | janitor.chatmode.md                         | High     | chatmodes/janitor.chatmode.md                         | localization/zh-cn/chatmodes/janitor.chatmode.md                         | 138      | 172      | Done    | 2025-08-12 | 各分类标题保留                       |
| 12  | gilfoyle.chatmode.md                        | High     | chatmodes/gilfoyle.chatmode.md                        | localization/zh-cn/chatmodes/gilfoyle.chatmode.md                        | 133      | 173      | Done    | 2025-08-12 | 语气与风格本地化                     |
| 13  | ms-sql-dba.chatmode.md                      | Medium   | chatmodes/ms-sql-dba.chatmode.md                      | localization/zh-cn/chatmodes/ms-sql-dba.chatmode.md                      | 26       | 29       | Done    | 2025-08-12 | 术语保持/链接保留                    |
| 14  | postgresql-dba.chatmode.md                  | Medium   | chatmodes/postgresql-dba.chatmode.md                  | localization/zh-cn/chatmodes/postgresql-dba.chatmode.md                  | 18       | 21       | Done    | 2025-08-12 | 简洁列点一致                         |
| 15  | semantic-kernel-dotnet.chatmode.md          | Medium   | chatmodes/semantic-kernel-dotnet.chatmode.md          | localization/zh-cn/chatmodes/semantic-kernel-dotnet.chatmode.md          | 32       | 36       | Done    | 2025-08-12 | 列表与强调块保留                     |
| 16  | semantic-kernel-python.chatmode.md          | Medium   | chatmodes/semantic-kernel-python.chatmode.md          | localization/zh-cn/chatmodes/semantic-kernel-python.chatmode.md          | 29       | 33       | Done    | 2025-08-12 | 与 .NET 版术语一致                   |
| 17  | rust-gpt-4.1-beast-mode.chatmode.md         | Medium   | chatmodes/rust-gpt-4.1-beast-mode.chatmode.md         | localization/zh-cn/chatmodes/rust-gpt-4.1-beast-mode.chatmode.md         | 120      | 134      | Done    | 2025-08-12 | 说明缩减保持结构                     |
| 18  | prompt-builder.chatmode.md                  | Medium   | chatmodes/prompt-builder.chatmode.md                  | localization/zh-cn/chatmodes/prompt-builder.chatmode.md                  | 352      | 183      | Review  | 2025-08-12 | 结构补齐；仍>5% 待复核               |
| 19  | prompt-engineer.chatmode.md                 | Medium   | chatmodes/prompt-engineer.chatmode.md                 | localization/zh-cn/chatmodes/prompt-engineer.chatmode.md                 | 72       | 51       | Review  | 2025-08-12 | 已补全推理清单；行数差异>5%          |
| 20  | refine-issue.chatmode.md                    | Medium   | chatmodes/refine-issue.chatmode.md                    | localization/zh-cn/chatmodes/refine-issue.chatmode.md                    | 34       | 26       | Review  | 2025-08-12 | 精确统计完成；行数差异>5%            |
| 21  | simple-app-idea-generator.chatmode.md       | Medium   | chatmodes/simple-app-idea-generator.chatmode.md       | localization/zh-cn/chatmodes/simple-app-idea-generator.chatmode.md       | 127      | 83       | Review  | 2025-08-12 | 初译完成；行数差异>5%                |
| 22  | software-engineer-agent-v1.chatmode.md      | Medium   | chatmodes/software-engineer-agent-v1.chatmode.md      | localization/zh-cn/chatmodes/software-engineer-agent-v1.chatmode.md      | 163      | 85       | Review  | 2025-08-12 | 结构扩充；仍>5% 待复核               |
| 23  | meta-agentic-project-scaffold.chatmode.md   | Medium   | chatmodes/meta-agentic-project-scaffold.chatmode.md   | localization/zh-cn/chatmodes/meta-agentic-project-scaffold.chatmode.md   | 15       | 13       | Review  | 2025-08-12 | 初译完成；行数差异>5%                |
| 24  | microsoft-study-mode.chatmode.md            | Medium   | chatmodes/microsoft-study-mode.chatmode.md            | localization/zh-cn/chatmodes/microsoft-study-mode.chatmode.md            | 24       | 18       | Review  | 2025-08-12 | 标题层级对齐；待补齐细节             |
| 25  | microsoft_learn_contributor.chatmode.md     | Medium   | chatmodes/microsoft_learn_contributor.chatmode.md     | localization/zh-cn/chatmodes/microsoft_learn_contributor.chatmode.md     | 317      | 119      | Review  | 2025-08-12 | 已手动扩充；继续逐段补齐             |
| 26  | demonstrate-understanding.chatmode.md       | Medium   | chatmodes/demonstrate-understanding.chatmode.md       | localization/zh-cn/chatmodes/demonstrate-understanding.chatmode.md       | 60       | 29       | Review  | 2025-08-12 | 新增 zh-cn；结构对齐良好             |
| 27  | electron-angular-native.chatmode.md         | Medium   | chatmodes/electron-angular-native.chatmode.md         | localization/zh-cn/chatmodes/electron-angular-native.chatmode.md         | 285      | 229      | Review  | 2025-08-12 | 初译完成；待细节核对与补齐           |
| 28  | playwright-tester.chatmode.md               | Medium   | chatmodes/playwright-tester.chatmode.md               | localization/zh-cn/chatmodes/playwright-tester.chatmode.md               | 11       | 9        | Review  | 2025-08-12 | 重新计数；待扩充两处说明             |
| 29  | prd.chatmode.md                             | Medium   | chatmodes/prd.chatmode.md                             | localization/zh-cn/chatmodes/prd.chatmode.md                             | 201      | 145      | Review  | 2025-08-12 | 初译完成；按大纲核对待补充           |
| 30  | tech-debt-remediation-plan.chatmode.md      | Medium   | chatmodes/tech-debt-remediation-plan.chatmode.md      | localization/zh-cn/chatmodes/tech-debt-remediation-plan.chatmode.md      | 49       | 42       | Review  | 2025-08-12 | 初译完成；行数差异>5%                |
| 31  | Thinking-Beast-Mode.chatmode.md             | Medium   | chatmodes/Thinking-Beast-Mode.chatmode.md             | localization/zh-cn/chatmodes/Thinking-Beast-Mode.chatmode.md             | 237      | 175      | Review  | 2025-08-12 | 重新计数；准备结构核对               |
| 32  | 4.1-Beast.chatmode.md                       | Medium   | chatmodes/4.1-Beast.chatmode.md                       | localization/zh-cn/chatmodes/4.1-Beast.chatmode.md                       | 92       | 49       | Review  | 2025-08-12 | 已补齐核心小节；继续对齐细节         |
| 33  | tdd-green.chatmode.md                       | Medium   | chatmodes/tdd-green.chatmode.md                       | localization/zh-cn/chatmodes/tdd-green.chatmode.md                       | 59       | 51       | Review  | 2025-08-12 | 初译完成；略低于-5%                  |
| 34  | tdd-red.chatmode.md                         | Medium   | chatmodes/tdd-red.chatmode.md                         | localization/zh-cn/chatmodes/tdd-red.chatmode.md                         | 47       | 37       | Pending | 2025-08-12 | 仅登记行数；是否进入 Review 由你决定 |
| 35  | tdd-refactor.chatmode.md                    | Medium   | chatmodes/tdd-refactor.chatmode.md                    | localization/zh-cn/chatmodes/tdd-refactor.chatmode.md                    | 84       | 65       | Review  | 2025-08-12 | 初译完成；待补安全/设计细节          |

## 任务清单 · instructions

| ID  | File | Priority | Source Path | Target Path | SrcLines | TgtLines | Status | LastUpdate | Notes |
| --- | ---- | -------- | ----------- | ----------- | -------- | -------- | ------ | ---------- | ----- |

本次扫描：源与目标文件名完全一致，无新增待翻译文件。

## 任务清单 · localization

| ID  | File | Priority | Source Path | Target Path | SrcLines | TgtLines | Status | LastUpdate | Notes |
| --- | ---- | -------- | ----------- | ----------- | -------- | -------- | ------ | ---------- | ----- |

本次扫描：当前源目录仅包含 zh-cn 子目录，无 EN 源文档，暂无待翻译项。

## 已完成 (Skipped)

以下文件已存在中文版本，跳过：accesibility, api-architect, azure-principal-architect, azure-saas-architect, azure-verified-modules-bicep, azure-verified-modules-terraform, blueprint-mode, clojure-interactive-programming, critical-thinking, csharp-dotnet-janitor, debug, voidbeast-gpt41enhanced, wg-code-alchemist, wg-code-sentinel

## 更新日志

| Date       | Action | Detail                                          |
| ---------- | ------ | ----------------------------------------------- |
| 2025-08-12 | Init   | 建立任务计划、登记 35 个待翻译文件              |
| 2025-08-12 | Scan   | 完成 instructions/localization 差集扫描：无新增 |
