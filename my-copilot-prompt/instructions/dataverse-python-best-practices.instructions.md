# 适用于 Python 的 Dataverse SDK - 最佳实践指南

## 概述
从 Microsoft 官方 PowerPlatform-DataverseClient-Python 存储库、示例和推荐工作流程中提取的生产就绪模式和最佳实践。

## 1. 安装及环境设置

### 生产安装
```bash
# Install the published SDK from PyPI
pip install PowerPlatform-Dataverse-Client

# Install Azure Identity for authentication
pip install azure-identity

# Optional: pandas integration for data manipulation
pip install pandas
```

### 开发安装
```bash
# Clone the repository
git clone https://github.com/microsoft/PowerPlatform-DataverseClient-Python.git
cd PowerPlatform-DataverseClient-Python

# Install in editable mode for live development
pip install -e .

# Install development dependencies
pip install pytest pytest-cov black isort mypy ruff
```

### Python版本支持
- **最低**：Python 3.10
- **推荐**：Python 3.11+ 以获得最佳性能
- **支持**：Python 3.10、3.11、3.12、3.13、3.14

### 验证安装
```python
from PowerPlatform.Dataverse import __version__
from PowerPlatform.Dataverse.client import DataverseClient
from azure.identity import InteractiveBrowserCredential

print(f"SDK Version: {__version__}")
print("Installation successful!")
```

---

## 2. 身份验证模式

### 交互式开发（基于浏览器）
```python
from azure.identity import InteractiveBrowserCredential
from PowerPlatform.Dataverse.client import DataverseClient

credential = InteractiveBrowserCredential()
client = DataverseClient("https://yourorg.crm.dynamics.com", credential)
```

**何时使用：** 本地开发、交互式测试、单用户场景。

### 生产（客户秘密）
```python
from azure.identity import ClientSecretCredential
from PowerPlatform.Dataverse.client import DataverseClient

credential = ClientSecretCredential(
    tenant_id="your-tenant-id",
    client_id="your-client-id",
    client_secret="your-client-secret"
)
client = DataverseClient("https://yourorg.crm.dynamics.com", credential)
```

**何时使用：** 服务器端应用程序、Azure 自动化、计划作业。

### 基于证书的身份验证
```python
from azure.identity import ClientCertificateCredential
from PowerPlatform.Dataverse.client import DataverseClient

credential = ClientCertificateCredential(
    tenant_id="your-tenant-id",
    client_id="your-client-id",
    certificate_path="path/to/certificate.pem"
)
client = DataverseClient("https://yourorg.crm.dynamics.com", credential)
```

**何时使用：** 高度安全的环境、证书固定要求。

### Azure CLI 身份验证
```python
from azure.identity import AzureCliCredential
from PowerPlatform.Dataverse.client import DataverseClient

credential = AzureCliCredential()
client = DataverseClient("https://yourorg.crm.dynamics.com", credential)
```

**何时使用：** 安装了 Azure CLI、Azure DevOps 管道的本地测试。

---

## 3. 单例客户端模式

**最佳实践**：创建一个 `DataverseClient` 实例并在整个应用程序中重复使用它。

```python
# ❌ ANTI-PATTERN: Creating new clients repeatedly
def fetch_account(account_id):
    credential = InteractiveBrowserCredential()
    client = DataverseClient("https://yourorg.crm.dynamics.com", credential)
    return client.get("account", account_id)

# ✅ PATTERN: Singleton client
class DataverseService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            credential = InteractiveBrowserCredential()
            cls._instance = DataverseClient(
                "https://yourorg.crm.dynamics.com", 
                credential
            )
        return cls._instance

# Usage
service = DataverseService()
account = service.get("account", account_id)
```

---

## 4、配置优化

### 连接设置
```python
from PowerPlatform.Dataverse.core.config import DataverseConfig
from PowerPlatform.Dataverse.client import DataverseClient
from azure.identity import ClientSecretCredential

config = DataverseConfig(
    language_code=1033,  # English (US)
    # Note: http_retries, http_backoff, http_timeout are reserved for internal use
)

credential = ClientSecretCredential(tenant_id, client_id, client_secret)
client = DataverseClient("https://yourorg.crm.dynamics.com", credential, config)
```

**关键配置选项：**
- `language_code`：API 响应的语言（默认值：英语 1033）

---

## 5. CRUD 操作最佳实践

### 创建操作

