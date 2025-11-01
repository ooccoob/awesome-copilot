## What
- 目标：基于新需求/变更更新实现计划文件（/plan/*.md），产出机器可执行的、分阶段的任务清单。
- 约束：确定性语言、零歧义；模板固定；包含状态徽章与校验标准。

## When
- 功能新增、重构、升级依赖、架构/流程变更落地前。

## Why
- 让 AI/人类均可直接按计划执行，减少沟通成本与偏差。

## How
- 读取 `${file}` → 严格套用模板 → 拆分独立 Phase/Tasks（可并行但标注依赖）。
- 对象：明确文件路径/函数/实现细节/变量值；标注验证标准与完成条件。
- 命名：REQ-/TASK-/GOAL-/ALT-/DEP-/FILE-/TEST-/RISK-/ASSUMPTION- 前缀统一。
- 输出：合法 Front Matter + 固定章节 + 表格列齐全，无占位符残留。

## Key Points
- 状态：Completed/In progress/Planned/Deprecated/On Hold + 徽章。
- 机器可读：表格/列表/结构化标识，避免含糊表述。
- 版本化：命名规范 [purpose]-[component]-[version].md。

## Compact Map
- Analyze changes → Update sections → Validate template → Save /plan/*.md

## Example Questions (10+)
- 如何把一组重构任务拆到可并行且独立验证的 Phase？
- 任务行里需要哪些“可自动验证”的完成标准？
- 如何引用具体函数/路径并避免歧义？
- 多仓或多模块时，如何标注跨模块依赖？
- 状态从 Planned 升到 In progress 的触发条件是什么？
- 如何组织“回滚/替代方案”并入 Alternatives？
- 如何将测试策略与 CI 流水线钩住？
- 如何给版本字段与文件名做一致性校验？
- 如何在审阅环节校验模板完整性与无占位符？
- 怎样记录人工审批节点与暂停条件？
- 计划更新的变更历史如何追加？

---
Source: d:\mycode\awesome-copilot\prompts\update-implementation-plan.prompt.md
Generated: 2025-10-17T00:00:00Z
