# 错误处理指南

本参考记录了预检验证期间的常见错误以及如何处理这些错误。

## 核心原则

**失败时继续。** 在最终报告中捕获所有问题，而不是在第一个错误处停止。这可以让用户全面了解需要修复的内容。

---

## 身份验证错误

### 未登录 (Azure CLI)

**检测：**
```
ERROR: Please run 'az login' to setup account.
ERROR: AADSTS700082: The refresh token has expired
```

**退出代码：** 非零

**处理：**
1. 注意报告中的错误
2. 包括修复步骤
3. 跳过剩余的 Azure CLI 命令
4. 如果可能，继续执行其他验证步骤

**报告条目：**
```markdown
#### ❌ Azure CLI Authentication Required

- **Severity:** Error
- **Source:** az cli
- **Message:** Not logged in to Azure CLI
- **Remediation:** Run `az login` to authenticate, then re-run preflight validation
- **Documentation:** https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli
```

### 未登录 (azd)

**检测：**
```
ERROR: not logged in, run `azd auth login` to login
```

**处理：**
1. 注意报告中的错误
2. 跳过 azd 命令
3. 建议`azd auth login`

**报告条目：**
```markdown
#### ❌ Azure Developer CLI Authentication Required

- **Severity:** Error
- **Source:** azd
- **Message:** Not logged in to Azure Developer CLI
- **Remediation:** Run `azd auth login` to authenticate, then re-run preflight validation
```

### 令牌已过期

**检测：**
```
AADSTS700024: Client assertion is not within its valid time range
AADSTS50173: The provided grant has expired
```

**处理：**
1. 注意错误
2. 建议重新验证
3. 跳过 Azure 操作

---

## 权限错误

### RBAC 权限不足

**检测：**
```
AuthorizationFailed: The client '...' with object id '...' does not have authorization 
to perform action '...' over scope '...'
```

**处理：**
1. **第一次尝试：** 使用 `--validation-level ProviderNoRbac` 重试
2. 请注意报告中的权限限制
3. 如果 ProviderNoRbac 也失败，请报告具体缺少的权限

**报告条目：**
```markdown
#### ⚠️ Limited Permission Validation

- **Severity:** Warning
- **Source:** what-if
- **Message:** Full RBAC validation failed; using read-only validation
- **Detail:** Missing permission: `Microsoft.Resources/deployments/write` on scope `/subscriptions/xxx`
- **Recommendation:** Request Contributor role on the target resource group, or verify deployment permissions with your administrator
```

### 未找到资源组

**检测：**
```
ResourceGroupNotFound: Resource group 'xxx' could not be found.
```

**处理：**
1. 报告中的注释
2. 建议创建资源组
3. 跳过此范围的假设分析

**报告条目：**
```markdown
#### ❌ Resource Group Does Not Exist

- **Severity:** Error
- **Source:** what-if
- **Message:** Resource group 'my-rg' does not exist
- **Remediation:** Create the resource group before deployment:
  ```bash
  az group create --名称 my-rg --位置 eastus
  ```
```

### 订阅访问被拒绝

**检测：**
```
SubscriptionNotFound: The subscription 'xxx' could not be found.
InvalidSubscriptionId: Subscription '...' is not valid
```

**处理：**
1. 报告中的注释
2. 建议检查订阅 ID
3. 列出可用的订阅

---

## 二头肌语法错误

### 编译错误

**检测：**
```
/path/main.bicep(22,51) : Error BCP064: Found unexpected tokens
/path/main.bicep(10,5) : Error BCP018: Expected the "=" character at this location
```

**处理：**
1. 解析行号/列号的错误输出
2. 在报告中包含所有错误（首先不要停止）
3. 继续假设（可能提供更多背景信息）

**报告条目：**
```markdown
#### ❌ Bicep Syntax Error

- **Severity:** Error
- **Source:** bicep build
- **Location:** `main.bicep:22:51`
- **Code:** BCP064
- **Message:** Found unexpected tokens in interpolated expression
- **Remediation:** Check the string interpolation syntax at line 22
- **Documentation:** https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/diagnostics/bcp064
```

### 找不到模块

**检测：**
```
Error BCP091: An error occurred reading file. Could not find file '...'
Error BCP190: The module is not valid
```

**处理：**
1. 注意缺少模块
2. 检查是否需要 `bicep restore`
3. 验证模块路径

### 参数文件问题

**检测：**
```
Error BCP032: The value must be a compile-time constant
Error BCP035: The specified object is missing required properties
```

