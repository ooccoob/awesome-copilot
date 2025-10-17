## What
- 使用 Playwright MCP 自动化填写指定在线表单（不提交），并在提交前请求人工复核。

## When to use
- 需要演示/验证自动化填表流程，确保数据准确但避免产生真实提交。

## Why it matters
- 降低手工成本；在安全前提下快速回放填表步骤以复核。

## How (关键流程)
- 启动浏览器 → 打开目标 URL → 定位输入控件 → 填写文本/日期/时间 → 上传图片 → 停止在提交前 → 请求复核
- 文件路径与权限检查；显式不触发提交事件

## Example questions (≥10)
1. 打开 https://forms.microsoft.com/url-of-my-form 并等待表单就绪的稳健选择器应该如何写？
2. 依次填入“Show: playwright live”“Date: 15 July”“Time: 1:00 AM”。
3. 为“Topic”文本框填入指定主题并截图确认。
4. 在文件上传控件上传本地图片 /Users/myuserName/Downloads/my-image.png 并校验成功态。
5. 如何确保在任何情况下都不会点击“Submit”？加入保护断言。
6. 完成后生成步骤截图与 HAR 归档以便复核。
7. 若元素动态加载，提供等待策略（locator + expect + timeout）。
8. 把选择器与步骤封装为可复用函数并输出示例。
9. 失败重试策略与错误截图保存位置如何配置？
10. 生成一段“请审核信息并确认是否提交”的复核提示文本。

## Key points
- CN: 稳健定位、不提交保护、文件上传、证据留存
- EN: Robust locators, no-submit guard, file upload, evidence capture

## Mind map (简要)
- 打开 → 定位 → 填写 → 上传 → 复核 → 证据

---
Source file: d:\mycode\awesome-copilot\prompts\playwright-automation-fill-in-form.prompt.md
Generated: 2025-10-17T00:00:00Z
