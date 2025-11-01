## What
- 目标：自动识别技术栈与实现模式，输出含版本/许可证/用法/规范/图示的蓝图（多格式）。
- 配置：PROJECT_TYPE/DEPTH_LEVEL/是否包含版本/许可证/图/用法/规范；输出格式与分类方式可选。

## When
- 新接手/重构大型代码库，需要统一生成规范与模板时。
- 需要为代码生成/一致性治理提供“事实蓝图”时。

## Why
- 形成可复用的技术画像，指导后续生成、评审与培训。
- 降低异构栈沟通成本，暴露升级路径与约束。

## How
- 扫描：项目/配置/依赖/脚本/CI。
- 分析：.NET/Java/JS/React/Python 分栈输出实践与配置。
- 规范：命名/组织/错误/日志/鉴权/校验/测试 等统一约定。
- 示例：API/数据访问/服务层/UI 代表代码。
- 地图：框架用法/集成点/工具链/基础设施/数据流。
- 决策：技术选型背景/替换计划/约束与兼容性。

## Key Points
- 输出 Implementation-Ready 时附模板/清单/检查表。
- 图示：栈图/依赖流/组件关系/数据流（可选）。
- 分类：按技术类型/分层/用途组织。

## Compact Map
- Detect → Analyze per stack → Conventions → Examples → Map → Decisions → Blueprint 输出

## Example Questions (10+)
- 如何在本仓中识别“真实使用”的框架而非仅依赖声明？
- 能输出 .NET 与 Java 的 DI/配置/日志差异与范式对照吗？
- 前端 React 状态管理与路由的实际用法能否抽取示例？
- 我们要实施“统一异常/返回体”，蓝图如何给出模板？
- 能列出升级高风险依赖与建议版本路径吗？
- 生成 Implementation-Ready 时，API/仓储/服务模板如何组织？
- 如何将蓝图结果用于 PR 审查自动校验？
- 是否可导出 JSON 供其它工具消费？
- 图示如何在 CI 中同步生成并校验？
- 多仓（前后端分离）如何合并成一份总蓝图？
- 蓝图与当前团队规范冲突时如何标注与裁剪？

---
Source: d:\mycode\awesome-copilot\prompts\technology-stack-blueprint-generator.prompt.md
Generated: 2025-10-17T00:00:00Z
