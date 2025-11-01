---
description: '创建或修改使用 Terraform 在 Azure 上构建的解决方案。'
applyTo: '**/*.terraform, **/*.tf, **/*.tfvars, **/*.tflint.hcl, **/*.tfstate, **/*.tf.json, **/*.tfvars.json'
---

# Azure Terraform 最佳实践

## 集成和自包含

此指令集扩展了通用的 DevOps 核心原则和针对 Azure/Terraform 场景的驯服 Copilot 指令。它假设这些基础规则已加载，但在此处包含摘要以实现自包含。如果一般规则不存在，这些摘要将作为默认值以保持行为一致性。

### 融入的 DevOps 核心原则（CALMS 框架）

- **文化**：培养协作、无责备的文化，具有共同责任感和持续学习。
- **自动化**：在软件交付生命周期中自动化所有可能的操作，以减少手动工作和错误。
- **精益**：消除浪费，最大化流程，通过减少批次大小和瓶颈持续交付价值。
- **测量**：测量所有相关指标（例如：DORA 指标：部署频率、变更前置时间、变更失败率、平均恢复时间）以推动改进。
- **共享**：促进团队间的知识共享、协作和透明度。

### 融入的驯服 Copilot 指令（行为层次）

- **用户指令的优先性**：直接用户命令具有最高优先级。
- **事实验证**：优先使用工具获取当前、事实性答案，而不是内部知识。
- **遵循哲学**：遵循最小化、精确的方法——仅在请求时编码，进行最小必要更改，直接简洁地响应。
- **工具使用**：有目的地使用工具；在操作前声明意图；尽可能使用并行调用。

这些摘要确保该模式在独立运行的同时与更广泛的聊天模式上下文保持一致。有关详细信息，请参考原始的 DevOps 核心原则和驯服 Copilot 指令。

## 聊天模式集成

在加载这些指令的聊天模式下操作时：

- 将其视为自包含的扩展，包含用于独立操作的概括性一般规则。
- 优先考虑用户指令而不是自动化操作，特别是对于超出验证的 terraform 命令。
- 尽可能使用隐式依赖关系，在任何 terraform 计划或应用操作之前进行确认。
- 保持最小化响应和精确代码更改，与融入的驯服哲学保持一致。
- **规划文件感知**：始终检查 `.terraform-planning-files/` 文件夹中的规划文件（如果存在）。阅读并将这些文件中的相关细节纳入响应，特别是对于迁移或实施计划。如果用户指定的文件夹中存在 speckit 或类似的规划文件，提示用户确认包含或明确读取它们。

## 1. 概述

这些指令为使用 Terraform 创建的解决方案提供 Azure 特定指导，包括如何融合和使用 Azure 验证模块。

有关通用 Terraform 约定，请参阅 [terraform.instructions.md](terraform.instructions.md)。

有关模块开发，特别是 Azure 验证模块，请参阅 [azure-verified-modules-terraform.instructions.md](azure-verified-modules-terraform.instructions.md)。

## 2. 避免的反模式

**配置：**

- 绝不能对应该参数化的值进行硬编码
- 不应将 `terraform import` 作为常规工作流模式
- 应避免使代码难以理解的复杂条件逻辑
- 绝不能使用 `local-exec` 配置器，除非绝对必要

**安全性：**

- 绝不能将机密存储在 Terraform 文件或状态中
- 必须避免过于宽松的 IAM 角色或网络规则
- 绝不能为方便禁用安全功能
- 绝不能使用默认密码或密钥

**操作：**

- 绝不能将 Terraform 变更直接应用到生产环境而不进行测试
- 必须避免对 Terraform 管理的资源进行手动更改
- 绝不能忽略 Terraform 状态文件损坏或不一致
- 绝不能从本地计算机为生产环境运行 Terraform
- 只能将 Terraform 状态文件（`**/*.tfstate`）用于只读操作，所有更改必须通过 Terraform CLI 或 HCL 进行。
- 只能将 `**/.terraform/**` 的内容（获取的模块和提供程序）用于只读操作。

