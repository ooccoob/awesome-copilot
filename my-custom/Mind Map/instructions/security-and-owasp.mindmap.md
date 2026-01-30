## What/When/Why/How
- What: 安全编码总则（OWASP Top10 导向）
- When: 任何代码生成/评审/重构时
- Why: 缺省安全、最小权限、防御性设计
- How: 访问控制/加密/输入输出/依赖/会话/反序列化等准则

## Key Points
- 访问控制/SSRF：默认拒绝；白名单 URL/主机/端口；防路径遍历
- 加密：HTTPS；静态数据加密；Argon2/bcrypt；密钥从环境/密管
- 注入：参数化查询；命令转义；前端输出编码/DOMPurify
- 配置/组件：生产关闭调试；安全响应头；依赖更新与扫描
- 认证/会话：Cookie Secure/HttpOnly/SameSite；限速/锁定
- 反序列化：禁用不安全反序列化；优先 JSON + 严格校验
- 评审：显式说明风险与缓解；教育式 Code Review

## Compact Map
- AC: least-privilege + deny-by-default
- Crypto: transit/rest + secrets mgmt
- Injection: SQL/OS/XSS → param/escape/sanitize
- Ops: headers + deps audit + no debug

## Example Questions
1) 是否实现“默认拒绝”和最小权限？
2) 外部 URL 是否基于严格白名单校验？
3) 密钥是否未硬编码且来源安全？
4) SQL 是否全部参数化并无拼接？
5) 前端是否避免 innerHTML 或使用消毒？
6) 生产环境是否关闭调试与堆栈暴露？
7) 是否设置 CSP/HSTS/X-Content-Type-Options 等头？
8) 登录/重置是否具限速与锁定策略？
9) 反序列化是否限制类型并优先 JSON？
10) 依赖是否经漏洞扫描并及时升级？
11) 评审是否解释风险与替代方案？

Source: d:\mycode\awesome-copilot\instructions\security-and-owasp.instructions.md | Generated: 2025-10-17
