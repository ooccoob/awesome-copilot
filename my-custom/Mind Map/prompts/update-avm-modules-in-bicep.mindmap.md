## What
- 目标：将 Bicep 文件中的 AVM 模块版本更新至最新，并校验/汇总更新结果。
- 输出：仅表格 + 简述总结；遵循语义化版本比较与 MCR tags API。

## When
- 基础设施模板需要常规升级或安全修复时。

## Why
- 跟进官方模块修复/特性；保持一致性与合规性。

## How
- 扫描 `${file}`：匹配 avm/res/{service}/{resource} 与当前版本。
- 查询 MCR tags：https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list
- 语义化排序选取最新；如疑似破坏性变更 → fetch 仓库文档审阅。
- 应用更新并使用 bicep lint/build 进行校验；仅对非破坏性项自动推进。
- 输出：模块|当前|最新|状态|动作|文档 链接 + 总结。

## Key Points
- 工具固定：search/searchResults/fetch/editFiles/runCommands/todos。
- 暂停策略：参数不兼容/安全策略变化/行为改变需人工确认。
- 维持文件有效性与风格，最小侵入。

## Compact Map
- Scan → Check → Compare → Review → Update → Validate → Output

## Example Questions (10+)
- 如何在多模块文件中只更新存在新版本的模块？
- 版本标签非规范时如何做健壮排序？
- 碰到参数破坏性变更如何生成差异清单？
- 可否只预览表格结果而不落地修改？
- bicep lint/build 失败如何回滚并给出指引？
- 私有镜像或断网环境如何处理 tags 查询？
- 兼容性审阅链接如何自动拼接？
- 是否支持批量处理文件夹内多个 bicep？
- 对“已是最新”如何标注与计数？
- 如何在 CI 里失败门禁并附上表格注释？
- 对版本 pin 策略如何保留注释与锁定？

---
Source: d:\mycode\awesome-copilot\prompts\update-avm-modules-in-bicep.prompt.md
Generated: 2025-10-17T00:00:00Z
