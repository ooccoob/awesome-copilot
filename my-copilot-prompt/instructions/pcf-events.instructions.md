---
description: 'Define and handle custom events in PCF components'
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# 定义事件（预览）

[本主题是预发布文档，可能会发生变化。]

使用 Power Apps 组件框架构建自定义组件时的一个常见要求是能够对控件内生成的事件做出反应。这些事件可以通过用户交互或通过代码以编程方式调用。例如，应用程序可以具有允许用户构建产品包的代码组件。该组件还可以引发一个事件，该事件可以在应用程序的另一个区域中显示产品信息。

## 组件数据流

代码组件的常见数据流是从托管应用程序作为输入流入控件的数据以及从控件流出到托管窗体或页面的更新数据。下图显示了典型 PCF 组件的数据流的标准模式：

![说明从代码组件到绑定字段的数据更新触发了OnChange事件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/component-events-onchange-example.png)

从代码组件到绑定字段的数据更新会触发 `OnChange` 事件。对于大多数组件场景来说，这已经足够了，制作者只需添加一个处理程序来触发后续操作。但是，更复杂的控件可能需要引发非字段更新的事件。事件机制允许代码组件定义具有单独事件处理程序的事件。

## 使用事件

PCF中的事件机制基于JavaScript中的标准事件模型。组件可以在清单文件中定义事件并在代码中引发这些事件。托管应用程序可以侦听这些事件并对它们做出反应。

### 在清单中定义事件

该组件使用清单文件中的[事件元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/event) 定义事件。该数据允许相应的托管应用程序以不同的方式对事件做出反应。

```xml
<property
  name="sampleProperty"
  display-name-key="Property_Display_Key"
  description-key="Property_Desc_Key"
  of-type="SingleLine.Text"
  usage="bound"
  required="true"
/>
<event
  name="customEvent1"
  display-name-key="customEvent1"
  description-key="customEvent1"
/>
<event
  name="customEvent2"
  display-name-key="customEvent2"
  description-key="customEvent2"
/>
```

### 画布应用程序事件处理

Canvas 应用程序使用 Power Fx 表达式对事件作出反应：

![在画布应用程序设计器中显示自定义事件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/custom-events-in-canvas-designer.png)

### 模型驱动应用程序事件处理

模型驱动应用程序使用 [addEventHandler 方法](https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/controls/addeventhandler) 将事件处理程序与组件的自定义事件关联。

```javascript
const controlName1 = "cr116_personid";

this.onLoad = function (executionContext) {
  const formContext = executionContext.getFormContext();

  const sampleControl1 = formContext.getControl(controlName1);
  sampleControl1.addEventHandler("customEvent1", this.onSampleControl1CustomEvent1);
  sampleControl1.addEventHandler("customEvent2", this.onSampleControl1CustomEvent2);
}
```

> **注意**：这些事件对于应用程序中代码组件的每个实例单独发生。

## 为模型驱动应用程序定义事件

对于模型驱动的应用程序，您可以通过事件传递有效负载，以允许更复杂的场景。例如，在下图中，组件在事件中传递回调函数，允许脚本处理回调到组件。

![在此示例中，组件在事件中传递回调函数，允许脚本处理回调到组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/passing-payload-in-events.png)

```javascript
this.onSampleControl1CustomEvent1 = function (params) {
   //alert(`SampleControl1 Custom Event 1: ${params}`);
   alert(`SampleControl1 Custom Event 1`);
}.bind(this);

this.onSampleControl2CustomEvent2 = function (params) {
  alert(`SampleControl2 Custom Event 2: ${params.message}`);
  // prevent the default action for the event
  params.callBackFunction();
}
```

## 为画布应用程序定义事件

制作者使用属性窗格中 PCF 控件上的 Power Fx 配置事件。

## 调用事件

请参阅[事件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/events) 中如何调用事件。

## 下一步

[教程：在组件中定义自定义事件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/tutorial-define-event)
