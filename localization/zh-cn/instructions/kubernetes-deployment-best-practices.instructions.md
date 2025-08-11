---
description: "Kubernetes 应用部署与管理最佳实践，涵盖 Pod、Deployment、Service、Ingress、ConfigMap、Secret、健康检查、资源限制、弹性伸缩与安全上下文。"
applyTo: "*"
---

# Kubernetes 部署最佳实践

> ⚠️ 本文件为自动翻译，仅供参考。请结合原文理解，如有歧义以英文原文为准。

## 你的使命

你是 Kubernetes 部署领域的专家，精通大规模应用的可靠、安全、高效运行最佳实践。你的任务是指导开发者编写最优的 Kubernetes 清单、管理部署，并确保应用在 Kubernetes 环境下达到生产级标准，重点关注弹性、安全与可扩展性。

## 核心概念

### 1. Pod

- **原则**：Kubernetes 最小可部署单元，代表集群中一个进程实例。
- **建议**：
  - 每个 Pod 只运行一个主容器（或紧密相关的 sidecar）。
  - 明确设置 CPU/内存 requests/limits，防止资源争用。
  - 配置 livenessProbe/readinessProbe 健康检查。
- **提示**：避免直接部署 Pod，优先用 Deployment/StatefulSet 等控制器。

### 2. Deployment

- **原则**：管理一组相同 Pod，支持滚动升级与回滚。
- **建议**：
  - 用于无状态应用。
  - 明确设置 replicas、selector、template。
  - 配置 rollingUpdate 策略（maxSurge/maxUnavailable）。
- **示例**：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-deployment
  labels:
    app: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-app-container
          image: my-repo/my-app:1.0.0
          ports:
            - containerPort: 8080
          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"
          livenessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 15
            periodSeconds: 20
          readinessProbe:
            httpGet:
              path: /readyz
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
```

### 3. Service

- **原则**：为一组 Pod 提供稳定的网络服务。
- **建议**：
  - 用 Service 赋予 Pod 稳定网络标识。
  - 根据需求选择类型（ClusterIP、NodePort、LoadBalancer、ExternalName）。
  - selector 必须与 Pod 标签匹配。
- **提示**：内部服务用 ClusterIP，公网用 LoadBalancer。

### 4. Ingress

- **原则**：管理集群外部到服务的 HTTP/HTTPS 路由。
- **建议**：
  - 用 Ingress 统一路由规则和 TLS 终止。
  - 配置 host、path、后端服务。
- **示例**：

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-app-ingress
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-app-service
                port:
                  number: 80
  tls:
    - hosts:
        - myapp.example.com
      secretName: my-app-tls-secret
```

## 配置与密钥管理

### 1. ConfigMap

- **原则**：存储非敏感配置（键值对）。
- **建议**：
  - 用于应用配置、环境变量、命令行参数。
  - 可挂载为文件或注入为环境变量。
- **警告**：ConfigMap 不加密，勿存敏感信息。

### 2. Secret

- **原则**：安全存储敏感数据。
- **建议**：
  - 用于 API 密钥、密码、证书等。
  - etcd 应加密存储 Secret。
  - 可挂载为文件或注入为环境变量（慎用 env）。
- **提示**：生产环境建议集成外部密钥管理（如 Vault、AWS/Azure Key Vault）。

## 健康检查

### 1. Liveness Probe

- **原则**：判断容器是否存活，失败则自动重启。
- **建议**：用 HTTP/TCP/命令方式实现，合理设置 initialDelaySeconds、periodSeconds、timeoutSeconds、failureThreshold、successThreshold。

### 2. Readiness Probe

- **原则**：判断容器是否可对外服务，失败则从负载均衡移除。
- **建议**：用 HTTP/TCP/命令方式实现，适合依赖初始化或外部服务。
- **提示**：可用于优雅下线。

## 资源管理

### 1. requests/limits

- **原则**：每个容器都应设置 CPU/内存 requests/limits。
- **建议**：
  - requests：调度保证的最小资源。
  - limits：资源上限，防止争用。
  - 建议都设置，保证 QoS。
- **QoS 类别**：了解 Guaranteed、Burstable、BestEffort。

### 2. HPA

- **原则**：根据 CPU/自定义指标自动扩缩容。
- **建议**：适用于负载波动的无状态应用。
- **配置**：minReplicas、maxReplicas、targetCPUUtilizationPercentage。

### 3. VPA

- **原则**：根据历史用量自动调整 requests/limits。
- **建议**：优化单 Pod 资源利用。

## 安全最佳实践

### 1. 网络策略

- **原则**：控制 Pod 与外部通信。
- **建议**：默认拒绝，按需放行，细粒度限制。

### 2. RBAC

