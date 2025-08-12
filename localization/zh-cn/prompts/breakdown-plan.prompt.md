---
mode: "agent"
description: "生成包含 Epic > Feature > Story/Enabler > Test 分解、依赖与优先级、自动化跟踪的完整项目计划与问题清单。"
---

# GitHub Issue 规划与项目自动化提示词（中文版）

## 目标（Goal）

扮演资深项目经理与 DevOps 专家（精通敏捷与 GitHub 项目管理）。读取完整的特性产物（PRD、UX 设计、技术拆解、测试计划），生成覆盖自动化建 issue、依赖关系、优先级与看板追踪的完整 GitHub 项目计划。

## GitHub 项目管理最佳实践

### 敏捷工作项分级（Hierarchy）

- Epic：跨多个功能的大型业务能力（里程碑层级）
- Feature：Epic 下可交付的用户功能
- Story：面向用户、可独立交付的需求
- Enabler：支撑 Story 的技术/架构性工作
- Test：用于验证 Story/Enabler 的质量工作
- Task：Story/Enabler 的实现级拆解

### 项目管理原则（Principles）

- INVEST：独立性、可协商、可创造价值、可估算、小而聚焦、可测试
- DoR：开始前具备清晰的验收标准
- DoD：质量关卡与完成判定
- 依赖管理：清晰的阻塞关系与关键路径
- 价值优先：基于业务价值与投入的矩阵排序

## 输入要求（Input Requirements）

使用本提示词前，请准备完整的测试/规划材料：

### 核心特性文档（Core Feature Documents）

1. Feature PRD：`/docs/ways-of-work/plan/{epic-name}/{feature-name}.md`
2. Technical Breakdown：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/technical-breakdown.md`
3. Implementation Plan：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`

### 相关规划提示词（Related Planning Prompts）

- 测试规划：使用 `plan-test` 进行测试策略、QA 计划与测试 issue 创建
- 架构规划：使用 `plan-epic-arch` 进行系统架构与技术设计
- 需求规划：使用 `plan-feature-prd` 输出详细需求与规格

## 输出格式（Output Format）

生成两份主要交付物：

1. 项目计划：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md`
2. Issue 创建清单：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/issues-checklist.md`

### 项目计划结构（Project Plan Structure）

#### 1. 项目概述（Overview）

- 功能摘要：简述与业务价值
- 成功标准：可衡量的结果与 KPI
- 关键里程碑：主要交付物拆解（不含时间）
- 风险评估：潜在阻塞与缓解策略

#### 2. 工作项分级（Work Item Hierarchy）

```mermaid
graph TD
    A[Epic: {Epic Name}] --> B[Feature: {Feature Name}]
    B --> C[Story 1: {User Story}]
    B --> D[Story 2: {User Story}]
    B --> E[Enabler 1: {Technical Work}]
    B --> F[Enabler 2: {Infrastructure}]

    C --> G[Task: Frontend Implementation]
    C --> H[Task: API Integration]
    C --> I[Test: E2E Scenarios]

    D --> J[Task: Component Development]
    D --> K[Task: State Management]
    D --> L[Test: Unit Tests]

    E --> M[Task: Database Schema]
    E --> N[Task: Migration Scripts]

    F --> O[Task: CI/CD Pipeline]
    F --> P[Task: Monitoring Setup]
```

#### 3. GitHub Issue 拆解（Issues Breakdown）

以下为各层级 Issue 模板（保持与英文版一一对应，字段齐全，便于直接复制粘贴使用）。

##### Epic Issue 模板

```markdown
# Epic: {Epic Name}

## Epic Description

{Epic summary from PRD}

## Business Value

- **Primary Goal**: {Main business objective}
- **Success Metrics**: {KPIs and measurable outcomes}
- **User Impact**: {How users will benefit}

## Epic Acceptance Criteria

- [ ] {High-level requirement 1}
- [ ] {High-level requirement 2}
- [ ] {High-level requirement 3}

## Features in this Epic

- [ ] #{feature-issue-number} - {Feature Name}

## Definition of Done

- [ ] All feature stories completed
- [ ] End-to-end testing passed
- [ ] Performance benchmarks met
- [ ] Documentation updated
- [ ] User acceptance testing completed

## Labels

`epic`, `{priority-level}`, `{value-tier}`

## Milestone

{Release version/date}

## Estimate

{Epic-level t-shirt size: XS, S, M, L, XL, XXL}
```

##### Feature Issue 模板

