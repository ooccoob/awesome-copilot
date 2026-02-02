---
name: chrome-devtools
description: 'Expert-level browser automation, debugging, and performance analysis using Chrome DevTools MCP. Use for interacting with web pages, capturing screenshots, analyzing network traffic, and profiling performance.'
license: MIT
---

# Chrome 开发者工具代理

## 概述

用于控制和检查实时 Chrome 浏览器的专业技能。该技能利用 `chrome-devtools` MCP 服务器来执行各种与浏览器相关的任务，从简单的导航到复杂的性能分析。

## 何时使用

在以下情况下使用此技能：

- **浏览器自动化**：导航页面、单击元素、填写表单和处理对话框。
- **目视检查**：截取网页的屏幕截图或文本快照。
- **调试**：检查控制台消息、评估页面上下文中的 JavaScript 以及分析网络请求。
- **性能分析**：记录和分析性能跟踪，以识别瓶颈和核心 Web 重要问题。
- **模拟**：调整视口大小或模拟网络/CPU 条件。

## 工具类别

### 1. 导航和页面管理

- `new_page`：打开新选项卡/页面。
- `navigate_page`：转到特定 URL、重新加载或导航历史记录。
- `select_page`：在打开的页面之间切换上下文。
- `list_pages`：查看所有打开的页面及其 ID。
- `close_page`：关闭特定页面。
- `wait_for`：等待页面上出现特定文本。

### 2. 输入与交互

- `click`：单击一个元素（使用快照中的 `uid`）。
- `fill` / `fill_form`：在输入中键入文本或一次填充多个字段。
- `hover`：将鼠标移到元素上。
- `press_key`：发送键盘快捷键或特殊键（例如“Enter”、“Control+C”）。
- `drag`：拖放元素。
- `handle_dialog`：接受或关闭浏览器警报/提示。
- `upload_file`：通过文件输入上传文件。

### 三、调试检查

- `take_snapshot`：获取基于文本的可访问性树（最适合识别元素）。
- `take_screenshot`：捕获页面或特定元素的视觉表示。
- `list_console_messages` / `get_console_message`：检查页面的控制台输出。
- `evaluate_script`：在页面上下文中运行自定义 JavaScript。
- `list_network_requests` / `get_network_request`：分析网络流量和请求详细信息。

### 4. 仿真与性能

- `resize_page`：更改视口尺寸。
- `emulate`：限制 CPU/网络或模拟地理位置。
- `performance_start_trace`：开始记录性能概况。
- `performance_stop_trace`：停止记录并保存轨迹。
- `performance_analyze_insight`：从记录的性能数据中获取详细分析。

## 工作流程模式

### 模式 A：识别元素（快照优先）

在查找元素时，始终首选 `take_snapshot` 而不是 `take_screenshot`。快照提供交互工具所需的 `uid` 值。

```markdown
1. `take_snapshot` to get the current page structure.
2. Find the `uid` of the target element.
3. Use `click(uid=...)` or `fill(uid=..., value=...)`.
```

### 模式 B：排除错误

当页面出现故障时，请检查控制台日志和网络请求。

```markdown
1. `list_console_messages` to check for JavaScript errors.
2. `list_network_requests` to identify failed (4xx/5xx) resources.
3. `evaluate_script` to check the value of specific DOM elements or global variables.
```

### 模式 C：性能分析

确定页面速度缓慢的原因。

```markdown
1. `performance_start_trace(reload=true, autoStop=true)`
2. Wait for the page to load/trace to finish.
3. `performance_analyze_insight` to find LCP issues or layout shifts.
```

## 最佳实践

- **上下文感知**：如果您不确定哪个选项卡当前处于活动状态，请始终运行 `list_pages` 和 `select_page`。
- **快照**：在任何主要导航或 DOM 更改后拍摄新快照，因为 `uid` 值可能会更改。
- **超时**：对 `wait_for` 使用合理的超时，以避免挂在加载缓慢的元素上。
- **屏幕截图**：谨慎使用 `take_screenshot` 进行视觉验证，但依赖 `take_snapshot` 进行逻辑处理。
