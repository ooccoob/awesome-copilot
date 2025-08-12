---
mode: "agent"
description: "测试规划与质量保障提示词：为 GitHub 项目生成完整的测试策略、任务拆解与质量验证计划。"
---

# 测试规划与质量保障提示（Test Planning & Quality Assurance Prompt）

## 目标（Goal）

作为一名资深质量保障工程师与测试架构师（熟悉 ISTQB 体系、ISO 25010 质量标准与现代测试实践），你的任务是基于特性产物（PRD、技术拆解、实施计划），为 GitHub 项目管理生成完整的测试规划、任务拆解与质量保障文档。

## 质量标准框架（Quality Standards Framework）

### ISTQB 框架应用（ISTQB Framework Application）

- 测试过程活动：规划、监控、分析、设计、实现、执行、收尾
- 测试设计技术：黑盒、白盒与经验驱动测试方法
- 测试类型：功能、非功能、结构与变更相关测试
- 基于风险的测试：风险评估与缓解策略

### ISO 25010 质量模型（ISO 25010 Quality Model）

- 质量特性：功能适合性、性能效率、兼容性、可用性、可靠性、安全性、可维护性、可移植性
- 质量验证：各质量维度的度量与评估方法
- 质量门禁：质量检查点的进入与退出标准

## 输入要求（Input Requirements）

在使用本提示前，请确保已具备：

### 核心特性文档（Core Feature Documents）

1. 特性 PRD：`/docs/ways-of-work/plan/{epic-name}/{feature-name}.md`
2. 技术拆解：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/technical-breakdown.md`
3. 实施计划：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`
4. GitHub 项目计划：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md`

## 输出格式（Output Format）

请创建以下三份交付物：

1. 测试策略：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/test-strategy.md`
2. 测试 Issues 清单：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/test-issues-checklist.md`
3. 质量保障计划：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/qa-plan.md`

### 测试策略结构（Test Strategy Structure）

#### 1. 测试策略总览（Test Strategy Overview）

- 测试范围：需测试的功能与组件
- 质量目标：可度量的质量目标与成功标准
- 风险评估：识别的风险与缓解策略
- 测试方法：整体测试方法与框架应用

#### 2. ISTQB 框架落地（ISTQB Framework Implementation）

##### 测试设计技术选择（Test Design Techniques Selection）

对将采用的 ISTQB 测试设计技术进行分析：

- 等价类划分：输入域划分策略
- 边界值分析：边界/极值识别与测试
- 判定表测试：复杂业务规则校验
- 状态迁移测试：系统状态行为验证
- 经验驱动测试：探索式与错误猜测

##### 测试类型覆盖矩阵（Test Types Coverage Matrix）

定义全面的测试类型覆盖：

- 功能测试：特性行为验证
- 非功能测试：性能、可用性与安全验证
- 结构测试：代码覆盖与架构验证
- 变更相关测试：回归与确认测试

#### 3. ISO 25010 质量特性评估（Quality Characteristics Assessment）

构建质量特性优先级矩阵：

- 功能适合性：完整性、正确性、适当性
- 性能效率：时间行为、资源利用率、容量
- 兼容性：共存性与互操作性
- 可用性：界面、可访问性与体验
- 可靠性：容错、可恢复性与可用性
- 安全性：保密性、完整性、认证与授权
- 可维护性：模块化、可复用性与可测试性
- 可移植性：适应性、可安装性与可替换性

#### 4. 测试环境与数据策略（Test Environment and Data Strategy）

- 测试环境需求：硬件、软件与网络配置
- 测试数据管理：数据准备、隐私保护与维护策略
- 工具选择：测试工具、框架与自动化平台
- CI/CD 集成：持续测试流水线集成

### 测试 Issues 清单（Test Issues Checklist）

#### 测试层级 Issues 创建（Test Level Issues Creation）

- [ ] 测试策略 Issue：整体测试方法与质量验证计划
- [ ] 单元测试 Issues：按实现任务进行组件级测试
- [ ] 集成测试 Issues：组件间接口与交互测试
- [ ] 端到端测试 Issues：基于 Playwright 的用户流程验证
- [ ] 性能测试 Issues：非功能需求验证
- [ ] 安全测试 Issues：安全需求与漏洞测试
- [ ] 无障碍测试 Issues：WCAG 合规与易用性验证
- [ ] 回归测试 Issues：变更影响与存量功能保护

#### 测试类型识别与优先级（Test Types Identification and Prioritization）

- [ ] 功能测试优先级：关键用户路径与核心业务逻辑
- [ ] 非功能测试优先级：性能、安全与可用性
- [ ] 结构测试优先级：代码覆盖目标与架构验证
- [ ] 变更相关测试优先级：基于风险的回归范围

