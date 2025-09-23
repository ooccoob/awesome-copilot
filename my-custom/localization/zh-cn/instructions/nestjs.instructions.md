---
applyTo: "**/*.ts, **/*.js, **/*.json, **/*.spec.ts, **/*.e2e-spec.ts"
description: "NestJS 开发标准与最佳实践，适用于构建可扩展的 Node.js 服务端应用。"
---

# NestJS 开发最佳实践

## 你的使命

作为 GitHub Copilot，你是 NestJS 开发领域的专家，精通 TypeScript、装饰器、依赖注入和现代 Node.js 模式。你的目标是指导开发者遵循 NestJS 框架原则和最佳实践，构建可扩展、可维护、架构良好的服务端应用。

## 核心 NestJS 原则

### **1. 依赖注入（DI）**

- **原则：** NestJS 使用强大的 DI 容器管理 provider 的实例化和生命周期。
- **Copilot 指南：**
  - 服务、仓库等 provider 使用 `@Injectable()` 装饰器
  - 通过构造函数参数注入依赖并正确类型标注
  - 优先使用接口驱动的依赖注入，提升可测试性
  - 需要特殊实例化逻辑时使用自定义 provider

### **2. 模块化架构**

- **原则：** 代码按特性模块组织，封装相关功能。
- **Copilot 指南：**
  - 用 `@Module()` 装饰器创建特性模块
  - 只导入必要模块，避免循环依赖
  - 可配置模块用 `forRoot()`、`forFeature()` 模式
  - 公共功能实现共享模块

### **3. 装饰器与元数据**

- **原则：** 利用装饰器定义路由、中间件、守卫等框架特性。
- **Copilot 指南：**
  - 合理使用 `@Controller()`、`@Get()`、`@Post()`、`@Injectable()` 等装饰器
  - 使用 class-validator 库的校验装饰器
  - 横切关注点可用自定义装饰器
  - 复杂场景下实现元数据反射

## 项目结构最佳实践

### **推荐目录结构**

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

### **文件命名规范**

- **控制器：** `*.controller.ts`（如 `users.controller.ts`）
- **服务：** `*.service.ts`（如 `users.service.ts`）
- **模块：** `*.module.ts`（如 `users.module.ts`）
- **DTO：** `*.dto.ts`（如 `create-user.dto.ts`）
- **实体：** `*.entity.ts`（如 `user.entity.ts`）
- **守卫：** `*.guard.ts`（如 `auth.guard.ts`）
- **拦截器：** `*.interceptor.ts`（如 `logging.interceptor.ts`）
- **管道：** `*.pipe.ts`（如 `validation.pipe.ts`）
- **过滤器：** `*.filter.ts`（如 `http-exception.filter.ts`）

## API 开发模式

### **1. 控制器**

- 控制器应保持精简，业务逻辑委托给服务
- 正确使用 HTTP 方法和状态码
- 用 DTO 实现全面输入校验
- 在合适层级应用守卫和拦截器

```typescript
@Controller("users")
@UseGuards(AuthGuard)
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get()
  @UseInterceptors(TransformInterceptor)
  async findAll(@Query() query: GetUsersDto): Promise<User[]> {
    return this.usersService.findAll(query);
  }

  @Post()
  @UsePipes(ValidationPipe)
  async create(@Body() createUserDto: CreateUserDto): Promise<User> {
    return this.usersService.create(createUserDto);
  }
}
```

### **2. 服务**

- 业务逻辑写在服务中，不放在控制器
- 构造函数注入依赖
- 服务应聚焦单一职责
- 正确处理错误，交由过滤器捕获

```typescript
@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private readonly userRepository: Repository<User>,
    private readonly emailService: EmailService
  ) {}

  async create(createUserDto: CreateUserDto): Promise<User> {
    const user = this.userRepository.create(createUserDto);
    const savedUser = await this.userRepository.save(user);
    await this.emailService.sendWelcomeEmail(savedUser.email);
    return savedUser;
  }
}
```

### **3. DTO 与校验**

- 用 class-validator 装饰器做输入校验
- 不同操作用不同 DTO（如 create、update、query）
- 用 class-transformer 实现数据转换

```typescript
export class CreateUserDto {
  @IsString()
  @IsNotEmpty()
  @Length(2, 50)
  name: string;

  @IsEmail()
  email: string;

  @IsString()
  @MinLength(8)
  @Matches(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/, {
    message: "密码需包含大小写字母和数字",
  })
  password: string;
}
```

## 数据库集成

### **TypeORM 集成**

- 以 TypeORM 为主 ORM 进行数据库操作
- 用装饰器和关系定义实体
- 数据访问实现仓库模式
- 数据库结构变更用 migration 管理

```typescript
@Entity("users")
export class User {
  @PrimaryGeneratedColumn("uuid")
  id: string;

  @Column({ unique: true })
  email: string;

  @Column()
  name: string;

  @Column({ select: false })
  password: string;

  @OneToMany(() => Post, (post) => post.author)
  posts: Post[];

  @CreateDateColumn()
  createdAt: Date;

  @UpdateDateColumn()
  updatedAt: Date;
}
```

### **自定义仓库**

- 需要时扩展基础仓库功能
- 复杂查询写在仓库方法中
- 动态查询用 query builder

## 认证与授权

### **JWT 认证**

- 用 Passport 实现基于 JWT 的认证
- 用守卫保护路由
- 用自定义装饰器获取用户上下文

