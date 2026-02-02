## 修改代码

对应用程序进行这些必要的更改。

- 安装客户端库
```
npm install @azure/monitor-opentelemetry
```

- 配置应用程序以使用 Azure Monitor
Node.js 应用程序通常有一个入口文件，该文件在 package.json 中列为“main”属性。找到此文件并在其中应用这些更改。
  - 需要顶部的客户端库。 __代码0__
  - 调用设置方法。 __代码0__

> 注意：应尽早调用 setup 方法，但必须在配置环境变量之后调用，因为它需要环境变量中的 App Insights 连接字符串。例如，如果应用程序使用 dotenv 加载环境变量，则应在其之后但在其他任何操作之前调用 setup 方法。
> 注意：由于我们修改了应用程序的代码，因此需要部署才能生效。

## 配置 App Insights 连接字符串

App Insights 资源具有连接字符串。将连接字符串添加为正在运行的应用程序的环境变量。您可以使用 Azure CLI 查询 App Insights 资源的连接字符串。请参阅 [scripts/appinsights.ps1]，了解要执行哪些 Azure CLI 命令来查询连接字符串。

获取连接字符串后，设置此环境变量及其值。

```
"APPLICATIONINSIGHTS_CONNECTION_STRING={your_application_insights_connection_string}"
```

如果应用程序具有 IaC 模板（例如代表其云实例的 Bicep 或 terraform 文件），则应将此环境变量添加到 IaC 模板中以在每个部署中应用。否则，请使用 Azure CLI 手动将环境变量应用到应用程序的云实例。查看要执行哪些 Azure CLI 命令来设置此环境变量。
