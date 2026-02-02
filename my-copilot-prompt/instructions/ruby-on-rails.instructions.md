---
description: 'Ruby on Rails coding conventions and guidelines'
applyTo: '**/*.rb'
---

# 红宝石 on Rails

## 一般准则

- 遵循 RuboCop 样式指南并使用 `rubocop`、`standardrb` 或 `rufo` 等工具来实现一致的格式。
- 对变量/方法使用蛇形命名法，对类/模块使用驼峰命名法。
- 保持方法简短、重点突出；使用提前返回、保护子句和私有方法来降低复杂性。
- 优先使用有意义的名称而不是简短或通用的名称。
- 仅在必要时发表评论——避免解释显而易见的事情。
- 将单一职责原则应用于类、方法和模块。
- 优先选择组合而不是继承；将可重用逻辑提取到模块或服务中。
- 保持控制器精简——将业务逻辑移至模型、服务或命令/查询对象中。
- 深思熟虑地应用“胖模型，瘦控制器”模式并具有清晰的抽象。
- 将业务逻辑提取到服务对象中以实现可重用性和可测试性。
- 使用部分或视图组件来减少重复并简化视图。
- 对于否定条件，请使用 `unless`，但为了清楚起见，应避免使用 `else`。
- 避免深层嵌套的条件 - 支持保护子句和方法提取。
- 使用安全导航 (`&.`) 而不是多个 `nil` 检查。
- 优先使用 `.present?`、`.blank?` 和 `.any?` 而不是手动 nil/empty 检查。
- 在路由和控制器操作中遵循 RESTful 约定。
- 使用 Rails 生成器一致地构建资源。
- 使用强参数安全地将属性列入白名单。
- 更喜欢枚举和类型化属性，以获得更好的模型清晰度和验证。
- 保持迁移与数据库无关；尽可能避免原始 SQL。
- 始终为外键和经常查询的列添加索引。
- 在数据库级别定义 `null: false` 和 `unique: true`，而不仅仅是在模型中。
- 使用 `find_each` 迭代大型数据集以减少内存使用。
- 为了清晰和重用，在模型中限定查询范围或使用查询对象。
- 谨慎使用 `before_action` 回调 — 避免其中包含业务逻辑。
- 使用 `Rails.cache` 存储昂贵的计算或频繁访问的数据。
- 使用 `Rails.root.join(...)` 而不是硬编码构建文件路径。
- 在关联中使用 `class_name` 和 `foreign_key` 来实现显式关系。
- 使用 `Rails.application.credentials` 或 ENV 变量将机密和配置保留在代码库之外。
- 为模型、服务和助手编写独立的单元测试。
- 通过请求/系统测试覆盖端到端逻辑。
- 使用后台作业 (ActiveJob) 进行非阻塞操作，例如发送电子邮件或调用 API。
- 使用 `FactoryBot` (RSpec) 或固定装置 (Minitest) 干净地设置测试数据。
- 避免使用 `puts` — 使用 `byebug`、`pry` 或记录器实用程序进行调试。
- 使用 YARD 或 RDoc 记录复杂的代码路径和方法。

## 应用程序目录结构

- 在`app/services`目录中定义服务对象来封装业务逻辑。
- 使用位于 `app/forms` 中的表单对象来管理验证和提交逻辑。
- 在 `app/serializers` 目录中实现 JSON 序列化器以格式化 API 响应。
- 在`app/policies`中定义授权策略，控制用户对资源的访问。
- 通过在 `app/graphql` 内组织架构、查询和突变来构建 GraphQL API。
- 在 `app/validators` 中创建自定义验证器以强制执行专门的验证逻辑。
- 将复杂的 ActiveRecord 查询隔离并封装在 `app/queries` 中，以实现更好的重用和可测试性。
- 在 `app/types` 目录中定义自定义数据类型和强制逻辑以扩展或覆盖 ActiveModel 类型行为。

## 命令

- 使用 `rails generate` 创建新模型、控制器和迁移。
- 使用 `rails db:migrate` 应用数据库迁移。
- 使用 `rails db:seed` 用初始数据填充数据库。
- 使用 `rails db:rollback` 恢复上次迁移。
- 使用 `rails console` 与 REPL 环境中的 Rails 应用程序交互。
- 使用 `rails server` 启动开发服务器。
- 使用 `rails test` 运行测试套件。
- 使用 `rails routes` 列出应用程序中所有定义的路由。
- 使用 `rails assets:precompile` 编译用于生产的资产。


## API 开发最佳实践

