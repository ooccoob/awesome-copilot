---
description: 'Ansible conventions and best practices'
applyTo: '**/*.yaml, **/*.yml'
---

# Ansible 约定和最佳实践

## 一般说明

- 使用 Ansible 配置和管理基础设施。
- 对 Ansible 配置使用版本控制。
- 保持事情简单；仅在必要时使用高级功能
- 为每个游戏、区块和任务提供一个简洁但具有描述性的 `name`
  - 以指示正在执行的操作的动作动词开头的名称，例如“安装”、“配置”或“复制”
  - 任务名称首字母大写
  - 为简洁起见，省略任务名称末尾的句点
  - 省略角色任务中的角色名称； Ansible在运行角色时会自动显示角色名称
  - 当包含来自单独文件的任务时，您可以在每个任务名称中包含文件名，以便更容易找到任务（例如，`<TASK_FILENAME> : <TASK_NAME>`）
- 使用注释提供有关**做什么**、**如何**和/或**为什么**要做某事的附加上下文
  - 不要包含多余的注释
- 使用云资源的动态清单
  - 使用标签根据环境、功能、位置等动态创建组。
  - 使用 `group_vars` 根据这些属性设置变量
- 尽可能使用幂等 Ansible 模块；避免 `shell`、`command` 和 `raw`，因为它们会破坏幂等性
  - 如果必须使用 `shell` 或 `command`，请在可行的情况下使用 `creates:` 或 `removes:` 参数，以防止不必要的执行
- 使用 [完全限定的集合名称 (FQCN)](https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Fully-Qualified-Collection-Name-FQCN) 确保选择正确的模块或插件
  - 将 `ansible.builtin` 集合用于[内置模块和插件](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/index.html#plugin-index)
- 将相关任务分组在一起以提高可读性和模块化性
- 对于 `state` 可选的模块，显式设置 `state: present` 或 `state: absent` 以提高清晰度和一致性
- 使用执行任务所需的最低权限
  - 如果所有包含的任务都需要超级用户权限，则仅在播放级别或 `include:` 语句上设置 `become: true` ；否则，在任务级别指定 `become: true`
  - 仅当需要超级用户权限时才在任务上设置 `become: true`

## 秘密管理

- 单独使用 Ansible 时，使用 Ansible Vault 存储机密
  - 使用以下过程可以轻松找到定义了存储变量的位置
    1. 创建以组命名的 `group_vars/` 子目录
    2. 在此子目录中，创建两个名为 `vars` 和 `vault` 的文件
    3. 在 `vars` 文件中，定义所需的所有变量，包括任何敏感变量
    4. 将所有敏感变量复制到 `vault` 文件，并在这些变量前添加 `vault_` 前缀
    5. 使用 Jinja2 语法调整 `vars` 文件中的变量以指向匹配的 `vault_` 变量： `db_password: "{{ vault_db_password }}"`
    6. 加密 `vault` 文件以保护其内容
    7. 使用剧本中 `vars` 文件中的变量名称
- 当将其他工具与 Ansible（例如 Terraform）一起使用时，将机密存储在第三方机密管理工具（例如 Hashicorp Vault、AWS Secrets Manager 等）中
  - 这允许所有工具引用秘密的单一事实来源，并防止配置不同步

## 风格

- 使用 2 个空格缩进并始终缩进列表
- 用一个空行分隔以下各项：
  - 两个主机块
  - 两个任务块
  - 托管并包含块
- 使用 `snake_case` 作为变量名
- 在 `vars:` 映射或变量文件中定义变量时，按字母顺序对变量进行排序
- 始终使用多行映射语法，无论映射中存在多少对
  - 它提高了可读性并减少了版本控制的变更集冲突
- 优先选择单引号而不是双引号
  - 唯一应该使用双引号的时候是当它们嵌套在单引号内时（例如 Jinja 地图引用），或者当您的字符串需要转义字符时（例如，使用“\n”表示换行符）
  - 如果必须编写长字符串，请使用折叠块标量语法（即 `>`）将换行符替换为空格或文字块标量语法（即 `|`）以保留换行符；省略所有特殊引用
- 戏剧的 `host` 部分应遵循以下一般顺序：
  - `hosts` 声明
  - 按字母顺序排列的主机选项（例如，`become`、`remote_user`、`vars`）
  - __代码0__
  - __代码0__
  - __代码0__
- 每项任务都应遵循以下一般顺序：
  - __代码0__
  - 任务声明（例如，`service:`、`package:`）
  - 任务参数（使用多行映射语法）
  - 循环运算符（例如 `loop`）
  - 按字母顺序排列的任务选项（例如 `become`、`ignore_errors`、`register`）
  - __代码0__
- 对于 `include` 语句，引用文件名，并且如果它们是多行的（例如，它们有标签），则仅在 `include` 语句之间使用空行

## 棉绒

- 使用 `ansible-lint` 和 `yamllint` 检查语法并强制执行项目标准
- 使用 `ansible-playbook --syntax-check` 检查语法错误
- 使用 `ansible-playbook --check --diff` 执行 playbook 执行的试运行

<!-- 
这些指南基于或复制自以下来源：

- [Ansible 文档 - 提示和技巧](https://docs.ansible.com/ansible/latest/tips_tricks/index.html)
- [Whitecloud Ansible 样式指南](https://github.com/whitecloud/ansible-styleguide)
-->