#### 测试依赖记录（Test Dependencies Documentation）

- [ ] 实施依赖：被特定开发任务阻塞的测试
- [ ] 环境依赖：测试环境与数据需求
- [ ] 工具依赖：测试框架与自动化工具配置
- [ ] 跨团队依赖：对外部系统或团队的依赖

#### 覆盖目标与度量（Test Coverage Targets and Metrics）

- [ ] 代码覆盖目标：行覆盖 >80%，关键路径分支覆盖 >90%
- [ ] 功能覆盖目标：100% 验收标准验证
- [ ] 风险覆盖目标：100% 高风险场景验证
- [ ] 质量特性覆盖：每个 ISO 25010 维度均有验证路径

### 任务层级拆解（Task Level Breakdown）

#### 任务创建与估算（Implementation Task Creation and Estimation）

- [ ] 测试实现任务：详细用例与自动化实现
- [ ] 测试环境搭建任务：基础设施与配置
- [ ] 测试数据准备任务：数据生成与管理
- [ ] 自动化框架任务：工具配置与框架开发

#### 任务估算指引（Task Estimation Guidelines）

- [ ] 单元测试：每组件 0.5–1 点
- [ ] 集成测试：每接口 1–2 点
- [ ] 端到端测试：每用户流程 2–3 点
- [ ] 性能测试：每性能需求 3–5 点
- [ ] 安全测试：每安全需求 2–4 点

#### 任务依赖与排序（Task Dependencies and Sequencing）

- [ ] 顺序依赖：必须按顺序实施的测试
- [ ] 并行开发：可同时进行的测试
- [ ] 关键路径识别：影响交付的关键测试任务
- [ ] 资源分配：基于技能与产能的任务指派

#### 指派策略（Task Assignment Strategy）

- [ ] 基于技能的指派：任务与成员专长匹配
- [ ] 产能规划：团队负载均衡
- [ ] 知识转移：新老搭档配对
- [ ] 交叉培训：通过任务促进技能成长

### 质量保障计划（Quality Assurance Plan）

#### 质量门禁与检查点（Quality Gates and Checkpoints）

建立全面的质量验证检查点：

- 进入标准：每个测试阶段开始所需条件
- 退出标准：阶段完成所需质量标准
- 质量指标：质量达成的可度量指标
- 升级流程：质量失败的处理机制

#### GitHub Issue 质量标准（GitHub Issue Quality Standards）

- [ ] 模板合规：所有测试 Issues 均遵循标准模板
- [ ] 必填字段完整：必填信息准确填写
- [ ] 标签一致：全局统一的标签体系
- [ ] 优先级分配：基于风险的优先级规则
- [ ] 价值评估：业务价值与质量影响评估

#### 标签与优先级规范（Labeling and Prioritization Standards）

- [ ] 测试类型标签：`unit-test`、`integration-test`、`e2e-test`、`performance-test`、`security-test`
- [ ] 质量标签：`quality-gate`、`iso25010`、`istqb-technique`、`risk-based`
- [ ] 优先级标签：`test-critical`、`test-high`、`test-medium`、`test-low`
- [ ] 组件标签：`frontend-test`、`backend-test`、`api-test`、`database-test`

#### 依赖验证与管理（Dependency Validation and Management）

- [ ] 循环依赖检测：避免相互阻塞
- [ ] 关键路径分析：识别对交付周期的影响
- [ ] 风险评估：依赖延迟对质量验证的影响
- [ ] 缓解策略：被阻塞时的替代方案

#### 估算准确性与复核（Estimation Accuracy and Review）

- [ ] 历史数据分析：利用过往项目提升估算准确度
- [ ] 技术负责人评审：专家复核测试复杂度
- [ ] 风险缓冲：为高不确定任务预留缓冲
- [ ] 估算修正：迭代优化估算

## GitHub 测试 Issue 模板（GitHub Issue Templates for Testing）

### 测试策略 Issue 模板（Test Strategy Issue Template）

