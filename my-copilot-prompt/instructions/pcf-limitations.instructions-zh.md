---
描述：“Power Apps 组件框架的限制和约束”
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# 局限性

通过 Power Apps 组件框架，您可以创建自己的代码组件来改善 Power Apps 和 Power Pages 中的用户体验。尽管您可以创建自己的组件，但仍有一些限制限制开发人员在代码组件中实现某些功能。以下是一些限制：

## 1. Dataverse 相关 API 不适用于 Canvas 应用程序

Microsoft Dataverse 相关 API（包括 WebAPI）尚不可用于 Power Apps 画布应用程序。有关各个 API 可用性的信息，请参阅 [Power Apps 组件框架 API 参考](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/)。

## 2. 捆绑外部库或使用平台库

代码组件应该使用 [React 控件和平台库](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/react-controls-platform-libraries) 或将所有代码（包括外部库内容）捆绑到主代码包中。 

要查看 Power Apps 命令行界面如何帮助将外部库内容捆绑到特定于组件的包中的示例，请参阅 [Angular 翻转组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/sample-controls/angular-flip-control) 示例。

## 3. 不要使用 HTML Web 存储对象

代码组件不应使用 HTML Web 存储对象（例如 `window.localStorage` 和 `window.sessionStorage`）来存储数据。本地存储在用户浏览器或移动客户端上的数据不安全，并且不能保证可靠可用。

## 4. Canvas 应用程序不支持自定义身份验证

Power Apps 画布应用程序不支持代码组件中的自定义身份验证。使用连接器来获取数据并采取行动。

## 相关主题

- [Power Apps 组件框架 API 参考](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/)
- [Power Apps 组件框架概述](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)
