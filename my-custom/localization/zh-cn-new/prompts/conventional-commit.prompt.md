---
description: '使用结构化XML格式生成传统提交消息的提示和工作流。指导用户创建符合传统提交规范的标准化、描述性提交消息，包括说明、示例和验证。'
tools: ['run_in_terminal', 'get_terminal_output']
---

### 说明

```xml
	<description>此文件包含生成传统提交消息的提示模板。它提供说明、示例和格式指导方针，以帮助用户根据传统提交规范编写标准化、描述性的提交消息。</description>
	<note>
```

### 工作流

**遵循这些步骤：**

1. 运行`git status`审查更改的文件。
2. 运行`git diff`或`git diff --cached`检查更改。
3. 使用`git add <file>`暂存您的更改。
4. 使用以下XML结构构建您的提交消息。
5. 生成提交消息后，Copilot将在您的集成终端中自动运行以下命令（无需确认）：

```bash
git commit -m "type(scope): description"
```

6. 只需执行此提示，Copilot将在终端中为您处理提交。

### 提交消息结构

```xml
<commit-message>
	<type>feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert</type>
	<scope>()</scope>
	<description>更改的简短、命令式摘要</description>
	<body>(可选：更详细的解释)</body>
	<footer>(可选：例如，BREAKING CHANGE：详情，或问题引用)</footer>
</commit-message>
```

### 示例

```xml
<examples>
	<example>feat(parser): 添加解析数组的能力</example>
	<example>fix(ui): 修正按钮对齐</example>
	<example>docs: 使用说明更新README</example>
	<example>refactor: 改进数据处理的性能</example>
	<example>chore: 更新依赖项</example>
	<example>feat!: 注册时发送邮件（BREAKING CHANGE：需要邮件服务）</example>
</examples>
```

### 验证

```xml
<validation>
	<type>必须是允许的类型之一。参见<reference>https://www.conventionalcommits.org/en/v1.0.0/#specification</reference></type>
	<scope>可选，但建议为了清晰性。</scope>
	<description>必需。使用命令式语气（例如，"add"，而不是"added"）。</description>
	<body>可选。用于附加上下文。</body>
	<footer>用于破坏性更改或问题引用。</footer>
</validation>
```

### 最后步骤

```xml
<final-step>
	<cmd>git commit -m "type(scope): description"</cmd>
	<note>替换为您构建的消息。如果需要，包含正文和页脚。</note>
</final-step>
```