---
description: "使用 LangChain 与 Python 的说明"
applyTo: "**/*.py"
---

# LangChain Python 说明

这些说明指导 GitHub Copilot 为 Python 中的 LangChain 应用程序生成代码和文档。重点关注 LangChain 特定的模式、API 和最佳实践。

## 可运行接口 (LangChain 特定)

LangChain 的 `Runnable` 接口是组合和执行链、聊天模型、输出解析器、检索器和 LangGraph 图的基础。它提供统一的 API 来调用、批处理、流式传输、检查和组合组件。

**关键的 LangChain 特定功能：**

- 所有主要的 LangChain 组件（聊天模型、输出解析器、检索器、图形）都实现 Runnable 接口。
- 支持同步 (`invoke`, `batch`, `stream`) 和异步 (`ainvoke`, `abatch`, `astream`) 执行。
- 批处理 (`batch`, `batch_as_completed`) 为并行 API 调用进行了优化；在 `RunnableConfig` 中设置 `max_concurrency` 来控制并行性。
- 流式 API (`stream`, `astream`, `astream_events`) 在产生输出时生成输出，对响应式 LLM 应用程序至关重要。
- 输入/输出类型是组件特定的（例如，聊天模型接受消息，检索器接受字符串，输出解析器接受模型输出）。
- 使用 `get_input_schema`、`get_output_schema` 及其 JSONSchema 变体检查 schema，用于验证和 OpenAPI 生成。
- 使用 `with_types` 覆盖复杂 LCEL 链的推断输入/输出类型。
- 使用 LCEL 声明式组合 Runnables：`chain = prompt | chat_model | output_parser`。
- 在 Python 3.11+ 中自动传播 `RunnableConfig`（标签、元数据、回调、并发性）；在 Python 3.9/3.10 的异步代码中手动传播。
- 使用 `RunnableLambda`（简单转换）或 `RunnableGenerator`（流式转换）创建自定义 runnables；避免直接子类化。
- 使用 `configurable_fields` 和 `configurable_alternatives` 配置运行时属性和替代方案，用于动态链和 LangServe 部署。

**LangChain 最佳实践：**

- 使用批处理进行并行 LLM 或检索器 API 调用；设置 `max_concurrency` 以避免速率限制。
- 对于聊天 UI 和长输出，优先使用流式 API。
- 始终验证自定义链和部署端点的输入/输出 schema。
- 在 `RunnableConfig` 中使用标签和元数据进行 LangSmith 中的跟踪和调试复杂链。
- 对于自定义逻辑，将函数包装在 `RunnableLambda` 或 `RunnableGenerator` 中，而不是子类化。
- 对于高级配置，通过 `configurable_fields` 和 `configurable_alternatives` 公开字段和替代方案。

- 使用 LangChain 的聊天模型集成进行对话式 AI：

- 从 `langchain.chat_models` 或 `langchain_openai` 导入（例如，`ChatOpenAI`）。
- 使用 `SystemMessage`、`HumanMessage`、`AIMessage` 组合消息。
- 对于工具调用，使用 `bind_tools(tools)` 方法。
- 对于结构化输出，使用 `with_structured_output(schema)`。

示例：

```python
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(model="gpt-4", temperature=0)
messages = [
    SystemMessage(content="你是一个有用的助手。"),
    HumanMessage(content="什么是 LangChain？")
]
response = chat.invoke(messages)
print(response.content)
```

- 将消息组合为 `SystemMessage`、`HumanMessage` 和可选的 `AIMessage` 对象的列表。
- 对于 RAG，将聊天模型与检索器/向量存储结合以进行上下文注入。
- 使用 `streaming=True` 进行实时令牌流式传输（如果支持）。
- 使用 `tools` 参数进行函数/工具调用（OpenAI、Anthropic 等）。
- 使用 `response_format="json"` 进行结构化输出（OpenAI 模型）。

最佳实践：

- 在下游任务中使用模型输出之前始终验证它们。
- 为清晰性和可靠性优先使用显式消息类型。
- 对于 Copilot，提供清晰、可操作的提示并记录预期输出。

