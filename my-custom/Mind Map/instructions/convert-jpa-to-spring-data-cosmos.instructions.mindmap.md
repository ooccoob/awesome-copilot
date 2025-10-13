# Step-by-step guide for converting Spring Boot JPA applications to use Azure Cosmos DB with Spring Data Cosmos - Instructions Mindmap

## 📊 摘要
Step-by-step guide for converting Spring Boot JPA applications to use Azure Cosmos DB with Spring Data Cosmos

本指令提供了关于Step-by-step guide for converting Spring Boot JPA applications to use Azure Cosmos DB with Spring Data Cosmos的核心规范和最佳实践,帮助开发者编写高质量、可维护的代码。

## 🎯 适用范围
- **文件类型**: `**/*.java,**/pom.xml,**/build.gradle,**/application*.properties`
- **技术栈**: Java, Azure, React, Spring
- **场景**: 开发和维护Step-by-step guide for converting Spring Boot JPA applications to use Azure Cosmos DB with Spring Data Cosmos相关项目时使用

## 💡 核心规则与最佳实践

### 主要规范
- Maven** (`pom.xml`):
- Gradle**: Apply same dependency changes for Gradle syntax
- Remove testcontainers and JPA-specific test dependencies
- Create `src/main/resources/application-cosmos.properties`:
- Update `src/main/resources/application.properties`:
- Create `src/main/java/<rootpkg>/config/CosmosConfiguration.java`:
- IMPORTANT**: Use `DefaultAzureCredentialBuilder().build()` instead of key-based authentication for production security
- Target all classes with JPA annotations (`@Entity`, `@MappedSuperclass`, `@Embeddable`)

### 代码质量标准
- 遵循行业标准编码规范
- 保持代码简洁可读
- 添加适当的注释和文档
- 进行充分的测试覆盖

## 📝 关键技术要点

### 项目配置
- 正确设置开发环境
- 配置必要的工具和依赖
- 遵循项目结构规范

### 实现标准
- 使用推荐的设计模式
- 遵循命名规范
- 注意性能和安全考虑

## 🗺️ 思维导图

```mindmap
- Step-by-step guide for converting Spring Boot JPA applications to use Azure Cosmos DB with Spring Data Cosmos
  - 适用范围
    - 文件类型: **/*.java,**/pom.xml,**/build.gradle,**/application*.properties
    - 技术栈: Java, Azure, React, Spring
  - 核心规则
    - High-level plan
    - Step-by-step
    - **Quick Reference: Common Post-Migration Fixes**
  - 最佳实践
    - 代码质量
    - 性能优化
    - 安全考虑
```

## 💾 保存说明
- 文件名: convert-jpa-to-spring-data-cosmos.instructions.mindmap.md
- 位置: Mind Map/instructions/
- 生成时间: 2025-10-13 19:57:53
- 文件类型: Instructions (编程规范/最佳实践)
