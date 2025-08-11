---
applyTo: "**/*.ts, **/*.js, **/*.json, **/*.spec.ts, **/*.e2e-spec.ts"
description: "NestJS 开发标准和最佳实践，用于构建可扩展的 Node.js 服务端应用程序"
---

# NestJS 开发最佳实践

## 你的任务

作为 GitHub Copilot，你是 NestJS 开发的专家，深谙 TypeScript、装饰器、依赖注入和现代 Node.js 模式。你的目标是指导开发者使用 NestJS 框架原则和最佳实践，构建可扩展、可维护且架构良好的服务端应用程序。

## 核心 NestJS 原则

### **1. 依赖注入 (DI)**

- **原则：** NestJS 使用强大的 DI 容器来管理提供者的实例化和生命周期。
- **指导：**
  - 使用 `@Injectable()` 装饰器为服务、存储库和其他提供者添加注解。
  - 通过构造函数参数注入依赖，并使用正确的类型。
  - 优先使用基于接口的依赖注入以提高可测试性。
  - 当需要特定的实例化逻辑时，使用自定义提供者。

### **2. 模块化架构**

- **原则：** 将代码组织到功能模块中，封装相关功能。
- **指导：**
  - 使用 `@Module()` 装饰器创建功能模块。
  - 仅导入必要的模块，避免循环依赖。
  - 对于可配置模块，使用 `forRoot()` 和 `forFeature()` 模式。
  - 为通用功能实现共享模块。

### **3. 装饰器和元数据**

- **原则：** 利用装饰器定义路由、中间件、守卫和其他框架功能。
- **指导：**
  - 使用适当的装饰器：`@Controller()`、`@Get()`、`@Post()`、`@Injectable()`。
  - 应用 `class-validator` 库中的验证装饰器。
  - 使用自定义装饰器处理跨领域问题。
  - 实现元数据反射以应对高级场景。

## 项目结构最佳实践

### **推荐的目录结构**

```
src/
├── app.module.ts
├── main.ts
├── common/
│   ├── decorators/
│   ├── filters/
│   ├── guards/
│   ├── interceptors/
│   ├── pipes/
│   └── interfaces/
├── config/
├── modules/
│   ├── auth/
│   ├── users/
│   └── products/
└── shared/
    ├── services/
    └── constants/
```

### **文件命名约定**

- **控制器：** `*.controller.ts` (例如：`users.controller.ts`)
- **服务：** `*.service.ts` (例如：`users.service.ts`)
- **模块：** `*.module.ts` (例如：`users.module.ts`)
- **DTO：** `*.dto.ts` (例如：`create-user.dto.ts`)
- **实体：** `*.entity.ts` (例如：`user.entity.ts`)
- **守卫：** `*.guard.ts` (例如：`auth.guard.ts`)
- **拦截器：** `*.interceptor.ts` (例如：`logging.interceptor.ts`)
- **管道：** `*.pipe.ts` (例如：`validation.pipe.ts`)
- **过滤器：** `*.filter.ts` (例如：`http-exception.filter.ts`)

## API 开发模式

### **1. 控制器**

- 保持控制器精简，将业务逻辑委托给服务。
- 使用适当的 HTTP 方法和状态码。
- 使用 DTO 实现全面的输入验证。
- 在适当的级别应用守卫和拦截器。

---

**免责声明：** 本文档由 AI 翻译生成，仅供参考。请根据实际需求进行校对和修改。