#### 单条记录
```python
record_data = {
    "name": "Contoso Ltd",
    "telephone1": "555-0100",
    "creditlimit": 100000.00,
}
created_ids = client.create("account", record_data)
record_id = created_ids[0]
print(f"Created: {record_id}")
```

#### 批量创建（自动优化）
```python
# SDK automatically uses CreateMultiple for arrays > 1 record
records = [
    {"name": f"Company {i}", "creditlimit": 50000 + (i * 1000)}
    for i in range(100)
]
created_ids = client.create("account", records)
print(f"Created {len(created_ids)} records")
```

**性能**：批量创建在内部进行了优化；无需手动批处理。

### 读操作

#### 按 ID 的单条记录
```python
account = client.get("account", "account-guid-here")
print(account.get("name"))
```

#### 过滤和选择查询
```python
# Returns paginated results (generator)
for page in client.get(
    "account",
    filter="creditlimit gt 50000",
    select=["name", "creditlimit", "telephone1"],
    orderby="name",
    top=100
):
    for account in page:
        print(f"{account['name']}: ${account['creditlimit']}")
```

**关键参数：**
- `filter`：OData 过滤器（必须使用**小写**逻辑名称）
- `select`：要检索的字段（提高性能）
- `orderby`：对结果进行排序
- `top`：每页最大记录数（默认：5000）
- `page_size`：覆盖分页的页面大小

#### SQL 查询（只读）
```python
# SQL queries are read-only; use for complex analytics
results = client.query_sql("""
    SELECT TOP 10 name, creditlimit 
    FROM account 
    WHERE creditlimit > 50000
    ORDER BY name
""")

for row in results:
    print(f"{row['name']}: ${row['creditlimit']}")
```

**限制：**
- 只读（仅 SELECT，无 DML）
- 对于复杂的连接和分析很有用
- 可能会被组织政策禁用

### 更新操作

#### 单条记录
```python
client.update("account", "account-guid", {
    "creditlimit": 150000.00,
    "name": "Updated Company Name"
})
```

#### 批量更新（广播相同更改）
```python
# Update all selected records with same data
account_ids = ["id1", "id2", "id3"]
client.update("account", account_ids, {
    "industrycode": 1,  # Retail
    "accountmanagerid": "manager-guid"
})
```

#### 配对更新（1:1 记录更新）
```python
# For different updates per record, send multiple calls
updates = {
    "id1": {"creditlimit": 100000},
    "id2": {"creditlimit": 200000},
    "id3": {"creditlimit": 300000},
}
for record_id, data in updates.items():
    client.update("account", record_id, data)
```

### 删除操作

#### 单条记录
```python
client.delete("account", "account-guid")
```

#### 批量删除（优化）
```python
# SDK automatically uses BulkDelete for large lists
record_ids = ["id1", "id2", "id3", ...]
client.delete("account", record_ids, use_bulk_delete=True)
```

---

## 6. 错误处理和恢复

### 异常层次结构
```python
from PowerPlatform.Dataverse.core.errors import (
    DataverseError,           # Base class
    ValidationError,          # Validation failures
    MetadataError,           # Table/column operations
    HttpError,               # HTTP-level errors
    SQLParseError            # SQL query syntax errors
)

try:
    client.create("account", {"name": None})  # Invalid
except ValidationError as e:
    print(f"Validation failed: {e}")
    # Handle validation-specific logic
except DataverseError as e:
    print(f"General SDK error: {e}")
    # Handle other SDK errors
```

### 重试逻辑模式
```python
import time
from PowerPlatform.Dataverse.core.errors import HttpError

def create_with_retry(table_name, record_data, max_retries=3):
    """Create record with exponential backoff retry logic."""
    for attempt in range(max_retries):
        try:
            return client.create(table_name, record_data)
        except HttpError as e:
            if attempt == max_retries - 1:
                raise
            
            # Exponential backoff: 1s, 2s, 4s
            backoff_seconds = 2 ** attempt
            print(f"Attempt {attempt + 1} failed. Retrying in {backoff_seconds}s...")
            time.sleep(backoff_seconds)

# Usage
created_ids = create_with_retry("account", {"name": "Contoso"})
```

### 429（请求速率限制）处理
```python
import time
from PowerPlatform.Dataverse.core.errors import HttpError

try:
    accounts = client.get("account", top=5000)
except HttpError as e:
    if "429" in str(e):
        # Rate limited; wait and retry
        print("Rate limited. Waiting 60 seconds...")
        time.sleep(60)
        accounts = client.get("account", top=5000)
    else:
        raise
```

---

## 7. 表和列管理