- LLM 客户端工厂：集中化提供程序配置（API 密钥）、超时、重试和遥测。提供单一位置来切换提供程序或客户端设置。
- 提示模板：将模板存储在 `prompts/` 下并通过安全帮助程序加载。保持模板小且可测试。
- 链 vs 代理：对于确定性管道（RAG、摘要），优先使用链。当需要规划或动态工具选择时使用代理。
- 工具：为工具实现类型化适配器接口；严格验证输入和输出。
- 内存：默认为无状态设计。当需要内存时，存储最小上下文并记录保留/擦除策略。
- 检索器：构建检索 + 重排序管道。保持向量存储 schema 稳定（id、文本、元数据）。

### 模式

- 回调和跟踪：使用 LangChain 回调并与 LangSmith 或您的跟踪系统集成以捕获请求/响应生命周期。
- 关注点分离：将提示构建、LLM 连接和业务逻辑分开，以简化测试并减少意外的提示更改。

## 嵌入和向量存储

- 使用一致的块分割和元数据字段（source、page、chunk_index）。
- 缓存嵌入以避免重复未更改文档的成本。
- 本地/开发：Chroma 或 FAISS。生产：根据规模和 SLA 选择托管向量数据库（Pinecone、Qdrant、Milvus、Weaviate）。

## 向量存储 (LangChain 特定)

- 使用 LangChain 的向量存储集成进行语义搜索、检索增强生成 (RAG) 和文档相似性工作流。
- 始终使用支持的嵌入模型初始化向量存储（例如，OpenAIEmbeddings、HuggingFaceEmbeddings）。
- 对于生产环境，优先使用官方集成（例如，Chroma、FAISS、Pinecone、Qdrant、Weaviate）；对于测试和演示使用 InMemoryVectorStore。
- 将文档存储为带有 `page_content` 和 `metadata` 的 LangChain `Document` 对象。
- 使用 `add_documents(documents, ids=...)` 添加/更新文档。始终提供唯一 ID 以进行 upserts。
- 使用 `delete(ids=...)` 按 ID 删除文档。
- 使用 `similarity_search(query, k=4, filter={...})` 检索前 k 个相似文档。使用元数据过滤器进行范围搜索。
- 对于 RAG，将您的向量存储连接到检索器并与 LLM 链接（参见 LangChain 检索器和 RAGChain 文档）。
- 对于高级搜索，使用向量存储特定的选项：Pinecone 支持混合搜索和元数据过滤；Chroma 支持过滤和自定义距离指标。
- 始终在您的环境中验证向量存储集成和 API 版本；LangChain 版本之间的破坏性更改很常见。
- 示例 (InMemoryVectorStore)：

```python
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

embedding_model = OpenAIEmbeddings()
vector_store = InMemoryVectorStore(embedding=embedding_model)

documents = [Document(page_content="LangChain 内容", metadata={"source": "doc1"})]
vector_store.add_documents(documents=documents, ids=["doc1"])

results = vector_store.similarity_search("什么是 RAG？", k=2)
for doc in results:
    print(doc.page_content, doc.metadata)
```

- 对于生产环境，优先使用持久向量存储（Chroma、Pinecone、Qdrant、Weaviate）并根据提供程序文档配置身份验证、扩展和备份。
- 参考：https://python.langchain.com/docs/integrations/vectorstores/

## 提示工程和治理

- 将规范提示存储在 `prompts/` 下，并通过文件名从代码中引用它们。
- 编写单元测试，断言必需的占位符存在，并且呈现的提示符合预期模式（长度、存在的变量）。
- 维护影响行为的提示和 schema 更改的 CHANGELOG。

## 聊天模型

LangChain 为聊天模型提供一致的接口，具有监控、调试和优化的附加功能。

### 集成

集成可以是：

1. 官方：由 LangChain 团队或提供程序维护的打包 `langchain-<provider>` 集成。
2. 社区：贡献的集成（在 `langchain-community` 中）。

聊天模型通常遵循带有 `Chat` 前缀的命名约定（例如，`ChatOpenAI`、`ChatAnthropic`、`ChatOllama`）。没有 `Chat` 前缀（或有 `LLM` 后缀）的模型通常实现较旧的字符串输入/字符串输出接口，对于现代聊天工作流不太受欢迎。

