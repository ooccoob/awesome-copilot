## What/When/Why/How
- What: Python 代码风格、注释、类型注解与测试实践
- When: 编写/评审 Python 代码与文档时
- Why: 提升可读、可维护与可靠性
- How: 遵循 PEP 8/257，类型注解 + 文档字符串，覆盖边界用例

## Key Points
- 风格：PEP 8；4 空格缩进；行宽≤79；合理空行
- 注释：函数/类 docstring（PEP 257）；解释“为何而非是什么”
- 类型：typing 注解（List/Dict/Optional）；公共 API 全量标注
- 结构：单一职责；拆分复杂函数；清晰命名
- 异常：显式捕获；友好消息；避免裸 except
- 依赖：用途注释；最小化依赖
- 测试：关键路径与边界；示例 + 期望行为

## Compact Map
- Conventions: PEP8/PEP257/typing
- Docs: docstring 参数/返回/异常
- Errors: try/except/raise 自定义异常
- Tests: 单元 + 边界 + 文档示例

## Example Questions
1) 公开函数是否都有类型注解与 docstring？
2) 命名是否表达意图且遵循 snake_case/PascalCase？
3) 复杂函数能否拆解为小函数并复用？
4) 异常是否精确捕获并给出可诊断信息？
5) 注释是否解释设计权衡与原因？
6) 外部库使用是否必要并已注明用途？
7) 常见边界（空、None、大输入）是否覆盖？
8) 模块是否保持单一职责与清晰结构？
9) 文档示例能否直接复制运行？
10) 行为变化是否伴随测试更新？
11) 是否避免魔法数字/字符串并集中常量？

Source: d:\mycode\awesome-copilot\instructions\python.instructions.md | Generated: 2025-10-17
