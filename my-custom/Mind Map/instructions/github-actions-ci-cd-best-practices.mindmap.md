## What/When/Why/How
- What: GitHub Actions CI/CD 设计与安全/性能最佳实践（结构/作业/步骤/权限/缓存/矩阵/部署）
- When: 新建/审查工作流、引入安全基线、优化时长与稳定性
- Why: 降低风险与成本、提升可维护性与可观测性
- How: 清晰触发/并发/权限、作业依赖与 outputs、严谨 actions 版本、SAST/SCA/OIDC、缓存/矩阵并行、环境与回滚

## Key Points
- 结构: name/on/concurrency/permissions；复用 workflow_call
- 作业: runs-on/needs/outputs/if 条件；并行与分阶段
- 步骤: uses 版本固定（tag/commit SHA）；name/with/env 明确
- 安全: secrets/环境密钥；OIDC 云鉴权；最小权限 GITHUB_TOKEN
- 依赖安全: dependency-review/CodeQL/Sonar；secret scanning
- 性能: actions/cache；精心设计 key/restore-keys；fetch-depth:1
- 矩阵: strategy.matrix include/exclude/fail-fast
- 产物: upload/download-artifact；retention-days
- 部署: staging→prod；审批/回滚/健康检查；蓝绿/金丝雀/旗标
- 观察: 日志/指标/告警/追踪；失败重试与超时

## Compact Map
结构/权限→作业/依赖→步骤/版本→安全→性能/缓存→矩阵→产物→测试→部署/回滚→观察

## Example Questions (10+)
1) 为 Node monorepo 生成构建+测试+缓存工作流
2) 设计最小权限 permissions 与需要写入的作业覆盖
3) 使用 OIDC 对接 AWS/Azure 的配置样例
4) 引入 CodeQL 与 dependency-review 并在 PR 阻断
5) 设计 matrix 在多 OS/Node 版本并行测试
6) 构建产物上传/下载并传递到部署作业
7) 使用 concurrency 限制 main 分支并发发布
8) 配置环境审批与生产回滚 runbook 步骤
9) 大仓 checkout 优化（fetch-depth/LFS/Submodule 选择）
10) 添加缓存 key 策略与命中率优化

Source: d:\mycode\awesome-copilot\instructions\github-actions-ci-cd-best-practices.instructions.md | Generated: 2025-10-17T00:00:00Z
