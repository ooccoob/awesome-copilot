---
description: 'Code components for model-driven apps implementation and configuration'
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# 模型驱动应用程序的代码组件

Power Apps 组件框架使开发人员能够扩展模型驱动应用程序中的可视化效果。专业开发人员可以使用 [Microsoft Power Platform CLI](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/get-powerapps-cli) 创建、调试、导入代码组件并将其添加到模型驱动应用程序。

## 组件使用

您可以将代码组件添加到：
- 专栏
- 网格
- 子网格

在模型驱动的应用程序中。

> **重要**：默认情况下，为模型驱动应用程序启用 Power Apps 组件框架。请参阅[画布应用的代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/component-framework-for-canvas-apps) 了解如何为画布应用启用 Power Apps 组件框架。

## 实现代码组件

在开始创建代码组件之前，请确保您已安装使用 Power Apps 组件框架开发组件所需的所有[先决条件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf#prerequisites)。

[创建您的第一个代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/implementing-controls-using-typescript) 一文演示了创建代码组件的分步过程。

## 将代码组件添加到模型驱动应用程序

要将代码组件添加到模型驱动应用程序中的列或表，请参阅[将代码组件添加到模型驱动应用程序](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/add-custom-controls-to-a-field-or-entity)。

### 示例

**线性滑块控制：**

![添加线性滑块控件](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/media/add-slider.png)

**数据集网格组件：**

![数据集网格组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/add-dataset-component.png)

## 更新现有代码组件

每当您更新代码组件并希望在运行时查看更改时，您需要更改清单文件中的版本属性。 

**最佳实践**：建议您在进行更改时始终更改组件的版本。

## 另请参阅

- [Power Apps 组件框架概述](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)
- [创建您的第一个代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/implementing-controls-using-typescript)
- [学习 Power Apps 组件框架](https://learn.microsoft.com/en-us/training/paths/use-power-apps-component-framework)
