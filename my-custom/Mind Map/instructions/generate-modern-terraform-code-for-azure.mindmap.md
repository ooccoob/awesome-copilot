## What/When/Why/How
- What: 现代化 Azure Terraform 编写规范（版本/模块/变量输出/后端/验证/CI）
- When: 新建 IaC、重构 TF、引入模块化/远端状态与 CI 校验时
- Why: 可复用/可维护/可协作；最小依赖且幂等；安全存储状态
- How: 固定 provider/TF 版本、分 main/variables/outputs、模块化封装、远端 backend、validate/plan、文档化

## Key Points
- 版本: 锁定 Terraform/azurerm/azapi；优先 azurerm，azapi 补缺
- 结构: main/variables/outputs 分离；统一命名与 fmt
- 模块: 可复用资源组装；输入/输出清晰；避免复制粘贴
- 变量/输出: 类型/描述/默认值/敏感标记
- 幂等: 避免非幂等脚本；合理 lifecycle/条件
- 状态: 远端后端（Azure Storage + 锁）；禁提交本地 state
- 依赖: 控制外部 provider/模块；新增需说明与审批
- 文档: README + terraform-docs；变更后更新图与说明
- 校验: validate/plan、本地钩子与 CI

## Compact Map
版本→结构→模块→变量/输出→幂等→状态→依赖→文档→校验

## Example Questions (10+)
1) 初始化 azurerm + 远端状态存储的最小示例
2) 将现有资源提炼为模块并暴露关键 outputs
3) 设计 variables.tf（类型/描述/默认/敏感）模板
4) azapi 与 azurerm 混用的场景与注释规范
5) 在 PR 中集成 terraform fmt/validate/plan
6) lifecycle 块用于避免资源抖动的示例
7) modules 目录约定与版本化策略
8) 使用 terraform-docs 生成 README 的方式
9) 为关键变量提供默认值与输入校验
10) 大规模多工作区与后端命名规范

Source: d:\mycode\awesome-copilot\instructions\generate-modern-terraform-code-for-azure.instructions.md | Generated: 2025-10-17T00:00:00Z
