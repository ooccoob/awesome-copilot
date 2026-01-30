## What / When / Why / How

- What: Azure SaaS 架构师模式（多租户/B2B&B2C 差异化设计）
- When: 需要围绕 SaaS 商业模型设计多租户架构与运营体系
- Why: 以 WAF+SaaS 指南优先满足 SaaS 业务诉求（隔离/规模/成本/合规）
- How: 先确认 B2B/B2C 模式→文档查证→确定租户与隔离模型→部署/运营方案

## Key Points

- 先查 SaaS 文档（WAF SaaS、SaaS 多租户指南、部署戳/Noisy Neighbor）
- B2B：更强隔离/定制/合规；B2C：高密度共享/极致成本/隐私
- 模式选择：共享/池化/独享/部署戳（Scale Unit）
- 身份：B2B 联邦/企业 SSO；B2C 社交登录与隐私
- 计费/监控：租户级指标、成本分摊、限流与配额

## Compact Map

- 业务模型
  - B2B vs B2C 关键差异
- 租户/隔离
  - 数据/计算/网络与密钥隔离
- 扩展性
  - 部署戳、地域与数据驻留
- 成本
  - 共享策略与成本分摊
- 运维
  - 生命周期/自助/计费监控

## Example Questions (10+)

- 明确是 B2B、B2C 还是混合？对应的优先级是什么？
- 选用何种租户隔离模型？哪些数据必须强隔离？
- 是否需要部署戳来作为规模单元与隔离域？
- 租户鉴权/授权与品牌白标的支持范围？
- 计费与用量度量的需求与技术落点？
- 噪声邻居如何监控与缓解（限流/配额/隔离）？
- 合规与数据驻留的区域与策略限制？
- 租户生命周期（开通/扩容/迁移/停用）如何自动化？
- 监控告警如何做到租户粒度？
- 多区域灾备与 RTO/RPO 目标是什么？
- 成本与性能的权衡如何对不同租户分层？

---
Source: d:\mycode\awesome-copilot\chatmodes\azure-saas-architect.chatmode.md
Generated: {{timestamp}}
