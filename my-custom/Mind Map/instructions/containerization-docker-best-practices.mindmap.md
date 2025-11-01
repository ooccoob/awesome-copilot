## What/When/Why/How

- What: Dockerfile/镜像/运行/编排最佳实践：多阶段构建、最小镜像、层优化、.dockerignore、非 root、健康检查、安全扫描、资源/日志/网络/存储/编排。
- When: 构建/优化/审计容器镜像与运行时；CI/CD 集成时。
- Why: 更小更快更安全、可复现与可回滚、降低攻击面与成本。
- How: Multi-stage 构建、选择官方最小基镜、合并 RUN 清理缓存、精确 COPY、定义 USER/EXPOSE/CMD/ENTRYPOINT、ENV 外化配置、HEALTHCHECK、Trivy/Hadolint、资源限额与集中日志监控。

## Key Points

- 构建: Multi-stage(依赖/构建/测试/生产)；依赖先 COPY 以缓存；仅复制运行必需产物。
- 基镜: alpine/slim/distroless；固定版本避免 latest；多架构支持。
- 层: 合并 RUN；清理 apt 缓存；变更频繁的 COPY 置后。
- 忽略: .dockerignore 完整维护(依赖/产物/IDE/文档/测试)。
- 安全: 非 root USER；最小能力/只读 rootfs；签名/验证；避免在层中包含机密。
- 健康: HEALTHCHECK(liveness/readiness)。
- 运行: 资源 requests/limits；结构化日志；持久化用卷；隔离网络与策略。
- 编排: 滚动更新/自愈/服务发现；K8s 首选复杂场景。

## Compact Map

- Build → multi-stage/层优化
- Base → minimal/versioned
- Copy → 精选/顺序
- Security → USER/cap/seccomp
- Health → HEALTHCHECK
- Runtime → 资源/日志/卷/网络
- CI → hadolint/Trivy

## Example Questions (10+)

1) Node/Java 项目如何拆分多阶段构建？
2) distroless 使用时调试策略？
3) COPY 顺序如何最大化缓存命中？
4) .dockerignore 的必备条目有哪些？
5) 非 root 用户权限不足如何排错？
6) HEALTHCHECK 失败的重试与阈值怎么设？
7) Trivy 扫描阻断发布的门槛定义？
8) 只读根文件系统下如何写入必要数据？
9) 多平台镜像构建的实践？
10) Kubernetes 资源 requests/limits 的初始估算？

---
Source: d:\mycode\awesome-copilot\instructions\containerization-docker-best-practices.instructions.md | Generated: 2025-10-17
