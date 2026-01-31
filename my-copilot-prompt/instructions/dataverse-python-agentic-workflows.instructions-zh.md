# Dataverse SDK for Python - 代理工作流程指南

## ⚠️预览功能通知

**状态**：截至 2025 年 12 月，此功能处于 **公共预览版**  
**上市**：全面上市 (GA) 日期待定  
**文档**：完整的实施细节即将发布  

本指南涵盖了使用 Dataverse SDK for Python 构建代理工作流的概念框架和计划功能。在正式发布之前，特定的 API 和实现可能会发生变化。

---

## 1. 概述：Dataverse 的代理工作流程

### 什么是代理工作流程？

代理工作流程是自主、智能的流程，其中：
- **代理**根据数据和规则做出决策并采取行动
- **工作流程**编排复杂的多步骤操作
- **Dataverse** 是企业数据的中心事实来源

Dataverse SDK for Python 旨在帮助数据科学家和开发人员无需 .NET 专业知识即可构建这些智能系统。

### 关键能力（计划）

SDK 的战略定位是支持：

1. **自主数据代理** - 独立查询、更新和评估数据质量
2. **表单预测和自动填充** - 根据数据模式和上下文预填写表单
3. **模型上下文协议 (MCP)** 支持 - 启用标准化代理到工具通信
4. **代理对代理 (A2A)** 协作 - 多个代理共同完成复杂的任务
5. **语义建模** - 数据关系的自然语言理解
6. **安全模拟** - 代表特定用户运行操作并进行审计跟踪
7. **内置合规性** - 强制执行数据治理和保留策略

---

## 2. 代理系统的架构模式

### 多代理模式
```python
# Conceptual pattern - specific APIs pending GA
class DataQualityAgent:
    """Autonomous agent that monitors and improves data quality."""
    
    def __init__(self, client):
        self.client = client
    
    async def evaluate_data_quality(self, table_name):
        """Evaluate data quality metrics for a table."""
        records = await self.client.get(table_name)
        
        metrics = {
            'total_records': len(records),
            'null_values': sum(1 for r in records if None in r.values()),
            'duplicate_records': await self._find_duplicates(table_name)
        }
        return metrics
    
    async def auto_remediate(self, issues):
        """Automatically fix identified data quality issues."""
        # Agent autonomously decides on remediation actions
        pass

class DataEnrichmentAgent:
    """Autonomous agent that enriches data from external sources."""
    
    async def enrich_accounts(self):
        """Enrich account data with market information."""
        accounts = await self.client.get("account")
        
        for account in accounts:
            enrichment = await self._lookup_market_data(account['name'])
            await self.client.update("account", account['id'], enrichment)
```

### 代理编排模式
```python
# Conceptual pattern - specific APIs pending GA
class DataPipeline:
    """Orchestrates multiple agents working together."""
    
    def __init__(self, client):
        self.quality_agent = DataQualityAgent(client)
        self.enrichment_agent = DataEnrichmentAgent(client)
        self.sync_agent = SyncAgent(client)
    
    async def run(self, table_name):
        """Execute multi-agent workflow."""
        # Step 1: Quality check
        print("Running quality checks...")
        issues = await self.quality_agent.evaluate_data_quality(table_name)
        
        # Step 2: Enrich data
        print("Enriching data...")
        await self.enrichment_agent.enrich_accounts()
        
        # Step 3: Sync to external systems
        print("Syncing to external systems...")
        await self.sync_agent.sync_to_external_db(table_name)
```

---

## 3.模型上下文协议（MCP）支持（计划中）

### 什么是MCP？

模型上下文协议 (MCP) 是一个开放标准，用于：
- **工具定义** - 描述可用的工具/功能
- **工具调用** - 允许法学硕士使用参数调用工具
- **上下文管理** - 管理代理和工具之间的上下文
- **错误处理** - 标准化错误响应

### MCP 集成模式（概念）

```python
# Conceptual pattern - specific APIs pending GA
from dataverse_mcp import DataverseMCPServer

# Define available tools
tools = [
    {
        "name": "query_accounts",
        "description": "Query accounts with filters",
        "parameters": {
            "filter": "OData filter expression",
            "select": "Columns to retrieve",
            "top": "Maximum records"
        }
    },
    {
        "name": "create_account",
        "description": "Create a new account",
        "parameters": {
            "name": "Account name",
            "credit_limit": "Credit limit amount"
        }
    },
    {
        "name": "update_account",
        "description": "Update account fields",
        "parameters": {
            "account_id": "Account GUID",
            "updates": "Dictionary of field updates"
        }
    }
]

# Create MCP server
server = DataverseMCPServer(client, tools=tools)

# LLMs can now use Dataverse tools
await server.handle_tool_call("query_accounts", {
    "filter": "creditlimit gt 100000",
    "select": ["name", "creditlimit"]
})
```

---

## 4. 代理对代理 (A2A) 协作（计划中）

### A2A沟通模式

