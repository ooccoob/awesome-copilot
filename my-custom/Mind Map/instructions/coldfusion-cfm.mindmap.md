## What/When/Why/How

- What: ColdFusion CFM 页面规范：CFScript、输入校验、HTMX 兼容、调试输出控制、SQL 注入防护。
- When: CFM 模板/页面开发与调试。
- Why: 提升安全与可维护性，避免变量插值/调试泄露导致的问题。
- How: 使用 cfqueryparam；在 HTMX 目标文件首行关闭调试；在 <cfoutput> 中使用 ## 转义 #。

## Key Points

- 风格: CFScript 优先；一致命名；2 空格缩进。
- 安全: 输入校验/消毒；cfqueryparam；敏感数据不入源码。
- HTMX: 在 <cfoutput> 中用 ## 避免变量插值；HTMX 目标文件首行 `<cfsetting showDebugOutput = "false">`。
- 架构: 公共逻辑拆到 CFC；cfinclude 复用但避免循环包含。
- 错误: cftry/cfcatch + 日志。

## Compact Map

- Style → CFScript/缩进
- Security → cfqueryparam/输入校验
- HTMX → ## 转义/关闭调试
- Reuse → CFC/包含
- Errors → try/catch

## Example Questions (10+)

1) HTMX 片段如何避免 # 被解释？
2) 何时需要在首行关闭调试输出？
3) 表单输入的标准校验流程？
4) cfincludes 的循环依赖如何检测？
5) 在 CFM 中组织脚本与标签的最佳平衡？
6) 错误日志的字段应包含哪些上下文？
7) 如何将业务逻辑迁移到 CFC？
8) 多环境配置与凭据安全注入怎么做？
9) 防止 XSS 的输出编码策略？
10) 页面片段可测试性的提升方法？

---
Source: d:\mycode\awesome-copilot\instructions\coldfusion-cfm.instructions.md | Generated: 2025-10-17
