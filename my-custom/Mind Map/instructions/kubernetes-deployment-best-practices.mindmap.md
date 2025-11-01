## What/When/Why/How
- What: 在 Kubernetes 上部署与运维应用的生产级最佳实践（Pod/Deployment/Service/Ingress/配置/密钥/探针/资源/伸缩/安全）。
- When: 设计/评审/调试 K8s 清单与集群运行特性时。
- Why: 提升可靠性、安全性、可观测性与可扩展性，减少中断与性能抖动。
- How: 以控制器为中心建模、声明资源边界与健康检查、最小权限与网络策略、完善监控告警。

## Key Points
- Pod：单主容器或紧耦合 sidecar；设置 requests/limits；liveness/readiness。
- Deployment：无状态工作负载首选；滚动升级策略 maxSurge/maxUnavailable。
- Service：稳定虚拟IP；选择合适 type（ClusterIP/NodePort/LoadBalancer）。
- Ingress：统一路由与 TLS 终止；规则基于 host/path。
- 配置：ConfigMap 非敏感；Secret 存放凭证（建议集成外部密管）。
- 健康检查：启动/存活/就绪探针参数合理化，避免误杀或过迟发现。
- 资源：定义 requests/limits 以获 QoS；评估 HPA/VPA 策略。
- 安全：NetworkPolicy、RBAC 最小权限、PodSecurityContext（非 root、RO 根 FS、降权）。
- 镜像：最小化基底、扫描漏洞、避免 :latest；签名与策略。
- 观测：STDOUT/STDERR 日志收集、Prometheus/Grafana 指标与告警、分布式追踪。

## Compact Map
K8s
- Workloads: Pod/Deployment
- Networking: Service/Ingress/Policy
- Config: CM/Secret
- Health: Probes
- Resources: QoS/HPA/VPA
- Security: RBAC/PSC
- Observability: Logs/Metrics/Tracing
- Strategy: Rolling/Blue-Green/Canary

## Checklist
- [ ] 资源与探针齐备
- [ ] 安全上下文最小权限
- [ ] 网络策略默认拒绝
- [ ] 镜像扫描与固定标签
- [ ] HPA/VPA 评估
- [ ] 监控/日志/告警接入
- [ ] 回滚路径清晰

## Example Questions (≥10)
- 如何为 Web 服务配置就绪与存活探针的合理参数？
- HPA 触发阈值与自定义指标如何选择？
- 何时用 Deployment、何时用 StatefulSet？
- Ingress TLS 终止的证书管理怎么做？
- 如何用 NetworkPolicy 实现默认拒绝与基于标签的放行？
- Secret 以 env 注入与以 Volume 挂载的取舍？
- 滚动升级失败如何快速回滚并排查原因？
- 如何避免 :latest 与确保可复现部署？
- 如何标准化日志并导入集中式系统？
- 多租户/多命名空间下 RBAC 最佳拆分方式？

Source: d:\mycode\awesome-copilot\instructions\kubernetes-deployment-best-practices.instructions.md | Generated: 2025-10-17
