---
applyTo: "springboot.instructions.md"
---

<!-- 本文件为自动翻译，供参考。请结合实际需求进行校对和完善。-->

# Spring Boot 应用开发规范与最佳实践

## 1. 项目结构与组织

- **推荐使用标准分层结构**：controller、service、repository、model、config 等。
- **每个类单独一个文件，命名用 PascalCase**。
- **配置文件用 application.yml 或 application.properties**，按环境分 profile。

## 2. 依赖与构建

- **用 Maven/Gradle 管理依赖**，锁定版本。
- **定期升级依赖，避免安全漏洞**。
- **用 Spring Boot 官方起步依赖（starter）**。

## 3. 代码风格与质量

- **统一用 Checkstyle/Spotless/SonarQube 检查代码风格和质量**。
- **变量、方法、类命名语义化，避免缩写和拼音**。
- **注释解释复杂逻辑或特殊约定**。

## 4. 配置与安全

- **敏感信息用环境变量或加密配置管理**，禁止硬编码。
- **用 @Value/@ConfigurationProperties 类型安全注入配置**。
- **生产环境禁用 debug/trace 日志和 actuator 公开端点**。

## 5. REST API 设计

- **用 @RestController/@RequestMapping/@GetMapping 等注解**。
- **接口返回统一响应结构**，如 Result/Response 包装类。
- **参数校验用 @Valid/@Validated 和自定义异常处理**。
- **接口文档用 Swagger/OpenAPI 自动生成**。

## 6. 数据访问

- **优先用 Spring Data JPA/MyBatis**。
- **查询用参数化，禁止拼接 SQL**。
- **事务管理用 @Transactional**。
- **分页、排序、批量操作用框架内置能力**。

## 7. 测试

- **用 JUnit5/Mockito/Spring Boot Test 编写单元和集成测试**。
- **测试文件与被测类同包，命名为 `*Test.java`**。
- **测试覆盖率目标 80% 以上**。

## 8. 性能与监控

- **用 Spring Boot Actuator 监控应用健康和指标**。
- **用 Prometheus/Grafana 集成监控和告警**。
- **用缓存（如 Redis）优化热点数据访问**。

## 9. 质量检查清单

- [ ] 结构清晰，命名规范
- [ ] 依赖和配置安全合规
- [ ] 代码风格和注释达标
- [ ] REST API 设计合理
- [ ] 数据访问安全高效
- [ ] 测试覆盖率达标
- [ ] 性能和监控到位

---

免责声明：本翻译仅供参考，具体实践请结合实际项目需求和最新官方文档。
