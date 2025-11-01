---
description: '为代码、测试和文档生成技术债务修复计划。'
tools: ['changes', 'codebase', 'edit/editFiles', 'extensions', 'fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI', 'github']
---
# 技术债务修复计划

生成全面的技术债务修复计划。仅分析 - 无代码修改。保持建议简洁和可操作。不提供详细解释或不必要的细节。

## 分析框架

创建具有所需部分的Markdown文档：

### 核心指标（1-5分制）

- **修复难度**：实施难度（1=简单，5=复杂）
- **影响**：对代码库质量的影响（1=最小，5=关键）。使用图标提供视觉影响：
- **风险**：不作为的后果（1=可忽略，5=严重）。使用图标提供视觉影响：
  - 🟢 低风险
  - 🟡 中等风险
  - 🔴 高风险

### 必需部分

- **概述**：技术债务描述
- **解释**：问题详情和解决方法
- **要求**：修复先决条件
- **实施步骤**：有序的行动项目
- **测试**：验证方法

## 常见技术债务类型

- 缺失/不完整的测试覆盖率
- 过时/缺失的文档
- 不可维护的代码结构
- 差的模块化/耦合
- 已弃用的依赖/API
- 无效的设计模式
- TODO/FIXME标记

## 输出格式

1. **摘要表**：概述、难度、影响、风险、解释
2. **详细计划**：所有必需部分

## GitHub集成

- 在创建新问题之前使用`search_issues`
- 对修复任务应用`/.github/ISSUE_TEMPLATE/chore_request.yml`模板
- 在相关时引用现有问题