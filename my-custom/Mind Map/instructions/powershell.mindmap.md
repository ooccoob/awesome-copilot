## What/When/Why/How
- What: PowerShell 脚本/函数（Cmdlet 风格）最佳实践
- When: 编写/评审脚本与模块时
- Why: 提升一致性、自动化友好与安全性
- How: Verb-Noun 命名 + 参数设计 + 管道/输出 + 错误处理

## Key Points
- 命名：Get-Verb 合法动词；名词单数；PascalCase
- 参数：标准名 Path/Name/Force；[switch]；ValidateSet
- 管道：ValueFromPipeline/ByPropertyName；Begin/Process/End
- 输出：对象优先 PSCustomObject；-PassThru 模式
- 错误：SupportsShouldProcess/ConfirmImpact；$PSCmdlet.WriteError
- 日志：Verbose/Warning/Error 区分；非交互设计
- 风格：避免别名与缩写；全 Cmdlet/参数名；风格一致

## Compact Map
- Structure: [CmdletBinding] + param + blocks
- Streams: Verbose/Warning/Error/Output
- Safety: ShouldProcess + Try/Catch + ErrorRecord

## Example Questions
1) 函数是否使用 Verb-Noun 且动词受 Get-Verb 认可？
2) 参数是否清晰、验证完善且类型合适？
3) 是否支持管道输入与逐项处理？
4) 是否返回对象而非格式化文本？
5) 是否实现 ShouldProcess/ConfirmImpact？
6) 错误处理是否构造标准 ErrorRecord？
7) 是否避免别名（?、%）并使用全名？
8) 是否可非交互执行（无 Read-Host）？
9) -PassThru 是否遵循动作 cmdlet 约定？
10) 帮助注释是否完整（Synopsis/Example/Outputs）？
11) 变量与作用域是否合理且无泄漏？

Source: d:\mycode\awesome-copilot\instructions\powershell.instructions.md | Generated: 2025-10-17
