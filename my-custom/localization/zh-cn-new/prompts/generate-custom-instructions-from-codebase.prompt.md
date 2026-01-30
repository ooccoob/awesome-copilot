---
description: 'GitHub Copilot的迁移和代码演进指令生成器。分析两个项目版本（分支、提交或发布）之间的差异，创建精确的指令，使Copilot能够在技术迁移、重大重构或框架版本升级期间保持一致性。'
mode: 'agent'
---

# 迁移和代码演进指令生成器

## 配置变量

```
${MIGRATION_TYPE="Framework Version|Architecture Refactoring|Technology Migration|Dependencies Update|Pattern Changes"}
<!-- 迁移或演进的类型 -->

${SOURCE_REFERENCE="branch|commit|tag"}
<!-- 源参考点（之前状态） -->

${TARGET_REFERENCE="branch|commit|tag"}
<!-- 目标参考点（之后状态） -->

${ANALYSIS_SCOPE="Entire project|Specific folder|Modified files only"}
<!-- 分析范围 -->

${CHANGE_FOCUS="Breaking Changes|New Conventions|Obsolete Patterns|API Changes|Configuration"}
<!-- 变更的主要方面 -->

${AUTOMATION_LEVEL="Conservative|Balanced|Aggressive"}
<!-- Copilot建议的自动化级别 -->

${GENERATE_EXAMPLES="true|false"}
<!-- 包含转换示例 -->

${VALIDATION_REQUIRED="true|false"}
<!-- 应用前需要验证 -->
```

## 生成的提示

