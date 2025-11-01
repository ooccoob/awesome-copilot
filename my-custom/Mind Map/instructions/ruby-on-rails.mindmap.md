## What/When/Why/How
- What: Rails 开发规范（风格、结构、API、前端、测试）
- When: 新建/重构 Rails 应用或 API 时
- Why: 提升一致性与可维护性，降低缺陷
- How: RuboCop + SRP + 服务对象/表单对象/序列化器 + Hotwire

## Key Points
- 风格/命名：snake_case/CamelCase；Rubocop 格式化
- 结构：Fat Model/Thin Controller（谨慎）；Service/Query/Policy/Serializer/Validator/Type
- API：RESTful；命名空间版本；分页/速率限制/CORS；结构化错误
- 数据：索引/外键/非空/唯一；find_each；避免 N+1（includes）
- 配置/密钥：credentials/ENV；Rails.root.join 路径
- 前端：Hotwire(Turbo+Stimulus)；组件化视图；可达性
- 测试：模型/请求/系统测试；工厂/fixtures；VCR/WebMock；覆盖率
- 作业：ActiveJob 用于异步；避免阻塞

## Compact Map
- Layers: model/service/form/query/policy/serializer
- API: routes/versions/errors/rate-limit
- Data: indexes/fk/null/unique
- FE: Hotwire + Stimulus + SCSS

## Example Questions
1) 控制器是否纤薄且无业务逻辑？
2) 是否将复杂流程抽取为服务对象并可复用？
3) API 是否版本化、分页并返回一致错误？
4) 是否避免 N+1 并为查询字段建索引？
5) 机密是否通过 credentials/ENV 管理？
6) 前端是否采用 Hotwire/Stimulus 提升交互？
7) 测试是否隔离外部依赖并具系统测试？
8) 迁移是否包含索引/非空/唯一约束？
9) 大数据遍历是否使用 find_each？
10) 背景任务是否用 ActiveJob 并可测试？
11) 日志与监控是否覆盖关键路径？

Source: d:\mycode\awesome-copilot\instructions\ruby-on-rails.instructions.md | Generated: 2025-10-17
