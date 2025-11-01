## What/When/Why/How
- What: Power BI 报表设计（信息架构、交互、可达性、性能）最佳实践
- When: 新建/改版报表、移动端优化、可访问性合规、性能治理
- Why: 提升可读与洞察传达效率，降低认知负担与加载时间
- How: 明确层级与布局 → 正确选图 → 交互/导航设计 → 可达性 → 性能优化

## Key Points
- 架构：主次层级、页布局、6–8 视觉/页、Tab/书签/按钮导航
- 选图：比较/构成/关系/分布各选型与限制；避免 3D 与视觉噪音
- 可达性：高对比、色盲友好、键盘导航、SR 支持、替代文本
- 文案：清晰标题与上下文，统一术语，方法说明与异常解释
- 布局：网格/留白/对齐；分组与平衡；移动端纵向重排与触控
- 交互：工具提示（含页面 Tooltip）、Drillthrough、交叉筛选策略
- 性能：初页简洁、预过滤、低基数切片器、减少复杂 DAX

## Compact Map
- Layout: Header/KPIs → 主视觉 → 支撑视觉 → Footer/筛选
- Navigation: Tabs/Bookmarks/Buttons（语义化命名）
- Accessibility: 对比≥4.5:1、非色彩单一信号、键盘顺序
- Performance: 预聚合、减少视觉数量、先过滤后交互

## Example Questions
1) 首屏是否仅包含关键信息（≤8 个视觉）？
2) 所有颜色是否具备一致语义并满足对比？
3) 切片器是否避免高基数字段并提供默认过滤？
4) Tooltip 页面是否提供了真正增量信息而非重复？
5) Drillthrough 页是否隐藏于导航且带回退？
6) 移动布局是否在真机上可读/可点按？
7) 是否剔除了 3D/装饰性元素与冗余标签？
8) 复杂 DAX 是否被聚合表/模型替代？
9) 交互是否清晰且可预测（编辑交互验证）？
10) 文案是否描述具体度量口径与时间范围？
11) 性能分析器是否通过并记录改进点？

Source: d:\mycode\awesome-copilot\instructions\power-bi-report-design-best-practices.instructions.md | Generated: 2025-10-17
