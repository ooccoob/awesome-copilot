## What/When/Why/How
- What: Copilot Prompt 文件编写规范（前言、模式、工具、模型、结构）
- When: 为团队创建可复用 Prompt 时
- Why: 让行为可预测、权限最小、跨仓可移植
- How: 前置元数据 + 明确输入/工具/输出/验证的体例

## Key Points
- Frontmatter：description/mode/tools/model；单引号；逐行
- 命名：kebab-case；.prompt.md；.github/prompts/ 目录
- 结构：Mission→Scope→Inputs→Workflow→Output→QA
- 输入：${input:name[:placeholder]}；缺失时的处理策略
- 工具：最小集合；顺序敏感时列顺序；副作用警示/确认
- 风格：祈使句，短句，避免文化隐喻；可本地化
- 输出：格式与落盘路径；成功/失败条件；验收步骤
- 维护：版本化、定期审查、引用规范文档

## Compact Map
- Metadata: mode/tools/model
- Body: directive→steps→checks
- Safety: least-privilege + guardrails
- QA: run in VS Code + checklist

## Example Questions
1) 是否声明了正确的 mode（ask/edit/agent）？
2) tools 是否最小且顺序合理？
3) 输入变量是否含占位/默认与缺失策略？
4) 工作流是否覆盖准备/执行/后置？
5) 输出位置/格式/模板是否明确？
6) 何时判定失败并要求重试/停止？
7) 是否含安全提示与高危操作确认？
8) 是否链接相关 prompts/说明文档？
9) QA 清单是否可操作（命令/检查点）？
10) 是否通过 Chat: Run Prompt 在示例场景验证？
11) 是否便于跨仓移植并保留元数据？

Source: d:\mycode\awesome-copilot\instructions\prompt.instructions.md | Generated: 2025-10-17
