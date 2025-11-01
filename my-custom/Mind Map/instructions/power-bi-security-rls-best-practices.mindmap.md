## What/When/Why/How
- What: Power BI 安全与行级安全（RLS）实践：静态/动态 RLS、嵌入式、数据库侧策略、治理与审计
- When: 设计/落地权限隔离、内嵌应用与合规审计时
- Why: 最小权限与防数据越权，满足合规、稳定上线
- How: DAX 过滤 + CUSTOMDATA/USERNAME + 嵌入 EffectiveIdentity + DB RLS + 治理监控

## Key Points
- RLS 基础：基于用户/角色的 DAX 过滤；默认拒绝（FALSE）
- 动态 RLS：CUSTOMDATA()/USERNAME() + 映射表/层级/时间窗
- 嵌入式：EffectiveIdentity 指定 roles/customData，按数据集多租隔离
- DB 侧安全：SQL/Fabric 安全策略（Security Policy + 函数谓词）
- 多租户：按租户/区域过滤；跨数据集/报表的身份传递
- 治理监控：审计度量（可访问行数占比）、违例告警、角色验证
- 反模式：宽松默认 TRUE；过度复杂 DAX；角色漂移

## Compact Map
- DAX: USERNAME/CUSTOMDATA → role filter
- Embed: EffectiveIdentity → roles/customData
- DB-RLS: predicate fn + security policy
- Gov: audit measures + alerts + group mgmt

## Example Questions
1) RLS 过滤对未匹配用户是否默认拒绝？
2) 动态 RLS 的 CUSTOMDATA/USERNAME 来源在哪一层设定？
3) 角色/地域/时间窗等复合条件是否拆分为维表？
4) 嵌入式是否正确设置 EffectiveIdentity（roles/customData）？
5) 是否评估 DB 侧 RLS 与模型侧 RLS 的边界与一致性？
6) 跨报表/数据集的身份是否一致传递并可审计？
7) 审计度量（可访问行数/占比）是否纳入治理看板？
8) 角色变更是否自动化同步至工作区/网关权限？
9) 反模式（默认 TRUE/复杂嵌套）是否已被清理？
10) 多租户是否验证“租户间绝对隔离”与缓存影响？
11) 压测大用户量下的角色评估与刷新是否稳定？

Source: d:\mycode\awesome-copilot\instructions\power-bi-security-rls-best-practices.instructions.md | Generated: 2025-10-17
