---
post_title: "create-spring-boot-kotlin-project.prompt.md Use Cases"
author1: "github-copilot"
post_slug: "create-spring-boot-kotlin-project-prompt-use-cases"
microsoft_alias: "copilot"
featured_image: ""
categories: []
tags: ["use-cases", "spring-boot", "kotlin", "java", "project-scaffolding"]
ai_note: "Generated with AI assistance."
summary: "Use cases for the Create Spring Boot Kotlin Project prompt."
post_date: "2025-10-20"
---

<!-- markdownlint-disable MD041 -->

## What

- 一个用于快速搭建和生成 Spring Boot + Kotlin 项目骨架的提示词。

## When

- 在开始一个新的基于 Spring Boot 和 Kotlin 的微服务或 Web 应用项目时。
- 当需要一个包含特定依赖项（如 WebFlux, JPA, Actuator）的入门项目时。
- 在进行技术原型设计或概念验证（PoC）时。

## Why

- 自动化项目创建过程，避免手动访问 Spring Initializr 网站或使用 IDE 的向导。
- 确保项目结构和构建文件（`build.gradle.kts` 或 `pom.xml`）的正确性和一致性。
- 快速获得一个可以立即运行和开发的基础项目。

## How

- 使用 `/create-spring-boot-kotlin-project` 命令并指定你需要的 Spring Boot 版本、依赖项和项目元数据。
- AI 将生成一个包含完整项目结构的压缩文件，或者提供一个可以下载该项目的链接。
- 你可以解压文件并在你喜欢的 IDE 中打开项目。

## Key points (英文+中文对照)

- Project Scaffolding (项目脚手架)
- Spring Boot Initializr (Spring Boot 初始化器)
- Dependency Management (依赖管理)
- Kotlin Development (Kotlin 开发)

## 使用场景

### 1. 创建一个新的 RESTful API 服务 (Creating a New RESTful API Service)

- **用户故事**: 作为一名后端开发人员，我需要快速启动一个新的微服务，它将使用 Spring WebFlux 暴露 RESTful API。
- **例 1**: `/create-spring-boot-kotlin-project 创建一个使用 Gradle、Spring Boot 3.1 和 Kotlin 的项目，包含 `spring-boot-starter-webflux` 和 `spring-boot-starter-actuator` 依赖。`
- **例 2**: `/create-spring-boot-kotlin-project 我需要一个使用 Maven 的 Spring Boot 项目，用于构建一个简单的 CRUD API。`

### 2. 带有数据库访问的项目 (Project with Database Access)

- **用户故事**: 作为一名全栈开发人员，我正在构建一个需要连接到 PostgreSQL 数据库的 Web 应用。
- **例 1**: `/create-spring-boot-kotlin-project 创建一个 Spring Boot Kotlin 项目，包含 `spring-boot-starter-data-jpa` 和 `postgresql` 驱动依赖。`
- **例 2**: `/create-spring-boot-kotlin-project 我需要一个使用 Spring Data R2DBC 与 MySQL 数据库进行异步交互的项目。`

### 3. 消息驱动的微服务 (Message-Driven Microservice)

- **用户故事**: 作为一名系统工程师，我需要创建一个消费来自 RabbitMQ 队列消息的服务。
- **例 1**: `/create-spring-boot-kotlin-project 创建一个 Spring Boot Kotlin 项目，集成 `spring-boot-starter-amqp` 依赖。`
- **例 2**: `/create-spring-boot-kotlin-project 我需要一个使用 Spring for Apache Kafka 的项目。`

### 4. 用于学习和实验的项目 (Project for Learning and Experimentation)

- **用户故事**: 作为一名正在学习 Kotlin 和 Spring Boot 的学生，我想要一个可以动手实践的基础项目。
- **例 1**: `/create-spring-boot-kotlin-project 创建一个最简单的 Spring Boot Kotlin "Hello World" 项目。`

## 原始文件

- [create-spring-boot-kotlin-project.prompt.md](../../prompts/create-spring-boot-kotlin-project.prompt.md)