```markdown
# Feature: {Feature Name}

## Feature Description

{Feature summary from PRD}

## User Stories in this Feature

- [ ] #{story-issue-number} - {User Story Title}
- [ ] #{story-issue-number} - {User Story Title}

## Technical Enablers

- [ ] #{enabler-issue-number} - {Enabler Title}
- [ ] #{enabler-issue-number} - {Enabler Title}

## Dependencies

**Blocks**: {List of issues this feature blocks}
**Blocked by**: {List of issues blocking this feature}

## Acceptance Criteria

- [ ] {Feature-level requirement 1}
- [ ] {Feature-level requirement 2}

## Definition of Done

- [ ] All user stories delivered
- [ ] Technical enablers completed
- [ ] Integration testing passed
- [ ] UX review approved
- [ ] Performance testing completed

## Labels

`feature`, `{priority-level}`, `{value-tier}`, `{component-name}`

## Epic

#{epic-issue-number}

## Estimate

{Story points or t-shirt size}
```

##### User Story Issue 模板

```markdown
# User Story: {Story Title}

## Story Statement

As a **{user type}**, I want **{goal}** so that **{benefit}**.

## Acceptance Criteria

- [ ] {Specific testable requirement 1}
- [ ] {Specific testable requirement 2}
- [ ] {Specific testable requirement 3}

## Technical Tasks

- [ ] #{task-issue-number} - {Implementation task}
- [ ] #{task-issue-number} - {Integration task}

## Testing Requirements

- [ ] #{test-issue-number} - {Test implementation}

## Dependencies

**Blocked by**: {Dependencies that must be completed first}

## Definition of Done

- [ ] Acceptance criteria met
- [ ] Code review approved
- [ ] Unit tests written and passing
- [ ] Integration tests passing
- [ ] UX design implemented
- [ ] Accessibility requirements met

## Labels

`user-story`, `{priority-level}`, `frontend/backend/fullstack`, `{component-name}`

## Feature

#{feature-issue-number}

## Estimate

{Story points: 1, 2, 3, 5, 8}
```

##### Technical Enabler Issue 模板

```markdown
# Technical Enabler: {Enabler Title}

## Enabler Description

{Technical work required to support user stories}

## Technical Requirements

- [ ] {Technical requirement 1}
- [ ] {Technical requirement 2}

## Implementation Tasks

- [ ] #{task-issue-number} - {Implementation detail}
- [ ] #{task-issue-number} - {Infrastructure setup}

## User Stories Enabled

This enabler supports:

- #{story-issue-number} - {Story title}
- #{story-issue-number} - {Story title}

## Acceptance Criteria

- [ ] {Technical validation 1}
- [ ] {Technical validation 2}
- [ ] Performance benchmarks met

## Definition of Done

- [ ] Implementation completed
- [ ] Unit tests written
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] Code review approved

## Labels

`enabler`, `{priority-level}`, `infrastructure/api/database`, `{component-name}`

## Feature

#{feature-issue-number}

## Estimate

{Story points or effort estimate}
```

#### 4. 优先级-价值矩阵（Priority & Value Matrix）

| Priority | Value  | Criteria                        | Labels                            |
| -------- | ------ | ------------------------------- | --------------------------------- |
| P0       | High   | Critical path, blocking release | `priority-critical`, `value-high` |
| P1       | High   | Core functionality, user-facing | `priority-high`, `value-high`     |
| P1       | Medium | Core functionality, internal    | `priority-high`, `value-medium`   |
| P2       | Medium | Important but not blocking      | `priority-medium`, `value-medium` |
| P3       | Low    | Nice to have, technical debt    | `priority-low`, `value-low`       |

#### 5. 估算指引（Estimation Guidelines）

- Story Points（Fibonacci）：1/2/3/5/8/13+
- T-Shirt（Epic/Feature）：XS/S/M/L/XL

#### 6. 依赖管理（Dependency Management）

包含阻塞、相关、前置、并行等类型。可参考下方 mermaid 示例并按需扩展。

#### 7. Sprint 规划（Sprint Planning）

##### Sprint 产能规划（Capacity Planning）

- 团队速度（Velocity）：{每个 Sprint 的平均 Story Points}
- Sprint 时长：{建议 2 周}
- 缓冲比例：20% 预留给突发与缺陷修复
- 专注系数：70–80% 时间用于已计划工作

##### Sprint 目标定义（Goal Definition）

```markdown
## Sprint {N} Goal

**Primary Objective**: {本次 Sprint 的主要可交付物}

**Stories in Sprint**:

- #{issue} - {Story title} ({points} pts)
- #{issue} - {Story title} ({points} pts)

**Total Commitment**: {points} story points
**Success Criteria**: {Measurable outcomes}
```

