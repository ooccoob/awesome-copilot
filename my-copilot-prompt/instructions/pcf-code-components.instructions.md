---
description: 'Understanding code components structure and implementation'
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# 代码组件

代码组件是一种解决方案组件，可以包含在解决方案文件中并导入到不同的环境中。它们可以添加到模型驱动应用程序和画布应用程序中。

## 三大核心要素

代码组件由三个元素组成：

1. **清单**
2. **组件实现**
3. **资源**

> **注意**：对于模型驱动应用程序和画布应用程序，使用 Power Apps 组件框架的代码组件的定义和实现是相同的。唯一的区别是配置部分。

## 清单

清单是定义组件的 `ControlManifest.Input.xml` 元数据文件。它是一个 XML 文档，描述：

- 组件名称
- 可以配置的数据类型，可以是 `field` 或 `dataset`
- 添加组件时可以在应用程序中配置的任何属性
- 组件需要的资源文件列表

### 明确目的

当用户配置代码组件时，清单文件中的数据会过滤可用组件，以便只有上下文的有效组件可用于配置。清单文件中定义的属性将呈现为配置列，以便用户可以指定值。然后，这些属性值在运行时可供组件使用。

更多信息：[清单架构参考](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/)

## 组件实现

代码组件是使用 TypeScript 实现的。每个代码组件必须包含一个实现代码组件接口中描述的方法的对象。 [Power Platform CLI](https://learn.microsoft.com/en-us/power-platform/developer/cli/introduction) 使用 `pac pcf init` 命令自动生成带有存根实现的 `index.ts` 文件。

### 所需方法

组件对象实现这些生命周期方法：

- **init** （必需）- 页面加载时调用
- **updateView**（必需）- 当应用程序数据更改时调用
- **getOutputs** （可选）- 当用户更改数据时返回值
- **destroy**（必需）- 页面关闭时调用

### 组件生命周期

#### 页面加载

加载页面时，应用程序使用清单中的数据创建一个对象：

```typescript
var obj = new <"namespace on manifest">.<"constructor on manifest">();
```

示例：
```typescript
var controlObj = new SampleNameSpace.LinearInputComponent();
```

然后页面初始化该组件：

```typescript
controlObj.init(context, notifyOutputChanged, state, container);
```

**初始化参数：**

|参数|描述 |
|-----------|-------------|
| __代码0__ |包含有关如何配置组件和所有参数的所有信息。通过 `context.parameters.<property name from manifest>` 访问输入属性。包括 Power Apps 组件框架 API。 |
| __代码0__ |每当组件有准备异步检索的新输出时，都会向框架发出警报。 |
| __代码0__ |如果使用 `setControlState` 方法显式存储，则包含来自上一页加载的组件数据。 |
| __代码0__ |开发人员可以向其附加 UI 的 HTML 元素的 HTML div 元素。 |

#### 用户更改数据

当用户与组件交互以更改数据时，调用在 `init` 方法中传递的 `notifyOutputChanged` 方法。平台通过调用 `getOutputs` 方法进行响应，该方法返回包含用户所做更改的值。对于 `field` 组件，这通常是新值。

#### 应用程序更改数据

如果平台更改了数据，它会调用组件的 `updateView` 方法并将新的上下文对象作为参数传递。应实现此方法来更新组件中显示的值。

#### 页面关闭

当用户离开页面时，代码组件将失去作用域，并且为对象分配的所有内存都将被清除。但是，某些方法（如事件处理程序）可能会保留并消耗基于浏览器实现的内存。

**最佳实践：**
- 实现 `setControlState` 方法以在同一会话中下次存储信息
- 实现 `destroy` 方法以在页面关闭时删除清理代码，例如事件处理程序

## 资源

清单文件中的资源节点是指组件实现其可视化所需的资源。每个代码组件必须有一个资源文件来构建其可视化。该工具生成的 `index.ts` 文件是 `code` 资源。必须至少有 1 个代码资源。

### 其他资源

您可以在清单中定义其他资源文件：

- CSS 文件
- 图片网络资源
- 用于本地化的 Resx Web 资源

更多信息：[资源元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/resources)

## 相关资源

- [创建并构建代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf)
- [了解如何使用解决方案打包和分发扩展](https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)
