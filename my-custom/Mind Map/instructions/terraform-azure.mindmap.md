## What
- 在 Azure 上使用 Terraform 的实践：结构化代码、AVM 模块、安全/成本/状态/验证与 DevOps 行为

## When
- 设计/实现/审查 Azure 基础设施即代码（IaC）方案时

## Why
- 对齐微软 AVM 与 CALMS 原则，降低风险、提升一致性与可维护性

## How
- 组织
  - main/variables/outputs/terraform/locals 拆分；必要时按域拆文件；snake_case
- AVM
  - 优先使用 Azure Verified Modules；若无则按 AVM 风格实现；除非用户声明使用私有注册表或拒绝
- 变量/风格
  - 明确类型+描述；敏感变量标记；动态块与 coalesce/try；locals 精确定义
- 反模式
  - 禁止硬编码/默认密码、local-exec 滥用、生产直改、手工漂移、宽泛权限
- Secrets
  - Managed Identity 优先；Key Vault 存储；Terraform v1.11+ 支持 ephemeral secrets
- 输出
  - 仅必要输出；敏感输出 sensitive=true
- 本地值
  - locals 组合常用值与标签/命名
- 实践
  - 减少冗余 depends_on；count/for_each 选择；根模块可用 data，复用模块尽量参数化
  - 版本固定并跟进；后端使用 Azure 存储+加密+锁
- 结构建议
  - infra 根模块 + environments tfvars；避免按环境分支/仓库/文件夹
- Azure 特性
  - 命名与标签、资源组策略、网络（私有端点/NSG/ASG/防火墙）、最小权限
- 成本/验证
  - 预算确认；非生产降配；terraform validate；询问后再 plan；ARM_SUBSCRIPTION_ID 来自环境变量

## Key Points
- 计划文件与 speckit 如存在应先读取
- 任何 plan/apply 前需确认

## Compact Map
- 结构: main/vars/outputs/locals/provider
- AVM: 发现/复用/自研
- 安全: secret/MI/KV/最小权限
- 状态: 远端/加密/锁
- 验证: validate→(确认)→plan

## Example Questions
1) 本项目是否存在 .terraform-planning-files/ 需读取？
2) 该资源是否有 AVM 可复用？
3) 哪些变量需要 sensitive/类型/描述补全？
4) 哪些 depends_on 可移除？
5) 采用 count 还是 for_each 更稳？
6) 后端状态是否启用加密和锁？
7) 哪些输出可以裁剪或标记 sensitive？
8) 有哪处使用了 local-exec 可替代？
9) 私有端点/网络策略是否满足最小暴露？
10) 计划执行前需哪些用户确认？
11) ARM_SUBSCRIPTION_ID 如何注入？

Source: d:\mycode\awesome-copilot\instructions\terraform-azure.instructions.md | Generated: 2025-10-17
