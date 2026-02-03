---
description: 'Comprehensive technology-agnostic prompt generator for documenting end-to-end application workflows. Automatically detects project architecture patterns, technology stacks, and data flow patterns to generate detailed implementation blueprints covering entry points, service layers, data access, error handling, and testing approaches across multiple technologies including .NET, Java/Spring, React, and microservices architectures.'

agent: 'agent'
---
# 项目工作流程文档生成器

## 配置变量

```
${PROJECT_TYPE="Auto-detect|.NET|Java|Spring|Node.js|Python|React|Angular|Microservices|Other"}
<!-- Primary technology stack -->

${ENTRY_POINT="API|GraphQL|Frontend|CLI|Message Consumer|Scheduled Job|Custom"}
<!-- Starting point for the flow -->

${PERSISTENCE_TYPE="Auto-detect|SQL Database|NoSQL Database|File System|External API|Message Queue|Cache|None"}
<!-- Data storage type -->

${ARCHITECTURE_PATTERN="Auto-detect|Layered|Clean|CQRS|Microservices|MVC|MVVM|Serverless|Event-Driven|Other"}
<!-- Primary architecture pattern -->

${WORKFLOW_COUNT=1-5}
<!-- Number of workflows to document -->

${DETAIL_LEVEL="Standard|Implementation-Ready"}
<!-- Level of implementation detail to include -->

${INCLUDE_SEQUENCE_DIAGRAM=true|false}
<!-- Generate sequence diagram -->

${INCLUDE_TEST_PATTERNS=true|false}
<!-- Include testing approach -->
```

## 生成的提示

```
"Analyze the codebase and document ${WORKFLOW_COUNT} representative end-to-end workflows 
that can serve as implementation templates for similar features. Use the following approach:
```

### 初始检测阶段

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

### 工作流程文档说明

对于系统中每个最具代表性的 `${WORKFLOW_COUNT}` 工作流程：

#### 1. 工作流程概述
   - 提供工作流程的名称和简要说明
   - 解释其服务的商业目的
   - 识别触发动作或事件
   - 列出完整工作流程中涉及的所有文件/类

#### 2. 入口点实现

**API入口点：**
```
${ENTRY_POINT == "API" || ENTRY_POINT == "Auto-detect" ? 
  "- Document the API controller class and method that receives the request
   - Show the complete method signature including attributes/annotations
   - Include the full request DTO/model class definition
   - Document validation attributes and custom validators
   - Show authentication/authorization attributes and checks" : ""}
```

**GraphQL 入口点：**
```
${ENTRY_POINT == "GraphQL" || ENTRY_POINT == "Auto-detect" ? 
  "- Document the GraphQL resolver class and method
   - Show the complete schema definition for the query/mutation
   - Include input type definitions
   - Show resolver method implementation with parameter handling" : ""}
```

**前端入口点：**
```
${ENTRY_POINT == "Frontend" || ENTRY_POINT == "Auto-detect" ? 
  "- Document the component that initiates the API call
   - Show the event handler that triggers the request
   - Include the API client service method
   - Show state management code related to the request" : ""}
```

**消息消费者入口点：**
```
${ENTRY_POINT == "Message Consumer" || ENTRY_POINT == "Auto-detect" ? 
  "- Document the message handler class and method
   - Show message subscription configuration
   - Include the complete message model definition
   - Show deserialization and validation logic" : ""}
```

#### 3. 服务层实现
   - 记录每个服务类及其依赖关系
   - 显示带有参数和返回类型的完整方法签名
   - 包括具有关键业务逻辑的实际方法实现
   - 记录适用的接口定义
   - 显示依赖注入注册模式

**CQRS 模式：**
```
${ARCHITECTURE_PATTERN == "CQRS" || ARCHITECTURE_PATTERN == "Auto-detect" ? 
  "- Include complete command/query handler implementations" : ""}
```

**干净的架构模式：**
```
${ARCHITECTURE_PATTERN == "Clean" || ARCHITECTURE_PATTERN == "Auto-detect" ? 
  "- Show use case/interactor implementations" : ""}
```

