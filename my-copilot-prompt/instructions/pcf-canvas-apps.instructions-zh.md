---
描述：“画布应用程序实现、安全性和配置的代码组件”
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# Canvas 应用程序的代码组件

专业开发人员可以使用 Power Apps 组件框架创建可在其画布应用程序中使用的代码组件。应用程序开发者可以使用 Power Apps 组件框架通过 [Microsoft Power Platform CLI](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/get-powerapps-cli) 创建、导入代码组件并将其添加到画布应用程序。

> **注意**：某些 API 可能在画布应用程序中不可用。我们建议您检查每个 API 以确定其可用位置。

## 安全考虑

> **警告**：代码组件包含可能不是由 Microsoft 生成的代码，并且在 Power Apps Studio 中呈现时可能会访问安全令牌和数据。将代码组件添加到画布应用程序时，请确保代码组件解决方案来自受信任的来源。播放canvas应用时不存在此漏洞。

### Power Apps Studio 中的安全警告

当您在 Power Apps Studio 中打开包含代码组件的画布应用时，会显示有关潜在不安全代码的警告消息。 Power Apps Studio 环境中的代码组件可以访问安全令牌；因此，只应打开来自可信来源的组件。

**最佳实践：**
- 管理员和系统定制人员应在将所有代码组件导入环境之前检查和验证它们
- 仅在验证后才向制造商提供组件
- 当您使用非托管解决方案导入代码组件或使用 `pac pcf push` 安装代码组件时，会显示 `Default` 发布者

![安全警告](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/canvas-app-safety-warning.png)

## 先决条件

- 需要 Power Apps 许可证。详细信息：[Power Apps 组件框架许可](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview#licensing)
- 需要系统管理员权限才能在环境中启用 Power Apps 组件框架功能

## 启用 Power Apps 组件框架功能

要将代码组件添加到应用程序，您需要在要使用它们的每个环境中启用 Power Apps 组件框架功能。默认情况下，为模型驱动应用启用 Power Apps 组件功能。

### 启用画布应用程序的步骤：

1. 登录 [Power Apps](https://powerapps.microsoft.com/)
2. 选择 **设置** ![设置](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/settings.png)，然后选择 **管理中心**

   ![设置和管理中心](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/select-admin-center-from-settings.png)

3. 在左侧窗格中，选择“**环境**”，选择要启用此功能的环境，然后选择“**设置**”
4. 展开**产品**，然后选择**功能**
5. 从可用功能列表中，打开 **画布应用的 Power Apps 组件框架**，然后选择 **保存**

   ![启用 Power Apps 组件框架](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/enable-pcf-feature.png)

## 实现代码组件

在您的环境中启用 Power Apps 组件框架功能后，您可以开始实现代码组件的逻辑。有关分步教程，请转到[创建您的第一个代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/implementing-controls-using-typescript)。

**建议**：在开始实施之前检查画布应用程序中代码组件的[限制](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/limitations)。

## 将组件添加到画布应用程序

1. 转到 Power Apps Studio
2. 创建新的画布应用程序，或编辑要添加代码组件的现有应用程序

   > **重要**：在继续下一步之前，请确保包含代码组件的解决方案 .zip 文件已[导入](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/import-update-export-solutions) 到 Microsoft Dataverse 中。

3. 在左侧窗格中，选择“**添加 (+)**”，然后选择“**获取更多组件**”

   ![插入组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/insert-code-components-using-get-more-components.png)

4. 选择“**代码**”选项卡，从列表中选择一个组件，然后选择“**导入**”

   ![导入组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/insert-component-add-sample-component.png)

5. 在左侧窗格中，选择 **+**，展开 **代码组件**，然后选择组件以将其添加到应用程序中

   ![添加组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/add-sample-component-from-list.png)

> **注意**：您还可以通过选择“**插入 > 自定义 > 导入组件**”来添加组件。此选项将在未来版本中删除，因此我们建议使用上述流程。

### 组件属性

在“属性”选项卡上，您会注意到显示了代码组件属性。

![默认代码组件属性窗格](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/property-pane-with-parameters.png)

> **注意**：如果您希望属性在默认“属性”选项卡中可用，则可以通过更新代码组件的清单版本来重新导入现有代码组件。与以前一样，这些属性将继续在“高级属性”选项卡上可用。

## 从 Canvas 应用程序中删除代码组件

1. 打开已添加代码组件的应用程序
2. 在左侧窗格中，选择 **树视图**，然后选择已添加代码组件的屏幕
3. 在该组件旁边，选择“**更多 (...)**”，然后选择“**删除**”

   ![删除代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/delete-code-component.png)

4. 保存应用程序以查看更改

## 更新现有代码组件

每当您更新代码组件并希望查看运行时更改时，您都需要更改清单文件中的 `version` 属性。我们建议您在进行更改时更改组件的版本。

> **注意**：仅当应用程序在 Power Apps Studio 中关闭或重新打开时，现有代码组件才会更新。当您重新打开应用程序时，它会要求您更新代码组件。仅删除或添加代码组件回应用程序不会更新组件。首先发布更新的解决方案中的所有自定义项，否则不会显示对代码组件所做的更新。

## 另请参阅

- [Power Apps 组件框架概述](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview)
- [创建您的第一个代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/implementing-controls-using-typescript)
- [学习 Power Apps 组件框架](https://learn.microsoft.com/en-us/training/paths/use-power-apps-component-framework)
