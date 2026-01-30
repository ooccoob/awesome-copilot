## 项目工作流蓝图生成器（思维导图）

- What
  - 自动分析代码库并输出端到端工作流文档蓝图（多技术栈适配）
- When
  - 新成员入项、重构/迁移、规范化工程实践
- Why
  - 沿既有模式复制新特性，减少偏差与返工
- How
  - 自动/指定：项目类型、入口、持久化、架构模式
  - 每个工作流：入口→服务→映射→数据访问→响应→异常→异步→测试→时序图
  - 模板：.NET/Spring/React 等分场景落地代码模板与命名规范
  - 产出：实施模板、常见陷阱、扩展点、实施顺序与质量门禁

- Key Points (CN/EN)
  - Auto-detect patterns
  - Entry/Service/Repo/DTO
  - CQRS/Clean/MVC
  - Sequence diagram, Tests

- Example Questions (≥10)
  1) 本仓库的主入口与跨层依赖如何识别？
  2) 代表性工作流应选哪几个以覆盖 80% 场景？
  3) 数据映射/验证/事务边界的统一模式是什么？
  4) 是否采用 CQRS/Clean，命名与目录是否一致？
  5) 典型错误处理/日志/重试/幂等等横切如何统一？
  6) 持久化层的 ORM/SQL 与分区/多租策略？
  7) 响应 DTO 与状态码规范为何？
  8) 异步/队列/回调在何处接入并如何跟踪？
  9) 测试金字塔与样例如何组织？
  10) 新特性按何步骤接入最安全？

- Compact Mind Map
  - 入口→服务→DAO→DTO→异常→异步→测试→图

- Source: prompts/project-workflow-analysis-blueprint-generator.prompt.md
- Generated: 2025-10-17
