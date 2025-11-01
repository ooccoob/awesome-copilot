## What/When/Why/How
- What: Power Apps Canvas Apps YAML 与 Power Fx 结构要点速览
- When: 读取/审查 .pa.yaml、组件与屏幕建模、源码管控与校验
- Why: 保持结构正确、可读可维护、可追溯，避免 schema 偏差与合并冲突
- How: 按 schema v3.0 组织 App/Screens/ComponentDefinitions/DataSources/EditorState，公式一律以 = 开头

## Key Points
- 根结构：App/Properties、Screens、ComponentDefinitions、DataSources、EditorState
- 控件定义：Control/Properties/[Children]；容器相对定位；Children 顺序即 z-index
- 版本：Control: Type@semver；默认最新
- 公式：一律以 = Power Fx；行为属性可用分号串联；null 表示无值
- 数据源：Table/Actions；连接器参数按需配置
- 组件：自定义属性（Input/Output/Event/Action/Function）与类型
- 命名：控件/组件 PascalCase；屏幕具名；属性精确匹配 schema
- 校验：必需字段、命名模式、缩进与结构；常见错误集中在拼写与未加 =

## Compact Map
- App.Properties: StartScreen, BackEnabled, ...
- Screen: Properties + Children[Control]
- Control: Control + Properties + (Children)
- ComponentDefinitions: DefinitionType + CustomProperties + Children
- DataSources: Type(Table|Actions) + Parameters
- EditorState: ScreensOrder/ComponentDefinitionsOrder

## Example Questions
1) 该控件缺失 Control/Properties/Children 等必需节点吗？
2) 属性是否全部使用 = 前缀的 Power Fx？
3) Children 顺序是否符合期望的 z-index 叠放？
4) 自定义组件的属性种类是否正确（Input/Output/...）？
5) 是否存在未 delegable 的公式会导致大数据集拉取？
6) CodeComponent/PCF 的命名是否满足模式要求？
7) 数据源类型与参数是否与连接器一致？
8) 是否把仅用于编辑器的元数据提交进了源码库？
9) 版本标注（Button@2.x）是否必要并与运行时兼容？
10) 合并冲突处缩进/命名是否破坏 schema？
11) 是否通过 CLI/Studio 校验并在 PR 中做 schema 校验？

Source: d:\mycode\awesome-copilot\instructions\power-apps-canvas-yaml.instructions.md | Generated: 2025-10-17
