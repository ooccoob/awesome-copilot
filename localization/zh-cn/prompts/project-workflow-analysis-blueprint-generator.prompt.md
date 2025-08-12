````prompt
---
description: '跨技术栈的端到端项目工作流文档生成器：自动检测项目架构模式、技术栈与数据流，生成覆盖入口层、服务层、数据访问、错误处理与测试方法的实现级蓝图，适配 .NET、Java/Spring、React、微服务等架构场景。'
---

# 项目工作流文档生成器（Project Workflow Documentation Generator）

## 配置变量（Configuration Variables）

```
${PROJECT_TYPE="Auto-detect|.NET|Java|Spring|Node.js|Python|React|Angular|Microservices|Other"}
<!-- 主技术栈；保留变量名，翻译注释即可 -->

${ENTRY_POINT="API|GraphQL|Frontend|CLI|Message Consumer|Scheduled Job|Custom"}
<!-- 工作流起点类型 -->

${PERSISTENCE_TYPE="Auto-detect|SQL Database|NoSQL Database|File System|External API|Message Queue|Cache|None"}
<!-- 持久化方式 -->

${ARCHITECTURE_PATTERN="Auto-detect|Layered|Clean|CQRS|Microservices|MVC|MVVM|Serverless|Event-Driven|Other"}
<!-- 架构模式 -->

${WORKFLOW_COUNT=1-5}
<!-- 需要生成文档的代表性工作流数量 -->

${DETAIL_LEVEL="Standard|Implementation-Ready"}
<!-- 细节级别（标准/可直接落地） -->

${INCLUDE_SEQUENCE_DIAGRAM=true|false}
<!-- 是否生成时序图 -->

${INCLUDE_TEST_PATTERNS=true|false}
<!-- 是否包含测试方法 -->
```

## 生成的提示（Generated Prompt）

```
"Analyze the codebase and document ${WORKFLOW_COUNT} representative end-to-end workflows
that can serve as implementation templates for similar features. Use the following approach:
```

### 初始检测阶段（Initial Detection Phase）

```
${PROJECT_TYPE == "Auto-detect" ?
  "Begin by examining the codebase structure to identify technologies:
   - Check for .NET solutions/projects, Spring configurations, Node.js/Express files, etc.
   - Identify the primary programming language(s) and frameworks in use
   - Determine the architectural patterns based on folder structure and key components"
  : "Focus on ${PROJECT_TYPE} patterns and conventions"}
```

```
${ENTRY_POINT == "Auto-detect" ?
  "Identify typical entry points by looking for:
   - API controllers or route definitions
   - GraphQL resolvers
   - UI components that initiate network requests
   - Message handlers or event subscribers
   - Scheduled job definitions"
  : "Focus on ${ENTRY_POINT} entry points"}
```

```
${PERSISTENCE_TYPE == "Auto-detect" ?
  "Determine persistence mechanisms by examining:
   - Database context/connection configurations
   - Repository implementations
   - ORM mappings
   - External API clients
   - File system interactions"
  : "Focus on ${PERSISTENCE_TYPE} interactions"}
```

### 工作流文档编写指引（Workflow Documentation Instructions）

针对系统中最具代表性的 `${WORKFLOW_COUNT}` 个工作流，逐项输出：

#### 1. 工作流总览（Workflow Overview）
- 工作流名称与简述
- 业务目标与价值
- 触发动作或事件来源
- 全链路涉及的文件/类清单

#### 2. 入口层实现（Entry Point Implementation）

API 入口（API Entry Points）
```
${ENTRY_POINT == "API" || ENTRY_POINT == "Auto-detect" ?
  "- Document the API controller class and method that receives the request
   - Show the complete method signature including attributes/annotations
   - Include the full request DTO/model class definition
   - Document validation attributes and custom validators
   - Show authentication/authorization attributes and checks" : ""}
```

GraphQL 入口（GraphQL Entry Points）
```
${ENTRY_POINT == "GraphQL" || ENTRY_POINT == "Auto-detect" ?
  "- Document the GraphQL resolver class and method
   - Show the complete schema definition for the query/mutation
   - Include input type definitions
   - Show resolver method implementation with parameter handling" : ""}
```

前端入口（Frontend Entry Points）
```
${ENTRY_POINT == "Frontend" || ENTRY_POINT == "Auto-detect" ?
  "- Document the component that initiates the API call
   - Show the event handler that triggers the request
   - Include the API client service method
   - Show state management code related to the request" : ""}
```

消息消费入口（Message Consumer Entry Points）
```
${ENTRY_POINT == "Message Consumer" || ENTRY_POINT == "Auto-detect" ?
  "- Document the message handler class and method
   - Show message subscription configuration
   - Include the complete message model definition
   - Show deserialization and validation logic" : ""}
```

#### 3. 服务层实现（Service Layer Implementation）
- 服务类与其依赖
- 完整方法签名（参数与返回类型）
- 关键业务逻辑实现片段
- 接口定义（如适用）
- 依赖注入注册方式

CQRS 场景（CQRS Patterns）
```
${ARCHITECTURE_PATTERN == "CQRS" || ARCHITECTURE_PATTERN == "Auto-detect" ?
  "- Include complete command/query handler implementations" : ""}
```

