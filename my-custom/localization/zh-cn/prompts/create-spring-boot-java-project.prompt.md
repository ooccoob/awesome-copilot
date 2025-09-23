---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "findTestFiles", "problems", "runCommands", "runTests", "search", "searchResults", "terminalLastCommand", "testFailure", "usages"]
description: "创建 Spring Boot Java 项目骨架"
---

# 创建 Spring Boot Java 项目（prompt）

- 请确保系统已安装：

  - Java 21
  - Docker
  - Docker Compose

- 若需自定义项目名，请在 [download-spring-boot-project-template](./create-spring-boot-java-project.prompt.md#download-spring-boot-project-template) 中修改 `artifactId` 与 `packageName`

- 若需更新 Spring Boot 版本，请在 [download-spring-boot-project-template](./create-spring-boot-java-project.prompt.md#download-spring-boot-project-template) 中修改 `bootVersion`

## 检查 Java 版本

- 在终端运行以下命令检查 Java 版本

```shell
java -version
```

## 下载 Spring Boot 项目模板

- 在终端运行以下命令下载 Spring Boot 项目模板

```shell
curl https://start.spring.io/starter.zip \
  -d artifactId=demo \
  -d bootVersion=3.4.5 \
  -d dependencies=lombok,configuration-processor,web,data-jpa,postgresql,data-redis,data-mongodb,validation,cache,testcontainers \
  -d javaVersion=21 \
  -d packageName=com.example \
  -d packaging=jar \
  -d type=maven-project \
  -o starter.zip
```

## 解压下载的文件

- 在终端运行以下命令解压下载的文件

```shell
unzip starter.zip -d .
```

## 删除下载的 zip 文件

- 在终端运行以下命令删除下载的 zip 文件

```shell
rm -f starter.zip
```

## 添加额外依赖

- 在 `pom.xml` 中插入 `springdoc-openapi-starter-webmvc-ui` 与 `archunit-junit5`

```xml
<dependency>
  <groupId>org.springdoc</groupId>
  <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
  <version>2.8.6</version>
</dependency>
<dependency>
  <groupId>com.tngtech.archunit</groupId>
  <artifactId>archunit-junit5</artifactId>
  <version>1.2.1</version>
  <scope>test</scope>
</dependency>
```

## 添加 SpringDoc、Redis、JPA 与 MongoDB 配置

- 在 `application.properties` 中插入 SpringDoc 配置

```properties
# SpringDoc configurations
springdoc.swagger-ui.doc-expansion=none
springdoc.swagger-ui.operations-sorter=alpha
springdoc.swagger-ui.tags-sorter=alpha
```

- 在 `application.properties` 中插入 Redis 配置

```properties
# Redis configurations
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.password=rootroot
```

- 在 `application.properties` 中插入 JPA 配置

```properties
# JPA configurations
spring.datasource.driver-class-name=org.postgresql.Driver
spring.datasource.url=jdbc:postgresql://localhost:5432/postgres
spring.datasource.username=postgres
spring.datasource.password=rootroot
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
```

- 在 `application.properties` 中插入 MongoDB 配置

```properties
# MongoDB configurations
spring.data.mongodb.host=localhost
spring.data.mongodb.port=27017
spring.data.mongodb.authentication-database=admin
spring.data.mongodb.username=root
spring.data.mongodb.password=rootroot
spring.data.mongodb.database=test
```

## 添加 `docker-compose.yaml`（Redis、PostgreSQL、MongoDB）

- 在项目根创建 `docker-compose.yaml` 并添加以下服务：`redis:6`、`postgresql:17`、`mongo:8`

  - redis 服务需：
    - 密码 `rootroot`
    - 端口映射 6379:6379
    - 挂载卷 `./redis_data` 至 `/data`
  - postgresql 服务需：
    - 密码 `rootroot`
    - 端口映射 5432:5432
    - 挂载卷 `./postgres_data` 至 `/var/lib/postgresql/data`
  - mongo 服务需：
    - 初始化 root 用户名 `root`
    - 初始化 root 密码 `rootroot`
    - 端口映射 27017:27017
    - 挂载卷 `./mongo_data` 至 `/data/db`

## 添加 `.gitignore`

- 在 `.gitignore` 中添加 `redis_data`、`postgres_data`、`mongo_data`

## 运行 Maven 测试

- 执行 maven clean test 检查项目可用性

```shell
./mvnw clean test
```

## 运行项目（可选）

- （可选）`docker-compose up -d` 启动服务，`./mvnw spring-boot:run` 运行项目，`docker-compose rm -sf` 停止服务。

## 分步执行

```

```