```
"分析两个项目状态之间的代码演进，为GitHub Copilot生成精确的迁移指令。这些指令将指导Copilot在未来修改中自动应用相同的转换模式。遵循此方法论：

### 阶段1：比较状态分析

#### 结构变更检测
- 比较${SOURCE_REFERENCE}和${TARGET_REFERENCE}之间的文件夹结构
- 识别已移动、重命名或删除的文件
- 分析配置文件的变更
- 记录新增和已删除的依赖项

#### 代码转换分析
${MIGRATION_TYPE == "Framework Version" ?
  "- 识别框架版本之间的API变更
   - 分析正在使用的新功能
   - 记录过时的方法/属性
   - 注意语法或约定变更" : ""}

${MIGRATION_TYPE == "Architecture Refactoring" ?
  "- 分析架构模式变更
   - 识别引入的新抽象
   - 记录职责重组
   - 注意数据流变更" : ""}

${MIGRATION_TYPE == "Technology Migration" ?
  "- 分析一项技术被另一项替换
   - 识别功能等价物
   - 记录API和语法变更
   - 注意新的依赖项和配置" : ""}

#### 转换模式提取
- 识别应用的重复转换
- 分析从旧格式到新格式的转换规则
- 记录异常和特殊情况
- 创建前后对应矩阵

### 阶段2：迁移指令生成

创建具有此结构的`.github/copilot-migration-instructions.md`文件：

\`\`\`markdown
# GitHub Copilot迁移指令

## 迁移上下文
- **类型**：${MIGRATION_TYPE}
- **从**：${SOURCE_REFERENCE}
- **到**：${TARGET_REFERENCE}
- **日期**：[GENERATION_DATE]
- **范围**：${ANALYSIS_SCOPE}

## 自动转换规则

### 1. 强制转换
${AUTOMATION_LEVEL != "Conservative" ?
  "[AUTOMATIC_TRANSFORMATION_RULES]
   - **旧模式**：[OLD_CODE]
   - **新模式**：[NEW_CODE]
   - **触发器**：何时检测此模式
   - **操作**：要自动应用的转换" : ""}

### 2. 需要验证的转换
${VALIDATION_REQUIRED == "true" ?
  "[TRANSFORMATIONS_WITH_VALIDATION]
   - **检测到的模式**：[DESCRIPTION]
   - **建议的转换**：[NEW_APPROACH]
   - **需要的验证**：[VALIDATION_CRITERIA]
   - **替代方案**：[ALTERNATIVE_OPTIONS]" : ""}

### 3. API对应关系
${CHANGE_FOCUS == "API Changes" || MIGRATION_TYPE == "Framework Version" ?
  "[API_CORRESPONDENCE_TABLE]
   | 旧API   | 新API   | 注释     | 示例        |
   | --------- | --------- | --------- | -------------- |
   | [OLD_API] | [NEW_API] | [CHANGES] | [CODE_EXAMPLE] | " : ""} |

### 4. 要采用的新模式
[DETECTED_EMERGING_PATTERNS]
- **模式**：[PATTERN_NAME]
- **使用**：[WHEN_TO_USE]
- **实现**：[HOW_TO_IMPLEMENT]
- **好处**：[ADVANTAGES]

### 5. 要避免的过时模式
[DETECTED_OBSOLETE_PATTERNS]
- **过时模式**：[OLD_PATTERN]
- **避免原因**：[REASONS]
- **替代方案**：[NEW_PATTERN]
- **迁移**：[CONVERSION_STEPS]

## 文件类型特定指令

${GENERATE_EXAMPLES == "true" ?
  "### 配置文件
   [CONFIG_TRANSFORMATION_EXAMPLES]

   ### 主要源文件
   [SOURCE_TRANSFORMATION_EXAMPLES]

   ### 测试文件
   [TEST_TRANSFORMATION_EXAMPLES]" : ""}

## 验证和安全

### 自动控制点
- 每次转换后要执行的验证
- 运行以验证变更的测试
- 要监控的性能指标
- 要执行的兼容性检查

### 手动升级
需要人工干预的情况：
- [COMPLEX_CASES_LIST]
- [ARCHITECTURAL_DECISIONS]
- [BUSINESS_IMPACTS]

## 迁移监控

### 跟踪指标
- 自动迁移的代码百分比
- 需要手动验证的次数
- 自动转换的错误率
- 每个文件的平均迁移时间

### 错误报告
如何向Copilot报告不正确的转换：
- 改进规则的反馈模式
- 要记录的异常
- 要对指令进行的调整

\`\`\`

### 阶段3：上下文示例生成

${GENERATE_EXAMPLES == "true" ?
  "#### 转换示例
   对于每个识别的模式，生成：

   \`\`\`
   // 之前 (${SOURCE_REFERENCE})
   [OLD_CODE_EXAMPLE]

   // 之后 (${TARGET_REFERENCE})
   [NEW_CODE_EXAMPLE]

   // COPILOT指令
   当您看到此模式[TRIGGER]时，按照以下步骤将其转换为[NEW_PATTERN]：[STEPS]
   \`\`\`" : ""}

### 阶段4：验证和优化

#### 指令测试
- 在测试代码上应用指令
- 验证转换一致性
- 根据结果调整规则
- 记录异常和边界情况

#### 迭代优化
${AUTOMATION_LEVEL == "Aggressive" ?
  "- 优化规则以最大化自动化
   - 减少检测中的误报
   - 提高转换准确性
   - 记录经验教训" : ""}

### 最终结果

使GitHub Copilot能够的迁移指令：
1. **自动应用** 未来修改中相同的转换
2. **保持一致性** 与新采用的约定
3. **避免过时模式** 通过自动提供替代方案
4. **加速未来迁移** 通过利用获得的经验
5. **减少错误** 通过自动化重复转换

这些指令将Copilot转变为智能迁移助手，能够一致可靠地重现您的技术演进决策。
"
```

## 典型用例

### 框架版本迁移
非常适合记录从Angular 14到Angular 17、React类组件到Hooks，或.NET Framework到.NET Core的转换。自动识别破坏性变更并生成相应的转换规则。

### 技术栈演进
在完全替换技术时必不可少：jQuery到React、REST到GraphQL、SQL到NoSQL。创建具有模式映射的综合迁移指南。

### 架构重构
适用于大型重构，如单体到微服务、MVC到清洁架构，或组件到可组合架构。为未来类似的转换保留架构知识。

### 设计模式现代化
用于采用新模式：仓储模式、依赖注入、观察者到响应式编程。记录基本原理和实现差异。

## 独特优势

### 🧠 **人工智能增强**
与传统迁移文档不同，这些指令"训练"GitHub Copilot在未来代码修改期间自动重现您的技术演进决策。

### 🔄 **知识资本化**
将特定项目经验转换为可重用的规则，避免迁移专业知识流失并加速未来类似的转换。

### 🎯 **上下文感知精度**
不是通用建议，而是生成针对您特定代码库定制的指令，包含来自项目演进的真实前后示例。

### ⚡ **自动化一致性**
确保新的代码添加自动遵循新约定，防止架构回归并保持代码演进一致性。