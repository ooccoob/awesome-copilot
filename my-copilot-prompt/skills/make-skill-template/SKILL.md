---
name: make-skill-template
description: 'Create new Agent Skills for GitHub Copilot from prompts or by duplicating this template. Use when asked to "create a skill", "make a new skill", "scaffold a skill", or when building specialized AI capabilities with bundled resources. Generates SKILL.md files with proper frontmatter, directory structure, and optional scripts/references/assets folders.'
---

# 制作技能模板

用于创建新特工技能的元技能。当您需要构建新的技能文件夹、生成 SKILL.md 文件或帮助用户了解代理技能规范时，请使用此技能。

## 何时使用此技能

- 用户要求“创建一项技能”、“制作一项新技能”或“搭建一项技能”
- 用户希望为其 GitHub Copilot 设置添加专门功能
- 用户需要帮助使用捆绑资源构建技能
- 用户想要复制此模板作为起点

## 先决条件

- 了解该技能应该完成什么任务
- 对功能和触发器进行清晰、关键字丰富的描述
- 了解所需的任何捆绑资源（脚本、参考、资产、模板）

## 创造新技能

### 第 1 步：创建技能目录

创建一个具有小写连字符名称的新文件夹：

```
skills/<skill-name>/
└── SKILL.md          # Required
```

### 第2步：使用 Frontmatter 生成 SKILL.md

每项技能都需要带有 `name` 和 `description` 的 YAML frontmatter：

```yaml
---
name: <skill-name>
description: '<What it does>. Use when <specific triggers, scenarios, keywords users might say>.'
---
```

#### Frontmatter 字段要求

|领域 |必填 |限制条件|
|-------|----------|-------------|
| __代码0__ | **是** | 1-64 个字符，仅限小写字母/数字/连字符，必须与文件夹名称匹配 |
| __代码0__ | **是** | 1-1024 个字符，必须描述它的作用以及何时使用它 |
| __代码0__ |没有 |许可证名称或对捆绑的 LICENSE.txt 的引用 |
| __代码0__ |没有 | 1-500 个字符，需要时环境要求 |
| __代码0__ |没有 |附加属性的键值对 |
| __代码0__ |没有 |以空格分隔的预先批准的工具列表（实验性）|

#### 描述 最佳实践

**关键**：`description` 是自动技能发现的主要机制。包括：

1. **什么**该技能的作用（能力）
2. **何时**使用它（触发器、场景、文件类型）
3. **关键字** 用户可能在提示中提及

**好例子：**

```yaml
description: 'Toolkit for testing local web applications using Playwright. Use when asked to verify frontend functionality, debug UI behavior, capture browser screenshots, or view browser console logs. Supports Chrome, Firefox, and WebKit.'
```

**糟糕的例子：**

```yaml
description: 'Web testing helpers'
```

### 第三步：编写技能主体

在 frontmatter 之后，添加 markdown 说明。推荐栏目：

|部分|目的|
|---------|---------|
| __代码0__ |简要概述 |
| __代码0__ |强化描述触发点 |
| __代码0__ |所需工具、依赖项 |
| __代码0__ |任务的编号步骤 |
| __代码0__ |常见问题及解决方案 |
| __代码0__ |捆绑文档的链接 |

### 第 4 步：添加可选目录（如果需要）

|文件夹|目的|何时使用 |
|--------|---------|-------------|
| __代码0__ |可执行代码（Python、Bash、JS）|执行操作的自动化 |
| __代码0__ |文件代理读取| API 参考、架构、指南 |
| __代码0__ |静态文件按原样使用 |图像、字体、模板 |
| __代码0__ |起始代码代理修改|脚手架延长|

## 示例：完整的技能结构

```
my-awesome-skill/
├── SKILL.md                    # Required instructions
├── LICENSE.txt                 # Optional license file
├── scripts/
│   └── helper.py               # Executable automation
├── references/
│   ├── api-reference.md        # Detailed docs
│   └── examples.md             # Usage examples
├── assets/
│   └── diagram.png             # Static resources
└── templates/
    └── starter.ts              # Code scaffold
```

## 快速入门：复制此模板

1. 复制 `make-skill-template/` 文件夹
2. 重命名为您的技能名称（小写，连字符）
3. 更新`SKILL.md`：
   - 更改 `name:` 以匹配文件夹名称
   - 编写关键字丰富的 `description:`
   - 将正文内容替换为您的说明
4. 根据需要添加捆绑资源
5. 使用 `npm run skill:validate` 进行验证

## 验证清单

- [ ] 文件夹名称为小写并带有连字符
- [ ] `name` 字段与文件夹名称完全匹配
- [ ] `description` 为 10-1024 个字符
- [ ] `description` 解释什么和何时
- [ ] `description` 用单引号括起来
- [ ] 正文内容少于 500 行
- [ ] 捆绑资产每个小于 5MB

## 故障排除

|问题 |解决方案 |
|-------|----------|
|技能未被发现|使用更多关键字和触发器改进描述 |
|名称验证失败 |确保小写，无连续连字符，匹配文件夹 |
|描述太短|添加功能、触发器和关键字 |
|未找到资产 |使用技能根目录的相对路径 |

## 参考文献

- 特工技能官方规格：<https://agentskills.io/specification>