```python
# Conceptual pattern - specific APIs pending GA
class DataValidationAgent:
    """Validates data before downstream agents process it."""
    
    async def validate_and_notify(self, data):
        """Validate data and notify other agents."""
        if await self._is_valid(data):
            # Publish event that other agents can subscribe to
            await self.publish_event("data_validated", data)
        else:
            await self.publish_event("validation_failed", data)

class DataProcessingAgent:
    """Waits for valid data from validation agent."""
    
    async def __init__(self):
        self.subscribe("data_validated", self.process_data)
    
    async def process_data(self, data):
        """Process already-validated data."""
        # Agent can safely assume data is valid
        result = await self._transform(data)
        await self.publish_event("processing_complete", result)
```

---

## 5. 构建自治数据代理

### 数据质量代理示例
```python
# Working example with current SDK features
from PowerPlatform.Dataverse.client import DataverseClient
from azure.identity import InteractiveBrowserCredential
import json

class DataQualityAgent:
    """Monitor and report on data quality."""
    
    def __init__(self, org_url, credential):
        self.client = DataverseClient(org_url, credential)
    
    def analyze_completeness(self, table_name, required_fields):
        """Analyze field completeness."""
        records = self.client.get(
            table_name,
            select=required_fields
        )
        
        missing_by_field = {field: 0 for field in required_fields}
        total = 0
        
        for page in records:
            for record in page:
                total += 1
                for field in required_fields:
                    if field not in record or record[field] is None:
                        missing_by_field[field] += 1
        
        # Calculate completeness percentage
        completeness = {
            field: ((total - count) / total * 100) 
            for field, count in missing_by_field.items()
        }
        
        return {
            'table': table_name,
            'total_records': total,
            'completeness': completeness,
            'missing_counts': missing_by_field
        }
    
    def detect_duplicates(self, table_name, key_fields):
        """Detect potential duplicate records."""
        records = self.client.get(table_name, select=key_fields)
        
        all_records = []
        for page in records:
            all_records.extend(page)
        
        seen = {}
        duplicates = []
        
        for record in all_records:
            key = tuple(record.get(f) for f in key_fields)
            if key in seen:
                duplicates.append({
                    'original_id': seen[key],
                    'duplicate_id': record.get('id'),
                    'key': key
                })
            else:
                seen[key] = record.get('id')
        
        return {
            'table': table_name,
            'duplicate_count': len(duplicates),
            'duplicates': duplicates
        }
    
    def generate_quality_report(self, table_name):
        """Generate comprehensive quality report."""
        completeness = self.analyze_completeness(
            table_name,
            ['name', 'telephone1', 'emailaddress1']
        )
        
        duplicates = self.detect_duplicates(
            table_name,
            ['name', 'emailaddress1']
        )
        
        return {
            'timestamp': pd.Timestamp.now().isoformat(),
            'table': table_name,
            'completeness': completeness,
            'duplicates': duplicates
        }

# Usage
client = DataverseClient("https://<org>.crm.dynamics.com", InteractiveBrowserCredential())
agent = DataQualityAgent("https://<org>.crm.dynamics.com", InteractiveBrowserCredential())

report = agent.generate_quality_report("account")
print(json.dumps(report, indent=2))
```

### 形态预测代理示例
```python
# Conceptual pattern using current SDK capabilities
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

class FormPredictionAgent:
    """Predict and autofill form values."""
    
    def __init__(self, org_url, credential):
        self.client = DataverseClient(org_url, credential)
        self.model = None
    
    def train_on_historical_data(self, table_name, features, target):
        """Train prediction model on historical data."""
        # Collect training data
        records = []
        for page in self.client.get(table_name, select=features + [target]):
            records.extend(page)
        
        df = pd.DataFrame(records)
        
        # Train model
        X = df[features].fillna(0)
        y = df[target]
        
        self.model = RandomForestRegressor()
        self.model.fit(X, y)
        
        return self.model.score(X, y)
    
    def predict_field_values(self, table_name, record_id, features_data):
        """Predict missing field values."""
        if self.model is None:
            raise ValueError("Model not trained. Call train_on_historical_data first.")
        
        # Predict
        prediction = self.model.predict([features_data])[0]
        
        # Return prediction with confidence
        return {
            'record_id': record_id,
            'predicted_value': prediction,
            'confidence': self.model.score([features_data], [prediction])
        }
```

---

## 6. 与 AI/ML 服务集成

### LLM整合模式
```python
# Using LLM to interpret Dataverse data
from openai import OpenAI

class DataInsightAgent:
    """Use LLM to generate insights from Dataverse data."""
    
    def __init__(self, org_url, credential, openai_key):
        self.client = DataverseClient(org_url, credential)
        self.llm = OpenAI(api_key=openai_key)
    
    def analyze_with_llm(self, table_name, sample_size=100):
        """Analyze data using LLM."""
        # Get sample data
        records = []
        count = 0
        for page in self.client.get(table_name):
            records.extend(page)
            count += len(page)
            if count >= sample_size:
                break
        
        # Create summary for LLM
        summary = f"""
        Table: {table_name}
        Total records sampled: {len(records)}
        
        Sample data:
        {json.dumps(records[:5], indent=2, default=str)}
        
        Provide insights about this data.
        """
        
        # Ask LLM
        response = self.llm.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": summary}]
        )
        
        return response.choices[0].message.content
```

