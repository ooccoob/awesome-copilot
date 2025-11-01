## 专业 Prompt 构建器（思维导图）

- What
  - 以问答方式收集需求并生成生产级 .prompt.md（含 front matter/tool/model）
- When
  - 新建面向 Copilot 的任务化 Prompt
- Why
  - 结构清晰、工具集成、质量与可维护性
- How
  - 身份/目的→角色→任务→上下文变量→步骤→输出→工具→技术配置→质量标准
  - 产出模板遵循仓库范式，便于复用与扩展

- Key Points (CN/EN)
  - Front matter; Tools
  - Persona; Steps
  - Output; Validation

- Example Questions (≥10)
  1) 预期文件名与一句话描述？
  2) Persona 的技术栈/年限/职责？
  3) 主要/次要任务与验收标准？
  4) 输入/上下文变量与 workspace 依赖？
  5) 需要哪些工具（读/改/搜索/执行）？
  6) 输出格式与是否创建/修改文件？
  7) 约束（风格/规范/依赖/限制）？
  8) 质量与校验环节（测试/lint/评审）？
  9) 失败模式与回退策略？
  10) 是否需指定运行模式与模型？

- Compact Mind Map
  - 目的→角色→任务→上下文→步骤→输出→工具→质量

- Source: prompts/prompt-builder.prompt.md
- Generated: 2025-10-17
