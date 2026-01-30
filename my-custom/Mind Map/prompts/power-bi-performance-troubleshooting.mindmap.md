## Power BI 性能排障指南（思维导图）

- What
  - 模型/报表/查询/容量的系统性性能诊断与优化流程
- When
  - 页面加载>10s、交互>3s、查询>30s、刷新超时/失败
- Why
  - 快速定位瓶颈（模型/度量/可视/容量/网关），给出可执行改进
- How
  - 定义问题与范围→采集基线→分域诊断（模型/DAX/报表/容量）
  - 工具：Performance Analyzer、DAX Studio、Fabric/Premium 容量指标
  - 快速修复：减少可视、上移过滤、优化切片器、精简交互
  - 高级方案：存储模式策略、聚合表、网关与容量扩展
  - 监控：KPI、阈值告警、周/月度健康检查

- Key Points (CN/EN)
  - Baseline; Bottleneck isolation
  - DAX Studio Server Timings
  - Aggregations; Incremental refresh
  - Capacity/Gateway tuning

- Example Questions (≥10)
  1) 最慢页面的三个可视分别耗时多少（查询/渲染占比）？
  2) 哪些度量计算存在深层迭代/上下文切换？
  3) 模型是否存在高基数文本列与多对多导致的开销？
  4) 是否可通过聚合表/增量刷新减少数据量？
  5) 切片器是否高基数且影响全局？可否替换为搜索/层级？
  6) 容量 CPU/内存是否长期高位？是否出现排队/超时？
  7) 网关是否成为瓶颈（并发/带宽/位置）？
  8) 直接查询是否缺少源端索引/折叠？
  9) 移动端/小屏布局是否单独优化？
  10) 快速获益清单与两周内落地路线图？

- Compact Mind Map
  - 问题→基线→诊断→修复→扩展→监控

- Source: prompts/power-bi-performance-troubleshooting.prompt.md
- Generated: 2025-10-17
