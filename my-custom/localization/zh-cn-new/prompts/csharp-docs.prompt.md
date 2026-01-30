---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems']
description: '确保C#类型使用XML注释记录并遵循文档最佳实践。'
---

# C#文档最佳实践

- 公共成员应该使用XML注释记录。
- 鼓励也记录内部成员，特别是如果它们复杂或不够自解释。

## 所有API的指导

- 使用`<summary>`提供类型或成员功能的简短一句话描述。以现在时、第三人称动词开始描述摘要。
- 使用`<remarks>`提供额外信息，可以包括实现细节、使用说明或任何其他相关上下文。
- 对语言特定关键字如`null`、`true`、`false`、`int`、`bool`等使用`<see langword>`。
- 对内联代码片段使用`<c>`。
- 对如何使用成员的使用示例使用`<example>`。
  - 对代码块使用`<code>`。`<code>`标签应放在`<example>`标签内。使用`language`属性添加代码示例的语言，例如，`<code language="csharp">`。
- 对内联引用其他类型或成员（在句子中）使用`<see cref>`。
- 对"另请参见"部分中的独立（不在句子中）引用其他类型或成员使用`<seealso>`。
- 使用`<inheritdoc/>`从基类或接口继承文档。
  - 除非有主要行为变更，在这种情况下您应该记录差异。

## 方法

- 使用`<param>`描述方法参数。
  - 描述应该是不指定数据类型的名词短语。
  - 以介绍性冠词开始。
  - 如果参数是标志枚举，以"A bitwise combination of the enumeration values that specifies..."开始描述。
  - 如果参数是非标志枚举，以"One of the enumeration values that specifies..."开始描述。
  - 如果参数是布尔值，措辞应该是"`<see langword="true" />` to ...; otherwise, `<see langword="false" />`."的形式。
  - 如果参数是"out"参数，措辞应该是"When this method returns, contains .... This parameter is treated as uninitialized."的形式。
- 使用`<paramref>`在文档中引用参数名。
- 使用`<typeparam>`描述泛型类型或方法中的类型参数。
- 使用`<typeparamref>`在文档中引用类型参数。
- 使用`<returns>`描述方法返回的内容。
  - 描述应该是不指定数据类型的名词短语。
  - 以介绍性冠词开始。
  - 如果返回类型是布尔值，措辞应该是"`<see langword="true" />` if ...; otherwise, `<see langword="false" />`."的形式。

## 构造函数

- 摘要措辞应该是"Initializes a new instance of the <Class> class [or struct]."。

## 属性

- `<summary>`应该以以下内容开始：
  - "Gets or sets..."用于读写属性。
  - "Gets..."用于只读属性。
  - "Gets [or sets] a value that indicates whether..."用于返回布尔值的属性。
- 使用`<value>`描述属性的值。
  - 描述应该是不指定数据类型的名词短语。
  - 如果属性有默认值，在单独句子中添加，例如，"The default is `<see langword="false" />`"。
  - 如果值类型是布尔值，措辞应该是"`<see langword="true" />` if ...; otherwise, `<see langword="false" />`. The default is ..."的形式。

## 异常

- 使用`<exception cref>`记录构造函数、属性、索引器、方法、运算符和事件抛出的异常。
- 记录成员直接抛出的所有异常。
- 对于嵌套成员抛出的异常，只记录用户最可能遇到的异常。
- 异常描述描述抛出异常的条件。
  - 省略句首的"Thrown if ..."或"If ..."。直接陈述条件，例如"An error occurred when accessing a Message Queuing API."