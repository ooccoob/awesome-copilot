## What / When / Why / How

- What: Azure Verified Modules（AVM）Bicep 实践模式
- When: 需要用 Bicep 以模块化、可复用、最佳实践方式交付资源
- Why: 通过官方验证模块降低配置错误、提升一致性与可维护性
- How: 选择 AVM 模块→版本固定→示例起步→参数审阅→lint/validate→部署

## Key Points

- 索引/仓库：AVM index 与 GitHub 源
- 引用：br/public:avm/res/{service}/{resource}:{version}
- 版本：MCR tags 查询并固定版本
- 规范：命名（res/ptn/utl），参数/输出审阅
- 校验：bicep lint + schema 校验 + 最佳实践检查

## Compact Map

- 发现模块→阅读示例
- 固定版本→替换参数
- 本地验证：restore/build/format/lint
- 部署前审查：参数、输出、诊断、策略
- 文档化：README/变更记录/回滚

## Example Questions (10+)

- 对应资源是否已有 AVM 模块？索引/源码链接是？
- 版本固定到哪个 tag？如何查询可用版本？
- 该模块的必填/可选参数与默认值有哪些坑？
- 需开启哪些诊断/日志与加固设置？
- 多环境参数化如何组织（param files/vars）？
- 组合多个 AVM 模块的依赖与输出对接？
- 构建校验流水线如何配置（lint/build/validate）？
- 回滚策略与幂等性如何保障？
- 命名与标记是否符合企业规范？
- 部署配额/限制与区域差异有哪些？
- 如何在 PR 中运行 bicep lint 以阻断不合规？

---
Source: d:\mycode\awesome-copilot\chatmodes\azure-verified-modules-bicep.chatmode.md
Generated: {{timestamp}}