#### 8. 项目看板配置（Project Board）

- 列（Backlog/Sprint Ready/In Progress/In Review/Testing/Done）
- 自定义字段（Priority/Value/Component/Estimate/Sprint/Assignee/Epic）

#### 9. 自动化与 Actions（Automation）

##### 自动化创建 Feature Issues（GitHub Actions）

```yaml
name: Create Feature Issues

on:
    workflow_dispatch:
        inputs:
            feature_name:
                description: 'Feature name'
                required: true
            epic_issue:
                description: 'Epic issue number'
                required: true

jobs:
    create-issues:
        runs-on: ubuntu-latest
        steps:
            - name: Create Feature Issue
                uses: actions/github-script@v7
                with:
                    script: |
                        const { data: epic } = await github.rest.issues.get({
                            owner: context.repo.owner,
                            repo: context.repo.repo,
                            issue_number: ${{ github.event.inputs.epic_issue }}
                        });

                        const featureIssue = await github.rest.issues.create({
                            owner: context.repo.owner,
                            repo: context.repo.repo,
                            title: `Feature: ${{ github.event.inputs.feature_name }}`,
                            body: `# Feature: ${{ github.event.inputs.feature_name }}\n\n...`,
                            labels: ['feature', 'priority-medium'],
                            milestone: epic.data.milestone?.number
                        });
```

##### 自动化状态更新（基于 PR 事件）

```yaml
name: Update Issue Status

on:
    pull_request:
        types: [opened, closed]

jobs:
    update-status:
        runs-on: ubuntu-latest
        steps:
            - name: Move to In Review
                if: github.event.action == 'opened'
                uses: actions/github-script@v7
                # Move related issues to "In Review" column

            - name: Move to Done
                if: github.event.action == 'closed' && github.event.pull_request.merged
                uses: actions/github-script@v7
                # Move related issues to "Done" column
```

### Issue 创建清单（Issue Creation Checklist）

#### 预创建准备（Pre-Creation Preparation）

- [ ] 特性产物齐全：PRD、UX 设计、技术拆解、测试计划
- [ ] Epic 已存在：创建父 Epic，包含标签与里程碑
- [ ] 项目看板已配置：列、自定义字段与自动化规则
- [ ] 团队产能评估：完成 Sprint 规划与资源分配

#### Epic 层级（Epic Level Issues）

- [ ] 创建 Epic，撰写完整描述与验收标准
- [ ] 创建/绑定里程碑并设置目标发布日期
- [ ] 应用标签：`epic`、优先级、价值、团队等
- [ ] 将 Epic 加入项目看板的合适列

#### Feature 层级（Feature Level Issues）

- [ ] 创建 Feature 并关联父 Epic
- [ ] 识别并记录 Feature 依赖
- [ ] 完成 Feature 估算（T-Shirt 或 Story Points）
- [ ] 明确 Feature 验收标准并可度量

#### Story/Enabler/Test 层级（在 `/docs/ways-of-work/plan/{epic-name}/{feature-name}/issues-checklist.md` 中归档）

- [ ] 创建用户故事并符合 INVEST
- [ ] 识别技术推进项（Enablers）并排序
- [ ] 使用 Fibonacci 估点
- [ ] 建立故事与推进项之间的依赖映射
- [ ] 明确并细化可测试的验收标准

## 成功度量（Success Metrics）

### 项目管理 KPI（Project Management KPIs）

- Sprint 预测性：每个 Sprint >80% 的承诺工作按期完成
- Cycle Time：从 “In Progress” 到 “Done” 的平均时长 <5 个工作日
- Lead Time：从 “Backlog” 到 “Done” 的平均时长 <2 周
- 缺陷逃逸率：<5% 的故事在发布后需要修复
- 团队速度：跨多个 Sprint 的 Story Points 交付稳定

### 流程效率指标（Process Efficiency Metrics）

- Issue 创建时效：<1 小时完成完整的特性拆解
- 依赖解决时效：<24 小时清理阻塞依赖
- 状态更新准确率：>95% 的自动状态迁移正确
- 文档完整度：100% 的 Issue 均按模板要求填写
- 跨团队协作：外部依赖在 2 个工作日内闭环

### 交付指标（Project Delivery Metrics）

- DoD 遵循率：100% 完成项满足完成定义
- 验收标准覆盖：100% 验收标准得到验证
- Sprint 目标达成：>90% 的 Sprint 目标成功交付
- 干系人满意度：>90% 对已交付功能认可
- 计划准确性：估算与实际交付时间偏差 <10%

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](../../issues) 进行反馈。
