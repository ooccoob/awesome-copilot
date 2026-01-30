---
post_title: Java Spring Boot Prompt Use Cases
author1: github-copilot
post_slug: java-springboot-prompt-use-cases
microsoft_alias: copilot
featured_image: ''
categories: []
tags: ['spring-boot', 'prompt']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for java-springboot.prompt.md covering setup, configuration, web layer, service layer, data access, logging, testing, and security.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

- Spring Boot 开发最佳实践：结构、配置、Web/Service/数据层、测试、安全与日志。

## When

- 新建或重构 Spring Boot 应用，期望高可维护性与一致标准时。

## Why

- 降低隐性复杂度，提升测试性、扩展性与安全性。

## How

- 结构：按领域分包；使用 starters
- 配置：application.yml + @ConfigurationProperties + Profiles
- 控制层：DTO + 校验(@Valid) + 全局异常(@ControllerAdvice)
- 服务层：无状态 + @Transactional 粒度恰当
- 数据层：Spring Data JPA/投影/定制查询
- 测试：JUnit5/切片测试/集成测试/Testcontainers
- 安全与日志：Spring Security/BCrypt/SLF4J 参数化

## Key points (英文+中文对照)

- Feature-oriented packaging; typed config（特性导向的包结构；类型安全的配置）
- DTOs, validation, global error handling（DTOs、数据校验、全局异常处理）
- Transactions, projections, test slices（事务控制、数据投影、测试切片）

## 使用场景

### 1. 快速搭建项目结构

- **用户故事：** 作为 Spring Boot 新项目的负责人，我希望按照最佳实践快速搭建项目骨架，以保证后续开发的一致性与可扩展性。
- **例1：** "/java-springboot [提供现有包结构截图] 请根据提示评估当前分层包结构，并生成按领域划分的重构方案。"
- **例2：** "/java-springboot 请结合 starters 建议，列出这个空白项目在 pom.xml 中需要引入的 Spring Boot starter 清单。"
- **例3：** "/java-springboot [提供 pom.xml 片段] 请检查依赖列表，建议是否应改用 Maven 或 Gradle 并给出迁移步骤。"
- **例4：** "/java-springboot 帮我根据模块功能拆分 package 前缀，例如 order、inventory、billing，各自需要的关键类有哪些？"
- **例5：** "/java-springboot [提供 README.md] 请补充项目初始化说明，确保新成员能按照提示中的结构与依赖快速启动项目。"

### 2. 优雅地管理依赖注入

- **用户故事：** 作为资深开发者，我希望项目中的依赖注入模式统一、可测试，并符合构造器注入与不可变对象的最佳实践。
- **例1：** "/java-springboot [选择一段 Service 代码] 请指出其中的字段注入问题，并生成构造器注入的改写建议。"
- **例2：** "/java-springboot [提供多成员变量的类] 请确认所有依赖是否可以声明为 private final，给出必要的修正步骤。"
- **例3：** "/java-springboot 请列出我们常见的组件分类示例，指出哪些类应使用 @Component/@Service/@Repository/@RestController。"
- **例4：** "/java-springboot [提供一个配置类] 请检查工厂方法是否需要转换为 @ConfigurationProperties 绑定。"
- **例5：** "/java-springboot 帮我写一个代码审查清单，用于检测团队提交是否遵循构造器注入与依赖显式声明。"

### 3. 管理配置与环境隔离

- **用户故事：** 作为运维开发混合角色，我需要确保配置文件清晰可维护，并能在不同环境下安全切换。
- **例1：** "/java-springboot [提供 application.properties] 请按提示转换为 application.yml，并拆分出 dev/prod profile。"
- **例2：** "/java-springboot 帮我设计一个 @ConfigurationProperties 类，用于绑定支付网关配置并附带示例配置文件。"
- **例3：** "/java-springboot [提供一段硬编码的秘钥使用代码] 请输出基于环境变量或 Vault 的改造建议。"
- **例4：** "/java-springboot 请列出多环境配置同步时的检查清单，确保 profile 切换不会遗漏依赖。"
- **例5：** "/java-springboot [提供 docker-compose.yml] 请评估它与 Spring Profiles 的协作方式，并给出改进建议。"

### 4. 构建一致的 RESTful API

