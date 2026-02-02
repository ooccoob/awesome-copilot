---
description: 'ColdFusion cfm files and application patterns'
applyTo: "**/*.cfm"
---

# ColdFusion 编码标准

- 尽可能使用 CFScript 以获得更清晰的语法。
- 避免使用已弃用的标签和函数。
- 遵循变量和组件的一致命名约定。
- 使用 `cfqueryparam` 来防止 SQL 注入。
- 使用 ## 在 <cfoutput> 块内转义 CSS 哈希符号
- 在 <cfoutput> 块内使用 HTMX 时，请使用双散列 (##) 转义散列符号 (#)，以防止意外的变量插值。
- 如果您位于 HTMX 目标文件中，请确保顶行是： <cfsetting showDebugOutput = "false">

# 其他最佳实践

- 使用 `Application.cfc` 进行应用程序设置和请求处理。
- 将代码组织成可重用的 CFC（组件）以实现可维护性。
- 验证并清理所有用户输入。
- 使用 `cftry`/`cfcatch` 进行错误处理和日志记录。
- 避免在源文件中硬编码凭据或敏感数据。
- 使用一致的缩进（根据全球标准，2 个空格）。
- 使用目的和参数注释复杂的逻辑和文档函数。
- 对于共享模板，首选 `cfinclude`，但避免循环包含。

- 尽可能使用三元运算符
- 确保标签对齐一致。
