---
description: 'Specification-Driven Workflow v1 provides a structured approach to software development, ensuring that requirements are clearly defined, designs are meticulously planned, and implementations are thoroughly documented and validated.'
applyTo: '**'
---
# 规范驱动工作流程 v1

**规范驱动的工作流程：**
弥合需求和实施之间的差距。

**始终维护这些工件：**

- **`requirements.md`**：结构化 EARS 表示法中的用户故事和验收标准。
- **`design.md`**：技术架构、序列图、实现注意事项。
- **`tasks.md`**：详细的、可追踪的实施计划。

## 通用文档框架

**文件规则：**
使用详细模板作为所有文档的**主要事实来源**。

**摘要格式：**
仅用于简洁的工件，例如变更日志和拉取请求描述。

### 详细的文档模板

#### 操作文档模板（所有步骤/执行/测试）

```bash
### [TYPE] - [ACTION] - [TIMESTAMP]
**Objective**: [Goal being accomplished]
**Context**: [Current state, requirements, and reference to prior steps]
**Decision**: [Approach chosen and rationale, referencing the Decision Record if applicable]
**Execution**: [Steps taken with parameters and commands used. For code, include file paths.]
**Output**: [Complete and unabridged results, logs, command outputs, and metrics]
**Validation**: [Success verification method and results. If failed, include a remediation plan.]
**Next**: [Automatic continuation plan to the next specific action]
```

#### 决策记录模板（所有决策）

```bash
### Decision - [TIMESTAMP]
**Decision**: [What was decided]
**Context**: [Situation requiring decision and data driving it]
**Options**: [Alternatives evaluated with brief pros and cons]
**Rationale**: [Why the selected option is superior, with trade-offs explicitly stated]
**Impact**: [Anticipated consequences for implementation, maintainability, and performance]
**Review**: [Conditions or schedule for reassessing this decision]
```

### 摘要格式（用于报告）

#### 简化的操作日志

用于生成简洁的变更日志。每个日志条目均源自完整的操作文档。

__代码0__

#### 压缩决策记录

用于拉取请求摘要或执行摘要。

__代码0__

## 执行工作流程（6相循环）

**切勿跳过任何步骤。使用一致的术语。减少歧义。**

### **第 1 阶段：分析**

**目标：**

- 了解问题所在。
- 分析现有系统。
- 产生一套清晰的、可测试的需求。
- 思考可能的解决方案及其影响。

**清单：**

- [ ] 阅读所有提供的代码、文档、测试和日志。
      - 记录文件清单、摘要和初步分析结果。
- [ ] 在 **EARS 符号** 中定义要求：
      - 将功能请求转换为结构化的、可测试的需求。
      - 格式：`WHEN [a condition or event], THE SYSTEM SHALL [expected behavior]`
- [ ] 确定依赖性和约束。
      - 记录包含风险和缓解策略的依赖图。
- [ ] 绘制数据流和交互图。
      - 记录系统交互图和数据模型。
- [ ] 目录边缘情况和失败。
      - 记录全面的边缘案例矩阵和潜在的故障点。
- [ ] 评估信心。
      - 根据需求的清晰度、复杂性和问题范围生成**置信度分数 (0-100%)**。
      - 记录分数及其基本原理。

**关键约束：**

- **在所有要求都明确并记录下来之前，不要继续。**

### **第二阶段：设计**

**目标：**

- 创建全面的技术设计和详细的实施计划。

**清单：**

- [ ] **根据置信度分数定义自适应执行策略：**
  - **高置信度 (>85%)**
    - 制定全面、分步骤的实施计划。
    - 跳过概念验证步骤。
    - 继续全面、自动化的实施。
    - 维护标准的综合文档。
  - **中等置信度 (66–85%)**
    - 优先考虑 **概念验证 (PoC)** 或 **最小可行产品 (MVP)**。
    - 为 PoC/MVP 定义明确的成功标准。
    - 首先构建并验证 PoC/MVP，然后逐步扩展计划。
    - 记录 PoC/MVP 目标、执行和验证结果。
  - **低置信度 (<66%)**
    - 第一阶段致力于研究和知识建设。
    - 使用语义搜索并分析类似的实现。
    - 将研究结果综合成研究文件。
    - 研究后重新运行分析阶段。
    - 仅当信心仍然较低时才升级。

- [ ] **在 `design.md` 中记录技术设计：**
  - **架构：** 组件和交互的高级概述。
  - **数据流：** 图表和描述。
  - **接口：** API 契约、模式、面向公众的函数签名。
  - **数据模型：**数据结构和数据库模式。

- [ ] **文档错误处理：**
  - 创建包含程序和预期响应的错误矩阵。

- [ ] **定义单元测试策略。**

- [ ] **在 `tasks.md` 中创建实施计划：**
  - 对于每项任务，包括描述、预期结果和依赖性。

**关键约束：**

- **在设计和计划完成并经过验证之前，不要继续实施。**

### **第 3 阶段：实施**

**目标：**

- 根据设计和计划编写生产质量的代码。

**清单：**

- [ ] 以小的、可测试的增量编写代码。
      - 使用代码更改、结果和测试链接记录每个增量。
- [ ] 从依赖向上实现。
      - 记录解决顺序、理由和验证。
- [ ] 遵循惯例。
      - 用决策记录记录遵守情况和任何偏差。
- [ ] 添加有意义的评论。
      - 关注意图（“为什么”），而不是机制（“什么”）。
- [ ] 按计划创建文件。
      - 文档文件创建日志。
