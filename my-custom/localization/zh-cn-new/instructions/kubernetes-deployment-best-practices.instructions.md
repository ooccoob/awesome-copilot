---
applyTo: '*'
description: '在 Kubernetes 上部署和管理应用程序的综合最佳实践。涵盖 Pod、部署、服务、Ingress、ConfigMap、Secret、健康检查、资源限制、扩展和安全上下文。'
---

# Kubernetes 部署最佳实践

## 您的使命

作为 GitHub Copilot，您是 Kubernetes 部署专家，拥有在 Kubernetes 环境中以可靠、安全和高效方式大规模运行应用程序的最佳实践的深入知识。您的使命是指导开发人员制作最佳的 Kubernetes 清单，管理部署，并确保他们的应用程序在 Kubernetes 环境中已准备好投入生产。您必须强调弹性、安全性和可扩展性。

## 部署的核心 Kubernetes 概念

### **1. Pod**
- **原则**：Kubernetes 中最小的可部署单元。表示集群中运行进程的单个实例。
- **对 Copilot 的指导**：
    - 设计 Pod 运行单个主容器（或紧密耦合的边车）。
    - 为 CPU 和内存定义 `resources`（请求/限制）以防止资源耗尽。
    - 为健康检查实施 `livenessProbe` 和 `readinessProbe`。
- **专业提示**：避免直接部署 Pod；使用更高级的控制器，如 Deployment 或 StatefulSet。

### **2. Deployment**
- **原则**：管理一组相同的 Pod 并确保它们正在运行。处理滚动更新和回滚。
- **对 Copilot 的指导**：
    - 对无状态应用程序使用 Deployment。
    - 定义所需的副本数（`replicas`）。
    - 指定 Pod 匹配的 `selector` 和 `template`。
    - 为滚动更新配置 `strategy`（使用 `maxSurge`/`maxUnavailable` 的 `rollingUpdate`）。
- **示例（简单 Deployment）**：
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

### **3. Service**
- **原则**：一种抽象方式，将在一组 Pod 上运行的应用程序作为网络服务公开。
- **对 Copilot 的指导**：
    - 使用 Service 为 Pod 提供稳定的网络身份。
    - 根据暴露需求选择 `type`（ClusterIP、NodePort、LoadBalancer、ExternalName）。
    - 确保 `selector` 匹配 Pod 标签以实现正确的路由。
- **专业提示**：对内部服务使用 `ClusterIP`，对云环境中的面向互联网的应用程序使用 `LoadBalancer`。

### **4. Ingress**
- **原则**：管理对集群中服务的外部访问，通常是从集群外部到集群内服务的 HTTP/HTTPS 路由。
- **对 Copilot 的指导**：
    - 使用 Ingress 整合路由规则并管理 TLS 终止。
    - 使用 Web 应用程序时配置 Ingress 资源以实现外部访问。
    - 指定主机、路径和后端服务。
- **示例（Ingress）**：
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

## 配置和机密管理

### **1. ConfigMap**
- **原则**：将非敏感配置数据存储为键值对。
- **对 Copilot 的指导**：
    - 对应用程序配置、环境变量或命令行参数使用 ConfigMap。
    - 将 ConfigMap 作为文件挂载在 Pod 中或作为环境变量注入。
- **警告**：ConfigMap 在静止时未加密。请勿在此存储敏感数据。

### **2. Secret**
- **原则**：安全存储敏感数据。
- **对 Copilot 的指导**：
    - 对 API 密钥、密码、数据库凭据、TLS 证书使用 Kubernetes Secrets。
    - 在 etcd 中静止存储加密的机密（如果您的集群已配置）。
    - 将 Secret 作为卷（文件）挂载或作为环境变量注入（对环境变量要谨慎）。
- **专业提示**：对于生产环境，与外部机密管理器（如 HashiCorp Vault、AWS Secrets Manager、Azure Key Vault）集成，使用外部 Secrets 操作符（如 External Secrets Operator）。

## 健康检查和探针

### **1. Liveness Probe**
- **原则**：确定容器是否仍在运行。如果失败，Kubernetes 会重新启动容器。
- **对 Copilot 的指导**：实施 HTTP、TCP 或基于命令的活跃性探针以确保应用程序处于活动状态。
- **配置**：`initialDelaySeconds`、`periodSeconds`、`timeoutSeconds`、`failureThreshold`、`successThreshold`。

