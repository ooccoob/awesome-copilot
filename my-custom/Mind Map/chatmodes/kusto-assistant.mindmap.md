## What / When / Why / How

- What: Kusto (KQL) 助手（查询/调优/可视化/诊断）
- When: 需要在 Azure Data Explorer/Log Analytics 中编写与优化查询
- Why: 快速定位问题与洞察、优化成本与性能
- How: 需求→样本→查询→分析→可视化/导出→复用

## Key Points

- 语法：let/extend/summarize/join/project/parse
- 性能：时间/范围过滤、索引、分片
- 调优：探查→算子重排→限制输出
- 可视化：render 系列
- 诊断：异常/空洞/尖峰

## Compact Map

- 数据源/范围
- 查询构造/验证
- 性能与成本
- 可视化与导出
- 模板与复用

## Example Questions (10+)

- 数据范围与时间窗如何限定？
- 哪些计算可以提前过滤或预聚合？
- join 的基数与方向如何选择？
- 如何识别与修复慢查询？
- render 选择哪种图表最有效？
- 样本/异常数据如何验证？
- 查询结果如何导出与共享？
- 通用查询如何模板化复用？
- 成本控制策略是什么？
- 监控与告警如何设置？
- 常见反模式有哪些？

---
Source: d:\mycode\awesome-copilot\chatmodes\kusto-assistant.chatmode.md
Generated: {{timestamp}}
