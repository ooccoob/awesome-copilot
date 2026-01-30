---
post_title: "springboot.instructions.md Use Cases"
author1: "github-copilot"
post_slug: "springboot-instructions-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "springboot", "java-development", "backend-development"]
ai_note: "Generated with AI assistance."
summary: "Spring Boot 开发指令的使用场景"
post_date: "2025-10-27"
---

<!-- markdownlint-disable MD041 -->

## What

- Spring Boot 开发最佳实践指导规范

## When

- 开发 Spring Boot 应用程序时
- 进行代码审查时
- 需要遵循 Spring Boot 最佳实践时

## Why

- 确保代码质量和可维护性
- 遵循标准开发规范

## How

- 使用构造函数注入
- 外部化配置
- 按功能组织包结构
- 使用 @Service 注解服务类
- 使用 SLF4J 记录日志

## Key points (英文+中文对照)

- Constructor Injection（构造函数注入）
- Externalized Configuration（外部化配置）
- Feature-based Packages（基于功能的包结构）
- Service Layer Design（服务层设计）
- Security Best Practices（安全最佳实践）

## 使用场景

### 1. 代码组织与架构设计

- 用户故事：作为架构师，我需要设计清晰的项目结构
- 例 1："[提供当前包结构] 请根据 Spring Boot 指令帮我重构代码组织"
- 例 2："[提供 controller 代码] 请帮我抽取业务逻辑到服务层"
- 例 3："请审查当前代码的包结构是否合理"
- 例 4："请帮我创建基于功能的包结构"
- 例 5："请检查工具类是否符合 final + private constructor 标准"

### 2. 依赖注入与配置

- 用户故事：作为开发者，我需要正确配置依赖注入
- 例 1："[提供现有 bean] 请帮我将字段注入改为构造函数注入"
- 例 2："[提供配置文件] 请帮我转换为 YAML 格式"
- 例 3："请帮我创建环境配置文件"
- 例 4："请帮我配置 @ConfigurationProperties"
- 例 5："请帮我设置秘密管理"

### 3. 服务层开发

- 用户故事：作为开发人员，我需要创建清晰的服务层
- 例 1："[提供业务逻辑] 请帮我抽取为 @Service 类"
- 例 2："[提供服务类] 请帮我确保无状态设计"
- 例 3："请帮我设计服务接口"
- 例 4："请帮我添加 DTO 转换逻辑"
- 例 5："请帮我优化服务方法签名"

### 4. 日志记录

- 用户故事：作为运维人员，我需要建立统一的日志标准
- 例 1："[提供现有代码] 请帮我添加 SLF4J 日志"
- 例 2："[提供 System.out.println] 请帮我替换为参数化日志"
- 例 3："请帮我创建日志配置"
- 例 4："请帮我设计日志格式"
- 例 5："请帮我添加敏感信息脱敏"

### 5. 安全与验证

- 用户故事：作为安全工程师，我需要确保应用安全
- 例 1："[提供 SQL 查询] 请帮我改为参数化查询"
- 例 2："[提供请求对象] 请帮我添加 JSR-380 验证"
- 例 3："请帮我审查安全漏洞"
- 例 4："请帮我添加输入验证"
- 例 5："请帮我配置 XSS 防护"

### 6. 构建与测试

- 用户故事：作为测试工程师，我需要验证构建和测试
- 例 1："请帮我运行 Maven 构建"
- 例 2："请帮我运行 Gradle 构建"
- 例 3："请帮我执行测试套件"
- 例 4："请帮我生成 JAR 包"
- 例 5："请帮我创建容器镜像"

## 原始文件

- [springboot.instructions.md](../../instructions/springboot.instructions.md)
