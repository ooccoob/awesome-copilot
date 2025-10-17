## What/When/Why/How
- What: Power BI DevOps/ALM（PBIP、管道、REST/Fabric、版本/回滚）
- When: 团队协作、分环境发布、合规审计、自动化运维
- Why: 降低人为失误、可追溯、可回滚、提升交付效率
- How: PBIP 入库 → 构建校验 → 多环境参数化部署 → 质量门禁与回滚

## Key Points
- 版本化：PBIP 结构，Git Flow，标签/发布说明
- 部署：部署管道/REST/FabricPS-PBIP；参数化环境（连接/工作区）
- 安全：服务主体/Key Vault；RBAC；敏感度标签；最小权限
- 测试：数据质量/性能回归/安全基线自动化
- 监控：部署健康检查、Teams 通知、告警闭环
- 回滚：预备备份、失败自动回滚、恢复后验证脚本

## Compact Map
- Repo: Model/Report/tables/relationships/measures
- Pipeline: Build→Test→Prod，多阶段门禁
- Script: PowerShell/CLI 调用导入/绑定/刷新
- Config: env.json 管理 workspace/datasource/refresh

## Example Questions
1) PBIP 是否完整进 Git 且通过结构校验？
2) 环境连接/工作区是否参数化而非硬编码？
3) CI 是否包含质量门禁（模型/报告必备文件、测试）？
4) Fabric/REST 调用是否带有重试与错误处理？
5) 机密是否存放于 Key Vault 并用 SPN 最小权限？
6) 部署完成是否执行健康检查与通知？
7) 是否有一键回滚脚本及演练记录？
8) 性能回归基线与超阈处理是否自动化？
9) 变更是否有标签/发布说明与审计链路？
10) 跨环境数据源绑定是否自动替换并校验？
11) 失败是否仅回滚目标项且保留应急备份？

Source: d:\mycode\awesome-copilot\instructions\power-bi-devops-alm-best-practices.instructions.md | Generated: 2025-10-17
