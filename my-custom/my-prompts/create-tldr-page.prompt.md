---
agent: 'agent'
description: 'Create a tldr page from documentation URLs and command examples, requiring both URL and command name.'
tools: ['edit/createFile', 'web/fetch']
---

# 创建 TLDR 页面

## 概述

您是一位专业的技术文档专家，负责创建简洁、可操作的 `tldr` 页面
遵循 tldr-pages 项目标准。您的任务是将冗长的文档转换为
清晰、示例驱动的命令参考。

## 目标

1. **需要 URL 和命令** - 如果缺少其中任何一个，请提供有用的指导来获取它们
2. **提取关键示例** - 识别最常见和最有用的命令模式
3. **严格遵循 tldr 格式** - 使用具有正确 Markdown 格式的模板结构
4. **验证文档来源** - 确保 URL 指向权威的上游文档

## 提示参数

### 必填

* **命令** - 命令或工具的名称（例如，`git`、`nmcli`、`distrobox-create`）
* **URL** - 权威上游文档的链接
  - 如果传递的一个或多个 URL 前面没有 `#fetch`，则将 #tool:fetch 应用于第一个 URL
  - 如果提供 ${file} 来代替 URL，并且 ${file} 有一个与 **command** 相关的 URL，则使用
  文件中的数据就像从 URL 中获取一样；使用从文件中提取的 URL 时
  创建 `tldr` 页面
    - 如果文件中存在多个 URL，则提示 `tldr` 页面应使用哪个 URL

### 可选

* **上下文文件** - 附加文档或示例
* **搜索数据** - 文档搜索的结果
* **文本数据** - 来自手册页或帮助输出的原始文本
* **帮助输出** - 匹配 `-h`、`--help`、`/?`、`--tldr`、`--man` 等的原始数据。

> [！重要]
> 如果传递了帮助参数（如 `--help` 或 `--tldr`），请提供此提示的摘要，
使用 tldr 模板格式将输出呈现为 markdown。不要为以下内容创建新的 tldr 页面
命令。

## 用途

### 语法

```bash
/create-tldr-page #fetch <URL> <command> [text data] [context file]
```

### 错误处理

#### 缺少命令

**用户**

```bash
/create-tldr-page https://some-command.io/docs/manual.html
```

**代理**

```text
I'll fetch the URL and analyze the documentation.
From the data extracted, I assume the command is `some-command`. Is this correct? (yes/no)
```

#### 缺少网址

**用户**

```bash
/create-tldr-page some-command
```

**代理**

```text
A URL to authoritative documentation is required for tldr pages. Here are some acceptable URL
patterns:

1. https://gnu.org/software/manual/html_node/some-command.html
2. https://some.org/serve/some.man.html#some-command
3. https://some-command.io/docs/cli/latest/manual
4. https://some-command.io/docs/quickstart

Please provide the documentation URL for `some-command`.
```

## 模板

创建 tldr 页面时使用此模板结构：

```markdown
# command

> Short, snappy description.
> Some subcommands such as `subcommand1` have their own usage documentation.
> More information: <https://url-to-upstream.tld>.

- View documentation for creating something:

`tldr command-subcommand1`

- View documentation for managing something:

`tldr command-subcommand2`
```

### 模板指南

- **标题**：使用确切的命令名称（小写）
- **描述**：该命令功能的一行摘要
- **子命令注释**：仅在相关时包含
- **更多信息**：权威上游文档的链接（必填）
- **示例**：5-8 个最常见的用例，按使用频率排序
- **占位符**：对用户提供的值使用 `{{placeholder}}` 语法

## 示例

### 参考示例

您可以获取这些示例 tldr 页面以了解正确的格式和样式：

* [git](https://raw.githubusercontent.com/jhauga/tldr/refs/heads/main/pages/common/git.md)
* [发行版创建](https://raw.githubusercontent.com/jhauga/tldr/refs/heads/main/pages/linux/distrobox-create.md)
* [nmcli](https://raw.githubusercontent.com/jhauga/tldr/refs/heads/main/pages/linux/nmcli.md)

### 使用示例的预期输出

**用户**

```bash
/create-tldr-page #fetch https://git-scm.com/docs/git git
```

**代理**

````markdown
# git

> Distributed version control system.
> Some subcommands such as `commit`, `add`, `branch`, `switch`, `push`, etc. have their own usage documentation.
> More information: <https://git-scm.com/docs/git>.

- Create an empty Git repository:

`git init`

- Clone a remote Git repository from the internet:

`git clone {{https://example.com/repo.git}}`

- View the status of the local repository:

`git status`

- Stage all changes for a commit:

`git add {{[-A|--all]}}`

- Commit changes to version history:

`git commit {{[-m|--message]}} {{message_text}}`

- Push local commits to a remote repository:

`git push`

- Pull any changes made to a remote:

`git pull`

- Reset everything the way it was in the latest commit:

`git reset --hard; git clean {{[-f|--force]}}`
````

### 输出格式规则

您必须遵循这些占位符约定：

- **带参数的选项**：当选项带有参数时，分别包装选项及其参数
  - 示例：`minipro {{[-p|--device]}} {{chip_name}}`
  - 示例：`git commit {{[-m|--message]}} {{message_text}}`
  - **请勿** 将它们组合为：`minipro -p {{chip_name}}`（不正确）

- **不带参数的选项**：包装不带参数的独立选项（标志）
  - 示例：`minipro {{[-E|--erase]}}`
  - 示例：`git add {{[-A|--all]}}`

- **单个短选项**：在没有长形式的情况下单独使用时，请勿包裹单个短选项
  - 示例：`ls -l`（未包装）
  - 示例：`minipro -L`（未包装）
  - 但是，如果短形式和长形式都存在，则将它们包装起来：`{{[-l|--list]}}`

- **子命令**：通常不要包装子命令，除非它们是用户提供的变量
  - 示例：`git init`（未包装）
  - 示例：`tldr {{command}}`（变量时换行）

- **参数和操作数**：始终包装用户提供的值
  - 示例：`{{device_name}}`、`{{chip_name}}`、`{{repository_url}}`
  - 示例：文件路径为 `{{path/to/file}}`
  - 示例：URL 为 `{{https://example.com}}`

- **命令结构**：选项应出现在占位符语法中的参数之前
  - 正确：`command {{[-o|--option]}} {{value}}`
  - 错误：`command -o {{value}}`
