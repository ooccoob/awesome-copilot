---
description: 'Application lifecycle management (ALM) for PCF code components'
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj,sln}'
---

# 代码组件应用程序生命周期管理 (ALM)

ALM 是一个术语，用于描述软件应用程序的生命周期管理，包括开发、维护和治理。详细信息：[使用 Microsoft Power Platform 进行应用程序生命周期管理 (ALM)](https://learn.microsoft.com/en-us/power-platform/alm/overview-alm)。

本文从 Microsoft Dataverse 中的代码组件的角度介绍了处理生命周期管理特定方面的注意事项和策略：

1. 开发和调试 ALM 注意事项
2. 代码组件解决策略
3. 版本控制和部署更新
4. 画布应用程序 ALM 注意事项

## 开发和调试 ALM 注意事项

开发代码组件时，您将遵循以下步骤：

1. 使用 `pac pcf init` 从模板创建代码组件项目 (`pcfproj`)。更多信息：[创建并构建代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf)。
2. 实现代码组件逻辑。更多信息：[组件实现](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/custom-controls-overview#component-implementation)。
3. 使用本地测试工具调试代码组件。更多信息：[调试代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/debugging-custom-controls)。
4. 创建解决方案项目 (`cdsproj`) 并添加代码组件项目作为参考。更多信息：[打包代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/import-custom-controls)。
5. 以发布模式构建代码组件以进行分发和部署。

### Dataverse 的两种部署方法

当您的代码组件准备好在模型驱动应用程序、画布应用程序或门户中进行测试时：

1. **`pac pcf push`**：这会将单个代码组件一次部署到 `--solution-unique-name` 参数指定的解决方案，或者在未指定解决方案时部署到临时 PowerAppsTools 解决方案。

2. **使用 `pac solution init` 和 `msbuild`**：构建引用一个或多个代码组件的 `cdsproj` 解决方案项目。每个代码组件都使用 `pac solution add-reference` 添加到 `cdsproj` 中。解决方案项目可以包含对多个代码组件的引用，而代码组件项目可能只包含单个代码组件。

下图显示了 `cdsproj` 和 `pcfproj` 项目之间的一对多关系：

![cdsproj 和 pcfproj 项目之间的一对多关系](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/code-component-projects.png)

更多信息：[打包代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/import-custom-controls#package-a-code-component)。

## 构建 pcfproj 代码组件项目

构建 `pcfproj` 项目时，生成的 JavaScript 取决于用于构建的命令和 `pcfproj` 文件中的 `PcfBuildMode`。

通常不会将在开发模式下构建的代码组件部署到 Microsoft Dataverse 中，因为它通常太大而无法导入，并且可能会导致运行时性能降低。更多信息：[部署到 Microsoft Dataverse 后进行调试](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/debugging-custom-controls#debugging-after-deploying-into-microsoft-dataverse)。

为了使 `pac pcf push` 生成发布版本，通过在 `OutputPath` 元素下添加新元素，在 `pcfproj` 内设置 `PcfBuildMode` ：

```xml
<PropertyGroup>
   <Name>my-control</Name>
   <ProjectGuid>6aaf0d27-ec8b-471e-9ed4-7b3bbc35bbab</ProjectGuid>
   <OutputPath>$(MSBuildThisFileDirectory)out\controls</OutputPath>
   <PcfBuildMode>production</PcfBuildMode>
</PropertyGroup>
```

### 构建命令

|命令|默认行为 |使用 PcfBuildMode=生产 |
|---------|-----------------|------------------------------|
| npm 开始观看 |永远发展|   |
| pac pcf 推送 |开发构建 |发布版本 |
| npm 运行构建 |开发构建 | __代码0__ |

更多信息：[打包代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/import-custom-controls#package-a-code-component)。

## 构建 .cdsproj 解决方案项目

构建解决方案项目 (`.cdsproj`) 时，您可以选择将输出生成为托管或非托管解决方案。托管解决方案用于部署到不是该解决方案的开发环境的任何环境。这包括测试、UAT、SIT 和生产环境。详细信息：[托管和非托管解决方案](https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions)。

`SolutionPackagerType` 包含在 `pac solution init` 创建的 `.cdsproj` 文件中，但最初被注释掉。取消注释该部分并设置为“托管”、“非托管”或“两者”。

```xml
<!-- Solution Packager overrides, un-comment to use: SolutionPackagerType (Managed, Unmanaged, Both) -->
<PropertyGroup>
   <SolutionPackageType>Managed</SolutionPackageType>
</PropertyGroup>
```

### 构建配置结果

|命令|解决方案包类型 |结果 |
|---------|-------------------|---------|
|微软构建 |管理|托管解决方案内的开发构建 |
| msbuild /p:configuration=发布 |管理|在托管解决方案中发布构建 |
|微软构建|非托管|非托管解决方案内的开发构建 |
| msbuild /p:configuration=发布 |非托管|在非托管解决方案中发布构建 |

更多信息：[打包代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/import-custom-controls#package-a-code-component)。

## 使用代码组件进行源代码控制

开发代码组件时，建议您使用源代码控制提供程序，例如 Azure DevOps 或 GitHub。使用 git 源代码管理提交更改时，`pac pcf init` 模板提供的 `.gitignore` 文件将确保某些文件不会添加到源代码管理中，因为它们要么由 `npm` 恢复，要么作为构建过程的一部分生成：

```
# dependencies
/node_modules

# generated directory
**/generated

# output directory
/out

# msbuild output directories
/bin
/obj
```

由于排除了 `/out` 文件夹，因此生成的 `bundle.js` 文件（和相关资源）将不会添加到源代码管理中。当您的代码组件是手动构建或作为自动构建管道的一部分构建时，将使用最新代码构建 `bundle.js` 以确保包含所有更改。

此外，构建解决方案时，任何关联解决方案 zip 文件都不会提交到源代码管理。相反，输出将作为二进制版本工件发布。

## 将 SolutionPackager 与代码组件结合使用

除了对 `pcfproj` 和 `cdsproj` 进行源代码控制之外，[SolutionPackager](https://learn.microsoft.com/en-us/power-platform/alm/solution-packager-tool) 还可用于将解决方案逐步解包到其各自的部分中，作为一系列可以提交到源代码控制的 XML 文件。这样做的优点是能够以人类可读的格式创建元数据的完整图片，以便您可以使用拉取请求或类似的方式跟踪更改。

> **注意**：此时，SolutionPackager 与使用 `pac solution clone` 的不同之处在于，它可以增量地用于从 Dataverse 解决方案导出更改。

### 示例解决方案结构

使用 `SolutionPackager /action: Extract` 解压包含代码组件的解决方案后，它将类似于：

```
.
├── Controls
│   └── prefix_namespace.ControlName
│       ├── bundle.js *
│       └── css
│          └── ControlName.css *
│       ├── ControlManifest.xml *
│       └── ControlManifest.xml.data.xml
├── Entities
│   └── Contact
│       ├── FormXml
│       │   └── main
│       │       └── {3d60f361-84c5-eb11-bacc-000d3a9d0f1d}.xml
│       ├── Entity.xml
│       └── RibbonDiff.xml
└── Other
    ├── Customizations.xml
    └── Solution.xml
```

在 `Controls` 文件夹下，您可以看到解决方案中包含的每个代码组件都有子文件夹。将此文件夹结构提交到源代码管理时，您将排除上面标有星号 (*) 的文件，因为它们将在为相应组件构建 `pcfproj` 项目时输出。

唯一需要的文件是 `*.data.xml` 文件，因为它们包含描述打包过程所需资源的元数据。

详细信息：[SolutionPackager 命令行参数](https://learn.microsoft.com/en-us/power-platform/alm/solution-packager-tool#solutionpackager-command-line-arguments)。

## 代码组件解决方案策略

使用 Dataverse 解决方案将代码组件部署到下游环境。在解决方案中部署代码组件有两种策略：

### 1. 细分解决方案

使用 `pac solution init` 创建解决方案项目，然后使用 `pac solution add-reference` 添加一个或多个代码组件。然后可以将该解决方案导出并导入到下游环境中，而其他分段解决方案将依赖于代码组件解决方案，因此必须首先将其部署到该环境中。

**采用分段解决方案方法的原因：**

1. **生命周期版本控制** - 您希望在与解决方案其他部分不同的生命周期中开发、部署和版本控制代码组件。这在“融合团队”场景中很常见，其中开发人员构建的代码组件正在被应用程序制造商使用。

2. **共享使用** - 您希望在多个环境之间共享代码组件，因此不希望将代码组件与任何其他解决方案组件耦合。如果您是 ISV 或正在开发供组织不同部门使用的代码组件，则可能会出现这种情况。

### 2. 单一解决方案

在 Dataverse 环境中创建单个解决方案，然后将代码组件与其他解决方案组件（例如表、模型驱动应用程序或画布应用程序）一起添加，而其他解决方案组件又引用这些代码组件。该解决方案可以导出和导入到下游环境中，而无需任何解决方案间的依赖关系。

### 解决方案生命周期概述

![解决策略](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/solution-strategies.png)

详细信息：[使用解决方案打包和分发扩展](https://learn.microsoft.com/en-us/powerapps/developer/data-platform/introduction-solutions)。

## 代码组件和自动构建管道

除了手动构建和部署代码组件解决方案之外，您还可以使用自动构建管道来构建和打包代码组件。

- 如果您使用的是 Azure DevOps，则可以使用 [Microsoft Power Platform Build Tool for Azure DevOps](https://learn.microsoft.com/en-us/power-platform/alm/devops-build-tools)。
- 如果您使用的是 GitHub，则可以使用 [Power Platform GitHub 操作](https://learn.microsoft.com/en-us/power-platform/alm/devops-github-actions)。

### 自动化构建管道的优点

- **省时** - 消除手动任务使构建和打包更快
- **可重复** - 每次执行相同的操作，不依赖于团队成员
- **版本控制一致性** - 相对于以前版本的自动版本控制
- **可维护** - 构建所需的一切都包含在源代码管理中

## 版本控制和部署更新

部署和更新代码组件时，拥有一致的版本控制策略非常重要。常见的版本控制策略是[语义版本控制](https://semver.org/)，其格式为：`MAJOR.MINOR.PATCH`。

### 增加PATCH版本

`ControlManifest.Input.xml` 将代码组件版本存储在控制元素中：

```xml
<control namespace="..." constructor="..." version="1.0.0" display-name-key="..." description-key="..." control-type="...">
```

将更新部署到代码组件时，`ControlManifest.Input.xml` 中的版本必须至少增加其 PATCH（版本的最后部分）才能检测到更改。

**更新版本的命令：**

```bash
# Advance the PATCH version by one
pac pcf version --strategy manifest

# Specify an exact PATCH value (e.g., in automated build pipeline)
pac pcf version --patchversion <PATCH VERSION>
```

### 何时增加 MAJOR 和 MINOR 版本

建议代码组件版本的 MAJOR 和 MINOR 版本与分布式的 Dataverse 解决方案保持同步。

[Dataverse 解决方案有四个部分](https://learn.microsoft.com/en-us/powerapps/maker/data-platform/update-solutions#understanding-version-numbers-for-updates)：`MAJOR.MINOR.BUILD.REVISION`。

|代码组件 |数据宇宙解决方案 |笔记|
|----------------|-------------------|--------|
|专业|专业|使用管道变量或最后提交的值设置 |
|次要|次要|使用管道变量或最后提交的值设置 |
|补丁|建造| $(Build.BuildId) | $(构建.BuildId) |
| ---|修订| $(修订版：r) |

## Canvas 应用程序 ALM 注意事项

在画布应用程序中使用代码组件与在模型驱动应用程序中使用代码组件不同。必须通过在“插入”面板上选择“**获取更多组件**”将代码组件显式添加到应用程序中。将代码组件添加到画布应用程序后，它就会作为内容包含在应用程序定义中。

要在部署代码组件（并且控件版本递增）后更新到新版本的代码组件，应用开发者必须首先在 Power Apps Studio 中打开应用，并在更新代码组件对话框中出现提示时选择 **更新**。然后必须保存并发布该应用程序，以便用户播放该应用程序时使用新版本。

![更新代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/media/upgrade-code-component.png)

如果应用程序未更新或使用 **Skip**，应用程序将继续使用旧版本的代码组件，即使它在环境中不存在，因为它已被新版本覆盖。

由于应用程序包含代码组件的副本，因此可以在不同画布应用程序内部的单个环境中并行运行不同版本的代码组件。但是，您不能在同一应用程序中并行运行不同版本的代码组件。

> **注意**：虽然此时您可以导入画布应用程序，而无需将匹配的代码组件部署到该环境，但建议您始终确保更新应用程序以使用最新版本的代码组件，并且首先将相同版本部署到该环境或作为同一解决方案的一部分。

## 相关文章

- [使用 Microsoft Power Platform 进行应用程序生命周期管理 (ALM)](https://learn.microsoft.com/en-us/power-platform/alm/overview-alm)
- [Power Apps 组件框架 API 参考](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/)
- [创建您的第一个组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/implementing-controls-using-typescript)
- [调试代码组件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/debugging-custom-controls)
