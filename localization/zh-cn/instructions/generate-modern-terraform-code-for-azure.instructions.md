```instructions
---
description: '为 Azure 生成现代 Terraform 代码的指南'
applyTo: '**/*.tf'
---

## 1. 使用最新 Terraform 及 Provider
始终以最新稳定版 Terraform 和 Azure provider 为目标。在代码中指定所需的 Terraform 和 provider 版本，确保强制执行。及时更新 provider 以获取新特性和修复。

## 2. 代码结构清晰
合理拆分 Terraform 配置文件：
- `main.tf`：资源定义
- `variables.tf`：输入参数
- `outputs.tf`：输出参数
- 命名规范统一，格式化（`terraform fmt`）
这样便于维护和查阅。

## 3. 封装为模块
用 Terraform module 组织可复用基础设施组件。多处用到的资源集合：
- 建立独立 module，定义变量/输出
- 通过引用 module 复用，避免重复代码
- 提升一致性和可维护性

## 4. 善用变量与输出
- **参数化**所有可配置项，变量需注明类型和描述
- **可选变量**建议提供默认值
- **用 outputs** 暴露关键资源属性，便于其他模块或用户引用
- **敏感值**需标记，保护机密

## 5. Provider 选择（AzureRM vs AzAPI）
- **大多数场景用 `azurerm` provider**，稳定且覆盖面广
- **仅在需要最新特性或 azurerm 不支持的资源时用 `azapi`**
- **在代码注释中说明选择原因**
- 如有需要可混用，但优先选 azurerm

## 6. 依赖最小化
- **未经确认不要引入额外 provider 或 module**
- 如需特殊 provider（如 `random`、`tls`）或外部 module：
  - 注释说明原因
  - 确保用户同意
- 保持基础设施栈精简，避免不必要复杂度

## 7. 保证幂等性
- 配置应可多次 apply，结果一致
- **避免非幂等操作**：
  - 每次 apply 都运行的脚本
  - 可能重复创建冲突的资源
- **多次 `terraform apply` 测试**，第二次应无变更
- 用资源生命周期或条件表达式优雅处理漂移或外部变更

## 8. 状态管理
- **用远程后端**（如 Azure Storage 带锁）安全存储 state
- 支持团队协作
- **绝不提交 state 文件到源码库**
- 防止冲突，保持状态一致

## 9. 文档与架构图
- **文档需及时更新**
- **每次代码变更后更新 README.md**，补充变量、输出、用法
- 推荐用 `terraform-docs` 自动化
- **每次重大变更后更新架构图**
- 文档和图让团队都能理解基础设施

## 10. 校验与测试变更
- **运行 `terraform validate`**，并检查 `terraform plan` 输出再 apply
- 及早发现错误或意外修改
- **建议自动化检查**：
  - CI 流水线
  - pre-commit 钩子
  - 强制格式化、lint、基础校验

---

> 本文件为自动翻译，仅供参考。如有歧义请以英文原文为准。
```
