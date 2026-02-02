---
description: 'How to use and run PCF sample components from the PowerApps-Samples repository'
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# 如何使用示例组件

本部分列出的所有示例组件都可以从 [github.com/microsoft/PowerApps-Samples/tree/master/component-framework](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework) 下载，以便您可以在模型驱动或画布应用程序中试用它们。

本节下的各个示例组件主题为您提供示例组件、其视觉外观以及完整示例组件的链接的概述。

## 在尝试示例组件之前

要尝试示例组件，您必须首先：

- [下载](https://docs.github.com/repositories/working-with-files/using-files/downloading-source-code-archives#downloading-source-code-archives-from-the-repository-view) 或[克隆](https://docs.github.com/repositories/creating-and-managing-repositories/cloning-a-repository) 此存储库 [github.com/microsoft/PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples)。
- 安装 [安装适用于 Windows 的 Power Platform CLI](https://learn.microsoft.com/en-us/power-platform/developer/cli/introduction#install-power-platform-cli-for-windows)。

## 尝试示例组件

按照 [README.md](https://github.com/microsoft/PowerApps-Samples/blob/master/component-framework/README.md) 中的步骤生成包含控件的解决方案，以便您可以在模型驱动或画布应用程序中导入并尝试示例组件。

## 如何运行示例组件

使用以下步骤在模型驱动或画布应用程序中导入并试用示例组件。

### 分步过程

1. **下载或克隆存储库**
   - [下载](https://docs.github.com/repositories/working-with-files/using-files/downloading-source-code-archives#downloading-source-code-archives-from-the-repository-view) 或[克隆](https://docs.github.com/repositories/creating-and-managing-repositories/cloning-a-repository) [github.com/microsoft/PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples)。

2. **打开开发者命令提示符**
   - 打开 [Visual Studio 开发人员命令提示符](https://learn.microsoft.com/visualstudio/ide/reference/command-prompt-powershell) 并导航到 `component-framework` 文件夹。
   - 在 Windows 上，您可以在“开始”中键入 `developer command prompt` 以打开开发人员命令提示符。

3. **安装依赖项**
   - 导航到您要尝试的组件，例如 `IncrementControl`，然后运行：
   ```bash
   npm install
   ```

4. **恢复项目**
   - 命令完成后，运行：
   ```bash
   msbuild /t:restore
   ```

5. **创建解决方案文件夹**
   - 在示例组件文件夹中创建一个新文件夹：
   ```bash
   mkdir IncrementControlSolution
   ```

6. **导航到解决方案文件夹**
   ```bash
   cd IncrementControlSolution
   ```

7. **初始化解决方案**
   - 在您创建的文件夹中，运行 `pac solution init` 命令：
   ```bash
   pac solution init --publisher-name powerapps_samples --publisher-prefix sample
   ```
   > **注意**：此命令在文件夹中创建一个名为 `IncrementControlSolution.cdsproj` 的新文件。

8. **添加组件参考**
   - 运行 `pac solution add-reference` 命令，并将 `path` 设置为 `.pcfproj` 文件的位置：
   ```bash
   pac solution add-reference --path ../../IncrementControl
   ```
   或
   ```bash
   pac solution add-reference --path ../../IncrementControl/IncrementControl.pcfproj
   ```
   > **重要**：引用包含要添加的控件的 `.pcfproj` 文件的文件夹。

9. **构建解决方案**
   - 要从解决方案项目生成 zip 文件，请运行以下三个命令：
   ```bash
   msbuild /t:restore
   msbuild /t:rebuild /restore /p:Configuration=Release
   msbuild
   ```
   - 生成的解决方案 zip 文件将位于 `IncrementControlSolution\bin\debug` 文件夹中。

10. **导入解决方案**
    - 现在您已经有了 zip 文件，您有两个选择：
      - 使用 [make.powerapps.com](https://make.powerapps.com/) 手动将解决方案导入到您的环境中。
      - 或者，要使用 Power Apps CLI 命令导入解决方案，请参阅[连接到您的环境](https://learn.microsoft.com/powerapps/developer/component-framework/import-custom-controls#connecting-to-your-environment) 和 [部署](https://learn.microsoft.com/powerapps/developer/component-framework/import-custom-controls#deploying-code-components) 部分。

11. **向应用程序添加组件**
    - 最后，要将代码组件添加到模型驱动和画布应用程序，请参阅：
      - [将组件添加到模型驱动应用程序](https://learn.microsoft.com/powerapps/developer/component-framework/add-custom-controls-to-a-field-or-entity)
      - [将组件添加到画布应用程序](https://learn.microsoft.com/powerapps/developer/component-framework/component-framework-for-canvas-apps#add-components-to-a-canvas-app)

## 可用的样品组件

该存储库包含许多示例组件，包括：

- AngularJSFlipControl
- 画布网格控件
- 选择选择器控件
- ChoicesPickerReactControl
- 代码解释器控件
- 控制状态API
- 数据集网格
- 设备API控制
- Facepile反应控制
- FluentThemingAPI 控件
- 格式化API控制
- IFrame控件
- 图片上传控件
- 增量控制
- 线性输入控制
- 本地化API控制
- 查找简单控件
- 地图控制
- 模型驱动网格控制
- 多选选项集控件
- 导航API控制
- 对象输出控制
- PowerAppsGridCustomizerControl
- 属性设置表控件
- React标准控件
- 表格控件
- 表格表格
- WebAPI控制

每个示例都演示了 Power Apps 组件框架的不同方面，并且可以作为您自己的组件的学习资源或起点。
