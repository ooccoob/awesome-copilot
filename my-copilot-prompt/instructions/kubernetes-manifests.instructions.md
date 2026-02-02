---
applyTo: 'k8s/**/*.yaml,k8s/**/*.yml,manifests/**/*.yaml,manifests/**/*.yml,deploy/**/*.yaml,deploy/**/*.yml,charts/**/templates/**/*.yaml,charts/**/templates/**/*.yml'
description: 'Best practices for Kubernetes YAML manifests including labeling conventions, security contexts, pod security, resource management, probes, and validation commands'
---

# Kubernetes 清单说明

## 您的使命

创建生产就绪的 Kubernetes 清单，通过一致的标签、适当的资源管理和全面的运行状况检查，优先考虑安全性、可靠性和卓越运营。

## 标签约定

**必需的标签**（推荐 Kubernetes）：
- `app.kubernetes.io/name`：应用程序名称
- `app.kubernetes.io/instance`：实例标识符
- `app.kubernetes.io/version`：版本
- `app.kubernetes.io/component`：组件角色
- `app.kubernetes.io/part-of`：应用程序组
- `app.kubernetes.io/managed-by`：管理工具

**附加标签**：
- `environment`：环境名称
- `team`：所属团队
- `cost-center`：用于计费

**有用的注释**：
- 文件和所有权
- 监控：`prometheus.io/scrape`、`prometheus.io/port`、`prometheus.io/path`
- 更改跟踪：git 提交、部署日期

## 安全上下文默认值

**Pod 级别**：
- __代码0__
- `runAsUser` 和 `runAsGroup`：特定 ID
- `fsGroup`：文件系统组
- __代码0__

**容器级**：
- __代码0__
- `readOnlyRootFilesystem: true` （带有用于可写目录的 tmpfs 挂载）
- `capabilities.drop: [ALL]`（仅添加需要的内容）

## Pod 安全标准

使用 Pod 安全准入：
- **受限**（建议用于生产）：强制安全强化
- **基线**：最低安全要求
- 在命名空间级别应用

## 资源请求和限制

**始终定义**：
- 请求：保证最低限度（安排）
- 限制：允许的最大值（防止耗尽）

**QoS 等级**：
- **保证**：请求==限制（最适合关键应用程序）
- **突发**：请求<限制（灵活的资源使用）
- **BestEffort**：未定义资源（避免在生产中）

## 健康探针

**活性**：重新启动不健康的容器
**准备就绪**：控制流量路由
**启动**：保护启动缓慢的应用程序

为每个配置适当的延迟、周期、超时和阈值。

## 推出策略

**部署策略**：
- `RollingUpdate` 与 `maxSurge` 和 `maxUnavailable`
- 设置 `maxUnavailable: 0` 以实现零停机

**高可用性**：
- 至少 2-3 个副本
- Pod 中断预算 (PDB)
- 反关联性规则（跨节点/区域传播）
- 用于可变负载的水平 Pod 自动缩放器 (HPA)

## 验证命令

**部署前**：
- __代码0__
- __代码0__
- `kubeconform -strict manifest.yaml`（架构验证）
- `helm template ./chart | kubeconform -strict`（用于头盔）

**政策验证**：
- OPA 竞赛、Kyverno 或 Datree

## 推出和回滚

**部署**：
- __代码0__
- __代码0__

**回滚**：
- __代码0__
- __代码0__
- __代码0__

**重新启动**：
- __代码0__

## 舱单清单

- [ ] 标签：应用标准标签
- [ ] 注释：文档和监控
- [ ] 安全性：runAsNonRoot、readOnlyRootFilesystem、删除功能
- [ ] 资源：定义的请求和限制
- [ ] 探针：活跃度、就绪度、启动配置
- [ ] 图片：特定标签（从不：最新）
- [ ] 副本：至少 2-3 个用于生产
- [ ] 策略：滚动更新并适当激增/不可用
- [ ] PDB：为生产定义
- [ ] 反亲和性：配置为HA
- [ ] 优雅关闭：terminationGracePeriodSeconds 设置
- [ ] 验证：试运行和 kubeconform 通过
- [ ] Secrets：在 Secrets 资源中，而不是 ConfigMaps
- [ ] NetworkPolicy：最低权限访问（如果适用）

## 最佳实践总结

1. 使用标准标签和注释
2. 始终以非 root 身份运行并删除功能
3. 定义资源请求和限制
4. 实现所有三种探针类型
5. 将图像标签固定到特定版本
6. 配置HA反亲和性
7. 设置 Pod 中断预算
8. 使用滚动更新实现零不可用性
9. 申请前验证清单
10. 尽可能启用只读根文件系统
