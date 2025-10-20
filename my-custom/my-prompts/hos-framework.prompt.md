---
description: 'HOS框架开发规范'
---

# HOS 框架开发规范

## 技术栈

### 前端

- Nodejs：14.17.3
- Vue：^2.6.11
- HosUI：^1.0.0
- axios：^0.25.0
- vue-cli：4.5.14
- vue-i18n：^8.27.0
- webpack：5.52.1

### 后端

- JDK：1.8
- Spring Boot：2.7.11
- Spring Cloud：2021.0.7
- Spring Cloud Alibaba：2021.0.5.0
- mysql/Oracle/人大金仓/南大通用/高斯/达梦：mysql8.0+/Oracle 11gr2/KingbaseES V9R1/GBase 8S/8C/OpenGauss5.0.3/DM8
- Druid：1.2.4
- Mybatis/Mybatis Plus：3.5.9/3.5.1
- Jackson：2.13.5
- Apache CommonUtils/Hutools：5.8.5
- jjwt：0.9.0
- poi：4.1.2
- Slf4J+Logback：1.7.36+1.2.12
- redis：6.0
- Nacos：2.2.0
- Open Feign：3.17
- Gateway：3.1.7
- Redisson：7.15.2
- xxl-Job：2.2.0
- ELK：6.5
- ElasticSearch：7.17.9
- Sentinel：1.8.6
- Seata：1.4.1
- Prometheus：2.22.1
- SonarQube：9.2
- Skywalking：8.7.0

## 工程结构

### 前端结构

```text
hos
├── node_modules           # 项目依赖包
├── public                # 模板文件，包含 environment.js 等全局配置
├── src                   # 项目资源主目录
│   ├── biz               # 业务代码目录
│   │   ├── api           # 接口配置
│   │   ├── assets        # 静态文件
│   │   ├── axios         # 自定义拦截器
│   │   ├── components    # 通用组件
│   │   ├── constant      # 静态常量
│   │   ├── directive     # 自定义指令
│   │   ├── enum          # 全局枚举
│   │   ├── i18n          # 国际化配置
│   │   ├── store         # vuex 配置
│   │   ├── styles        # 公共样式
│   │   ├── utils         # 工具方法
│   │   └── views         # 页面
│   ├── sys               # 系统代码目录
│   │   ├── hos-base-mdm  # 基础主数据模块
│   │   ├── hos-app-base  # 基础模块
│   │   └── ...           # 其他系统模块
│   ├── defaultSettings   # 默认配置项
│   ├── main.js           # 主入口
│   └── permission.js     # 路由守卫
├── static                # 静态资源（hisUI页面等）
├── vue.config.js         # Vue 配置
├── .env                  # 环境变量配置
└── ...                   # 其他文件
```

#### 主要模块说明

