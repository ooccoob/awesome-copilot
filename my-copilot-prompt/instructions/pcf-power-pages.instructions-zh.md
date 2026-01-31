---
描述：“在 Power Pages 站点中使用代码组件”
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# 在高级页面中使用代码组件

Power Pages 现在支持为使用 Power Apps 组件框架创建的模型驱动应用程序构建的控件。要在 Power Pages 站点网页中使用代码组件：

![使用组件框架创建代码组件，然后将代码组件添加到模型驱动应用表单中，并在门户基本表单内配置代码组件字段](https://learn.microsoft.com/en-us/power-pages/configure/media/component-framework/steps.png)

完成这些步骤后，用户可以使用具有相应 [form](https://learn.microsoft.com/en-us/power-pages/getting-started/add-form) 组件的网页与代码组件交互。

## 先决条件

- 您需要系统管理员权限才能在环境中启用代码组件功能
- 您的 Power Pages 网站版本需要为 [9.3.3.x](https://learn.microsoft.com/en-us/power-apps/maker/portals/versions/version-9.3.3.x) 或更高版本
- 您的起始站点包需要为 [9.2.2103.x](https://learn.microsoft.com/en-us/power-apps/maker/portals/versions/package-version-9.2.2103) 或更高版本

## 创建并打包代码组件

要了解如何在 Power Apps 组件框架中创建和打包代码组件，请转到[创建您的第一个组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/implementing-controls-using-typescript)。

### 支持的字段类型和格式

Power Pages 支持使用代码组件的受限字段类型和格式。下表列出了所有支持的字段数据类型和格式：

**支持的类型：**
- 货币
- 日期和时间.日期和时间
- 日期和时间.DateOnly
- 十进制
- 枚举
- 浮点数
- 多个
- 选项集
- 单行电子邮件
- 单线电话
- 单行文本
- 单行文本区域
- 单线行情指示器
- 单行.URL
- 两种选择
- 整体

有关详细信息，请参阅[属性列表和说明](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/property#remarks)。

### 高级页面中不支持的代码组件

不支持以下代码组件 API：
- [设备.captureAudio](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/device/captureaudio)
- [设备.captureImage](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/device/captureimage)
- [设备.捕获视频](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/device/capturevideo)
- [Device.getBarcodeValue](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/device/getbarcodevalue)
- [设备.getCurrentPosition](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/device/getcurrentposition)
- [设备.pickFile](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/device/pickfile)
- [实用程序](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/utility)

**附加限制：**
- [uses-feature](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/uses-feature) 元素不得设置为 true
- Power Apps 组件框架 [不支持值元素](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/manifest-schema-reference/property#value-elements-that-are-not-supported)
- 不支持绑定到表单中多个字段的 Power Apps 组件框架 (PCF) 控件

## 将代码组件添加到模型驱动应用程序中的字段

要了解如何将代码组件添加到模型驱动应用程序中的字段，请转到[将代码组件添加到字段](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/add-custom-controls-to-a-field-or-entity#add-a-code-component-to-a-column)。

> **重要**：Power Pages 的代码组件可用于使用 **Web** 客户端选项的 Web 浏览器。

### 添加使用数据工作区

您还可以使用 [数据工作区](https://learn.microsoft.com/en-us/power-pages/configure/data-workspace-forms) 将代码组件添加到表单。

1. 在数据工作区表单设计器中编辑 Dataverse 表单时，选择一个字段
2. 选择 **+ 组件** 并为该字段选择适当的组件

   ![将组件添加到表单](https://learn.microsoft.com/en-us/power-pages/configure/media/component-framework/add-component-to-form.png)

3. 选择**保存**和**发布表单**

## 为代码组件配置 Power Pages 站点

将代码组件添加到模型驱动应用程序中的字段后，您可以将 Power Pages 配置为在表单上使用代码组件。

启用代码组件有两种方法：

### 在 Design Studio 中启用代码组件

要使用设计工作室在表单上启用代码组件：

1. [将表单添加到页面](https://learn.microsoft.com/en-us/power-pages/getting-started/add-form) 后，选择添加代码组件的字段，然后选择 **编辑字段**
2. 选择 **启用自定义组件** 字段

   ![在设计工作室中启用自定义组件](https://learn.microsoft.com/en-us/power-pages/configure/media/component-framework/enable-code-component.png)

3. 当您预览站点时，您应该会看到自定义组件已启用

### 在门户管理应用程序中启用代码组件

要使用门户管理应用程序将代码组件添加到基本表单：

1. 打开[门户管理](https://learn.microsoft.com/en-us/power-pages/configure/portal-management-app)应用程序
2. 在左侧窗格中，选择**基本表单**
3. 选择要添加代码组件的表单
4. 选择**相关**
5. 选择**基本表单元数据**
6. 选择**新基本表单元数据**
7. 选择**类型**作为**属性**
8. 选择**属性逻辑名称**
9. 输入**标签**
10. 对于 **控件样式**，选择 **代码组件**
11. 保存并关闭表单

## 使用 Portal Web API 的代码组件

可以构建代码组件并将其添加到可以使用 [门户 Web API](https://learn.microsoft.com/en-us/power-pages/configure/web-api-overview) 执行创建、检索、更新和删除操作的网页。在开发门户解决方案时，此功能允许更多的自定义选项。有关详细信息，请参阅[实现示例门户 Web API 组件](https://learn.microsoft.com/en-us/power-pages/configure/implement-webapi-component)。

## 下一步

[教程：在门户中使用代码组件](https://learn.microsoft.com/en-us/power-pages/configure/component-framework-tutorial)

## 另请参阅

- [Power Apps 组件框架概述](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)
- [创建您的第一个组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/implementing-controls-using-typescript)
- [将代码组件添加到模型驱动应用程序中的列或表](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/add-custom-controls-to-a-field-or-entity)