整洁架构（Clean Architecture Patterns）
```
${ARCHITECTURE_PATTERN == "Clean" || ARCHITECTURE_PATTERN == "Auto-detect" ?
  "- Show use case/interactor implementations" : ""}
```

#### 4. 数据映射模式（Data Mapping Patterns）
- DTO 与领域模型的映射代码
- 对象映射器配置或手动映射方法
- 映射过程中的校验逻辑
- 产生的领域事件

#### 5. 数据访问实现（Data Access Implementation）
- 仓储接口与实现类
- 完整方法签名与参数/返回类型
- 具体查询/命令实现
- 实体/模型定义及属性
- 事务处理模式

SQL 数据库模式（SQL Database Patterns）
```
${PERSISTENCE_TYPE == "SQL Database" || PERSISTENCE_TYPE == "Auto-detect" ?
  "- Include ORM configurations, annotations, or Fluent API usage
   - Show actual SQL queries or ORM statements" : ""}
```

NoSQL 数据库模式（NoSQL Database Patterns）
```
${PERSISTENCE_TYPE == "NoSQL Database" || PERSISTENCE_TYPE == "Auto-detect" ?
  "- Show document structure definitions
   - Include document query/update operations" : ""}
```

#### 6. 响应构建（Response Construction）
- 响应 DTO/模型定义
- 领域/实体到响应模型的映射
- 状态码选择逻辑
- 错误响应结构与生成方式

#### 7. 错误处理模式（Error Handling Patterns）
- 工作流内使用的异常类型
- 各层 try/catch 模式
- 全局异常处理配置
- 错误日志实现
- 重试策略与熔断器模式
- 失败场景的补偿措施

#### 8. 异步处理模式（Asynchronous Processing Patterns）
- 后台任务调度代码
- 事件发布实现
- 消息队列发送
- 回调或 Webhook 实现
- 异步跟踪与监控

测试方法（可选，Testing Approach）
```
${INCLUDE_TEST_PATTERNS ?
  "9. **Testing Approach**
     - Document unit test implementations for each layer
     - Show mocking patterns and test fixture setup
     - Include integration test implementations
     - Document test data generation approaches
     - Show API/controller test implementations" : ""}
```

时序图（可选，Sequence Diagram）
```
${INCLUDE_SEQUENCE_DIAGRAM ?
  "10. **Sequence Diagram**
      - Generate a detailed sequence diagram showing all components
      - Include method calls with parameter types
      - Show return values between components
      - Document conditional flows and error paths" : ""}
```

#### 11. 命名约定（Naming Conventions）
请给出一致的命名规范覆盖：
- 控制器命名（如 `EntityNameController`）
- 服务命名（如 `EntityNameService`）
- 仓储命名（如 `IEntityNameRepository`）
- DTO 命名（如 `EntityNameRequest`、`EntityNameResponse`）
- CRUD 方法命名模式
- 变量命名约定
- 文件组织模式

#### 12. 实现模板（Implementation Templates）
提供可复用的代码模板以支持：
- 基于既有模式新增 API 端点
- 实现新的服务方法
- 新增仓储方法
- 定义新的领域模型类
- 正确实现错误处理

### 面向特定技术的实现模式（Technology-Specific Implementation Patterns）

.NET 实现模式（若检测到）
```
${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Auto-detect" ?
  "- Complete controller class with attributes, filters, and dependency injection
   - Service registration in Startup.cs or Program.cs
   - Entity Framework DbContext configuration
   - Repository implementation with EF Core or Dapper
   - AutoMapper profile configurations
   - Middleware implementations for cross-cutting concerns
   - Extension method patterns
   - Options pattern implementation for configuration
   - Logging implementation with ILogger
   - Authentication/authorization filter or policy implementations" : ""}
```

Spring/Java 实现模式（若检测到）
```
${PROJECT_TYPE == "Java" || PROJECT_TYPE == "Spring" || PROJECT_TYPE == "Auto-detect" ?
  "- Complete controller class with annotations and dependency injection
   - Service implementation with transaction boundaries
   - Repository interface and implementation
   - JPA entity definitions with relationships
   - DTO class implementations
   - Bean configuration and component scanning
   - Exception handler implementations
   - Custom validator implementations" : ""}
```

React 实现模式（若检测到）
```
${PROJECT_TYPE == "React" || PROJECT_TYPE == "Auto-detect" ?
  "- Component structure with props and state
   - Hook implementation patterns (useState, useEffect, custom hooks)
   - API service implementation
   - State management patterns (Context, Redux)
   - Form handling implementations
   - Route configuration" : ""}
```

### 实施建议（Implementation Guidelines）

基于已文档化的工作流，给出新增功能时的具体实施指南：

#### 1. 分步实施流程（Step-by-Step Implementation Process）
- 新增相似功能的起步位置
- 实施顺序（例如 model → repository → service → controller）
- 如何与现有横切关注点集成

#### 2. 常见陷阱（Common Pitfalls to Avoid）
- 标注易错环节
- 性能考量
- 常见缺陷与绕坑建议

#### 3. 扩展机制（Extension Mechanisms）
- 如何接入既有扩展点
- 在不修改既有代码前提下新增行为
- 配置驱动的特性扩展模式

**结语（Conclusion）：**
以保持与当前代码库一致性的前提，总结必须遵循的关键模式，指引新功能的持续实现。

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](https://github.com/ooccoob/datafill/issues) 进行反馈。

````
