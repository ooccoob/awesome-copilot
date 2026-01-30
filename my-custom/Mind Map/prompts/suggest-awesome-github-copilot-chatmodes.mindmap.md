## Suggest Awesome Copilot Chat Modes — Mind Map

### What
- 基于仓库与会话上下文，推荐 awesome-copilot 中尚未安装的自定义 Chat Modes。

### When
- 需要扩充能力库、避免重复安装、提升工作流覆盖度时。

### Why
- 精准补齐能力短板，复用成熟模式，降低维护成本。

### How
- 抓取清单→扫描本地 .github/chatmodes → 解析前言描述 → 语境匹配 → 列表化推荐（去重/理由/链接）。

### Key Points (中/英)
- 抓取/Fetch
- 去重/Deduplicate
- 匹配/Match
- 解释/Explain
- 资产清单/Inventory
- 安装/Install (on demand)

### Compact map
- Inputs: awesome README.chatmodes + local chatmodes
- Process: fetch → parse → diff → rank → table output
- Output: 建议表（链接、是否已装、相似项、理由）

### Example Questions (≥10)
- 如何识别与本地近似但不完全重复的 chatmode？
- 匹配相关性的特征权重（语言/框架/痛点）如何设定？
- 表格输出应包含哪些最有用的字段？
- 何时需要请求用户确认再执行安装？
- 如何在安装阶段保证原文件不被修改？
- 断网或抓取失败的降级策略？
- 如何追踪本地 chatmodes 的来源与版本？
- 推荐排序是否需要基于近期聊天上下文动态调整？
- 多仓库场景下的共享与去重策略？
- 成功安装后的使用引导应包含哪些示例？

---
- Source: d:\mycode\awesome-copilot\prompts\suggest-awesome-github-copilot-chatmodes.prompt.md
- Generated: 2025-10-17
