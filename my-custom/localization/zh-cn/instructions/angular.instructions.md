---
description: "Angular 专用编码规范与最佳实践"
applyTo: "**/*.ts, **/*.html, **/*.scss, **/*.css"
---

# Angular 开发指引

本指引用于帮助开发高质量的 Angular 应用，推荐使用 TypeScript、Angular Signals 进行状态管理，并遵循 https://angular.dev 上的官方最佳实践。

## 项目背景

- 使用最新 Angular 版本（默认采用独立组件 standalone components）
- 采用 TypeScript 保证类型安全
- 使用 Angular CLI 进行项目初始化与脚手架搭建
- 遵循 Angular 风格指南（https://angular.dev/style-guide）
- 如有需要，推荐使用 Angular Material 或其他现代 UI 库实现一致化样式

## 开发规范

### 架构

- 除非必须，优先使用独立组件（standalone components）
- 按功能模块或领域组织代码，便于扩展
- 对特性模块采用懒加载优化性能
- 有效利用 Angular 内置依赖注入系统
- 智能组件与展示组件分离，关注点清晰

### TypeScript

- 在 `tsconfig.json` 启用 strict 模式
- 为组件、服务、模型定义清晰接口与类型
- 使用类型保护与联合类型提升健壮性
- 结合 RxJS 运算符（如 `catchError`）实现健壮的错误处理
- 表单推荐使用类型化（如 `FormGroup`、`FormControl`）的响应式表单

### 组件设计

- 遵循 Angular 生命周期钩子最佳实践
- Angular 19 及以上优先用 `input()`、`output()`、`viewChild()`、`viewChildren()`、`contentChild()`、`contentChildren()` 函数代替装饰器，否则用装饰器
- 合理选择变更检测策略（默认或 `OnPush` 提升性能）
- 保持模板简洁，将逻辑放在组件类或服务中
- 善用指令与管道实现复用

### 样式

- 使用组件级 CSS 封装（默认 ViewEncapsulation.Emulated）
- 推荐 SCSS，统一主题风格
- 利用 CSS Grid、Flexbox 或 Angular CDK Layout 实现响应式设计
- 使用 Angular Material 时遵循其主题规范
- 保证无障碍（a11y），合理使用 ARIA 属性与语义化 HTML

### 状态管理

- 组件与服务中优先用 Angular Signals 实现响应式状态管理
- 使用 `signal()`、`computed()`、`effect()` 实现响应式更新
- 可变状态用 writable signals，派生状态用 computed signals
- 用 signals 和 UI 反馈处理加载与错误状态
- 结合 RxJS 时，模板中用 AsyncPipe 处理 observable

### 数据获取

- 用 Angular `HttpClient` 调用 API，类型安全
- 用 RxJS 运算符处理数据转换与错误
- 独立组件中用 `inject()` 注入依赖
- 实现缓存策略（如 observable 用 `shareReplay`）
- API 响应数据存入 signals 实现响应式更新
- 全局拦截器统一处理 API 错误

### 安全

- 用 Angular 内置机制净化用户输入
- 路由守卫实现认证与授权
- 用 `HttpInterceptor` 实现 CSRF 防护与 API 认证
- 表单用响应式表单与自定义校验器校验输入
- 遵循 Angular 安全最佳实践（如避免直接操作 DOM）

### 性能

- 生产环境用 `ng build --prod` 优化构建
- 路由懒加载减少初始包体积
- 用 `OnPush` 策略和 signals 精细化变更检测
- `ngFor` 循环用 trackBy 提升渲染性能
- 如有需要，结合 Angular Universal 实现 SSR 或 SSG

### 测试

- 用 Jasmine 和 Karma 编写组件、服务、管道单元测试
- 用 Angular `TestBed` 结合 mock 依赖测试组件
- 用 Angular 测试工具测试 signal 状态更新
- 端到端测试可用 Cypress 或 Playwright
- 用 `HttpClientTestingModule` mock HTTP 请求
- 关键功能保证高测试覆盖率

## 实施流程

1. 规划项目结构与功能模块
2. 定义 TypeScript 接口与模型
3. 用 Angular CLI 脚手架生成组件、服务、管道
4. 用 signals 实现数据服务与 API 集成
5. 构建可复用组件，明确输入输出
6. 添加响应式表单与校验
7. 用 SCSS 实现样式与响应式设计
8. 实现懒加载路由与守卫
9. 用 signals 实现错误与加载状态处理
10. 编写单元与端到端测试
11. 优化性能与包体积

## 其他建议

- 遵循 Angular 命名规范（如 `feature.component.ts`, `feature.service.ts`）
- 用 Angular CLI 命令生成模板代码
- 用 JSDoc 注释文档化组件与服务
- 保证无障碍合规（WCAG 2.1）
- 如有需要，使用 Angular 内置 i18n 实现国际化
- 复用工具与共享模块，保持代码 DRY
- 状态管理统一用 signals，保证响应式更新

---

**免责声明**：本文档由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 本地化。如有错误或不当之处，欢迎通过 [issues](../../issues) 反馈。