#### 4. 数据映射模式
   - 将 DTO 记录到域模型映射代码
   - 显示对象映射器配置或手动映射方法
   - 在映射期间包含验证逻辑
   - 记录映射期间创建的任何域事件

#### 5. 数据访问实现
   - 文档存储库接口及其实现
   - 显示带有参数和返回类型的完整方法签名
   - 包括实际的查询实现
   - 记录具有所有属性的实体/模型类定义
   - 显示事务处理模式

**SQL 数据库模式：**
```
${PERSISTENCE_TYPE == "SQL Database" || PERSISTENCE_TYPE == "Auto-detect" ? 
  "- Include ORM configurations, annotations, or Fluent API usage
   - Show actual SQL queries or ORM statements" : ""}
```

**NoSQL 数据库模式：**
```
${PERSISTENCE_TYPE == "NoSQL Database" || PERSISTENCE_TYPE == "Auto-detect" ? 
  "- Show document structure definitions
   - Include document query/update operations" : ""}
```

#### 6. 响应构建
   - 记录响应 DTO/模型类定义
   - 显示从域/实体模型到响应模型的映射
   - 包括状态代码选择逻辑
   - 文档错误响应结构和生成

#### 7. 错误处理模式
   - 记录工作流程中使用的异常类型
   - 在每一层显示 try/catch 模式
   - 包括全局异常处理程序配置
   - 记录错误日志实现
   - 显示重试策略或断路器模式
   - 包括针对故障场景的补偿措施

#### 8. 异步处理模式
   - 文档后台作业调度代码
   - 显示事件发布实施
   - 包括消息队列发送模式
   - 记录回调或 webhook 实现
   - 显示如何跟踪和监控异步操作

**测试方法（可选）：**
```
${INCLUDE_TEST_PATTERNS ? 
  "9. **Testing Approach**
     - Document unit test implementations for each layer
     - Show mocking patterns and test fixture setup
     - Include integration test implementations
     - Document test data generation approaches
     - Show API/controller test implementations" : ""}
```

**序列图（可选）：**
```
${INCLUDE_SEQUENCE_DIAGRAM ? 
  "10. **Sequence Diagram**
      - Generate a detailed sequence diagram showing all components
      - Include method calls with parameter types
      - Show return values between components
      - Document conditional flows and error paths" : ""}
```

#### 11. 命名约定
记录一致的模式：
- 控制器命名（例如 `EntityNameController`）
- 服务命名（例如 `EntityNameService`）
- 存储库命名（例如 `IEntityNameRepository`）
- DTO 命名（例如 `EntityNameRequest`、`EntityNameResponse`）
- CRUD 操作的方法命名模式
- 变量命名约定
- 文件组织模式

#### 12. 实施模板
提供可重用的代码模板：
- 按照模式创建新的 API 端点
- 实施新的服务方式
- 添加新的存储库方法
- 创建新的领域模型类
- 实施正确的错误处理

### 特定技术的实施模式

**.NET 实现模式（如果检测到）：**
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

**Spring 实现模式（如果检测到）：**
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

**React 实现模式（如果检测到）：**
```
${PROJECT_TYPE == "React" || PROJECT_TYPE == "Auto-detect" ? 
  "- Component structure with props and state
   - Hook implementation patterns (useState, useEffect, custom hooks)
   - API service implementation
   - State management patterns (Context, Redux)
   - Form handling implementations
   - Route configuration" : ""}
```

### 实施指南

根据记录的工作流程，提供实施新功能的具体指导：

#### 1. 分步实施流程
- 添加类似功能时从哪里开始
- 实现顺序（例如，模型→存储库→服务→控制器）
- 如何与现有的跨领域关注点集成

#### 2. 要避免的常见陷阱
- 识别当前实施中容易出错的区域
- 注意性能注意事项
- 列出遇到的常见错误或问题

#### 3. 扩展机制
- 记录如何插入现有扩展点
- 展示如何在不修改现有代码的情况下添加新行为
- 解释配置驱动的功能模式

**结论：**
最后总结了在以下情况下应遵循的最重要模式： 
实施新功能以保持与代码库的一致性。”