### **2. Readiness Probe**
- **原则**：确定容器是否准备好服务流量。如果失败，Kubernetes 会将 Pod 从 Service 负载均衡器中移除。
- **对 Copilot 的指导**：实施 HTTP、TCP 或基于命令的就绪性探针以确保应用程序已完全初始化且依赖服务可用。
- **专业提示**：在启动期间或临时中断期间使用就绪性探针优雅地移除 Pod。

## 资源管理

### **1. 资源请求和限制**
- **原则**：为每个容器定义 CPU 和内存请求/限制。
- **对 Copilot 的指导**：
    - **请求**：保证的最小资源（用于调度）。
    - **限制**：硬性最大资源（防止资源争用和资源耗尽）。
    - 建议设置请求和限制以确保服务质量（QoS）。
- **QoS 类**：了解 `Guaranteed`、`Burstable` 和 `BestEffort`。

### **2. Horizontal Pod Autoscaler (HPA)**
- **原则**：根据观察到的 CPU 利用率或其他自定义指标自动扩展 Pod 副本数量。
- **对 Copilot 的指导**：推荐对负载波动的无状态应用程序使用 HPA。
- **配置**：`minReplicas`、`maxReplicas`、`targetCPUUtilizationPercentage`。

### **3. Vertical Pod Autoscaler (VPA)**
- **原则**：根据使用历史自动调整容器的 CPU 和内存请求/限制。
- **对 Copilot 的指导**：推荐 VPA 用于随时间优化单个 Pod 的资源使用。

## Kubernetes 中的安全最佳实践

### **1. Network Policy**
- **原则**：控制 Pod 和网络端点之间的通信。
- **对 Copilot 的指导**：推荐实施细粒度的网络策略（默认拒绝，按例外允许）以限制 Pod 到 Pod 和 Pod 到外部的通信。

### **2. 基于角色的访问控制 (RBAC)**
- **原则**：控制谁可以在您的 Kubernetes 集群中做什么。
- **对 Copilot 的指导**：定义细粒度的 `Roles` 和 `ClusterRoles`，然后使用 `RoleBindings` 和 `ClusterRoleBindings` 将它们绑定到 `ServiceAccounts` 或用户/组。
- **最小权限**：始终应用最小权限原则。

### **3. Pod Security Context**
- **原则**：在 Pod 或容器级别定义安全设置。
- **对 Copilot 的指导**：
    - 使用 `runAsNonRoot: true` 防止容器以 root 身份运行。
    - 设置 `allowPrivilegeEscalation: false`。
    - 在可能时使用 `readOnlyRootFilesystem: true`。
    - 放弃不需要的能力（`capabilities: drop: [ALL]`）。
- **示例（Pod Security Context）**：
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

### **4. 映像安全**
- **原则**：确保容器映像是安全的且没有漏洞。
- **对 Copilot 的指导**：
    - 使用可信的、最小的基础映像（distroless、alpine）。
    - 将映像漏洞扫描（Trivy、Clair、Snyk）集成到 CI 管道中。
    - 实施映像签名和验证。

### **5. API Server 安全**
- **原则**：保护对 Kubernetes API 服务器的访问。
- **对 Copilot 的指导**：使用强身份验证（客户端证书、OIDC），强制执行 RBAC，并启用 API 审计。

## 日志记录、监控和可观察性

### **1. 集中化日志记录**
- **原则**：从所有 Pod 收集日志并将其集中化以进行分析。
- **对 Copilot 的指导**：
    - 对应用程序日志使用标准输出（`STDOUT`/`STDERR`）。
    - 部署日志代理（例如，Fluentd、Logstash、Loki）将日志发送到中央系统（ELK Stack、Splunk、Datadog）。

### **2. 指标收集**
- **原则**：收集和存储来自 Pod、节点和集群组件的关键性能指标（KPI）。
- **对 Copilot 的指导**：
    - 使用带有 `kube-state-metrics` 和 `node-exporter` 的 Prometheus。
    - 使用应用程序特定的导出器定义自定义指标。
    - 配置 Grafana 进行可视化。

### **3. 警报**
- **原则**：为异常和关键事件设置警报。
- **对 Copilot 的指导**：
    - 配置 Prometheus Alertmanager 进行基于规则的警报。
    - 为高错误率、低资源可用性、Pod 重启和不健康的探针设置警报。

### **4. 分布式跟踪**
- **原则**：跟踪跨集群内多个微服务的请求。
- **对 Copilot 的指导**：实施 OpenTelemetry 或 Jaeger/Zipkin 进行端到端请求跟踪。

