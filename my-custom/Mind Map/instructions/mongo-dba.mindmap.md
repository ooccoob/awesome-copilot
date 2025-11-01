## MongoDB DBA 指南（速览）

### 这是什么/何时使用/为什么/如何做
- What: Copilot 在 mongodb-dba 聊天模式下应遵循的运维/管理行为准则。
- When: 连接集群、建库建集合、备份恢复、性能与安全审计、版本升级兼容等 DBA 任务。
- Why: 提供面向 MongoDB 7.x+ 的可靠、可审计、可扩展实践，并统一回答风格。
- How: 优先 VS Code 扩展/Compass 工具；链接官方文档；提示弃用项（ensureIndex→createIndexes、MMAPv1→WiredTiger）与安全基线（SCRAM/TLS/审计）。

### 关键要点
- 工具优先: VS Code MongoDB 扩展与 Compass；Shell 仅在需要时给出命令。
- 管理范围: 副本集/分片、角色与认证、索引与性能分析、备份（mongodump/restore）。
- 升级注意: 版本兼容矩阵、参数变化、弃用/移除功能替代方案。
- 安全: RBAC、加密传输、最小权限、审计开启与日志留存。
- 参考: 始终附上官方文档链接用于自查与排障。

### 紧凑脑图
- 连接/可视化→建模与索引→性能分析→备份恢复→安全基线→升级与兼容→官方文档

### 开发者示例问题（≥10）
- 如何用 VS Code 扩展连接一个带 TLS 的副本集？
- 大表创建复合索引的评估与回退策略？
- 如何排查慢查询并给出 createIndexes 建议？
- mongodump 在线备份对性能的影响如何评估？
- 不同版本之间 featureCompatibilityVersion 的升级顺序？
- 分片键选择的基准与热点写入规避策略？
- 如何设计只读审计角色并最小化权限？
- WiredTiger 压缩配置对存储与性能的权衡？
- 如何发现并替换已弃用的 ensureIndex 调用？
- 生产环境故障转移（failover）演练的步骤与检查表？

—
Source: d:\mycode\awesome-copilot\instructions\mongo-dba.instructions.md | Generated: 2025-10-17
