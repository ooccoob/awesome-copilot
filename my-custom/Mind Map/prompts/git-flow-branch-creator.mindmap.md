## What
- 分析 git status/diff（或 --cached）判定 Git Flow 分支类型（feature/release/hotfix），生成语义化分支名并自动切换。

## When
- 本地已有改动，需要快速按 Git Flow 规范创建合适分支时。

## Why
- 统一分支策略，减少判断/命名成本，避免失误。

## How
- 采集：git status + diff
- 判定：变更性质→分支类型（决策树）
- 命名：kebab-case + 语义化 + 可选工单号
- 执行：从 develop/master 创建并切换；输出后续步骤
- 边界：混合改动/无改动/已有分支/重名

## Key points (CN)
- feature 默认；release=版本/说明；hotfix=紧急修复
- 检查目标分支存在、权限与重名冲突
- 建议备用命名与人工覆盖

## Key points (EN)
- Analyze changes → classify → name → create
- Handle edge cases; provide next steps
- Prefer semantic, concise branch names

## Example questions
- “检测当前改动应走 hotfix 还是 feature？”
- “给出 3 个可选语义分支名并创建？”

## 思维导图（要点）
- 分析→分类→命名→创建
- 预检/冲突/回退

—
- Source: d:\mycode\awesome-copilot\prompts\git-flow-branch-creator.prompt.md
- Generated: 2025-10-17
