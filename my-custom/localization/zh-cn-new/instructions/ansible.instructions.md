---
description: 'Ansible约定和最佳实践'
applyTo: '**/*.yaml, **/*.yml'
---

# Ansible约定和最佳实践

## 一般指令

- 使用Ansible配置和管理基础设施。
- 对Ansible配置使用版本控制。
- 保持简单；仅在必要时使用高级功能
- 为每个play、block和task提供简洁但描述性的`name`
  - 以指示正在执行的操作的动作动词开始名称，例如"安装"、"配置"或"复制"
  - 任务名称的首字母大写
  - 为简洁起见，任务名称末尾省略句号
  - 从角色任务中省略角色名称；Ansible在运行角色时会自动显示角色名称
  - 当从单独文件包含任务时，您可以在每个任务名称中包含文件名以便更容易定位任务（例如，`<TASK_FILENAME> : <TASK_NAME>`）
- 使用注释提供关于**什么**、**如何**和/或**为什么**正在做某事的额外上下文
  - 不要包含冗余注释
- 对云资源使用动态清单
  - 使用标签基于环境、功能、位置等动态创建组
  - 使用`group_vars`基于这些属性设置变量
- 尽可能使用幂等Ansible模块；避免`shell`、`command`和`raw`，因为它们会破坏幂等性
  - 如果必须使用`shell`或`command`，在可行时使用`creates:`或`removes:`参数以防止不必要的执行
- 使用[完全限定的集合名称（FQCN）](https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Fully-Qualified-Collection-Name-FQCN)确保选择正确的模块或插件
  - 对[内置模块和插件](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/index.html#plugin-index)使用`ansible.builtin`集合
- 将相关任务分组在一起以提高可读性和模块化
- 对于`state`可选的模块，显式设置`state: present`或`state: absent`以提高清晰度和一致性
- 使用执行任务所需的最低权限
  - 仅在所有包含的任务都需要超级用户特权时在play级别或`include:`语句上设置`become: true`；否则，在任务级别指定`become: true`
  - 仅在任务需要超级用户特权时在任务上设置`become: true`

## 密钥管理

- 单独使用Ansible时，使用Ansible Vault存储密钥
  - 使用以下流程使查找定义了加密变量的位置变得容易
    1. 创建以组命名的`group_vars/`子目录
    2. 在此子目录内，创建两个名为`vars`和`vault`的文件
    3. 在`vars`文件中，定义所有需要的变量，包括任何敏感变量
    4. 将所有敏感变量复制到`vault`文件中，并使用`vault_`前缀这些变量
    5. 调整`vars`文件中的变量以使用Jinja2语法指向匹配的`vault_`变量：`db_password: "{{ vault_db_password }}"`
    6. 加密`vault`文件以保护其内容
    7. 在您的playbook中使用`vars`文件中的变量名
- 将Ansible与其他工具（例如Terraform）一起使用时，在第三方密钥管理工具（例如Hashicorp Vault、AWS Secrets Manager等）中存储密钥
  - 这允许所有工具引用密钥的单一真实来源，并防止配置不同步

## 样式

- 使用2空格缩进并始终缩进列表
- 用单个空行分隔以下各项：
  - 两个主机块
  - 两个任务块
  - 主机和包含块
- 对变量名使用`snake_case`
- 在`vars:`映射或变量文件中定义变量时按字母顺序排序
- 始终使用多行映射语法，无论映射中存在多少对
  - 它提高了可读性并减少了版本控制的变更集冲突
- 优先使用单引号而不是双引号
  - 您应该使用双引号的唯一时间是当它们嵌套在单引号内（例如Jinja映射引用）时，或者当您的字符串需要转义字符时（例如使用"\n"表示换行）
  - 如果必须编写长字符串，使用折叠块标量语法（即`>`）用空格替换换行符，或使用字面块标量语法（即`|`）保留换行符；省略所有特殊引号
- play的`host`部分应遵循以下一般顺序：
  - `hosts`声明
  - 按字母顺序排列的主机选项（例如`become`、`remote_user`、`vars`）
  - `pre_tasks`
  - `roles`
  - `tasks`
- 每个任务应遵循以下一般顺序：
  - `name`
  - 任务声明（例如`service:`、`package:`）
  - 任务参数（使用多行映射语法）
  - 循环操作符（例如`loop`）
  - 按字母顺序排列的任务选项（例如`become`、`ignore_errors`、`register`）
  - `tags`
- 对于`include`语句，引用文件名，仅当`include`语句是多行时（例如它们有标签）在`include`语句之间使用空行

## 代码检查

- 使用`ansible-lint`和`yamllint`检查语法并强制执行项目标准
- 使用`ansible-playbook --syntax-check`检查语法错误
- 使用`ansible-playbook --check --diff`执行playbook执行的试运行

<!--
这些指南基于或复制自以下来源：

- [Ansible文档 - 提示和技巧](https://docs.ansible.com/ansible/latest/tips_tricks/index.html)
- [Whitecloud Ansible样式指南](https://github.com/whitecloud/ansible-styleguide)
-->