---
agent: 'agent'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'problems']
description: 'Create ASP.NET Minimal API endpoints with proper OpenAPI documentation'
---

# 带有 OpenAPI 的 ASP.NET 最小 API

您的目标是帮助我创建结构良好的 ASP.NET Minimal API 端点，并具有正确的类型和全面的 OpenAPI/Swagger 文档。

## API组织

- 使用 `MapGroup()` 扩展对相关端点进行分组
- 使用端点过滤器来处理横切关注点
- 使用单独的端点类构建更大的 API
- 考虑对复杂的 API 使用基于功能的文件夹结构

## 请求和响应类型

- 定义显式请求和响应 DTO/模型
- 创建具有适当验证属性的清晰模型类
- 对不可变的请求/响应对象使用记录类型
- 使用符合 API 设计标准的有意义的属性名称
- 应用 `[Required]` 和其他验证属性来强制执行约束
- 使用 ProblemDetailsService 和 StatusCodePages 获取标准错误响应

## 类型处理

- 使用具有显式类型绑定的强类型路由参数
- 使用 `Results<T1, T2>` 表示多种响应类型
- 对于强类型响应，返回 `TypedResults` 而不是 `Results`
- 利用 C# 10+ 功能，例如可为 null 的注释和仅限 init 的属性

## 开放API文档

- 使用.NET 9中添加的内置OpenAPI文档支持
- 定义操作摘要和描述
- 使用 `WithName` 扩展方法添加操作Id
- 使用 `[Description()]` 添加属性和参数的描述
- 为请求和响应设置正确的内容类型
- 使用文档转换器添加服务器、标签和安全方案等元素
- 使用模式转换器将自定义应用到 OpenAPI 模式