### 创建自定义表
```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

# Define columns with types
columns = {
    "new_Title": "string",
    "new_Quantity": "int",
    "new_Amount": "decimal",
    "new_Completed": "bool",
    "new_Priority": Priority,  # Creates option set/picklist
    "new_CreatedDate": "datetime"
}

table_info = client.create_table(
    "new_CustomTable",
    primary_column_schema_name="new_Name",
    columns=columns
)

print(f"Created table: {table_info['table_schema_name']}")
```

### 获取表元数据
```python
table_info = client.get_table_info("account")
print(f"Schema Name: {table_info['table_schema_name']}")
print(f"Logical Name: {table_info['table_logical_name']}")
print(f"Entity Set: {table_info['entity_set_name']}")
print(f"Primary ID: {table_info['primary_id_attribute']}")
```

### 列出所有表
```python
tables = client.list_tables()
for table in tables:
    print(f"{table['table_schema_name']} ({table['table_logical_name']})")
```

### 栏目管理
```python
# Add columns to existing table
client.create_columns("new_CustomTable", {
    "new_Status": "string",
    "new_Priority": "int"
})

# Delete columns
client.delete_columns("new_CustomTable", ["new_Status", "new_Priority"])

# Delete table
client.delete_table("new_CustomTable")
```

---

## 8. 分页和大型结果集

### 分页模式
```python
# Retrieve all accounts in pages
all_accounts = []
for page in client.get(
    "account",
    top=500,      # Records per page
    page_size=500
):
    all_accounts.extend(page)
    print(f"Retrieved page with {len(page)} records")

print(f"Total: {len(all_accounts)} records")
```

### 使用连续令牌进行手动分页
```python
# For complex paging scenarios
skip_count = 0
page_size = 1000

while True:
    page = client.get("account", top=page_size, skip=skip_count)
    if not page:
        break
    
    print(f"Page {skip_count // page_size + 1}: {len(page)} records")
    skip_count += page_size
```

---

## 9. 文件操作

### 上传小文件 (< 128 MB)
```python
from pathlib import Path

file_path = Path("document.pdf")
record_id = "account-guid"

# Single PATCH upload
response = client.upload_file(
    table_name="account",
    record_id=record_id,
    file_column_name="new_documentfile",
    file_path=file_path
)
print(f"Upload successful: {response}")
```

### 通过分块上传大文件
```python
from pathlib import Path

file_path = Path("large_video.mp4")
record_id = "account-guid"

# SDK automatically chunks large files
response = client.upload_file(
    table_name="account",
    record_id=record_id,
    file_column_name="new_videofile",
    file_path=file_path,
    chunk_size=4 * 1024 * 1024  # 4 MB chunks
)
print(f"Chunked upload complete")
```

---

## 10.OData过滤器优化

### 区分大小写规则
```python
# ❌ WRONG: Uppercase logical names
results = client.get("account", filter="Name eq 'Contoso'")

# ✅ CORRECT: Lowercase logical names
results = client.get("account", filter="name eq 'Contoso'")

# ✅ Values ARE case-sensitive when needed
results = client.get("account", filter="name eq 'Contoso Ltd'")
```

### 过滤表达式示例
```python
# Equality
client.get("account", filter="name eq 'Contoso'")

# Greater than / Less than
client.get("account", filter="creditlimit gt 50000")
client.get("account", filter="createdon lt 2024-01-01")

# String contains
client.get("account", filter="contains(name, 'Ltd')")

# AND/OR operations
client.get("account", filter="(name eq 'Contoso') and (creditlimit gt 50000)")
client.get("account", filter="(industrycode eq 1) or (industrycode eq 2)")

# NOT operation
client.get("account", filter="not(statecode eq 1)")
```

### 选择并展开
```python
# Select specific columns (improves performance)
client.get("account", select=["name", "creditlimit", "telephone1"])

# Expand related records
client.get(
    "account",
    expand=["parentaccountid($select=name)"],
    select=["name", "parentaccountid"]
)
```

---

## 11. 缓存管理

### 刷新缓存
```python
# Clear SDK internal cache after bulk operations
client.flush_cache()

# Useful after:
# - Metadata changes (table/column creation)
# - Bulk deletes
# - Metadata synchronization
```

---

## 12. 性能最佳实践

### 做的 ✅
1. **使用 `select` 参数**：仅获取需要的列
   ```python
   client.get("account", select=["name", "creditlimit"])
   ```

2. **批量操作**：一次创建/更新多条记录
   ```python
   ids = client.create("account", [record1, record2, record3])
   ```