---

## 7. 安全模拟和审计跟踪

### 计划能力

SDK将支持代表特定用户运行操作：

```python
# Conceptual pattern - specific APIs pending GA
from dataverse_security import ImpersonationContext

# Run as different user
with ImpersonationContext(client, user_id="user-guid"):
    # All operations run as this user
    client.create("account", {"name": "New Account"})
    # Audit trail: Created by [user-guid] at [timestamp]

# Retrieve audit trail
audit_log = client.get_audit_trail(
    table="account",
    record_id="record-guid",
    action="create"
)
```

---

## 8. 合规性和数据治理

### 计划性治理特点

```python
# Conceptual pattern - specific APIs pending GA
from dataverse_governance import DataGovernance

# Define retention policy
governance = DataGovernance(client)
governance.set_retention_policy(
    table="account",
    retention_days=365
)

# Define data classification
governance.classify_columns(
    table="account",
    classifications={
        "name": "Public",
        "telephone1": "Internal",
        "creditlimit": "Confidential"
    }
)

# Enforce policies
governance.enforce_all_policies()
```

---

## 9. 当前支持代理工作流程的 SDK 功能

虽然完整的代理功能处于预览状态，但当前的 SDK 功能已经支持代理构建：

### ✅ 现已上市
- **CRUD 操作** - 创建、检索、更新、删除数据
- **批量操作** - 高效处理大型数据集
- **查询功能** - OData 和 SQL 用于灵活的数据检索
- **元数据操作** - 使用表和列定义
- **错误处理** - 结构化异常层次结构
- **分页** - 处理大型结果集
- **文件上传** - 管理文档附件

### 🔜 即将到来
- 完整的 MCP 集成
- A2A 协作原语
- 增强的身份验证/模拟
- 治理政策执行
- 本机异步/等待支持
- 高级缓存策略

---

## 10. 开始：立即构建您的第一个代理

```python
from PowerPlatform.Dataverse.client import DataverseClient
from azure.identity import InteractiveBrowserCredential
import json

class SimpleDataAgent:
    """Your first Dataverse agent."""
    
    def __init__(self, org_url):
        credential = InteractiveBrowserCredential()
        self.client = DataverseClient(org_url, credential)
    
    def check_health(self, table_name):
        """Agent function: Check table health."""
        try:
            tables = self.client.list_tables()
            matching = [t for t in tables if t['LogicalName'] == table_name]
            
            if not matching:
                return {"status": "error", "message": f"Table {table_name} not found"}
            
            # Get record count
            records = []
            for page in self.client.get(table_name):
                records.extend(page)
                if len(records) > 1000:
                    break
            
            return {
                "status": "healthy",
                "table": table_name,
                "record_count": len(records),
                "timestamp": pd.Timestamp.now().isoformat()
            }
        
        except Exception as e:
            return {"status": "error", "message": str(e)}

# Usage
agent = SimpleDataAgent("https://<org>.crm.dynamics.com")
health = agent.check_health("account")
print(json.dumps(health, indent=2))
```

---

## 11. 资源和文档

### 官方文档
- [Dataverse SDK for Python 概述](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/sdk-python/overview)
- [处理数据](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/sdk-python/work-data)
- [发布计划：代理工作流程](https://learn.microsoft.com/en-us/power-platform/release-plan/2025wave2/data-platform/build-agentic-flows-dataverse-sdk-python)

### 外部资源
- [模型上下文协议](https://modelcontextprotocol.io/)
- [Azure 人工智能服务](https://learn.microsoft.com/en-us/azure/ai-services/)
- [Python 异步/等待](https://docs.python.org/3/library/asyncio.html)

### 存储库
- [SDK源码](https://github.com/microsoft/PowerPlatform-DataverseClient-Python)
- [问题和功能请求](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/issues)

---

## 12. 常见问题解答：代理工作流程

**问：我现在可以通过当前的 SDK 使用代理吗？**  
答：是的！使用当前的功能来构建类似代理的系统。 GA 中将提供全面的 MCP/A2A 支持。

**问：当前的 SDK 和代理功能有什么区别？**  
A：当前：同步CRUD； Agentic：异步、自主决策、代理协作。

**问：从预览版到正式版会有重大变化吗？**  
答：有可能。这是预览功能；预计在正式发布之前 API 会得到改进。

**问：今天我如何为代理工作流程做好准备？**  
答：使用当前的 CRUD 操作构建代理，设计时考虑异步模式，使用 MCP 规范来实现未来的兼容性。

**问：代理功能有成本差异吗？**  
答：目前未知。检查接近 GA 的发行说明。

---

## 13. 后续步骤

1. **使用当前 SDK 功能构建原型**
2. **当 MCP 集成可用时加入预览**
3. **通过 GitHub 问题提供反馈**
4. **关注 GA 公告**以及完整的 API 文档
5. **准备好后迁移到完整的代理**功能

Dataverse SDK for Python 将自己定位为在 Microsoft Power Platform 上构建智能、自主数据系统的首选平台。