这些在融入的驯服 Copilot 指令基础上构建，用于安全、操作实践。

---

## 3. 清晰组织代码

使用逻辑文件分离构建 Terraform 配置：

- 使用 `main.tf` 用于资源
- 使用 `variables.tf` 用于输入
- 使用 `outputs.tf` 用于输出
- 使用 `terraform.tf` 用于提供程序配置
- 使用 `locals.tf` 抽象复杂表达式并提高可读性
- 遵循一致的命名约定和格式（`terraform fmt`）
- 如果 main.tf 或 variables.tf 文件变得过大，按资源类型或功能将它们拆分为多个文件（例如：`main.networking.tf`、`main.storage.tf` - 将等效变量移动到 `variables.networking.tf` 等）

对变量和模块名使用 `snake_casing`。

## 4. 使用 Azure 验证模块 (AVM)

任何重要资源如果有可用的 AVM 都应该使用。AVM 设计为与良好架构框架保持一致，由 Microsoft 支持和维护，有助于减少需要维护的代码量。关于如何发现这些的信息可在 [用于 Terraform 的 Azure 验证模块](azure-verified-modules-terraform.instructions.md) 中找到。

如果资源没有可用的 Azure 验证模块，建议创建一个"AVM 风格的"模块，以与现有工作保持一致，并为向上游社区做出贡献提供机会。

此指令的例外情况是用户被指导使用内部私有注册表，或者明确表示他们不希望使用 Azure 验证模块。

这与融入的 DevOps 自动化原则保持一致，通过利用预验证、社区维护的模块。

## 5. 变量和代码风格标准

在解决方案代码中遵循与 AVM 对齐的编码标准以保持一致性：

- **变量命名**：对所有变量名使用 snake_case（根据 TFNFR4 和 TFNFR16）。具有描述性并与命名约定保持一致。
- **变量定义**：所有变量必须有显式类型声明（根据 TFNFR18）和全面描述（根据 TFNFR17）。避免集合值的可空默认值（根据 TFNFR20），除非有特定需要。
- **敏感变量**：适当标记敏感变量，避免显式设置 `sensitive = false`（根据 TFNFR22）。正确处理敏感默认值（根据 TFNFR23）。
- **动态块**：在适当的地方对可选嵌套对象使用动态块（根据 TFNFR12），并利用 `coalesce` 或 `try` 函数进行默认值（根据 TFNFR13）。
- **代码组织**：考虑专门为本地值使用 `locals.tf`（根据 TFNFR31），并确保本地值的精确类型（根据 TFNFR33）。

## 6. 机密

最好的机密是不需要存储的机密。例如，使用托管标识而不是密码或密钥。

在支持时使用带有只写参数的 `ephemeral` 机密（Terraform v1.11+）以避免将机密存储在状态文件中。请查阅模块文档以了解可用性。

在需要机密的地方，除非指导使用不同的服务，否则存储在 Key Vault 中。

永远不要将机密写入本地文件系统或提交到 git。

适当标记敏感值，将它们与其他属性隔离，避免输出敏感数据，除非绝对必要。遵循 TFNFR19、TFNFR22 和 TFNFR23。

## 7. 输出

- **避免不必要的输出**，仅使用这些来暴露其他配置需要的信息。
- 对包含机密的输出使用 `sensitive = true`
- 为所有输出提供清晰的描述

```hcl
output "resource_group_name" {
  description = "创建的资源组名称"
  value       = azurerm_resource_group.example.name
}

output "virtual_network_id" {
  description = "虚拟网络 ID"
  value       = azurerm_virtual_network.example.id
}
```

## 8. 本地值使用

- 对计算值和复杂表达式使用本地值
- 通过提取重复表达式提高可读性
- 将相关值组合为结构化的本地值

```hcl
locals {
  common_tags = {
    Environment = var.environment
    Project     = var.project_name
    Owner       = var.owner
    CreatedBy   = "terraform"
  }

  resource_name_prefix = "${var.project_name}-${var.environment}"
  location_short       = substr(var.location, 0, 3)
}
```

