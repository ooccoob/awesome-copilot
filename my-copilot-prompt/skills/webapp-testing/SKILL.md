---
name: webapp-testing
description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.
---

# 网络应用程序测试

此技能可以使用 Playwright 自动化对本地 Web 应用程序进行全面测试和调试。

## 何时使用此技能

当您需要执行以下操作时，请使用此技能：
- 在真实浏览器中测试前端功能
- 验证 UI 行为和交互
- 调试 Web 应用程序问题
- 捕获屏幕截图以用于文档或调试
- 检查浏览器控制台日志
- 验证表单提交和用户流程
- 检查跨视口的响应式设计

## 先决条件

- 系统上安装了 Node.js
- 本地运行的 Web 应用程序（或可访问的 URL）
- 如果不存在，剧作家将自动安装

## 核心能力

### 1. 浏览器自动化
- 导航至 URL
- 单击按钮和链接
- 填写表单字段
- 选择下拉菜单
- 处理对话框和警报

### 2. 验证
- 断言元素存在
- 验证文本内容
- 检查元素可见性
- 验证网址
- 测试响应行为

### 3、调试
- 捕获屏幕截图
- 查看控制台日志
- 检查网络请求
- 调试失败的测试

## 使用示例

### 示例 1：基本导航测试
```javascript
// Navigate to a page and verify title
await page.goto('http://localhost:3000');
const title = await page.title();
console.log('Page title:', title);
```

### 示例2：表单交互
```javascript
// Fill out and submit a form
await page.fill('#username', 'testuser');
await page.fill('#password', 'password123');
await page.click('button[type="submit"]');
await page.waitForURL('**/dashboard');
```

### 示例 3：屏幕截图
```javascript
// Capture a screenshot for debugging
await page.screenshot({ path: 'debug.png', fullPage: true });
```

## 指南

1. **始终验证应用程序是否正在运行** - 在运行测试之前检查本地服务器是否可访问
2. **使用显式等待** - 在交互之前等待元素或导航完成
3. **失败时捕获屏幕截图** - 捕获屏幕截图以帮助调试问题
4. **清理资源** - 完成后始终关闭浏览器
5. **优雅地处理超时** - 为缓慢的操作设置合理的超时
6. **增量测试** - 从简单的交互开始，然后再进行复杂的流程
7. **明智地使用选择器** - 优先使用 data-testid 或基于角色的选择器而不是 CSS 类

## 常见模式

### 模式：等待元素
```javascript
await page.waitForSelector('#element-id', { state: 'visible' });
```

### 模式：检查元素是否存在
```javascript
const exists = await page.locator('#element-id').count() > 0;
```

### 模式：获取控制台日志
```javascript
page.on('console', msg => console.log('Browser log:', msg.text()));
```

### 模式：处理错误
```javascript
try {
  await page.click('#button');
} catch (error) {
  await page.screenshot({ path: 'error.png' });
  throw error;
}
```

## 局限性

- 需要 Node.js 环境
- 无法测试本机移动应用程序（请改用 React Native 测试库）
- 复杂的身份验证流程可能存在问题
- 一些现代框架可能需要特定配置
