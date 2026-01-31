# 自动仪表应用程序

使用 Azure 门户自动检测 Azure 应用服务中托管的 Web 应用以实现 App Insights，而无需进行任何代码更改。仅以下类型的应用程序可以自动检测。请参阅[支持的环境和资源提供程序](https://learn.microsoft.com/azure/azure-monitor/app/codeless-overview#supported-environments-languages-and-resource-providers)。

- Azure 应用服务中托管的 ASP.NET Core 应用
- Azure 应用服务中托管的 Node.js 应用

构建一个 URL，将用户带到 Azure 门户中的应用服务应用程序的 Application Insights 边栏选项卡。
```
https://portal.azure.com/#resource/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{app_service_name}/monitoringSettings
```

使用上下文或要求用户获取 subscription_id、resource_group_name 和托管 web 应用程序的 app_service_name。
