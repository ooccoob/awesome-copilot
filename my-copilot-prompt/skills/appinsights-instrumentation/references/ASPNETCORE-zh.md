## 修改代码

对应用程序进行这些必要的更改。

- 安装客户端库
```
dotnet add package Azure.Monitor.OpenTelemetry.AspNetCore
```

- 配置应用程序以使用 Azure Monitor
ASP.NET Core 应用程序通常具有“构建”应用程序的 Program.cs 文件。找到该文件并应用这些更改。
  - 在顶部添加 `using Azure.Monitor.OpenTelemetry.AspNetCore;`
  - 在调用 `builder.Build()` 之前，添加此行 `builder.Services.AddOpenTelemetry().UseAzureMonitor();`。

> 注意：由于我们修改了应用程序的代码，因此需要部署应用程序才能生效。

## 配置 App Insights 连接字符串

App Insights 资源具有连接字符串。将连接字符串添加为正在运行的应用程序的环境变量。您可以使用 Azure CLI 查询 App Insights 资源的连接字符串。请参阅 [scripts/appinsights.ps1](scripts/appinsights.ps1) 了解要执行哪些 Azure CLI 命令来查询连接字符串。

获取连接字符串后，设置此环境变量及其值。

```
"APPLICATIONINSIGHTS_CONNECTION_STRING={your_application_insights_connection_string}"
```

如果应用程序具有 IaC 模板（例如代表其云实例的 Bicep 或 terraform 文件），则应将此环境变量添加到 IaC 模板中以在每个部署中应用。否则，请使用 Azure CLI 手动将环境变量应用到应用程序的云实例。请参阅 [scripts/appinsights.ps1](scripts/appinsights.ps1) 了解要执行哪些 Azure CLI 命令来设置此环境变量。

> 重要提示：请勿修改 appsettings.json。这是一种已弃用的配置 App Insights 的方法。环境变量是新推荐的方式。
