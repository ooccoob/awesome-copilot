````prompt
---
description: '智能 Git Flow 分支创建器：分析 git status/diff，依据 nvie Git Flow 分支模型生成合适的分支并自动创建。'
tools: ['run_in_terminal', 'get_terminal_output']
---

### 指南

```xml
<instructions>
	<title>Git Flow Branch Creator</title>
	<description>本提示会使用 git status 与 git diff（或 git diff --cached）分析当前改动，依据 Git Flow 分支模型智能判定分支类型并生成语义化分支名。</description>
	<note>
		直接运行该提示，Copilot 将分析改动并为你创建合适的 Git Flow 分支。
	</note>
</instructions>
```

### 工作流

**按以下步骤执行：**

1. 运行 `git status` 查看仓库状态与变更文件
2. 运行 `git diff`（未暂存改动）或 `git diff --cached`（已暂存改动）分析改动性质
3. 结合下方“Git Flow 分支分析框架”进行判定
4. 确定分支类型
5. 生成符合约定的语义化分支名
6. 创建并自动切换到该分支
7. 输出分析总结与后续步骤

### Git Flow 分支分析框架

```xml
<analysis-framework>
	<branch-types>
		<feature>
			<purpose>新特性、增强、非关键改进</purpose>
			<branch-from>develop</branch-from>
			<merge-to>develop</merge-to>
			<naming>feature/descriptive-name 或 feature/ticket-number-description</naming>
			<indicators>
				<indicator>新增功能</indicator>
				<indicator>UI/UX 改进</indicator>
				<indicator>新增 API 端点/方法</indicator>
				<indicator>非破坏性的数据库 schema 增加</indicator>
				<indicator>新增配置项</indicator>
				<indicator>非关键的性能优化</indicator>
			</indicators>
		</feature>

		<release>
			<purpose>发布准备、版本号提升、最终测试</purpose>
			<branch-from>develop</branch-from>
			<merge-to>develop AND master</merge-to>
			<naming>release-X.Y.Z</naming>
			<indicators>
				<indicator>版本号变更</indicator>
				<indicator>构建配置更新</indicator>
				<indicator>文档定稿</indicator>
				<indicator>发布前的小修小补</indicator>
				<indicator>发布说明更新</indicator>
				<indicator>依赖版本锁定</indicator>
			</indicators>
		</release>

		<hotfix>
			<purpose>生产环境关键问题的紧急修复</purpose>
			<branch-from>master</branch-from>
			<merge-to>develop AND master</merge-to>
			<naming>hotfix-X.Y.Z 或 hotfix/critical-issue-description</naming>
			<indicators>
				<indicator>安全漏洞修复</indicator>
				<indicator>生产关键故障</indicator>
				<indicator>数据损坏修复</indicator>
				<indicator>服务中断处理</indicator>
				<indicator>紧急配置变更</indicator>
			</indicators>
		</hotfix>
	</branch-types>
</analysis-framework>
```

### 分支命名约定

```xml
<naming-conventions>
	<feature-branches>
		<format>feature/[ticket-number-]descriptive-name</format>
		<examples>
			<example>feature/user-authentication</example>
			<example>feature/PROJ-123-shopping-cart</example>
			<example>feature/api-rate-limiting</example>
			<example>feature/dashboard-redesign</example>
		</examples>
	</feature-branches>

	<release-branches>
		<format>release-X.Y.Z</format>
		<examples>
			<example>release-1.2.0</example>
			<example>release-2.1.0</example>
			<example>release-1.0.0</example>
		</examples>
	</release-branches>

	<hotfix-branches>
		<format>hotfix-X.Y.Z OR hotfix/critical-description</format>
		<examples>
			<example>hotfix-1.2.1</example>
			<example>hotfix/security-patch</example>
			<example>hotfix/payment-gateway-fix</example>
			<example>hotfix-2.1.1</example>
		</examples>
	</hotfix-branches>
</naming-conventions>
```

### 分析流程

```xml
<analysis-process>
	<step-1>
		<title>改动性质分析</title>
		<description>从修改文件类型、目录与差异内容判断改动性质</description>
		<criteria>
			<files-modified>关注扩展名、目录结构与用途</files-modified>
			<change-scope>判断新增/修复/发布准备</change-scope>
			<urgency-level>评估是否为生产级紧急问题</urgency-level>
		</criteria>
	</step-1>

	<step-2>
		<title>Git Flow 分类</title>
		<description>将改动映射到合适的 Git Flow 分支类型</description>
		<decision-tree>
			<question>是否为生产关键紧急修复？</question>
			<if-yes>选择 hotfix</if-yes>
			<if-no>
				<question>是否为发布准备（版本、发布说明、构建配置）？</question>
				<if-yes>选择 release</if-yes>
				<if-no>默认选择 feature</if-no>
			</if-no>
		</decision-tree>
	</step-2>

	<step-3>
		<title>分支命名生成</title>
		<description>创建语义化且简洁的分支名</description>
		<guidelines>
			<use-kebab-case>使用小写连字符</use-kebab-case>
			<be-descriptive>清晰表意</be-descriptive>
			<include-context>可包含工单号或上下文</include-context>
			<keep-concise>保持简洁</keep-concise>
		</guidelines>
	</step-3>
</analysis-process>
```

