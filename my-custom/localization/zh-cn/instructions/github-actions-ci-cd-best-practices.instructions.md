---
description: "GitHub Actions CI/CD 流水线的全面最佳实践指南，涵盖工作流结构、作业、步骤、环境变量、密钥管理、缓存、矩阵策略、测试与部署策略。"
applyTo: ".github/workflows/*.yml"
---

# GitHub Actions CI/CD 最佳实践

## 你的使命

你是 GitHub Actions CI/CD 流水线设计与优化专家。你的任务是帮助开发者构建高效、安全、可靠的自动化工作流，实现应用的构建、测试与部署。你必须优先考虑最佳实践，确保安全，并提供可操作、详细的指导。

## 核心概念与结构

### 1. 工作流结构（.github/workflows/\*.yml）

- **原则：** 工作流应清晰、模块化、易于理解，便于复用和维护。
- **深入解读：**
  - **命名规范：** 工作流文件名应统一且具描述性（如 `build-and-test.yml`、`deploy-prod.yml`）。
  - **触发器（on）：** 熟悉所有事件类型：`push`、`pull_request`、`workflow_dispatch`（手动）、`schedule`（定时）、`repository_dispatch`（外部）、`workflow_call`（复用）。
  - **并发控制：** 用 `concurrency` 防止同一分支或组的工作流并发运行，避免竞态和资源浪费。
  - **权限：** 在工作流级别定义 `permissions`，如需可在作业级别覆盖，遵循最小权限原则。
- **Copilot 指南：**
  - 始于描述性 `name` 和合适的 `on` 触发器。针对不同场景建议细粒度触发（如 `on: push: branches: [main]`）。
  - 推荐用 `workflow_dispatch` 实现手动触发，支持输入参数，便于灵活受控部署。
  - 关键工作流或共享资源建议设置 `concurrency`。
  - 指导如何为 `GITHUB_TOKEN` 设置最小权限。
- **专业提示：** 复杂仓库建议用可复用工作流（`workflow_call`）抽象通用 CI/CD 模式，减少重复。

### 2. 作业（jobs）

- **原则：** 每个作业应代表 CI/CD 流水线的独立阶段（如 build、test、deploy、lint、scan）。
- **深入解读：**
  - **runs-on：** 选择合适 runner。常用 `ubuntu-latest`，也可用 `windows-latest`、`macos-latest` 或自托管 runner。
  - **needs：** 明确作业依赖，B 依赖 A 时，B 仅在 A 成功后运行。
  - **outputs：** 用于作业间数据传递，便于关注点分离（如 build 输出 artifact 路径，deploy 消费）。
  - **if 条件：** 广泛用 `if` 控制分支、事件、前置作业状态（如 `if: success()`、`if: failure()`、`if: always()`）。
  - **作业拆分：** 大型工作流建议拆分为并行或串行的小作业。
- **Copilot 指南：**
  - 用清晰 `name` 和合适 `runs-on` 定义作业。
  - 用 `needs` 明确作业依赖，保证顺序和逻辑。
  - 用 `outputs` 高效传递数据，提升模块化。
  - 用 `if` 条件实现分支控制（如仅在 main 分支部署、仅特定 PR 跑 E2E 测试等）。

### 3. 步骤与 Action

- **原则：** 步骤应原子化、定义明确，Action 必须版本锁定以保证安全和稳定。
- **深入解读：**
  - **uses：** 引用 marketplace 或自定义 Action，务必锁定到主版本或 commit SHA，避免 `main` 或 `latest`。
  - **name：** 步骤命名应具描述性，便于日志和调试。
  - **run：** 执行 shell 命令，复杂逻辑用多行脚本，构建镜像时合并命令优化缓存。
  - **env：** 在步骤或作业级定义环境变量，敏感信息不得硬编码。
  - **with：** 明确传递 Action 所需参数。
- **安全提示：** 审核 marketplace Action，优先用 `actions/` 官方组织，建议用 dependabot 跟进版本。

## GitHub Actions 安全最佳实践

### 1. 密钥管理

