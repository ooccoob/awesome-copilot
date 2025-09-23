---
mode: 'agent'
description: '依据 https://llmstxt.org/ 规范更新仓库根目录 llms.txt，使其反映最新文档与规格结构，且保持对 LLM 友好。'
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 更新 LLMs.txt 文件

更新仓库根目录的 `llms.txt` 以反映文档、规格或结构变更；保持规范合规与对 LLM 友好。

## 分析与规划
- 审阅当前 llms.txt 与官方规范
- 分析仓库结构与变化
- 发现新增/删除/迁移的关键文档
- 制定更新计划（新增、移除、重组）

## 实施要求
- 严格遵循 llmstxt.org 的结构（H1、引用摘要、若干 H2 区段列文件）
- 使用相对路径与清晰描述
- 仅收录理解仓库所必需的文件
- 验证所有链接有效

## 成功标准
- 结构合规；链接有效；内容清晰；对 LLM 与人类均友好
