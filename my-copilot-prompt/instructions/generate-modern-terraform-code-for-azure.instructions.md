---
description: 'Guidelines for generating modern Terraform code for Azure'
applyTo: '**/*.tf'
---

## 1.使用最新的 Terraform 和提供程序
始终以最新的稳定 Terraform 版本和 Azure 提供程序为目标。在代码中，指定所需的 Terraform 和提供程序版本以强制执行此操作。保持提供商版本更新以获得新功能和修复。

## 2. 干净地组织代码
具有逻辑文件分离的结构 Terraform 配置：

- 使用 `main.tf` 获取资源
- 使用 `variables.tf` 作为输入
- 使用 `outputs.tf` 进行输出
- 遵循一致的命名约定和格式 (`terraform fmt`)

这使得代码易于浏览和维护。

## 3. 封装成模块

使用 Terraform 模块对可重用基础设施组件进行分组。对于将在多个上下文中使用的任何资源集：

- 创建一个具有自己的变量/输出的模块
- 引用它而不是重复代码
- 这促进了重用和一致性

## 4. 利用变量和输出

- **使用具有类型和描述的变量对所有可配置值进行参数化
- **在适合可选变量的情况下提供默认值**
- **使用输出**公开关键资源属性以供其他模块或用户参考
- **相应地标记敏感值**以保护秘密

## 5. 提供商选择（AzureRM 与 AzAPI）

- **大多数情况下使用 `azurerm` 提供程序** – 它提供高稳定性并涵盖大多数 Azure 服务
- **仅在您需要的情况下才使用 `azapi` 提供程序**：
  - 最新的 Azure 功能
  - `azurerm` 尚不支持的资源
- **在代码注释中记录选择**
- 如果需要，两个提供程序可以一起使用，但在有疑问时更喜欢 `azurerm`

## 6. 最小的依赖性

- **请勿在未经确认的情况下引入**超出项目范围的其他提供程序或模块
- 如果需要特殊的提供程序（例如 `random`、`tls`）或外部模块：
  - 添加评论来解释
  - 确保用户批准
- 保持基础设施堆栈精简并避免不必要的复杂性

## 7. 确保幂等性

- 编写可重复应用并获得相同结果的配置
- **避免非幂等操作**：
  - 每次应用时运行的脚本
  - 如果创建两次可能会发生冲突的资源
- **通过多次 `terraform apply` 运行进行测试**并确保第二次运行结果为零更改
- 使用资源生命周期设置或条件表达式来优雅地处理偏差或外部更改

## 8. 状态管理

- **使用远程后端**（例如具有状态锁定的 Azure 存储）来安全地存储 Terraform 状态
- 启用团队协作
- **永远不要将状态文件**提交到源代码管理
- This prevents conflicts and keeps the infrastructure state consistent

## 9. 文件和图表

- **维护最新文档**
- **Update README.md** with any new variables, outputs, or usage instructions whenever the code changes
- Consider using tools like `terraform-docs` for automation
- **Update architecture diagrams** to reflect infrastructure changes after each significant update
- Well-documented code and diagrams ensure the whole team understands the infrastructure

## 10. 验证和测试更改

- **Run `terraform validate`** and review the `terraform plan` output before applying changes
- 及早发现错误或意外修改
- **考虑实施自动检查**：
  - CI 管道
  - 预提交挂钩
  - Enforce formatting, linting, and basic validation