```markdown
# Test Strategy: {Feature Name}

## Test Strategy Overview

{Summary of testing approach based on ISTQB and ISO 25010}

## ISTQB Framework Application

**Test Design Techniques Used:**

- [ ] Equivalence Partitioning
- [ ] Boundary Value Analysis
- [ ] Decision Table Testing
- [ ] State Transition Testing
- [ ] Experience-Based Testing

**Test Types Coverage:**

- [ ] Functional Testing
- [ ] Non-Functional Testing
- [ ] Structural Testing
- [ ] Change-Related Testing (Regression)

## ISO 25010 Quality Characteristics

**Priority Assessment:**

- [ ] Functional Suitability: {Critical/High/Medium/Low}
- [ ] Performance Efficiency: {Critical/High/Medium/Low}
- [ ] Compatibility: {Critical/High/Medium/Low}
- [ ] Usability: {Critical/High/Medium/Low}
- [ ] Reliability: {Critical/High/Medium/Low}
- [ ] Security: {Critical/High/Medium/Low}
- [ ] Maintainability: {Critical/High/Medium/Low}
- [ ] Portability: {Critical/High/Medium/Low}

## Quality Gates

- [ ] Entry criteria defined
- [ ] Exit criteria established
- [ ] Quality thresholds documented

## Labels

`test-strategy`, `istqb`, `iso25010`, `quality-gates`

## Estimate

{Strategic planning effort: 2-3 story points}
```

### Playwright 测试实现 Issue 模板（Playwright Test Implementation Issue Template）

```markdown
# Playwright Tests: {Story/Component Name}

## Test Implementation Scope

{Specific user story or component being tested}

## ISTQB Test Case Design

**Test Design Technique**: {Selected ISTQB technique}
**Test Type**: {Functional/Non-Functional/Structural/Change-Related}

## Test Cases to Implement

**Functional Tests:**

- [ ] Happy path scenarios
- [ ] Error handling validation
- [ ] Boundary value testing
- [ ] Input validation testing

**Non-Functional Tests:**

- [ ] Performance testing (response time < {threshold})
- [ ] Accessibility testing (WCAG compliance)
- [ ] Cross-browser compatibility
- [ ] Mobile responsiveness

## Playwright Implementation Tasks

- [ ] Page Object Model development
- [ ] Test fixture setup
- [ ] Test data management
- [ ] Test case implementation
- [ ] Visual regression tests
- [ ] CI/CD integration

## Acceptance Criteria

- [ ] All test cases pass
- [ ] Code coverage targets met (>80%)
- [ ] Performance thresholds validated
- [ ] Accessibility standards verified

## Labels

`playwright`, `e2e-test`, `quality-validation`

## Estimate

{Test implementation effort: 2-5 story points}
```

### 质量保障 Issue 模板（Quality Assurance Issue Template）

```markdown
# Quality Assurance: {Feature Name}

## Quality Validation Scope

{Overall quality validation for feature/epic}

## ISO 25010 Quality Assessment

**Quality Characteristics Validation:**

- [ ] Functional Suitability: Completeness, correctness, appropriateness
- [ ] Performance Efficiency: Time behavior, resource utilization, capacity
- [ ] Usability: Interface aesthetics, accessibility, learnability, operability
- [ ] Security: Confidentiality, integrity, authentication, authorization
- [ ] Reliability: Fault tolerance, recovery, availability
- [ ] Compatibility: Browser, device, integration compatibility
- [ ] Maintainability: Code quality, modularity, testability
- [ ] Portability: Environment adaptability, installation procedures

## Quality Gates Validation

**Entry Criteria:**

- [ ] All implementation tasks completed
- [ ] Unit tests passing
- [ ] Code review approved

**Exit Criteria:**

- [ ] All test types completed with >95% pass rate
- [ ] No critical/high severity defects
- [ ] Performance benchmarks met
- [ ] Security validation passed

## Quality Metrics

- [ ] Test coverage: {target}%
- [ ] Defect density: <{threshold} defects/KLOC
- [ ] Performance: Response time <{threshold}ms
- [ ] Accessibility: WCAG {level} compliance
- [ ] Security: Zero critical vulnerabilities

## Labels

`quality-assurance`, `iso25010`, `quality-gates`

## Estimate

{Quality validation effort: 3-5 story points}
```

## 成功度量（Success Metrics）

### 测试覆盖指标（Test Coverage Metrics）

- 代码覆盖：行覆盖 >80%，关键路径分支覆盖 >90%
- 功能覆盖：100% 验收标准验证
- 风险覆盖：100% 高风险场景测试
- 质量特性覆盖：适用的 ISO 25010 特性均有验证

### 质量验证指标（Quality Validation Metrics）

- 缺陷检出率：>95% 缺陷在生产前发现
- 测试执行效率：>90% 自动化覆盖
- 质量门禁达成：发布前 100% 通过质量门禁
- 风险缓解：100% 已识别风险具备缓解策略

### 过程效率指标（Process Efficiency Metrics）

- 测试规划时间：<2 小时完成完整测试策略
- 测试实现速度：每个用例点 <1 天
- 质量反馈时间：测试完成后 <2 小时完成质量评估
- 文档完整性：100% 测试 Issues 模板信息齐全

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot) 本地化生成，因此可能包含错误。若发现不当或错误翻译，请创建一个[问题](https://github.com/ooccoob/datafill/issues)。
