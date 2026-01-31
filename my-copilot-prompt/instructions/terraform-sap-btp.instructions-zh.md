---
描述：“SAP 业务技术平台 (SAP BTP) 的 Terraform 约定和指南。”
applyTo: '**/*.tf, **/*.tfvars, **/*.tflint.hcl, **/*.tf.json, **/*.tfvars.json'
---

# SAP BTP 上的 Terraform – 最佳实践和惯例

## 核心原则

保持 Terraform 代码最少、模块化、可重复、安全和可审计。
始终对 Terraform HCL 进行版本控制，并且从不对生成的状态进行版本控制。

## 安全性

强制：
- 使用最新稳定的 Terraform CLI 和提供程序版本；主动升级安全补丁。
- 不要提交机密、凭证、证书、Terraform 状态或计划输出工件。
- 将所有秘密变量和输出标记为 `sensitive = true`。
- 首选临时/只写提供者身份验证 (Terraform >= 1.11)，因此秘密永远不会保留在状态中。
- 最小化敏感输出；只发出下游自动化真正需要的内容。
- 在 CI 中连续扫描 `tfsec`、`trivy`、`checkov`（至少选择一个）。
- 定期检查提供商凭据、轮换密钥并在支持的情况下启用 MFA。

## 模块化

结构清晰、速度快：
- 按逻辑域（例如权利、服务实例）划分，而不是按环境划分。
- 仅将模块用于可重用的多资源模式；避免使用单一资源包装模块。
- 保持模块层次结构浅；避免深度嵌套和循环依赖。
- 通过 `outputs` 仅公开必要的跨模块数据（需要时标记为敏感）。

## 可维护性

目标是显式>隐式。
- 评论“为什么”，而不是“什么”；避免重述明显的资源属性。
- 参数化（变量）而不是硬编码；仅在合理时才提供默认值。
- 优先选择外部现有基础设施的数据源；对于刚刚在同一根目录中创建的资源，切勿使用输出。
- 避免通用可重用模块中的数据源；需要输入。
- 删除未使用/速度慢的数据源；它们会降低计划时间。
- 对派生或重复表达式使用 `locals` 以集中逻辑。

## 样式和格式

### 一般
- 资源、变量、输出的描述性、一致的名称。
- Snake_case 用于变量和局部变量。
- 2 个空格缩进；运行`terraform fmt -recursive`。

### 布局和文件

推荐结构：
```text
my-sap-btp-app/
├── infra/                      # Root module
│   ├── main.tf                 # Core resources (split by domain when large)
│   ├── variables.tf            # Inputs
│   ├── outputs.tf              # Outputs
│   ├── provider.tf             # Provider config(s)
│   ├── locals.tf               # Local/derived values
│   └── environments/           # Environment var files only
│       ├── dev.tfvars
│       ├── test.tfvars
│       └── prod.tfvars
├── .github/workflows/          # CI/CD (if GitHub)
└── README.md                   # Documentation
```

规则：
- 不要为每个环境创建单独的分支/存储库/文件夹（反模式）。
- 保持环境漂移最小；仅对 *.tfvars 文件中的差异进行编码。
- 将超大的 `main.tf` / `variables.tf` 拆分为逻辑命名的片段（例如 `main_services.tf`、`variables_services.tf`）。
  保持命名一致。

### 资源块组织

顺序（顶部 → 底部）：可选 `depends_on`，然后是 `count`/`for_each`，然后是属性，最后是 `lifecycle`。
- 仅当 Terraform 无法推断依赖性时（例如，数据源需要权利），才使用 `depends_on`。
- 使用 `count` 作为可选的单一资源； `for_each` 用于由稳定地址的映射键控的多个实例。
- 组属性：先必填，后可选；逻辑部分之间的空行。
- 在部分内按字母顺序排列以加快扫描速度。

### 变量
- 每个变量：显式 `type`，非空 `description`。
- 优先选择具体类型（`object`、`map(string)` 等）而不是 `any`。
- 避免集合默认为空；使用空列表/地图代替。

### 当地人
- 集中计算或重复的表达式。
- 将相关值分组到对象局部变量中以实现内聚性。

### 输出
- 仅公开下游模块/自动化消耗的内容。
- 标记秘密 `sensitive = true`。
- 始终给出明确的 `description`。

### 格式化和检查
- 运行 `terraform fmt -recursive` （CI 中必需）。
- 在预提交/CI 中强制执行 `tflint` （以及可选的 `terraform validate`）。

