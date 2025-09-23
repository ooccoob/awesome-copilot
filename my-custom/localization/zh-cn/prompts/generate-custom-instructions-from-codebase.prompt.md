---
description: "为 GitHub Copilot 生成迁移与演进说明：比较两个项目版本并产出精确的自动化指导，确保技术迁移/重构的一致性。"
---

# 迁移与代码演进说明生成器

## 配置变量

```
${MIGRATION_TYPE="Framework Version|Architecture Refactoring|Technology Migration|Dependencies Update|Pattern Changes"}
<!-- 迁移或演进的类型 -->

${SOURCE_REFERENCE="branch|commit|tag"}
<!-- 源参考点（变更前状态） -->

${TARGET_REFERENCE="branch|commit|tag"}
<!-- 目标参考点（变更后状态） -->

${ANALYSIS_SCOPE="Entire project|Specific folder|Modified files only"}
<!-- 分析范围 -->

${CHANGE_FOCUS="Breaking Changes|New Conventions|Obsolete Patterns|API Changes|Configuration"}
<!-- 关注的主要变更方面 -->

${AUTOMATION_LEVEL="Conservative|Balanced|Aggressive"}
<!-- Copilot 建议的自动化程度 -->

${GENERATE_EXAMPLES="true|false"}
<!-- 是否包含转换示例 -->

${VALIDATION_REQUIRED="true|false"}
<!-- 是否在应用前要求验证 -->
```

## 生成的提示词

