---
name: writing-plans
description: 当设计完成且您需要为没有代码库上下文的工程师提供详细实现任务时使用 - 创建全面实现计划，包含确切文件路径、完整代码示例和验证步骤，假设工程师具有最少的领域知识
---

# 编写计划

## 概述

编写全面实现计划，假设工程师对我们的代码库零上下文且品味可疑。记录他们需要知道的一切：每个任务要触摸哪些文件、代码、测试、他们可能需要的文档、如何测试。给他们整个计划作为小任务。DRY。YAGNI。TDD。频繁提交。

假设他们是熟练的开发者，但几乎不了解我们的工具集或问题域。假设他们不太了解好的测试设计。

**开始时宣布：** "我正在使用编写计划技能创建实现计划。"

**上下文：** 这应该在专用工作树中运行（由头脑风暴技能创建）。

**保存计划到：** `docs/plans/YYYY-MM-DD-<功能名称>.md`

## 小任务粒度

**每个步骤是一个动作（2-5分钟）：**
- "写失败测试" - 步骤
- "运行确保它失败" - 步骤
- "写使测试通过的最少代码" - 步骤
- "运行测试确保通过" - 步骤
- "提交" - 步骤

## 计划文档标题

**每个计划必须以此标题开始：**

```markdown
# [功能名称] 实现计划

> **对于Claude：** 必需子技能：使用superpowers:executing-plans逐个任务实现此计划。

**目标：** [一句话描述这构建什么]

**架构：** [关于方法的2-3句话]

**技术栈：** [关键技术/库]

---
```

## 任务结构

```markdown
### 任务N：[组件名称]

**文件：**
- 创建：`exact/path/to/file.py`
- 修改：`exact/path/to/existing.py:123-145`
- 测试：`tests/exact/path/to/test.py`

**步骤1：写失败测试**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```

**步骤2：运行测试验证失败**

运行：`pytest tests/path/test.py::test_name -v`
预期：失败，"function not defined"

**步骤3：写最小实现**

```python
def function(input):
    return expected
```

**步骤4：运行测试验证通过**

运行：`pytest tests/path/test.py::test_name -v`
预期：通过

**步骤5：提交**

```bash
git add tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```
```

## 记住
- 总是确切文件路径
- 计划中完整代码（不是"添加验证"）
- 带预期输出的确切命令
- 用@语法引用相关技能
- DRY、YAGNI、TDD、频繁提交

## 执行交接

保存计划后，提供执行选择：

**"计划完成并保存到`docs/plans/<filename>.md`。两个执行选项：**

**1. 子代理驱动（此会话）** - 我每个任务派遣新子代理，任务间审查，快速迭代

**2. 并行会话（分离）** - 在工作树中打开新会话，带检查点批次执行

**哪种方法？"**

**如果选择子代理驱动：**
- **必需子技能：** 使用superpowers:subagent-driven-development
- 留在此会话
- 每个任务新子代理 + 代码审查

**如果选择并行会话：**
- 指导他们在工作树中打开新会话
- **必需子技能：** 新会话使用superpowers:executing-plans