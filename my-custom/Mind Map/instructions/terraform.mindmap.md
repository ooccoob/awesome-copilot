## What
- Terraform 通用规范：安全、模块化、可维护、风格/文档/测试

## When
- 编写/审查任何 Terraform 配置时

## Why
- 降低风险、提升可读性与复用性，加速 plan/apply 并减少隐患

## How
- 安全
  - 固定稳定版本；Secrets 管理器/参数存储；永不入库；变量/输出标记 sensitive；最小权限；私网优先；全链路加密
- 模块化
  - 大块拆项目；模块封装相关资源；避免过度抽象与环依赖；通过 outputs 暴露必要信息
- 维护
  - 注释解释“为什么”；变量代替硬编码；恰当 data source；locals 统一重复值
- 风格
  - 一致命名；缩进 2；分组文件与资源；depends_on/for_each/count 放在开头、lifecycle 结尾；排序与空行
  - terraform fmt/validate/tflint 常跑
- 文档
  - 变量/输出含 type+description；README；terraform-docs 生成
- 测试
  - .tftest.hcl 覆盖正负场景；幂等

## Key Points
- 避免不必要 data sources；优先模块参数
- 用 maps for_each 稳定地址

## Compact Map
- 安全: 版本/密钥/权限/加密
- 模块: 分层/输出
- 维护: 注释/变量/locals
- 风格: 缩进/排序/分区
- 文档: 描述/README
- 测试: tftest

## Example Questions
1) 哪些变量/输出缺少描述或类型？
2) 哪些敏感项需要标记/迁移到 Secret 管理？
3) 哪些 data 源可以被参数替代？
4) for_each 与 count 是否选择得当？
5) 有无冗余 depends_on？
6) 哪些资源应拆分到模块？
7) 哪些输出可删除或设为 sensitive？
8) tflint/validate 是否已集成到 CI？
9) 测试是否覆盖失败路径？
10) 命名/排序/空行是否统一？
11) README 是否说明部署与变量？

Source: d:\mycode\awesome-copilot\instructions\terraform.instructions.md | Generated: 2025-10-17