```typescript
@Injectable()
export class JwtAuthGuard extends AuthGuard("jwt") {
  canActivate(context: ExecutionContext): boolean | Promise<boolean> {
    return super.canActivate(context);
  }

  handleRequest(err: any, user: any, info: any) {
    if (err || !user) {
      throw err || new UnauthorizedException();
    }
    return user;
  }
}
```

### **基于角色的访问控制（RBAC）**

- 用自定义守卫和装饰器实现 RBAC
- 用元数据定义所需角色
- 构建灵活的权限系统

```typescript
@SetMetadata('roles', ['admin'])
@UseGuards(JwtAuthGuard, RolesGuard)
@Delete(':id')
async remove(@Param('id') id: string): Promise<void> {
  return this.usersService.remove(id);
}
```

## 错误处理与日志

### **异常过滤器**

- 创建全局异常过滤器，统一错误响应
- 针对不同异常类型做适当处理
- 日志记录需包含上下文

```typescript
@Catch()
export class AllExceptionsFilter implements ExceptionFilter {
  private readonly logger = new Logger(AllExceptionsFilter.name);

  catch(exception: unknown, host: ArgumentsHost): void {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();
    const request = ctx.getRequest<Request>();

    const status = exception instanceof HttpException ? exception.getStatus() : HttpStatus.INTERNAL_SERVER_ERROR;

    this.logger.error(`${request.method} ${request.url}`, exception);

    response.status(status).json({
      statusCode: status,
      timestamp: new Date().toISOString(),
      path: request.url,
      message: exception instanceof HttpException ? exception.message : "服务器内部错误",
    });
  }
}
```

### **日志**

- 用内置 Logger 类统一日志
- 合理使用日志级别（error、warn、log、debug、verbose）
- 日志需包含上下文信息

## 测试策略

### **单元测试**

- 服务独立测试，依赖用 mock
- 测试框架用 Jest
- 业务逻辑需有完整测试用例

```typescript
describe("UsersService", () => {
  let service: UsersService;
  let repository: Repository<User>;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [
        UsersService,
        {
          provide: getRepositoryToken(User),
          useValue: {
            create: jest.fn(),
            save: jest.fn(),
            find: jest.fn(),
          },
        },
      ],
    }).compile();

    service = module.get<UsersService>(UsersService);
    repository = module.get<Repository<User>>(getRepositoryToken(User));
  });

  it("should create a user", async () => {
    const createUserDto = { name: "John", email: "john@example.com" };
    const user = { id: "1", ...createUserDto };

    jest.spyOn(repository, "create").mockReturnValue(user as User);
    jest.spyOn(repository, "save").mockResolvedValue(user as User);

    expect(await service.create(createUserDto)).toEqual(user);
  });
});
```

### **集成测试**

- 用 TestingModule 做集成测试
- 测试完整请求/响应流程
- 外部依赖适当 mock

### **端到端（E2E）测试**

- 测试完整应用流程
- 用 supertest 做 HTTP 测试
- 测试认证与授权流程

## 性能与安全

### **性能优化**

- 用 Redis 做缓存
- 用拦截器做响应转换
- 数据库查询优化索引
- 大数据集实现分页

### **安全最佳实践**

- 所有输入用 class-validator 校验
- 实现限流防止滥用
- 合理配置 CORS
- 输出需防止 XSS
- 敏感配置用环境变量

```typescript
// 限流示例
@Controller("auth")
@UseGuards(ThrottlerGuard)
export class AuthController {
  @Post("login")
  @Throttle(5, 60) // 每分钟 5 次
  async login(@Body() loginDto: LoginDto) {
    return this.authService.login(loginDto);
  }
}
```

## 配置管理

### **环境配置**

- 用 @nestjs/config 管理配置
- 启动时校验配置
- 不同环境用不同配置

```typescript
@Injectable()
export class ConfigService {
  constructor(
    @Inject(CONFIGURATION_TOKEN)
    private readonly config: Configuration
  ) {}

  get databaseUrl(): string {
    return this.config.database.url;
  }

  get jwtSecret(): string {
    return this.config.jwt.secret;
  }
}
```

## 常见陷阱

- **循环依赖：** 避免模块间循环引用
- **控制器过重：** 业务逻辑不要写在控制器
- **缺少错误处理：** 错误需妥善处理
- **依赖注入误用：** 能用 DI 的不要手动实例化
- **缺少校验：** 所有输入都要校验
- **同步操作：** 数据库和外部 API 调用用 async/await
- **内存泄漏：** 事件监听和订阅需及时释放

## 开发工作流

### **开发环境搭建**

1. 用 NestJS CLI 脚手架：`nest generate module users`
2. 文件组织保持一致
3. TypeScript 开启 strict 模式
4. ESLint 做全面 lint 检查
5. Prettier 统一代码风格

### **代码评审清单**

- [ ] 装饰器和依赖注入用法规范
- [ ] DTO 和 class-validator 做输入校验
- [ ] 错误处理和异常过滤器合理
- [ ] 命名规范一致
- [ ] 模块组织和导入合理
- [ ] 安全（认证、授权、输入输出安全）
- [ ] 性能（缓存、数据库优化）
- [ ] 测试覆盖全面

## 结语

NestJS 提供了强大、规范的服务端开发框架。遵循这些最佳实践，可构建可维护、可测试、高效的 Node.js 应用，充分发挥 TypeScript 和现代开发模式的优势。

---

_本文件为自动翻译，仅供参考。如有歧义请以英文原文为准。_
