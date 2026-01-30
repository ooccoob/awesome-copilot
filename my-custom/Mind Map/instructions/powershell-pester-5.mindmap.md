## What/When/Why/How
- What: PowerShell Pester v5 测试编写规范
- When: 为函数/模块新增或重构测试时
- Why: 稳定回归、可读报告与可维护用例
- How: Describe/Context/It 层级 + Should 断言 + Mock/标签/跳过

## Key Points
- 结构：*.Tests.ps1；仅在 Pester 块内写代码
- 导入：BeforeAll . $PSScriptRoot/Func.ps1
- 生命周期：BeforeAll/Each、AfterEach/All 作用域
- 断言：Be/Contain/HaveCount/Throw 等
- Mock：Mock/-ParameterFilter；Should -Invoke/InvokeVerifiable
- 数据：-ForEach/-TestCases 参数化；模板化名称
- 配置：New-PesterConfiguration；Run/Filter/Output/TestResult/Should

## Compact Map
- Blocks: Describe→Context→It
- Tools: Mock + Should 断言族
- Ops: TagFilter/Skip/Config

## Example Questions
1) 测试是否完全隔离、无共享状态？
2) 导入与依赖是否在 BeforeAll 处理？
3) Mock 的参数过滤与调用次数校验是否完整？
4) 异常路径是否用 Should -Throw 覆盖？
5) 是否使用 -ForEach 提升参数化覆盖度？
6) 结果输出是否为对象而非文本？
7) 配置是否输出 NUnitXml 报告以供 CI？
8) 快/慢/集成用例是否用标签可筛选？
9) Skip 是否有条件控制并记录原因？
10) Should.ErrorAction 是否设置以收集多失败？
11) 清理逻辑是否在 AfterEach/All 完成？

Source: d:\mycode\awesome-copilot\instructions\powershell-pester-5.instructions.md | Generated: 2025-10-17
