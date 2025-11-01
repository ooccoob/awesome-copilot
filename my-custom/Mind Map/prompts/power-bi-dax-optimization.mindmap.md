## Power BI DAX 优化器（思维导图）

- What
  - 分析/优化 DAX 公式以提升性能、可读性与可维护性
- When
  - 可视刷新慢、模型复杂、度量依赖深
- Why
  - 通过变量/上下文优化/函数替换显著降低计算代价
- How
  - 性能：识别昂贵迭代/重复计算；避免不必要的上下文切换
  - 可读性：命名良好的 VAR；结构化缩进与注释
  - 最佳实践：DIVIDE 防 0；COUNTROWS vs COUNT；SELECTEDVALUE
  - 可维护性：参数化常量、复用中间结果、减少列计算
  - 输出：优化后公式 + 变更解释 + 预期收益

- Key Points (CN/EN)
  - Context transition; Iterators
  - VAR caching; DIVIDE
  - Filter efficiency; Table expr

- Example Questions (≥10)
  1) 当前最慢的 3 个度量是什么？能否拆分为 VAR？
  2) 是否使用 FILTER 作为筛选参数导致过度扫描？
  3) 能否将除法替换为 DIVIDE 增强健壮性？
  4) 哪些列计算可改为度量以减小模型？
  5) 是否存在反复计算的表达式可缓存为 VAR？
  6) 时间智能是否可替换为标准模式（YoY/移动平均）？
  7) 是否存在过深依赖链导致的 FE 压力？
  8) 空值/BLANK 行为是否被正确保持？
  9) 复杂筛选能否改写为表表达式以提升选择性？
  10) 优化前后性能对比与回归测试计划？

- Compact Mind Map
  - 性能→可读性→最佳实践→可维护性→验证

- Source: prompts/power-bi-dax-optimization.prompt.md
- Generated: 2025-10-17
