## What / When / Why / How
- What: Ansible 风格与最佳实践（可读、幂等、安全、可移植）。
- When: 编写 Playbook/Role/Inventory/变量文件与 CI 集成时。
- Why: 提升幂等与可维护性，减少变更冲突与执行惊喜。
- How: FQCN、模块优先（避免 shell/command/raw）、清晰命名、Vault/第三方密管、lint 与语法检查。

## Key points
- 结构与命名：每个 play/block/task 有动作动词开头的 name；2 空格缩进；YAML 多行映射；变量 snake_case 排序。
- 幂等：优先 idempotent 模块；必须用 shell/command 时配合 creates/removes。
- Inventory：动态清点+标签分组；group_vars 按环境/功能设置。
- 最小权限：仅在必要层级设置 become；任务级优先。
- FQCN：使用 ansible.builtin 等集合保证模块解析一致性。
- 机密：Ansible Vault 分层（vars/vault+vault_ 前缀映射）；与 Terraform 等时用外部密管（HV/AWS SM）。
- Lint 与检查：ansible-lint/yamllint；syntax-check；--check --diff 试运行。
- 风格：分块空行、include 命名、任务字段顺序统一（name→模块→参数→loop→选项→tags）。

## Compact map
- 目标: 幂等/可读/安全
- 结构: plays/roles/vars
- 命名: 动词开头 name
- 模块: FQCN/避免 shell
- 权限: become 最小化
- 机密: Vault/外部密管
- 校验: lint/check/dry-run

## Example questions (10+)
- 我该如何用 creates/removes 让 shell 任务幂等？
- 变量与凭据如何在 group_vars 的 vars/vault 分离？
- 何时使用 block 与 rescue/always 结构？
- 动态库存如何基于标签自动分组环境？
- 模板化与 Jinja 过滤器有哪些易错点？
- include_role vs import_role 的差异与适用场景？
- 如何在 CI 中集成 ansible-lint 与 --check --diff？
- 任务级 become 与 play 级 become 的取舍？
- 常见模块（package/service/file）可替代 shell 的示例？
- 如何组织大型角色的 defaults/vars/handlers/files？
- inventory 与变量优先级冲突如何排查？

—
Source: d:\mycode\awesome-copilot\instructions\ansible.instructions.md | Generated: {{timestamp}}
