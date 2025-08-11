---
description: "使用结构化 XML 格式生成 Conventional Commit 规范提交信息的提示与工作流。引导用户创建标准化、描述性强的提交信息，符合 Conventional Commits 规范，包含操作指引、示例和校验说明。"
tools: ["run_in_terminal", "get_terminal_output"]
---

### 操作指引

```xml
	<description>本文件为生成 Conventional Commit 规范提交信息的提示模板，提供操作指引、示例和格式规范，帮助用户按照 Conventional Commits 规范编写标准化、描述性强的提交信息。</description>
	<note>
```

### 工作流

**请按以下步骤操作：**

1. 运行 `git status` 查看变更文件。
2. 运行 `git diff` 或 `git diff --cached` 检查具体改动。
3. 用 `git add <file>` 暂存你的更改。
4. 按下方 XML 结构构建你的提交信息。
5. 生成提交信息后，Copilot 会自动在集成终端执行如下命令（无需确认）：

```bash
git commit -m "type(scope): description"
```

6. 只需执行本提示，Copilot 会自动为你完成提交。

### 提交信息结构

```xml
<commit-message>
	<type>feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert</type>
	<scope>()</scope>
	<description>对更改的简短祈使句描述</description>
	<body>（可选：更详细说明）</body>
	<footer>（可选：如 BREAKING CHANGE: 详情，或 issue 关联）</footer>
</commit-message>
```

### 示例

```xml
<examples>
	<example>feat(parser): 新增数组解析能力</example>
	<example>fix(ui): 修正按钮对齐</example>
	<example>docs: 更新 README，补充用法说明</example>
	<example>refactor: 优化数据处理性能</example>
	<example>chore: 升级依赖包</example>
	<example>feat!: 注册时发送邮件（BREAKING CHANGE: 需配置邮件服务）</example>
</examples>
```

### 校验说明

```xml
<validation>
	<type>必须为允许的类型之一。详见 <reference>https://www.conventionalcommits.org/zh-hans/v1.0.0/#summary</reference></type>
	<scope>可选，但推荐填写以增强可读性。</scope>
	<description>必填。使用祈使句（如“新增”，而非“已新增”）。</description>
	<body>可选。用于补充背景或细节。</body>
	<footer>用于 BREAKING CHANGE 或 issue 关联。</footer>
</validation>
```

### 最后一步

```xml
<final-step>
	<cmd>git commit -m "type(scope): description"</cmd>
	<note>请用你构建的提交信息替换。若有 body 和 footer，请一并包含。</note>
</final-step>
```

---

**免责声明**：本文档由[GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot)本地化。因此，可能包含错误。如果您发现任何不适当的翻译或错误，请创建一个[议题](../../issues)。
