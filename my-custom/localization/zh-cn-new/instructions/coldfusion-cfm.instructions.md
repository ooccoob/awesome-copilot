---
description: 'ColdFusion cfm文件和应用程序模式'
applyTo: "**/*.cfm"
---

# ColdFusion编码标准

- 尽可能使用CFScript以获得更清洁的语法。
- 避免使用已弃用的标签和函数。
- 遵循变量和组件的一致命名约定。
- 使用`cfqueryparam`防止SQL注入。
- 在<cfoutput>块内使用##转义CSS哈希符号。
- 在<cfoutput>块内使用HTMX时，通过使用双哈希(##)转义哈希符号(#)以防止意外的变量插值。
- 如果您在HTMX目标文件中，请确保顶行是：<cfsetting showDebugOutput = "false">

# 其他最佳实践

- 使用`Application.cfc`进行应用程序设置和请求处理。
- 将代码组织为可重用的CFC（组件）以提高可维护性。
- 验证和清理所有用户输入。
- 使用`cftry`/`cfcatch`进行错误处理和日志记录。
- 避免在源文件中硬编码凭据或敏感数据。
- 使用一致的缩进（2个空格，按照全局标准）。
- 为复杂逻辑添加注释，并用目的和参数记录函数。
- 对于共享模板优先使用`cfinclude`，但避免循环包含。

- 尽可能使用三元运算符
- 确保一致的制表符对齐。