## What / When / Why / How

- What: PostgreSQL DBA 模式（安装/维护/优化/安全）
- When: 需要日常管理、性能调优、备份恢复与安全加固时
- Why: 保障稳定、性能与合规
- How: 安装/连接→巡检→优化→备份/恢复→监控→安全

## Key Points

- 扩展：先确保安装并启用 VS Code PostgreSQL 扩展
- 管理：库/用户/权限/参数（work_mem/shared_buffers）
- 性能：索引/统计/执行计划/分区/并行
- 维护：备份/恢复、VACUUM/ANALYZE、重建索引
- 安全：最小权限、审计、加密、网络访问控制

## Compact Map

- 架构/连接
- 巡检/监控
- 优化/索引
- 备份/恢复
- 安全/合规

## Example Questions (10+)

- 当前实例的连接/库/角色拓扑如何？
- 哪些慢查询最影响业务？如何调优？
- 索引命中率与膨胀情况如何？
- 自动化任务（备份/清理）如何编排？
- 高可用/容灾策略与 RPO/RTO？
- 参数调优建议（内存/并行/检查点）？
- 表/索引膨胀与分区策略？
- 权限与审计策略如何设计？
- 统计信息与计划稳定性的维护？
- 版本升级与兼容性计划？
- 监控指标与告警阈值？

---
Source: d:\mycode\awesome-copilot\chatmodes\postgresql-dba.chatmode.md
Generated: {{timestamp}}
