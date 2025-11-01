## 文档综述（What/When/Why/How）

- What：创建 Spring Boot Kotlin 项目骨架的提示词（JDK21、Gradle KTS、Docker/Compose）

- When：需快速集成 WebFlux、R2DBC、Redis Reactive、Mongo Reactive、SpringDoc、Testcontainers 时

- Why：提升 Kotlin 项目起步一致性，提供可运行与测试的最小可行样板

- How：校验 Java→下载模板（gradle-kotlin）→添加依赖与配置→docker-compose 三服务→.gitignore→gradlew 测试/运行

## 示例提问（Examples）

- “在 build.gradle.kts 注入 springdoc/webflux-ui 与 archunit-junit5，补充 application.properties 配置”

- “创建 compose 服务并忽略数据目录，运行 gradlew clean test”

## 结构化要点（CN/EN）

- 依赖/Deps：webflux-ui/archunit-junit5

- 配置/Config：R2DBC/Redis/Mongo

- 编排/Orchestration：docker-compose

- 校验/Check：gradlew clean test

## 中文思维导图

- 模板下载
  - start.spring.io
- 依赖注入
  - build.gradle.kts
- 配置文件
  - properties
- 编排文件
  - compose 服务
- 验证
  - 测试/运行

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-spring-boot-kotlin-project.prompt.md

- 生成时间：2025-10-17
