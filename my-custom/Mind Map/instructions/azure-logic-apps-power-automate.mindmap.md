## What / When / Why / How
- What: Azure Logic Apps / Power Automate 基于 WDL 的工作流建模与工程实践。
- When: 需编排触发器/连接器/HTTP/数据操作/错误与监控/安全/版本化/成本治理时。
- Why: 企业级自动化与集成，高可靠、可观测、可运维与可治理。
- How: 标准 JSON 结构；选择合适触发器；具名动作+Scope 分组；runAfter/重试/超时；表达式/变量；并行/循环；Key Vault/托管标识；APIM 前置；版本化与 CI/CD。

## Key points
- 结构：definition 与 parameters；triggers/actions/outputs/parameters/staticResults。
- 触发：Request/Recurrence/Event；设置认证、分页、超时。
- 动作：HTTP/Connector/Data operation；Scope+runAfter 构建成功/失败分支；重试策略。
- 表达式：字符串/集合/条件/时间/JSON；复杂表达式应注释。
- 参数与变量：可复用与环境化；Initialize/Set/Append。
- 控制流：If/Switch/ForEach/Until；并发与批量限制。
- 安全：托管标识、Key Vault、最小权限、IP 限制、加密、RBAC；敏感数据脱敏。
- 监控：诊断、跟踪 ID、AI/LogAnalytics、告警；SLA 监控与死信处理。
- APIM：JWT 验证、限流、日志/变换；以“Workflow as API” 暴露。
- 版本化与成本：URI/参数/并行版本；触发与动作优化、批量/压缩、计划与资源合理化。

## Compact map
- 触发→动作→控制流→错误/重试→输出
- 参数/变量→环境→CI/CD
- 安全：MSI/KeyVault/RBAC/IP
- 观测：日志/告警/相关性
- 前置：APIM 策略

## Example questions (10+)
- runAfter+Scope 如何实现“尝试/捕获/失败告警”的结构？
- ForEach 并发与外部 API 限流如何折中？
- 复杂条件表达式的可读性与可维护性提升技巧？
- 如何以托管标识安全调用受保护的 API？
- 何时拆分为多个工作流而非深层嵌套？
- Power Automate 与 Logic Apps 的连接器与环境差异如何迁移？
- 如何把工作流暴露到 APIM 并施加 JWT/速率限制？
- 如何建立端到端相关性与业务 KPI 监控？
- 成本热点（触发/动作/数据传输）如何诊断与优化？
- 错误分类（网络/业务校验/权限）下的不同处理策略？

—
Source: d:\mycode\awesome-copilot\instructions\azure-logic-apps-power-automate.instructions.md | Generated: {{timestamp}}
