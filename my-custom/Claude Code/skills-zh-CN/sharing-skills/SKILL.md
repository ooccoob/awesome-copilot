---
name: sharing-skills
description: 当您开发了广泛有用的技能，想通过pull request贡献给上游时使用 - 指导分支、提交、推送和创建PR的过程，将技能贡献回上游仓库
---

# 分享技能

## 概述

将您本地分支的技能贡献回上游仓库。

**工作流：** 分支 → 编辑/创建技能 → 提交 → 推送 → PR

## 何时分享

**在以下情况分享：**
- 技能广泛应用（不是项目特定）
- 其他人会受益的模式/技术
- 经过良好测试和文档化
- 遵循writing-skills指南

**在以下情况保留个人：**
- 项目或组织特定
- 实验性或不稳定
- 包含敏感信息
- 对一般用途太狭窄/小众

## 先决条件

- 安装并认证了`gh` CLI
- 工作目录是`~/.config/superpowers/skills/`（您的本地克隆）
- **必需：** 技能已使用writing-skills TDD过程测试

## 分享工作流

### 1. 确保您在main上并同步

```bash
cd ~/.config/superpowers/skills/
git checkout main
git pull upstream main
git push origin main  # 推送到您的fork
```

### 2. 创建功能分支

```bash
# 分支名称：add-skillname-skill
skill_name="your-skill-name"
git checkout -b "add-${skill_name}-skill"
```

### 3. 创建或编辑技能

```bash
# 在skills/中处理您的技能
# 创建新技能或编辑现有技能
# 技能应该在skills/category/skill-name/SKILL.md中
```

### 4. 提交更改

```bash
# 添加并提交
git add skills/your-skill-name/
git commit -m "添加${skill_name}技能

$(cat <<'EOF'
这个技能做什么和为什么有用的简要描述。

用以下方式测试：[描述测试方法]
EOF
)"
```

### 5. 推送到您的Fork

```bash
git push -u origin "add-${skill_name}-skill"
```

### 6. 创建Pull Request

```bash
# 使用gh CLI创建PR到上游
gh pr create \
  --repo upstream-org/upstream-repo \
  --title "添加${skill_name}技能" \
  --body "$(cat <<'EOF'
## 摘要
技能的简要描述和它解决什么问题。

## 测试
描述您如何测试这个技能（压力场景、基线测试等）。

## 上下文
关于为什么需要这个技能以及应该如何使用的任何额外上下文。
EOF
)"
```

## 完整示例

这是一个分享名为"async-patterns"技能的完整示例：

```bash
# 1. 与上游同步
cd ~/.config/superpowers/skills/
git checkout main
git pull upstream main
git push origin main

# 2. 创建分支
git checkout -b "add-async-patterns-skill"

# 3. 创建/编辑技能
# （在skills/async-patterns/SKILL.md上工作）

# 4. 提交
git add skills/async-patterns/
git commit -m "添加async-patterns技能

在测试和应用代码中处理异步操作的模式。

用以下方式测试：多个压力场景测试代理合规性。"

# 5. 推送
git push -u origin "add-async-patterns-skill"

# 6. 创建PR
gh pr create \
  --repo upstream-org/upstream-repo \
  --title "添加async-patterns技能" \
  --body "## 摘要
在测试和应用代码中正确处理异步操作的模式。

## 测试
用多个应用场景测试。代理成功将模式应用到新代码。

## 上下文
解决常见异步陷阱，如竞争条件、不当错误处理和时间问题。"
```

## PR被合并后

一旦您的PR被合并：

1. 同步您的本地main分支：
```bash
cd ~/.config/superpowers/skills/
git checkout main
git pull upstream main
git push origin main
```

2. 删除功能分支：
```bash
git branch -d "add-${skill_name}-skill"
git push origin --delete "add-${skill_name}-skill"
```

## 故障排除

**"gh: command not found"**
- 安装GitHub CLI：https://cli.github.com/
- 认证：`gh auth login`

**"Permission denied (publickey)"**
- 检查SSH密钥：`gh auth status`
- 设置SSH：https://docs.github.com/en/authentication

**"技能已存在"**
- 您在创建修改版本
- 考虑不同的技能名称或与技能维护者协调

**PR合并冲突**
- 在最新上游上变基：`git fetch upstream && git rebase upstream/main`
- 解决冲突
- 强制推送：`git push -f origin your-branch`

## 多技能贡献

**不要在一个PR中批量处理多个技能。**

每个技能应该：
- 有自己的功能分支
- 有自己的PR
- 可独立审查

**为什么？** 单个技能可以独立审查、迭代和合并。

## 相关技能

- **writing-skills** - 必需：在分享前如何创建经过良好测试的技能