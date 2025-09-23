---
description: "Bicep 基础设施即代码最佳实践"
applyTo: "**/*.bicep"
---

## 命名规范

- 编写 Bicep 代码时，所有名称（变量、参数、资源）均用 lowerCamelCase
- 资源类型建议用描述性符号名（如 'storageAccount'，而非 'storageAccountName'）
- 不要在符号名中使用 'name'，符号名代表资源本身而非资源名称
- 不要通过后缀区分变量和参数

## 结构与声明

- 所有参数应在文件顶部声明，并加 @description 注解
- 所有资源使用最新稳定 API 版本
- 所有参数均加描述性 @description 注解
- 命名参数应指定最小和最大字符长度

## 参数

- 默认值应适合测试环境（如低成本计费档位）
- 谨慎使用 @allowed，避免阻止有效部署
- 部署间变化的设置应用参数实现

## 变量

- 变量类型自动推断自解析值
- 复杂表达式应用变量承载，避免直接嵌入资源属性

## 资源引用

- 资源引用应用符号名，避免用 reference() 或 resourceId() 函数
- 资源依赖通过符号名（如 resourceA.id）建立，避免显式 dependsOn
- 跨资源属性访问用 existing 关键字，不要通过 outputs 传递

## 资源名称

- 用 uniqueString() 模板表达式生成有意义且唯一的资源名
- uniqueString() 结果需加前缀，因部分资源名不能以数字开头

## 子资源

- 避免子资源嵌套过深
- 用 parent 属性或嵌套方式实现子资源关联，避免手动拼接子资源名

## 安全

- 输出中绝不包含密钥或机密
- 输出应直接用资源属性（如 storageAccount.properties.primaryEndpoints）

## 文档

- 在 Bicep 文件中添加有用的 // 注释提升可读性

---

**免责声明**：本文档由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 本地化。如有错误或不当之处，欢迎通过 [issues](../../issues) 反馈。
