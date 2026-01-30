---
description: '将成熟的课程从域内存文件合并到其说明文件中。语法：`/memory-merger >domain [scope]`其中scope是`global`（默认）、`user`、`workspace`或`ws`。'
---

# 内存合并器

您将域的成熟学习内容从其内存文件合并到其说明文件中，确保知识保留且冗余最少。

**使用待办事项列表**跟踪您在过程步骤中的进度并保持用户知情。

## 范围

内存说明可以存储在两个范围中：

- **全局**（`global`或`user`）- 存储在`<global-prompts>`（`vscode-userdata:/User/prompts/`）并应用于所有VS Code项目
- **工作区**（`workspace`或`ws`）- 存储在`<workspace-instructions>`（`<workspace-root>/.github/instructions/`）并仅应用于当前项目

默认范围是**全局**。

在整个提示中，`<global-prompts>`和`<workspace-instructions>`指代这些目录。

## 语法

```
/memory-merger >domain-name [scope]
```

- `>domain-name` - 必需。要合并的域（例如，`>clojure`、`>git-workflow`、`>prompt-engineering`）
- `[scope]` - 可选。以下之一：`global`、`user`（都表示全局）、`workspace`或`ws`。默认为`global`

**示例：**
- `/memory-merger >prompt-engineering` - 合并全局提示工程内存
- `/memory-merger >clojure workspace` - 合并工作区clojure内存
- `/memory-merger >git-workflow ws` - 合并工作区git-workflow内存

## 过程

### 1. 解析输入并读取文件

- **提取**域和范围从用户输入
- **确定**文件路径：
  - 全局：`<global-prompts>/{domain}-memory.instructions.md` → `<global-prompts>/{domain}.instructions.md`
  - 工作区：`<workspace-instructions>/{domain}-memory.instructions.md` → `<workspace-instructions>/{domain}.instructions.md`
- 用户可能输错了域名，如果找不到内存文件，glob目录并确定那里是否有匹配项。如有疑问，请求用户输入。
- **读取**两个文件（内存文件必须存在；说明文件可能不存在）

### 2. 分析并提议

审查所有内存部分并为合并考虑呈现它们：

```
## 提议合并的内存

### 内存：[标题]
**内容：**[关键点]
**位置：**[在说明中的位置]

[更多内存]...
```

说："请审查这些内存。使用'go'批准所有或指定要跳过的那些。"

**停止并等待用户输入。**

### 3. 定义质量标准

建立10/10标准什么构成令人敬畏的合并结果说明：
1. **零知识损失** - 每个细节、示例和细微差别都保留
2. **最少冗余** - 重叠指导原则整合
3. **最大可扫描性** - 清晰层次、并行结构、策略性粗体、逻辑分组

### 4. 合并和迭代

开发最终合并说明**尚未更新文件**：

1. 起草合并说明，整合批准的内存
2. 根据质量标准评估
3. 完善结构、措辞、组织
4. 重复直到合并说明达到10/10标准

### 5. 更新文件

一旦最终合并说明达到10/10标准：

- **创建或更新**说明文件与最终合并内容
  - 如果创建新文件，包含适当的前置内容
  - **合并来自内存和说明文件的`applyTo`模式**如果两者都存在，确保全面覆盖而不重复
- **从内存文件中移除**合并的部分

## 示例

```
用户："/memory-merger >clojure"

代理：
1. 读取clojure-memory.instructions.md和clojure.instructions.md
2. 提议3个内存进行合并
3. [停止]

用户："go"

代理：
4. 定义10/10的质量标准
5. 合并新说明候选，迭代到10/10
6. 更新clojure.instructions.md
7. 清理clojure-memory.instructions.md
```