---
mode: 'agent'
description: '基于新的需求或代码变更，更新既有解决方案规范文件，使其适配生成式 AI 高效消费。'
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 更新规范（Update Specification）

你的任务是根据新需求或代码变更，更新现有规范文件：`${file}`。

规范文件必须清晰定义解决方案组件的需求（Requirements）、约束（Constraints）与接口（Interfaces），并结构化以便生成式 AI 高效解析：准确、无歧义、可追踪、自包含。

## AI 友好规范撰写最佳实践
- 使用精确、明确且无歧义的语言
- 区分：需求 / 约束 / 建议
- 使用结构化格式（标题、列表、表格）
- 避免比喻、口语或上下文缺失引用
- 定义所有缩写与领域术语
- 适当包含示例与边界用例
- 文档必须自包含，不依赖外部上下文

规范文件应保存在 [/spec/](/spec/) 目录，命名模式：`[a-z0-9-]+.md`，文件名需描述内容主题并以高层类别开头（schema/tool/data/infrastructure/process/architecture/design 之一）。

Markdown 必须语法正确且易解析。

使用以下模板完整填充所有部分（Front Matter 示例）：

```md
---
title: [规范主题的简明标题]
version: [可选: 1.0 或 日期]
date_created: [YYYY-MM-DD]
last_updated: [可选: YYYY-MM-DD]
owner: [可选: 负责团队或个人]
tags: [可选: 标签列表，如 infrastructure, process, design]
---

# Introduction
[简述规范目标与适用范围]

## 1. Purpose & Scope
[说明目的、范围、受众、假设]

## 2. Definitions
[定义缩写与术语]

## 3. Requirements, Constraints & Guidelines
- **REQ-001**: Requirement 1
- **SEC-001**: Security Requirement 1
- **[3 LETTERS]-001**: Other Requirement 1
- **CON-001**: Constraint 1
- **GUD-001**: Guideline 1
- **PAT-001**: Pattern 1

## 4. Interfaces & Data Contracts
[接口/数据契约/示例]

## 5. Acceptance Criteria
- **AC-001**: Given … When … Then …
- **AC-002**: System shall … under …

## 6. Test Automation Strategy
- Test Levels: Unit / Integration / E2E
- Frameworks: 列出语言或平台对应
- Test Data Management: …
- CI/CD Integration: …
- Coverage Requirements: …
- Performance Testing: …

## 7. Rationale & Context
[设计与约束背后的动机]

## 8. Dependencies & External Integrations
- **EXT-001**: …
- **SVC-001**: …
- **INF-001**: …
- **DAT-001**: …
- **PLT-001**: …
- **COM-001**: …

## 9. Examples & Edge Cases
```code
// 示例或边界用例
```

## 10. Validation Criteria
[验证规范符合性的检查点]

## 11. Related Specifications / Further Reading
[相关规范链接]
```

---
本地化文件。若发现翻译问题或需改进，请提交 Issue。
