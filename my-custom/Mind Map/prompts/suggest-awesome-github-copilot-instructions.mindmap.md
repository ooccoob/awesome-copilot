## What
- 目标：基于当前仓库与会话上下文，筛选 awesome-copilot 中相关 instructions，避免与本地重复，并以表格输出候选。
- 输入：远端 README.instructions.md 清单；本地 instructions/*.instructions.md 的 front matter（description/applyTo）；仓库语言/框架/流程信号。
- 输出：建议表（上游链接、本地相似项、已安装状态、理由）；待用户确认后再安装。

## When
- 新仓库初始化或引入新技术栈/部署方式时。
- 需要补齐规范（安全/质量/流程/文档/基础设施）空白时。
- 本地指令老旧或重复亟需对齐社区最佳实践时。

## Why
- 统一生成式协作规范，减少风格漂移与重复劳动。
- 复用高质量社区指令以提升效率与一致性。
- 与本地现状对齐，避免冲突与冗余。

## How
- 获取远端指令目录 → 扫描本地 instructions → 解析 front matter → 结合仓库特征做匹配 → 去重并生成候选表。
- 去重：先按主题/文件名近似归并，再比对 description/applyTo 判定“重复/近重复/互补”。
- 安装策略：仅在用户确认后下载至 .github/instructions/；不改文件内容；用 todos 跟踪进度。

## Key Points
- 工具：fetch/githubRepo/目录扫描/front matter 解析；仅输出建议表，禁止直接安装。
- 维度：语言/框架/测试/安全/文档/部署/数据/接口。
- 结果：结构化表格、链接可点、理由简洁有力、避免冗余。

## Compact Map
- Discovery: 远端清单 + 本地清单 + front matter
- Analysis: 识别技术栈信号（.cs/.ts/.java/.py、Docker、Bicep、CI）→ 匹配缺口
- Suggest: 表格列=上游文件|描述|已装|本地相似|理由（✅/❌ 状态）
- Next: 用户选中 → 下载 → 校验入库

## Example Questions (10+)
- 我们以 Java + Vue 为主，优先推荐哪些 instructions？
- 与现有 hos 规范会否冲突，如何判定“近重复”？
- applyTo 想限定到 src/biz/**，front matter 如何写？
- Bicep/基础设施规范有哪些可复用指令？
- 能推荐覆盖单元/集成/端到端测试的指令组合吗？
- 如何在安装前生成本地 vs 上游差异预览？
- 如果同名不同语义，建议保留还是合并？
- 请按技术相关性输出 Top 10 候选并解释理由。
- 是否有日志脱敏/密钥管理/依赖安全的指令？
- 多仓多语言场景如何分仓/分路径应用？
- 如何持续跟踪上游更新并提示本地升级？

---
Source: d:\mycode\awesome-copilot\prompts\suggest-awesome-github-copilot-instructions.prompt.md
Generated: 2025-10-17T00:00:00Z
