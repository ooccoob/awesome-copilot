## What
- 目标：基于代码现状更新 OO 组件技术文档，遵循 C4/Arc42/IEEE1016/敏捷文档原则。
- 范围：概览/架构/接口/实现/示例/质量属性/参考等，并刷新 mermaid 图与字段表。

## When
- 组件实现或依赖发生显著变化；新增接口/配置/行为或弃用能力。

## Why
- 让维护者快速理解当前实现/接口/依赖与约束，提升可维护性与一致性。

## How
- 读取 `${file}` front matter 获取 component_path（或从正文推断）。
- 分析源码：结构/继承/模式/公共 API/异常/集成流/性能/安全等。
- 与现有文档对比，更新差异；刷新示例与依赖版本；标注废弃与破坏性变化。
- 按模板更新各章节；更新 mermaid 组件/类/时序图；更新 last_updated。

## Key Points
- 语言优化：针对 C#/Java/TS/Python 的惯例与特性补充细节。
- 错误处理：缺文件/路径/源码访问不足时给出限制与建议。
- 输出保持原结构与格式；必要时新增小节但不破坏层次。

## Compact Map
- Read doc → Locate component → Analyze code → Update sections → Refresh diagrams → Validate

## Example Questions (10+)
- 该组件当前使用了哪些设计模式，应如何在文档中体现？
- 公共 API 的参数/返回/异常变化点有哪些？
- 组件依赖与外部系统交互如何建模并图示？
- 性能瓶颈与容量预估如何记录？
- 安全要点（鉴权/数据保护/审计）如何补充？
- .NET/Java/TS/Python 语言特定注意点分别有哪些？
- 如何标注弃用 API 与迁移路径？
- 示例代码如何与当前实现保持同步且可编译？
- mermaid 图如何与当前结构一致并最小化噪音？
- 如何维护版本历史与变更说明？
- 文档中哪些内容可自动生成，哪些需要人工补充？

---
Source: d:\mycode\awesome-copilot\prompts\update-oo-component-documentation.prompt.md
Generated: 2025-10-17T00:00:00Z
