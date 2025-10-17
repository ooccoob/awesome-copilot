## NestJS 开发规范（速览）

### 这是什么/何时使用/为什么/如何做
- What: NestJS 项目结构、DI、模块化、装饰器、DTO 校验、错误处理、测试与安全等最佳实践。
- When: 设计/重构服务端应用、评审代码、搭建基础骨架与中台能力时。
- Why: 提升可维护性、可测试性与可扩展性；统一目录与命名规范。
- How: 模块化 + 控制器瘦身 + 服务承载业务 + DTO+class-validator + 全局异常过滤器 + 日志与缓存。

### 关键要点
- 结构: common/（装饰器/过滤器/守卫/拦截器/管道）、config/、modules/、shared/。
- DI: @Injectable 注入；接口驱动；自定义 Provider；避免循环依赖。
- 控制器: 仅编排；用守卫/拦截器；正确 HTTP 语义。
- 服务: 纯业务；仓储注入；错误上抛由过滤器统一处理。
- DTO: class-validator + class-transformer；按场景拆分 create/update/query。
- DB: TypeORM 实体/关系/迁移；复杂查询使用 QueryBuilder 或仓储方法。
- 安全: JWT/Guard/RBAC；限流/输入校验/CORS/XSS 输出净化。
- 测试: Jest 单测+集成；mock 仓储与外部依赖；E2E 覆盖鉴权与流程。

### 紧凑脑图
- 架构: 模块化→控制器瘦→服务执业务→DTO 校验→TypeORM→异常过滤→日志
- 跨切: RBAC/限流/缓存/配置/环境变量
- 测试: 单元/集成/E2E

### 开发者示例问题（≥10）
- 如何拆分一个“肥 controller”的重构步骤？
- 自定义 Provider 与 interface-based 注入的示例？
- DTO 校验错误如何通过全局过滤器统一返回？
- TypeORM 事务边界与异常回滚策略？
- 如何实现角色+权限码的复合授权守卫？
- 拦截器里做响应转换与缓存的最佳实践？
- Jest 中 mock Repository 的常见写法？
- 如何处理循环依赖模块（forwardRef 等）的副作用？
- 限流器在多实例部署下如何共享配额？
- 多环境配置的校验（zod或自定义）如何落地？

—
Source: d:\mycode\awesome-copilot\instructions\nestjs.instructions.md | Generated: 2025-10-17
