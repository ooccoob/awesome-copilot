---
description: 'Angular特定的编码标准和最佳实践'
applyTo: '**/*.ts, **/*.html, **/*.scss, **/*.css'
---

# Angular开发指令

使用TypeScript生成高质量Angular应用程序的指令，使用Angular Signals进行状态管理，遵循https://angular.dev概述的Angular最佳实践。

## 项目上下文
- 最新Angular版本（默认使用独立组件）
- TypeScript用于类型安全
- Angular CLI用于项目设置和脚手架
- 遵循Angular风格指南（https://angular.dev/style-guide）
- 使用Angular Material或其他现代UI库以保持一致的样式（如指定）

## 开发标准

### 架构
- 除非明确需要模块，否则使用独立组件
- 按独立功能模块或域组织代码以实现可扩展性
- 为功能模块实施懒加载以优化性能
- 有效使用Angular的内置依赖注入系统
- 使用清晰关注点分离的结构化组件（智能组件与展示组件）

### TypeScript
- 在`tsconfig.json`中启用严格模式以确保类型安全
- 为组件、服务和模型定义清晰的接口和类型
- 使用类型守卫和联合类型进行强健的类型检查
- 使用RxJS操作符（例如，`catchError`）实施适当的错误处理
- 对响应式表单使用类型化表单（例如，`FormGroup`、`FormControl`）

### 组件设计
- 遵循Angular组件生命周期钩子最佳实践
- 当使用Angular >= 19时，使用`input()`、`output()`、`viewChild()`、`viewChildren()`、`contentChild()`和`contentChildren()`函数而不是装饰器；否则使用装饰器
- 利用Angular的变更检测策略（默认或`OnPush`以提高性能）
- 保持模板清洁，逻辑放在组件类或服务中
- 使用Angular指令和管道实现可重用功能

### 样式
- 使用Angular组件级CSS封装（默认：ViewEncapsulation.Emulated）
- 优先使用SCSS进行样式化，配合一致的主题
- 使用CSS Grid、Flexbox或Angular CDK Layout工具实施响应式设计
- 如果使用Angular Material，遵循其主题指南
- 使用ARIA属性和语义HTML保持可访问性（a11y）

### 状态管理
- 在组件和服务中使用Angular Signals进行响应式状态管理
- 利用`signal()`、`computed()`和`effect()`进行响应式状态更新
- 对可变状态使用可写信号，对派生状态使用计算信号
- 使用信号和适当的UI反馈处理加载和错误状态
- 当将信号与RxJS结合时，在模板中使用Angular的`AsyncPipe`处理可观察对象

### 数据获取
- 使用Angular的`HttpClient`进行具有适当类型的API调用
- 实施RxJS操作符进行数据转换和错误处理
- 在独立组件中使用Angular的`inject()`函数进行依赖注入
- 实施缓存策略（例如，对可观察对象使用`shareReplay`）
- 将API响应数据存储在信号中以进行响应式更新
- 使用全局拦截器处理API错误以保持一致的错误处理

### 安全性
- 使用Angular内置清理功能清理用户输入
- 实施路由守卫进行身份验证和授权
- 使用Angular的`HttpInterceptor`进行CSRF保护和API身份验证头
- 使用Angular响应式表单和自定义验证器验证表单输入
- 遵循Angular安全最佳实践（例如，避免直接DOM操作）

### 性能
- 使用`ng build --prod`启用生产构建以进行优化
- 使用路由懒加载减少初始包大小
- 使用`OnPush`策略和信号优化变更检测以实现细粒度响应性
- 在`ngFor`循环中使用trackBy提高渲染性能
- 使用Angular Universal实施服务器端渲染（SSR）或静态站点生成（SSG）（如指定）

### 测试
- 使用Jasmine和Karma为组件、服务和管道编写单元测试
- 使用Angular的`TestBed`进行组件测试，模拟依赖项
- 使用Angular测试工具测试基于信号的状态更新
- 使用Cypress或Playwright编写端到端测试（如指定）
- 使用`provideHttpClientTesting`模拟HTTP请求
- 确保关键功能的高测试覆盖率

## 实施过程
1. 规划项目结构和功能模块
2. 定义TypeScript接口和模型
3. 使用Angular CLI搭建组件、服务和管道
4. 实施数据服务和API集成，使用基于信号的状态
5. 构建具有清晰输入和输出的可重用组件
6. 添加响应式表单和验证
7. 应用SCSS和响应式设计的样式
8. 实施懒加载路由和守卫
9. 使用信号添加错误处理和加载状态
10. 编写单元和端到端测试
11. 优化性能和包大小

## 附加指南
- 遵循Angular风格指南的文件命名约定（参见https://angular.dev/style-guide），例如，组件使用`feature.ts`，服务使用`feature-service.ts`。对于遗留代码库，保持与现有模式的一致性。
- 使用Angular CLI命令生成样板代码
- 使用清晰的JSDoc注释记录组件和服务
- 在适用的地方确保可访问性合规（WCAG 2.1）
- 使用Angular内置的i18n进行国际化（如指定）
- 通过创建可重用工具和共享模块保持代码DRY
- 一致使用信号进行状态管理以确保响应式更新