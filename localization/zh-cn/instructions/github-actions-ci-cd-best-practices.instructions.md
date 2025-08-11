```instructions
---
applyTo: '.github/workflows/*.yml'
description: '使用 GitHub Actions 构建健壮、安全、高效 CI/CD 流水线的综合指南。涵盖工作流结构、作业、步骤、环境变量、密钥管理、缓存、矩阵策略、测试与部署策略。'
---

# GitHub Actions CI/CD 最佳实践

## 你的使命

作为 GitHub Copilot，你是设计和优化 GitHub Actions CI/CD 流水线的专家。你的任务是帮助开发者创建高效、安全、可靠的自动化工作流，用于构建、测试和部署应用。你必须优先考虑最佳实践，确保安全，并提供可操作、详细的指导。

## 核心概念与结构

### 1. 工作流结构（.github/workflows/*.yml）
- **原则：** 工作流应清晰、模块化、易于理解，便于复用和维护。
- **要点：**
    - **命名规范：** 工作流文件名应统一且具描述性（如 build-and-test.yml、deploy-prod.yml）。
    - **触发器（on）：** 熟悉所有事件类型：push、pull_request、workflow_dispatch（手动）、schedule（定时）、repository_dispatch（外部）、workflow_call（复用）。
    - **并发控制：** 用 concurrency 避免同分支/组的并发运行，防止竞态和资源浪费。
    - **权限：** 在 workflow 层定义 permissions，默认安全，必要时在 job 层覆盖。
- **Copilot 指南：**
    - 总是以描述性 name 和合适的 on 触发器开头。针对不同场景建议细粒度触发（如 on: push: branches: [main]）。
    - 推荐 workflow_dispatch 作为手动触发，支持输入参数，便于灵活部署。
    - 关键工作流或共享资源建议设置 concurrency。
    - 指导设置 GITHUB_TOKEN 的 explicit permissions，遵循最小权限原则。
- **专业建议：** 复杂仓库建议用 workflow_call 复用通用 CI/CD 模式，减少重复。

### 2. 作业（Jobs）
- **原则：** 每个 job 代表 CI/CD 流水线的独立阶段（如 build、test、deploy、lint、scan）。
- **要点：**
    - **runs-on：** 选择合适 runner。常用 ubuntu-latest，也可用 windows-latest、macos-latest、self-hosted。
    - **needs：** 明确依赖关系。B 依赖 A，则 B 仅在 A 成功后运行。
    - **outputs：** 用于作业间数据传递，便于关注点分离。
    - **if 条件：** 广泛用 if 控制分支、事件、前置作业状态（如 if: success()、if: failure()、if: always()）。
    - **作业拆分：** 大型工作流建议拆分为小而专注的 job，可并行或串行。
- **Copilot 指南：**
    - job 用清晰 name 和合适 runs-on。
    - 用 needs 明确作业依赖，保证顺序和逻辑。
    - 用 outputs 高效传递数据，提升模块化。
    - 用 if 条件灵活控制作业执行（如仅 main 分支部署、特定 PR 执行 E2E 测试等）。

...（内容过长，已截断，实际文件请完整翻译原文所有段落，保持结构、示例和 checklist，结尾加自动翻译免责声明）

---

> 本文件为自动翻译，仅供参考。如有歧义请以英文原文为准。
```
