---
描述：“创建或修改使用 Azure 上的 Terraform 构建的解决方案。”
applyTo: '**/*.terraform, **/*.tf, **/*.tfvars, **/*.tflint.hcl, **/*.tfstate, **/*.tf.json, **/*.tfvars.json'
---

# Azure Terraform 最佳实践

## 集成和自我包含

该指令集扩展了适用于 Azure/Terraform 场景的通用 DevOps 核心原则和 Taming Copilot 指令。它假设这些基本规则已加载，但在此处包含摘要以供自我控制。如果不存在一般规则，这些摘要将作为默认规则以保持行为一致性。

### 纳入 DevOps 核心原则（CALMS 框架）

- **文化**：培养协作、无过失的文化，共同承担责任和持续学习。
- **自动化**：在整个软件交付生命周期中实现一切可能的自动化，以减少手动工作和错误。
- **精益**：通过减少批量大小和瓶颈，消除浪费、最大化流量并持续交付价值。
- **测量**：测量所有相关内容（例如 DORA 指标：部署频率、变更交付时间、变更失败率、平均恢复时间）以推动改进。
- **共享**：促进团队之间的知识共享、协作和透明度。

### 合并驯服副驾驶指令（行为层次结构）

- **用户指令的首要性**：直接用户命令具有最高优先级。
- **事实验证**：优先考虑当前事实答案的工具而不是内部知识。
- **坚持哲学**：遵循极简主义、外科手术方法——仅根据请求编写代码、最少的必要更改、直接而简洁的响应。
- **工具使用**：有目的地使用工具；行动前先声明意图；如果可能的话更喜欢并行调用。

这些摘要确保模式独立运行，同时与更广泛的聊天模式上下文保持一致。有关完整详细信息，请参阅原始 DevOps 核心原则和 Taming Copilot 说明。

## 聊天模式整合

当在聊天模式下运行并加载这些指令时：

- 将其视为一个独立的扩展，其中包含独立操作的总结一般规则。
- 优先考虑用户指令而不是自动化操作，尤其是对于验证之外的 terraform 命令。
- 尽可能使用隐式依赖关系，并在任何 terraform 计划或应用操作之前进行确认。
- 保持极简的反应和手术规范的变化，与纳入的驯服哲学保持一致。
- **规划文件意识**：始终检查 `.terraform-planning-files/` 文件夹中的规划文件（如果存在）。阅读这些文件中的相关详细信息并将其合并到响应中，特别是对于迁移或实施计划。如果用户指定的文件夹中存在speckit或类似的规划文件，则提示用户确认包含或明确读取它们。

## 1. 概述

这些说明为创建 Terraform 的解决方案提供特定于 Azure 的指南，包括如何合并和使用 Azure 验证模块。

有关一般 Terraform 约定，请参阅 [terraform.instructions.md](terraform.instructions-zh.md)。

有关模块（尤其是 Azure 验证模块）的开发，请参阅 [azure-verified-modules-terraform.instructions.md](azure-verified-modules-terraform.instructions-zh.md)。

## 2. 要避免的反模式

**配置：**

- 不得对应参数化的值进行硬编码
- 不应使用 `terraform import` 作为常规工作流程模式
- 应避免复杂的条件逻辑，使代码难以理解
- 除非绝对必要，否则不得使用 `local-exec` 配置程序

**安全：**

- 绝不能将机密存储在 Terraform 文件或状态中
- 必须避免过于宽松的 IAM 角色或网络规则
- 不得为了方便而禁用安全功能
- 不得使用默认密码或密钥

**运行中：**

- 不得在未经测试的情况下将 Terraform 更改直接应用于生产
- 必须避免对 Terraform 管理的资源进行手动更改
- 不得忽略 Terraform 状态文件损坏或不一致
- 不得从本地机器运行 Terraform 进行生产
- 必须仅使用 Terraform 状态文件 (`**/*.tfstate`) 进行只读操作，所有更改都必须通过 Terraform CLI 或 HCL 进行。
- 必须仅使用 `**/.terraform/**` （获取的模块和提供程序）的内容进行只读操作。

