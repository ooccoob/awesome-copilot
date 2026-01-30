## What / When / Why / How

- What: Azure Terraform 实施专家（生成/审查 *.tf）
- When: 需要落地 IaC 并对齐 AVM/最佳实践
- Why: 保证正确性、可维护性与安全一致性
- How: 预检路径→写/改 *.tf→validate/fmt→可选 plan（需确认）→最终检查

## Key Points

- 显式同意：禁止执行破坏性命令；plan/apply 前必须征询
- 预检：outputBasePath=infra/；必要时创建
- 校验：terraform init/validate/fmt；建议 tflint/terraform-docs
- depends_on：优先隐式依赖，清理冗余
- 规划文件：读取 .terraform-planning-files/* 并对齐 INFRA 目标
- 标准：INFRA 计划>terraform-*.instructions>AVM 最佳实践
- 终检：无硬编码密钥/命名规范/标签/版本/依赖正确

## Compact Map

- 发现→生成/重构→校验→审查→终检→（询问）plan

## Example Questions (10+)

- 输出目录与模块结构如何组织？
- 现有 *.tf 中冗余 depends_on 在哪里？
- 资源命名/标签是否符合约定？
- Provider/模块版本与计划一致吗？
- Key Vault/MI/存储等引用是否正确？
- tflint/validate/fmt 的结果如何修复？
- 计划文件的目标与差异点？
- 需要哪些变量/locals/outputs？
- 是否存在未使用代码片段？
- 何时需要运行 plan 并如何参数化？

---
Source: d:\mycode\awesome-copilot\chatmodes\terraform-azure-implement.chatmode.md
Generated: {{timestamp}}
