## 修改代码

对应用程序进行这些必要的更改。

- 安装客户端库
```
pip install azure-monitor-opentelemetry
```

- 配置应用程序以使用 Azure Monitor
Python 应用程序通过 Python 标准库中的记录器类发送遥测数据。创建一个模块，用于配置和创建可以发送遥测数据的记录器。

```python
import logging
from azure.monitor.opentelemetry import configure_azure_monitor

configure_azure_monitor(
    logger_name="<your_logger_namespace>"
)
logger = logging.getLogger("<your_logger_namespace>")
```

> 注意：由于我们修改了应用程序的代码，因此需要部署才能生效。

## 配置 App Insights 连接字符串

App Insights 资源具有连接字符串。将连接字符串添加为正在运行的应用程序的环境变量。您可以使用 Azure CLI 查询 App Insights 资源的连接字符串。请参阅 [scripts/appinsights.ps1]，了解要执行哪些 Azure CLI 命令来查询连接字符串。

获取连接字符串后，设置此环境变量及其值。

```
"APPLICATIONINSIGHTS_CONNECTION_STRING={your_application_insights_connection_string}"
```

如果应用程序具有 IaC 模板（例如代表其云实例的 Bicep 或 terraform 文件），则应将此环境变量添加到 IaC 模板中以在每个部署中应用。否则，请使用 Azure CLI 手动将环境变量应用到应用程序的云实例。查看要执行哪些 Azure CLI 命令来设置此环境变量。

## 发送数据

创建一个配置为发送遥测数据的记录器。
```python
logger = logging.getLogger("<your_logger_namespace>")
logger.setLevel(logging.INFO)
```

然后通过调用其日志记录方法发送遥测事件。
```python
logger.info("info log")
```