- 使用 Rails 的 `resources` 构建路由以遵循 RESTful 约定。
- 使用命名空间路由（例如 `/api/v1/`）进行版本控制和前向兼容性。
- 使用 `ActiveModel::Serializer` 或 `fast_jsonapi` 序列化响应以获得一致的输出。
- 为每个响应返回正确的 HTTP 状态代码（例如，200 OK、201 Created、422 Unprocessable Entity）。
- 使用 `before_action` 过滤器来加载和授权资源，而不是业务逻辑。
- 利用分页（例如 `kaminari` 或 `pagy`）来返回大型数据集的端点。
- 使用中间件或 gem（如 `rack-attack`）对敏感端点进行速率限制和节流。
- 以结构化 JSON 格式返回错误，包括错误代码、消息和详细信息。
- 使用强参数清理输入参数并将其列入白名单。
- 使用自定义序列化器或演示器将内部逻辑与响应格式分离。
- 急切加载相关数据时，使用 `includes` 避免 N+1 查询。
- 实现非阻塞任务的后台作业，例如发送电子邮件或与外部 API 同步。
- 记录请求/响应元数据以进行调试、可观察性和审核。
- 使用 OpenAPI (Swagger)、`rswag` 或 `apipie-rails` 记录端点。
- 使用 CORS 标头 (`rack-cors`) 允许在需要时跨源访问您的 API。
- 确保敏感数据永远不会在 API 响应或错误消息中暴露。

## 前端开发最佳实践

- 使用 `app/javascript` 作为使用 Webpacker 或 esbuild 管理 Rails 6+ 中的 JavaScript 包、模块和前端逻辑的主目录。
- 按组件或域（而不是文件类型）构建 JavaScript，以保持模块化。
- 利用 Hotwire（Turbo + Stimulus）进行实时更新并在 Rails 本机应用程序中使用最少的 JavaScript。
- 使用 Stimulus 控制器将行为绑定到 HTML 并以声明方式管理 UI 逻辑。
- 使用 `app/assets/stylesheets` 下的 SCSS 模块、Tailwind 或 BEM 约定来组织样式。
- 通过将重复标记提取到部分或组件中来保持视图逻辑干净。
- 使用语义 HTML 标签并在所有视图中遵循可访问性 (a11y) 最佳实践。
- 避免内联 JavaScript 和样式；相反，为了清晰和可重用性，将逻辑移动到单独的 `.js` 或 `.scss` 文件中。
- 使用资产管道或捆绑器进行缓存和压缩来优化资产（图像、字体、图标）。
- 使用 `data-*` 属性来桥接前端交互性与 Rails 生成的 HTML 和 Stimulus。
- 使用系统测试 (Capybara) 或使用 Cypress 或 Playwright 等工具进行集成测试来测试前端功能。
- 使用特定于环境的资源加载来防止生产中不必要的脚本或样式。
- 遵循设计系统或组件库以保持 UI 的一致性和可扩展性。
- 使用延迟加载、Turbo Frames 和延迟 JS 优化首次绘制时间 (TTFP) 和资源加载。

## 测试指南

- 使用 `test/models` (Minitest) 或 `spec/models` (RSpec) 为模型编写单元测试来验证业务逻辑。
- 使用夹具 (Minitest) 或具有 `FactoryBot` (RSpec) 的工厂来干净、一致地管理测试数据。
- 在 `test/controllers` 或 `spec/requests` 下组织控制器规范以测试 RESTful API 行为。
- 优先使用 RSpec 中的 `before` 块或 Minitest 中的 `setup` 来初始化公共测试数据。
- 避免在测试中使用外部 API — 使用 `WebMock`、`VCR` 或 `stub_request` 来隔离测试环境。
- 在 Minitest 中使用 `system tests` 或在 RSpec 中使用 Capybara 的 `feature specs` 来模拟完整的用户流程。
- 将缓慢且昂贵的测试（例如外部服务、文件上传）隔离到单独的测试类型或标签中。
- 运行 `SimpleCov` 等测试覆盖率工具以确保足够的代码覆盖率。
- 在测试中避免使用 `sleep` ；将 `perform_enqueued_jobs` (Minitest) 或 `ActiveJob::TestHelper` 与 RSpec 结合使用。
- 使用数据库清理工具（`rails test:prepare`、`DatabaseCleaner` 或 `transactional_fixtures`）在测试之间保持干净状态。
- 通过使用 `ActiveJob::TestHelper` 或 `have_enqueued_job` 匹配器排队和执行作业来测试后台作业。
- 使用 CI 工具（例如 GitHub Actions、CircleCI）确保测试在不同环境中一致运行。
- 使用自定义匹配器 (RSpec) 或自定义断言 (Minitest) 来实现可重用且富有表现力的测试逻辑。
- 按类型（例如 `:model`、`:request`、`:feature`）标记测试，以实现更快、更有针对性的测试运行。
- 避免脆弱的测试——除非明确必要，否则不要依赖特定的时间戳、随机数据或顺序。
- 为跨多个层（模型、视图、控制器）的端到端流编写集成测试。
- 保持测试快速、可靠，并且像生产代码一样干燥。
