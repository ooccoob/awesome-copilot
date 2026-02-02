---
description: 'Best practices and guidance for developing PCF code components'
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj,css,html}'
---

# 代码组件的最佳实践和指南

开发、部署和维护代码组件需要跨多个领域的知识组合。本文概述了为开发代码组件的专业人员制定的最佳实践和指南。

## Power Apps 组件框架

### 避免将开发版本部署到 Dataverse

代码组件可以在[生产或开发模式](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/code-components-alm#building-pcfproj-code-component-projects)中构建。避免将开发版本部署到 Dataverse，因为它们会对性能产生不利影响，甚至可能因其大小而阻止部署。即使您计划稍后部署发布版本，如果您没有自动发布管道，也很容易忘记重新部署。更多信息：[调试自定义控件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/debugging-custom-controls)。

### 避免使用不受支持的框架方法

其中包括使用 `ComponentFramework.Context` 上存在的未记录的内部方法。这些方法可能有效，但由于不受支持，它们可能在未来版本中停止工作。不支持使用访问主机应用程序 HTML 文档对象模型 (DOM) 的控制脚本。主机应用程序 DOM 中代码组件边界之外的任何部分如有更改，恕不另行通知。

### 使用 `init` 方法请求网络所需资源

当宿主上下文加载代码组件时，首先调用 `init` 方法。使用此方法请求任何网络资源（例如元数据），而不是等待 `updateView` 方法。如果在请求返回之前调用 `updateView` 方法，您的代码组件必须处理此状态并提供可视化加载指示器。

### 清理 `destroy` 方法内的资源

当从浏览器 DOM 中删除代码组件时，托管上下文会调用 `destroy` 方法。使用 `destroy` 方法关闭任何 `WebSockets` 并删除添加到容器元素外部的事件处理程序。如果您使用的是 React，请在 `destroy` 方法中使用 `ReactDOM.unmountComponentAtNode` 。以这种方式清理资源可以防止由于在给定浏览器会话中加载和卸载代码组件而导致的任何性能问题。

### 避免对数据集属性进行不必要的刷新调用

如果您的代码组件是数据集类型，则绑定的数据集属性会公开 `refresh` 方法，该方法会导致托管上下文重新加载数据。调用此方法会不必要地影响代码组件的性能。

### 尽量减少对 `notifyOutputChanged` 的调用

在某些情况下，不希望每次调用 `notifyOutputChanged` 时都更新 UI 控件（例如按键或鼠标移动事件），因为更多的调用会导致传播到父上下文的事件多于所需的事件。相反，请考虑在控件失去焦点或用户的触摸或鼠标事件完成时使用事件。

### 检查 API 可用性

在为不同主机（模型驱动应用程序、画布应用程序、门户）开发代码组件时，请务必检查您用于支持这些平台的 API 的可用性。例如，`context.webAPI` 在画布应用程序中不可用。有关各个 API 可用性的信息，请参阅 [Power Apps 组件框架 API 参考](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/)。

### 管理传递给 `updateView` 的临时空属性值

当数据未准备好时，空值将传递给 `updateView` 方法。您的组件应该考虑这种情况，并期望数据可能为空，并且后续的 `updateView` 循环可以包含更新的值。 `updateView` 可用于 [standard](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/control/updateview) 和 [React](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/react-control/updateview) 组件。

## 模型驱动的应用程序

### 不要直接与 `formContext` 交互

如果您有使用客户端 API 的经验，您可能习惯于与 `formContext` 交互以访问属性、控件并调用 API 方法，例如 `save`、`refresh` 和 `setNotification`。代码组件预计可以跨各种产品（例如模型驱动应用程序、画布应用程序和仪表板）工作，因此它们不能依赖于 `formContext`。

解决方法是将代码组件绑定到列并向该列添加 `OnChange` 事件处理程序。代码组件可以更新列值，并且 `OnChange` 事件处理程序可以访问 `formContext`。将来将添加对自定义事件的支持，这将允许在控件外部通信更改，而无需添加列配置。

### 限制对 `WebApi` 的调用的大小和频率

使用 `context.WebApi` 方法时，请限制调用次数和数据量。每次调用 `WebApi` 时，都会计入用户的 API 权限和服务保护限制。对记录执行 CRUD 操作时，请考虑有效负载的大小。一般来说，请求负载越大，代码组件的速度就越慢。

## 画布应用程序

### 最大限度地减少屏幕上的组件数量

每次将组件添加到画布应用程序时，都需要有限的时间来渲染。渲染时间随着添加的每个组件而增加。当您使用开发人员性能工具向屏幕添加更多内容时，请仔细测量代码组件的性能。

目前，每个代码组件都捆绑了自己的共享库，例如 Fluent UI 和 React。加载同一库的多个实例不会多次加载这些库。但是，加载多个不同的代码组件会导致浏览器加载这些库的多个捆绑版本。将来，这些库将能够与代码组件一起加载和共享。

### 允许开发者设计您的代码组件的样式

当应用程序开发者从画布应用程序内部使用代码组件时，他们希望使用与其应用程序的其余部分相匹配的样式。使用输入属性为主题元素提供自定义选项，例如颜色和大小。使用 Microsoft Fluent UI 时，将这些属性映射到库提供的主题元素。将来，主题支持将添加到代码组件中，以使此过程变得更容易。

### 遵循 Canvas 应用程序性能最佳实践

Canvas 应用程序在应用程序和解决方案检查器内部提供了广泛的最佳实践。在添加代码组件之前，请确保您的应用程序遵循这些建议。有关更多信息，请参阅：

- [提高画布应用性能的技巧](https://learn.microsoft.com/en-us/powerapps/maker/canvas-apps/performance-tips)
- [Power Apps 中优化性能的注意事项](https://powerapps.microsoft.com/blog/considerations-for-optimized-performance-in-power-apps/)

## TypeScript 和 JavaScript

### ES5 与 ES6

默认情况下，代码组件以 ES5 为目标，以支持旧版浏览器。如果您不想支持这些较旧的浏览器，您可以在 `pcfproj` 文件夹的 `tsconfig.json` 中将目标更改为 ES6。更多信息：[ES5 与 ES6](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/debugging-custom-controls#es5-vs-es6)。

### 模块导入

始终将所需的模块捆绑为代码组件的一部分，而不是使用需要使用 `SCRIPT` 标记加载的脚本。例如，如果您想要使用非 Microsoft 图表 API，其中示例显示将 `<script type="text/javascript" src="somechartlibrary.js></script>` 添加到页面，则代码组件内部不支持此操作。捆绑所有必需的模块可以将代码组件与其他库隔离，并且还支持在离线模式下运行。

> **注意**：尚不支持使用组件清单中的库节点来支持跨组件共享库。

### 棉绒

Linting 是工具可以扫描代码以查找潜在问题的地方。 `pac pcf init` 使用的模板将 `eslint` 模块安装到您的项目中，并通过添加 `.eslintrc.json` 文件来配置它。

要配置，请在命令行使用：

```bash
npx eslint --init
```

然后根据提示回答以下问题：

- **您想如何使用 ESLint？** 答案：检查语法、发现问题并强制执行代码风格
- **您的项目使用什么类型的模块？**答案：JavaScript 模块（导入/导出）
- **您的项目使用哪个框架？**答案：React
- **您的项目使用 TypeScript 吗？** 答案：是
- **你的代码在哪里运行？**答案：浏览器
- **您希望如何为您的项目定义风格？** 答案：回答有关您的风格的问题
- **您希望配置文件采用什么格式？** 答案：JSON
- **您使用什么样式的缩进？**答案：空格
- **字符串使用什么引号？** 答案：单引号
- **您使用什么行结尾？** 答案：Windows
- **您需要分号吗？** 答案：是

在使用 `eslint` 之前，您需要向 `package.json` 添加一些脚本：

```json
"scripts": {
   ...
   "lint": "eslint MY_CONTROL_NAME --ext .ts,.tsx",
   "lint:fix": "npm run lint -- --fix"
}
```

现在在命令行中，您可以使用：

```bash
npm run lint:fix
```

此外，您可以通过添加到 `.eslintrc.json` 来添加要忽略的文件：

```json
"ignorePatterns": ["**/generated/*.ts"]
```

## HTML 浏览器用户界面开发

### 使用 Microsoft Fluent UI React

[Fluent UI React](https://developer.microsoft.com/fluentui#/get-started/web) 是官方 [开源](https://github.com/microsoft/fluentui) React 前端框架，旨在构建无缝融入各种 Microsoft 产品的体验。 Power Apps 本身使用 Fluent UI，这意味着您可以创建与其他应用程序一致的 UI。

#### 使用 Fluent 中基于路径的导入来减小包大小

目前，与 `pac pcf init` 一起使用的代码组件模板不会使用树摇动，这是 `webpack` 检测导入的未使用的模块并将其删除的过程。如果使用以下命令从 Fluent UI 导入，它将导入并捆绑整个库：

```typescript
import { Button } from '@fluentui/react'
```

为了避免导入和捆绑整个库，您可以使用基于路径的导入，其中使用显式路径导入特定的库组件：

```typescript
import { Button } from '@fluentui/react/lib/Button';
```

使用特定路径可以减少开发和发布版本中的包大小。

#### 优化 React 渲染

使用 React 时，请遵循有关最小化组件渲染的 React 特定最佳实践：

- 仅当绑定属性或框架方面更改需要 UI 反映更改时，才在 `updateView` 方法内调用 `ReactDOM.render` 。您可以使用 `updatedProperties` 来确定发生了什么变化。
- 尽可能使用 `PureComponent` （对于类组件）或 `React.memo` （对于函数组件）以避免不必要的重新渲染。
- 对于大型 React 组件，将 UI 解构为较小的组件以提高性能。
- 避免在渲染函数内使用箭头函数和函数绑定，因为这些做法会为每个渲染创建一个新的回调闭包。

### 检查辅助功能

确保代码组件可访问，以便仅键盘用户和屏幕阅读器用户可以使用它们：

- 提供鼠标/触摸事件的键盘导航替代方案
- 确保设置 `alt` 和 [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)（可访问的富 Internet 应用程序）属性，以便屏幕阅读器读出代码组件接口的准确表示
- 现代浏览器开发人员工具提供了检查可访问性的有用方法

详细信息：[在 Power Apps 中创建可访问的画布应用](https://learn.microsoft.com/en-us/powerapps/maker/canvas-apps/accessible-apps)。

### 始终使用异步网络调用

进行网络调用时，切勿使用同步阻塞请求，因为这会导致应用程序停止响应并导致性能下降。更多信息：[与 HTTP 和 HTTPS 资源异步交互](https://learn.microsoft.com/en-us/powerapps/developer/model-driven-apps/best-practices/business-logic/interact-http-https-resources-asynchronously)。

### 为多个浏览器编写代码

模型驱动应用程序、画布应用程序和门户都支持多个浏览器。请务必仅使用所有现代浏览器都支持的技术，并针对目标受众使用一组具有代表性的浏览器进行测试。

- [限制和配置](https://learn.microsoft.com/en-us/powerapps/maker/canvas-apps/limits-and-config)
- [支持的网络浏览器](https://learn.microsoft.com/en-us/power-platform/admin/supported-web-browsers-and-mobile-devices)
- [office使用的浏览器](https://learn.microsoft.com/en-us/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins)

### 代码组件应规划支持多个客户端和屏幕格式

代码组件可以在多个客户端（模型驱动应用程序、画布应用程序、门户）和屏幕格式（移动设备、平板电脑、Web）中呈现。

- 使用 `trackContainerResize` 允许代码组件响应可用宽度和高度的变化
- 使用 `allocatedHeight` 和 `allocatedWidth` 可以与 `getFormFactor` 结合使用来确定代码组件是否在移动设备、平板电脑或 Web 客户端上运行
- 实施 `setFullScreen` 允许用户扩展以使用空间有限的整个可用屏幕
- 如果代码组件无法在给定的容器大小中提供有意义的体验，则应适当禁用功能并向用户提供反馈

### 始终使用作用域 CSS 规则

当您使用 CSS 为代码组件实现样式时，请确保使用自动生成的应用于组件容器 `DIV` 元素的 CSS 类将 CSS 范围限定为您的组件。如果您的 CSS 作用域为全局，则可能会破坏呈现代码组件的表单或屏幕的现有样式。

例如，如果您的命名空间是 `SampleNamespace` 并且您的代码组件名称是 `LinearInputComponent`，您可以使用以下命令添加自定义 CSS 规则：

```css
.SampleNamespace\.LinearInputComponent rule-name
```

### 避免使用 Web 存储对象

代码组件不应使用 HTML Web 存储对象（例如 `window.localStorage` 和 `window.sessionStorage`）来存储数据。本地存储在用户浏览器或移动客户端上的数据不安全，并且不能保证可靠可用。

## ALM/Azure DevOps/GitHub

请参阅有关 [代码组件应用程序生命周期管理 (ALM)](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/code-components-alm) 的文章，了解使用 ALM/Azure DevOps/GitHub 的代码组件的最佳实践。

## 相关文章

- [什么是代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/custom-controls-overview)
- [画布应用程序的代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/component-framework-for-canvas-apps)
- [创建并构建代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf)
- [学习 Power Apps 组件框架](https://learn.microsoft.com/en-us/training/paths/use-power-apps-component-framework)
- [在 Power Pages 中使用代码组件](https://learn.microsoft.com/en-us/power-apps/maker/portals/component-framework)
