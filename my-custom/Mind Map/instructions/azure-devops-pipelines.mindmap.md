## What / When / Why / How
- What: Azure DevOps Pipeline YAML 规范与复用策略（构建/测试/部署/安全/观测）。
- When: 新建/拆分/优化 CI/CD 流水线与模板时。
- Why: 稳定可重用、可观测、最小权限与高性能。
- How: 阶段/作业/步骤分层；变量/参数/模板化；缓存与并行；Key Vault 机密；审批与环境策略。

## Key points
- 结构：stages→jobs→steps；依赖显式；大管道拆分与模板复用。
- 构建：固定代理镜像；缓存 npm/NuGet/Maven；制品命名与保留策略；质量门（lint/test/security）。
- 测试：发布测试与覆盖率；按影响测试；失败快速反馈。
- 安全：Key Vault+变量组；最小权限服务连接；依赖与 SAST 扫描；生产审批门。
- 部署：环境晋级；deployment jobs；蓝绿/金丝雀；回滚与健康检查；IaC（ARM/Bicep/Terraform）。
- 性能：并行矩阵；缓存；浅克隆；高效 Docker 多阶段；资源触发。
- 观测：日志/通知；AI/Monitor；失败与性能分析；文档化与排障手册。
- 触发：分支/路径/PR/计划/资源；过滤避免无谓触发。

## Compact map
- 复用: templates/extends
- 变量: groups/secrets
- 安全: least-privilege
- 部署: env/策略/回滚
- 性能: 并行/缓存
- 观测: logs/alerts

## Example questions (10+)
- 何时使用 extends 模板与何时仅用 steps/job 模板？
- 如何基于路径过滤仅构建受影响项目？
- 多环境机密如何统一在 Key Vault 管理并按环境注入？
- PR 与主干触发的质量门与审批门应如何区分？
- 矩阵并行构建与缓存策略如何协同？
- Docker 镜像层缓存与多阶段构建如何提速？
- 部署健康检查失败如何自动回滚？
- 如何在管道中发布测试/覆盖率并做质量门？
- 模板版本化与跨仓库复用的实践？
- 如何用环境与审批来保护生产？

—
Source: d:\mycode\awesome-copilot\instructions\azure-devops-pipelines.instructions.md | Generated: {{timestamp}}
