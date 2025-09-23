---
mode: 'agent'
description: '根据新增/更新需求，更新既有实施计划文件，以交付新特性、重构、升级依赖、设计/架构/基础设施变更等。'
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 更新实施计划（Implementation Plan）

## 主指令

你是一名 AI 代理，需要基于新增或变更的需求，更新 `${file}` 对应的实施计划。输出必须机器可读、可确定、可被其他 AI 或人类直接执行。

## 执行上下文

该提示用于 AI↔AI 通信与自动处理。所有指令须逐字执行，不依赖人工解释。

## 核心要求

- 产出可执行的实施计划
- 用语确定、无歧义
- 结构便于机器解析
- 自包含、无需外部上下文

## 计划结构

- 阶段化、原子化任务
- 每阶段具备完成度量
- 任务可并行，除非声明依赖
- 描述包含精确文件路径/函数名/实现细节

## AI 优化标准

- 明确语言，无需解释
- 使用表格/清单等可解析结构
- 指定路径、标识符与常量
- 在任务中提供完整上下文
- 使用标准化前缀（REQ-/TASK- 等）
- 提供自动校验的验证准则

## 输出文件规范

- 存放目录：`/plan/`
- 命名：`[purpose]-[component]-[version].md`
- purpose 前缀：`upgrade|refactor|feature|data|infrastructure|process|architecture|design`
- 示例：`upgrade-system-command-4.md`、`feature-auth-module-1.md`
- 文件为合法 Markdown，带 front matter

## 模板（强制）

...（保持与英文版一致的模板正文与校验规则，此处略）
