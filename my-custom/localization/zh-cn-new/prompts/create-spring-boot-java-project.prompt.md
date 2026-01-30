---
mode: 'agent'
description: '创建Spring Boot Java项目骨架'
---

# 创建Spring Boot Java项目提示

- 请确保您的系统上安装了以下软件：

  - Java 21
  - Docker
  - Docker Compose

- 如果需要自定义项目名称，请更改[下载Spring Boot项目模板](./create-spring-boot-java-project.prompt.md#download-spring-boot-project-template)中的`artifactId`和`packageName`

- 如果需要更新Spring Boot版本，请更改[下载Spring Boot项目模板](./create-spring-boot-java-project.prompt.md#download-spring-boot-project-template)中的`bootVersion`

## 检查Java版本

- 在终端中运行以下命令并检查Java版本

```shell
java -version
```

## 下载Spring Boot项目模板

- 在终端中运行以下命令下载Spring Boot项目模板

```shell
curl https://start.spring.io/starter.zip \
  -d artifactId=${input:projectName:demo-java} \
  -d bootVersion=3.4.5 \
  -d dependencies=lombok,configuration-processor,web,data-jpa,postgresql,data-redis,data-mongodb,validation,cache,testcontainers \
  -d javaVersion=21 \
  -d packageName=com.example \
  -d packaging=jar \
  -d type=maven-project \
  -o starter.zip
```

## 解压下载的文件

- 在终端中运行以下命令解压下载的文件

```shell
unzip starter.zip -d ./${input:projectName:demo-java}
```

## 删除下载的zip文件

- 在终端中运行以下命令删除下载的zip文件

```shell
rm -f starter.zip
```

## 切换到项目根目录

- 在终端中运行以下命令切换到项目根目录

```shell
cd ${input:projectName:demo-java}
```

## 添加额外依赖项

- 将`springdoc-openapi-starter-webmvc-ui`和`archunit-junit5`依赖项插入`pom.xml`文件

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

## 添加SpringDoc、Redis、JPA和MongoDB配置

- 将SpringDoc配置插入`application.properties`文件

```properties
# SpringDoc配置
springdoc.swagger-ui.doc-expansion=none
springdoc.swagger-ui.operations-sorter=alpha
springdoc.swagger-ui.tags-sorter=alpha
```

- 将Redis配置插入`application.properties`文件

```properties
# Redis配置
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.password=rootroot
```

- 将JPA配置插入`application.properties`文件

```properties
# JPA配置
spring.datasource.driver-class-name=org.postgresql.Driver
spring.datasource.url=jdbc:postgresql://localhost:5432/postgres
spring.datasource.username=postgres
spring.datasource.password=rootroot
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
```

- 将MongoDB配置插入`application.properties`文件

```properties
# MongoDB配置
spring.data.mongodb.host=localhost
spring.data.mongodb.port=27017
spring.data.mongodb.authentication-database=admin
spring.data.mongodb.username=root
spring.data.mongodb.password=rootroot
spring.data.mongodb.database=test
```

## 添加包含Redis、PostgreSQL和MongoDB服务的`docker-compose.yaml`

- 在项目根目录创建`docker-compose.yaml`并添加以下服务：`redis:6`、`postgresql:17`和`mongo:8`。

  - redis服务应该具有
    - 密码`rootroot`
    - 将端口6379映射到6379
    - 将卷`./redis_data`挂载到`/data`
  - postgresql服务应该具有
    - 密码`rootroot`
    - 将端口5432映射到5432
    - 将卷`./postgres_data`挂载到`/var/lib/postgresql/data`
  - mongo服务应该具有
    - 初始化数据库root用户名`root`
    - 初始化数据库root密码`rootroot`
    - 将端口27017映射到27017
    - 将卷`./mongo_data`挂载到`/data/db`

## 添加`.gitignore`文件

- 在`.gitignore`文件中插入`redis_data`、`postgres_data`和`mongo_data`目录

## 运行Maven测试命令

- 运行maven clean test命令检查项目是否正常工作

```shell
./mvnw clean test
```

## 运行Maven运行命令（可选）

- （可选）`docker-compose up -d`启动服务，`./mvnw spring-boot:run`运行Spring Boot项目，`docker-compose rm -sf`停止服务。

## 让我们一步一步来完成