### 边界情况与校验

```xml
<edge-cases>
	<mixed-changes>
		<scenario>同时包含特性与缺陷修复</scenario>
		<resolution>优先选择占比更大者，或建议拆分为多个分支</resolution>
	</mixed-changes>

	<no-changes>
		<scenario>无改动</scenario>
		<resolution>提示用户先完成变更或检查 git status</resolution>
	</no-changes>

	<existing-branch>
		<scenario>已位于 feature/hotfix/release 分支</scenario>
		<resolution>评估是否仍需新建分支</resolution>
	</existing-branch>

	<conflicting-names>
		<scenario>建议的分支名已存在</scenario>
		<resolution>追加序号后缀或给出备选名</resolution>
	</conflicting-names>
</edge-cases>
```

### 示例

```xml
<examples>
	<example-1>
		<scenario>新增用户注册 API</scenario>
		<analysis>新增功能，非紧急</analysis>
		<branch-type>feature</branch-type>
		<branch-name>feature/user-registration-api</branch-name>
		<command>git checkout -b feature/user-registration-api develop</command>
	</example-1>

	<example-2>
		<scenario>修复认证安全漏洞</scenario>
		<analysis>安全修复，生产紧急</analysis>
		<branch-type>hotfix</branch-type>
		<branch-name>hotfix/auth-security-patch</branch-name>
		<command>git checkout -b hotfix/auth-security-patch master</command>
	</example-2>

	<example-3>
		<scenario>版本升级至 2.1.0 并完善发布说明</scenario>
		<analysis>发布准备</analysis>
		<branch-type>release</branch-type>
		<branch-name>release-2.1.0</branch-name>
		<command>git checkout -b release-2.1.0 develop</command>
	</example-3>

	<example-4>
		<scenario>提升数据库查询性能并更新缓存策略</scenario>
		<analysis>性能优化，非关键</analysis>
		<branch-type>feature</branch-type>
		<branch-name>feature/database-performance-optimization</branch-name>
		<command>git checkout -b feature/database-performance-optimization develop</command>
	</example-4>
</examples>
```

### 校验清单

```xml
<validation>
	<pre-analysis>
		<check>仓库状态干净（避免冲突的未提交更改）</check>
		<check>起始分支合理（feature/release 从 develop，hotfix 从 master）</check>
		<check>远端同步最新</check>
	</pre-analysis>

	<analysis-quality>
		<check>覆盖所有改动文件</check>
		<check>分支类型选择符合 Git Flow 原则</check>
		<check>分支命名语义化且符合约定</check>
		<check>考虑并处理边界情况</check>
	</analysis-quality>

	<execution-safety>
		<check>目标基线分支（develop/master）存在且可访问</check>
		<check>建议分支名不与现有重复</check>
		<check>有创建分支的权限</check>
	</execution-safety>
</validation>
```

### 最终执行

```xml
<execution-protocol>
	<analysis-summary>
		<git-status>git status 输出</git-status>
		<git-diff>git diff 关键片段</git-diff>
		<change-analysis>改动类型分析</change-analysis>
		<branch-decision>分支类型判定理由</branch-decision>
	</analysis-summary>

	<branch-creation>
		<command>git checkout -b [branch-name] [source-branch]</command>
		<confirmation>确认分支创建与当前分支</confirmation>
		<next-steps>给出提交、推送等后续建议</next-steps>
	</branch-creation>

	<fallback-options>
		<alternative-names>提供 2-3 个备选分支名</alternative-names>
		<manual-override>若判定不准，允许手动指定类型</manual-override>
	</fallback-options>
</execution-protocol>
```

### Git Flow 参考

```xml
<gitflow-reference>
	<main-branches>
		<master>生产分支，每个提交对应一次发布</master>
		<develop>开发集成分支，汇集最新开发变更</develop>
	</main-branches>

	<supporting-branches>
		<feature>从 develop 分出，合回 develop</feature>
		<release>从 develop 分出，合回 develop 与 master</release>
		<hotfix>从 master 分出，合回 develop 与 master</hotfix>
	</supporting-branches>

	<merge-strategy>
		<flag>合并使用 --no-ff 保留分支历史</flag>
		<tagging>在 master 上打 tag 标记发布</tagging>
		<cleanup>合并后删除分支</cleanup>
	</merge-strategy>
</gitflow-reference>
```

---

**免责声明**：本文件由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 自动本地化，可能存在不准确之处。若发现不当或错误翻译，请提交 [Issue](https://github.com/ooccoob/datafill/issues) 进行反馈。

````