- **biz/**：业务相关代码，包含接口、页面、工具、组件等。
- **sys/**：系统级模块，hos-base-app 为基础模块，新增框架可平级扩展。
- **static/**：hisUI 页面及菜单配置。
- **main.js**：应用主入口。
- **permission.js**：全局路由守卫。
- **vue.config.js**：构建与打包配置，含插件、别名、代理等。
- **.env**：环境变量，后端地址、加密、登录等参数。
- **public/environment.js**：全局变量定义，配合 returnGlobalValue 方法使用。
- **defaultSettings/**：首页、缓存、多页签等默认配置。

#### 业务模块结构示例

```text
views/
├── user/           # 用户模块
│   ├── index.vue
│   ├── components/
│   └── dialog/
├── system/         # 系统设置模块
├── order-manage/   # 订单管理模块
└── ...
```

#### API 目录结构示例

```text
api/
├── common.js    # 基础模块接口
├── staff.js     # 用户模块接口
├── system.js    # 系统模块接口
└── ...
```

#### 项目别称（路径别名）

| 别名        | 目录路径                    | 说明         |
| ----------- | --------------------------- | ------------ |
| @           | biz                         | 业务目录     |
| @src        | ./                          | 工程目录     |
| @core       | sys                         | 系统目录     |
| @base       | sys/hos-app-base            | 系统基础模块 |
| @components | sys/hos-app-base/components | 公共组件     |

> 新增别名需在 vue.config.js 中配置。

### 后端结构

采用微服务/单体双模工程结构，支持一套代码同时满足单体和微服务两种部署方式。

```text
oa-mediway-boot
├── oa-business-parent                  # 业务相关模块根目录
│   ├── hos-app                         # 基础平台模块
│   │   ├── hos-app-cloud-runner        # 基础平台微服务启动模块
│   │   │   ├── src/main/java/com.mediway/hos
│   │   │   │   ├── HosSecurityConfig.java      # 安全配置类
│   │   │   │   ├── SecurityLoginConfig.java    # 登录配置类
│   │   │   │   └── HosApplication.java         # 启动类
│   │   │   └── src/main/resource
│   │   │       ├── application.yml             # 模块配置文件
│   │   │       ├── application-dev.yml
│   │   │       └── logback-spring.xml
│   │   ├── hos-app-message              # 基础平台消息模块
│   │   │   ├── hos-app-message-cloud-runner
│   │   │   │   ├── src/main/java/com.mediway/hos
│   │   │   │   │   ├── HosSecurityConfig.java
│   │   │   │   │   ├── SecurityLoginConfig.java
│   │   │   │   │   └── HosMessageApplication.java
│   │   │   │   └── src/main/resource
│   │   │   │       ├── application.yml
│   │   │   │       ├── application-dev.yml
│   │   │   │       └── logback-spring.xml
│   ├── oa-contract                      # 合同业务模块
│   │   ├── oa-contract-api              # 对外接口模块
│   │   │   └── com.mediway/oa.contract/api
│   │   ├── oa-contract-controller       # 控制模块
│   │   │   └── com.mediway/oa.contract/controller
│   │   ├── oa-contract-cloud-runner     # 微服务启动模块
│   │   │   ├── src/main/java/com.mediway/hos
│   │   │   │   ├── HosSecurityConfig.java
│   │   │   │   ├── SecurityLoginConfig.java
│   │   │   │   └── ContractApplication.java
│   │   │   └── src/main/resource
│   │   │       ├── application.yml
│   │   │       ├── application-dev.yml
│   │   │       └── logback-spring.xml
│   │   ├── oa-contract-model            # 实体模块
│   │   │   └── com.mediway/oa.contract/model
│   │   │       ├── entity               # 实体类，需继承BaseEntity
│   │   │       └── vo                   # 视图对象
│   │   ├── oa-contract-service          # 服务模块
│   │   │   └── com.mediway/oa.contract/service
│   │   │       ├── annotation           # 自定义注解
│   │   │       ├── config               # 配置类
│   │   │       ├── constant             # 常量类
│   │   │       ├── enums                # 枚举类
│   │   │       ├── exception            # 异常类
│   │   │       ├── filter               # 过滤器
│   │   │       ├── mapper               # 继承BaseMapper
│   │   │       ├── service              # 继承BaseService
│   │   │       │   └── impl             # 继承BaseServiceImpl
│   │   │       └── utils                # 工具类
│   │   │   └── src/main/resource/contract
│   │   │       └── XXMapper.xml         # Mybatis映射文件
│   ├── oa-boot-runner                   # 单体启动模块，包含统一启动类和配置文件
│   │   ├── src/main/java/com.mediway/OAApplication.java
│   │   └── src/main/resource
│   │       ├── application.yml
│   │       ├── application-dev.yml
│   │       └── logback-spring.xml
│   ├── oa-user                          # 用户业务模块，结构同合同模块
│   │   ...
├── oa-doc                               # 项目文档，如初始化SQL等
├── oa-generator                         # 代码生成器
```

#### 主要说明

- 每个业务模块分为 api、controller、model、service、cloud-runner 等子模块，便于解耦和复用。
- 支持单体和微服务双模式部署，启动方式灵活。
- 依赖关系：api 依赖 model，service 依赖 model，controller 依赖 service 和 api，boot-runner 依赖所有 controller，cloud-runner 依赖 controller。

## 代码规范

以下规范基于 HOS 官方规范页梳理，提炼为便于 GitHub Copilot 理解与辅助生成代码的要点与示例。请在新项目与代码评审中一致执行。

### 前端规范

- 通用
  - 统一使用 ES2015+ 与 Vue 2 SFC（.vue）。禁止使用 eval/with。优先模块化与按需加载。
  - 文件/目录命名：kebab-case（短横线），资源小写；组件名使用 PascalCase。
  - 严禁将敏感信息硬编码到前端代码与仓库（遵循“安全与 OWASP”附录）。
- CSS/SASS
  - 选择器语义化、层级浅（<= 3 层），避免使用 id 选择器与 !important；公共主题变量集中在样式变量文件。
  - 单位：0 无单位；字体 rem；长度优先 px/rem；颜色统一十六进制小写；通过 Autoprefixer 处理前缀。
  - SASS 使用 @use/@forward 管理变量与 mixin；模块内样式使用 scoped；样式文件按功能拆分。
- HTML
  - 语义化标签，属性/标签小写；图片必须有 alt；禁止内联样式；head 设置 charset、viewport、lang。
  - 资源加载：CSS 放 head，JS 尾部或使用异步策略；合理使用 defer。
- JavaScript
  - 变量 const/let；严格相等 ===；模板字符串；解构与展开；禁止 var；单一职责函数。
  - 命名：变量/函数 camelCase，类 PascalCase，常量 UPPER_SNAKE_CASE。
  - 注释：JSDoc/行内注释阐述“为什么”；避免无意义注释；TODO/FIXME 标记需跟踪。
- Vue
  - 组件名 PascalCase；单文件组件三段顺序：template/script/style；样式使用 scoped。
  - props 声明类型、默认值与必填；禁止直接修改 props；使用 computed 派生数据；emit 明确定义事件。
  - 路由命名规范化，按路由切分懒加载；避免滥用 v-html（如必须使用请先用 DOMPurify 等进行白名单清洗，防 XSS）。
  - 目录结构：业务放 biz，系统模块放 sys；公用组件放 sys/hos-app-base/components；保持与工程结构章节一致。
- 纯净版/主题约定（节选）
  - 查询区布局统一；弹窗宽度/间距遵循设计规范；统一交互与空态、加载态。

示例 - 安全渲染文本（防 XSS）：

```vue
<template>
  <div>{{ safeText }}</div>
  <!-- 避免 v-html；如必须使用，先消毒：-->
  <!-- <div v-html="sanitizedHtml" /> -->
  <!-- 使用 DOMPurify 之类库：sanitizedHtml = DOMPurify.sanitize(userHtml) -->
  <!-- 并限制允许标签与属性白名单 -->
</template>
<script>
export default {
  name: 'UserCard',
  props: { text: { type: String, default: '' } },
  computed: {
    safeText() {
      return String(this.text || '');
    },
  },
};
</script>
<style scoped>
.user-card {
  padding: 12px;
}
</style>
```

### 后端规范

- 命名
  - 包小写，类 PascalCase，方法/变量 camelCase，常量 UPPER_SNAKE_CASE，枚举名为名词单数。
  - 通用 CRUD 命名：getById/listBy.../create/save/update/remove/delete 等，保持语义一致。
- 注释
  - 类/方法使用 Javadoc，说明职责、参数、返回值与异常；作者与创建时间按团队约定控制（避免无意义噪音）。
- 日志

  - 使用 SLF4J 占位符，严禁字符串拼接、System.out、printStackTrace；根据场景选择级别（error/warn/info/debug）。
  - 仅在边界处记录异常（记录一次）；大量 debug 日志需 isDebugEnabled 守护避免性能损耗。
  - 日志含关键业务上下文（但不包含敏感信息明文）。

  示例 - 参数化日志与异常：

  ```java
  private static final Logger log = LoggerFactory.getLogger(UserService.class);
  try {
  		userRepo.save(user);
  		log.info("User saved. id={}, name={}", user.getId(), user.getName());
  } catch (DataAccessException ex) {
  		log.error("Persist user failed. id={}", user.getId(), ex); // 记录一次并抛出业务异常
  		throw new BizException("USER_SAVE_FAILED", ex);
  }
  ```

- 异常处理
  - 预检查优于捕获运行时异常；不以异常作为流程控制；资源使用 try-with-resources；禁止捕获 Throwable。
  - 统一返回体（见“接口数据结构规范”）；自定义业务异常分类清晰；避免吞异常。
- 安全
  - 入参校验（JSR-303/@Validated）；鉴权与鉴定；输出脱敏；严禁 SQL 拼接（统一使用 MyBatis #{} 占位）。
  - 防止 XSS/CSRF/重放/SSRF/路径遍历：
    - 跳转使用白名单；上传/文件访问校验路径、后缀与大小；对外请求基于严格 allow-list。
  - 加密与密钥：禁止硬编码凭证；通过环境变量/密钥管理服务注入。
- 单元测试
  - 遵循 AIR 原则（Automatic/Independent/Repeatable）；最少编写 happy path + 1-2 个边界用例；尽量隔离外部依赖（Mock）。
- 性能
  - 避免在循环中访问 DB/Redis/远程服务；优先批量/分页；只查询需要字段；合理使用缓存与过期策略。
- 接口
  - RESTful：路径使用名词复数，方法语义与 HTTP 动作对齐（GET/POST/PUT/DELETE）。
  - JSON UTF-8；毫秒/时间戳或 ISO-8601 标准；超大整型以字符串传输；URL 长度限制与分页边界校验。
- 设计与流程
  - 单一职责、组合优于继承、依赖倒置、开闭原则、DRY；必要时补充状态/时序/类图辅助沟通与评审。

### 数据库规范

- 命名与结构
  - 数据库/表/字段小写下划线；表前缀建议 hos*（临时 hos_tmp*，视图 hos*v*）。
  - 主键：优先使用 UUID（CHAR(32)/VARCHAR(32)），或与业务一致的雪花/序列；布尔字段命名 is_xxx。
  - 标准审计字段：id、create_time、update_time、create_by、update_by、is_deleted 等。
- 类型与约束
  - 金额使用 DECIMAL(precision, scale)；定长使用 CHAR，变长使用 VARCHAR；大文本 TEXT 慎用。
  - 字段 NOT NULL + 合理默认值；字符集/排序规则统一。
- 索引
  - 命名：主键 pk*表名*列，唯一 uk*表名*列，普通 idx*表名*列；遵循最左匹配；避免低选择性列。
  - 为 JOIN/过滤/排序字段建索引；覆盖索引与前缀索引按需；避免在索引列上做函数/隐式类型转换。
- SQL 编写
  - 严禁拼接 SQL；使用预编译/占位符；避免 SELECT \*；控制 IN 列表大小；优先 EXISTS 替代 COUNT 大表扫描。
  - 禁用外键/级联（由服务层保证数据一致）；谨慎 TRUNCATE；分页优化（覆盖索引/游标/延迟关联）。
- ORM（MyBatis/Plus）
  - 使用 resultMap/显式列映射；占位使用 #{} 而非 ${}；避免 Map 直接输出；更新自动维护 update_time。
  - 避免“大而全”更新语句；事务边界清晰；合理控制 N+1 查询。
- 多数据库兼容
  - 避免使用各库保留字作为对象名；必要时使用引用符；抽象差异（分页/时间/函数）并集中处理。

### Git 使用规范

- 分支模型
  - master：线上稳定分支。
  - feature/\*：从 master 拉取，用于功能开发；示例：feature-user-profile。
  - test-x.y.z：集成测试分支；从 master 拉取；POM 版本 x.y.z-SNAPSHOT。
  - release-x.y.z：预发布分支；从 master 拉取；POM 版本 x.y.z-RELEASE。
- 版本与合并流程
  - feature → test（集成与兼容性验证）→ release（发布验收）→ master（上线）。
  - 开发在个人功能分支完成，确保通过流水线与代码审查后合并。

### 接口数据结构规范

- 统一返回体：code/msg/data；code=200 表示成功，其他为失败；错误时 data 置空（null）。
- 分页返回：data 内含 total/size/current/records。

示例 - 成功返回：

```json
{
  "code": 200,
  "msg": "OK",
  "data": { "id": "123", "name": "Alice" }
}
```

示例 - 分页返回：

```json
{
  "code": 200,
  "msg": "OK",
  "data": {
    "total": 120,
    "size": 10,
    "current": 1,
    "records": [{ "id": "1", "name": "A" }]
  }
}
```

示例 - 失败返回：

```json
{
  "code": 500,
  "msg": "INTERNAL_ERROR",
  "data": null
}
```

### 组件集成规范

- 集成方式
  - 方式一：后端以组件 Jar 形式引入（企业私服/制品库管理依赖）。
  - 方式二：独立微服务对接（通过 OpenFeign/HTTP 调用）。
- 后端要求
  - 模块命名：hos-app-xxx；工程结构遵循“后端结构”章节（api/controller/model/service/cloud-runner）。
  - 配置命名：framework.<module>.\_；数据库表前缀 hos\_\_；完善说明文档与初始化脚本。
  - 示例（Maven 依赖，版本替换为实际发布版本）：
    ```xml
    <dependency>
    	<groupId>com.example.hos</groupId>
    	<artifactId>hos-app-xxx</artifactId>
    	<version>1.0.0-RELEASE</version>
    </dependency>
    ```
- 前端要求
  - 模块位置：src/sys/hos-app-xxx，与 hos-app-base 平级；遵循前端规范；公共组件复用。
  - 分支与权限：event_dev/test/release 命名；按仓库策略配置最小化权限、受保护分支与评审校验。

——
附：安全与 OWASP 要点（跨章节适用）

- 严格的访问控制与最小权限；后端“缺省拒绝”。
- 所有外部入参校验与清理；所有数据库访问使用参数化查询；所有跨端通信使用 HTTPS。
- 会话/令牌安全：HttpOnly/Secure/SameSite；敏感数据加密存储；密钥从环境或密管服务加载，禁止硬编码。
- 关键安全响应头：CSP/HSTS/X-Content-Type-Options 等；生产禁用调试与详细错误。

## 快速开发

### 后端开发

以下指引汇总自“quickStart/backend”文档，面向日常开发与 Copilot 辅助，提供最小可行步骤与安全要点。

#### 环境与工具

- JDK 1.8；Maven 3.6+；IDE 建议 IntelliJ IDEA（安装 Lombok、MyBatisX 插件）。
- 数据库按需选择（MySQL/Oracle/Kingbase/GBase/DM/OpenGauss 等），Redis 6.0，注册中心 Nacos 2.2.0。
- 秘密信息一律走环境变量或密管服务；禁止硬编码在配置或仓库。

Maven 私服（示例，替换占位符）：

```xml
<!-- settings.xml 中定义 mirror/profile（请使用企业私服地址与凭证占位符） -->
<mirrors>
  <mirror>
    <id>company-nexus</id>
    <mirrorOf>*</mirrorOf>
    <url>https://nexus.example.com/repository/maven-public/</url>
  </mirror>
  <!-- 其余 mirror 可按需配置 -->

</mirrors>
```

#### 运行项目（单体/微服务）

- 单体：启动 oa-boot-runner（统一 Application 与配置）；微服务：启动各业务模块 cloud-runner。
- 先启动基础组件（Nacos/DB/Redis），再启网关与业务服务；使用 dev/test 等 Spring profile。
- application.yml/application-dev.yml 常见项：数据源、注册中心地址、服务端口、日志；确保不同库的方言/驱动正确。

#### 新建业务模块

- 模块结构：api/controller/model/service/cloud-runner；包名小写分段，类名 PascalCase。
- 依赖关系：api→model；service→model；controller→service+api；cloud-runner→controller。

#### 第一个 CRUD（MyBatis-Plus）

- 实体：使用 @TableName/@TableId/@TableField，继承 BaseEntity（含分页与审计字段）。
- Mapper：继承 BaseMapper<Entity>；自定义 SQL 用 XML 编写（使用 #{} 占位符，禁止 ${} 拼接）。
- Service：继承 BaseService/BaseServiceImpl，封装领域逻辑；标注 @Transactional 按需控制事务边界。
- Controller：可继承 BaseController，统一返回体 BaseResponse{code/msg/data}。

分页查询（示例片段）：

```java
@GetMapping("/selectPage")
public BaseResponse<IPage<Staff>> selectPage(Staff staff){
  IPage<Staff> page = new Page<>(staff.getCurrent(), staff.getSize());
  return BaseResponse.success(staffService.selectPage(page, staff));
}
```

#### 复杂查询（多表/VO）

- 定义 VO 作为结果载体；Mapper XML 使用 JOIN 明确列映射（resultMap），避免 SELECT *。
- Service 组合查询条件；Controller 返回分页 IPage<VO>。

#### 调试登录与鉴权

- 获取 token：调用后端登录接口或按开发白名单策略放行特定路径（仅开发环境）。
- 前后端统一通过请求头携带令牌（如 Authorization: Bearer <token> 或 access-token），避免 query 传递。
- 严格区分开发与生产安全策略（生产禁用白名单绕过）。

#### 事务管理

- 在 Service 层使用 @Transactional(rollbackFor = Exception.class)；拆分长事务，避免跨服务分布式大事务（必要时使用可靠消息/补偿）。

#### 统一异常处理

- 业务异常 BizException 分类清晰，网关/Controller 只记录一次错误日志；全局异常处理器转换为统一返回体。

#### 接口文档（Swagger）

- 典型注解：@Api/@ApiOperation/@ApiImplicitParam 等；配置 Docket 后访问 /swagger-ui/。
- 生产环境限制文档暴露并加鉴权；文档即契约，参数与返回体与实现保持一致。

### 前端开发

以下指引汇总自“quickStart/frontend”文档，强调模块化、API 约定与安全实践。

#### 环境与 IDE

- Node.js 14+；Vue 2.6；HosUI 1.x。
- VS Code 建议安装：Vetur（必装）、中文语言包（必装）、Auto Rename Tag/Project Manager（可选）。
- 浏览器建议 Chrome 93+（或团队标准版本）。

#### 启动与连接后端

- 导入工程后配置后端地址（任选其一）：
  - devServer 代理：在 vue.config.js 的 devServer.proxy 中配置 '/api' → 后端网关地址。
  - 环境变量：.env.development 中设置 VUE_APP_BASE_URL='https://api.example.com'。
- 安装依赖使用企业私有 npm 仓库时，请使用 .npmrc/环境变量配置鉴权 Token，勿在文档或仓库泄露凭证。
- 运行：npm run serve。

#### 新建模块与路由

- 在 biz/views 下新建业务目录与页面（例如 user/staff/index.vue）。
- 在 biz/router/index.js 内添加静态路由：

```js
{
  path: '/user/staff',
  name: 'Staff',
  component: () => import('@/views/user/staff/index'),
}
```

#### 定义 API 与调用约定

- 模块前缀由 sys/hos-app-base/axios/modulesConfig 管理；业务模块 API 文件位于 biz/api/ 下。
- 可选 $config 覆盖模块的 baseURL（取自 VUE_APP_BASE_URL_* 环境变量）。
- 建议 API 形如：

```js
// biz/api/staff.js
export const selectPage = (params) => ({ url: '/user/staff/selectPage', method: 'get', params });
export const insert     = (data)   => ({ url: '/user/staff/insert',      method: 'post', data  });
export const updateById = (data)   => ({ url: '/user/staff/updateById',  method: 'post', data  });
export const deleteById = (id)     => ({ url: '/user/staff/deleteById',  method: 'post', params: { id } });
```

调用封装 $api（签名：module.file.apiName, params, headers）返回 Promise<data>：

```js
const query = { ...this.form, ...this.page };
this.$api('staff.selectPage', query).then((res) => {
  const { total, current, size, records } = res.data || {};
  this.tableData = records || [];
  this.page = { total, current, size };
});
```

#### 列表与表单（HosUI 组合）

- 列表：<hos-biz-table uid="..." :cols="..." data="staff.selectPage" :form="formObj">…</hos-biz-table>
- 弹窗：使用全局对话框 OPEN_DIALOG/CLOSE_DIALOG/UPDATE_TABLE 事件驱动交互；表单校验通过后调用保存 API 并刷新表格。

#### GET/POST 传参约定

- GET：参数经 params 拼接，后端以同名接收或 @RequestParam 指定。
- POST：主体在 data；如需混合参数，可在 data 与 params 分别传递并在后端使用 @RequestBody + 方法参数接收。

#### 安全与最佳实践

- 不在仓库提交真实地址/凭证；本地用 .env/.npmrc 覆盖并加入 .gitignore。
- 展示用户数据默认文本渲染，避免 v-html；如必须，先做白名单消毒（例如 DOMPurify），防 XSS。
- Axios 统一超时/重试与错误提示；对 401/403 做会话过期处理。

## 开发进阶

### 后端进阶（backendManual）

以下要点汇总自 developmentStage/backendManual，聚焦日常开发/排障与 Copilot 生成代码时的关键约束与示例。

- 产品名扩展（自定义应用名称）
  - 扩展点：实现并覆盖 SysConfigDataHandler.getAppName，返回产品/系统显示名称；确保包扫描能加载到实现类。
  - 验证：启动后检查登录页/关于页等处的产品名是否生效。

- 业务锁（并发互斥与防重复提交）
  - 服务接口：SysBusinessLockService.addLock(key, biz), hasLock(key, biz), unLock(key, biz)。
  - HTTP 接口：/api/sys/business-lock/addlock、/haslock、/unlock（POST/GET 视实现而定）。
  - 建议
    - 粒度选 key（如业务单号）+ biz（模块），超时自动释放；出错路径务必解锁（try/finally）。
    - 记录请求上下文，避免重复解锁/误解锁。

- 短信验证码（发送与校验）
  - 配置：yml 下 smscaptcha.*（网关、模板、开关、过期等）；密钥/账号放环境变量或密管，不入库与仓库。
  - 发送：CaptchaUtil.sendCaptcha(CaptchaSendVO)；校验：CaptchaUtil.checkCaptcha(id, code)。
  - 安全
    - 速率限制与图形验证码联动，防撞库与批量刷码；验证码仅短期有效并单次消费。

- 多数据库兼容（MyBatis _databaseId）
  - XML 中使用 <if test="_databaseId == 'mysql'">…</if> 条件片段，按库语法差异选择列/函数；避免在 Java 拼接 SQL。
  - 兼容点示例：分页函数、日期/字符串函数、布尔/空串比较、关键字引用。
  - 统一 Mapper 方法签名，返回字段命名与实体保持一致；优先 resultMap 明确列映射。

- 数据生命周期与操作日志（BussinessLogUtils）
  - 场景：单表、JOIN、父子（主从）、自定义；均可通过 LogProperty/BindProperty 描述“谁/何时/做了什么/前后值”。
  - 用法：BussinessLogUtils.processData(entity, props...) 或自定义组装 BussinessLogEntity；查看页支持时间线追溯。
  - 建议：仅记录必要字段并脱敏；异常只记录一次；批量操作记录汇总与明细分层。

- 数据权限（@DataScope + SQL 注入点）
  - 在 Mapper 方法上添加 @DataScope，入参携带 DataAuthParam；Mapper XML 在 where 中拼接 ${dataAuthParam.dataScopeSql}。
  - 前端通过 Header 传 component-code 标识组件场景，后端据此生成数据域限制（机构/科室/岗位/本人等）。
  - 安全：仅在已验证的 SQL 片段位置插入，外部条件一律使用 #{} 参数化，禁止 ${} 拼接不受控输入。

- 动态数据源（dynamic-datasource + @DS）
  - yml 定义多个数据源（如 master/slave/oracle），并指定默认；在方法或类上使用 @DS("slave") 切换。
  - 事务边界：同一事务内切源要谨慎，推荐“查询只读库、写入主库”并分事务；跨库一致性通过补偿/可靠消息。
  - 连接验证与健康检查：启动自检 URL/心跳 SQL，避免运行期首次调用失败。

- 动态参数（DynamicCustomParam/DynamicParamsUtil）
  - 定义实现类提供 code/value（如账号、机构、岗位、当前时间、token 等）；框架内置常用 code，可扩展业务专属。
  - 调用：DynamicParamsUtil.getValueByCode(code) / getAllValueMap()；适用于打印模板、导入/导出、规则引擎等场景。
  - 安全：动态取值中涉及身份信息应最小化、脱敏，严禁回传敏感标识。

以上特性均需遵循“安全与 OWASP”与“数据库/接口规范”：
  - 所有对外访问默认拒绝（Deny by default），白名单放行；所有 SQL 预编译；日志不落敏感数据。
  - 避免硬编码凭证/地址，改为环境变量占位；HTTP 统一 HTTPS；接口返回统一返回体并妥善处理错误码。

—

- 免密认证源登录（FreeAuth）
  - 场景：应用 A 免感知跳转应用 B；A 生成临时 token，B 调用 A 的校验接口换取用户信息后完成本地登录。
  - 菜单集成：配置目标 URL，开启“外链+免密”，设置“认证源编码”；A 侧在登录白名单中允许验证接口路径。
  - 故障排查：认证源未维护/URL 错误/临时 token 过期/用户不存在等分别定位到认证源配置与有效期校验。

- 后端国际化（数据国际化 i18n）
  - 存储/删除：I18nUtil.saveTransValue/saveBatchTransValue/deleteAllFieldBatchByLang；联合主键以“id1,id2”顺序拼接。
  - 查询自动翻译：实体字段使用 @HosI18nAutoTrans(tableName, fieldName, primary, i18nDataTable)。
  - 查询手动翻译：VO 字段使用 @HosI18nHandTrans；Service 中调用 I18nUtil.handTranslateList(...)；复杂/继承场景使用 I18nUtil.mapTransValue/…ByLang。
  - 模糊搜索：左联 hos_i18n_data 根据 language/field_code 匹配 translation 与源字段，兼容“开关关闭”时仅查源表。
  - 注意：仅对开启国际化的字段生效；请求头语言与默认语言需明确；为空是否显示原值受配置控制。

- 导入导出（Import/Export 管理）
  - 导入：
    - 管理维度：导入管理→sheet 管理→列管理。前置/后置可选 SQL 或 Spring Bean.method，自定义执行处理。
    - 列配置：唯一校验、字典项、关联表（表名/对比字段/静态条件/数据策略：逐条或全量预加载）、必填/长度/范围等。
    - 组件调用：sys 组件上传弹窗，传 moduleCode=规则编码；错误数据可下载校验反馈。
  - 导出：
    - 执行脚本：使用“JS 脚本生成 SQL 字符串”，根据导出类型（当前页/所选/查询）与 params 组装 SQL；严禁拼接外部未消毒输入。
    - 列/多表头/字典/关联表值转换与样式在“列管理”维护；前端用 <hos-biz-down> 传 code/ids/params。
  - 安全：
    - 严禁把真实连接/凭证写入配置；导入字段校验开启；导出脚本仅拼接受控字段与白名单排序，防注入。

- 第三方接口管理（Interface 管理）
  - 维护接口基本信息、入出参结构、测试与调用日志；结合“接口调用工具类”按配置发起请求。
  - 建议：统一鉴权/签名/重试策略封装；敏感 header 与秘钥走环境变量；回调/SSRF 强校验（域名/IP/端口/协议）。

- 接口权限（全局拦截器 + 注解 AOP）
  - 全局拦截器：基于资源路由与角色授权的中央校验；无需在代码标注。
  - 注解+AOP：在类/方法上使用 @PreAuth("permissionAll()|hasPermission('code')")；自定义 IPermissionHandler 校验角色与权限码。
  - 原则：类与方法同时存在时，以类级为准；开发者账号放行仅限开发环境；权限数据支持导入导出与生命周期查询。

- 生产许可（License）
  - 配置：framework.security.license.enable/name/version 等；开发环境可临时关闭；客户环境不应留有 enable 开关条目。
  - 激活：按引导获取机器码→BOS 申请→安装许可证→查看关于页信息；不匹配会禁止登录。

- 打印设计器（Lodop 模板）
  - 设计：可视化拖拽文本/长文本/图片/条码/二维码/表格/套打/线/矩形/椭圆/自定义 HTML；支持数据集/打印入参映射。
  - 调用：
    - iframe 方式：postMessage 调用父页 preview/print/getHtmlStr/getBase64 等；
    - 组件方式：<lodop-vue ref="lodopRef" :code :param>，调用 previewFn/printFn；不使用插件时传 printType='web'。
  - 自定义控件：在 src/biz/constant/lodop-custom-plugin 下以 JSON 扩展控件/属性/格式化函数。
  - 注意：接口需带 token 与 language 等动态头；图片优先 base64；确保浏览器/插件安装与安全策略。

- 登录与统一认证（表单/单点/扩展认证）
  - 表单：简版/精简版/专业版；岗位/岗位单元可作为登录上下文；登录日志策略 sync/async 可配置。
  - 单点（OAuth2）：在 yml 配置 issuer/authorization-uri/client-id/secret/redirect-uri，前后端地址用环境变量占位；仅在受信网络启用。
  - Token 策略：access/refresh 过期/刷新开关/签名 key/缓存前缀可配；续期忽略的接口通过 framework.security.renewal.ignores 配置。
  - 认证白名单：
    - 方式一：每模块 resources/META-INF/hos-security.factories（security-white=…）。
    - 方式二：yml hos-security.white-list 数组。
    - SecurityFilterChain 中合并与放行，其他路径默认鉴权。
  - 自定义认证：
    - 定义 Param（继承 AbstractHosLoginParam）与 Token（继承 AbstractHosAuthenticationToken）；
    - Converter 将请求映射为自定义 Token；Provider 载入用户并校验（验证码、短信码、策略、锁定/计数等）；
    - 在 SecurityLoginConfig 中注册 Converter/Provider；调用 /api/security/token?grantType=xxx 完成登录。



—

- 开放接口（OpenAPI）
  - 标注：在 Controller 方法上使用 @OpenApi(code, name, module, needToken, needSign...) 暴露接口；仅当在“开放接口管理”启用并绑定应用后可访问。
  - 路径与令牌：根据配置 restfulPath 形成统一前缀；调用 /api/openApi/openapibase/apisystem/getAcessToken 以 appId/appSecret 换取 apiAccessToken；后续请求使用 HTTPS，并在 Header 添加 apiAccessToken（及签名/时间戳/随机串防重放）。
  - 安全与配额：默认拒绝；启用签名校验、IP 白名单与频率限制；错误只返回必要信息，不暴露堆栈；回调/转发目标采用域名 allow-list 防 SSRF。

- PageOffice 打印与模板
  - 依赖与授权：引入 hos-app-print 组件；安装浏览器插件，按指引在线/离线激活 License；生产环境禁用调试开关。
  - 模板管理：支持新增/编辑/复制/删除；可定义数据集、字段映射、图片（base64/URL）、套打、多表头/分组、清除空行、纸张/边距/坐标等。
  - 前端调用：openPageOffice({ code/templateName, params, isPreview, sourceType })；支持预览或直接打印，并落打印日志；图片建议使用 base64，接口需携带 token 与 language 等动态头。
  - 故障排查：插件未安装/权限受限、字体缺失、打印机纸张不匹配（优先“取打印机纸张”）、跨域图片加载失败等。

- 打印模板与 Lodop 对比
  - Lodop：<lodop-vue ref="lodopRef" :code :param>，调用 previewFn/printFn；可用 printType='web' 无插件打印（能力受限）。
  - 选型建议：需要精确控件/套打/复杂模板时优先 PageOffice；轻量预览/简单票据可用 Lodop Web 模式。

- Redis 键事件监听
  - Redis 配置：开启 notify-keyspace-events=Egx 以接收过期/删除事件；生产建议按需开启，避免广播噪声。
  - Spring 监听：实现 KeyExpirationEventMessageListener/KeyDeleteEventMessageListener，并在配置类（可继承 RedisKeyListenConfig）注册；处理函数对 message.toString() 做幂等、鉴权与输入校验。
  - 集群注意：各节点参数需一致；跨分片事件仅在本分片触发；幂等与重试策略必备。

- 启动扩展与自动配置（安全配置装配）
  - 自动装配：自定义 @Configuration 使用 @AutoConfigureBefore/After 控制顺序；在 META-INF/spring.factories 中注册 EnableAutoConfiguration=...YourConfig。
  - 常见用途：扩展 SecurityFilterChain（白名单/鉴权策略）、注册自定义 Converter/Provider、模块化装配顺序控制。
  - 约束：避免在自动配置执行耗时 IO；使用 @ConditionalOnProperty/@ConditionalOnClass 精准生效；默认安全策略“缺省拒绝”。

- 短信服务（SMS）
  - 统一入口：SmsSendUtil.send(key, SmsSendParam)；参数包括 signCode/templateId/phones/params/context/appId/sign。
  - 扩展点：实现 SmsSender（send/createSmsSender）以接入厂商；平台侧支持签名/模板维护、开关、重试与发送日志。
  - 安全：密钥与账号使用环境变量/密管注入；限流与熔断；日志脱敏（号码打码/上下文去除敏感信息）。

- 多租户（Tenant）
  - 字段隔离：开启 MyBatis-Plus TenantLineInnerInterceptor，yml 配置 enable/column=tenant_id 与 ignore-table；DAO 层自动注入租户条件。
  - 数据源隔离：结合 dynamic-datasource 为租户切换数据源；读写分离与跨库事务需谨慎，优先补偿/可靠消息替代分布式大事务。
  - 常见陷阱：ThreadLocal 泄漏导致串租；异步/定时任务需显式设置租户上下文；白名单表/库需在配置或注解（如 @IgnoreDS）中排除。
  - 初始化：维护租户字典、默认库结构与管理员账号初始化脚本；为公共数据表明确是否走租户隔离。

以上新增能力均需遵循“安全与 OWASP 要点”：默认拒绝、最小权限、参数化 SQL、HTTPS、密钥不入库/不入仓、错误信息最小化、日志不落敏感数据。

### 前端进阶（frontManual）

- 路由与菜单
  - 系统路由：`@sys/router/base-router.js`；业务路由：`@/router/index.js`；建议 Sider 菜单不超过三级。
  - 静态路由 vs. 静态菜单路由：使用懒加载 component: () => import('...')；路由 meta 建议：title/icon/keepAlive。
  - 权限路由：后端菜单到前端路由的映射工具位于 `@sys/utils/router/router.js`。

- 全局路由守卫
  - 入口：`src/permission.js`；在 beforeEach/afterEach 校验登录与权限，按需加载语言包与页面元素。

- 嵌入外部页面（His/内联）
  - 在“菜单管理”配置加载类型为“非 Vue 组件”或外链 iframe；必要时结合免密登录（FreeAuth）与白名单。
  - 全局打开菜单方法：window.top.hos_openMenu(menu) 支持传 path/code、query、params。
  - 标签页切换事件：window.addEventListener('message', e => { if (e.data.type==='afterTabSwitch') {...} })。

- 国际化（前端）
  - 页面元素通过 `$lang(key)` 获取；静态路由可在 meta.pageCode 标识页面唯一编码用于拉取元素集合。
  - 提供表格行内翻译组件与对话框；注意多选、联合主键 id 传递格式与权限指令配合。

- 环境变量与安全
  - 仅 NODE_ENV/BASE_URL/以 VUE_APP 开头的变量会注入客户端；不要在仓库提交真实地址/凭证。
  - 更新 .env 后需重启服务；避免在前端持久化敏感密钥（遵循“安全与 OWASP”）。

- Vuex 全局状态
  - 目录：`@/store`；核心概念 state/getters/mutations/actions/modules；使用 mapState/mapGetters/... 辅助函数。

- Axios 拦截器与模块化扩展
  - 业务自定义拦截器目录：`src/biz/axios/modules`（导出 requestSuccess/Fail、responseSuccess/Fail）。
  - 核心拦截器：`src/sys/hos-app-base/axios/interceptors.js`（token 注入、错误集中处理、白名单）。

- 全局方法与自定义扩展
  - 全局方法：window.top.hos_openMenu/hos_closeDialog/hos_refreshContent/hos_utils.ls.get 等。
  - 扩展入口：`/biz/bizMain.js`（注册插件/原型方法），`/biz/mixins/globalMixin.js`（通用逻辑复用），`/biz/mixins/loginMixin.js`（登录成功钩子），`/biz/config.js`（业务白名单/错误码容忍等）。

- 前端安全补充
  - XSS：默认文本渲染；如需 v-html，使用经过白名单消毒的内容（如 DOMPurify 或内置 $xss）。
  - CSRF/签名/加解密：按需启用 needSign/needCrypt/needDecrypt；密钥放后端或安全存储，不在前端硬编码。

### 接口集成（interfaceIntegrate）

- 常用系统接口（举例）
  - 数据字典：/sys/dict-category/select-sort-tree、/sys/dict/select-pcode?code=xxx。
  - 系统参数：/sys/config/select-init（登录后加载）。
  - 图标管理：/sys/icon/select-by-code?code=xxx。
  - 内联菜单：/sys/resource-inline/list-menu?resourceMId=...。
  - 登录用户与权限：/sys/hos-user-account/login-user-info、/sys/resources/permission-resource-code?postId=...
  - 约定：统一返回体 code/msg/data；携带 access-token；使用 HTTPS；分页与超时边界校验。

- 第三方接口配置与调用
  - 配置项（Interfaces）：code/name/category/type(rest/soap)/way(get/post)/protocol/http(s)/prefix/url/headers/body/params/返回映射/超时等。
  - Rest 调用工具：InterfaceUtil.executeRest(…)/executeRestByParams(…)/executeRestByBody(…) 支持自定义 headers/params/body 与超时。
  - SOAP 调用工具：executeSoap/executeSoapReturnJson + splicingMessage/xml2JsonStr；支持 SOAPHeader/Body 结构递归拼装。
  - 动态参数：结合 DynamicParamsUtil 取当前用户/机构/岗位/时间等上下文填充请求。
  - 安全与治理
    - 默认拒绝 + 允许名单：外部域名/IP/端口严格 allow-list，禁止透传未校验的 URL，防 SSRF。
    - 强制 HTTPS、签名/时间戳/随机串防重放；敏感头信息脱敏；配置凭证走环境变量/密管。
    - 统一超时/重试策略、失败降级与告警；避免在日志中记录明文敏感数据。

### 常用工具（commonUtils）

- SpringContextUtils：获取 Bean/判断是否存在/类型查询；避免过度使用造成耦合。
- ThreadLocalManager：在业务线程保存/获取/清理上下文；注意清理与异步传播，防止泄漏与串租。
- DesensitizationUtil：常见字段脱敏（手机号/身份证/邮箱等）。
- JwtUtil：生成/解析/验证 token；仅用于无敏感信息的声明；签名密钥来自安全配置，不硬编码。
- ExcelUtils：导入/导出 xls/xlsx 到文件或响应；列名别名 aliasMap 支持；控制文件大小与类型白名单。
- WebServiceUtil（CXF）/HttpUtil（HttpClient）：
  - 默认超时：连接/读取/连接池获取；支持自定义 RequestConfig；务必设置合理超时与重试上限。
  - 提供 GET/POST/PUT/DELETE + JSON/FORM/XML 便捷方法；Header 中中文需编码（URLEncoder/URLDecoder）。
  - Spring MVC 接收 put/delete 表单参数需注册 OrderedFormContentFilter。
- IPUtils/UUIDUtils/MD5Util/ExportPdfUtils/HosExcelUtil/QRCodeUtil/AccountUtil 等：
  - 典型能力：IP 获取与范围判断、UUID 生成、MD5（仅用于校验，不用于密码存储）、PDF 导出、Excel 自定义导入、二维码生成解析、登录上下文快速获取。

安全与合规要点（适用于本节全部能力）
- 不硬编码任何密钥/token/密码；通过环境变量或密钥管理服务注入。
- 对外 HTTP 统一 HTTPS；配置严格 allow-list；输出与日志默认脱敏；参数校验并拒绝非法输入。
- 设定连接/读取/整体请求超时；对重试/回退做好幂等与限流；防雪崩。



