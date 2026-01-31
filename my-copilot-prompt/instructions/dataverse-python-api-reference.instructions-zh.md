---
适用于：'**'
---
# 适用于 Python 的 Dataverse SDK — API 参考指南

## DataverseClient类
与 Dataverse 交互的主要客户端。使用基本 URL 和 Azure 凭据进行初始化。

### 关键方法

#### 创建（表架构名称，记录）
创建单个或批量记录。返回 GUID 列表。

```python
# Single record
ids = client.create("account", {"name": "Acme"})
print(ids[0])  # First GUID

# Bulk create
ids = client.create("account", [{"name": "Contoso"}, {"name": "Fabrikam"}])
```

#### get(table_schema_name, record_id=None, 选择, 过滤器, orderby, 顶部, 展开, page_size)
使用 OData 选项获取单个记录或查询多个记录。

```python
# Single record
record = client.get("account", record_id="guid-here")

# Query with filter and paging
for batch in client.get(
    "account",
    filter="statecode eq 0",
    select=["name", "telephone1"],
    orderby=["createdon desc"],
    top=100,
    page_size=50
):
    for record in batch:
        print(record["name"])
```

#### 更新（表架构名称、ID、更改）
更新单个或批量记录。

```python
# Single update
client.update("account", "guid-here", {"telephone1": "555-0100"})

# Broadcast: apply same changes to many IDs
client.update("account", [id1, id2, id3], {"statecode": 1})

# Paired: one-to-one mapping
client.update("account", [id1, id2], [{"name": "A"}, {"name": "B"}])
```

#### 删除（表架构名称，ids，use_bulk_delete = True）
删除单个或批量记录。

```python
# Single delete
client.delete("account", "guid-here")

# Bulk delete (async)
job_id = client.delete("account", [id1, id2, id3])
```

#### create_table(table_schema_name、列、solution_unique_name=无、primary_column_schema_name=无)
创建自定义表。

```python
from enum import IntEnum

class ItemStatus(IntEnum):
    ACTIVE = 1
    INACTIVE = 2
    __labels__ = {
        1033: {"ACTIVE": "Active", "INACTIVE": "Inactive"}
    }

info = client.create_table("new_MyTable", {
    "new_Title": "string",
    "new_Quantity": "int",
    "new_Price": "decimal",
    "new_Active": "bool",
    "new_Status": ItemStatus
})
print(info["entity_logical_name"])
```

#### 创建列（表架构名称，列）
将列添加到现有表。

```python
created = client.create_columns("new_MyTable", {
    "new_Notes": "string",
    "new_Count": "int"
})
```

#### 删除列（表架构名称，列）
从表中删除列。

```python
removed = client.delete_columns("new_MyTable", ["new_Notes", "new_Count"])
```

#### 删除表（表架构名称）
删除自定义表（不可逆）。

```python
client.delete_table("new_MyTable")
```

#### 获取表信息（表架构名称）
检索表元数据。

```python
info = client.get_table_info("new_MyTable")
if info:
    print(info["table_logical_name"])
    print(info["entity_set_name"])
```

#### 列表_表()
列出所有自定义表。

```python
tables = client.list_tables()
for table in tables:
    print(table)
```

#### 刷新缓存（种类）
清除 SDK 缓存（例如选项列表标签）。

```python
removed = client.flush_cache("picklist")
```

## DataverseConfig类
配置客户端行为（超时、重试、语言）。

```python
from PowerPlatform.Dataverse.core.config import DataverseConfig

cfg = DataverseConfig()
cfg.http_retries = 3
cfg.http_backoff = 1.0
cfg.http_timeout = 30
cfg.language_code = 1033  # English

client = DataverseClient(base_url=url, credential=cred, config=cfg)
```

## 错误处理
捕获 `DataverseError` 以获取 SDK 特定的异常。检查 `is_transient` 来决定重试。

```python
from PowerPlatform.Dataverse.core.errors import DataverseError

try:
    client.create("account", {"name": "Test"})
except DataverseError as e:
    print(f"Code: {e.code}")
    print(f"Message: {e.message}")
    print(f"Transient: {e.is_transient}")
    print(f"Details: {e.to_dict()}")
```

## OData 过滤器提示
- 在过滤器表达式中使用精确的逻辑名称（小写）
- `select` 中的列名称自动小写
- `expand` 中的导航属性名称区分大小写

## 参考文献
- API 文档：https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/powerplatform.dataverse.client.dataverseclient
- 配置文档：https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/powerplatform.dataverse.core.config.dataverseconfig
- 错误：https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/powerplatform.dataverse.core.errors
