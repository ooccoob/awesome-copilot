## What

- 基于计划与变更跟踪的任务实现规范：按序执行、每步完成后更新 plan 与 changes

## When

- 执行 .copilot-tracking/plans 与 details 中的任务计划时

## Why

- 保证实现的完整性、可追溯性与一致性，形成可发布的变更记录

## How

- 准备
  - 必读：完整 plan、对应 changes、涉及文件与工程结构
- 执行
  - 严格按计划顺序；每任务前先读 details 全量内容；实现可工作的代码，遵循工程规范
- 标记与记录
  - 完成后将计划项 [ ]→[x]
  - 必填：在 changes 的 Added/Modified/Removed 追加条目（相对路径+一句话）
  - 若偏离计划，必须在相应部分注明原因
  - 阶段全部完成后标记阶段 [x]
- 质量
  - 错误处理/校验；命名/结构一致；必要文档与注释
- 持续验证
  - 每步验证需求 → 修正问题 → 更新 plan 与 changes → 下一个未完成任务
- 完成与发布
  - 全部 [x]、文件齐全、成功标准满足、无遗留错误
  - 在 changes 添加 Release Summary：文件清单/依赖/部署说明

## Key Points

- “读全量→实现→验证→打勾→记录变化”循环
- 任何偏离都要记录并解释

## Compact Map

- 准备: 读 plan/changes/details
- 执行: 严格顺序/工作代码
- 记录: 勾选 + changes 三类
- 质量: 规范/错误/文档
- 完成: Release Summary

## Example Questions

1) 本任务的 details 文件有哪些依赖前置？
2) 哪些文件需要最小必要修改？
3) 完成后应在 changes 的哪个分区记录？
4) 若实现偏离计划，如何在记录中说明？
5) 如何验证满足 success criteria？
6) 出现阻塞时的替代路径/降级是什么？
7) 如何保持命名与目录结构一致？
8) 何时需要补充单元/集成测试？
9) 完成阶段后如何正确标记 [x]？
10) Release Summary 需包含哪些维度？
11) 如何处理外部参考与本仓库规范冲突？

Source: d:\mycode\awesome-copilot\instructions\task-implementation.instructions.md | Generated: 2025-10-17
