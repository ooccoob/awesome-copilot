---
描述：'将域内存文件中的成熟课程合并到其指令文件中。语法：`/memory-merger >domain [scope]`，其中范围为 `global`（默认）、`user`、`workspace` 或 `ws`。
---

# 内存合并

您可以将领域内存文件中的成熟知识整合到其指令文件中，确保以最小的冗余保存知识。

**使用待办事项列表**跟踪流程步骤的进度并让用户了解情况。

## 范围

内存指令可以存储在两个范围中：

- **全局**（`global` 或 `user`） - 存储在 `<global-prompts>` (`vscode-userdata:/User/prompts/`) 中并适用于所有 VS Code 项目
- **工作空间**（`workspace` 或 `ws`） - 存储在 `<workspace-instructions>` (`<workspace-root>/.github/instructions/`) 中并仅适用于当前项目

默认范围是**全局**。

在整个提示中，`<global-prompts>` 和 `<workspace-instructions>` 引用这些目录。

## 语法

```
/memory-merger >domain-name [scope]
```

- `>domain-name` - 必需。要合并的域（例如 `>clojure`、`>git-workflow`、`>prompt-engineering`）
- `[scope]` - 可选。以下之一：`global`、`user`（均表示全局）、`workspace` 或 `ws`。默认为 `global`

**示例：**
- `/memory-merger >prompt-engineering` - 合并全局提示工程内存
- `/memory-merger >clojure workspace` - 合并工作区 clojure 内存
- `/memory-merger >git-workflow ws` - 合并工作区 git-workflow 内存

## 工艺流程

### 1. 解析输入并读取文件

- **从用户输入中提取**域和范围
- **确定**文件路径：
  - 全局：`<global-prompts>/{domain}-memory.instructions.md` → `<global-prompts>/{domain}.instructions.md`
  - 工作空间： `<workspace-instructions>/{domain}-memory.instructions.md` → `<workspace-instructions>/{domain}.instructions.md`
- 用户可能输入了错误的域，如果找不到内存文件，则 glob 目录并确定那里是否存在匹配项。如有疑问，请询问用户的意见。
- **读取**两个文件（内存文件必须存在；指令文件可能不存在）

### 2. 分析与建议

查看所有内存部分并将其呈现以供合并考虑：

```
## Proposed Memories for Merger

### Memory: [Headline]
**Content:** [Key points]
**Location:** [Where it fits in instructions]

[More memories]...
```

说：“请回顾这些记忆。用‘继续’批准所有内容或指定要跳过的内容。”

**停止并等待用户输入。**

### 3. 定义质量标准

建立 10/10 标准来确定什么构成了很棒的合并结果指令：
1. **零知识损失** - 保留每个细节、示例和细微差别
2. **最小冗余** - 合并重叠指导
3. **最大可浏览性** - 清晰的层次结构、并行结构、战略大胆、逻辑分组

### 4. 合并和迭代

开发最终合并指令**尚未更新文件**：

1. 起草包含批准记忆的合并指令
2. 根据质量标准进行评估
3. 完善结构、措辞、组织
4. 重复直到合并的指令满足 10/10 标准

### 5. 更新文件

一旦最终合并的指令满足 10/10 标准：

- **使用最终合并的内容创建或更新**说明文件
  - 如果创建新文件，请包含适当的前言
  - **合并内存和指令文件中的 `applyTo` 模式**（如果两者都存在），确保全面覆盖而不重复
- **从内存文件中删除**合并的部分

## 示例

```
User: "/memory-merger >clojure"

Agent:
1. Reads clojure-memory.instructions.md and clojure.instructions.md
2. Proposes 3 memories for merger
3. [STOPS]

User: "go"

Agent:
4. Defines quality bar for 10/10
5. Merges new instructions candidate, iterates to 10/10
6. Updates clojure.instructions.md
7. Cleans clojure-memory.instructions.md
```
