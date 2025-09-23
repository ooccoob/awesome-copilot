---
mode: 'agent'
description: '为指定 Markdown 文件的某一节生成/更新来自指定文件夹的文件索引或表格。'
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'findTestFiles', 'githubRepo', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
---
# 更新 Markdown 文件的索引

将 `${file}` 中的指定区域更新为 `${input:folder}` 目录的文件索引/表格（匹配 `${input:pattern}`）。

## 步骤
1. 读取 `${file}` 分析结构
2. 列出 `${input:folder}` 下符合 `${input:pattern}` 的文件
3. 判断是否已有索引/表格节，选择覆盖或新增
4. 生成合适的列表/表格结构
5. 更新内容并保持 Markdown 正确性
6. 校验格式与链接有效性

## 信息提取
- 名称、类型、简要描述（首行/标题）、可选的大小与修改时间

## 结构选项
- 简单列表、详细表格、按类别分节

## 要求
- 使用相对路径；按字母排序；处理特殊字符；保持原文档结构
