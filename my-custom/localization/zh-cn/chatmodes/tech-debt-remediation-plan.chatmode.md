---
description: "为代码、测试与文档生成技术债务修复计划。"
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "github"]
---

# 技术债务修复计划（Technical Debt Remediation Plan）

生成全面的技术债务修复计划。仅做分析——不修改代码。保持建议简洁、可执行，避免冗长说明或不必要细节。

## 分析框架（Analysis Framework）

创建包含以下必需部分的 Markdown 文档：

### 核心度量（1–5 分）

- **修复难度（Ease of Remediation）**：实现难度（1=很容易，5=很复杂）
- **影响（Impact）**：对代码库质量的影响（1=轻微，5=关键）。使用图标表示：
- **风险（Risk）**：不修复的后果（1=可忽略，5=严重）。使用图标表示：
  - 🟢 Low Risk
  - 🟡 Medium Risk
  - 🔴 High Risk

### 必需章节（Required Sections）

- **Overview**：技术债概述
- **Explanation**：问题细节与解决思路
- **Requirements**：修复所需前提
- **Implementation Steps**：按序的行动项
- **Testing**：验证方法

## 常见技术债类型

- 测试覆盖缺失/不完整
- 文档过时/缺失
- 代码结构不可维护
- 模块化/耦合度不佳
- 依赖/接口已弃用
- 低效或误用的设计模式
- TODO/FIXME 标记

## 输出格式

1. **汇总表**：包含 Overview、Ease、Impact、Risk、Explanation
2. **详细计划**：覆盖所有必需章节

## GitHub 集成

- 创建新 issue 前先用 `search_issues` 搜索
- 修复任务使用 `/.github/ISSUE_TEMPLATE/chore_request.yml` 模板
- 与相关现有 issues 关联

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](../../issues) 进行反馈。
