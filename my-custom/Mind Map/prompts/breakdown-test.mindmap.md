## 文档综述（What/When/Why/How）
- What：面向 GitHub 项目的测试规划与质量保障提示词，输出测试策略、任务分解、QA 计划与模板
- When：有 PRD/技术拆解/实现计划等产物，需要建立覆盖全流程、全类型测试与质量门禁时
- Why：以 ISTQB + ISO/IEC 25010 为框架，系统化定义测试范围、类型、质量特性与度量，提升交付质量
- How：基于输入文档生成三份产物（test-strategy.md、test-issues-checklist.md、qa-plan.md），内置分解清单、度量与模板

## 示例提问（Examples）
- “请基于该功能 PRD 和技术拆解生成 test-strategy.md，并给出测试类型覆盖矩阵与风险评估”
- “为此实现计划拆分可执行测试任务，按单元/集成/E2E/性能/安全生成 Issue 清单与估算”
- “依据 ISO 25010 制定质量门禁与度量阈值，并配套 QA 计划与检查项”

## 结构化要点（CN/EN）
- 过程/Process：计划→监控→分析→设计→实现→执行→完成 | Plan→Monitor→Analyze→Design→Implement→Execute→Complete
- 类型/Types：功能/非功能/结构/变更回归 | Functional/Non-functional/Structural/Change-related
- 设计/Design：等价类/边界/判表/状态/经验 | EP/BVA/Decision Table/State/XP-based
- 质量/Quality：功能性、性能、兼容、易用、可靠、安全、可维护、可移植 | ISO 25010
- 工具/Tools：Playwright E2E、覆盖率阈值、CI/CD 集成、模板化 Issue

## 中文思维导图
- 测试策略
  - 范围/目标/方法
  - ISTQB 设计技术选择
  - 测试类型覆盖矩阵
- ISO 25010 质量
  - 特性优先级与度量
  - 质量门禁（入口/出口）
- 环境与数据
  - 环境/数据/工具/流水线
- 任务分解与估算
  - 单元/集成/E2E/性能/安全/可及性
  - 依赖/关键路径/资源分配
- Issue 模板与度量
  - 模板合规/标签/优先级
  - 覆盖率/缺陷密度/性能阈值

## 溯源信息
- 源文件：d:\mycode\awesome-copilot\prompts\breakdown-test.prompt.md
- 生成时间：${new Date().toISOString()}
