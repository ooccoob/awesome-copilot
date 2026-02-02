---
description: 'Angular-specific coding standards and best practices'
applyTo: '**/*.ts, **/*.html, **/*.scss, **/*.css'
---

# 角度开发说明

使用 TypeScript 生成高质量 Angular 应用程序、使用 Angular 信号进行状态管理、遵循 https://angular.dev 中概述的 Angular 最佳实践的说明。

## 项目背景
- 最新的 Angular 版本（默认使用独立组件）
- 用于类型安全的 TypeScript
- 用于项目设置和脚手架的 Angular CLI
- 遵循 Angular 风格指南 (https://angular.dev/style-guide)
- 使用 Angular Material 或其他现代 UI 库来实现一致的样式（如果指定）

## 开发标准

### 建筑
- 除非明确需要模块，否则使用独立组件
- 按独立功能模块或域组织代码以实现可扩展性
- 对功能模块实施延迟加载以优化性能
- 有效使用 Angular 内置的依赖注入系统
- 具有明确关注点分离的结构组件（智能组件与演示组件）

### 打字稿
- 在 `tsconfig.json` 中启用严格模式以确保类型安全
- 为组件、服务和模型定义清晰的接口和类型
- 使用类型保护和联合类型进行稳健的类型检查
- 使用 RxJS 运算符实现正确的错误处理（例如 `catchError`）
- 使用类型化表单（例如 `FormGroup`、`FormControl`）作为反应式表单

### 组件设计
- 遵循 Angular 的组件生命周期挂钩最佳实践
- 当使用 Angular >= 19 时，使用 `input()` `output()`、`viewChild()`、`viewChildren()`、`contentChild()` 和 `contentChildren()` 函数而不是装饰器；否则使用装饰器
- 利用 Angular 的变更检测策略（默认或 `OnPush` 以获得性能）
- 保持组件类或服务中的模板和逻辑清晰
- 使用 Angular 指令和管道实现可重用功能

### 造型
- 使用Angular的组件级CSS封装（默认：ViewEncapsulation.Emulated）
- 更喜欢 SCSS 来设计具有一致主题的样式
- 使用 CSS Grid、Flexbox 或 Angular CDK 布局实用程序实施响应式设计
- 如果使用，请遵循 Angular Material 的主题指南
- 使用 ARIA 属性和语义 HTML 维护可访问性 (a11y)

### 状态管理
- 使用 Angular Signals 在组件和服务中进行反应式状态管理
- 利用 `signal()`、`computed()` 和 `effect()` 进行反应式状态更新
- 对可变状态使用可写信号，对派生状态使用计算信号
- 使用信号和正确的 UI 反馈处理加载和错误状态
- 将信号与 RxJS 组合时，使用 Angular 的 `AsyncPipe` 处理模板中的可观察量

### 数据获取
- 使用 Angular 的 `HttpClient` 进行 API 调用并输入正确的类型
- 实现 RxJS 运算符以进行数据转换和错误处理
- 使用 Angular 的 `inject()` 函数在独立组件中进行依赖注入
- 实施缓存策略（例如，用于可观察量的 `shareReplay`）
- 将 API 响应数据存储在信号中以进行反应式更新
- 使用全局拦截器处理 API 错误，以实现一致的错误处理

### 安全性
- 使用 Angular 的内置清理功能清理用户输入
- 实施路由防护以进行身份验证和授权
- 使用 Angular 的 `HttpInterceptor` 进行 CSRF 保护和 API 身份验证标头
- 使用 Angular 的反应式表单和自定义验证器验证表单输入
- 遵循 Angular 的安全最佳实践（例如，避免直接 DOM 操作）

### 性能
- 使用 `ng build --prod` 启用生产构建以进行优化
- 对路由使用延迟加载以减少初始包大小
- 使用 `OnPush` 策略和信号优化变更检测，实现细粒度反应
- 在 `ngFor` 循环中使用 trackBy 来提高渲染性能
- 使用 Angular Universal 实现服务器端渲染 (SSR) 或静态站点生成 (SSG)（如果指定）

### 测试
- 使用 Jasmine 和 Karma 为组件、服务和管道编写单元测试
- 使用 Angular 的 `TestBed` 进行具有模拟依赖项的组件测试
- 使用 Angular 的测试实用程序测试基于信号的状态更新
- 使用 Cypress 或 Playwright 编写端到端测试（如果指定）
- 使用 `provideHttpClientTesting` 模拟 HTTP 请求
- 确保关键功能的高测试覆盖率

## 实施流程
1. 规划项目结构和功能模块
2. 定义 TypeScript 接口和模型
3. 使用 Angular CLI 的脚手架组件、服务和管道
4. 通过基于信号的状态实现数据服务和 API 集成
5. 构建具有清晰输入和输出的可重用组件
6. 添加反应式表单和验证
7. 使用 SCSS 和响应式设计应用样式
8. 实施延迟加载的路线和守卫
9. 使用信号添加错误处理和加载状态
10. 编写单元和端到端测试
11. 优化性能和捆绑包大小

## 附加指南
- 遵循 Angular 风格指南的文件命名约定（请参阅 https://angular.dev/style-guide），例如，对组件使用 `feature.ts` ，对服务使用 `feature-service.ts` 。对于遗留代码库，保持与现有模式的一致性。
- 使用 Angular CLI 命令生成样板代码
- 使用清晰的 JSDoc 注释记录组件和服务
- 确保无障碍合规性 (WCAG 2.1)（如适用）
- 使用 Angular 的内置 i18n 进行国际化（如果指定）
- 通过创建可重用实用程序和共享模块来保持代码干燥
- 一致地使用信号进行状态管理以确保反应式更新
