---
mode: 'agent'
tools: ['changes', 'codebase', 'edit/editFiles', 'problems']
description: '创建带有正确OpenAPI文档的ASP.NET Minimal API端点'
---

# ASP.NET Minimal API with OpenAPI

您的目标是帮助我创建结构良好的ASP.NET Minimal API端点，具有正确的类型和全面的OpenAPI/Swagger文档。

## API组织

- 使用`MapGroup()`扩展对相关端点进行分组
- 对横切关注点使用端点过滤器
- 使用单独的端点类结构化更大的API
- 考虑为复杂API使用基于功能的文件夹结构

## 请求和响应类型

- 定义明确的请求和响应DTO/模型
- 创建带有适当验证属性的清晰模型类
- 使用记录类型表示不可变的请求/响应对象
- 使用与API设计标准对齐的有意义属性名称
- 应用`[Required]`和其他验证属性以强制执行约束
- 使用ProblemDetailsService和StatusCodePages获取标准错误响应

## 类型处理

- 使用带有显式类型绑定的强类型路由参数
- 使用`Results<T1, T2>`表示多个响应类型
- 返回`TypedResults`而不是`Results`以获得强类型响应
- 利用C# 10+特性，如可空注释和仅初始化属性

## OpenAPI文档

- 使用.NET 9中添加的内置OpenAPI文档支持
- 定义操作摘要和描述
- 使用`WithName`扩展方法添加operationIds
- 使用`[Description()]`为属性和参数添加描述
- 为请求和响应设置正确的内容类型
- 使用文档转换器添加服务器、标签和安全方案等元素
- 使用模式转换器对OpenAPI模式应用自定义