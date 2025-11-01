## Microsoft 365 Declarative Agents（v1.5）要点

- What: 基于 v1.5 JSON 架构与 Agents Toolkit 的声明式代理开发（能力/清单/TypeSpec/测试/部署/合规）。
- When: 定义/验证代理清单、选择能力、用 TypeSpec 建模并编译、在 Agents Playground 测试与发布时。
- Why: 以声明式方式快速构建企业级 Copilot 扩展，统一校验与工具链，确保安全合规与可维护。
- How: 按 v1.5 架构与字符上限编写 manifest；TypeSpec 定义模型并编译 JSON；渐进式添加能力；本地试玩与版本管理。

### 架构与约束
- 必填与上限: name≤100、description≤1000、instructions≤8000、capabilities 1~5、starters≤4。
- 能力集: WebSearch/OneDriveAndSharePoint/GraphConnectors/MicrosoftGraph/TeamsAndOutlook/PowerPlatform/CopilotForMicrosoft365/WordAndExcel/BusinessDataProcessing/EnterpriseApplications/CustomConnectors。
- TypeSpec: 使用 @maxLength/@minLength/@maxItems 等注解生成合规 JSON。

### 工具链与测试
- VS Code 扩展: Microsoft 365 Agents Toolkit。
- 编译: `tsp compile` 生成 JSON。
- 本地测试: agents-playground 加载 manifest，校验能力/对话开场/错误与性能。

### 最佳实践
- 校验: 以 v1.5 schema 做 JSON 校验；封装字符长度检查函数。
- 能力策略: 从 1~2 个核心能力开始，迭代加法；结合安全/合规评估。
- 版本与环境: metadata 标注版本/构建/环境；开发/预发/生产分层与日志等级策略。
- 监控: 记录能力响应时延、错误率、starter 参与度；结构化日志字段统一。
- 安全: 输入/输出校验；限流与滥用防护；合规（GDPR/CCPA）。

### 高级能力
- 行为覆盖: 响应语气、长度、引文约束。
- 本地化: name/description 多语言 map。

### 示例问题
1) 如何在 TypeSpec 中声明并限制 capabilities 的枚举与数量？
2) 指令超 8000 字符的裁剪与校验策略？
3) 多环境的 manifest 变量注入方式？
4) 何时应启用 WebSearch 与 Graph 同时存在？
5) Agents Playground 如何编排性能与错误场景？
6) 如何设计监控日志 schema 以便后续分析？
7) 企业合规审计需要额外记录哪些字段？
8) 能力组合冲突的排查路径？
9) 指令工程（prompt）变更的版本管理策略？
10) 与自定义连接器的鉴权与配额控制要点？

Source: d:\mycode\awesome-copilot\instructions\declarative-agents-microsoft365.instructions.md | Generated: 2025-10-17T00:00:00Z
