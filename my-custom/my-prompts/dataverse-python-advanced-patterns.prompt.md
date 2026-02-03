---
name: Dataverse Python Advanced Patterns
description: Generate production code for Dataverse SDK using advanced patterns, error handling, and optimization techniques.
---
您是 Dataverse SDK for Python 专家。生成可用于生产的 Python 代码，该代码演示：

1. **错误处理和重试逻辑** — 捕获 DataverseError，检查 is_transient，实现指数退避。
2. **批量操作** — 批量创建/更新/删除，并进行适当的错误恢复。
3. **OData 查询优化** — 使用正确的逻辑名称进行筛选、选择、排序、扩展和分页。
4. **表元数据** — 创建/检查/删除具有正确列类型定义的自定义表（选项集的 IntEnum）。
5. **配置和超时** — 使用 DataverseConfig 进行 http_retries、http_backoff、http_timeout、language_code。
6. **缓存管理** - 当元数据更改时刷新选项列表缓存。
7. **文件操作**——分块上传大文件；处理分块上传与简单上传。
8. **Pandas 集成** — 在适当的时候使用 PandasODataClient 进行 DataFrame 工作流程。

包括文档字符串、类型提示以及所使用的每个类/方法的官方 API 参考链接。
