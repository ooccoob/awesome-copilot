## DevOps 核心原则（CALMS + DORA）

- What: DevOps 文化/自动化/精益/度量/共享五大支柱与四大 DORA 指标实践。
- When: 设计交付流程、落地 CI/CD、度量改进、建立协作文化与知识共享时。
- Why: 提升交付速度与稳定性，降低风险，驱动持续改进与业务价值达成。
- How: 以自动化贯穿开发/测试/部署/安全；用度量驱动优化；打造分享与学习文化。

### CALMS 提要
- Culture: 无责后检、共享责任、反馈闭环、跨职能协作。
- Automation: CI/CD、IaC、配置管理、自动化测试、监控告警与安全扫描。
- Lean: 去浪费、缩批量、VSM、内建质量、JIT 交付。
- Measurement: 指标/日志/追踪、仪表盘、有效告警、实验与容量规划。
- Sharing: 模板/平台/文档、沟通渠道、结对/工作坊、ADR/Runbook。

### DORA 指标
- 部署频率(DF): 越高越好（精英每日多次）。
- 变更交付前置时间(LTFC): 越短越好（精英 <1h）。
- 变更失败率(CFR): 越低越好（0-15%）。
- 平均恢复时间(MTTR): 越短越好（<1h）。

### Compact Map
CALMS→(Culture/Automation/Lean/Measurement/Sharing) + DORA→(DF/LTFC/CFR/MTTR)

### 示例问题
1) 如何将安全扫描（SAST/DAST/SCA）并入 CI/CD？
2) 提高部署频率的最小增量策略？
3) 如何用 VSM 识别瓶颈并度量改进成效？
4) 降低 CFR 的回滚/验证/观测设计？
5) 将 MTTR 压到 <1h 的告警与 Runbook 体系？
6) 蓝绿/金丝雀的落地要点与自动化方案？
7) 构建/测试加速的缓存与并行化实践？
8) 统一日志/指标/追踪的字段与采样策略？
9) 如何以特性开关解耦部署与发布？
10) 推动无责后检的团队机制与模板？

Source: d:\mycode\awesome-copilot\instructions\devops-core-principles.instructions.md | Generated: 2025-10-17T00:00:00Z
