---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "确保 Java 类型使用 Javadoc 注释并遵循文档最佳实践。"
---

# Java 文档（Javadoc）最佳实践

- 公有与受保护成员应编写 Javadoc 注释。
- 建议为包可见与私有成员也编写注释，尤其当其复杂或不易自解释时。
- Javadoc 第一句为摘要描述，应简洁概述方法作用并以句号结尾。
- 使用 `@param` 描述方法参数，描述以小写字母开头且通常不以句号结尾。
- 使用 `@return` 描述返回值。
- 使用 `@throws`（或 `@exception`）记录方法可能抛出的异常。
- 使用 `@see` 引用其他类型或成员。
- 使用 `{@inheritDoc}` 继承基类或接口的文档。
  - 如存在重要行为差异，应记录差异点。
- 在泛型类型或方法上使用 `@param <T>` 标注类型参数。
- 使用 `{@code}` 书写行内代码片段。
- 使用 `<pre>{@code ... }</pre>` 书写代码块。
- 使用 `@since` 指明功能引入的版本（如版本号）。
- 使用 `@version` 标明成员版本。
- 使用 `@author` 指定作者。
- 使用 `@deprecated` 标记已弃用成员并提供替代方案。

```

```
