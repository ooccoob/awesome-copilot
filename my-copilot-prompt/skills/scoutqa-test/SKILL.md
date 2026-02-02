---
name: scoutqa-test
description: |
  This skill should be used when the user asks to "test this website", "run exploratory testing", "check for accessibility issues", "verify the login flow works", "find bugs on this page", or requests automated QA testing. Triggers on web application testing scenarios including smoke tests, accessibility audits, e-commerce flows, and user flow validation using ScoutQA CLI. IMPORTANT: Use this skill proactively after implementing web application features to verify they work correctly - don't wait for the user to ask for testing.
---

# ScoutQA 测试技能

使用 `scoutqa` CLI 对 Web 应用程序执行人工智能驱动的探索性测试。

**将 ScoutQA 视为智能测试合作伙伴**，可以自主探索、发现问题和验证功能。将测试委托给多个并行的 ScoutQA 执行，以最大限度地提高覆盖范围，同时节省时间。

## 何时使用此技能

在两种情况下使用此技能：

1. **用户请求测试** - 当用户明确要求测试网站或验证功能时
2. **主动验证** - 实现 Web 功能后，自动运行测试以验证实现是否正常工作

**主动使用示例：**
- 实现登录表单后 → 测试身份验证流程
- 添加表单验证后 → 验证验证规则和错误处理
- 构建结帐流程后 → 测试端到端购买流程
- 修复错误后→验证修复是否有效并且没有破坏其他功能

**最佳实践**：完成 Web 功能的实现后，在继续执行其他任务的同时，主动在后台启动 ScoutQA 测试以验证其是否有效。

## 运行测试

### 测试工作流程

复制此清单并跟踪您的进度：

测试进度：
- [ ] 编写具有明确期望的具体测试提示
- [ ] 在后台运行 scoutqa 命令
- [ ] 通知用户执行 ID 和浏览器 URL
- [ ] 提取并分析结果

**第1步：编写具体的测试提示**

请参阅下面的“编写有效的提示”部分以获取指南。

**步骤 2：运行 scoutqa 命令**

**重要**：使用 Bash 工具的超时参数（5000 毫秒 = 5 秒）来捕获执行详细信息：

调用 Bash 工具时，将 `timeout: 5000` 设置为参数：
- 这是 Claude Code 中 Bash 工具的内置超时参数（不是 Unix `timeout` 命令）
- 5 秒后，Bash 工具返回带有任务 ID 的控制权，进程继续在后台运行
- 这与 Unix `timeout` 不同，Unix `timeout` 会杀死进程 - 这里进程继续运行
- 前 5 秒从 ScoutQA 的输出中捕获执行 ID 和浏览器 URL
- 测试继续在 ScoutQA 的基础设施上远程运行后台任务

```bash
scoutqa --url "https://example.com" --prompt "Your test instructions"
```

在最初的几秒钟内，该命令将输出：

- **执行 ID**（例如 `019b831d-xxx`）
- **浏览器 URL**（例如 `https://scoutqa.ai/t/019b831d-xxx`）
- 显示测试进度的初始工具调用

5 秒超时后，Bash 工具返回任务 ID，命令继续在后台运行。测试运行时您可以处理其他任务。超时只是为了捕获初始输出（执行 ID 和浏览器 URL）——测试在本地作为后台任务运行，并在 ScoutQA 的基础设施上远程运行。

**第3步：告知用户执行ID和浏览器URL**

Bash 工具返回任务 ID 后（捕获前 5 秒内的执行详细信息），通知用户：
- ScoutQA 执行 ID 和浏览器 URL，以便他们可以监控浏览器中的进度
- 后台任务 ID（如果他们想稍后检查本地命令输出）

当您继续其他工作时，测试将继续在后台运行。

**第 4 步：提取并分析结果**

有关完整格式，请参阅下面的“呈现结果”部分。

### 命令选项

- `--url`（必需）：要测试的网站 URL
- `--prompt`（必填）：自然语言测试说明
- `--project-id`（可选）：与项目关联以进行跟踪

### 何时使用每个命令

**开始新测试？** → 使用 `scoutqa --url --prompt`
**代理需要更多上下文？** → 使用 `scoutqa send-message` （请参阅“跟进卡住的执行”）

## 编写有效的提示

专注于**要探索和验证的内容**，而不是规定性步骤。 ScoutQA 自主决定如何测试。

**示例：用户注册流程**

```bash
scoutqa --url "https://example.com" --prompt "
Explore the user registration flow. Test form validation edge cases,
verify error handling, and check accessibility compliance.
"
```

**示例：电子商务结帐**

```bash
scoutqa --url "https://shop.example.com" --prompt "
Test the checkout flow. Verify pricing calculations, cart persistence,
payment options, and mobile responsiveness.
"
```

**示例：运行并行测试以实现全面覆盖**

通过在一条消息中进行多个 Bash 工具调用来并行启动多个测试，每个测试将 Bash 工具的 `timeout` 参数设置为 `5000` （毫秒）：

```bash
# Test 1: Authentication & security
scoutqa --url "https://app.example.com" --prompt "
Explore authentication: login/logout, session handling, password reset,
and security edge cases.
"

# Test 2: Core features (runs in parallel)
scoutqa --url "https://app.example.com" --prompt "
Test dashboard and main user workflows. Verify data loading,
CRUD operations, and search functionality.
"

# Test 3: Accessibility (runs in parallel)
scoutqa --url "https://app.example.com" --prompt "
Conduct accessibility audit: WCAG compliance, keyboard navigation,
screen reader support, color contrast.
"
```

