## What
- 为任意语言/框架创建高效多阶段 Dockerfile，兼顾体积、安全与性能。

## When to use
- 构建/发布容器化应用，希望最小镜像、快速缓存、最小权限运行与健康检查。

## Why it matters
- 多阶段拆分与层优化可显著缩小体积与攻击面，提升交付与运行稳定性。

## How (关键流程)
- 阶段：builder(依赖/编译/测试) → runtime(仅运行所需)
- 基镜像：固定版本、slim/alpine、可选 distroless
- 层优化：.dockerignore、缓存顺序、合并 RUN、COPY --chown
- 安全：非 root 用户、删除构建工具、最小权限
- 性能：ARG 配置、HEALTHCHECK、按变更频率排序

## Example questions (≥10)
1. 为 Node.js 18 应用生成多阶段 Dockerfile（pnpm），并添加运行阶段非 root 用户。
2. 为 Python 3.11 FastAPI 生成 Dockerfile，使用 uvicorn 与 slim 基镜像并启用 HEALTHCHECK。
3. 给出 Java 17 Spring Boot 层拆分方案（依赖层/源码层）与构建缓存策略。
4. 如何在 Go 项目中使用多阶段启用 CGO=0 并复制仅二进制到 distroless？
5. 演示 .dockerignore 常见规则与对镜像体积的影响。
6. 使用 COPY --chown 设置权限避免运行期写入失败的示例。
7. 生成支持构建参数（ENV/ARG）的 Dockerfile，并说明如何在 CI 中覆盖。
8. 展示将秘密仅用于构建阶段且不泄漏到最终镜像的方法。
9. 添加多平台构建（buildx）与缓存导入导出配置示例。
10. 如何为前端静态站点（Vite）做 builder → nginx runtime 两阶段构建？

## Key points
- CN: 多阶段、可重复构建、镜像最小化、非 root、安全检查
- EN: Multi-stage, reproducible, minimal image, non-root, health/security checks

## Mind map (简要)
- 阶段 → 基镜像 → 层优化 → 安全 → 性能/健康 → CI/参数

---
Source file: d:\mycode\awesome-copilot\prompts\multi-stage-dockerfile.prompt.md
Generated: 2025-10-17T00:00:00Z
