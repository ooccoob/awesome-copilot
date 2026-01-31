---
适用于：'**'
---

# 适用于 Python 的 Dataverse SDK — 身份验证和安全模式

基于官方 Microsoft Azure SDK 身份验证文档和 Dataverse SDK 最佳实践。

## 1. 认证概述

适用于 Python 的 Dataverse SDK 使用 Azure Identity 凭据进行基于令牌的身份验证。此方法遵循最小权限原则，适用于本地开发、云部署和本地环境。

### 为什么基于令牌的身份验证？

**相对于连接字符串的优点**：
- 建立您的应用程序所需的特定权限（最小权限原则）
- 凭证的范围仅适用于预期的应用程序
- 通过托管身份，无需存储或泄露任何秘密
- 无需更改代码即可跨环境无缝工作

---

## 2. 凭证类型及选择

### 交互式浏览器凭证（本地开发）

**用于**：本地开发期间的开发人员工作站。

```python
from azure.identity import InteractiveBrowserCredential
from PowerPlatform.Dataverse.client import DataverseClient

# Opens browser for authentication
credential = InteractiveBrowserCredential()
client = DataverseClient(
    base_url="https://myorg.crm.dynamics.com",
    credential=credential
)

# First use prompts for sign-in; subsequent calls use cached token
records = client.get("account")
```

**何时使用**：
- ✅ 交互式开发和测试
- ✅ 带 UI 的桌面应用程序
- ❌ 后台服务或预定作业

---

### 默认 Azure 凭据（推荐用于所有环境）

**用于**：在多个环境中运行的应用程序（开发→测试→生产）。

```python
from azure.identity import DefaultAzureCredential
from PowerPlatform.Dataverse.client import DataverseClient

# Attempts credentials in this order:
# 1. Environment variables (app service principal)
# 2. Azure CLI credentials (local development)
# 3. Azure PowerShell credentials (local development)
# 4. Managed identity (when running in Azure)
credential = DefaultAzureCredential()

client = DataverseClient(
    base_url="https://myorg.crm.dynamics.com",
    credential=credential
)

records = client.get("account")
```

**优点**：
- 单一代码路径在任何地方都适用
- 不需要特定于环境的逻辑
- 自动检测可用的凭据
- 生产应用程序的首选

**凭证链**：
1. 环境变量（`AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_CLIENT_SECRET`）
2. Visual Studio 代码登录
3. Azure CLI (`az login`)
4. Azure PowerShell (`Connect-AzAccount`)
5. 托管身份（在 Azure VM、应用服务、AKS 等上）

---

### 客户端秘密凭证（服务主体）

**用途**：无人值守身份验证（计划作业、脚本、本地服务）。

```python
from azure.identity import ClientSecretCredential
from PowerPlatform.Dataverse.client import DataverseClient
import os

credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"]
)

client = DataverseClient(
    base_url="https://myorg.crm.dynamics.com",
    credential=credential
)

records = client.get("account")
```

**设置步骤**：
1. 在 Azure AD 中创建应用程序注册
2. 创建客户端机密（确保安全！）
3. 向应用程序授予 Dataverse 权限
4. 将凭据存储在环境变量或安全保管库中

**安全问题**：
- ⚠️ 切勿在源代码中硬编码凭证
- ⚠️ 将机密存储在 Azure Key Vault 或环境变量中
- ⚠️定期轮换凭证
- ⚠️ 使用所需的最低权限

---

### 托管身份凭据（Azure 资源）

**用于**：Azure 中托管的应用程序（应用程序服务、Azure Functions、AKS、VM）。

```python
from azure.identity import ManagedIdentityCredential
from PowerPlatform.Dataverse.client import DataverseClient

# No secrets needed - Azure manages identity
credential = ManagedIdentityCredential()

client = DataverseClient(
    base_url="https://myorg.crm.dynamics.com",
    credential=credential
)

records = client.get("account")
```

**好处**：
- ✅ 没有需要管理的秘密
- ✅ 自动令牌刷新
- ✅ 高度安全
- ✅ 内置到 Azure 服务