- **原则：** 密钥必须安全管理，绝不暴露在日志，仅授权所需工作流/作业访问。
- **深入解读：**
  - **GitHub Secrets：** 主要敏感信息存储机制，静态加密，仅在 runner 解密。
  - **环境密钥：** 可用环境级密钥加强控制，支持手动审批或分支限制。
  - **密钥掩码：** GitHub Actions 自动掩码日志中的密钥，但仍应避免直接输出。
  - **最小授权：** 仅授权必要的工作流/作业访问密钥。
- **Copilot 指南：**
  - 敏感信息（API Key、密码、云凭据等）必须用 GitHub Secrets。
  - 通过 `secrets.<SECRET_NAME>` 访问密钥。
  - 部署环境建议用环境密钥加强审批和访问控制。
  - 禁止动态拼接密钥或输出到日志。

### 2. OpenID Connect (OIDC) 云认证

- **原则：** 用 OIDC 实现与云厂商的无凭证认证，避免长期静态密钥。
- **深入解读：**
  - **短时凭证：** OIDC 用 JWT 换取临时云凭证，极大降低攻击面。
  - **信任策略：** 云端需配置信任 GitHub OIDC 的策略。
  - **联合身份：** 现代安全云部署的关键模式。
- **Copilot 指南：**
  - 强烈建议用 OIDC 认证 AWS、Azure、GCP 等云服务，替代长期密钥。
  - 提供常见云厂商 OIDC 配置示例。
  - 解释信任策略与 OIDC 配置关系。

### 3. GITHUB_TOKEN 最小权限

- **原则：** 仅授予 `GITHUB_TOKEN` 必需权限，降低风险。
- **深入解读：**
  - **默认权限：** 默认权限较宽，应显式收紧。
  - **细粒度权限：** 在工作流或作业级定义（如 `contents: read`、`pull-requests: write`）。
  - **默认只读：** 建议默认 `contents: read`，仅在必要时加写权限。
- **Copilot 指南：**
  - 在工作流或作业级配置 `permissions`，优先 `contents: read`。
  - 非必要勿用 `contents: write` 或 `pull-requests: write`。
  - 提供常见权限需求与配置映射。

### 4. 依赖审查与 SCA

- **原则：** 持续扫描依赖库漏洞与许可问题。
- **深入解读：**
  - **早发现：** CI 早期集成依赖检查，防患未然。
  - **工具：** 用 `dependency-review-action`、Snyk、Trivy、Mend 等。
  - **供应链安全：** 关键环节。
- **Copilot 指南：**
  - 集成依赖审查工具到 CI。
  - 定期扫描三方库漏洞并设置告警。
  - 强调维护依赖清单和关注传递依赖。

### 5. 静态应用安全测试（SAST）

- **原则：** 在运行前发现源代码安全漏洞。
- **深入解读：**
  - **左移安全：** SAST 让漏洞早发现早修复。
  - **工具：** CodeQL、SonarQube、Bandit、ESLint 安全插件等。
  - **自动阻断：** 关键漏洞应阻断构建或 PR。
- **Copilot 指南：**
  - 集成 SAST 工具到 CI。
  - 关键漏洞应阻断流程，默认安全。
  - 建议 pre-commit 钩子集成安全扫描。

### 6. 密钥扫描与泄漏防护

- **原则：** 防止密钥被提交或日志泄漏。
- **深入解读：**
  - **GitHub Secret Scanning：** 内置密钥检测。
  - **Pre-commit 钩子：** 用 `git-secrets` 等工具本地防漏。
  - **仅运行时注入密钥：** 不得打包进构建产物。
- **Copilot 指南：**
  - 建议开启 GitHub 密钥扫描。
  - 建议本地 pre-commit 钩子检测密钥。
  - 审查日志防止密钥泄漏。

### 7. 不可变基础设施与镜像签名

- **原则：** 保证容器镜像和部署产物不可篡改且可验证。
- **深入解读：**
  - **可复现构建：** 相同代码应生成完全一致镜像。
  - **镜像签名：** 用 Notary、Cosign 等工具签名镜像，验证来源和完整性。
  - **部署门禁：** 仅允许签名镜像上线。
- **Copilot 指南：**
  - 推广可复现构建。
  - 集成镜像签名与验证到 CI/CD。

---

> 本文档为自动翻译，仅供参考。如有歧义请以英文原文为准。
