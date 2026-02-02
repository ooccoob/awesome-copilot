---
applyTo: '**'
---
# Dataverse SDK for Python — 完整模块参考

## 包层次结构

```
PowerPlatform.Dataverse
├── client
│   └── DataverseClient
├── core
│   ├── config (DataverseConfig)
│   └── errors (DataverseError, ValidationError, MetadataError, HttpError, SQLParseError)
├── data (OData operations, metadata, SQL, file upload)
├── extensions (placeholder for future extensions)
├── models (placeholder for data models and types)
└── utils (placeholder for utilities and adapters)
```

## core.config 模块

管理客户端连接和行为设置。

### DataverseConfig类

语言、超时、重试的容器。不变的。

```python
from PowerPlatform.Dataverse.core.config import DataverseConfig

cfg = DataverseConfig(
    language_code=1033,        # Default English (US)
    http_retries=None,         # Reserved for future
    http_backoff=None,         # Reserved for future
    http_timeout=None          # Reserved for future
)

# Or use default static builder
cfg_default = DataverseConfig.from_env()
```

**关键属性：**
- `language_code: int = 1033` — 本地化标签和消息的 LCID。
- `http_retries: int | None` —（保留）暂时性错误的最大重试次数。
- `http_backoff: float | None` —（保留）重试之间的退避乘数。
- `http_timeout: float | None` —（保留）请求超时（以秒为单位）。

## core.errors 模块

SDK 操作的结构化异常层次结构。

### 数据空间错误（基础）

SDK 错误的基本异常。

```python
from PowerPlatform.Dataverse.core.errors import DataverseError

try:
    # SDK call
    pass
except DataverseError as e:
    print(f"Code: {e.code}")                # Error category
    print(f"Subcode: {e.subcode}")          # Specific error
    print(f"Message: {e.message}")          # Human-readable
    print(f"Status: {e.status_code}")       # HTTP status (if applicable)
    print(f"Transient: {e.is_transient}")   # Retry-worthy?
    details = e.to_dict()                  # Convert to dict
```

### 验证错误

数据操作期间验证失败。

```python
from PowerPlatform.Dataverse.core.errors import ValidationError
```

### 元数据错误

表/列创建、删除或检查失败。

```python
from PowerPlatform.Dataverse.core.errors import MetadataError

try:
    client.create_table("MyTable", {...})
except MetadataError as e:
    print(f"Metadata issue: {e.message}")
```

### Http错误

Web API HTTP 请求失败（4xx、5xx 等）。

```python
from PowerPlatform.Dataverse.core.errors import HttpError

try:
    client.get("account", record_id)
except HttpError as e:
    print(f"HTTP {e.status_code}: {e.message}")
    print(f"Service error code: {e.service_error_code}")
    print(f"Correlation ID: {e.correlation_id}")
    print(f"Request ID: {e.request_id}")
    print(f"Retry-After: {e.retry_after} seconds")
    print(f"Transient (retry?): {e.is_transient}")  # 429, 503, 504
```

### SQL解析错误

使用 `query_sql()` 时 SQL 查询语法错误。

```python
from PowerPlatform.Dataverse.core.errors import SQLParseError

try:
    client.query_sql("INVALID SQL HERE")
except SQLParseError as e:
    print(f"SQL parse error: {e.message}")
```

## 数据包

低级 OData 协议、元数据、SQL 和文件操作（内部委托）。

`data` 包主要是内部的； `client` 模块中的高级 `DataverseClient` 包装并公开：
- 通过 OData 进行 CRUD 操作
- 元数据管理（创建/更新/删除表和列）
- SQL查询执行
- 文件上传处理

用户通过 `DataverseClient` 方法（例如 `create()`、`get()`、`update()`、`delete()`、`create_table()`、`query_sql()`、`upload_file()`）与这些方法进行交互。

## 扩展包（占位符）

为未来的扩展点（例如自定义适配器、中间件）保留。

目前为空；使用核心和客户端模块来实现当前功能。

## 模型包（占位符）

保留用于未来的数据模型定义和类型定义。

目前空着。数据结构返回为 `dict` (OData) 并且是 JSON 可序列化的。

## utils 包（占位符）

保留给实用程序适配器和助手。

目前空着。未来版本中可能会添加辅助功能。

## 客户端模块

主要面向用户的 API。

### DataverseClient类

所有 Dataverse 操作的高级客户端。

```python
from azure.identity import InteractiveBrowserCredential
from PowerPlatform.Dataverse.client import DataverseClient
from PowerPlatform.Dataverse.core.config import DataverseConfig

# Create credential
credential = InteractiveBrowserCredential()

# Optionally configure
cfg = DataverseConfig(language_code=1033)

# Create client
client = DataverseClient(
    base_url="https://org.crm.dynamics.com",
    credential=credential,
    config=cfg  # optional
)
```

#### 增删改查方法

- `create(table_schema_name, records)` → `list[str]` — 创建记录，返回 GUID。
- `get(table_schema_name, record_id=None, select, filter, orderby, top, expand, page_size)` → 记录。
- `update(table_schema_name, ids, changes)` → `None` — 更新记录。
- `delete(table_schema_name, ids, use_bulk_delete=True)` → `str | None` — 删除记录。

#### 元数据方法

- `create_table(table_schema_name, columns, solution_unique_name, primary_column_schema_name)` → 元数据字典。
- __代码0__ → __代码1__。
- __代码0__ → __代码1__。
- __代码0__ → __代码1__。
- `get_table_info(table_schema_name)` → 元数据字典或 `None`。
- __代码0__ → __代码1__。

#### SQL 和实用程序

- `query_sql(sql)` → `list[dict]` — 执行只读 SQL。
- `upload_file(table_schema_name, record_id, file_name_attribute, path, mode, mime_type, if_none_match)` → `None` — 上传到文件列。
- `flush_cache(kind)` → `int` — 清除 SDK 缓存（例如 `"picklist"`）。

## 进口摘要

```python
# Main client
from PowerPlatform.Dataverse.client import DataverseClient

# Configuration
from PowerPlatform.Dataverse.core.config import DataverseConfig

# Errors
from PowerPlatform.Dataverse.core.errors import (
    DataverseError,
    ValidationError,
    MetadataError,
    HttpError,
    SQLParseError,
)
```

## 参考文献

- 模块文档：https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/
- 核心：https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/powerplatform.dataverse.core
- 数据：https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/powerplatform.dataverse.data
- 扩展：https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/powerplatform.dataverse.extensions
- 模型：https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/powerplatform.dataverse.models
- 实用程序：https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/powerplatform.dataverse.utils
- 客户端：https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/powerplatform.dataverse.client
