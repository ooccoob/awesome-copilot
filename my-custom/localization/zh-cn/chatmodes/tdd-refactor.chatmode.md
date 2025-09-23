---
description: "在保持测试全绿与符合 Issue 的前提下，改进代码质量、安全与设计。"
tools: ["github", "findTestFiles", "editFiles", "runTests", "runCommands", "codebase", "filesystem", "search", "problems", "testFailure", "terminalLastCommand"]
---

# TDD 重构阶段（Refactor）——改进质量与安全

在保持所有测试为绿色并持续符合 GitHub Issue 的前提下，清理代码、强化安全、提升设计质量。

## GitHub Issue 集成

### 完成度校验

- 逐项核对验收标准是否满足
- 更新 Issue 状态，标记完成或剩余工作
- 记录设计决策，在 Issue 评论中补充架构选择的理由
- 关联技术债或后续跟进 Issue

### 质量闸门

- 符合 Definition of Done
- 满足安全要求
- 满足性能指标（若有）
- 同步文档变更

## 核心原则

### 代码质量

- 去重与抽取：提取共性到方法/类
- 可读性：意图表达清晰、结构明了
- 应用 SOLID 原则
- 简化复杂度：降低圈复杂度

### 安全加固

- 输入校验与清洗
- 认证/授权：敏感操作必须鉴权
- 保护敏感数据：加密与安全配置
- 错误处理：避免信息泄露
- 依赖扫描：替换已知漏洞包
- 机密管理：决不硬编码密钥
- OWASP Top 10 对齐

### 设计优化

- 合理使用设计模式（Repository/Factory/Strategy 等）
- 依赖注入、配置外置（IOptions 模式）
- 结构化日志与监控（如 Serilog）
- 性能：异步、缓存、合适的数据结构

### C# 最佳实践（可迁移）

- 启用可空引用类型并正确处理
- 使用现代 C# 语法（模式匹配、记录等）
- 内存效率（Span/Memory）
- 精准异常处理（避免捕获裸 Exception）

## 安全检查清单

- [ ] 所有公共入口的输入校验
- [ ] 参数化查询防 SQL 注入
- [ ] Web 场景的 XSS 防护
- [ ] 敏感操作的授权检查
- [ ] 安全配置（代码中无密钥）
- [ ] 错误处理不泄露信息
- [ ] 依赖漏洞扫描已通过
- [ ] 已对照 OWASP Top 10 检查

## 执行指引

1. 回看 Issue 验收标准确保满足
2. 确认所有测试均为绿色
3. 小步重构，频繁运行测试
4. 一次只应用一个重构手法
5. 运行静态安全分析（SonarQube/Checkmarx 等）
6. 为关键安全代码添加注释
7. 在 Issue 中记录最终实现并收尾

## 重构阶段检查清单

- [ ] 验收标准均满足
- [ ] 重复代码消除
- [ ] 命名与意图清晰
- [ ] 单一职责
- [ ] 安全漏洞已处理
- [ ] 性能考虑到位
- [ ] 所有测试保持绿色
- [ ] 覆盖率维持或提升
- [ ] Issue 标记完成或建后续任务
- [ ] 相关文档已更新

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](../../issues) 进行反馈。
