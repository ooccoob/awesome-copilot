---
name: appinsights-instrumentation
description: 'Instrument a webapp to send useful telemetry data to Azure App Insights'
---

# AppInsights 仪器

此技能可以将 Web 应用程序的遥测数据发送到 Azure App Insights，以便更好地观察应用程序的运行状况。

## 何时使用该技能

当用户想要为其 Web 应用程序启用遥测时，请使用此技能。

## 先决条件

工作区中的应用程序必须是以下类型之一

- Azure 中托管的 ASP.NET Core 应用程序
- Azure 中托管的 Node.js 应用

## 指南

### 收集上下文信息

找出用户尝试添加遥测支持的应用程序的（编程语言、应用程序框架、托管）元组。这决定了如何对应用程序进行检测。阅读源代码以做出有根据的猜测。对于任何您不知道的事情都要与用户确认。您必须始终询问用户应用程序的托管位置（例如，在个人计算机上、在 Azure 应用服务代码中、在 Azure 应用服务容器中、在 Azure 容器应用中等）。 

### 如果可能，首选自动仪器

如果应用是 Azure 应用服务中托管的 C# ASP.NET Core 应用，请使用 [AUTO 指南](references/AUTO-zh.md) 帮助用户自动检测应用。

### 手动仪表

通过创建 AppInsights 资源并更新应用程序的代码来手动检测应用程序。 

#### 创建 AppInsights 资源

使用以下适合环境的选项之一。

- 将 AppInsights 添加到现有的 Bicep 模板。请参阅 [examples/appinsights.bicep](examples/appinsights.bicep) 了解要添加的内容。如果工作区中存在现有的 Bicep 模板文件，这是最佳选择。
- 使用 Azure CLI。请参阅 [scripts/appinsights.ps1](scripts/appinsights.ps1) 了解要执行哪些 Azure CLI 命令来创建 App Insights 资源。

无论选择哪个选项，都建议用户在有意义的资源组中创建 App Insights 资源，以便更轻松地管理资源。一个好的候选者是包含 Azure 中托管应用程序的资源的同一资源组。

#### 修改应用代码

- 如果应用是 ASP.NET Core 应用，请参阅 [ASPNETCORE 指南](references/ASPNETCORE-zh.md) 了解如何修改 C# 代码。
- 如果应用程序是 Node.js 应用程序，请参阅 [NODEJS 指南](references/NODEJS-zh.md) 了解如何修改 JavaScript/TypeScript 代码。
- 如果应用程序是Python应用程序，请参阅[PYTHON指南](references/PYTHON-zh.md)了解如何修改Python代码。
