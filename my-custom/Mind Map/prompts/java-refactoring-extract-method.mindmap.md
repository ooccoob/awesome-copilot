## What

- 使用 Extract Method 对高复杂度方法进行提炼，提高可读性/可测性/复用性，同时保持语义与行为不变。

## When

- LOC>15 / 语句>10 / 圈复杂度>10；或职责不清、嵌套深、重复片段。

## Why

- 降低耦合、提升内聚与一致性，便于单元测试与演进。

## How

- 识别可抽取块（计算/校验/构造/分支）→ 命名表达意图
- 抽取私有方法；保持参数最小与不可变
- 保留功能等价；必要处添加注释与测试
- 输出仅提供完整可编译方法（Java 17），附一行目的注释

## Key points (CN)

- 行为不变；副作用显式
- 降低参数个数；避免隐藏依赖
- 命名清晰，单一职责

## Key points (EN)

- Behavior-preserving extraction; intent-revealing names
- Minimize parameters; explicit side-effects
- Testability and reuse focus

## Example questions

- “对该复杂 if/else 逻辑抽取校验与构造两步？”
- “将循环内重复片段提取为方法并单测？”

## 思维导图（要点）

- 发现→命名→抽取→验证
- 语义等价与测试补齐

—

- Source: d:\mycode\awesome-copilot\prompts\java-refactoring-extract-method.prompt.md
- Generated: 2025-10-17
