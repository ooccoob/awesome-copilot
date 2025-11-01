## What / When / Why / How

- What: 需求文档 → Jira 史诗/用户故事 自动化助手（含去重与变更预览）
- When: 批量将产品/需求文档转化为可执行 backlog 时
- Why: 降低重复、显式审批、保障项目治理与可追溯
- How: 校验 MCP/权限→项目选择→解析文档→重复检测→预览→审批后分批创建/更新

## Key Points

- 严格边界：仅处理需求到 backlog；禁止系统/权限等越权操作
- 安全与限流：JQL 输入消毒、长度限制、批量上限（20 epics/50 stories）
- 变更管理：差异对比、显式确认、批量分组提交
- 追溯：为每个项关联来源文档片段与标签

## Compact Map

- 前置
  - 校验 MCP 连接与权限
  - 选择项目与偏好（labels/优先级/估点）
- 解析
  - 提取功能→分组为 epics
  - 分解为 stories（包含 DoD/AC）
- 去重
  - 基于标题/描述/AC 相似度
  - 给出处理选项（跳过/合并/更新/新建）
- 执行
  - 显示 diff→审批→分批创建/更新
  - 建立 Epic↔Story 关联

## Example Questions (10+)

- 你的 Jira 项目 Key 是什么？需要默认标签/优先级/估点吗？
- 需求文档的来源与格式？是否超过 1MB 需要拆分？
- 去重策略偏好：相似则合并、更新还是新建？
- Epic 与 Story 的命名/模板是否有团队规范？
- 接受哪些 Definition of Done 与 AC 模板？
- 是否允许更新已有项的描述/标签/优先级？
- 分批创建的粒度与顺序如何设置以避免速率限制？
- 需要生成哪些报表或 Dashboard 以便跟踪？
- 失败回滚策略是什么（撤销或变更标记）？
- 权限不足/连接失败时的处理流程？
- 如何标注与需求章节的溯源引用？

---
Source: d:\mycode\awesome-copilot\chatmodes\atlassian-requirements-to-jira.chatmode.md
Generated: {{timestamp}}
