## What / When / Why / How

- What: Azure Verified Modules（AVM）Terraform 实践模式
- When: 以 Terraform 交付 Azure 资源并遵循 AVM 标准
- Why: 使用官方验证模块减少踩坑，保证一致与可操作性
- How: 选择 AVM 模块→替换 source/加 version→enable_telemetry→示例起步→fmt/validate

## Key Points

- 发现：Terraform Registry 搜索 avm + 资源（Partner）
- 源：Azure/avm-res-{service}-{resource}/azurerm
- 版本：registry versions API 查询并固定
- 最佳实践：pin provider/module、启用 telemetry、tflint/自测
- PR 前置本地测试：./avm pre-commit / tflint / pr-check

## Compact Map

- 选模块/读示例
- 替换 source/加 version
- 设置 inputs 与 enable_telemetry
- 本地 fmt/validate/tflint & pre-commit
- PR 前运行 pr-check 并修复

## Example Questions (10+)

- 该资源的 AVM 模块地址与最新稳定版本？
- 我们需要哪些输入参数与输出对接到其他模块？
- provider 与模块版本如何 pin 定？
- 本地 pre-commit/tflint/pr-check 如何集成到 CI？
- 多租户/多环境如何组织 variables 与 workspaces？
- 针对配额/速率限制的部署节奏如何控制？
- 如何启用并上报 telemetry 以符合规范？
- 失败回滚策略与幂等性保证？
- 资源命名/标签是否符合企业策略？
- 需要哪些合规/安全设置默认开启？
- 如何写最小可复用示例供团队复用？

---
Source: d:\mycode\awesome-copilot\chatmodes\azure-verified-modules-terraform.chatmode.md
Generated: {{timestamp}}