## 9. 遵循推荐的 Terraform 实践

- **冗余 depends_on 检测**：搜索并删除在相同资源块中已隐式引用依赖资源的 `depends_on`。仅在明确需要时保留 `depends_on`。永不要依赖模块输出。

- **迭代**：对 0-1 资源使用 `count`，对多个资源使用 `for_each`。优先使用映射以获得稳定的资源地址。与 TFNFR7 保持一致。

- **数据源**：在根模块中可接受，但在可重用模块中避免。优先使用显式模块参数而不是数据源查找。

- **参数化**：使用带有显式 `type` 声明（TFNFR18）、全面描述（TFNFR17）和非空默认值（TFNFR20）的强类型变量。利用 AVM 暴露的变量。

- **版本控制**：以最新的稳定 Terraform 和 Azure 提供程序版本为目标。在代码中指定版本并保持更新（TFFR3）。

## 10. 文件夹结构

为 Terraform 配置使用一致的文件夹结构。

使用 tfvars 修改环境差异。通常，在为非生产环境进行成本优化的同时，保持环境相似。

反模式 - 每个环境的分支、每个环境的仓库、每个环境的文件夹 - 或类似的使环境之间难以测试根文件夹逻辑的布局。

注意可能影响此设计的工具，如 Terragrunt。

**建议的**结构是：

```text
my-azure-app/
├── infra/                          # Terraform 根模块（AZD 兼容）
│   ├── main.tf                     # 核心资源
│   ├── variables.tf                # 输入变量
│   ├── outputs.tf                  # 输出
│   ├── terraform.tf                # 提供程序配置
│   ├── locals.tf                   # 本地值
│   └── environments/               # 环境特定配置
│       ├── dev.tfvars              # 开发环境
│       ├── test.tfvars             # 测试环境
│       └── prod.tfvars             # 生产环境
├── .github/workflows/              # CI/CD 管道（如果使用 github）
├── .azdo/                          # CI/CD 管道（如果使用 Azure DevOps 则建议）
└── README.md                       # 文档
```

未经用户直接同意，切勿更改文件夹结构。

遵循 AVM 规范 TFNFR1、TFNFR2、TFNFR3 和 TFNFR4 以获得一致的文件命名和结构。

## Azure 特定最佳实践

### 资源命名和标记

- 遵循 [Azure 命名约定](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)
- 对多区域部署使用一致的区域命名和变量
- 实施一致的标记。

### 资源组策略

- 指定时使用现有资源组
- 仅在必要时创建新资源组并进行确认
- 使用表示目的和环境的描述性名称

### 网络考虑

- 在创建新网络资源之前验证现有 VNet/子网 ID（例如，此解决方案是否部署到现有的中心辐射型登陆区域）
- 适当使用 NSG 和 ASG
- 在需要时为 PaaS 服务实施专用端点，否则使用资源防火墙限制限制公共访问。在需要公共端点的地方注释例外。

### 安全性和合规性

- 使用托管标识而不是服务主体
- 实施带有适当 RBAC 的 Key Vault。
- 为审计跟踪启用诊断设置
- 遵循最小权限原则

## 成本管理

- 确认昂贵资源的预算批准
- 使用环境适当的规模（开发 vs 生产）
- 如果未指定，询问成本约束

## 状态管理

- 使用远程后端（Azure 存储）进行状态锁定
- 永远不要将状态文件提交到源代码控制
- 启用静态和传输中的加密

## 验证

- 对现有资源进行清单并提供删除未使用资源块的建议。
- 运行 `terraform validate` 检查语法
- 在运行 `terraform plan` 之前询问。Terraform plan 将需要订阅 ID，这应该从 ARM_SUBSCRIPTION_ID 环境变量获取，*而不是* 在提供程序块中编码。
- 首先在非生产环境中测试配置
- 确保幂等性（多次应用产生相同结果）

## 回退行为

如果一般规则未加载，默认为：最小化代码生成，对超出验证的任何 terraform 命令进行明确同意，并在所有建议中遵循 CALMS 原则。