---
post_title: 'create-spring-boot-java-project.prompt.md Use Cases'
author1: 'github-copilot'
post_slug: 'create-spring-boot-java-project-prompt-use-cases'
microsoft_alias: 'copilot'
featured_image: ''
categories: []
tags: ['use-cases', 'spring-boot', 'java', 'scaffold', 'maven', 'gradle']
ai_note: 'Generated with AI assistance.'
summary: 'Use case scenarios for scaffolding Spring Boot Java projects with standard structure, dependencies, profiles, Dockerization, and CI.'
post_date: '2025-10-20'
---

<!-- markdownlint-disable MD041 -->

## What

* 基于模板快速创建 Spring Boot Java 工程：标准目录、依赖、配置、环境分离、容器化与 CI。

## When

* 新项目初始化、PoC 快速验证、团队统一脚手架输出时。
* 需要一致的质量护栏（代码格式、静态检查、测试骨架、Git 钩子）时。

## Why

* 降低重复劳动与漏项风险，让新项目“即刻可跑、可测、可部署”。
* 将最佳实践预置化，保障团队一致性与可维护性。

## How

* 选择构建工具（Maven/Gradle）与 JDK 版本（建议 17+）。
* 预置模块：核心 Web、数据访问、安全、观察性（Actuator/Logging/Metrics）。
* 生成 Dockerfile、docker-compose 与 GitHub Actions/DevOps 流水线。
* 提供本地/测试/生产 profile 配置与密钥注入策略（不硬编码）。

## Key points (英文+中文对照)

* Opinionated defaults with overrides（带约定优于配置的默认项且可覆盖）
* Profiles and secrets management（多环境与密钥管理）
* CI-ready with tests and lint（自带测试与构建流水线）
* Containerization out of the box（内置容器化产物）
* Security and observability（安全与可观测性）

## 使用场景

### 1. 项目基础骨架生成（结构与依赖）

* 用户故事：作为后端工程师，我要一键生成标准 Spring Boot 项目结构与关键依赖，避免遗漏。
* 例1："/create-spring-boot-java-project 使用 Maven + JDK17，模块名 demo-api，添加 web/validation/devtools。"
* 例2："/create-spring-boot-java-project Gradle Kotlin DSL，启用 lombok + mapstruct + actuator。"
* 例3："/create-spring-boot-java-project 生成统一 package=com.example.demo，主类 DemoApplication。"
* 例4："/create-spring-boot-java-project 添加 slf4j + logback 配置模板与日志切割策略。"
* 例5："/create-spring-boot-java-project 引入 springdoc-openapi 并暴露 /swagger-ui/。"

### 2. 数据访问与配置（DB/ORM）

* 用户故事：作为数据工程负责人，我要集成 MySQL + MyBatis-Plus，预置分页与审计字段。
* 例1："/create-spring-boot-java-project 集成 MyBatis-Plus + HikariCP，生成示例实体/Mapper/Service/Controller。"
* 例2："/create-spring-boot-java-project application-dev.yml 配置 datasource 与日志级别。"
* 例3："/create-spring-boot-java-project 添加分页与统一返回体样例（code/msg/data）。"
* 例4："/create-spring-boot-java-project 提供多环境（dev/test/prod）与占位符，密钥仅走环境变量。"
* 例5："/create-spring-boot-java-project 示例单元测试：Repository + Service Happy Path。"

### 3. 安全与异常（Security/Errors）

* 用户故事：作为架构师，我要最小化安全面，预置异常处理与全局返回体转换。
* 例1："/create-spring-boot-java-project 引入 spring-boot-starter-security + 静态资源放行样例。"
* 例2："/create-spring-boot-java-project 增加全局异常处理器与统一错误码。"
* 例3："/create-spring-boot-java-project 记录一次错误日志并附请求上下文（脱敏）。"
* 例4："/create-spring-boot-java-project 添加 CORS 与 HTTPS 指南注释。"
* 例5："/create-spring-boot-java-project 为登录与健康检查添加最小路由。"

### 4. 可观测性与运维（Actuator/Logs/Metrics）

* 用户故事：作为 SRE，我要开箱能监控，便于排障与容量规划。
* 例1："/create-spring-boot-java-project 开启 actuator 并暴露 health/info/metrics。"
* 例2："/create-spring-boot-java-project 预置 logback-spring.xml，区分 json 与控制台模式。"
* 例3："/create-spring-boot-java-project 集成 Micrometer + Prometheus 示例配置。"
* 例4："/create-spring-boot-java-project 添加 traceId 注入与 MDC 样例。"
* 例5："/create-spring-boot-java-project 提供 Docker 健康检查与 readinessProbe。"

### 5. 容器化与部署（Docker/Compose/K8s）

* 用户故事：作为交付负责人，我要标准 Dockerfile 与 compose，支持本地与云端部署。
* 例1："/create-spring-boot-java-project 生成多阶段构建 Dockerfile（JDK17 + distroless）。"
* 例2："/create-spring-boot-java-project 提供 docker-compose.yml + MySQL + 应用服务。"
* 例3："/create-spring-boot-java-project 生成 Helm chart 雏形（可选）。"
* 例4："/create-spring-boot-java-project 支持环境变量注入与配置挂载。"
* 例5："/create-spring-boot-java-project 输出部署检查清单（端口、健康、日志、密钥）。"

### 6. CI/CD 与质量（Pipelines/Quality Gates）

* 用户故事：作为团队负责人，我要默认即有的构建/测试/扫描流水线，保障质量门。
* 例1："/create-spring-boot-java-project 生成 GitHub Actions：构建 + 测试 + 缓存 + artifact。"
* 例2："/create-spring-boot-java-project 集成 Spotless/Checkstyle/PMD。"
* 例3："/create-spring-boot-java-project 触发规则：PR/Push 到 main/test/release。"
* 例4："/create-spring-boot-java-project 发布镜像到容器仓库（标签含版本与 git sha）。"
* 例5："/create-spring-boot-java-project 失败通知与重试策略模板。"

## 原始文件

* [create-spring-boot-java-project.prompt.md](../../prompts/create-spring-boot-java-project.prompt.md)
