---
description: 'VueJS 3开发标准和最佳实践，使用Composition API和TypeScript'
applyTo: '**/*.vue, **/*.ts, **/*.js, **/*.scss'
---

# VueJS 3开发指令

使用Composition API、TypeScript和现代最佳实践构建高质量VueJS 3应用程序的指令。

## 项目上下文
- Vue 3.x，默认使用Composition API
- TypeScript用于类型安全
- 单文件组件（`.vue`），使用`<script setup>`语法
- 现代构建工具（推荐Vite）
- Pinia用于应用程序状态管理
- 官方Vue风格指南和最佳实践

## 开发标准

### 架构
- 偏好Composition API（`setup`函数和组合函数）而不是Options API
- 按功能或域组织组件和组合函数以实现可扩展性
- 将关注UI的组件（展示组件）与关注逻辑的组件（容器组件）分离
- 将可重用逻辑提取到`composables/`目录中的组合函数
- 按域结构化存储模块（Pinia），明确定义操作、状态和getter

### TypeScript集成
- 在`tsconfig.json`中启用`strict`模式以获得最大类型安全
- 使用`defineComponent`或`<script setup lang="ts">`配合`defineProps`和`defineEmits`
- 利用`PropType<T>`进行类型化props和默认值
- 对复杂的props和状态形状使用接口或类型别名
- 为事件处理器、refs和`useRoute`/`useRouter`钩子定义类型
- 在适用的地方实施通用组件和组合函数

### 组件设计
- 遵循组件单一职责原则
- 组件名称使用PascalCase，文件名使用kebab-case
- 保持组件小且专注于一个关注点
- 使用`<script setup>`语法以获得简洁性和性能
- 使用TypeScript验证props；仅在必要时进行运行时检查
- 偏好插槽和作用域插槽进行灵活组合

### 状态管理
- 使用Pinia进行全局状态：用`defineStore`定义存储
- 对于简单的本地状态，在`setup`中使用`ref`和`reactive`
- 使用`computed`进行派生状态
- 对复杂结构保持状态规范化
- 在Pinia存储中使用actions进行异步逻辑
- 利用存储插件进行持久化或调试

### Composition API模式
- 为共享逻辑创建可重用的组合函数，例如`useFetch`、`useAuth`
- 使用精确的依赖列表使用`watch`和`watchEffect`
- 在`onUnmounted`或watch清理回调中清理副作用
- 对深层依赖注入谨慎使用`provide`/`inject`
- 使用`useAsyncData`或第三方数据工具（Vue Query）

### 样式
- 对组件级样式使用`<style scoped>`或CSS Modules
- 考虑实用程序优先框架（Tailwind CSS）进行快速样式化
- 遵循BEM或功能性CSS约定进行类命名
- 利用CSS自定义属性进行主题化和设计令牌
- 使用CSS Grid和Flexbox实施移动优先、响应式设计
- 确保样式可访问（对比度、焦点状态）

### 性能优化
- 使用动态导入和`defineAsyncComponent`懒加载组件
- 使用`<Suspense>`进行异步组件加载回退
- 对静态或不经常更改的元素应用`v-once`和`v-memo`
- 使用Vue DevTools性能选项卡进行分析
- 避免不必要的观察器；在可能的地方偏好`computed`
- 树摇未使用的代码并利用Vite的优化功能

### 数据获取
- 使用组合函数如`useFetch`（Nuxt）或库如Vue Query
- 明确处理加载、错误和成功状态
- 在组件卸载或参数更改时取消过期请求
- 实施乐观更新并在失败时回滚
- 缓存响应并使用后台重新验证

### 错误处理
- 使用全局错误处理器（`app.config.errorHandler`）处理未捕获的错误
- 将有风险的逻辑包装在`try/catch`中；提供用户友好的消息
- 在组件中使用`errorCaptured`钩子进行本地边界
- 优雅地显示回退UI或错误警报
- 将错误记录到外部服务（Sentry、LogRocket）

### 表单和验证
- 使用库如VeeValidate或@vueuse/form进行声明式验证
- 使用受控的`v-model`绑定构建表单
- 在模糊或输入时进行验证，使用防抖以提高性能
- 在组合函数中处理文件上传和复杂多步表单
- 确保可访问的标签、错误公告和焦点管理

### 路由
- 使用Vue Router 4配合`createRouter`和`createWebHistory`
- 实施嵌套路由和路由级代码分割
- 使用导航守卫（`beforeEnter`、`beforeEach`）保护路由
- 在`setup`中使用`useRoute`和`useRouter`进行程序化导航
- 正确管理查询参数和动态段
- 通过路由元字段实施面包屑数据

### 测试
- 使用Vue Test Utils和Jest编写单元测试
- 关注行为，而不是实现细节
- 使用`mount`和`shallowMount`进行组件隔离
- 根据需要模拟全局插件（router、Pinia）
- 使用Cypress或Playwright添加端到端测试
- 使用axe-core集成测试可访问性

### 安全性
- 避免使用`v-html`；严格清理任何HTML输入
- 使用CSP头缓解XSS和注入攻击
- 在模板和指令中验证和转义数据
- 对所有API请求使用HTTPS
- 将敏感令牌存储在HTTP-only cookie中，而不是`localStorage`

### 可访问性
- 使用语义HTML元素和ARIA属性
- 管理模态框和动态内容的焦点
- 为交互式组件提供键盘导航
- 为图像和图标添加有意义的`alt`文本
- 确保颜色对比符合WCAG AA标准

## 实施过程
1. 规划组件和组合函数架构
2. 使用Vue 3和TypeScript初始化Vite项目
3. 定义Pinia存储和组合函数
4. 创建核心UI组件和布局
5. 集成路由和导航
6. 实施数据获取和状态逻辑
7. 构建带有验证和错误状态的表单
8. 添加全局错误处理和回退UI
9. 添加单元和E2E测试
10. 优化性能和包大小
11. 确保可访问性合规
12. 记录组件、组合函数和存储

## 附加指南
- 遵循Vue官方风格指南（vuejs.org/style-guide）
- 使用ESLint（配合`plugin:vue/vue3-recommended`）和Prettier保持代码一致性
- 编写有意义的提交消息并保持干净的git历史
- 保持依赖项最新并审计漏洞
- 使用JSDoc/TSDoc记录复杂逻辑
- 使用Vue DevTools进行调试和分析

## 常见模式
- 使用作用域插槽进行灵活UI的无渲染组件
- 使用provide/inject的复合组件
- 用于横切关注点的自定义指令
- 用于模态框和覆盖层的Teleport
- 用于全局实用程序（i18n、分析）的插件系统
- 用于参数化逻辑的组合函数工厂