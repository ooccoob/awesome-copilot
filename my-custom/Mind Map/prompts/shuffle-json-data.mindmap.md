## Shuffle JSON Data — Mind Map

### What
- 在验证结构安全前提下，对重复结构 JSON 对象进行洗牌/重排。

### When
- 需要生成演示/随机化样本或打散偏序但不破坏有效性的场景。

### Why
- 保持数据完整与一致，避免语法破坏或语义混乱。

### How
- 输入校验→变量合并→结构一致性检查→安全洗牌→按原格式输出。

### Key Points (中/英)
- 验证/Validation
- 同构/Homogeneous
- 非嵌套/No nesting (默认)
- 必需属性/Required props
- 忽略属性/Ignore props
- 变量覆盖/Overrides

### Compact map
- Inputs: file + variables
- Validate: syntax, keys set, nesting
- Shuffle: object-level by default
- Output: same encoding/format

### Example Questions (≥10)
- 默认模式下“同构”具体如何判定（键集合一致）？
- 哪些情形必须拒绝洗牌并报错？
- 如何通过变量开启对嵌套结构的安全处理？
- requiredProperties 与 ignoreProperties 的交互规则？
- 如何在保持换行/缩进/编码的同时输出？
- 大文件洗牌的性能与内存建议？
- 稳定随机（可复现种子）是否需要支持？
- 如何在 CI 中自动校验输入 JSON 的可洗牌性？
- 洗牌后的质量校验可输出哪些摘要？
- 失败时应返回怎样的可操作诊断信息？

---
- Source: d:\mycode\awesome-copilot\prompts\shuffle-json-data.prompt.md
- Generated: 2025-10-17
