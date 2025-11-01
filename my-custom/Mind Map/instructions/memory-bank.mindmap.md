## Memory Bank 作业规程（速览）

### 这是什么/何时使用/为什么/如何做
- What: 可复用的项目“记忆库”结构与工作流，确保会话重置后可无缝继续。
- When: 每个任务开始必须阅读；实现/决策后更新；收到“update memory bank”指令时全量审阅更新。
- Why: 将上下文、决策、任务进度外化为文档，降低遗忘与沟通成本。
- How: 维护核心文件（projectbrief、productContext、activeContext、systemPatterns、techContext、progress、tasks/），按“计划/执行/任务管理”流程迭代。

### 关键要点
- 目录与层次: Core（7 个）+ 可选扩展；文件间存在依赖关系（brief→context→active→progress/tasks）。
- 任务管理: tasks/ 按 TASKID 独立文件，含 _index.md 索引（状态/更新时间/下一步）。
- 更新触发: 发现新模式/重要改动/显式请求/需要澄清时；强调 activeContext、progress、tasks/。
- 指南文件: instructions 记录学习与偏好；形成“发现→验证→沉淀→应用”的闭环。
- 更新规范: 同步更新总体状态、子任务表、每日进展日志，并回填索引。

### 紧凑脑图
- 核心: brief→product/system/tech→active→progress+tasks
- 流程: 计划模式/执行模式/任务索引
- 触发: 新模式/大改动/显式更新命令
- 落地: 严格双写（表格状态+日志叙述）

### 开发者示例问题（≥10）
- 新建项目时缺少 projectbrief.md 应如何初始化？
- activeContext 与 progress 的边界与更新优先序？
- tasks/_index.md 的排序与筛选策略如何设计？
- “双写”时如何避免状态与日志不一致？
- 发现新模式时的最小可行记录模板是什么？
- 当日仅微小进展是否也需要进展日志？
- 如何将 PR 审查要点同步到 instructions？
- 如何追溯某决策的上下文来源与影响面？
- 跨任务共享信息应放在何处以避免重复？
- 批量重命名任务文件时的索引维护策略？

—
Source: d:\mycode\awesome-copilot\instructions\memory-bank.instructions.md | Generated: 2025-10-17