- **用户故事：** 作为后端接口设计者，我希望保证控制层遵循 RESTful 规范，使用 DTO、校验与统一异常处理。
- **例1：** "/java-springboot [提供一个 Controller] 请评估其 URL、HTTP 方法是否符合 REST 设计，并给出改进意见。"
- **例2：** "/java-springboot [提供 DTO 定义] 请检查是否缺少 Bean Validation 注解，补充建议及错误提示文案。"
- **例3：** "/java-springboot 帮我生成统一异常响应体和 @ControllerAdvice 样板，并说明如何映射自定义异常。"
- **例4：** "/java-springboot [选择一段直接返回实体的代码] 请建议如何改成 DTO 映射，同时说明转换层职责。"
- **例5：** "/java-springboot 帮我编写接口文档模板，涵盖路径、方法、请求体、响应示例及错误码。"

### 5. 编排业务逻辑与事务

- **用户故事：** 作为服务层维护者，我需要确保业务逻辑集中在无状态的 Service，并正确使用事务控制。
- **例1：** "/java-springboot [提供一个状态缓存的 Service] 请分析其是否违反无状态原则，并给出重构方案。"
- **例2：** "/java-springboot [提供多个数据库操作的函数] 请建议 @Transactional 放置位置及传播行为。"
- **例3：** "/java-springboot 帮我生成服务层代码模板，包含接口、实现、DTO 转换与异常抛出规范。"
- **例4：** "/java-springboot 请列出服务层单元测试要点，包括如何使用 Mockito 验证依赖交互。"
- **例5：** "/java-springboot [提供 serviceImpl 代码] 请指出与业务逻辑不相关的操作，建议迁移到其他层。"

### 6. 优化数据访问层

- **用户故事：** 作为数据层工程师，我希望 Repository 实现高效、安全，并能通过投影与自定义查询满足复杂场景。
- **例1：** "/java-springboot [提供 Repository 接口] 请确认其是否正确继承 JpaRepository 或 CrudRepository，并给出改进建议。"
- **例2：** "/java-springboot 帮我示范如何为复杂检索编写 @Query 注解与命名参数。"
- **例3：** "/java-springboot [提供原始 SQL 查询] 请给出对应的 JPA Criteria API 写法并阐述优缺点。"
- **例4：** "/java-springboot 请示例如何通过 DTO 投影减少数据传输，并补充分页处理注意事项。"
- **例5：** "/java-springboot [提供实体定义] 请检查是否需要添加乐观锁或审计字段，并给出实现方式。"

### 7. 强化日志与可观测性

- **用户故事：** 作为系统维护者，我需要统一的日志规范来支撑排障与审计，避免性能损耗与敏感信息泄露。
- **例1：** "/java-springboot [提供日志片段] 请纠正字符串拼接问题，改用参数化日志。"
- **例2：** "/java-springboot 帮我生成 SLF4J Logger 的声明模板，并说明在不同层记录日志的粒度。"
- **例3：** "/java-springboot [提供异常处理代码] 请建议如何记录一次异常且包含关键上下文。"
- **例4：** "/java-springboot 请列出生产环境日志策略，包括日志级别、追踪 ID 与脱敏要求。"
- **例5：** "/java-springboot 帮我设计日志审查检查表，确保合规性与性能最佳实践。"

### 8. 构建测试与质量保障体系

- **用户故事：** 作为质量负责人，我希望通过单元测试、切片测试与集成测试保障系统稳定性，并利用 Testcontainers 覆盖外部依赖。
- **例1：** "/java-springboot [提供一个测试类] 请判断是否应改用 @WebMvcTest 或 @DataJpaTest，并说明调整步骤。"
- **例2：** "/java-springboot 帮我列出服务层的 JUnit 5 + Mockito 测试模板，包含依赖注入与断言示例。"
- **例3：** "/java-springboot 请生成使用 @SpringBootTest 与 Testcontainers 的集成测试样板。"
- **例4：** "/java-springboot [提供 CI 配置] 请建议如何在流水线中引入测试切片与容器化数据库。"
- **例5：** "/java-springboot 请制作测试覆盖率检查清单，确保关键模块均有自动化测试。"

### 9. 加固安全防护

- **用户故事：** 作为安全负责人，我希望通过 Spring Security、密码加密与输入防护，降低认证与数据安全风险。
- **例1：** "/java-springboot [提供 SecurityConfig] 请检查是否正确配置认证与授权规则，并提出加固建议。"
- **例2：** "/java-springboot [提供用户注册逻辑] 请验证密码是否使用 BCrypt 编码，并给出修复步骤。"
- **例3：** "/java-springboot [提供 Repository 查询] 请评估是否存在 SQL 注入风险，建议使用参数化查询。"
- **例4：** "/java-springboot 帮我列出常见的 XSS 防护措施，并结合提示说明输出编码策略。"
- **例5：** "/java-springboot 请生成安全审计检查表，覆盖访问控制、日志与配置加固。"

## 原始文件

- [java-springboot.prompt.md](../../prompts/java-springboot.prompt.md)