```
"分析两个项目状态之间的代码演进，生成可供 GitHub Copilot 使用的精准迁移说明。这些说明将指导 Copilot 在未来修改中自动应用相同的转换模式。请遵循以下方法：

### 阶段 1：对比状态分析

#### 结构变更检测
- 比较 ${SOURCE_REFERENCE} 与 ${TARGET_REFERENCE} 的文件夹结构
- 识别移动、重命名、删除的文件
- 分析配置文件变更
- 记录新增与移除的依赖

#### 代码转换分析
${MIGRATION_TYPE == "Framework Version" ?
  "- 识别框架版本之间的 API 变化
   - 分析新特性的使用
   - 记录已废弃的方法/属性
   - 注意语法或约定的变化" : ""}

${MIGRATION_TYPE == "Architecture Refactoring" ?
  "- 分析架构模式的变化
   - 识别引入的新抽象
   - 记录职责重组
   - 注意数据流的变化" : ""}

${MIGRATION_TYPE == "Technology Migration" ?
  "- 分析技术替换
   - 识别功能等价点
   - 记录 API 与语法变化
   - 注意新依赖与配置" : ""}

#### 转换模式提取
- 识别重复发生的转换
- 分析从旧到新的转换规则
- 记录例外与特殊情况
- 创建前后对应矩阵

### 阶段 2：迁移说明生成

创建 `.github/copilot-migration-instructions.md`，结构如下：

\`\`\`markdown
# GitHub Copilot Migration Instructions

## Migration Context
- **Type**: ${MIGRATION_TYPE}
- **From**: ${SOURCE_REFERENCE}
- **To**: ${TARGET_REFERENCE}
- **Date**: [GENERATION_DATE]
- **Scope**: ${ANALYSIS_SCOPE}

## Automatic Transformation Rules

### 1. Mandatory Transformations
${AUTOMATION_LEVEL != "Conservative" ?
  "[AUTOMATIC_TRANSFORMATION_RULES]
   - **Old Pattern**: [OLD_CODE]
   - **New Pattern**: [NEW_CODE]
   - **Trigger**: When to detect this pattern
   - **Action**: Transformation to apply automatically" : ""}

### 2. Transformations with Validation
${VALIDATION_REQUIRED == "true" ?
  "[TRANSFORMATIONS_WITH_VALIDATION]
   - **Detected Pattern**: [DESCRIPTION]
   - **Suggested Transformation**: [NEW_APPROACH]
   - **Required Validation**: [VALIDATION_CRITERIA]
   - **Alternatives**: [ALTERNATIVE_OPTIONS]" : ""}

### 3. API Correspondences
${CHANGE_FOCUS == "API Changes" || MIGRATION_TYPE == "Framework Version" ?
  "[API_CORRESPONDENCE_TABLE]
   | Old API   | New API   | Notes     | Example        |
   | --------- | --------- | --------- | -------------- |
   | [OLD_API] | [NEW_API] | [CHANGES] | [CODE_EXAMPLE] | " : ""} |

### 4. New Patterns to Adopt
[DETECTED_EMERGING_PATTERNS]
- **Pattern**: [PATTERN_NAME]
- **Usage**: [WHEN_TO_USE]
- **Implementation**: [HOW_TO_IMPLEMENT]
- **Benefits**: [ADVANTAGES]

### 5. Obsolete Patterns to Avoid
[DETECTED_OBSOLETE_PATTERNS]
- **Obsolete Pattern**: [OLD_PATTERN]
- **Why Avoid**: [REASONS]
- **Alternative**: [NEW_PATTERN]
- **Migration**: [CONVERSION_STEPS]

## File Type Specific Instructions

${GENERATE_EXAMPLES == "true" ?
  "### Configuration Files
   [CONFIG_TRANSFORMATION_EXAMPLES]

   ### Main Source Files
   [SOURCE_TRANSFORMATION_EXAMPLES]

   ### Test Files
   [TEST_TRANSFORMATION_EXAMPLES]" : ""}

## Validation and Security

### Automatic Control Points
- Verifications to perform after each transformation
- Tests to run to validate changes
- Performance metrics to monitor
- Compatibility checks to perform

### Manual Escalation
Situations requiring human intervention:
- [COMPLEX_CASES_LIST]
- [ARCHITECTURAL_DECISIONS]
- [BUSINESS_IMPACTS]

## Migration Monitoring

### Tracking Metrics
- Percentage of code automatically migrated
- Number of manual validations required
- Error rate of automatic transformations
- Average migration time per file

### Error Reporting
How to report incorrect transformations to Copilot:
- Feedback patterns to improve rules
- Exceptions to document
- Adjustments to make to instructions

\`\`\`

### 阶段 3：上下文示例生成

${GENERATE_EXAMPLES == "true" ?
  "#### Transformation Examples
   对每个已识别的模式，生成：

   \`\`\`
   // BEFORE (${SOURCE_REFERENCE})
   [OLD_CODE_EXAMPLE]

   // AFTER (${TARGET_REFERENCE})
   [NEW_CODE_EXAMPLE]

   // COPILOT INSTRUCTIONS
   当检测到 [TRIGGER] 模式时，将其转换为 [NEW_PATTERN]，步骤： [STEPS]
   \`\`\`" : ""}

### 阶段 4：验证与优化

#### 说明测试
- 在测试代码上应用说明
- 验证转换一致性
- 根据结果调整规则
- 记录例外与边界情形

#### 迭代优化
${AUTOMATION_LEVEL == "Aggressive" ?
  "- 优化规则以最大化自动化
   - 降低检测的误报
   - 提升转换准确性
   - 记录经验教训" : ""}

### 最终结果

使 GitHub Copilot 能够：
1. 在未来修改中自动应用相同转换
2. 与新采用的约定保持一致
3. 自动提出替代方案以避免过时模式
4. 复用迁移经验以加速后续演进
5. 通过自动化减少错误

这些说明将 Copilot 转变为智能迁移助手，能够持续、可靠地复现你的技术演进决策。
"
```

## 典型用例

### 框架版本迁移

适用于记录从 Angular 14 → 17、React Class → Hooks、或 .NET Framework → .NET Core 的迁移。自动识别不兼容变更并生成相应转换规则。

### 技术栈演进

替换整项技术时必备：如 jQuery → React、REST → GraphQL、SQL → NoSQL。生成全面的迁移指南与模式映射。

### 架构重构

适合大型重构：单体 → 微服务、MVC → Clean Architecture、Component → Composable。为后续类似改造保留经验。

### 设计模式现代化

用于引入新模式：Repository、DI、从 Observer 到 Reactive Programming。记录动机与实现差异。

## 独特优势

### 🧠 人工智能增强

与传统迁移文档不同，这些说明“训练”GitHub Copilot 在未来修改中自动复现你的技术演进决策。

### 🔄 知识沉淀

将特定项目经验转化为可复用规则，避免知识流失，加速后续类似迁移。

### 🎯 上下文感知的精确性

不是通用建议，而是基于你代码库的定制化说明，并包含真实的前后对照示例。

### ⚡ 自动化一致性

确保新增代码自动遵循新约定，避免架构回退，保持代码演进连贯性。
