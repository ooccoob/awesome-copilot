---
name: microsoft-code-reference
description: Look up Microsoft API references, find working code samples, and verify SDK code is correct. Use when working with Azure SDKs, .NET libraries, or Microsoft APIs—to find the right method, check parameters, get working examples, or troubleshoot errors. Catches hallucinated methods, wrong signatures, and deprecated patterns by querying official docs.
compatibility: Requires Microsoft Learn MCP Server (https://learn.microsoft.com/api/mcp)
---

# 微软代码参考

## 工具

|需要|工具|示例|
|------|------|---------|
| API 方法/类查找 | __代码0__ | __代码1__ |
|工作代码示例 | __代码0__ | __代码1__ |
|完整 API 参考 | __代码0__ |从 `microsoft_docs_search` 获取 URL（用于重载、完整签名）|

## 查找代码示例

使用 `microsoft_code_sample_search` 获取官方的工作示例：

```
microsoft_code_sample_search(query: "upload file to blob storage", language: "csharp")
microsoft_code_sample_search(query: "authenticate with managed identity", language: "python")
microsoft_code_sample_search(query: "send message service bus", language: "javascript")
```

**何时使用：**
- 在编写代码之前——找到要遵循的工作模式
- 出现错误后——将您的代码与已知良好的示例进行比较
- 不确定初始化/设置 - 示例显示完整的上下文

## API 查询

```
# Verify method exists (include namespace for precision)
"BlobClient UploadAsync Azure.Storage.Blobs"
"GraphServiceClient Users Microsoft.Graph"

# Find class/interface
"DefaultAzureCredential class Azure.Identity"

# Find correct package
"Azure Blob Storage NuGet package"
"azure-storage-blob pip package"
```

当方法有多个重载或者您需要完整的参数详细信息时，获取完整页面。

## 错误故障排除

使用 `microsoft_code_sample_search` 查找工作代码示例并与您的实现进行比较。对于特定错误，请使用 `microsoft_docs_search` 和 `microsoft_docs_fetch`：

|错误类型|查询 |
|------------|-------|
|未找到方法 | __代码0__ |
|未找到类型 | __代码0__ |
|签名错误 | `"[ClassName] [MethodName] overloads"` → 获取整页 |
|已弃用警告 | __代码0__ |
|验证失败 | __代码0__ |
| 403 禁止__代码0__ |

## 何时验证

始终验证以下情况：
- 方法名称似乎“太方便”（`UploadFile` 与实际的 `Upload`）
- 混合 SDK 版本（v11 `CloudBlobClient` 与 v12 `BlobServiceClient`）
- 包名称不遵循约定（.NET 为 `Azure.*`，Python 为 `azure-*`）
- 第一次使用API

## 验证工作流程

在使用 Microsoft SDK 生成代码之前，请验证其是否正确：

1. **确认方法或包存在** — `microsoft_docs_search(query: "[ClassName] [MethodName] [Namespace]")`
2. **获取完整详细信息**（用于重载/复杂参数）— `microsoft_docs_fetch(url: "...")`
3. **查找工作示例** — `microsoft_code_sample_search(query: "[task]", language: "[lang]")`

对于简单的查找，仅步骤 1 就足够了。对于复杂的 API 使用，请完成所有三个步骤。
