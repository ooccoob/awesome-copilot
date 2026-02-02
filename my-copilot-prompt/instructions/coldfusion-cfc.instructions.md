---
description: 'ColdFusion Coding Standards for CFC component and application patterns'
applyTo: "**/*.cfc"
---

# CFC 文件的 ColdFusion 编码标准

- 尽可能使用 CFScript 以获得更清晰的语法。
- 避免使用已弃用的标签和函数。
- 遵循变量和组件的一致命名约定。
- 使用 `cfqueryparam` 来防止 SQL 注入。
- 使用 ## 在 <cfoutput> 块内转义 CSS 哈希符号

# 其他最佳实践

- 在适当的情况下，对组件属性和方法使用 `this` 范围。
- 记录所有函数的用途、参数和返回值（使用 Javadoc 或类似的风格）。
- 对函数和变量使用访问修饰符（`public`、`private`、`package`、`remote`）。
- 更喜欢依赖注入来进行组件协作。
- 避免 setter/getter 中的业务逻辑；保持简单。
- 验证和清理公共/远程方法中的所有输入参数。
- 根据需要使用 `cftry`/`cfcatch` 在方法内进行错误处理。
- 避免在 CFC 中对配置或凭据进行硬编码。
- 使用一致的缩进（根据全球标准，2 个空格）。
- 在组件内对相关方法进行逻辑分组。
- 为方法和属性使用有意义的描述性名称。
- 避免使用已弃用或不必要的 `cfcomponent` 属性。

- 尽可能使用三元运算符
- 确保标签对齐一致。
