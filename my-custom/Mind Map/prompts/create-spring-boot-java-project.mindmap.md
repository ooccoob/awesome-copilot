## 文档综述（What/When/Why/How）

- What：创建 Spring Boot Java 项目骨架的提示词（JDK21、Docker、Compose）

- When：需要快速脚手架并集成 Redis/PostgreSQL/Mongo、SpringDoc、Testcontainers 时

- Why：统一脚手架与配置，降低启动成本，并提供一键验证测试

- How：校验 Java→下载模板→解压→添加依赖与配置→docker-compose 三服务→.gitignore→mvnw 测试/运行

## 示例提问（Examples）

- “生成含 SpringDoc + ArchUnit 的 pom 片段并写入 application.properties 配置”

- “创建 docker-compose 与忽略目录，并运行 mvnw clean test 验证”

## 结构化要点（CN/EN）

- 依赖/Deps：springdoc/archunit/testcontainers

- 配置/Config：Redis/JPA/Mongo 参数

- 编排/Orchestration：docker-compose 三件套

- 校验/Check：mvnw clean test 通过

## 中文思维导图

- 模板下载
  - start.spring.io
- 依赖注入
  - pom 追加
- 配置文件
  - properties
- 编排文件
  - compose 服务
- 验证
  - 测试/运行

## 溯源信息

- 源文件：d:\mycode\awesome-copilot\prompts\create-spring-boot-java-project.prompt.md

- 生成时间：2025-10-17