**设置**：
1. 在 Azure 资源（应用服务、VM 等）上启用托管标识
2. 向托管身份授予 Dataverse 权限
3. 代码自动使用身份

---

## 3. 环境特定配置

### 本地发展

```python
# .env file (git-ignored)
DATAVERSE_URL=https://myorg-dev.crm.dynamics.com

# Python code
import os
from azure.identity import DefaultAzureCredential
from PowerPlatform.Dataverse.client import DataverseClient

# Uses your Azure CLI credentials
credential = DefaultAzureCredential()
client = DataverseClient(
    base_url=os.environ["DATAVERSE_URL"],
    credential=credential
)
```

**设置**：`az login` 使用您的开发者帐户

---

### Azure 应用服务/Azure 函数

```python
from azure.identity import ManagedIdentityCredential
from PowerPlatform.Dataverse.client import DataverseClient

# Automatically uses managed identity
credential = ManagedIdentityCredential()
client = DataverseClient(
    base_url="https://myorg.crm.dynamics.com",
    credential=credential
)
```

**设置**：在应用服务中启用托管身份，在 Dataverse 中授予权限

---

### 本地/第三方托管

```python
import os
from azure.identity import ClientSecretCredential
from PowerPlatform.Dataverse.client import DataverseClient

credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"]
)

client = DataverseClient(
    base_url="https://myorg.crm.dynamics.com",
    credential=credential
)
```

**设置**：创建服务主体、安全存储凭证、授予 Dataverse 权限

---

## 4. 客户端配置和连接设置

### 基本配置

```python
from PowerPlatform.Dataverse.core.config import DataverseConfig
from azure.identity import DefaultAzureCredential
from PowerPlatform.Dataverse.client import DataverseClient

cfg = DataverseConfig()
cfg.logging_enable = True  # Enable detailed logging

client = DataverseClient(
    base_url="https://myorg.crm.dynamics.com",
    credential=DefaultAzureCredential(),
    config=cfg
)
```

### HTTP 调优

```python
from PowerPlatform.Dataverse.core.config import DataverseConfig

cfg = DataverseConfig()

# Timeout settings
cfg.http_timeout = 30          # Request timeout in seconds

# Retry configuration
cfg.http_retries = 3           # Number of retry attempts
cfg.http_backoff = 1           # Initial backoff in seconds

# Connection reuse
cfg.connection_timeout = 5     # Connection timeout

client = DataverseClient(
    base_url="https://myorg.crm.dynamics.com",
    credential=credential,
    config=cfg
)
```

---

## 5. 安全最佳实践

### 1. 切勿对凭证进行硬编码

```python
# ❌ BAD - Don't do this!
credential = ClientSecretCredential(
    tenant_id="your-tenant-id",
    client_id="your-client-id",
    client_secret="your-secret-key"  # EXPOSED!
)

# ✅ GOOD - Use environment variables
import os
credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"]
)
```

### 2. 安全地存储秘密

**发展**：
```bash
# .env file (git-ignored)
AZURE_TENANT_ID=your-tenant-id
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-secret-key
```

**生产**：
```python
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# Retrieve secrets from Azure Key Vault
credential = DefaultAzureCredential()
client = SecretClient(
    vault_url="https://mykeyvault.vault.azure.net",
    credential=credential
)

secret = client.get_secret("dataverse-client-secret")
```

### 3. 实行最小权限原则

```python
# Grant minimal permissions:
# - Only read if app only reads
# - Only specific tables if possible
# - Time-limit credentials (auto-rotation)
# - Use managed identity instead of shared secrets
```

### 4. 监控身份验证事件

```python
import logging

logger = logging.getLogger("dataverse_auth")

try:
    client = DataverseClient(
        base_url="https://myorg.crm.dynamics.com",
        credential=credential
    )
    logger.info("Successfully authenticated to Dataverse")
except Exception as e:
    logger.error(f"Authentication failed: {e}")
    raise
```

### 5. 处理令牌过期

