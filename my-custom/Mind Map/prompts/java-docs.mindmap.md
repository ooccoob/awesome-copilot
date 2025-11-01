## What
- Java Javadoc 文档最佳实践与注解规范，覆盖可见性、标签与代码片段表达。

## When
- 公有/受保护成员（推荐私有/包级）需要清晰文档；复杂实现需补全说明时。

## Why
- 提升可读性、可维护性与 API 一致性，便于使用与演进。

## How
- 摘要首句为概述并以句号结束
- @param/@return/@throws/@see/@since/@version/@deprecated
- {@inheritDoc} 继承文档（行为变化需说明）
- {@code} 行内；<pre>{@code ...}</pre> 代码块
- 泛型类型参数：@param <T>

## Key points (CN)
- 文档“讲做什么”不复述实现
- 统一语气与术语；必要处链接参照
- 异常与版本信息完整

## Key points (EN)
- Clear summaries; proper tags usage
- Inherit docs when applicable; document deltas
- Inline and block code formatting conventions

## Example questions
- “为此公共方法添加完整 Javadoc（含异常）？”
- “如何在泛型类中标注类型参数说明？”

## 思维导图（要点）
- 摘要/标签
- 继承/差异
- 代码格式
- 版本/弃用

—
- Source: d:\mycode\awesome-copilot\prompts\java-docs.prompt.md
- Generated: 2025-10-17
