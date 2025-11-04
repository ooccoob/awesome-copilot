---
name: using-git-worktrees
description: 在开始需要与当前工作空间隔离的功能工作或执行实现计划之前使用 - 创建带有智能目录选择和安全验证的隔离git工作树
---

# 使用Git工作树

## 概述

Git工作树创建共享同一仓库的隔离工作区，允许同时处理多个分支而无需切换。

**核心原则：** 系统性目录选择 + 安全验证 = 可靠隔离。

**开始时宣布：** "我正在使用git工作树技能设置隔离工作区。"

## 目录选择过程

遵循此优先级顺序：

### 1. 检查现有目录

```bash
# 按优先级顺序检查
ls -d .worktrees 2>/dev/null     # 首选（隐藏）
ls -d worktrees 2>/dev/null      # 替代
```

**如果找到：** 使用该目录。如果两者都存在，`.worktrees`胜出。

### 2. 检查CLAUDE.md

```bash
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
```

**如果指定偏好：** 不询问就使用它。

### 3. 询问用户

如果目录不存在且CLAUDE.md无偏好：

```
找不到工作树目录。我应该在哪里创建工作树？

1. .worktrees/（项目本地，隐藏）
2. ~/.config/superpowers/worktrees/<project-name>/（全局位置）

您更喜欢哪个？
```

## 安全验证

### 对于项目本地目录（.worktrees或worktrees）

**必须在创建工作树前验证.gitignore：**

```bash
# 检查目录模式是否在.gitignore中
grep -q "^\.worktrees/$" .gitignore || grep -q "^worktrees/$" .gitignore
```

**如果不在.gitignore中：**

根据Jesse的规则"立即修复损坏的东西"：
1. 向.gitignore添加适当行
2. 提交更改
3. 继续工作树创建

**为什么关键：** 防止意外将工作树内容提交到仓库。

### 对于全局目录（~/.config/superpowers/worktrees）

无需.gitignore验证 - 完全在项目外部。

## 创建步骤

### 1. 检测项目名称

```bash
project=$(basename "$(git rev-parse --show-toplevel)")
```

### 2. 创建工作树

```bash
# 确定完整路径
case $LOCATION in
  .worktrees|worktrees)
    path="$LOCATION/$BRANCH_NAME"
    ;;
  ~/.config/superpowers/worktrees/*)
    path="~/.config/superpowers/worktrees/$project/$BRANCH_NAME"
    ;;
esac

# 用新分支创建工作树
git worktree add "$path" -b "$BRANCH_NAME"
cd "$path"
```

### 3. 运行项目设置

自动检测并运行适当设置：

```bash
# Node.js
if [ -f package.json ]; then npm install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then poetry install; fi

# Go
if [ -f go.mod ]; then go mod download; fi
```

### 4. 验证干净基线

运行测试确保工作树开始干净：

```bash
# 示例 - 使用项目适当命令
npm test
cargo test
pytest
go test ./...
```

**如果测试失败：** 报告失败，询问是否继续或调查。

**如果测试通过：** 报告就绪。

### 5. 报告位置

```
工作树在<完整路径>就绪
测试通过（<N>个测试，0个失败）
准备实现<功能名称>
```

## 快速参考

| 情况 | 操作 |
|-----------|--------|
| `.worktrees/`存在 | 使用它（验证.gitignore） |
| `worktrees/`存在 | 使用它（验证.gitignore） |
| 两者都存在 | 使用`.worktrees/` |
| 两者都不存在 | 检查CLAUDE.md → 询问用户 |
| 目录不在.gitignore中 | 立即添加 + 提交 |
| 基线测试失败 | 报告失败 + 询问 |
| 没有package.json/Cargo.toml | 跳过依赖安装 |

## 常见错误

**跳过.gitignore验证**
- **问题：** 工作树内容被跟踪，污染git状态
- **修复：** 创建项目本地工作树前总是grep .gitignore

**假设目录位置**
- **问题：** 创建不一致性，违反项目约定
- **修复：** 遵循优先级：现有 > CLAUDE.md > 询问

**失败测试下继续**
- **问题：** 无法区分新错误和预存问题
- **修复：** 报告失败，获得明确继续许可

**硬编码设置命令**
- **问题：** 在使用不同工具的项目上破坏
- **修复：** 从项目文件自动检测（package.json等）

## 示例工作流

```
您：我正在使用git工作树技能设置隔离工作区。

[检查.worktrees/ - 存在]
[验证.gitignore - 包含.worktrees/]
[创建工作树：git worktree add .worktrees/auth -b feature/auth]
[运行npm install]
[运行npm test - 47个通过]

工作树在/Users/jesse/myproject/.worktrees/auth就绪
测试通过（47个测试，0个失败）
准备实现auth功能
```

## 红旗

**绝不：**
- 无.gitignore验证创建工作树（项目本地）
- 跳过基线测试验证
- 无询问失败测试下继续
- 模糊时假设目录位置
- 跳过CLAUDE.md检查

**总是：**
- 遵循目录优先级：现有 > CLAUDE.md > 询问
- 验证项目本地的.gitignore
- 自动检测并运行项目设置
- 验证干净测试基线

## 集成

**被调用者：**
- **brainstorming**（阶段4） - 设计被批准且实现跟随时必需
- 任何需要隔离工作区的技能

**配对：**
- **finishing-a-development-branch** - 工作完成后清理必需
- **executing-plans**或**subagent-driven-development** - 工作在此工作树中发生