**处理：**
1. 注意参数问题
2. 指出哪些参数有问题
3. 建议修复

---

## 工具未安装

### 未找到 Azure CLI

**检测：**
```
'az' is not recognized as an internal or external command
az: command not found
```

**处理：**
1. 报告中的注释
2. 提供安装说明。
  - 如果可用，请使用 Azure MCP `extension_cli_install` 工具获取安装说明。
  - 否则，请在 https://learn.microsoft.com/en-us/cli/azure/install-azure-cli 中查找说明。
3. 跳过 az 命令

**报告条目：**
```markdown
#### ⏭️ Azure CLI Not Installed

- **Severity:** Warning
- **Source:** environment
- **Message:** Azure CLI (az) is not installed or not in PATH
- **Remediation:** Install the Azure CLI <ADD INSTALLATION INSTRUCTIONS HERE>
- **Impact:** What-if validation using az commands was skipped
```

### 未找到二头肌 CLI

**检测：**
```
'bicep' is not recognized as an internal or external command
bicep: command not found
```

**处理：**
1. 报告中的注释
2. Azure CLI 可能有内置的 Bicep - 尝试 `az bicep build`
3. 提供安装链接

**报告条目：**
```markdown
#### ⏭️ Bicep CLI Not Installed

- **Severity:** Warning
- **Source:** environment
- **Message:** Bicep CLI is not installed
- **Remediation:** Install Bicep CLI: https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install
- **Impact:** Syntax validation was skipped; Azure will validate during what-if
```

### 未找到 Azure 开发人员 CLI

**检测：**
```
'azd' is not recognized as an internal or external command
azd: command not found
```

**处理：**
1. 如果 `azure.yaml` 存在，则这是必需的
2. 如果可能，回退到 az CLI 命令
3. 报告中的注释

---

## 假设具体错误

### 嵌套模板限制

**检测：**
```
The deployment exceeded the nested template limit of 500
```

**处理：**
1. 注意作为警告（不是错误）
2. 解释受影响的资源显示为“忽略”
3. 建议人工审核

### 不支持模板链接

**检测：**
```
templateLink references in nested deployments won't be visible in what-if
```

**处理：**
1. 注意作为警告
2. 解释限制
3. 实际部署时会验证资源

### 未计算的表达式

**检测：** 显示函数名称（如 `[utcNow()]`）而不是值的属性

**处理：**
1. 注释作为信息
2. 解释这些是在部署时评估的
3. 不是错误

---

## 网络错误

### 超时

**检测：**
```
Connection timed out
Request timed out
```

**处理：**
1. 建议重试
2. 检查网络连接
3. 可能表明 Azure 服务问题

### SSL/TLS 错误

**检测：**
```
SSL: CERTIFICATE_VERIFY_FAILED
unable to get local issuer certificate
```

**处理：**
1. 报告中的注释
2. 可能表示代理或公司防火墙
3. 建议检查 SSL 设置

---

## 后备策略

当主要验证失败时，请按顺序尝试回退：

```
Provider (full RBAC validation)
    ↓ fails with permission error
ProviderNoRbac (validation without write permission check)
    ↓ fails
Template (static syntax only)
    ↓ fails
Report all failures and skip what-if analysis
```

**始终继续生成报告**，即使所有验证步骤都失败。

---

## 错误报告聚合

当出现多个错误时，将它们逻辑聚合：

1. **按来源分组**（二头肌、假设、权限）
2. **按严重性排序**（错误在警告之前）
3. **重复数据删除**类似错误
4. **在顶部提供摘要计数**

示例：
```markdown
## Issues

Found **3 errors** and **2 warnings**

### Errors (3)

1. [Bicep Syntax Error - main.bicep:22:51](#error-1)
2. [Bicep Syntax Error - main.bicep:45:10](#error-2)
3. [Resource Group Not Found](#error-3)

### Warnings (2)

1. [Limited Permission Validation](#warning-1)
2. [Nested Template Limit Reached](#warning-2)
```

---

## 退出代码参考

|工具|退出代码 |意义|
|------|-----------|---------|
| AZ | 0 |成功|
| AZ | 1 |一般错误 |
| AZ | 2 |未找到命令|
| AZ | 3 |缺少必需的参数 |
|阿兹德 | 0 |成功|
|阿兹德 | 1 |错误 |
|二头肌 | 0 |构建成功 |
|二头肌 | 1 |构建失败（错误）|
|二头肌 | 2 |构建成功但有警告 |
