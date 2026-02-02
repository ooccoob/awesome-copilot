---
description: 'React controls and platform libraries for PCF components'
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# React 控件和平台库

当您使用 React 和平台库时，您使用的是与 Power Apps 平台相同的基础设施。这意味着您不再需要为每个控件单独打包 React 和 Fluent 库。所有控件共享一个公共库实例和版本，以提供无缝且一致的体验。

## 好处

通过重用现有平台 React 和 Fluent 库，您可以期望：

- **减少控制包大小**
- **优化的解决方案包装**
- **更快的运行时传输、脚本编写和控制渲染**
- **设计和主题与 Power Apps Fluent 设计系统保持一致**

> **注意**：随着 GA 版本的发布，所有现有的虚拟控件将继续发挥作用。但是，应该使用最新的 CLI 版本（>=1.37）重新构建和部署它们，以方便将来平台 React 版本升级。

## 先决条件

与任何组件一样，您必须安装 [Visual Studio Code](https://code.visualstudio.com/Download) 和 [Microsoft Power Platform CLI](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/powerapps-cli#install-microsoft-power-platform-cli)。

> **注意**：如果您已安装适用于 Windows 的 Power Platform CLI，请确保您使用 `pac install latest` 命令运行最新版本。 Power Platform Tools for Visual Studio Code 应自动更新。

## 创建一个反应组件

> **注意**：这些说明要求您之前已经创建过代码组件。如果还没有，请参阅[创建您的第一个组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/implementing-controls-using-typescript)。

`pac pcf init` 命令有一个新的 `--framework` (`-fw`) 参数。将此参数的值设置为 `react`。

### 命令参数

|参数|价值|
|-----------|-------|
| --名称 |反应样本 |
| --命名空间|示例命名空间 |
| --模板|领域 |
| --框架|反应 |
| --run-npm-安装 |真（默认）|

### PowerShell命令

以下 PowerShell 命令使用参数快捷方式并创建一个 React 组件项目并运行 `npm-install`：

```powershell
pac pcf init -n ReactSample -ns SampleNamespace -t field -fw react -npm
```

现在，您可以像往常一样使用 `npm start` 在测试工具中构建和查看控件。

构建控件后，您可以将其打包到解决方案中，并将其用于模型驱动应用程序（包括自定义页面）和画布应用程序（如标准代码组件）。

## 与标准组件的差异

### ControlManifest.Input.xml

[控制元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/control) `control-type` 属性设置为 `virtual` 而不是 `standard`。

> **注意**：更改此值不会将组件从一种类型转换为另一种类型。

在 [resources 元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/resources) 中，找到两个新的 [platform-library element](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/platform-library) 子元素：

```xml
<resources>
  <code path="index.ts" order="1" />
  <platform-library name="React" version="16.14.0" />
  <platform-library name="Fluent" version="9.46.2" />
</resources>
```

> **注意**：有关有效平台库版本的更多信息，请参阅支持的平台库列表。

**建议**：我们建议使用 Fluent 8 和 9 的平台库。如果您不使用 Fluent，则应删除 `name` 属性值为 `Fluent` 的 `platform-library` 元素。

### 索引.ts

用于控件初始化的 [ReactControl.init](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/react-control/init) 方法没有 `div` 参数，因为 React 控件不直接渲染 DOM。相反，[ReactControl.updateView](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/react-control/updateview) 返回一个 ReactElement，其中包含 React 格式的实际控件的详细信息。

### 捆绑包.js

React 和 Fluent 库不包含在包中，因为它们是共享的，因此 bundle.js 的大小较小。

## 样品对照

示例中包含以下控件。它们的功能与标准版本相同，但由于是虚拟控件，因此提供更好的性能。

|样品|描述 |链接 |
|--------|-------------|------|
|选择PickerReact |标准 ChoicesPickerControl 转换为 React Control | ChoicesPickerReact 示例 |
|脸堆反应 | ReactStandardControl 转换为 React Control |脸堆反应 |

## 支持的平台库列表

平台库在构建和运行时均可供使用平台库功能的控件使用。目前平台提供以下版本，为当前支持的最高版本。

|图书馆 |套餐 |构建版本 |运行时版本 |
|---------|---------|---------------|-----------------|
|反应 |反应 | 16.14.0 | 17.0.2（模型）、16.14.0（画布）|
|流利| @flutterui/react | 8.29.0 | 8.29.0 |
|流利| @flutterui/react | 8.121.1 | 8.121.1 |
|流利| @fluidui/react-components | >=9.4.0 <=9.46.2 | 9.68.0 |

> **注意**：应用程序可能会在运行时加载更高兼容版本的平台库，但该版本可能不是可用的最新版本。 Fluent 8 和 Fluent 9 均受支持，但不能在同一清单中同时指定。

## 常见问题解答

### 问：我可以使用平台库将现有标准控件转换为 React 控件吗？

答：不可以。您必须使用新模板创建新控件，然后更新manifest 和index.ts 方法。作为参考，请比较上述标准样品和反应样品。

### 问：我可以将 React 控件和平台库与 Power Pages 一起使用吗？

答：不可以。React 控件和平台库目前仅支持画布和模型驱动应用程序。在 Power Pages 中，React 控件不会根据其他字段的更改进行更新。

## 相关文章

- [什么是代码组件？](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/custom-controls-overview)
- [画布应用程序的代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/component-framework-for-canvas-apps)
- [创建并构建代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf)
- [学习 Power Apps 组件框架](https://learn.microsoft.com/en-us/training/paths/use-power-apps-component-framework)
- [在 Power Pages 中使用代码组件](https://learn.microsoft.com/en-us/power-apps/maker/portals/component-framework)