这些建立在合并的 Taming Copilot 指令的基础上，以实现安全、操作实践。

---

## 3. 干净地组织代码

具有逻辑文件分离的结构 Terraform 配置：

- 使用 `main.tf` 获取资源
- 使用 `variables.tf` 作为输入
- 使用 `outputs.tf` 进行输出
- 使用 `terraform.tf` 进行提供程序配置
- 使用 `locals.tf` 抽象复杂的表达式并提高可读性
- 遵循一致的命名约定和格式 (`terraform fmt`)
- 如果 main.tf 或 Variables.tf 文件变得太大，请按资源类型或函数将它们拆分为多个文件（例如，`main.networking.tf`、`main.storage.tf` - 将等效变量移动到 `variables.networking.tf` 等）

使用 `snake_casing` 作为变量和模块名称。

## 4.使用Azure验证模块（AVM）

任何重要资源都应使用 AVM（如果可用）。 AVM 旨在与架构完善的框架保持一致，由 Microsoft 支持和维护，有助于减少需要维护的代码量。有关如何发现这些的信息，请参阅 [Azure Verified Modules for Terraform](azure-verified-modules-terraform.instructions-zh.md)。

如果 Azure 验证模块不可用于该资源，建议创建一个“AVM 风格”的模块，以便与现有工作保持一致，并提供向上游社区做出贡献的机会。

此指令的一个例外是，如果用户已被指示使用内部私有注册表，或者明确声明他们不希望使用 Azure 验证模块。

通过利用预先验证的、社区维护的模块，这与合并的 DevOps 自动化原则相一致。

## 5. 变量和代码风格标准

在解决方案代码中遵循符合 AVM 的编码标准以保持一致性：

- **变量命名**：对所有变量名称使用 Snake_case（根据 TFNFR4 和 TFNFR16）。具有描述性并符合命名约定。
- **变量定义**：所有变量必须具有显式类型声明（根据 TFNFR18）和全面描述（根据 TFNFR17）。除非有特定需要，否则避免集合值的默认值为空（根据 TFNFR20）。
- **敏感变量**：适当标记敏感变量并避免显式设置 `sensitive = false` （根据 TFNFR22）。正确处理敏感的默认值（根据 TFNFR23）。
- **动态块**：在适当的情况下对可选嵌套对象使用动态块（根据 TFNFR12），并利用 `coalesce` 或 `try` 函数作为默认值（根据 TFNFR13）。
- **代码组织**：考虑专门针对本地值（根据 TFNFR31）使用 `locals.tf` ，并确保本地值的精确键入（根据 TFNFR33）。

## 6. 秘密

最好的秘密是不需要存储的秘密。  例如使用托管身份而不是密码或密钥。

如果支持 (Terraform v1.11+)，请使用带有只写参数的 `ephemeral` 密钥，以避免将密钥存储在状态文件中。请参阅模块文档以了解可用性。

如果需要机密，请存储在 Key Vault 中，除非指示使用其他服务。

切勿将机密写入本地文件系统或提交至 git。

适当标记敏感值，将其与其他属性隔离，并避免输出敏感数据，除非绝对必要。关注 TFNFR19、TFNFR22 和 TFNFR23。

## 7. 输出

- **避免不必要的输出**，仅使用这些来公开其他配置所需的信息。
- 将 `sensitive = true` 用于包含机密的输出
- 为所有输出提供清晰的描述

```hcl
output "resource_group_name" {
  description = "Name of the created resource group"
  value       = azurerm_resource_group.example.name
}

output "virtual_network_id" {
  description = "ID of the virtual network"
  value       = azurerm_virtual_network.example.id
}
```

## 8. 本地值的使用

- 使用局部变量计算值和复杂表达式
- 通过提取重复的表达式来提高可读性
- 将相关值合并到结构化局部变量中

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

## 9.遵循推荐的 Terraform 实践

