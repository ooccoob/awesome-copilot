---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems']
description: '确保Java类型使用Javadoc注释进行记录并遵循文档最佳实践。'
---

# Java文档（Javadoc）最佳实践

- 公共和保护成员应该使用Javadoc注释记录。
- 鼓励记录包私有和私有成员，特别是如果它们复杂或不言自明。
- Javadoc注释的第一句是摘要描述。它应该是对方法功能的简明概述并以句号结尾。
- 对方法参数使用`@param`。描述以小写字母开始且不以句号结尾。
- 对方法返回值使用`@return`。
- 使用`@throws`或`@exception`记录方法抛出的异常。
- 使用`@see`引用其他类型或成员。
- 使用`{@inheritDoc}`从基类或接口继承文档。
  - 除非有重大行为变更，在这种情况下您应该记录差异。
- 对泛型类型或方法中的类型参数使用`@param <T>`。
- 对内联代码片段使用`{@code}`。
- 对代码块使用`<pre>{@code ... }</pre>`。
- 使用`@since`指示功能何时引入（例如版本号）。
- 使用`@version`指定成员的版本。
- 使用`@author`指定代码的作者。
- 使用`@deprecated`将成员标记为过时并提供替代方案。