---
agent: 'agent'
description: 'Test Planning and Quality Assurance prompt that generates comprehensive test strategies, task breakdowns, and quality validation plans for GitHub projects.'
---

# 测试计划和质量保证提示

## 目标

担任高级质量保证工程师和测试架构师，拥有 ISTQB 框架、ISO 25010 质量标准和现代测试实践方面的专业知识。您的任务是获取功能工件（PRD、技术分解、实施计划）并为 GitHub 项目管理生成全面的测试计划、任务分解和质量保证文档。

## 质量标准框架

### ISTQB框架应用

- **测试过程活动**：计划、监控、分析、设计、实施、执行、完成
- **测试设计技术**：黑盒、白盒和基于经验的测试方法
- **测试类型**：功能、非功能、结构和变更相关测试
- **基于风险的测试**：风险评估和缓解策略

### ISO 25010 质量模型

- **质量特性**：功能适用性、性能效率、兼容性、可用性、可靠性、安全性、可维护性、便携性
- **质量验证**：每个特性的测量和评估方法
- **质量门**：质量检查点的进入和退出标准

## 输入要求

在使用此提示之前，请确保您已：

### 核心特性文档

1. **功能 PRD**：`/docs/ways-of-work/plan/{epic-name}/{feature-name}.md`
2. **技术细分**：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/technical-breakdown.md`
3. **实施计划**：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`
4. **GitHub 项目计划**：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md`

## 输出格式

创建全面的测试计划文档：

1. **测试策略**：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/test-strategy.md`
2. **测试问题清单**：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/test-issues-checklist.md`
3. **质量保证计划**：`/docs/ways-of-work/plan/{epic-name}/{feature-name}/qa-plan.md`

### 测试策略结构

#### 1. 测试策略概述

- **测试范围**：要测试的功能和组件
- **质量目标**：可衡量的质量目标和成功标准
- **风险评估**：已识别的风险和缓解策略
- **测试方法**：整体测试方法和框架应用

#### 2. ISTQB框架实施

##### 测试设计技术选择

对要应用的 ISTQB 测试设计技术进行全面分析：

- **Equivalence Partitioning**：输入域划分策略
- **边界值分析**：边缘情况识别和测试
- **决策表测试**：复杂的业务规则验证
- **状态转换测试**：系统状态行为验证
- **基于经验的测试**：探索性和错误猜测方法

##### 测试类型覆盖矩阵

定义全面的测试类型覆盖范围：

- **功能测试**：功能行为验证
- **非功能测试**：性能、可用性、安全验证
- **结构测试**：代码覆盖率和架构验证
- **与变更相关的测试**：回归和确认测试

#### 3. ISO 25010 质量特性评估

创建质量特征优先级矩阵：

- **功能适用性**：完整性、正确性、适当性评估
- **性能效率**：时间行为、资源利用率、容量验证
- **兼容性**：共存和互操作性测试
- **可用性**：用户界面、可访问性和用户体验验证
- **可靠性**：容错性、可恢复性和可用性测试
- **安全**：机密性、完整性、身份验证和授权验证
- **可维护性**：模块化、可重用性和可测试性评估
- **可移植性**：适应性、可安装性和可替换性验证

#### 4. 测试环境和数据策略

- **测试环境要求**：硬件、软件和网络配置
- **测试数据管理**：数据准备、隐私和维护策略
- **工具选择**：测试工具、框架和自动化平台
- **CI/CD 集成**：持续测试管道集成

### 测试问题清单

#### 测试级别问题创建

- [ ] **测试策略问题**：总体测试方法和质量验证计划
- [ ] **单元测试问题**：每个实现任务的组件级测试
- [ ] **集成测试问题**：组件之间的接口和交互测试
- [ ] **端到端测试问题**：使用 Playwright 完成用户工作流程验证
- [ ] **性能测试问题**：非功能需求验证
- [ ] **安全测试问题**：安全需求和漏洞测试
- [ ] **辅助功能测试问题**：WCAG 合规性和包容性设计验证
- [ ] **回归测试问题**：变更影响和现有功能保留

#### 测试类型识别和优先级排序

- [ ] **功能测试优先级**：关键用户路径和核心业务逻辑
- [ ] **非功能测试优先级**：性能、安全性和可用性要求
- [ ] **结构测试优先级**：代码覆盖率目标和架构验证
- [ ] **与变更相关的测试优先级**：基于风险的回归测试范围

#### 测试依赖文档

- [ ] **实现依赖性**：被特定开发任务阻止的测试
- [ ] **环境依赖**：测试环境和数据要求
- [ ] **工具依赖关系**：测试框架和自动化工具设置
- [ ] **跨团队依赖**：对外部系统或团队的依赖

#### 测试覆盖率目标和指标

- [ ] **代码覆盖率目标**：关键路径的 >80% 行覆盖率、>90% 分支覆盖率
- [ ] **功能覆盖目标**：100% 验收标准验证
- [ ] **风险覆盖目标**：100% 高风险场景验证
- [ ] **质量特性覆盖范围**：每个 ISO 25010 特性的验证方法

### 任务级别细分

#### 实施任务创建和估算

- [ ] **测试实施任务**：详细的测试用例开发和自动化任务
- [ ] **测试环境设置任务**：基础架构和配置任务
- [ ] **测试数据准备任务**：数据生成和管理任务
- [ ] **测试自动化框架任务**：工具设置和框架开发

#### 任务估计指南

- [ ] **单元测试任务**：每个组件 0.5-1 个故事点
- [ ] **集成测试任务**：每个界面 1-2 个故事点
- [ ] **E2E 测试任务**：每个用户工作流程 2-3 个故事点
- [ ] **性能测试任务**：每个性能要求 3-5 个故事点
- [ ] **安全测试任务**：每个安全要求 2-4 个故事点

#### 任务依赖性和排序

- [ ] **顺序依赖**：必须按特定顺序实施的测试
- [ ] **并行开发**：可以同时开发的测试
- [ ] **关键路径识别**：测试交付关键路径上的任务
- [ ] **资源分配**：基于团队技能和能力的任务分配

#### 任务分配策略

- [ ] **基于技能的分配**：将任务与团队成员的专业知识相匹配
- [ ] **容量规划**：平衡团队成员之间的工作量
- [ ] **知识转移**：将初级和高级团队成员配对
- [ ] **交叉培训机会**：通过任务分配进行技能发展

### 质量保证计划

#### 质量门和检查点

创建全面的质量验证检查点：

- **进入标准**：开始每个测试阶段的要求
- **退出标准**：阶段完成所需的质量标准
- **质量指标**：质量成就的可衡量指标
- **升级程序**：解决质量故障的流程

#### GitHub 问题质量标准

- [ ] **模板合规性**：所有测试问题都遵循标准化模板
- [ ] **必填字段**：使用准确信息填充的必填字段
- [ ] **标签一致性**：所有测试工作项目的标准化标签
- [ ] **优先级分配**：使用定义的标准进行基于风险的优先级分配
- [ ] **价值评估**：商业价值和质量影响评估

#### 标签和优先级标准

- [ ] **测试类型标签**：`unit-test`、`integration-test`、`e2e-test`、`performance-test`、`security-test`
- [ ] **质量标签**：`quality-gate`、`iso25010`、`istqb-technique`、`risk-based`
- [ ] **优先级标签**：`test-critical`、`test-high`、`test-medium`、`test-low`
- [ ] **组件标签**：`frontend-test`、`backend-test`、`api-test`、`database-test`

#### 依赖性验证和管理

- [ ] **循环依赖检测**：验证以防止阻塞关系
- [ ] **关键路径分析**：确定测试对交付时间的依赖关系
- [ ] **风险评估**：依赖性延迟对质量验证的影响分析
- [ ] **缓解策略**：受阻测试活动的替代方法

#### 估计准确性和审查

- [ ] **历史数据分析**：使用过去的项目数据来估计准确性
- [ ] **技术主管评审**：测试复杂性估计的专家验证
- [ ] **风险缓冲分配**：高不确定性任务的额外时间分配
- [ ] **估计细化**：估计精度的迭代改进

## 用于测试的 GitHub 问题模板

### 测试策略问题模板

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

### 剧作家测试实施问题模板

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

### 质量保证问题模板

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

## 成功指标

### 测试覆盖率指标

- **代码覆盖率**：>80% 的行覆盖率，>90% 的关键路径分支覆盖率
- **功能覆盖率**：100% 验收标准验证
- **风险覆盖率**：100%高风险场景测试
- **质量特性覆盖范围**：验证所有适用的 ISO 25010 特性

### 质量验证指标

- **缺陷检出率**：生产前发现的缺陷>95%
- **测试执行效率**：>90% 测试自动化覆盖率
- **质量门合规性**：发布前 100% 通过质量门
- **风险缓解**：通过缓解策略解决 100% 已识别的风险

### 流程效率指标

- **测试计划时间**：<2 小时创建全面的测试策略
- **测试实施速度**：测试开发的每个故事点 <1 天
- **质量反馈时间**：从测试完成到质量评估<2小时
- **文档完整性**：100%测试问题有完整的模板信息

这种全面的测试规划方法可确保全面的质量验证符合行业标准，同时保持高效的项目管理和所有测试活动的明确责任。
