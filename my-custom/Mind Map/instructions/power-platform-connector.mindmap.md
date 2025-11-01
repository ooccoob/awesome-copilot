## What/When/Why/How
- What: Power Platform 自定义连接器 JSON Schema/Swagger/设置规范
- When: 使用 paconn 设计/校验/发布连接器时
- Why: 通过扩展校验与 IntelliSense 降低错误率
- How: 严格 Swagger 2.0 + x-ms-* 扩展 + Properties/Settings 协同

## Key Points
- 文件：apiDefinition.swagger.json / apiProperties.json / settings.json
- 扩展：x-ms-summary/visibility/pageable/trigger/... 参数/模式扩展
- 安全：至多两种 securityDefinitions；None 不可与其他并存
- 参数：描述/必填/format（含 Power 平台扩展）；动态值/树/模式
- 属性：连接参数/策略模板（routerequesttoendpoint 等）/品牌元数据
- 设置：环境 GUID、URL、版本、路径映射
- 校验：必填字段、模式/格式、路径/主机/URL 规则
- 常见问题：$ref 位置、触发配置、分页/文件选择器、枚举值

## Compact Map
- Swagger: paths/definitions + x-ms-*
- Properties: auth/brand/policy
- Settings: env/paths/urls
- Tools: paconn validate / VS Code 校验

## Example Questions
1) swagger/info/paths 是否齐全且合规？
2) x-ms-* 扩展是否用于触发/分页/动态列表？
3) 安全定义是否≤2 且类型单一？
4) 参数是否有 x-ms-summary、描述与格式？
5) 路径是否以 / 开头，host 格式是否合法？
6) 枚举/可见性/触发类型是否在允许集合内？
7) apiProperties 是否包含 iconBrandColor 与品牌元？
8) policy 模板是否正确配置分页/路由等？
9) settings 的环境 GUID/URL/版本是否匹配目标？
10) $ref 是否仅指向 definitions/parameters/responses？
11) 是否通过 paconn/门户双重验证？

Source: d:\mycode\awesome-copilot\instructions\power-platform-connector.instructions.md | Generated: 2025-10-17