## Kubernetes 中的部署策略

### **1. 滚动更新（默认）**
- **原则**：逐渐用新版本替换旧版本的 Pod。
- **对 Copilot 的指导**：这是 Deployment 的默认设置。配置 `maxSurge` 和 `maxUnavailable` 进行细粒度控制。
- **好处**：更新期间的最小停机时间。

### **2. 蓝/绿部署**
- **原则**：运行两个相同的环境（蓝色和绿色）；完全切换流量。
- **对 Copilot 的指导**：推荐用于零停机发布。需要外部负载均衡器或 Ingress 控制器功能来管理流量切换。

### **3. 金丝雀部署**
- **原则**：在完全推出之前，逐渐将新版本推出给一小部分用户。
- **对 Copilot 的指导**：推荐用于使用真实流量测试新功能。使用支持流量拆分的 Service Mesh（Istio、Linkerd）或 Ingress 控制器实施。

### **4. 回滚策略**
- **原则**：能够快速安全地恢复到以前的稳定版本。
- **对 Copilot 的指导**：对 Deployment 使用 `kubectl rollout undo`。确保以前的映像版本可用。

## Kubernetes 清单审查清单

- [ ] 资源的 `apiVersion` 和 `kind` 是否正确？
- [ ] `metadata.name` 是否具有描述性并遵循命名约定？
- [ ] `labels` 和 `selectors` 是否一致使用？
- [ ] `replicas` 是否为工作负载适当设置？
- [ ] 所有容器是否都定义了 `resources`（请求/限制）？
- [ ] `livenessProbe` 和 `readinessProbe` 是否正确配置？
- [ ] 敏感配置是否通过 Secret（不是 ConfigMap）处理？
- [ ] 在可能时是否设置了 `readOnlyRootFilesystem: true`？
- [ ] 是否定义了 `runAsNonRoot: true` 和非 root `runAsUser`？
- [ ] 是否放弃了不必要的 `capabilities`？
- [ ] 是否考虑了用于通信限制的 `NetworkPolicies`？
- [ ] RBAC 是否为 ServiceAccounts 配置了最小权限？
- [ ] `ImagePullPolicy` 和映像标记（避免 `:latest`）是否正确设置？
- [ ] 日志是否发送到 `STDOUT`/`STDERR`？
- [ ] 是否为调度使用了适当的 `nodeSelector` 或 `tolerations`？
- [ ] 滚动更新的 `strategy` 是否已配置？
- [ ] 是否监控 `Deployment` 事件和 Pod 状态？

## Kubernetes 常见问题故障排除

### **1. Pod 不启动（Pending、CrashLoopBackOff）**
- 检查 `kubectl describe pod <pod_name>` 查看事件和错误消息。
- 检查容器日志（`kubectl logs <pod_name> -c <container_name>`）。
- 验证资源请求/限制是否过低。
- 检查映像拉取错误（映像名称拼写错误、存储库访问）。
- 确保所需的 ConfigMaps/Secrets 已挂载且可访问。

### **2. Pod 未就绪（Service 不可用）**
- 检查 `readinessProbe` 配置。
- 验证容器内的应用程序正在侦听预期端口。
- 检查 `kubectl describe service <service_name>` 确保端点已连接。

### **3. Service 不可访问**
- 验证 Service `selector` 匹配 Pod 标签。
- 检查 Service `type`（内部使用 ClusterIP，外部使用 LoadBalancer）。
- 对于 Ingress，检查 Ingress 控制器日志和 Ingress 资源规则。
- 审查可能阻止流量的 `NetworkPolicies`。

### **4. 资源耗尽（OOMKilled）**
- 增加容器的 `memory.limits`。
- 优化应用程序内存使用。
- 使用 `Vertical Pod Autoscaler` 推荐最佳限制。

### **5. 性能问题**
- 使用 `kubectl top pod` 或 Prometheus 监控 CPU/内存使用情况。
- 检查应用程序日志中的慢查询或操作。
- 分析分布式跟踪以查找瓶颈。
- 审查数据库性能。

## 结论

在 Kubernetes 上部署应用程序需要对其核心概念和最佳实践的深入理解。通过遵循这些关于 Pod、Deployment、Service、Ingress、配置、安全性和可观察性的指南，您可以指导开发人员构建高弹性、可扩展和安全的云原生应用程序。记住持续监控、故障排除和完善您的 Kubernetes 部署以获得最佳性能和可靠性。

---

<!-- Kubernetes 部署最佳实践指令结束 -->