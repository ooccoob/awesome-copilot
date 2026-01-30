---
post_title: "atlassian-requirements-to-jira — 用例"
post_slug: "atlassian-requirements-to-jira-use-cases"
tags: ['chatmode','atlassian','jira','usecase']
ai_note: '根据 chatmodes/atlassian-requirements-to-jira.chatmode.md 生成的中文用例'
summary: '将产品需求或文档快速转换为 Jira 史诗/故事/任务和验收标准的场景示例。'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

什么

- 把自由文本的需求说明或 Word/Confluence 文档结构化为 Jira 可导入的工作项（epic/story/task）并生成验收标准。

何时

- 在需求评审后需要快速生成 backlog 条目或在产品迭代前准备 Sprint 规划内容时。

为什么

- 节省人工拆分与填写工作，提高 backlog 一致性并确保验收标准可测试。

如何

- 提供需求描述或 Confluence 页面链接并指定拆分粒度，系统输出 CSV/JSON 可导入的 Jira 条目及验收标准模板。

关键要点 (EN / ZH)

- EN: Break down requirements to epics/stories/tasks; create acceptance criteria; produce importable CSV/JSON.
- ZH: 将需求拆解为史诗/故事/任务；生成验收标准；输出可导入的 CSV/JSON。

示例场景

1) 从 PRD 生成 Story 列表
- 示例提示："把下面的 PRD 段落拆成最多 12 个故事，每个故事包括标题、描述与验收标准。"
- 预期产出：12 条 story 的 CSV，可直接导入 Jira。

2) 为每个故事生成估算与依赖
- 示例提示："为下列故事建议 Story Points（1/2/3/5/8）并标出横向依赖。"
- 预期产出：每个 story 的估算与依赖关系表。

3) 生成 Sprint 划分建议
- 示例提示："把这些 stories 按 2 周 Sprint 分组并生成每 Sprint 的目标。"
- 预期产出：Sprint 列表与目标说明。

4) 批量导入模板
- 示例提示："输出用于 Jira CSV 导入的字段映射及样例行。"
- 预期产出：CSV 模板示例与字段说明。

5) 转换验收标准为测试用例骨架
- 示例提示："为每个验收标准生成基本的测试步骤骨架（手动/自动）。"
- 预期产出：每个 story 对应的测试用例骨架。

原始 chatmode: ../../../../chatmodes/atlassian-requirements-to-jira.chatmode.md
---
post_title: "atlassian-requirements-to-jira.chatmode.md Use Cases"
author1: "github-copilot"
post_slug: "atlassian-requirements-to-jira-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "jira", "requirements", "epic", "user-story", "change-management"]
ai_note: "Generated with AI assistance."
summary: "将需求文档安全地转化为 Jira Epics 与 User Stories，内置去重、变更管理、审批关口与批量限流。"
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 使用 Atlassian MCP 工具链，把用户显式提供的需求文档解析为结构化的 Jira 事项：按特性生成 Epics，并分解出带验收标准的 User Stories，支持重复检测、差异预览与用户批准后再落库。

## When

- 需要将一份或多份需求说明（Markdown/纯文本等）快速转化为 Jira 待办，并保持与现有条目一致且无重复时。
- 需要在迭代中对已有条目进行“受控更新”（预览差异 → 明确批准）时。

## Why

- 以标准化流程减少手工录入与重复劳动，同时在权限校验、JQL 注入防护、字符转义、批量限流（≤20 Epics、≤50 Stories/批）等方面保障安全与稳定。

## How

- 前置：验证 Atlassian MCP Server 安装、连接可用、权限足够；交互选择 Jira Project Key 与偏好（标签、优先级、估点字段等）。
- 分析：仅读取用户显式提供的文档（类型与大小校验），抽取特性→Epic、功能点→Story、验收标准与依赖。
- 去重：以“已清洗”的 JQL 查询现有 Epics/Stories，计算相似度并给出合并/更新/跳过建议。
- 审批：全部变更先展示预览（新增/修改/删除差异），需用户确认后方可执行。
- 执行：在速率限制与权限校验下批量创建/更新，自动建立 Epic-Story 关联、打标签、应用优先级与估点；输出操作日志与回滚建议。

