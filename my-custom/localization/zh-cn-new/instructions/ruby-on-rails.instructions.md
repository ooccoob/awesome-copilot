---
description: 'Ruby on Rails 编码约定和指南'
applyTo: '**/*.rb'
---

# Ruby on Rails

## 一般指南

- 遵循 RuboCop 样式指南并使用 `rubocop`、`standardrb` 或 `rufo` 等工具进行一致的格式化。
- 变量/方法使用 snake_case，类/模块使用 CamelCase。
- 保持方法简短且专注；使用早期返回、保护子句和私有方法来降低复杂性。
- 优先使用有意义的名称而不是简短或通用的名称。
- 仅在必要时注释——避免解释显而易见的内容。
- 对类、方法和模块应用单一职责原则。
- 优先使用组合而不是继承；将可重用逻辑提取到模块或服务中。
- 保持控制器瘦——将业务逻辑移动到模型、服务或命令/查询对象。
- 理性地应用"胖模型、瘦控制器"模式并使用清晰的抽象。
- 将业务逻辑提取到服务对象中以实现可重用性和可测试性。
- 使用部分或视图组件来减少重复并简化视图。
- 对否定条件使用 `unless`，但为清晰起见避免与 `else` 一起使用。
- 避免深度嵌套的条件语句——优先使用保护子句和方法提取。
- 使用安全导航（`&.`）而不是多个 `nil` 检查。
- 优先使用 `.present?`、`.blank?` 和 `.any?` 而不是手动的 nil/empty 检查。
- 在路由和控制器操作中遵循 RESTful 约定。
- 使用 Rails 生成器一致地构建资源。
- 使用强参数安全地将属性列入白名单。
- 优先使用枚举和类型化属性以获得更好的模型清晰度和验证。
- 保持迁移数据库无关；尽可能避免原始 SQL。
- 始终为外键和经常查询的列添加索引。
- 在数据库级别定义 `null: false` 和 `unique: true`，而不仅仅是在模型中。
- 使用 `find_each` 迭代大数据集以减少内存使用。
- 在模型中限定查询或使用查询对象以实现清晰性和可重用性。
- 谨慎使用 `before_action` 回调——避免在其中放置业务逻辑。
- 使用 `Rails.cache` 存储昂贵的计算或频繁访问的数据。
- 使用 `Rails.root.join(...)` 构建文件路径而不是硬编码。
- 在关联中使用 `class_name` 和 `foreign_key` 来明确关系。
- 使用 `Rails.application.credentials` 或 ENV 变量将密钥和配置排除在代码库之外。
- 为模型、服务和助手编写独立的单元测试。
- 使用请求/系统测试覆盖端到端逻辑。
- 对非阻塞操作（如发送邮件或调用 API）使用后台作业（ActiveJob）。
- 使用 `FactoryBot`（RSpec）或 fixtures（Minitest）干净地设置测试数据。
- 避免使用 `puts`——使用 `byebug`、`pry` 或 logger 实用程序进行调试。
- 使用 YARD 或 RDoc 记录复杂的代码路径和方法。

## 应用程序目录结构

- 在 `app/services` 目录中定义服务对象以封装业务逻辑。
- 使用位于 `app/forms` 的表单对象来管理验证和提交逻辑。
- 在 `app/serializers` 目录中实现 JSON 序列化器以格式化 API 响应。
- 在 `app/policies` 中定义授权策略以控制用户对资源的访问。
- 通过在 `app/graphql` 内部组织模式、查询和变更来构建 GraphQL API。
- 在 `app/validators` 中创建自定义验证器以强制执行专门的验证逻辑。
- 在 `app/queries` 中隔离和封装复杂的 ActiveRecord 查询以实现更好的可重用性和可测试性。
- 在 `app/types` 目录中定义自定义数据类型和强制转换逻辑以扩展或覆盖 ActiveModel 类型行为。

## 命令

- 使用 `rails generate` 创建新模型、控制器和迁移。
- 使用 `rails db:migrate` 应用数据库迁移。
- 使用 `rails db:seed` 用初始数据填充数据库。
- 使用 `rails db:rollback` 撤销最后一次迁移。
- 使用 `rails console` 在 REPL 环境中与 Rails 应用程序交互。
- 使用 `rails server` 启动开发服务器。
- 使用 `rails test` 运行测试套件。
- 使用 `rails routes` 列出应用程序中所有定义的路由。
- 使用 `rails assets:precompile` 为生产编译资产。


## API 开发最佳实践

