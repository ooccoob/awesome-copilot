## What / When / Why / How

- What: Power BI DAX 专家（可读/高效/可维护）
- When: 度量/计算复杂、性能敏感时
- Why: 标准化 DAX 模式提高正确性与可维护
- How: 先查 MS Docs→变量化→上下文控制→时间智能→调试/优化

## Key Points

- 变量：减少重复计算、提升可读性
- 引用：列全限定，度量不限定
- 错误：用 DIVIDE 等容错函数；Power Query 先保证质量
- 性能：减少上下文切换；选择高效函数
- 调试：变量分步；DAX Studio/性能分析

## Compact Map

- 需求→度量设计→变量/上下文
- 时间智能→测试/优化

## Example Questions (10+)

- 这条度量的业务语义是否明确可测？
- 哪些部分可用变量提取减少重复？
- 上下文切换是否必要且可控？
- 时间智能应采用何种标准模式？
- 是否存在昂贵迭代器可替换？
- BLANK 的处理是否正确？
- 度量命名/格式是否一致？
- 性能瓶颈如何验证与定位？
- 计算组是否更合适？
- 与星型模型的契合度如何？

---
Source: d:\mycode\awesome-copilot\chatmodes\power-bi-dax-expert.chatmode.md
Generated: {{timestamp}}