- [ ] 实时更新任务状态。

**关键约束：**

- **在记录并测试所有实施步骤之前，不要合并或部署代码。**

### **第 4 阶段：验证**

**目标：**

- 验证实施是否满足所有要求和质量标准。

**清单：**

- [ ] 执行自动化测试。
      - 记录输出、日志和覆盖率报告。
      - 对于故障，记录根本原因分析和补救措施。
- [ ] 必要时进行手动验证。
      - 记录程序、清单和结果。
- [ ] 测试边缘情况和错误。
      - 记录结果和正确错误处理的证据。
- [ ] 验证性能。
      - 记录指标并分析关键部分。
- [ ] 记录执行轨迹。
      - 记录路径分析和运行时行为。

**关键约束：**

- **在完成所有验证步骤并解决所有问题之前，请勿继续。**

### **阶段 5：反思**

**目标：**

- 改进代码库、更新文档并分析性能。

**清单：**

- [ ] 重构以提高可维护性。
      - 记录决策、前后比较以及影响。
- [ ] 更新所有项目文档。
      - 确保所有自述文件、图表和注释都是最新的。
- [ ] 确定潜在的改进。
      - 记录待办事项并确定优先级。
- [ ] 验证成功标准。
      - 记录最终验证矩阵。
- [ ] 进行荟萃分析。
      - 反思效率、工具使用和协议遵守情况。
- [ ] 自动创建技术债务问题。
      - 记录库存和补救计划。

**关键约束：**

- **在记录所有文档和改进操作之前，不要关闭该阶段。**

### **阶段 6：交接**

**目标：**

- 打包工作以供审查和部署，并过渡到下一个任务。

**清单：**

- [ ] 生成执行摘要。
      - 使用**压缩决策记录**格式。
- [ ] 准备拉取请求（如果适用）：
    1. 执行摘要。
    2. 来自**简化操作日志**的变更日志。
    3. 验证工件和决策记录的链接。
    4. 指向最终 `requirements.md`、`design.md` 和 `tasks.md` 的链接。
- [ ] 完成工作区。
      - 将中间文件、日志和临时工件存档到 `.agent_work/`。
- [ ] 继续执行下一个任务。
      - 文档转换或完成。

**关键约束：**

- **在所有移交步骤完成并记录之前，不要认为任务已完成。**

## 故障排除和重试协议

**如果您遇到错误、歧义或阻碍：**

**清单：**

1. **重新分析**：
   - 重新审视分析阶段。
   - 确认所有要求和约束都清晰且完整。
2. **重新设计**：
   - 重新审视设计阶段。
   - 根据需要更新技术设计、计划或依赖项。
3. **重新计划**：
   - 调整 `tasks.md` 中的实施计划以解决新发现。
4. **重试执行**：
   - 使用更正的参数或逻辑重新执行失败的步骤。
5. **升级**：
   - 如果重试后问题仍然存在，请遵循升级协议。

**关键约束：**

- **切勿在未解决的错误或含糊之处继续进行。始终记录故障排除步骤和结果。**

## 技术债务管理（自动化）

### 身份证明和文件记录

- **代码质量**：使用静态分析在实施过程中持续评估代码质量。
- **捷径**：在决策记录中明确记录所有速度超过质量的决策及其后果。
- **工作区**：监控组织偏差和命名不一致。
- **文档**：跟踪不完整、过时或丢失的文档。

### 自动发行创建模板

```text
**Title**: [Technical Debt] - [Brief Description]
**Priority**: [High/Medium/Low based on business impact and remediation cost]
**Location**: [File paths and line numbers]
**Reason**: [Why the debt was incurred, linking to a Decision Record if available]
**Impact**: [Current and future consequences (e.g., slows development, increases bug risk)]
**Remediation**: [Specific, actionable resolution steps]
**Effort**: [Estimate for resolution (e.g., T-shirt size: S, M, L)]
```

### 修复（自动优先）

- 通过依赖性分析进行基于风险的优先级排序。
- 工作量估计有助于未来的规划。
- 为大型重构工作提出迁移策略。

## 质量保证（自动化）

### 持续监控

- **静态分析**：检查代码风格、质量、安全漏洞和架构规则遵守情况。
- **动态分析**：监控临时环境中的运行时行为和性能。
- **文档**：自动检查文档的完整性和准确性（例如链接、格式）。

### 质量指标（自动跟踪）

- 代码覆盖率和差距分析。
- 每个函数/方法的循环复杂度得分。
- 可维护性指标评估。
- 技术债务比率（例如，估计的修复时间与开发时间）。
- 文档覆盖率（例如，带注释的公共方法）。

## EARS 符号参考

**EARS（需求语法的简单方法）** - 需求的标准格式：

- **无处不在**：`THE SYSTEM SHALL [expected behavior]`
- **事件驱动**：`WHEN [trigger event] THE SYSTEM SHALL [expected behavior]`
- **状态驱动**：`WHILE [in specific state] THE SYSTEM SHALL [expected behavior]`
- **不需要的行为**：`IF [unwanted condition] THEN THE SYSTEM SHALL [required response]`
- **可选**：`WHERE [feature is included] THE SYSTEM SHALL [expected behavior]`
- **复杂**：上述模式的组合以满足复杂的需求

每项要求必须是：

- **可测试**：可以通过自动或手动测试进行验证
- **明确**：可以进行单一解释
- **必要**：有助于实现系统的目的
- **可行**：可以在限制范围内实施
- **可追溯**：链接到用户需求和设计元素
