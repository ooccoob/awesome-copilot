---
description: 'ColdFusion CFC组件和应用程序模式的编码标准'
applyTo: "**/*.cfc"
---

# ColdFusion CFC文件的编码标准

- 尽可能使用CFScript以获得更清洁的语法。
- 避免使用已弃用的标签和函数。
- 遵循变量和组件的一致命名约定。
- 使用`cfqueryparam`防止SQL注入。
- 在<cfoutput>块内使用##转义CSS哈希符号。

# 其他最佳实践

- 适当时对组件属性和方法使用`this`作用域。
- 用目的、参数和返回值记录所有函数（使用Javadoc或类似样式）。
- 对函数和变量使用访问修饰符（`public`、`private`、`package`、`remote`）。
- 优先使用依赖注入进行组件协作。
- 避免在setter/getter中包含业务逻辑；保持简单。
- 在public/remote方法中验证和清理所有输入参数。
- 根据需要在方法内使用`cftry`/`cfcatch`进行错误处理。
- 避免在CFC中硬编码配置或凭据。
- 使用一致的缩进（2个空格，按照全局标准）。
- 在组件内逻辑地分组相关方法。
- 为方法和属性使用有意义的、描述性的名称。
- 避免使用已弃用或不必要的`cfcomponent`属性。

- 尽可能使用三元运算符
- 确保一致的制表符对齐。