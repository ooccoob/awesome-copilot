# 数据填报系统 — 架构草案

## 目标

为数据填报平台定义可交付的系统架构：支持表单模板定义、填报、审批、导入导出与审计；具备可伸缩性、安全性与可运维性。

## 高级组件

- 前端（单页应用）
  - 技术：Vue 3 + Vite 或 React + Vite
  - 组件：表单编辑器、填报页、列表/查询、审批工作台、导入/导出模块
- 后端 API 层
  - 技术：Spring Boot（Java）或 FastAPI（Python）
  - 职责：鉴权、表单模板管理、条目 CRUD、导入/导出任务、审计与权限检查
- 数据存储
  - 主存储：关系数据库（Postgres / Kingbase）
  - 附加：对象存储（S3 兼容）用于存放导入文件与导出文件
- 异步任务与队列
  - 技术：RabbitMQ / Redis Streams / Celery（若使用 Python）
  - 用途：处理大文件导入、导出、批量校验与统计任务
- 缓存
  - 技术：Redis
  - 用途：会话缓存、权限缓存、热点数据缓存
- 日志与监控
  - 日志：集中化（ELK / Loki）
  - 指标：Prometheus + Grafana
- CI/CD
  - 构建、测试、镜像发布、部署到 staging/production

## 数据流（简化）

1. 用户请求（浏览器） -> API 网关 / 后端（认证中间件）
2. 后端读取/写入关系型数据库
3. 大文件上载到对象存储，后端创建导入任务（写入任务表）并推送到消息队列
4. 异步 worker 拉取任务，处理并将结果写回数据库或对象存储，状态通知用户
5. 操作与变更写入审计日志表，必要时同步到日志平台

## API 边界（概览）

- /api/v1/auth/* : 登录、登出、用户信息
- /api/v1/forms/* : 表单模板管理（CRUD、预览）
- /api/v1/entries/* : 填报条目（CRUD、提交、状态流转、导出）
- /api/v1/import : 上传并创建导入任务（异步）
- /api/v1/export : 导出请求与状态
- /api/v1/audit : 审计日志查询

## 鉴权与权限模型

- 认证：OAuth2 / JWT（Access Token + Refresh Token）或基于 Session（HttpOnly Cookie）
- 授权：RBAC（角色 -> 权限），资源级权限扩展（例如：按表单模板的拥有者或组织隔离）
- 安全：API 强制 HTTPS，参数/文件校验，SSRF/文件路径限制，严格的 CORS 策略

## 非功能需求（NFR）

- 可用性：99.9%（示例）
- 性能：常规 API 响应 < 300ms（在合理负载下）
- 可扩展性：后端无状态，水平扩展；异步工作者分离扩展
- 数据保留：审计日志按策略归档至对象存储或冷存储
- 合规性/安全：敏感字段加密存储（如需要），访问审计

## 部署拓扑（简述）

- Kubernetes 集群（推荐）
  - Deployment：api, workers, frontend
  - StatefulSet：数据库（或外部托管 DB）
  - Redis、消息队列作为独立服务或托管服务
  - 存储：对象存储（S3 或兼容服务）
- 备份：数据库定期备份、对象存储备份策略

## 关键决策点与选项

- 如果组织已有 Kingbase/Postgres，优先复用以降低运维成本
- 导入导出为异步任务，避免阻塞 API 响应
- 表单 schema 采用 JSON Schema 可复用且易于渲染

## 下一步（可执行）

1. 细化数据库 schema（核心表：form_templates, entries, users, roles, audit_logs, import_tasks）
2. 完善 OpenAPI（为每个端点补全请求/响应 schema 与错误码）
3. 设计表单模板的 JSON Schema 规范并提供示例
4. 生成后端 stub（Spring Boot 或 FastAPI）并搭建 CI

## 验收标准（设计阶段）

- 完整的架构文档包含组件图、数据流、部署拓扑与 NFR
- OpenAPI 草案与核心 DB 模式草案存在
- 关键风险与缓解措施列出

---
文档路径：`design/architecture/architecture.md`