```python
from azure.core.exceptions import ClientAuthenticationError
import time

def create_with_auth_retry(client, table_name, payload, max_retries=2):
    """Create record, retrying if token expired."""
    for attempt in range(max_retries):
        try:
            return client.create(table_name, payload)
        except ClientAuthenticationError:
            if attempt < max_retries - 1:
                logger.warning("Token expired, retrying...")
                time.sleep(1)
            else:
                raise
```

---

## 6. 多租户应用程序

### 租户感知客户端

```python
from azure.identity import DefaultAzureCredential
from PowerPlatform.Dataverse.client import DataverseClient

def get_client_for_tenant(tenant_id: str) -> DataverseClient:
    """Get DataverseClient for specific tenant."""
    credential = DefaultAzureCredential()
    
    # Dataverse URL contains tenant-specific org
    base_url = f"https://{get_org_for_tenant(tenant_id)}.crm.dynamics.com"
    
    return DataverseClient(
        base_url=base_url,
        credential=credential
    )

def get_org_for_tenant(tenant_id: str) -> str:
    """Map tenant to Dataverse organization."""
    # Implementation depends on your multi-tenant strategy
    # Could be database lookup, configuration, etc.
    pass
```

---

## 7. 身份验证故障排除

### 错误：“访问被拒绝”(403)

```python
try:
    client.get("account")
except DataverseError as e:
    if e.status_code == 403:
        print("User/app lacks Dataverse permissions")
        print("Ensure Dataverse security role is assigned")
```

### 错误：“凭据无效”(401)

```python
# Check credential source
from azure.identity import DefaultAzureCredential

try:
    cred = DefaultAzureCredential(exclude_cli_credential=False, 
                                  exclude_powershell_credential=False)
    # Force re-authentication
    import subprocess
    subprocess.run(["az", "login"])
except Exception as e:
    print(f"Authentication failed: {e}")
```

### 错误：“无效租户” 

```python
# Verify tenant ID
import json
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
token = credential.get_token("https://dataverse.dynamics.com/.default")

# Decode token to verify tenant
import base64
payload = base64.b64decode(token.token.split('.')[1] + '==')
claims = json.loads(payload)
print(f"Token tenant: {claims.get('tid')}")
```

---

## 8. 凭证生命周期

### 令牌刷新

Azure Identity 自动处理令牌刷新：

```python
# Tokens are cached and refreshed automatically
credential = DefaultAzureCredential()

# First call acquires token
client.get("account")

# Subsequent calls reuse cached token
client.get("contact")

# If token expires, SDK automatically refreshes
```

### 会话管理

```python
class DataverseSession:
    """Manages DataverseClient lifecycle."""
    
    def __init__(self, base_url: str):
        from azure.identity import DefaultAzureCredential
        
        self.client = DataverseClient(
            base_url=base_url,
            credential=DefaultAzureCredential()
        )
    
    def __enter__(self):
        return self.client
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup if needed
        pass

# Usage
with DataverseSession("https://myorg.crm.dynamics.com") as client:
    records = client.get("account")
```

---

## 9. 数据宇宙特定的安全性

### 行级安全性 (RLS)

用户的 Dataverse 安全角色决定可访问的记录：

```python
from azure.identity import InteractiveBrowserCredential
from PowerPlatform.Dataverse.client import DataverseClient

# Each user gets client with their credentials
def get_user_client(user_username: str) -> DataverseClient:
    # User must already be authenticated
    credential = InteractiveBrowserCredential()
    
    client = DataverseClient(
        base_url="https://myorg.crm.dynamics.com",
        credential=credential
    )
    
    # User only sees records they have access to
    return client
```

### 安全角色

分配所需的最少角色：
- **系统管理员**：完全访问权限（避免应用程序）
- **销售经理**：销售表格+报告
- **服务代表**：服务案例+知识
- **自定义**：创建具有特定表权限的角色

---

## 10.另请参阅

- [Azure 身份客户端库](https://learn.microsoft.com/en-us/python/api/azure-identity)
- [向 Azure 服务进行身份验证](https://learn.microsoft.com/en-us/azure/developer/python/sdk/authentication/overview)
- [Azure Key Vault for Secrets](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)
- [数据宇宙安全模型](https://learn.microsoft.com/en-us/power-platform/admin/security/security-overview)
