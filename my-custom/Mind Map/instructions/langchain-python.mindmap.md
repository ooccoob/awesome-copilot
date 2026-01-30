## What/When/Why/How
- What: 使用 LangChain(Python) 构建链/图/检索/RAG/聊天模型的可组合应用，围绕 Runnable 接口与 LCEL。
- When: 需要批处理/流式/异步、结构化输出、工具调用与可观测的 LLM 应用时。
- Why: 统一可组合抽象、强大执行与调试接口、丰富集成生态。
- How: 以 Runnable 为核心组合（prompt|model|parser），利用 batch/stream/async、schema 校验与配置化切换。

## Key Points
- Runnable：invoke/batch/stream 与 ainvoke/abatch/astream；max_concurrency 控并发。
- Streaming：stream/astream/astream_events 提升交互体验。
- 组合：LCEL 管道 + RunnableLambda/Generator 自定义，with_types 与 configurable_*。
- Schema：get_input/output_schema；with_structured_output；OpenAPI/校验。
- 聊天模型：ChatOpenAI 等；System/Human/AI messages；bind_tools；response_format。
- RAG：Retriever + VectorStore；向量库（Chroma/FAISS/Pinecone 等）初始化与过滤。
- 向量：Document{id,text,metadata}；add_documents/upsert/delete/similarity_search。
- 工程：客户端工厂、提示模板管理、回调与 LangSmith 追踪、速率限制/重试。
- 测试：模拟 LLM 与嵌入以实现确定性单测；缓存嵌入。
- 安全：输出不可信、URL/命令验证、最小化敏感数据持久化。

## Compact Map
LangChain Py
- Runnable/LCEL
- Chat Models/Tools
- Schema/Structured
- RAG/VectorStores
- Streaming/Async
- Tracing/Rate-limit

## Checklist
- [ ] 为关键 chain 声明输入/输出 schema
- [ ] 使用 batch 并设 max_concurrency
- [ ] UI 采用 streaming 增强响应
- [ ] 工具调用输入输出严格校验
- [ ] 嵌入与检索缓存
- [ ] 单测模拟 LLM/Embeddings

## Example Questions (≥10)
- 如何把 prompt|model|parser 组合为可复用链？
- 如何用 batch_as_completed 管理大量并发调用？
- astream 与 astream_events 在前端 UI 的差异与使用场景？
- with_structured_output 如何定义并验证 JSON 输出？
- 如何实现工具调用并校验结果后再反馈模型？
- 向量库如何做分区与 metadata 过滤？
- 如何在 LangSmith 中追踪并定位慢链路？
- 何时使用 RunnableGenerator 而非自定义子类？
- 如何在 Python 3.9/3.10 传播 RunnableConfig？
- 生产上如何处理速率限制与重试退避？

Source: d:\mycode\awesome-copilot\instructions\langchain-python.instructions.md | Generated: 2025-10-17
