---
mode: "agent"
description: "为解决方案创建新的规格说明文件，优化以便生成式 AI 消费。"
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
---

# 创建规格说明（Create Specification）

你的目标是为 `${input:SpecPurpose}` 创建一份新的规格说明文件。

该规格说明必须以清晰、无歧义、便于生成式 AI 高效使用的方式，定义解决方案组件的需求、约束与接口。遵循既定文档标准，确保内容可被机器读取且自包含。

## 面向 AI 的规格最佳实践

- 使用精确、明确、无歧义的语言。
- 清晰区分“需求、约束、建议”。
- 使用结构化格式（标题、列表、表格）便于解析。
- 避免成语、隐喻或依赖上下文的表达。
- 定义所有缩写与领域术语。
- 在适用处提供示例与边界情形。
- 文档须自包含，不依赖外部上下文。

规格文件需保存至 [/spec/](/spec/) 目录，并按如下命名：`spec-[a-z0-9-]+.md`，名称应能描述内容，且以高层目的前缀开始（从以下之一选择：schema、tool、data、infrastructure、process、architecture、design）。

文件必须是格式良好的 Markdown。

规格文件必须遵循以下模板，确保各节内容完整；front matter 需按示例结构：

````md
---
title: [Concise Title Describing the Specification's Focus]
version: [Optional: e.g., 1.0, Date]
date_created: [YYYY-MM-DD]
last_updated: [Optional: YYYY-MM-DD]
owner: [Optional: Team/Individual responsible for this spec]
tags: [Optional: List of relevant tags or categories, e.g., `infrastructure`, `process`, `design`, `app` etc]
---

# Introduction

[A short concise introduction to the specification and the goal it is intended to achieve.]

## 1. Purpose & Scope

[Provide a clear, concise description of the specification's purpose and the scope of its application. State the intended audience and any assumptions.]

## 2. Definitions

[List and define all acronyms, abbreviations, and domain-specific terms used in this specification.]

## 3. Requirements, Constraints & Guidelines

[Explicitly list all requirements, constraints, rules, and guidelines. Use bullet points or tables for clarity.]

- **REQ-001**: Requirement 1
- **SEC-001**: Security Requirement 1
- **[3 LETTERS]-001**: Other Requirement 1
- **CON-001**: Constraint 1
- **GUD-001**: Guideline 1
- **PAT-001**: Pattern to follow 1

## 4. Interfaces & Data Contracts

[Describe the interfaces, APIs, data contracts, or integration points. Use tables or code blocks for schemas and examples.]

## 5. Acceptance Criteria

[Define clear, testable acceptance criteria for each requirement using Given-When-Then format where appropriate.]

- **AC-001**: Given [context], When [action], Then [expected outcome]
- **AC-002**: The system shall [specific behavior] when [condition]
- **AC-003**: [Additional acceptance criteria as needed]

## 6. Test Automation Strategy

[Define the testing approach, frameworks, and automation requirements.]

- **Test Levels**: Unit, Integration, End-to-End
- **Frameworks**: MSTest, FluentAssertions, Moq (for .NET applications)
- **Test Data Management**: [approach for test data creation and cleanup]
- **CI/CD Integration**: [automated testing in GitHub Actions pipelines]
- **Coverage Requirements**: [minimum code coverage thresholds]
- **Performance Testing**: [approach for load and performance testing]

## 7. Rationale & Context

[Explain the reasoning behind the requirements, constraints, and guidelines. Provide context for design decisions.]

## 8. Dependencies & External Integrations

[Define the external systems, services, and architectural dependencies required for this specification. Focus on **what** is needed rather than **how** it's implemented. Avoid specific package or library versions unless they represent architectural constraints.]

### External Systems

- **EXT-001**: [External system name] - [Purpose and integration type]

### Third-Party Services

- **SVC-001**: [Service name] - [Required capabilities and SLA requirements]

### Infrastructure Dependencies

- **INF-001**: [Infrastructure component] - [Requirements and constraints]

### Data Dependencies

- **DAT-001**: [External data source] - [Format, frequency, and access requirements]

### Technology Platform Dependencies

- **PLT-001**: [Platform/runtime requirement] - [Version constraints and rationale]

### Compliance Dependencies

- **COM-001**: [Regulatory or compliance requirement] - [Impact on implementation]

**Note**: This section should focus on architectural and business dependencies, not specific package implementations. For example, specify "OAuth 2.0 authentication library" rather than "Microsoft.AspNetCore.Authentication.JwtBearer v6.0.1".

## 9. Examples & Edge Cases

```code
// Code snippet or data example demonstrating the correct application of the guidelines, including edge cases
```
````

## 10. Validation Criteria

[List the criteria or tests that must be satisfied for compliance with this specification.]

## 11. Related Specifications / Further Reading

[Link to related spec 1]
[Link to relevant external documentation]

```

```
