## What/When/Why/How

- What: Bicep 基础与团队规范：命名/结构/参数与变量/资源引用/依赖/命名策略/安全/文档注释。
- When: 编写/重构/评审 Bicep 模板与模块时；引入新资源或跨模块复用时。
- Why: 提升可读性与可维护性，增强可复用与安全性，减少部署失败与命名冲突。
- How: 采用 lowerCamelCase、使用符号名引用资源、尽量通过现有资源(existing)、用 uniqueString 组合命名、在参数加描述与长度约束、避免泄漏秘密。

## Key Points

- 命名: 变量/参数/资源符号名统一 lowerCamelCase；符号名用资源语义而非“*Name”。
- 结构: 参数置顶并 @description；优先最新稳定 API；限制命名参数最小/最大长度。
- 参数: 默认值偏安全/低成本；@allowed 谨慎使用；跨环境差异走参数。
- 变量: 用于承载复杂表达式，自动推断类型。
- 引用: 用符号名与 .id 建依赖，少用 dependsOn；跨文件/现有资源用 existing；少传过多 output。
- 资源名: 结合 uniqueString()，前缀避免数字开头；子资源用 parent/nesting，避免手工拼 name。
- 安全: 输出中不要包含 secrets/keys；输出用资源属性而不是敏感值。
- 文档: 合理 // 注释，讲清“为什么”。

## Compact Map

- Naming → lowerCamelCase; 语义化符号名
- Parameters → @description; 长度/默认值/少 @allowed
- Variables → 承载复杂表达式
- Resources → 符号名引用; existing; 依赖通过 .id
- Names → uniqueString + 前缀; 子资源 parent
- Security → 不输出 secrets
- Docs → 有用注释

## Example Questions (10+)

1) 如何优雅给参数添加 @description 与长度约束？
2) uniqueString 与环境/订阅/位置组合命名有哪些模式？
3) 何时用 existing 取代跨模块 output/输入？
4) 如何通过符号名隐式表达 dependsOn？
5) 子资源 parent 与嵌套两种写法的取舍？
6) 怎样避免资源名以数字开头导致的校验失败？
7) 参数默认值如何选择低成本 SKU？
8) 复杂表达式应该放变量还是内嵌？
9) 多模块共享资源 ID 的最佳实践？
10) 输出中如何避免暴露机密信息？
11) 迁移到新 API 版本时的最小回归策略？

---
Source: d:\mycode\awesome-copilot\instructions\bicep-code-best-practices.instructions.md | Generated: 2025-10-17
