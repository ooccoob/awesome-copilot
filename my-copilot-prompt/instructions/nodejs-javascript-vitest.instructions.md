---
description: "Guidelines for writing Node.js and JavaScript code with Vitest testing"
applyTo: '**/*.js, **/*.mjs, **/*.cjs'
---

# 代码生成指南

## 编码标准
- 将 JavaScript 与 ES2022 功能和 Node.js (20+) ESM 模块结合使用
- 使用 Node.js 内置模块并尽可能避免外部依赖
- 在添加之前询问用户是否需要任何其他依赖项
- 始终对异步代码使用 async/await，并使用 'node:util' promisify 函数来避免回调
- 保持代码简单且可维护
- 使用描述性变量和函数名称
- 除非绝对必要，否则不要添加注释，代码应该是不言自明的
- 切勿使用 `null`，始终使用 `undefined` 作为可选值
- 更喜欢函数而不是类

## 测试
- 使用Vitest进行测试
- 为所有新功能和错误修复编写测试
- 确保测试涵盖边缘情况和错误处理
- 切勿更改原始代码以使其更易于测试，而是编写覆盖原始代码的测试

## 文档
- 添加新功能或进行重大更改时，请根据需要更新 README.md 文件

## 用户交互
- 如果您不确定实施细节、设计选择或需要澄清需求，请提出问题
- 始终使用与问题相同的语言回答，但生成的内容（如代码、注释或文档）使用英语
