---
描述：“在 PCF 组件中使用依赖库”
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# 依赖库（预览）

[本主题是预发布文档，可能会发生变化。]

使用模型驱动应用程序，您可以重用另一个组件中包含的预构建库，该组件作为多个组件的依赖项加载。

在多个控件中拥有预构建库的副本是不可取的。通过减少使用该库的所有组件的加载时间，重用现有库可以提高性能，尤其是当库很大时。库重用还有助于减少构建过程中的维护开销。

## 之前和之后

**之前**：每个 PCF 组件中包含的自定义库文件
![显示每个 pcf 组件中包含的自定义库文件的图表](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/dependent-library-before-example.png)

**之后**：从库控件调用共享函数的组件
![显示组件从库控件调用共享函数的图](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/dependent-library-after-example.png)

## 实施步骤

要使用依赖库，您需要：

1. 创建一个包含该库的**库组件**。该组件可以提供一些功能或仅作为库的容器。
2. 配置另一个组件以依赖于库组件加载的库。

默认情况下，库会在依赖组件加载时加载，但您可以将其配置为按需加载。

这样您就可以在库控件中独立维护库，并且依赖的控件不需要与它们捆绑库的副本。

## 它是如何运作的

您需要将配置数据添加到组件项目中，以便构建过程按照您想要的方式部署您的库。通过添加或编辑以下文件来设置此配置数据：

- **featureconfig.json**
- **webpack.config.js**
- 编辑清单架构以**注册依赖项**

### 功能配置.json

添加此文件可覆盖组件的默认功能标志，而无需修改 `node_modules` 文件夹中生成的文件。

**功能标志：**

|旗帜|描述 |
|------|-------------|
| __代码0__ |使组件能够使用库资源。 |
| __代码0__ |使组件能够使用自定义 Web 包。必须为定义库资源的组件启用此功能。 |

默认情况下，这些值为 `off`。将它们设置为 `on` 以覆盖默认值。

**示例1：**
```json
{ 
  "pcfAllowCustomWebpack": "on" 
} 
```

**示例2：**
```json
{ 
   "pcfResourceDependency": "on",
   "pcfAllowCustomWebpack": "off" 
} 
```

### webpack.config.js

组件的构建过程使用 [Webpack](https://webpack.js.org/) 将代码和依赖项捆绑到可部署的资产中。要从该捆绑中排除您的库，请将 `webpack.config.js` 文件添加到项目根文件夹中，并将库的别名指定为 `externals`。 [了解有关 Webpack 外部配置选项的更多信息](https://webpack.js.org/configuration/externals/)

当库别名为 `myLib` 时，此文件可能如下所示：

```javascript
/* eslint-disable */ 
"use strict"; 

module.exports = { 
  externals: { 
    "myLib": "myLib" 
  }, 
}  
```

### 注册依赖项

使用清单架构的 [资源](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/resources) 内的 [依赖项元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/dependency)。

```xml
<resources>
  <dependency
    type="control"
    name="samples_SampleNS.SampleStubLibraryPCF"
    order="1"
  />
  <code path="index.ts" order="2" />
</resources>
```

### 依赖项作为组件的按需加载

您可以按需加载依赖库，而不是在组件加载时加载依赖库。按需加载为更复杂的控件提供了灵活性，仅在需要时加载依赖项，特别是当依赖库很大时。

![显示使用库中的函数的图，其中库是按需加载的](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/dependent-library-on-demand-load.png)

要启用按需加载，您需要：

**步骤 1**：将这些 [platform-action 元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/platform-action)、[feature-usage 元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/feature-usage) 和 [uses-feature 元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/uses-feature) 子元素添加到 [control 元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/control)：

```xml
<platform-action action-type="afterPageLoad" />
<feature-usage>
   <uses-feature name="Utility"
      required="true" />
</feature-usage>
```

**步骤 2**：将 [依赖元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/dependency) 的 `load-type` 属性设置为 `onDemand`。

```xml
<dependency type="control"
      name="samples_SampleNamespace.StubLibrary"
      load-type="onDemand" />
```

## 下一步

尝试指导您创建依赖库的教程：

[教程：在组件中使用依赖库](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/tutorial-use-dependent-libraries)
