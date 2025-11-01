## What/When/Why/How
- What: Power BI 语义模型/数据建模最佳实践（星型、关系、存储模式）
- When: 设计新模型或重构、性能/成本问题、DirectQuery/复合模型决策时
- Why: 性能、可维护性、可理解性与治理都依赖良好建模
- How: 维度/事实分离、单向过滤、键与索引、存储与分区、RLS 与治理

## Key Points
- 星型：维度小而描述、事实细粒度；避免过度雪花与单大表
- 关系：维度(1)→事实(*) 单向；避免环与滥用双向；桥表处理 M2M
- 存储：Import/DirectQuery/Dual/Hybrid；增量刷新；预聚合
- 性能：列/行裁剪、数据类型优化、索引、查询简化、慢查询治理
- 时间：日期表规范（标记 Date 表）；SCD1/2；角色扮演维度 USERELATIONSHIP
- 安全：RLS 动态/基于角色；治理文档与血缘；版本与变更管理

## Compact Map
- Fact：外键、数字度量、统一粒度
- Dim：代理键、层级、描述列、Unknown 行
- Relations：单向、避免环、桥表处理多对多
- Storage：Import for 维度/汇总，DQ for 海量事实，Dual for 共享维度
- Advanced：复合模型、聚合表、增量刷新、分区策略

## Example Questions
1) 该表是事实还是维度？粒度是否一致？
2) 有无不必要的文本列/计算列可以下推到 Power Query？
3) 关系是否单向且无环？多对多是否用桥表？
4) DirectQuery 索引与物化视图是否合理？
5) 日期表是否连续并被标记为 Date 表？
6) 是否需要 Dual/Hybrid 支撑复合模型？
7) 行列裁剪是否到位，容量与刷新策略是否匹配？
8) RLS 与治理文档是否完备且已测试？
9) 复杂度高的 DAX 能否转为聚合表？
10) 是否记录与验证了业务口径（度量定义）？
11) 性能分析器/DAX Studio 发现的瓶颈是什么？

Source: d:\mycode\awesome-copilot\instructions\power-bi-data-modeling-best-practices.instructions.md | Generated: 2025-10-17
