---
description: 'Next.js + Tailwind开发标准和指令'
applyTo: '**/*.tsx, **/*.ts, **/*.jsx, **/*.js, **/*.css'
---

# Next.js + Tailwind开发指令

使用Tailwind CSS样式化和TypeScript构建高质量Next.js应用程序的指令。

## 项目上下文

- 最新Next.js（App Router）
- TypeScript用于类型安全
- Tailwind CSS用于样式化

## 开发标准

### 架构
- 带服务器和客户端组件的App Router
- 按功能/域分组路由
- 实施适当的错误边界
- 默认使用React Server Components
- 在可能的地方利用静态优化

### TypeScript
- 启用严格模式
- 清晰的类型定义
- 使用类型守卫进行适当的错误处理
- 使用Zod进行运行时类型验证

### 样式
- 具有一致调色板的Tailwind CSS
- 响应式设计模式
- 深色模式支持
- 遵循容器查询最佳实践
- 保持语义HTML结构

### 状态管理
- React Server Components用于服务器状态
- React hooks用于客户端状态
- 适当的加载和错误状态
- 在适当时使用乐观更新

### 数据获取
- Server Components用于直接数据库查询
- React Suspense用于加载状态
- 适当的错误处理和重试逻辑
- 缓存失效策略

### 安全性
- 输入验证和清理
- 适当的身份验证检查
- CSRF保护
- 速率限制实施
- 安全的API路由处理

### 性能
- 使用next/image进行图像优化
- 使用next/font进行字体优化
- 路由预取
- 适当的代码分割
- 包大小优化

## 实施过程
1. 规划组件层次结构
2. 定义类型和接口
3. 实施服务器端逻辑
4. 构建客户端组件
5. 添加适当的错误处理
6. 实施响应式样式
7. 添加加载状态
8. 编写测试