### 接口

聊天模型实现 `BaseChatModel` 并支持 Runnable 接口：流式传输、异步、批处理等。许多操作接受并返回 LangChain `messages`（角色如 `system`、`user`、`assistant`）。有关详细信息，请参阅 BaseChatModel API 参考。

关键方法包括：

- `invoke(messages, ...)` — 发送消息列表并接收响应。
- `stream(messages, ...)` — 随着令牌到达流式传输部分输出。
- `batch(inputs, ...)` — 批处理多个请求。
- `bind_tools(tools)` — 附加工具适配器以进行工具调用。
- `with_structured_output(schema)` — 请求结构化响应的帮助程序。

### 输入和输出

- LangChain 支持自己的消息格式和 OpenAI 的消息格式；在您的代码库中一致地选择一种。
- 消息包括 `role` 和 `content` 块；在支持的地方，内容可以包括结构化或多模态负载。

### 标准参数

通常支持的参数（取决于提供程序）：

- `model`：模型标识符（例如，`gpt-4o`、`gpt-3.5-turbo`）。
- `temperature`：随机性控制（0.0 确定性 — 1.0 创造性）。
- `timeout`：取消前等待的秒数。
- `max_tokens`：响应令牌限制。
- `stop`：停止序列。
- `max_retries`：网络/限制失败的重试尝试。
- `api_key`、`base_url`：提供程序身份验证和端点配置。
- `rate_limiter`：可选的 BaseRateLimiter，用于间隔请求并避免提供程序配额错误。

> 注意：并非所有提供程序都实现了所有参数。始终查阅提供程序集成文档。

### 工具调用

聊天模型可以调用工具（API、数据库、系统适配器）。使用 LangChain 的工具调用 API 来：

- 使用严格的输入/输出类型注册工具。
- 观察和记录工具调用请求和结果。
- 在将它们传递回模型或执行副作用之前验证工具输出。

有关示例和安全模式，请参阅 LangChain 文档中的工具调用指南。

### 结构化输出

使用 `with_structured_output` 或 schema 强制方法从模型请求 JSON 或类型化输出。结构化输出对于可靠提取和下游处理（解析器、数据库写入、分析）至关重要。

### 多模态

某些模型支持多模态输入（图像、音频）。检查提供程序文档以了解支持的输入类型和限制。多模态输出很少见 — 将它们视为实验性并严格验证。

### 上下文窗口

模型具有以令牌为单位的有限上下文窗口。在设计对话流时：

- 保持消息简洁并优先考虑重要上下文。
- 当超过窗口时，在模型外部修剪旧上下文（总结或存档）。
- 使用检索器 + RAG 模式来显示相关的长格式上下文，而不是将大文档粘贴到聊天中。

## 高级主题

### 速率限制

- 在初始化聊天模型时使用 `rate_limiter` 来间隔调用。
- 实现指数退避重试，并在受到限制时考虑回退模型或降级模式。

### 缓存

- 对话的精确输入缓存通常无效。考虑语义缓存（基于嵌入）进行重复的语义级查询。
- 语义缓存引入对嵌入的依赖，并非普遍适用。
- 仅在减少成本并满足正确性要求的地方缓存（例如，FAQ 机器人）。

## 最佳实践

- 为公共 API 使用类型提示和数据类。
- 在调用 LLM 或工具之前验证输入。
- 从机密管理器加载机密；从不记录机密或未编辑的模型输出。
- 确定性测试：模拟 LLM 和嵌入调用。
- 缓存嵌入和频繁的检索结果。
- 可观察性：记录 request_id、模型名称、延迟和清理的令牌计数。
- 为外部调用实现指数退避和幂等性。

## 安全和隐私

- 将模型输出视为不可信。在执行生成的代码或系统命令之前进行清理。
- 验证任何用户提供的 URL 和输入，以避免 SSRF 和注入攻击。
- 记录数据保留并添加 API 以根据请求擦除用户数据。
- 限制存储的 PII 并在静态时加密敏感字段。