- 使用 Rails 的 `resources` 构建路由以遵循 RESTful 约定。
- 使用命名空间路由（例如：`/api/v1/`）进行版本控制和向前兼容。
- 使用 `ActiveModel::Serializer` 或 `fast_jsonapi` 序列化响应以获得一致的输出。
- 为每个响应返回适当的 HTTP 状态码（例如：200 OK、201 Created、422 Unprocessable Entity）。
- 使用 `before_action` 过滤器加载和授权资源，而不是业务逻辑。
- 利用分页（例如：`kaminari` 或 `pagy`）处理返回大数据集的端点。
- 使用中间件或像 `rack-attack` 这样的 gem 对敏感端点进行速率限制和节流。
- 以结构化 JSON 格式返回错误，包括错误代码、消息和详细信息。
- 使用强参数清理和将输入参数列入白名单。
- 使用自定义序列化器或呈现器将内部逻辑与响应格式分离。
- 在预加载相关数据时使用 `includes` 避免 N+1 查询。
- 为非阻塞任务（如发送邮件或与外部 API 同步）实现后台作业。
- 记录请求/响应元数据以进行调试、可观察性和审计。
- 使用 OpenAPI（Swagger）、`rswag` 或 `apipie-rails` 记录端点。
- 使用 CORS 标头（`rack-cors`）在需要时允许跨域访问您的 API。
- 确保敏感数据永远不会暴露在 API 响应或错误消息中。

## 前端开发最佳实践

- 在 Rails 6+ 中使用 Webpacker 或 esbuild 时，使用 `app/javascript` 作为管理 JavaScript 包、模块和前端逻辑的主要目录。
- 按组件或域而不是文件类型来组织 JavaScript，以保持模块化。
- 在 Rails 原生应用中利用 Hotwire（Turbo + Stimulus）进行实时更新和最少的 JavaScript。
- 使用 Stimulus 控制器将行为绑定到 HTML 并声明式地管理 UI 逻辑。
- 在 `app/assets/stylesheets` 下使用 SCSS 模块、Tailwind 或 BEM 约定组织样式。
- 通过将重复标记提取到部分或组件中来保持视图逻辑清洁。
- 在所有视图中使用语义 HTML 标签并遵循可访问性（a11y）最佳实践。
- 避免内联 JavaScript 和样式；而是将逻辑移动到单独的 `.js` 或 `.scss` 文件以实现清晰性和可重用性。
- 使用资产管道或捆绑器优化资产（图像、字体、图标）以进行缓存和压缩。
- 使用 `data-*` 属性将前端交互性与 Rails 生成的 HTML 和 Stimulus 连接起来。
- 使用系统测试（Capybara）或带有 Cypress 或 Playwright 等工具的集成测试来测试前端功能。
- 使用特定于环境的资产加载来防止生产中不必要的脚本或样式。
- 遵循设计系统或组件库以保持 UI 一致性和可扩展性。
- 使用懒加载、Turbo Frames 和延迟 JS 优化首次绘制时间（TTFP）和资产加载。

## 测试指南

- 使用 `test/models`（Minitest）或 `spec/models`（RSpec）为模型编写单元测试以验证业务逻辑。
- 使用 fixtures（Minitest）或带有 `FactoryBot`（RSpec）的工厂来干净且一致地管理测试数据。
- 在 `test/controllers` 或 `spec/requests` 下组织控制器规范以测试 RESTful API 行为。
- 优先在 RSpec 中使用 `before` 块或在 Minitest 中使用 `setup` 来初始化通用测试数据。
- 避免在测试中命中外部 API——使用 `WebMock`、`VCR` 或 `stub_request` 来隔离测试环境。
- 在 Minitest 中使用 `system tests` 或在 RSpec 中使用带有 Capybara 的 `feature specs` 来模拟完整的用户流程。
- 将缓慢和昂贵的测试（例如：外部服务、文件上传）隔离到单独的测试类型或标签中。
- 运行像 `SimpleCov` 这样的测试覆盖率工具以确保足够的代码覆盖率。
- 在测试中避免 `sleep`；使用 `perform_enqueued_jobs`（Minitest）或带有 RSpec 的 `ActiveJob::TestHelper`。
- 使用数据库清理工具（`rails test:prepare`、`DatabaseCleaner` 或 `transactional_fixtures`）在测试之间保持清洁状态。
- 通过使用 `ActiveJob::TestHelper` 排队和执行作业或使用 `have_enqueued_job` 匹配器来测试后台作业。
- 使用 CI 工具（例如：GitHub Actions、CircleCI）确保测试在各环境中一致运行。
- 使用自定义匹配器（RSpec）或自定义断言（Minitest）以实现可重用和富有表现力的测试逻辑。
- 按类型标记测试（例如：`:model`、`:request`、`:feature`）以进行更快和定向的测试运行。
- 避免脆弱的测试——除非明确必要，否则不要依赖特定时间戳、随机数据或顺序。
- 为跨多个层（模型、视图、控制器）的端到端流程编写集成测试。
- 保持测试快速、可靠，并与生产代码一样 DRY。