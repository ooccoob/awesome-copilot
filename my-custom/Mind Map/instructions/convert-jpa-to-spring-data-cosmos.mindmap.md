## What/When/Why/How

- What: 从 JPA 迁移到 Spring Data Cosmos 的端到端指南：依赖/配置/实体/仓库/服务层/安全/种子/测试/模板兼容/排障。
- When: 将关系型模型迁至 Cosmos 文档型存储，或云原生化改造时。
- Why: 支持水平扩展/低延迟/多区域写；削减阻抗不匹配与模板破碎。
- How: 替换依赖→新增 cosmos profile→配置 DefaultAzureCredential→实体 String id/@Container/@PartitionKey→仓库 CosmosRepository→服务层填充关系→转测与模板修复→系统化编译/运行排障。

## Key Points

- 依赖/配置: 移除 JPA/H2；加入 azure-spring-data-cosmos/azure-identity；application-cosmos.properties；profile=cosmos。
- 实体: id 改 String；加 @Container/@PartitionKey；移除 JPA 注解；关系改 ID 集合+@JsonIgnore 的瞬态对象；避免对持久字段使用 @JsonIgnore。
- 仓库: JpaRepository→CosmosRepository；方法签名与分页调整；findPetTypes→findAllOrderByName。
- 服务层: 负责根据 ID 载入对象并填充瞬态属性；控制器仅经服务访问。
- 安全: User.authorities 存储为 Set<String>；UserDetailsService 转换为 GrantedAuthority；确保密码可序列化。
- 测试: 大量重命名/类型迁移；mvn compile/test-compile 分阶段修复；移除 JPA 专属注解；断言改 String。
- 模板: 系统性遍历页面；修复 SpEL EL1008E；确保服务层填充关系。
- 运行/排障: BigDecimal/JDK17 反射问题；Iterable→List 转换；健康检查去 DB；方法签名冲突需重命名。

## Compact Map

- Config → deps/profile/identity
- Entity → String id/关系→IDs+transient
- Repo → CosmosRepository/签名变更
- Service → 关系填充/控制器只调服务
- Security → Set<String> authorities
- Test → 编译/测试系统修复
- Template → 页面巡检/SpEL 修复
- Troubleshoot → BigDecimal/Iterable/Health

## Example Questions (10+)

1) 关系由对象改 ID 后如何保证模板不破？
2) 哪些 repository 方法需要去掉 Pageable？
3) User/Authority 的序列化注意事项？
4) Iterable→List 的安全转换方式？
5) BigDecimal 在 JDK17 的兼容策略？
6) 方法签名冲突的系统性重命名规则？
7) 服务层 populateRelationships 的通用模式？
8) 测试用例中 ID 迁移搜索替换策略？
9) health readiness 去 DB 的配置示例？
10) findPetTypes→findAllOrderByName 的影响范围？

---
Source: d:\mycode\awesome-copilot\instructions\convert-jpa-to-spring-data-cosmos.instructions.md | Generated: 2025-10-17