**实现**：通过三个 Bash 工具调用发送一条消息。对于每个 Bash 工具调用，将 `timeout` 参数设置为 `5000` 毫秒。 5 秒后，每个 Bash 调用都会返回一个任务 ID，同时进程继续在后台运行。这会捕获初始输出中每个测试的执行 ID 和浏览器 URL，然后所有三个测试继续并行运行（在 ScoutQA 基础设施上作为本地和远程后台任务）。

**关键准则：**

- 描述**测试什么**，而不是**如何测试**（ScoutQA 找出步骤）
- 关注目标、边缘案例和关注点
- 为不同的测试区域运行多个并行执行
- 相信 ScoutQA 能够自主探索和发现问题
- 调用 scoutqa 命令时，始终将 Bash 工具的 `timeout` 参数设置为 `5000` 毫秒（这将在 5 秒后返回控制权，同时进程在后台继续进行）
- 对于并行测试，在一条消息中进行多个 Bash 工具调用
- 请记住：Bash 工具超时 ≠ Unix 超时命令（Bash 超时在后台继续进程，Unix 超时杀死它）

### 常见测试场景

**部署后冒烟测试：**

```bash
scoutqa --url "$URL" --prompt "
Smoke test: verify critical functionality works after deployment.
Check homepage, navigation, login/logout, and key user flows.
"
```

**可访问性审核：**

```bash
scoutqa --url "$URL" --prompt "
Audit accessibility: WCAG 2.1 AA compliance, keyboard navigation,
screen reader support, color contrast, and semantic HTML.
"
```

**电子商务测试：**

```bash
scoutqa --url "$URL" --prompt "
Explore e-commerce functionality: product search/filtering,
cart operations, checkout flow, and pricing calculations.
"
```

**SaaS 应用程序：**

```bash
scoutqa --url "$URL" --prompt "
Test SaaS app: authentication, dashboard, CRUD operations,
permissions, and data integrity.
"
```

**表单验证：**

```bash
scoutqa --url "$URL" --prompt "
Test form validation: edge cases, error handling, required fields,
format validation, and successful submission.
"
```

**移动响应能力：**

```bash
scoutqa --url "$URL" --prompt "
Check mobile experience: responsive layout, navigation,
touch interactions, and viewport behavior.
"
```

**功能验证（实施后）：**

```bash
scoutqa --url "$URL" --prompt "
Verify the new [feature name] works correctly. Test core functionality,
edge cases, error handling, and integration with existing features.
"
```

**示例：编码功能后主动测试**

实现用户注册表单后，自动验证其是否有效：

```bash
scoutqa --url "http://localhost:3000/register" --prompt "
Test the newly implemented registration form. Verify:
- Form validation (email format, password strength, required fields)
- Error messages display correctly
- Successful registration flow
- Edge cases (duplicate emails, special characters, etc.)
"
```

当实施在上下文中是新鲜的时，这会立即捕获问题。

## 展示结果

### 立即演示（开始测试后）

运行 scoutqa 命令后，立即向用户显示执行详细信息：

```markdown
**ScoutQA Test Started**

Execution ID: `019b831d-xxx`
View Live: https://scoutqa.ai/t/019b831d-xxx

The test is running remotely. You can view real-time progress in your browser at the link above while I continue with other tasks.
```

### 最终结果（完成后）

执行完成后，使用以下格式呈现结果：

```markdown
**ScoutQA Test Results**

Execution ID: `ex_abc123`

**Issues Found:**

[High] Accessibility: Missing alt text on logo image

- Impact: Screen readers cannot describe the logo
- Location: Header navigation

[Medium] Usability: Submit button not visible on mobile viewport

- Impact: Users cannot complete form on mobile devices
- Location: Contact form, bottom of page

[Low] Functional: Search returns no results for valid queries

- Impact: Search feature appears broken
- Location: Main search bar

**Summary:** Found 3 issues across accessibility, usability, and functional categories. See full interactive report with screenshots at the URL above.
```

始终包括：

- **执行 ID**（例如 `ex_abc123`）供参考
- **发现的问题** 包括严重性、类别（可访问性、可用性、功能性）、影响和位置

## 跟进陷入困境的执行

如果远程代理遇到困难或需要澄清，请使用 `send-message` 继续：

```bash
# Example: Agent is stuck at login, user provides credentials
scoutqa send-message --execution-id ex_abc123 --prompt "
Use these test credentials: username: testuser@example.com, password: TestPass123
"

# Example: Agent asks which flow to test next
scoutqa send-message --execution-id ex_abc123 --prompt "
Focus on the checkout flow next, skip the wishlist feature
"
```

## 检查测试结果

ScoutQA 测试在 ScoutQA 的基础设施上远程运行。开始测试并设置短超时以捕获执行 ID 后：

1. 测试继续远程运行（不在本地后台运行）
2. 您可以立即继续其他工作
3. 要稍后检查结果，请访问测试开始时提供的浏览器 URL
4. 或者，使用 `scoutqa get-execution --execution-id <id>` 通过 CLI 获取结果

**最佳实践**：通过将 Bash 工具的 `timeout` 参数设置为 `5000` 毫秒来开始测试。 5 秒后，Bash 工具返回控制权并提供任务 ID 和执行详细信息（执行 ID 和浏览器 URL），同时测试继续在后台运行。然后，您可以继续其他工作，并在需要时在 ScoutQA 网站上或通过 CLI 检查结果。

## 故障排除

|问题 |解决方案 |
| ---------------------------- | -------------------------------------------------- |
| __代码0__ |安装 CLI：`npm i -g @scoutqa/cli@latest` |
|身份验证已过期/未经授权 |运行 `scoutqa auth login` |
|测试挂起或需要输入 |使用 `scoutqa send-message --execution-id` |
|检查测试结果 |访问浏览器 URL 或 `scoutqa get-execution --execution-id` |
