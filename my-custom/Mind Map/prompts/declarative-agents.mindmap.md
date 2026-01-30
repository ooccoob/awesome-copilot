## 文档综述（What/When/Why/How）

- What：Microsoft 365 Copilot 声明式代理开发套件（v1.5），含三类工作流、TypeSpec 与 Agents Toolkit 集成

- When：新建或优化企业级 M365 声明式代理、做合规校验与性能优化时

- Why：标准化清单与流程，减少试错；提供 TypeSpec/JSON 双形态与工具链集成

- How：三工作流（基础/高级/校验）→能⼒选择（≤5）→清单约束（长度/数组）→Playground 测试→监控与最佳实践

## 示例提问（Examples）

- “按工作流2为多租户合规与本地化设计代理，输出 TypeSpec + JSON”

- “校验现有 manifest 是否符合 v1.5 限制并优化对话开场”

## 结构化要点（CN/EN）

- 能力/Capabilities：≤5（WebSearch/Graph/OneDrive…）

- 约束/Limits：name(100)/desc(1000)/instr(8000)，starters≤4

- TypeSpec/JSON：互转 & 校验 | Compile to JSON

- 工具/Toolkit：VS Code 扩展/Playground/生命周期

## 中文思维导图

- 工作流
  - 基础/高级/校验
- 能力配置
  - 组合与交互
- 清单约束
  - 长度/数量
- 集成
  - TypeSpec/Toolkit
- 部署与监控

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\declarative-agents.prompt.md

- 生成时间：2025-10-17
