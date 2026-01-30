## What/When/Why/How

- What: ColdFusion CFC 编码规范：风格/命名/SQL 注入防护/作用域/错误处理/文档。
- When: 编写/评审 CFC 组件与方法时。
- Why: 提升可读性/安全性与可维护性，避免过时特性与注入漏洞。
- How: 偏好 CFScript；统一命名与缩进；使用 cfqueryparam；this 作用域与访问修饰符；函数文档与输入校验。

## Key Points

- 风格: CFScript 优先；2 空格缩进；避免废弃标签/函数。
- 安全: SQL 一律 cfqueryparam；配置/凭据不硬编码；输入校验与清理。
- 作用域/访问: this 属性/方法按需；public/private/package/remote 明确。
- 设计: Setter/Getters 保持简单；依赖注入代替紧耦合；相关方法分组。
- 错误: cftry/cfcatch 适度使用；日志记录。
- 文档: 方法目的/参数/返回值注释。

## Compact Map

- Style → CFScript/缩进
- Security → cfqueryparam/不硬编码
- Scope → this/访问级别
- Design → DI/简洁 getters
- Errors → try/catch
- Docs → 注释

## Example Questions (10+)

1) 何时使用 remote 函数并如何校验参数？
2) cfqueryparam 的类型与长度约束怎么选？
3) CFC 如何进行依赖注入与解耦？
4) 组件属性应放在哪个作用域？
5) 错误处理与日志的边界在哪里？
6) 废弃标签的替代方案？
7) Setter/Getter 中避免业务逻辑的实践？
8) 统一 2 空格缩进的 lint 方案？
9) 如何编写高质量函数注释？
10) 多文件组件的组织策略？

---
Source: d:\mycode\awesome-copilot\instructions\coldfusion-cfc.instructions.md | Generated: 2025-10-17
