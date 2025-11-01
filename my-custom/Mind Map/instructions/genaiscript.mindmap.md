## What/When/Why/How
- What: GenAIScript 代码/脚本生成指引（TS/ESM、全局类型、API 优先）
- When: 需要编写/评审 GenAIScript 脚本或答疑其语法/API 时
- Why: 统一风格、少依赖 Node 内置、简化样例并可审阅（TODO 标注）
- How: 仅用 genaiscript.d.ts 暴露的 API；TypeScript ESM；尽量省异常处理；必要处加 TODO

## Key Points
- 语言: TypeScript + ESM；避免 Node.js imports（除非确需）
- API: 优先使用 GenAIScript 全局类型/函数
- 错误: 示例尽量不包裹复杂异常；不确定点用 TODO 注解
- 可读性: 简短、直观、便于审查

## Compact Map
TS/ESM→全局 API→少异常→TODO 注记→可读示例

## Example Questions (10+)
1) 生成一个最小可运行的 GenAIScript 脚本模板
2) 如何在脚本中引用全局类型而不显式导入？
3) 用 GenAIScript API 实现一个简单的工具链调用
4) 将复杂分支逻辑拆成可读的函数与 TODO 提醒
5) 在不使用 Node 内置模块时如何进行文本处理？
6) 给出脚本参数化与默认值处理的示例
7) 如何组织多段消息与描述信息以复用？
8) 在不捕获异常的前提下标注潜在失败点
9) 生成一个演示脚本并添加审阅 TODO 列表
10) 将已有 Node 风格脚本改为仅用 GenAIScript API

Source: d:\mycode\awesome-copilot\instructions\genaiscript.instructions.md | Generated: 2025-10-17T00:00:00Z
