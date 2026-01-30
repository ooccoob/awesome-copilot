## What
- 从两个项目状态（分支/提交/标签）对比中提炼“迁移/演进规则”，生成供 Copilot 自动套用的迁移指令与 `.github/copilot-migration-instructions.md`。

## When
- 框架版本升级、架构重构、技术栈迁移、依赖升级、模式变更时，需保持风格一致与自动化迁移。

## Why
- 将一次性迁移经验固化为可复用规则，降低后续变更成本与错误率，维持一致性。

## How
- 比较分析：结构/依赖/配置/API 变化；抽取重复转换模式与前后映射。
- 规则产出：按“必做/需验证”分层，定义触发、动作、例外；建立 API 对照表；标注新/废弃模式与替代。
- 示例驱动：为每个模式提供 before/after 与步骤说明。
- 校验与监控：自动检查点、测试集、性能与兼容性、度量与反馈迭代。

## Key points (CN)
- 变量化 MIGRATION_TYPE/CHANGE_FOCUS/ANALYSIS_SCOPE 驱动生成
- 提炼可重复转换；明确触发/动作/校验
- API 对照与废弃模式替代
- 指标监控与持续优化

## Key points (EN)
- Diff-driven transformation rules; mandatory vs validated
- API correspondence; deprecated → alternative
- Example-first guidance; metrics and feedback loop

## Example questions
- “对比 develop…release/1.2 生成 Spring 升级迁移规则？”
- “提炼 Class → Hooks 的自动转换指令？”
- “REST → GraphQL 的 API 映射表与示例？”

## 思维导图（要点）
- 比较分析：结构/依赖/API/配置
- 规则生成：必做/需验证/例外
- 示例：before/after/触发→动作
- 校验与安全：断言/测试/回滚
- 监控：比例/错误率/耗时→改进

—
- Source: d:\mycode\awesome-copilot\prompts\generate-custom-instructions-from-codebase.prompt.md
- Generated: 2025-10-17
