## What/When/Why/How
- What: Power BI 自定义可视化（React/D3/TS）开发要点与工程清单
- When: 需实现内置图表无法满足的交互/渲染/格式化能力时
- Why: 将业务专属视觉编码为复用组件，增强生态、提升可解释性
- How: 遵循 API/Capabilities/FormattingModel/Interactivity/Testing 体系化落地

## Key Points
- 工程：pbiviz 工具初始化；tsconfig 合理；开发 server 与热更新
- 结构：Visual 类生命周期 update/constructor；DataView 解析与映射
- React 集成：ReactDOM.render/props 传递；拆分组件；最小重渲染
- D3：选择/数据绑定/比例尺/过渡；与 Power BI 选择器与交互对齐
- 格式化：FormattingModel 卡片/属性；条件格式；颜色与数据点开关
- 交互：选择管理/上下文菜单/工具提示 wrapper；Landing Page
- 测试：Jest/RTL/可视化测试工具；Host mock；覆盖关键路径
- 性能：数据裁剪（dataReduction）、虚拟化、rAF 队列、差量更新

## Compact Map
- API：IVisual/IVisualHost/DataView/SelectionManager/TooltipService
- Capabilities：dataViewMappings、objects、dataRoles、suppressDefaultTitle
- Formatting：formattingSettings utils -> cards/properties
- Interactivity：select/clear/contextmenu；工具提示信息结构
- 构建/打包：pbiviz package；AppSource 发布合规检查

## Example Questions
1) DataView 到组件 props 的映射是否清晰且最小？
2) 选择/高亮/上下文菜单是否与宿主行为一致？
3) FormattingModel 是否覆盖关键自定义项并有默认值？
4) 大数据量下是否启用窗口/TopN 裁剪与差量渲染？
5) React/D3 是否避免不必要重绘（key、memo、join）？
6) 工具提示是否提供了有意义的维度/度量信息？
7) 条件格式颜色是否符合无障碍与品牌规范？
8) 是否具备完整的 Jest/可视化/交互测试与 Host mock？
9) 包体积与依赖是否最小、无高危许可？
10) 是否通过验证与签名，满足 AppSource 合规？
11) update 分支是否幂等并处理空 dataView？

Source: d:\mycode\awesome-copilot\instructions\power-bi-custom-visuals-development.instructions.md | Generated: 2025-10-17