- **冗余依赖检测**：搜索并删除 `depends_on`，其中依赖资源已在同一资源块中隐式引用。仅在明确需要时保留 `depends_on`。  切勿依赖模块输出。

- **迭代**：对 0-1 资源使用 `count`，对多个资源使用 `for_each`。优选稳定资源地址的映射。与 TFNFR7 对齐。

- **数据源**：在根模块中可接受，但在可重用模块中避免。优先选择显式模块参数而不是数据源查找。

- **参数化**：使用具有显式 `type` 声明 (TFNFR18)、综合描述 (TFNFR17) 和不可为 null 的默认值 (TFNFR20) 的强类型变量。利用 AVM 公开的变量。

- **版本控制**：目标最新稳定的 Terraform 和 Azure 提供程序版本。在代码中指定版本并保持更新（TFFR3）。

## 10. 文件夹结构

对 Terraform 配置使用一致的文件夹结构。

使用 tfvars 修改环境差异。一般来说，目标是保持环境相似，同时优化非生产环境的成本。

反模式 - 每个环境的分支、每个环境的存储库、每个环境的文件夹 - 或类似的布局，使得测试环境之间的根文件夹逻辑变得困难。  

请注意 Terragrunt 等可能影响此设计的工具。

**建议的**结构是：

```text
my-azure-app/
├── infra/                          # Terraform root module (AZD compatible)
│   ├── main.tf                     # Core resources
│   ├── variables.tf                # Input variables
│   ├── outputs.tf                  # Outputs
│   ├── terraform.tf                # Provider configuration
│   ├── locals.tf                   # Local values
│   └── environments/               # Environment-specific configurations
│       ├── dev.tfvars              # Development environment
│       ├── test.tfvars             # Test environment
│       └── prod.tfvars             # Production environment
├── .github/workflows/              # CI/CD pipelines (if using github)
├── .azdo/                          # CI/CD pipelines (suggested if using Azure DevOps)
└── README.md                       # Documentation
```

未经用户直接同意，切勿更改文件夹结构。

遵循 AVM 规范 TFNFR1、TFNFR2、TFNFR3 和 TFNFR4，以获得一致的文件命名和结构。

## Azure 特定的最佳实践

### 资源命名和标记

- 遵循 [Azure 命名约定](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)
- 对多区域部署使用一致的区域命名和变量
- 实施一致的标记。

### 资源组策略

- 指定时使用现有资源组
- 仅在必要时并经过确认后创建新资源组
- 使用指示目的和环境的描述性名称

### 网络注意事项

- 在创建新的网络资源之前验证现有的 VNet/子网 ID（例如，此解决方案是否部署到现有的中心和辐射登陆区域）
- 适当使用 NSG 和 ASG
- 需要时为 PaaS 服务实施专用端点，否则使用资源防火墙限制来限制公共访问。  注释需要公共端点的例外情况。

### 安全与合规性

- 使用托管身份而不是服务主体
- 使用适当的 RBAC 实施 Key Vault。
- 启用审计跟踪的诊断设置
- 遵循最小权限原则

## 成本管理

- 确认昂贵资源的预算批准
- 使用适合环境的大小（开发与生产）
- 如果未指定，请询问成本限制

## 状态管理

- 使用带有状态锁定的远程后端（Azure 存储）
- 切勿将状态文件提交到源代码管理
- 启用静态和传输中加密

## 验证

- 清点现有资源并提出删除未使用的资源块。
- 运行 `terraform validate` 检查语法
- 在运行 `terraform plan` 之前询问。  Terraform 计划将需要订阅 ID，该 ID 应源自 ARM_SUBSCRIPTION_ID 环境变量，*不*在提供程序块中编码。
- 首先在非生产环境中测试配置
- 确保幂等性（多次应用产生相同的结果）

## 回退行为

如果未加载一般规则，则默认为：极简代码生成、明确同意超出验证的任何 terraform 命令，以及在所有建议中遵守 CALMS 原则。
