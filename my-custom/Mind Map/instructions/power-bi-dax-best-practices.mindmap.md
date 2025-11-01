## What/When/Why/How
- What: Power BI DAX 可维护与高性能编写指南
- When: 新增/重构度量、发现性能问题、建立团队规范
- Why: 通过变量、上下文管理与时序函数提升可读与性能
- How: 变量优先、CALCULATE 正确用法、时间智能与调试策略

## Key Points
- 变量：VAR/RETURN 提升可读/复用/性能；一次计算多处使用
- 引用：列始终表限定；度量不表限定；命名清晰分层
- 错误：DIVIDE 优于 /；防御性设计避免 IFERROR 滥用
- 过滤：CALCULATE 直接表达式优先，少 FILTER(table, ...)
- 时间：YTD/MTD/QoQ/YoY 正确日期表与 DATES* 函数
- 排名与累计：RANKX、运行总和、ABC/Pareto 模式
- 性能：减少嵌套 CALCULATE、避免不必要上下文转换
- 调试：逐步变量返回、性能计时、边界用例验证

## Compact Map
- Base → Derived → KPI 分层命名
- Time: DATESYTD/DATESBETWEEN/DATEADD/SAMEPERIODLASTYEAR
- Context: 行/筛选/上下文转换语义
- Patterns: TopN with ties、Dynamic measure selector

## Example Questions
1) 是否用 VAR 提取昂贵子表达式并复用？
2) 列是否全部表限定、度量是否不带表前缀？
3) CALCULATE 是否用多个直接过滤而非内联 FILTER？
4) 时间智能是否基于“标记的”日期表？
5) 是否避免了将 BLANK 过早转为 0 的反模式？
6) 复杂度高的度量能否下推到模型/聚合？
7) 是否提供了调试 measure（步骤返回/耗时）？
8) 是否存在不必要的上下文转换或迭代器？
9) 命名是否分层（Base/Derived/KPI），含义清晰？
10) 关键口径是否附带业务注释与版本历史？
11) 性能分析器显示的热点在何处，如何量化改进？

Source: d:\mycode\awesome-copilot\instructions\power-bi-dax-best-practices.instructions.md | Generated: 2025-10-17