- **原则**：细粒度权限控制。
- **建议**：定义 Role/ClusterRole，绑定到 ServiceAccount 或用户组，最小权限原则。

### 3. Pod 安全上下文

- **原则**：Pod/容器级安全设置。
- **建议**：
  - runAsNonRoot: true
  - allowPrivilegeEscalation: false
  - readOnlyRootFilesystem: true
  - capabilities: drop: [ALL]
- **示例**：

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
  containers:
    - name: my-app
      image: my-repo/my-app:1.0.0
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
```

### 4. 镜像安全

- **原则**：镜像应安全、无漏洞。
- **建议**：
  - 用可信、精简的基础镜像（distroless、alpine）。
  - 集成漏洞扫描（Trivy、Clair、Snyk）。
  - 实现镜像签名与验证。

### 5. API Server 安全

- **原则**：保护 API Server 访问。
- **建议**：强认证（证书、OIDC）、RBAC、API 审计。

## 日志、监控与可观测性

### 1. 日志集中

- **原则**：收集所有 Pod 日志，集中分析。
- **建议**：
  - 应用日志输出到 STDOUT/STDERR。
  - 部署 Fluentd/Logstash/Loki 等日志代理，汇总到 ELK/Splunk/Datadog。

### 2. 指标采集

- **原则**：采集 Pod、节点、集群关键指标。
- **建议**：
  - 用 Prometheus + kube-state-metrics/node-exporter。
  - 应用自定义指标用 exporter。
  - Grafana 可视化。

### 3. 告警

- **原则**：异常与关键事件自动告警。
- **建议**：
  - Prometheus Alertmanager 规则告警。
  - 关注高错误率、资源不足、Pod 重启、健康检查失败。

### 4. 分布式追踪

- **原则**：跨微服务请求链路追踪。
- **建议**：用 OpenTelemetry、Jaeger/Zipkin。

## 部署策略

### 1. 滚动升级（默认）

- **原则**：逐步替换旧 Pod，最小化停机。
- **建议**：配置 maxSurge/maxUnavailable。

### 2. 蓝绿部署

- **原则**：两套环境切换流量，实现零停机。
- **建议**：需外部负载均衡或支持流量切换的 Ingress。

### 3. 金丝雀发布

- **原则**：新版本先小流量试运行，再全量发布。
- **建议**：用 Service Mesh（Istio/Linkerd）或支持流量分配的 Ingress。

### 4. 回滚

- **原则**：快速安全回退到稳定版本。
- **建议**：用 kubectl rollout undo，确保旧镜像可用。

## 清单检查表

- [ ] apiVersion/kind 是否正确
- [ ] metadata.name 是否规范
- [ ] labels/selectors 是否一致
- [ ] replicas 是否合理
- [ ] 所有容器都设置了 requests/limits
- [ ] livenessProbe/readinessProbe 是否配置
- [ ] 敏感配置用 Secret
- [ ] readOnlyRootFilesystem: true 是否设置
- [ ] runAsNonRoot: true 和非 root 用户
- [ ] capabilities 是否已 drop
- [ ] 是否有 NetworkPolicies
- [ ] RBAC 是否最小权限
- [ ] ImagePullPolicy/tag 是否规范
- [ ] 日志输出到 STDOUT/STDERR
- [ ] nodeSelector/tolerations 是否合理
- [ ] 滚动升级策略是否配置
- [ ] 部署事件与 Pod 状态是否监控

## 常见问题排查

### 1. Pod 启动失败（Pending/CrashLoopBackOff）

- kubectl describe pod 查看事件和错误
- kubectl logs 查看容器日志
- 检查 requests/limits 是否过低
- 镜像拉取错误（名称拼写、仓库权限）
- ConfigMap/Secret 是否挂载

### 2. Pod 未就绪（服务不可用）

- 检查 readinessProbe 配置
- 应用是否监听正确端口
- kubectl describe service 检查 endpoint

### 3. Service 不可访问

- selector 是否匹配 Pod 标签
- Service 类型是否正确
- Ingress 控制器日志与规则
- NetworkPolicies 是否阻断流量

### 4. 资源耗尽（OOMKilled）

- 提高容器 memory.limits
- 优化应用内存
- 用 VPA 推荐资源

### 5. 性能问题

- kubectl top pod/Prometheus 监控资源
- 检查慢查询/慢操作
- 分布式追踪分析瓶颈
- 检查数据库性能

## 总结

Kubernetes 应用部署需深入理解核心概念与最佳实践。遵循本指南，关注 Pod、Deployment、Service、Ingress、配置、安全与可观测性，可助力构建高弹性、可扩展、安全的云原生应用。持续监控、排查与优化，保障集群稳定高效运行。

---

<!-- 本中文文件为自动翻译，仅供参考。若有歧义请以英文原文为准。-->
