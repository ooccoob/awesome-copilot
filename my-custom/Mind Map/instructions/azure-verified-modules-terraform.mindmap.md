## What / When / Why / How
- What: Azure Verified Modules (AVM) 的 Terraform 使用/开发规范与强制校验流程。
- When: 选型/引用 AVM 模块、提交 PR、在 CI 本地前置检查时。
- Why: 快速复用经验证模块，确保一致性与合规，避免 PR 校验失败。
- How: 到 Registry/AVM 索引检索模块；按命名/版本固定引用；启用遥测；提交前必须运行本地 ./avm 脚本与 tf 工具校验。

## Key points
- 强制本地检查（必须执行）：
  - ./avm pre-commit
  - ./avm tflint
  - ./avm pr-check
- 模块来源与命名：
  - 资源模块 Azure/avm-res-{service}-{resource}/azurerm
  - 模式模块 Azure/avm-ptn-{pattern}/azurerm
  - 工具模块 Azure/avm-utl-{utility}/azurerm
- 版本：使用 ~> 约束；生产可锁定具体版本；升级前读变更日志。
- 示例起步：复制官方 example，source 指向 Registry 地址并添加 version 与 enable_telemetry=true。
- 质量：terraform fmt/validate；有意义变量与标签；文档与示例覆盖。
- 发现：AVM 索引/Registry 查询；GitHub 仓库查看实现。

## Compact map
- 发现: 索引/Registry
- 选择: 模块命名/类型
- 引用: source+version+telemetry
- 校验: fmt/validate/avm 脚本
- 提交: 文档+示例+通过

## Example questions (10+)
- 如何为 storage account 选择正确的 AVM 资源模块与版本？
- ~> 与固定版本的升级策略如何制定？
- ./avm pr-check 失败常见原因与定位方法？
- 如何将 AVM 模块组合成企业级 Pattern 模块？
- 何时需要 avm-utl-* 工具模块（如 regions）？
- enable_telemetry 的数据用途与隐私注意？
- tfvars 与模块输入的组织与命名建议？
- TFLint 在 AVM 项目中的规则定制？
- 多模块依赖的资源创建顺序与显式 depends_on？
- 在 CI 中如何强制执行本地三步检查？

—
Source: d:\mycode\awesome-copilot\instructions\azure-verified-modules-terraform.instructions.md | Generated: {{timestamp}}