## Key points (英文+中文对照)

- Explicit approval required（所有创建/更新需明确批准）
- Batch limits: 20 epics / 50 stories（批量限流）
- Sanitize JQL & escape content（清洗 JQL 与转义描述/摘要）
- Permission validated before ops（操作前校验权限）
- Preview diffs, then apply（先预览差异，再执行）

## 使用场景

### 1. 环境准备与项目选择（MCP setup & project selection）

- 用户故事：作为集成者，我要确保 MCP 已就绪、能列出可见项目并验证我对目标项目具有创建权限。
- 例 1："检查 MCP 安装并测试连接，如失败请给出配置步骤与重试建议。"
- 例 2："列出可见项目（键/名称/描述），提示我选择 Project Key。"
- 例 3："验证我在所选项目上的创建/更新权限，不足则给出替代方案。"
- 例 4："收集默认标签、优先级映射与估点字段启用情况。"
- 例 5："保存本次会话的项目偏好，用于后续批量操作。"

### 2. 从需求到 Epics/Stories（Document → backlog）

- 用户故事：作为需求方，我提供一份≤1MB 的合法需求文档，希望自动拆分为 Epics 与 Stories 并附带验收标准与 DoD。
- 例 1："校验并仅读取我明确提供的文件，拒绝越界访问。"
- 例 2："抽取主要特性为 Epics，并给出业务价值/范围/成功标准。"
- 例 3："为每个 Epic 分解 Stories（用户视角标题、背景、Gherkin 风格验收标准）。"
- 例 4："在 Story 中标注非功能性与依赖，并附上来源章节的追溯链接。"
- 例 5："生成预览清单（待创建 Epics/Stories 数量与摘要），等待我批准。"

### 3. 重复检测与变更管理（Duplicate detection & change management）

- 用户故事：作为维护者，我要避免重复创建，并以差异视图受控更新既有条目。
- 例 1："使用已清洗的 JQL 在指定项目中搜索相似 Epics/Stories。"
- 例 2："展示相似项（标题/描述/验收标准/标签）与相似度说明。"
- 例 3："对需更新的条目生成差异预览（+新增，-删除，~修改）。"
- 例 4："请求我选择：跳过/合并/更新/创建新条目。"
- 例 5："仅在我选择并确认后执行更新，并记录操作轨迹。"

### 4. 批量创建与关联（Rate-limited batch create & linking）

- 用户故事：作为执行者，我希望在限流与权限校验下安全批量创建，并自动完成故事与史诗的关联及属性设置。
- 例 1："遵守批量限制：每批最多 20 个 Epics、50 个 Stories。"
- 例 2："按顺序创建：先 Epics 后 Stories，并建立 Epic Link。"
- 例 3："应用标签/优先级/估点等项目偏好与约定。"
- 例 4："对描述与摘要进行长度限制与特殊字符转义。"
- 例 5："输出含链接的操作日志与回滚要点。"

### 5. 质量校验与守卫（Quality checks & guards）

- 用户故事：作为质量负责人，我需要保证条目质量与安全边界不被突破。
- 例 1："Stories 自动检查 INVEST 与验收标准数量（≥3）。"
- 例 2："DoD 覆盖：单测/集成/文档/预发验证/可达性（如适用）。"
- 例 3："拒绝创建包含脚本/命令等不当内容的描述。"
- 例 4："严格限制范围：仅项目管理操作，拒绝系统/权限/配置修改。"
- 例 5："所有 JQL 输入均参数化与转义，限定在当前项目。"

## 原始文件

- [chatmodes/atlassian-requirements-to-jira.chatmode.md](../../../chatmodes/atlassian-requirements-to-jira.chatmode.md)
