---
name: requesting-code-review
description: 在完成任务、实现主要功能或合并前验证工作满足要求时使用 - 派遣superpowers:code-reviewer子代理在继续之前对照计划或要求审查实现
---

# 请求代码审查

派遣superpowers:code-reviewer子代理在问题级联前捕获它们。

**核心原则：** 早审查，常审查。

## 何时请求审查

**强制性：**
- 在子agent驱动开发中每个任务后
- 完成主要功能后
- 合并到main前

**可选但有价值：**
- 卡住时（新视角）
- 重构前（基线检查）
- 修复复杂错误后

## 如何请求

**1. 获取git SHA：**
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # 或 origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**2. 派遣code-reviewer子代理：**

使用Task工具与superpowers:code-reviewer类型，填写`code-reviewer.md`中的模板

**占位符：**
- `{WHAT_WAS_IMPLEMENTED}` - 您刚构建的
- `{PLAN_OR_REQUIREMENTS}` - 它应该做的
- `{BASE_SHA}` - 起始提交
- `{HEAD_SHA}` - 结束提交
- `{DESCRIPTION}` - 简要摘要

**3. 对反馈采取行动：**
- 立即修复关键问题
- 在继续前修复重要问题
- 记录次要问题供以后处理
- 如果审查者错误就回绝（带推理）

## 示例

```
[刚完成任务2：添加验证函数]

您：让我在继续前请求代码审查。

BASE_SHA=$(git log --oneline | grep "Task 1" | head -1 | awk '{print $1}')
HEAD_SHA=$(git rev-parse HEAD)

[派遣superpowers:code-reviewer子代理]
  WHAT_WAS_IMPLEMENTED: 会话索引的验证和修复函数
  PLAN_OR_REQUIREMENTS: docs/plans/deployment-plan.md中的任务2
  BASE_SHA: a7981ec
  HEAD_SHA: 3df7661
  DESCRIPTION: 添加了带4种问题类型的verifyIndex()和repairIndex()

[子代理返回]：
  优点：干净架构，真实测试
  问题：
    重要：缺少进度指示器
    次要：报告间隔的魔术数字（100）
  评估：准备好继续

您：[修复进度指示器]
[继续到任务3]
```

## 与工作流集成

**子Agent驱动开发：**
- 每个任务后审查
- 在问题复合前捕获它们
- 在移动到下一个任务前修复

**执行计划：**
- 每个批次（3个任务）后审查
- 获得反馈，应用，继续

**临时开发：**
- 合并前审查
- 卡住时审查

## 红旗

**绝不：**
- 因为"简单"跳过审查
- 忽略关键问题
- 在未修复重要问题下继续
- 与有效技术反馈争论

**如果审查者错误：**
- 用技术推理回绝
- 显示证明它工作的代码/测试
- 请求澄清

参见模板：requesting-code-review/code-reviewer.md