3. **使用分页**：不要一次加载所有记录
   ```python
   for page in client.get("account", top=1000):
       process_page(page)
   ```

4. **重用客户端实例**：创建一次，使用多次
   ```python
   client = DataverseClient(url, credential)  # Once
   # Reuse throughout app
   ```

5. **在服务器上应用过滤器**：让 Dataverse 在返回之前进行过滤
   ```python
   client.get("account", filter="creditlimit gt 50000")
   ```

### 不该做的事❌
1. **不要获取所有列**：指定您需要的内容
   ```python
   # Slow
   client.get("account")
   ```

2. **不要在循环中创建记录**：对它们进行批处理
   ```python
   # Slow
   for record in records:
       client.create("account", record)
   ```

3. **不要一次加载所有结果**：使用分页
   ```python
   # Slow
   all_accounts = list(client.get("account"))
   ```

4. **不要重复创建新客户端**：重用单例
   ```python
   # Inefficient
   for i in range(100):
       client = DataverseClient(url, credential)
   ```

---

## 13. 常见模式总结

### 模式：Upsert（创建或更新）
```python
def upsert_account(name, data):
    """Create account or update if exists."""
    try:
        # Try to find existing
        results = list(client.get("account", filter=f"name eq '{name}'"))
        if results:
            account_id = results[0]['accountid']
            client.update("account", account_id, data)
            return account_id, "updated"
        else:
            ids = client.create("account", {"name": name, **data})
            return ids[0], "created"
    except Exception as e:
        print(f"Upsert failed: {e}")
        raise
```

### 模式：带有错误恢复的批量操作
```python
def create_with_recovery(records):
    """Create records with per-record error tracking."""
    results = {"success": [], "failed": []}
    
    try:
        ids = client.create("account", records)
        results["success"] = ids
    except Exception as e:
        # If bulk fails, try individual records
        for i, record in enumerate(records):
            try:
                ids = client.create("account", record)
                results["success"].append(ids[0])
            except Exception as e:
                results["failed"].append({"index": i, "record": record, "error": str(e)})
    
    return results
```

---

## 14. 依赖项和版本

### 核心依赖
- **azure-identity** >= 1.17.0（身份验证）
- **azure-core** >= 1.30.2（HTTP 客户端）
- **请求** >= 2.32.0（HTTP 请求）
- **Python** >= 3.10

### 可选依赖项
- **pandas**（数据操作）
- **reportlab**（文件示例的 PDF 生成）

### 开发工具
- **pytest** >= 7.0.0（测试）
- **黑色** >= 23.0.0（代码格式）
- **mypy** >= 1.0.0（类型检查）
- **皱褶** >= 0.1.0（掉毛）

---

## 15. 常见问题故障排除

### 导入错误：没有名为“PowerPlatform”的模块
```bash
# Verify installation
pip show PowerPlatform-Dataverse-Client

# Reinstall
pip install --upgrade PowerPlatform-Dataverse-Client

# Check virtual environment is activated
which python  # Should show venv path
```

### 认证失败
```python
# Verify credentials have Dataverse access
# Try interactive auth first for testing
from azure.identity import InteractiveBrowserCredential
credential = InteractiveBrowserCredential(
    tenant_id="your-tenant-id"  # Specify if multiple tenants
)

# Check org URL format
# ✓ https://yourorg.crm.dynamics.com
# ❌ https://yourorg.crm.dynamics.com/
# ❌ https://yourorg.crm4.dynamics.com (regional)
```

### HTTP 429 速率限制
```python
# Reduce request frequency
# Implement exponential backoff (see Error Handling section)
# Reduce page size
client.get("account", top=500)  # Instead of 5000
```

### 元数据错误：找不到表
```python
# Verify table exists (schema name is case-insensitive for existence, but case-sensitive for API)
tables = client.list_tables()
print([t['table_schema_name'] for t in tables])

# Use exact schema name
table_info = client.get_table_info("new_customprefixed_table")
```

### 未启用 SQL 查询
```python
# query_sql() requires org config
# If disabled, fallback to OData
try:
    results = client.query_sql("SELECT * FROM account")
except Exception:
    # Fallback to OData
    results = client.get("account")
```

---

## 参考链接
- [官方存储库](https://github.com/microsoft/PowerPlatform-DataverseClient-Python)
- [PyPI 包](https://pypi.org/project/PowerPlatform-Dataverse-Client/)
- [Azure 身份文档](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme)
- [Dataverse Web API 文档](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview)
