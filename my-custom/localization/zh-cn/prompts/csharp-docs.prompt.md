---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems"]
description: "确保 C# 类型使用 XML 注释并遵循文档最佳实践。"
---

# C# 文档注释最佳实践

- 公有成员应使用 XML 注释。
- 建议为内部成员编写注释，尤其是复杂或不易自解释的成员。
- 使用 `<summary>` 描述方法概览，简要说明方法作用。
- 使用 `<param>` 记录方法参数。
- 使用 `<returns>` 记录返回值。
- 使用 `<remarks>` 补充更多信息，可包含实现细节、使用说明或其他上下文。
- 使用 `<example>` 提供如何使用的示例。
- 使用 `<exception>` 记录方法可能抛出的异常。
- 使用 `<see>` 与 `<seealso>` 引用其他类型或成员。
- 使用 `<inheritdoc/>` 继承基类或接口的文档。
  - 若有重要行为差异，应记录差异点。
- 使用 `<typeparam>` 标注泛型类型或方法的类型参数。
- 使用 `<typeparamref>` 在文档中引用类型参数。
- 使用 `<c>` 书写行内代码。
- 使用 `<code>` 书写代码块。
- 使用 `<see langword>` 引用语言关键字，如 `null`、`true`、`false`、`int`、`bool` 等。

```

```
