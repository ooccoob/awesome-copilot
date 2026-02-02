---
description: 'Power Apps Component Framework overview and fundamentals'
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# Power Apps 组件框架概述

Power Apps 组件框架使专业开发人员和应用程序开发人员能够为模型驱动和画布应用程序创建代码组件。这些代码组件可用于增强处理表单、视图、仪表板和画布应用程序屏幕上的数据的用户的用户体验。

## 关键能力

您可以使用 PCF 来：
- 将表单上显示数字文本值的列替换为 `dial` 或 `slider` 代码组件
- 将列表转换为绑定到数据集的完全不同的视觉体验，例如 `Calendar` 或 `Map`

## 重要限制

- Power Apps 组件框架仅适用于统一接口，不适用于旧版 Web 客户端
- 本地环境当前不支持 Power Apps 组件框架

## PCF 与 Web 资源有何不同

与 HTML Web 资源不同，代码组件是：
- 呈现为同一上下文的一部分
- 与任何其他组件同时加载
- 为用户提供无缝体验

代码组件可以是：
- 在 Power Apps 功能的全部范围内使用
- 在不同的表和表单中多次重复使用
- 将所有 HTML、CSS 和 TypeScript 文件捆绑到一个解决方案包中
- 跨环境移动
- 通过 AppSource 提供

## 主要优势

### 丰富的框架API
- 组件生命周期管理
- 上下文数据和元数据访问
- 通过 Web API 无缝访问服务器
- 实用程序和数据格式化方法
- 设备功能：摄像头、定位、麦克风
- 用户体验元素：对话框、查找、全页渲染

### 发展效益
- 支持现代网络实践
- 优化性能
- 复用性高
- 将所有文件捆绑到一个解决方案文件中
- 处理因性能原因而被销毁并重新加载的情况，同时保留状态

## 许可要求

Power Apps 组件框架许可基于所使用的数据和连接的类型：

### 高级代码组件
直接通过用户的浏览器客户端（而不是通过连接器）连接到外部服务或数据的代码组件：
- 被视为优质组件
- 使用这些的应用程序变得高级
- 最终用户需要 Power Apps 许可证

通过添加到清单来声明为高级：
```xml
<external-service-usage enabled="true">
  <domain>www.microsoft.com</domain>
</external-service-usage>
```

### 标准代码组件
不连接外部服务或数据的代码组件：
- 使用这些标准功能的应用程序仍然是标准的
- 最终用户需要最低 Office 365 许可证

**注意**：如果在连接到 Microsoft Dataverse 的模型驱动应用程序中使用代码组件，最终用户将需要 Power Apps 许可证。

## 相关资源

- [什么是代码组件？](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/custom-controls-overview)
- [画布应用程序的代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/component-framework-for-canvas-apps)
- [创建并构建代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf)
- [学习 Power Apps 组件框架](https://learn.microsoft.com/en-us/training/paths/use-power-apps-component-framework)
- [在 Power Pages 中使用代码组件](https://learn.microsoft.com/en-us/power-apps/maker/portals/component-framework)

## 培训资源

- [使用 Power Apps 组件框架创建组件 - 培训](https://learn.microsoft.com/en-us/training/paths/create-components-power-apps-component-framework/)
- [Microsoft 认证：Power Platform 开发助理](https://learn.microsoft.com/en-us/credentials/certifications/power-platform-developer-associate/)