## 文档

强制：
- 所有变量和输出上的 `description` + `type`。
- 简洁的根 `README.md`：目的、先决条件、身份验证模型、用法（初始化/计划/应用）、测试、回滚。
- 使用 `terraform-docs` 生成模块文档（如果可能的话添加到 CI）。
- 仅在澄清非显而易见的决定或限制时发表评论。

## 状态管理
- 使用支持锁定的远程后端（例如 Terraform Cloud、AWS S3、GCS、Azure 存储）。避免 SAP BTP 对象存储（可靠锁定和安全性功能不足）。
- 切勿提交 `*.tfstate` 或备份。
- 加密静态和传输中的状态；按最小权限原则限制访问。

## 验证
- 在提交之前运行 `terraform validate` （语法和内部检查）。
- 在 `terraform plan` 之前与用户确认（需要身份验证和全局帐户子域）。通过 env vars 或 tfvars 提供身份验证；切勿在提供程序块中内联机密。
- 首先在非产品中进行测试；确保幂等适用。

## 测试
- 使用 Terraform 测试框架 (`*.tftest.hcl`) 进行模块逻辑和不变量。
- 涵盖成功和失败的路径；保持测试无状态/幂等。
- 在可行的情况下更喜欢模拟外部数据源。

## SAP BTP 提供商细节

指南：
- 使用 `data "btp_subaccount_service_plan"` 解析服务计划 ID，并引用该数据源中的 `serviceplan_id`。

示例：
```terraform
data "btp_subaccount_service_plan" "example" {
  subaccount_id = var.subaccount_id
  service_name  = "your_service_name"
  plan_name     = "your_plan_name"
}

resource "btp_subaccount_service_instance" "example" {
  subaccount_id  = var.subaccount_id
  serviceplan_id = data.btp_subaccount_service_plan.example.id
  name           = "my-example-instance"
}
```

显式依赖关系（提供者无法推断）：
```terraform
resource "btp_subaccount_entitlement" "example" {
  subaccount_id = var.subaccount_id
  service_name  = "your_service_name"
  plan_name     = "your_plan_name"
}

data "btp_subaccount_service_plan" "example" {
  subaccount_id = var.subaccount_id
  service_name  = "your_service_name"
  plan_name     = "your_plan_name"
  depends_on    = [btp_subaccount_entitlement.example]
}
```

订阅还取决于权利；当提供者无法通过属性推断链接时添加 `depends_on` （匹配 `service_name`/`plan_name` ↔ `app_name`）。

## 工具集成

### HashiCorp Terraform MCP 服务器
使用 Terraform MCP 服务器进行交互式架构查找、资源块起草和验证。
1. 安装并运行服务器（请参阅 https://github.com/mcp/hashicorp/terraform-mcp-server）。
2. 将其作为工具添加到您的 Copilot / MCP 客户端配置中。
3. 在创作之前查询提供程序架构（例如，列出资源、数据源）。
4. 生成草稿资源块，然后手动细化命名和标记标准。
5. 验证计划摘要（切勿包含秘密）；在 `apply` 之前与审阅者确认差异。

### 地形注册表
请参考 SAP BTP 提供程序文档：https://registry.terraform.io/providers/SAP/btp/latest/docs 了解权威资源和数据源字段。如果不确定，请与注册表文档交叉检查 MCP 响应。

## 反模式（避免）

配置：
- 硬编码环境特定值（使用变量和 tfvar）。
- `terraform import` 的常规使用（仅限迁移）。
- 深层/不透明的条件逻辑和动态块会降低清晰度。
- `local-exec` 配置程序，除了不可避免的集成差距。
- 除非明确证明合理（拆分模块），否则将 SAP BTP 提供程序与 Cloud Foundry 提供程序混合在同一根目录中。

安全性：
- 在 HCL、状态或 VCS 中存储机密。
- 禁用加密、验证或扫描以提高速度。
- 使用默认密码/密钥或跨环境重复使用凭据。

运营：
- 直接生产无需事先进行非产品验证。
- Terraform 之外的手动漂移更改。
- 忽略状态不一致/腐败症状。
- 运行生产适用于不受控制的本地笔记本电脑（使用 CI/CD 或批准的运行程序）。
- 从原始 `*.tfstate` 而不是输出/数据源读取业务数据。

所有更改都必须通过 Terraform CLI + HCL 进行——切勿手动改变状态。
