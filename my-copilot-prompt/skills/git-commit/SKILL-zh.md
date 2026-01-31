---
名称：git-commit
描述：'使用传统的提交消息分析、智能暂存和消息生成来执行 git commit。当用户要求提交更改、创建 git 提交或提及“/commit”时使用。支持：(1) 自动检测更改的类型和范围，(2) 从差异生成常规提交消息，(3) 具有可选类型/范围/描述覆盖的交互式提交，(4) 用于逻辑分组的智能文件分段
许可证：麻省理工学院
允许的工具：Bash
---

# Git 提交与传统提交

## 概述

使用常规提交规范创建标准化的语义 git 提交。分析实际差异以确定适当的类型、范围和消息。

## 常规提交格式

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## 提交类型

|类型 |目的|
| ---------- | ------------------------------ |
| __代码0__ |新功能 |
| __代码0__ |错误修复 |
| __代码0__ |仅文档 |
| __代码0__ |格式/风格（无逻辑）|
| __代码0__ |代码重构（无功能/修复）|
| __代码0__ |绩效提升|
| __代码0__ |添加/更新测试 |
| __代码0__ |构建系统/依赖项 |
| __代码0__ | CI/配置更改 |
| __代码0__ |维护/杂项 |
| __代码0__ |恢复提交 |

## 重大变化

```
# Exclamation mark after type/scope
feat!: remove deprecated endpoint

# BREAKING CHANGE footer
feat: allow config to extend other configs

BREAKING CHANGE: `extends` key behavior changed
```

## 工作流程

### 1. 分析差异

```bash
# If files are staged, use staged diff
git diff --staged

# If nothing staged, use working tree diff
git diff

# Also check status
git status --porcelain
```

### 2. 阶段文件（如果需要）

如果没有任何内容上演或者您想要以不同的方式对更改进行分组：

```bash
# Stage specific files
git add path/to/file1 path/to/file2

# Stage by pattern
git add *.test.*
git add src/components/*

# Interactive staging
git add -p
```

**永远不要提交机密**（.env、credentials.json、私钥）。

### 3. 生成提交消息

分析差异以确定：

- **类型**：这是什么样的改变？
- **范围**：哪些区域/模块受到影响？
- **描述**：更改内容的一行摘要（现在时、祈使语气、<72 个字符）

### 4. 执行提交

```bash
# Single line
git commit -m "<type>[scope]: <description>"

# Multi-line with body/footer
git commit -m "$(cat <<'EOF'
<type>[scope]: <description>

<optional body>

<optional footer>
EOF
)"
```

## 最佳实践

- 每次提交一次逻辑更改
- 现在时：“添加”而不是“添加”
- 祈使语气：“修复错误”而不是“修复错误”
- 参考问题：`Closes #123`、`Refs #456`
- 将描述控制在 72 个字符以内

## Git 安全协议

- 永远不要更新 git 配置
- 未经明确请求，切勿运行破坏性命令（--force、硬重置）
- 除非用户要求，否则切勿跳过挂钩（--no-verify）
- 切勿强制推送到主/主控
- 如果提交由于钩子而失败，请修复并创建新的提交（不要修改）
