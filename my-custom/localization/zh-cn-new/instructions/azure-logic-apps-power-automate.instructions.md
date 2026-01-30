---
description: 'Azure Logic Apps 和 Power Automate 工作流开发指南，包含工作流定义语言（WDL）、集成模式和企业自动化的最佳实践'
applyTo: "**/*.json,**/*.logicapp.json,**/workflow.json,**/*-definition.json,**/*.flow.json"
---

# Azure Logic Apps 和 Power Automate 指导原则

## 概述

这些指导原则将帮助您使用基于 JSON 的工作流定义语言（WDL）编写高质量的 Azure Logic Apps 和 Microsoft Power Automate 工作流定义。Azure Logic Apps 是一个基于云的集成平台即服务（iPaaS），提供 1,400+ 个连接器来简化跨服务和协议的集成。遵循这些指导原则来创建健壮、高效且可维护的云工作流自动化解决方案。

## 工作流定义语言结构

在处理 Logic Apps 或 Power Automate 流 JSON 文件时，确保您的工作流遵循此标准结构：

```json
{
  "definition": {
    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
    "actions": { },
    "contentVersion": "1.0.0.0",
    "outputs": { },
    "parameters": { },
    "staticResults": { },
    "triggers": { }
  },
  "parameters": { }
}
```

## Azure Logic Apps 和 Power Automate 开发最佳实践

### 1. 触发器

- **根据您的场景使用适当的触发器类型**：
  - **请求触发器**：用于类似同步 API 的工作流
  - **重复触发器**：用于计划操作
  - **基于事件的触发器**：用于反应模式（Service Bus、Event Grid 等）
- **配置适当的触发器设置**：
  - 设置合理的超时时间段
  - 为高容量数据源使用分页设置
  - 实现适当的身份验证

```json
"triggers": {
  "manual": {
    "type": "Request",
    "kind": "Http",
    "inputs": {
      "schema": {
        "type": "object",
        "properties": {
          "requestParameter": {
            "type": "string"
          }
        }
      }
    }
  }
}
```

### 2. 操作

- **描述性地命名操作**以指示其目的
- **使用范围组织复杂工作流**进行逻辑分组
- **为不同操作使用适当的操作类型**：
  - HTTP 操作用于 API 调用
  - 连接器操作用于内置集成
  - 数据操作操作用于转换

```json
"actions": {
  "Get_Customer_Data": {
    "type": "Http",
    "inputs": {
      "method": "GET",
      "uri": "https://api.example.com/customers/@{triggerBody()?['customerId']}",
      "headers": {
        "Content-Type": "application/json"
      }
    },
    "runAfter": {}
  }
}
```

### 3. 错误处理和可靠性

- **实现健壮的错误处理**：
  - 使用 "runAfter" 配置处理失败
  - 为瞬态错误配置重试策略
  - 使用带有 "runAfter" 条件的范围进行错误分支
- **为关键操作实现回退机制**
- **为外部服务调用添加超时**
- **使用 runAfter 条件**进行复杂错误处理场景

```json
"actions": {
  "HTTP_Action": {
    "type": "Http",
    "inputs": { },
    "retryPolicy": {
      "type": "fixed",
      "count": 3,
      "interval": "PT20S",
      "minimumInterval": "PT5S",
      "maximumInterval": "PT1H"
    }
  },
  "Handle_Success": {
    "type": "Scope",
    "actions": { },
    "runAfter": {
      "HTTP_Action": ["Succeeded"]
    }
  },
  "Handle_Failure": {
    "type": "Scope",
    "actions": {
      "Log_Error": {
        "type": "ApiConnection",
        "inputs": {
          "host": {
            "connection": {
              "name": "@parameters('$connections')['loganalytics']['connectionId']"
            }
          },
          "method": "post",
          "body": {
            "LogType": "WorkflowError",
            "ErrorDetails": "@{actions('HTTP_Action').outputs.body}",
            "StatusCode": "@{actions('HTTP_Action').outputs.statusCode}"
          }
        }
      },
      "Send_Notification": {
        "type": "ApiConnection",
        "inputs": {
          "host": {
            "connection": {
              "name": "@parameters('$connections')['office365']['connectionId']"
            }
          },
          "method": "post",
          "path": "/v2/Mail",
          "body": {
            "To": "support@contoso.com",
            "Subject": "Workflow Error - HTTP Call Failed",
            "Body": "<p>The HTTP call failed with status code: @{actions('HTTP_Action').outputs.statusCode}</p>"
          }
        },
        "runAfter": {
          "Log_Error": ["Succeeded"]
        }
      }
    },
    "runAfter": {
      "HTTP_Action": ["Failed", "TimedOut"]
    }
  }
}
```

### 4. 表达式和函数

- **使用内置表达式函数**转换数据
- **保持表达式简洁易读**
- **用注释记录复杂表达式**

常用表达式模式：
- 字符串操作：`concat()`、`replace()`、`substring()`
- 集合操作：`filter()`、`map()`、`select()`
- 条件逻辑：`if()`、`and()`、`or()`、`equals()`
- 日期/时间操作：`formatDateTime()`、`addDays()`
- JSON 处理：`json()`、`array()`、`createArray()`

```json
"Set_Variable": {
  "type": "SetVariable",
  "inputs": {
    "name": "formattedData",
    "value": "@{map(body('Parse_JSON'), item => {
      return {
        id: item.id,
        name: toUpper(item.name),
        date: formatDateTime(item.timestamp, 'yyyy-MM-dd')
      }
    })}"
  }
}
```

#### 在 Power Automate 条件中使用表达式

Power Automate 支持在条件中使用高级表达式来检查多个值。在处理复杂逻辑条件时，使用以下模式：

- 对于比较单个值：使用基本条件设计器界面
- 对于多个条件：在高级模式中使用高级表达式

Power Automate 中条件常用的逻辑表达式函数：

| 表达式 | 描述 | 示例 |
|------------|-------------|---------|
| `and` | 如果两个参数都为真则返回真 | `@and(equals(item()?['Status'], 'completed'), equals(item()?['Assigned'], 'John'))` |
| `or` | 如果任一参数为真则返回真 | `@or(equals(item()?['Status'], 'completed'), equals(item()?['Status'], 'unnecessary'))` |
| `equals` | 检查值是否相等 | `@equals(item()?['Status'], 'blocked')` |
| `greater` | 检查第一个值是否大于第二个 | `@greater(item()?['Due'], item()?['Paid'])` |
| `less` | 检查第一个值是否小于第二个 | `@less(item()?['dueDate'], addDays(utcNow(),1))` |
| `empty` | 检查对象、数组或字符串是否为空 | `@empty(item()?['Status'])` |
| `not` | 返回布尔值的相反值 | `@not(contains(item()?['Status'], 'Failed'))` |

示例：检查状态是否为 "completed" 或 "unnecessary"：
```
@or(equals(item()?['Status'], 'completed'), equals(item()?['Status'], 'unnecessary'))
```

示例：检查状态是否为 "blocked" 且分配给特定人员：
```
@and(equals(item()?['Status'], 'blocked'), equals(item()?['Assigned'], 'John Wonder'))
```

示例：检查付款是否逾期且未完成：
```
@and(greater(item()?['Due'], item()?['Paid']), less(item()?['dueDate'], utcNow()))
```

**注意：** 在 Power Automate 中，在表达式中访问前面步骤的动态值时，使用语法 `item()?['PropertyName']` 来安全地访问集合中的属性。

### 5. 参数和变量

- **参数化您的工作流**以便跨环境重用
- **对工作流内的临时值使用变量**
- **定义清晰的参数模式**，包含默认值和描述

```json
"parameters": {
  "apiEndpoint": {
    "type": "string",
    "defaultValue": "https://api.dev.example.com",
    "metadata": {
      "description": "API 端点的基础 URL"
    }
  }
},
"variables": {
  "requestId": "@{guid()}",
  "processedItems": []
}
```

### 6. 控制流

- **使用条件**进行分支逻辑
- **实现并行分支**进行独立操作
- **为集合使用具有合理批量大小的 foreach 循环**
- **应用 until 循环**并配置适当的退出条件

```json
"Process_Items": {
  "type": "Foreach",
  "foreach": "@body('Get_Items')",
  "actions": {
    "Process_Single_Item": {
      "type": "Scope",
      "actions": { }
    }
  },
  "runAfter": {
    "Get_Items": ["Succeeded"]
  },
  "runtimeConfiguration": {
    "concurrency": {
      "repetitions": 10
    }
  }
}
```

### 7. 内容和消息处理

- **验证消息模式**以确保数据完整性
- **实现适当的内容类型处理**
- **使用 Parse JSON 操作**处理结构化数据

```json
"Parse_Response": {
  "type": "ParseJson",
  "inputs": {
    "content": "@body('HTTP_Request')",
    "schema": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "data": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": { }
          }
        }
      }
    }
  }
}
```

### 8. 安全最佳实践

- **尽可能使用托管标识**
- **在 Key Vault 中存储机密**
- **为连接实施最小权限访问**
- **使用身份验证保护 API 端点**
- **为 HTTP 触发器实施 IP 限制**
- **对参数和消息中的敏感数据应用数据加密**
- **使用 Azure RBAC** 控制 Logic Apps 资源的访问
- **定期进行安全审查**工作流和连接

```json
"Get_Secret": {
  "type": "ApiConnection",
  "inputs": {
    "host": {
      "connection": {
        "name": "@parameters('$connections')['keyvault']['connectionId']"
      }
    },
    "method": "get",
    "path": "/secrets/@{encodeURIComponent('apiKey')}/value"
  }
},
"Call_Protected_API": {
  "type": "Http",
  "inputs": {
    "method": "POST",
    "uri": "https://api.example.com/protected",
    "headers": {
      "Content-Type": "application/json",
      "Authorization": "Bearer @{body('Get_Secret')?['value']}"
    },
    "body": {
      "data": "@variables('processedData')"
    }
  },
  "authentication": {
    "type": "ManagedServiceIdentity"
  },
  "runAfter": {
    "Get_Secret": ["Succeeded"]
  }
}
```

## 性能优化

- **最小化不必要的操作**
- **在可用时使用批量操作**
- **优化表达式**以降低复杂性
- **配置适当的超时值**
- **为大型数据集实施分页**
- **为可并行操作实施并发控制**

```json
"Process_Items": {
  "type": "Foreach",
  "foreach": "@body('Get_Items')",
  "actions": {
    "Process_Single_Item": {
      "type": "Scope",
      "actions": { }
    }
  },
  "runAfter": {
    "Get_Items": ["Succeeded"]
  },
  "runtimeConfiguration": {
    "concurrency": {
      "repetitions": 10
    }
  }
}
```

### 工作流设计最佳实践

- **将工作流限制在 50 个操作或更少**以获得最佳设计器性能
- **在必要时将复杂的业务逻辑分解**为多个较小的工作流
- **使用部署槽**进行需要零停机部署的任务关键型逻辑应用
- **避免在触发器和操作定义中使用硬编码属性**
- **添加描述性注释**提供有关触发器和操作定义的上下文
- **在可用时使用内置操作**而不是共享连接器以获得更好的性能
- **使用集成账户**进行 B2B 场景和 EDI 消息处理
- **重用工作流模板**用于组织内的标准模式
- **避免范围和操作的深度嵌套**以保持可读性

### 监控和可观测性

- **配置诊断设置**以捕获工作流运行和指标
- **添加跟踪 ID**以关联相关工作流运行
- **实施全面的日志记录**并配置适当的详细级别
- **为工作流失败和性能下降设置警报**
- **使用 Application Insights**进行端到端跟踪和监控

## 平台类型和注意事项

### Azure Logic Apps 与 Power Automate

虽然 Azure Logic Apps 和 Power Automate 共享相同的基础工作流引擎和语言，但它们有不同的目标受众和功能：

- **Power Automate**：
  - 为业务用户提供用户友好的界面
  - Power Platform 生态系统的一部分
  - 与 Microsoft 365 和 Dynamics 365 集成
  - 用于 UI 自动化的桌面流功能

- **Azure Logic Apps**：
  - 企业级集成平台
  - 以开发人员为中心，具有高级功能
  - 更深入的 Azure 服务集成
  - 更广泛的监控和操作功能

### Logic App 类型

#### 消费型 Logic Apps
- 按执行付费定价模型
- 无服务器架构
- 适用于可变或不可预测的工作负载

#### 标准 Logic Apps
- 基于 App Service Plan 的固定定价
- 可预测的性能
- 支持本地开发
- 与 VNets 集成

#### 集成服务环境（ISE）
- 专用部署环境
- 更高的吞吐量和更长的执行持续时间
- 直接访问 VNet 资源
- 隔离的运行时环境

### Power Automate 许可证类型
- **Power Automate 每用户计划**：用于个人用户
- **Power Automate 每流计划**：用于特定工作流
- **Power Automate 流程计划**：用于 RPA 功能
- **Office 365 包含的 Power Automate**：Office 365 用户的有限功能

## 常见集成模式

### 架构模式
- **中介模式**：使用 Logic Apps/Power Automate 作为系统间的编排层
- **基于内容的路由**：根据内容将消息路由到不同目标
- **消息转换**：在不同格式之间转换消息（JSON、XML、EDI 等）
- **分散聚合**：并行分发工作并聚合结果
- **协议桥接**：连接具有不同协议的系统（REST、SOAP、FTP 等）
- **凭单检查**：将大型负载外部存储在 blob 存储或数据库中
- **Saga 模式**：使用补偿操作管理分布式事务处理失败
- **编排模式**：协调多个服务而不使用中央编排器

### 操作模式
- **异步处理模式**：用于长时间运行的操作
  ```json
  "LongRunningAction": {
    "type": "Http",
    "inputs": {
      "method": "POST",
      "uri": "https://api.example.com/longrunning",
      "body": { "data": "@triggerBody()" }
    },
    "retryPolicy": {
      "type": "fixed",
      "count": 3,
      "interval": "PT30S"
    }
  }
  ```

- **Webhook 模式**：用于基于回调的处理
  ```json
  "WebhookAction": {
    "type": "ApiConnectionWebhook",
    "inputs": {
      "host": {
        "connection": {
          "name": "@parameters('$connections')['servicebus']['connectionId']"
        }
      },
      "body": {
        "content": "@triggerBody()"
      },
      "path": "/subscribe/topics/@{encodeURIComponent('mytopic')}/subscriptions/@{encodeURIComponent('mysubscription')}"
    }
  }
  ```

### 企业集成模式
- **B2B 消息交换**：在贸易伙伴之间交换 EDI 文档（AS2、X12、EDIFACT）
- **集成账户**：用于存储和管理 B2B 构件（协议、模式、映射）
- **规则引擎**：使用 Azure Logic Apps 规则引擎实施复杂的业务规则
- **消息验证**：根据模式验证消息以确保合规性和数据完整性
- **事务处理**：处理业务事务并使用补偿事务进行回滚

## Logic Apps 的 DevOps 和 CI/CD

### 源代码控制和版本管理

- **将 Logic App 定义存储在源代码控制中**（Git、Azure DevOps、GitHub）
- **使用 ARM 模板**部署到多个环境
- **实施适合您发布节奏的分支策略**
- **使用标签或版本属性**对 Logic Apps 进行版本管理

### 自动化部署

- **使用 Azure DevOps 管道**或 GitHub Actions 进行自动化部署
- **实施参数化**处理环境特定值
- **使用部署槽**进行零停机部署
- **在 CI/CD 管道中包含部署后验证**测试

```yaml
# Logic App 部署的 Azure DevOps YAML 管道示例
trigger:
  branches:
    include:
    - main
    - release/*

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: AzureResourceManagerTemplateDeployment@3
  inputs:
    deploymentScope: 'Resource Group'
    azureResourceManagerConnection: 'Your-Azure-Connection'
    subscriptionId: '$(subscriptionId)'
    action: 'Create Or Update Resource Group'
    resourceGroupName: '$(resourceGroupName)'
    location: '$(location)'
    templateLocation: 'Linked artifact'
    csmFile: '$(System.DefaultWorkingDirectory)/arm-templates/logicapp-template.json'
    csmParametersFile: '$(System.DefaultWorkingDirectory)/arm-templates/logicapp-parameters-$(Environment).json'
    deploymentMode: 'Incremental'
```

## 跨平台注意事项

在同时使用 Azure Logic Apps 和 Power Automate 时：

- **导出/导入兼容性**：可以从 Power Automate 导出流并导入到 Logic Apps，但可能需要进行一些修改
- **连接器差异**：某些连接器在一个平台中可用，但在另一个平台中不可用
- **环境隔离**：Power Automate 环境提供隔离，可能具有不同的策略
- **ALM 实践**：考虑对 Logic Apps 使用 Azure DevOps，对 Power Automate 使用解决方案

### 迁移策略

- **评估**：评估复杂性和迁移适用性
- **连接器映射**：映射平台间的连接器并识别差距
- **测试策略**：在切换前实施并行测试
- **文档**：记录所有配置更改以供参考

```json
// Power Platform 解决方案的 Power Automate 流结构示例
{
  "SolutionName": "MyEnterpriseFlows",
  "Version": "1.0.0",
  "Flows": [
    {
      "Name": "OrderProcessingFlow",
      "Type": "Microsoft.Flow/flows",
      "Properties": {
        "DisplayName": "Order Processing Flow",
        "DefinitionData": {
          "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
          "triggers": {
            "When_a_new_order_is_created": {
              "type": "ApiConnectionWebhook",
              "inputs": {
                "host": {
                  "connectionName": "shared_commondataserviceforapps",
                  "operationId": "SubscribeWebhookTrigger",
                  "apiId": "/providers/Microsoft.PowerApps/apis/shared_commondataserviceforapps"
                }
              }
            }
          },
          "actions": {
            // 这里将定义操作
          }
        }
      }
    }
  ]
}
```

## 实用 Logic App 示例

### 具有 API 集成的 HTTP 请求处理程序

此示例演示了一个 Logic App，它接受 HTTP 请求，验证输入数据，调用外部 API，转换响应，并返回格式化的结果。

```json
{
  "definition": {
    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
    "actions": {
      "Validate_Input": {
        "type": "If",
        "expression": {
          "and": [
            {
              "not": {
                "equals": [
                  "@triggerBody()?['customerId']",
                  null
                ]
              }
            },
            {
              "not": {
                "equals": [
                  "@triggerBody()?['requestType']",
                  null
                ]
              }
            }
          ]
        },
        "actions": {
          "Get_Customer_Data": {
            "type": "Http",
            "inputs": {
              "method": "GET",
              "uri": "https://api.example.com/customers/@{triggerBody()?['customerId']}",
              "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer @{body('Get_API_Key')?['value']}"
              }
            },
            "runAfter": {
              "Get_API_Key": [
                "Succeeded"
              ]
            }
          },
          "Get_API_Key": {
            "type": "ApiConnection",
            "inputs": {
              "host": {
                "connection": {
                  "name": "@parameters('$connections')['keyvault']['connectionId']"
                }
              },
              "method": "get",
              "path": "/secrets/@{encodeURIComponent('apiKey')}/value"
            }
          },
          "Parse_Customer_Response": {
            "type": "ParseJson",
            "inputs": {
              "content": "@body('Get_Customer_Data')",
              "schema": {
                "type": "object",
                "properties": {
                  "id": { "type": "string" },
                  "name": { "type": "string" },
                  "email": { "type": "string" },
                  "status": { "type": "string" },
                  "createdDate": { "type": "string" },
                  "orders": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "orderId": { "type": "string" },
                        "orderDate": { "type": "string" },
                        "amount": { "type": "number" }
                      }
                    }
                  }
                }
              }
            },
            "runAfter": {
              "Get_Customer_Data": [
                "Succeeded"
              ]
            }
          },
          "Switch_Request_Type": {
            "type": "Switch",
            "expression": "@triggerBody()?['requestType']",
            "cases": {
              "Profile": {
                "actions": {
                  "Prepare_Profile_Response": {
                    "type": "SetVariable",
                    "inputs": {
                      "name": "responsePayload",
                      "value": {
                        "customerId": "@body('Parse_Customer_Response')?['id']",
                        "customerName": "@body('Parse_Customer_Response')?['name']",
                        "email": "@body('Parse_Customer_Response')?['email']",
                        "status": "@body('Parse_Customer_Response')?['status']",
                        "memberSince": "@formatDateTime(body('Parse_Customer_Response')?['createdDate'], 'yyyy-MM-dd')"
                      }
                    }
                  }
                }
              },
              "OrderSummary": {
                "actions": {
                  "Calculate_Order_Statistics": {
                    "type": "Compose",
                    "inputs": {
                      "totalOrders": "@length(body('Parse_Customer_Response')?['orders'])",
                      "totalSpent": "@sum(body('Parse_Customer_Response')?['orders'], item => item.amount)",
                      "averageOrderValue": "@if(greater(length(body('Parse_Customer_Response')?['orders']), 0), div(sum(body('Parse_Customer_Response')?['orders'], item => item.amount), length(body('Parse_Customer_Response')?['orders'])), 0)",
                      "lastOrderDate": "@if(greater(length(body('Parse_Customer_Response')?['orders']), 0), max(body('Parse_Customer_Response')?['orders'], item => item.orderDate), '')"
                    }
                  },
                  "Prepare_Order_Response": {
                    "type": "SetVariable",
                    "inputs": {
                      "name": "responsePayload",
                      "value": {
                        "customerId": "@body('Parse_Customer_Response')?['id']",
                        "customerName": "@body('Parse_Customer_Response')?['name']",
                        "orderStats": "@outputs('Calculate_Order_Statistics')"
                      }
                    },
                    "runAfter": {
                      "Calculate_Order_Statistics": [
                        "Succeeded"
                      ]
                    }
                  }
                }
              }
            },
            "default": {
              "actions": {
                "Set_Default_Response": {
                  "type": "SetVariable",
                  "inputs": {
                    "name": "responsePayload",
                    "value": {
                      "error": "Invalid request type specified",
                      "validTypes": [
                        "Profile",
                        "OrderSummary"
                      ]
                    }
                  }
                }
              }
            },
            "runAfter": {
              "Parse_Customer_Response": [
                "Succeeded"
              ]
            }
          },
          "Log_Successful_Request": {
            "type": "ApiConnection",
            "inputs": {
              "host": {
                "connection": {
                  "name": "@parameters('$connections')['applicationinsights']['connectionId']"
                }
              },
              "method": "post",
              "body": {
                "LogType": "ApiRequestSuccess",
                "CustomerId": "@triggerBody()?['customerId']",
                "RequestType": "@triggerBody()?['requestType']",
                "ProcessingTime": "@workflow()['run']['duration']"
              }
            },
            "runAfter": {
              "Switch_Request_Type": [
                "Succeeded"
              ]
            }
          },
          "Return_Success_Response": {
            "type": "Response",
            "kind": "Http",
            "inputs": {
              "statusCode": 200,
              "body": "@variables('responsePayload')",
              "headers": {
                "Content-Type": "application/json"
              }
            },
            "runAfter": {
              "Log_Successful_Request": [
                "Succeeded"
              ]
            }
          }
        },
        "else": {
          "actions": {
            "Return_Validation_Error": {
              "type": "Response",
              "kind": "Http",
              "inputs": {
                "statusCode": 400,
                "body": {
                  "error": "Invalid request",
                  "message": "Request must include customerId and requestType",
                  "timestamp": "@utcNow()"
                }
              }
            }
          }
        },
        "runAfter": {
          "Initialize_Response_Variable": [
            "Succeeded"
          ]
        }
      },
      "Initialize_Response_Variable": {
        "type": "InitializeVariable",
        "inputs": {
          "variables": [
            {
              "name": "responsePayload",
              "type": "object",
              "value": {}
            }
          ]
        }
      }
    },
    "contentVersion": "1.0.0.0",
    "outputs": {},
    "parameters": {
      "$connections": {
        "defaultValue": {},
        "type": "Object"
      }
    },
    "triggers": {
      "manual": {
        "type": "Request",
        "kind": "Http",
        "inputs": {
          "schema": {
            "type": "object",
            "properties": {
              "customerId": {
                "type": "string"
              },
              "requestType": {
                "type": "string",
                "enum": [
                  "Profile",
                  "OrderSummary"
                ]
              }
            }
          }
        }
      }
    }
  },
  "parameters": {
    "$connections": {
      "value": {
        "keyvault": {
          "connectionId": "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Web/connections/keyvault",
          "connectionName": "keyvault",
          "id": "/subscriptions/{subscription-id}/providers/Microsoft.Web/locations/{location}/managedApis/keyvault"
        },
        "applicationinsights": {
          "connectionId": "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Web/connections/applicationinsights",
          "connectionName": "applicationinsights",
          "id": "/subscriptions/{subscription-id}/providers/Microsoft.Web/locations/{location}/managedApis/applicationinsights"
        }
      }
    }
  }
}
```

### 具有错误处理的事件驱动流程

此示例演示了一个 Logic App，它处理来自 Azure Service Bus 的事件，使用健壮的错误处理处理消息处理，并为弹性实施重试模式。

```json
{
  "definition": {
    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
    "actions": {
      "Parse_Message": {
        "type": "ParseJson",
        "inputs": {
          "content": "@triggerBody()?['ContentData']",
          "schema": {
            "type": "object",
            "properties": {
              "eventId": { "type": "string" },
              "eventType": { "type": "string" },
              "eventTime": { "type": "string" },
              "dataVersion": { "type": "string" },
              "data": {
                "type": "object",
                "properties": {
                  "orderId": { "type": "string" },
                  "customerId": { "type": "string" },
                  "items": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "productId": { "type": "string" },
                        "quantity": { "type": "integer" },
                        "unitPrice": { "type": "number" }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "runAfter": {}
      },
      "Try_Process_Order": {
        "type": "Scope",
        "actions": {
          "Get_Customer_Details": {
            "type": "Http",
            "inputs": {
              "method": "GET",
              "uri": "https://api.example.com/customers/@{body('Parse_Message')?['data']?['customerId']}",
              "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer @{body('Get_API_Key')?['value']}"
              }
            },
            "runAfter": {
              "Get_API_Key": [
                "Succeeded"
              ]
            },
            "retryPolicy": {
              "type": "exponential",
              "count": 5,
              "interval": "PT10S",
              "minimumInterval": "PT5S",
              "maximumInterval": "PT1H"
            }
          },
          "Get_API_Key": {
            "type": "ApiConnection",
            "inputs": {
              "host": {
                "connection": {
                  "name": "@parameters('$connections')['keyvault']['connectionId']"
                }
              },
              "method": "get",
              "path": "/secrets/@{encodeURIComponent('apiKey')}/value"
            }
          },
          "Validate_Stock": {
            "type": "Foreach",
            "foreach": "@body('Parse_Message')?['data']?['items']",
            "actions": {
              "Check_Product_Stock": {
                "type": "Http",
                "inputs": {
                  "method": "GET",
                  "uri": "https://api.example.com/inventory/@{items('Validate_Stock')?['productId']}",
                  "headers": {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer @{body('Get_API_Key')?['value']}"
                  }
                },
                "retryPolicy": {
                  "type": "fixed",
                  "count": 3,
                  "interval": "PT15S"
                }
              },
              "Verify_Availability": {
                "type": "If",
                "expression": {
                  "and": [
                    {
                      "greater": [
                        "@body('Check_Product_Stock')?['availableStock']",
                        "@items('Validate_Stock')?['quantity']"
                      ]
                    }
                  ]
                },
                "actions": {
                  "Add_To_Valid_Items": {
                    "type": "AppendToArrayVariable",
                    "inputs": {
                      "name": "validItems",
                      "value": {
                        "productId": "@items('Validate_Stock')?['productId']",
                        "quantity": "@items('Validate_Stock')?['quantity']",
                        "unitPrice": "@items('Validate_Stock')?['unitPrice']",
                        "availableStock": "@body('Check_Product_Stock')?['availableStock']"
                      }
                    }
                  }
                },
                "else": {
                  "actions": {
                    "Add_To_Invalid_Items": {
                      "type": "AppendToArrayVariable",
                      "inputs": {
                        "name": "invalidItems",
                        "value": {
                          "productId": "@items('Validate_Stock')?['productId']",
                          "requestedQuantity": "@items('Validate_Stock')?['quantity']",
                          "availableStock": "@body('Check_Product_Stock')?['availableStock']",
                          "reason": "Insufficient stock"
                        }
                      }
                    }
                  }
                },
                "runAfter": {
                  "Check_Product_Stock": [
                    "Succeeded"
                  ]
                }
              }
            },
            "runAfter": {
              "Get_Customer_Details": [
                "Succeeded"
              ]
            }
          },
          "Check_Order_Validity": {
            "type": "If",
            "expression": {
              "and": [
                {
                  "equals": [
                    "@length(variables('invalidItems'))",
                    0
                  ]
                },
                {
                  "greater": [
                    "@length(variables('validItems'))",
                    0
                  ]
                }
              ]
            },
            "actions": {
              "Process_Valid_Order": {
                "type": "Http",
                "inputs": {
                  "method": "POST",
                  "uri": "https://api.example.com/orders",
                  "headers": {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer @{body('Get_API_Key')?['value']}"
                  },
                  "body": {
                    "orderId": "@body('Parse_Message')?['data']?['orderId']",
                    "customerId": "@body('Parse_Message')?['data']?['customerId']",
                    "customerName": "@body('Get_Customer_Details')?['name']",
                    "items": "@variables('validItems')",
                    "processedTime": "@utcNow()",
                    "eventId": "@body('Parse_Message')?['eventId']"
                  }
                }
              },
              "Send_Order_Confirmation": {
                "type": "ApiConnection",
                "inputs": {
                  "host": {
                    "connection": {
                      "name": "@parameters('$connections')['office365']['connectionId']"
                    }
                  },
                  "method": "post",
                  "path": "/v2/Mail",
                  "body": {
                    "To": "@body('Get_Customer_Details')?['email']",
                    "Subject": "Order Confirmation: @{body('Parse_Message')?['data']?['orderId']}",
                    "Body": "<p>Dear @{body('Get_Customer_Details')?['name']},</p><p>Your order has been successfully processed.</p><p>Order ID: @{body('Parse_Message')?['data']?['orderId']}</p><p>Thank you for your business!</p>",
                    "Importance": "Normal",
                    "IsHtml": true
                  }
                },
                "runAfter": {
                  "Process_Valid_Order": [
                    "Succeeded"
                  ]
                }
              },
              "Complete_Message": {
                "type": "ApiConnection",
                "inputs": {
                  "host": {
                    "connection": {
                      "name": "@parameters('$connections')['servicebus']['connectionId']"
                    }
                  },
                  "method": "post",
                  "path": "/messages/complete",
                  "body": {
                    "lockToken": "@triggerBody()?['LockToken']",
                    "sessionId": "@triggerBody()?['SessionId']",
                    "queueName": "@parameters('serviceBusQueueName')"
                  }
                },
                "runAfter": {
                  "Send_Order_Confirmation": [
                    "Succeeded"
                  ]
                }
              }
            },
            "else": {
              "actions": {
                "Send_Invalid_Stock_Notification": {
                  "type": "ApiConnection",
                  "inputs": {
                    "host": {
                      "connection": {
                        "name": "@parameters('$connections')['office365']['connectionId']"
                      }
                    },
                    "method": "post",
                    "path": "/v2/Mail",
                    "body": {
                      "To": "@body('Get_Customer_Details')?['email']",
                      "Subject": "Order Cannot Be Processed: @{body('Parse_Message')?['data']?['orderId']}",
                      "Body": "<p>Dear @{body('Get_Customer_Details')?['name']},</p><p>We regret to inform you that your order cannot be processed due to insufficient stock for the following items:</p><p>@{join(variables('invalidItems'), '</p><p>')}</p><p>Please adjust your order and try again.</p>",
                      "Importance": "High",
                      "IsHtml": true
                    }
                  }
                },
                "Dead_Letter_Message": {
                  "type": "ApiConnection",
                  "inputs": {
                    "host": {
                      "connection": {
                        "name": "@parameters('$connections')['servicebus']['connectionId']"
                      }
                    },
                    "method": "post",
                    "path": "/messages/deadletter",
                    "body": {
                      "lockToken": "@triggerBody()?['LockToken']",
                      "sessionId": "@triggerBody()?['SessionId']",
                      "queueName": "@parameters('serviceBusQueueName')",
                      "deadLetterReason": "InsufficientStock",
                      "deadLetterDescription": "Order contained items with insufficient stock"
                    }
                  },
                  "runAfter": {
                    "Send_Invalid_Stock_Notification": [
                      "Succeeded"
                    ]
                  }
                }
              }
            },
            "runAfter": {
              "Validate_Stock": [
                "Succeeded"
              ]
            }
          }
        },
        "runAfter": {
          "Initialize_Variables": [
            "Succeeded"
          ]
        }
      },
      "Initialize_Variables": {
        "type": "InitializeVariable",
        "inputs": {
          "variables": [
            {
              "name": "validItems",
              "type": "array",
              "value": []
            },
            {
              "name": "invalidItems",
              "type": "array",
              "value": []
            }
          ]
        },
        "runAfter": {
          "Parse_Message": [
            "Succeeded"
          ]
        }
      },
      "Handle_Process_Error": {
        "type": "Scope",
        "actions": {
          "Log_Error_Details": {
            "type": "ApiConnection",
            "inputs": {
              "host": {
                "connection": {
                  "name": "@parameters('$connections')['applicationinsights']['connectionId']"
                }
              },
              "method": "post",
              "body": {
                "LogType": "OrderProcessingError",
                "EventId": "@body('Parse_Message')?['eventId']",
                "OrderId": "@body('Parse_Message')?['data']?['orderId']",
                "CustomerId": "@body('Parse_Message')?['data']?['customerId']",
                "ErrorDetails": "@result('Try_Process_Order')",
                "Timestamp": "@utcNow()"
              }
            }
          },
          "Abandon_Message": {
            "type": "ApiConnection",
            "inputs": {
              "host": {
                "connection": {
                  "name": "@parameters('$connections')['servicebus']['connectionId']"
                }
              },
              "method": "post",
              "path": "/messages/abandon",
              "body": {
                "lockToken": "@triggerBody()?['LockToken']",
                "sessionId": "@triggerBody()?['SessionId']",
                "queueName": "@parameters('serviceBusQueueName')"
              }
            },
            "runAfter": {
              "Log_Error_Details": [
                "Succeeded"
              ]
            }
          },
          "Send_Alert_To_Operations": {
            "type": "ApiConnection",
            "inputs": {
              "host": {
                "connection": {
                  "name": "@parameters('$connections')['office365']['connectionId']"
                }
              },
              "method": "post",
              "path": "/v2/Mail",
              "body": {
                "To": "operations@example.com",
                "Subject": "Order Processing Error: @{body('Parse_Message')?['data']?['orderId']}",
                "Body": "<p>An error occurred while processing an order:</p><p>Order ID: @{body('Parse_Message')?['data']?['orderId']}</p><p>Customer ID: @{body('Parse_Message')?['data']?['customerId']}</p><p>Error: @{result('Try_Process_Order')}</p>",
                "Importance": "High",
                "IsHtml": true
              }
            },
            "runAfter": {
              "Abandon_Message": [
                "Succeeded"
              ]
            }
          }
        },
        "runAfter": {
          "Try_Process_Order": [
            "Failed",
            "TimedOut"
          ]
        }
      }
    },
    "contentVersion": "1.0.0.0",
    "outputs": {},
    "parameters": {
      "$connections": {
        "defaultValue": {},
        "type": "Object"
      },
      "serviceBusQueueName": {
        "type": "string",
        "defaultValue": "orders"
      }
    },
    "triggers": {
      "When_a_message_is_received_in_a_queue": {
        "type": "ApiConnectionWebhook",
        "inputs": {
          "host": {
            "connection": {
              "name": "@parameters('$connections')['servicebus']['connectionId']"
            }
          },
          "body": {
            "isSessionsEnabled": true
          },
          "path": "/subscriptionListener",
          "queries": {
            "queueName": "@parameters('serviceBusQueueName')",
            "subscriptionType": "Main"
          }
        }
      }
    }
  },
  "parameters": {
    "$connections": {
      "value": {
        "keyvault": {
          "connectionId": "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Web/connections/keyvault",
          "connectionName": "keyvault",
          "id": "/subscriptions/{subscription-id}/providers/Microsoft.Web/locations/{location}/managedApis/keyvault"
        },
        "servicebus": {
          "connectionId": "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Web/connections/servicebus",
          "connectionName": "servicebus",
          "id": "/subscriptions/{subscription-id}/providers/Microsoft.Web/locations/{location}/managedApis/servicebus"
        },
        "office365": {
          "connectionId": "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Web/connections/office365",
          "connectionName": "office365",
          "id": "/subscriptions/{subscription-id}/providers/Microsoft.Web/locations/{location}/managedApis/office365"
        },
        "applicationinsights": {
          "connectionId": "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Web/connections/applicationinsights",
          "connectionName": "applicationinsights",
          "id": "/subscriptions/{subscription-id}/providers/Microsoft.Web/locations/{location}/managedApis/applicationinsights"
        }
      }
    }
  }
}
```

## 高级异常处理和监控

### 全面的异常处理策略

为健壮的工作流实施多层异常处理方法：

1. **预防措施**：
   - 对所有传入消息使用模式验证
   - 使用 `coalesce()` 和 `?` 操作符实施防御性表达式评估
   - 在关键操作前添加前置条件检查

2. **运行时错误处理**：
   - 使用具有嵌套 try/catch 模式的结构化错误处理范围
   - 为外部依赖实施断路器模式
   - 不同地捕获和处理特定错误类型

```json
"Process_With_Comprehensive_Error_Handling": {
  "type": "Scope",
  "actions": {
    "Try_Primary_Action": {
      "type": "Scope",
      "actions": {
        "Main_Operation": {
          "type": "Http",
          "inputs": { "method": "GET", "uri": "https://api.example.com/resource" }
        }
      }
    },
    "Handle_Connection_Errors": {
      "type": "Scope",
      "actions": {
        "Log_Connection_Error": {
          "type": "ApiConnection",
          "inputs": {
            "host": {
              "connection": {
                "name": "@parameters('$connections')['loganalytics']['connectionId']"
              }
            },
            "method": "post",
            "body": {
              "LogType": "ConnectionError",
              "ErrorCategory": "Network",
              "StatusCode": "@{result('Try_Primary_Action')?['outputs']?['Main_Operation']?['statusCode']}",
              "ErrorMessage": "@{result('Try_Primary_Action')?['error']?['message']}"
            }
          }
        },
        "Invoke_Fallback_Endpoint": {
          "type": "Http",
          "inputs": { "method": "GET", "uri": "https://fallback-api.example.com/resource" }
        }
      },
      "runAfter": {
        "Try_Primary_Action": ["Failed"]
      }
    },
    "Handle_Business_Logic_Errors": {
      "type": "Scope",
      "actions": {
        "Parse_Error_Response": {
          "type": "ParseJson",
          "inputs": {
            "content": "@outputs('Try_Primary_Action')?['Main_Operation']?['body']",
            "schema": {
              "type": "object",
              "properties": {
                "errorCode": { "type": "string" },
                "errorMessage": { "type": "string" }
              }
            }
          }
        },
        "Switch_On_Error_Type": {
          "type": "Switch",
          "expression": "@body('Parse_Error_Response')?['errorCode']",
          "cases": {
            "ResourceNotFound": {
              "actions": { "Create_Resource": { "type": "Http", "inputs": {} } }
            },
            "ValidationError": {
              "actions": { "Resubmit_With_Defaults": { "type": "Http", "inputs": {} } }
            },
            "PermissionDenied": {
              "actions": { "Elevate_Permissions": { "type": "Http", "inputs": {} } }
            }
          },
          "default": {
            "actions": { "Send_To_Support_Queue": { "type": "ApiConnection", "inputs": {} } }
          }
        }
      },
      "runAfter": {
        "Try_Primary_Action": ["Succeeded"]
      }
    }
  }
}
```

3. **集中式错误日志记录**：
   - 创建专用的错误处理 Logic App，供其他工作流调用
   - 使用关联 ID 记录错误以便跨系统跟踪
   - 按类型和严重性对错误进行分类以便更好地分析

### 高级监控架构

实施涵盖以下方面的全面监控策略：

1. **操作监控**：
   - **健康检查**：创建专用的健康检查工作流
   - **心跳模式**：实施定期检查以验证系统健康状况
   - **死信处理**：处理和分析失败的消息

2. **业务流程监控**：
   - **业务指标**：跟踪关键业务 KPI（订单处理时间、批准率）
   - **SLA 监控**：根据服务水平协议衡量性能
   - **关联跟踪**：实施端到端事务跟踪

3. **警报策略**：
   - **多渠道警报**：向适当渠道配置警报（电子邮件、SMS、Teams）
   - **基于严重性的路由**：根据业务影响路由警报
   - **警报关联**：对相关警报进行分组以防止警报疲劳

```json
"Monitor_Transaction_SLA": {
  "type": "Scope",
  "actions": {
    "Calculate_Processing_Time": {
      "type": "Compose",
      "inputs": "@{div(sub(ticks(utcNow()), ticks(triggerBody()?['startTime'])), 10000000)}"
    },
    "Check_SLA_Breach": {
      "type": "If",
      "expression": "@greater(outputs('Calculate_Processing_Time'), parameters('slaThresholdSeconds'))",
      "actions": {
        "Log_SLA_Breach": {
          "type": "ApiConnection",
          "inputs": {
            "host": {
              "connection": {
                "name": "@parameters('$connections')['loganalytics']['connectionId']"
              }
            },
            "method": "post",
            "body": {
              "LogType": "SLABreach",
              "TransactionId": "@{triggerBody()?['transactionId']}",
              "ProcessingTimeSeconds": "@{outputs('Calculate_Processing_Time')}",
              "SLAThresholdSeconds": "@{parameters('slaThresholdSeconds')}",
              "BreachSeverity": "@if(greater(outputs('Calculate_Processing_Time'), mul(parameters('slaThresholdSeconds'), 2)), 'Critical', 'Warning')"
            }
          }
        },
        "Send_SLA_Alert": {
          "type": "ApiConnection",
          "inputs": {
            "host": {
              "connection": {
                "name": "@parameters('$connections')['teams']['connectionId']"
              }
            },
            "method": "post",
            "body": {
              "notificationTitle": "SLA Breach Alert",
              "message": "Transaction @{triggerBody()?['transactionId']} exceeded SLA by @{sub(outputs('Calculate_Processing_Time'), parameters('slaThresholdSeconds'))} seconds",
              "channelId": "@{if(greater(outputs('Calculate_Processing_Time'), mul(parameters('slaThresholdSeconds'), 2)), parameters('criticalAlertChannelId'), parameters('warningAlertChannelId'))}"
            }
          }
        }
      }
    }
  }
}
```

## API 管理集成

将 Logic Apps 与 Azure API 管理集成以增强安全性、治理和管理：

### API 管理前端

- **通过 API 管理公开 Logic Apps**：
  - 为 Logic App HTTP 触发器创建 API 定义
  - 应用一致的 URL 结构和版本管理
  - 实施安全性和转换的 API 策略

### Logic Apps 的策略模板

```xml
<!-- Logic App API 策略示例 -->
<policies>
  <inbound>
    <!-- 身份验证 -->
    <validate-jwt header-name="Authorization" failed-validation-httpcode="401" failed-validation-error-message="Unauthorized">
      <openid-config url="https://login.microsoftonline.com/{tenant-id}/.well-known/openid-configuration" />
      <required-claims>
        <claim name="aud" match="any">
          <value>api://mylogicapp</value>
        </claim>
      </required-claims>
    </validate-jwt>

    <!-- 速率限制 -->
    <rate-limit calls="5" renewal-period="60" />

    <!-- 请求转换 -->
    <set-header name="Correlation-Id" exists-action="override">
      <value>@(context.RequestId)</value>
    </set-header>

    <!-- 日志记录 -->
    <log-to-eventhub logger-id="api-logger">
      @{
        return new JObject(
          new JProperty("correlationId", context.RequestId),
          new JProperty("api", context.Api.Name),
          new JProperty("operation", context.Operation.Name),
          new JProperty("user", context.User.Email),
          new JProperty("ip", context.Request.IpAddress)
        ).ToString();
      }
    </log-to-eventhub>
  </inbound>
  <backend>
    <forward-request />
  </backend>
  <outbound>
    <!-- 响应转换 -->
    <set-header name="X-Powered-By" exists-action="delete" />
  </outbound>
  <on-error>
    <base />
  </on-error>
</policies>
```

### 工作流即 API 模式

- **实施工作流即 API 模式**：
  - 专门将 Logic Apps 设计为 API 后端
  - 使用具有 OpenAPI 模式的请求触发器
  - 应用一致的响应模式
  - 实施适当的状态码和错误处理

```json
"triggers": {
  "manual": {
    "type": "Request",
    "kind": "Http",
    "inputs": {
      "schema": {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
          "customerId": {
            "type": "string",
            "description": "客户的唯一标识符"
          },
          "requestType": {
            "type": "string",
            "enum": ["Profile", "OrderSummary"],
            "description": "要处理的请求类型"
          }
        },
        "required": ["customerId", "requestType"]
      },
      "method": "POST"
    }
  }
}
```

## 版本管理策略

为 Logic Apps 和 Power Automate 流实施健壮的版本管理方法：

### 版本管理模式

1. **URI 路径版本管理**：
   - 在 HTTP 触发器路径中包含版本（/api/v1/resource）
   - 为每个主要版本维护单独的 Logic Apps

2. **参数版本管理**：
   - 向工作流定义添加版本参数
   - 根据版本参数使用条件逻辑

3. **并行版本管理**：
   - 将新版本与现有版本并行部署
   - 实施版本间的流量路由

### 版本迁移策略

```json
"actions": {
  "Check_Request_Version": {
    "type": "Switch",
    "expression": "@triggerBody()?['apiVersion']",
    "cases": {
      "1.0": {
        "actions": {
          "Process_V1_Format": {
            "type": "Scope",
            "actions": { }
          }
        }
      },
      "2.0": {
        "actions": {
          "Process_V2_Format": {
            "type": "Scope",
            "actions": { }
          }
        }
      }
    },
    "default": {
      "actions": {
        "Return_Version_Error": {
          "type": "Response",
          "kind": "Http",
          "inputs": {
            "statusCode": 400,
            "body": {
              "error": "Unsupported API version",
              "supportedVersions": ["1.0", "2.0"]
            }
          }
        }
      }
    }
  }
}
```

### 不同版本的 ARM 模板部署

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "logicAppName": {
      "type": "string",
      "metadata": {
        "description": "Logic App 的基础名称"
      }
    },
    "version": {
      "type": "string",
      "metadata": {
        "description": "要部署的 Logic App 版本"
      },
      "allowedValues": ["v1", "v2", "v3"]
    }
  },
  "variables": {
    "fullLogicAppName": "[concat(parameters('logicAppName'), '-', parameters('version'))]",
    "workflowDefinitionMap": {
      "v1": "[variables('v1Definition')]",
      "v2": "[variables('v2Definition')]",
      "v3": "[variables('v3Definition')]"
    },
    "v1Definition": {},
    "v2Definition": {},
    "v3Definition": {}
  },
  "resources": [
    {
      "type": "Microsoft.Logic/workflows",
      "apiVersion": "2019-05-01",
      "name": "[variables('fullLogicAppName')]",
      "location": "[resourceGroup().location]",
      "properties": {
        "definition": "[variables('workflowDefinitionMap')[parameters('version')]]"
      }
    }
  ]
}
```

## 成本优化技术

实施策略以优化 Logic Apps 和 Power Automate 解决方案的成本：

### Logic Apps 消费优化

1. **触发器优化**：
   - 在触发器中使用批处理在单次运行中处理多个项目
   - 实施适当的重复间隔（避免过度轮询）
   - 使用基于 webhook 的触发器而不是轮询触发器

2. **操作优化**：
   - 通过组合相关操作减少操作计数
   - 使用内置函数而不是自定义操作
   - 为 foreach 循环实施适当的并发设置

3. **数据传输优化**：
   - 最小化 HTTP 请求/响应中的负载大小
   - 使用本地文件操作而不是重复的 API 调用
   - 为大型负载实施数据压缩

### Logic Apps 标准（工作流）成本优化

1. **App Service Plan 选择**：
   - 为工作负载需求正确调整 App Service Plan 的大小
   - 根据负载模式实施自动缩放
   - 为可预测的工作负载考虑保留实例

2. **资源共享**：
   - 在共享的 App Service Plan 中整合工作流
   - 实施共享连接和集成资源
   - 高效地使用集成账户

### Power Automate 许可证优化

1. **许可证类型选择**：
   - 根据工作流复杂性选择适当的许可证类型
   - 为每用户计划实施适当的用户分配
   - 考虑高级连接器的使用要求

2. **API 调用减少**：
   - 缓存频繁访问的数据
   - 为多个记录实施批处理
   - 减少计划流的触发频率

### 成本监控和治理

```json
"Monitor_Execution_Costs": {
  "type": "ApiConnection",
  "inputs": {
    "host": {
      "connection": {
        "name": "@parameters('$connections')['loganalytics']['connectionId']"
      }
    },
    "method": "post",
    "body": {
      "LogType": "WorkflowCostMetrics",
      "WorkflowName": "@{workflow().name}",
      "ExecutionId": "@{workflow().run.id}",
      "ActionCount": "@{length(workflow().run.actions)}",
      "TriggerType": "@{workflow().triggers[0].kind}",
      "DataProcessedBytes": "@{workflow().run.transferred}",
      "ExecutionDurationSeconds": "@{div(workflow().run.duration, 'PT1S')}",
      "Timestamp": "@{utcNow()}"
    }
  },
  "runAfter": {
    "Main_Workflow_Actions": ["Succeeded", "Failed", "TimedOut"]
  }
}
```

## 增强安全实践

为 Logic Apps 和 Power Automate 工作流实施全面的安全措施：

### 敏感数据处理

1. **数据分类和保护**：
   - 识别和分类工作流中的敏感数据
   - 在日志和监控中对敏感数据实施掩码
   - 对静态和传输中的数据应用加密

2. **安全参数处理**：
   - 对所有机密和凭据使用 Azure Key Vault
   - 在运行时实施动态参数解析
   - 对敏感值应用参数加密

```json
"actions": {
  "Get_Database_Credentials": {
    "type": "ApiConnection",
    "inputs": {
      "host": {
        "connection": {
          "name": "@parameters('$connections')['keyvault']['connectionId']"
        }
      },
      "method": "get",
      "path": "/secrets/@{encodeURIComponent('database-connection-string')}/value"
    }
  },
  "Execute_Database_Query": {
    "type": "ApiConnection",
    "inputs": {
      "host": {
        "connection": {
          "name": "@parameters('$connections')['sql']['connectionId']"
        }
      },
      "method": "post",
      "path": "/datasets/default/query",
      "body": {
        "query": "SELECT * FROM Customers WHERE CustomerId = @CustomerId",
        "parameters": {
          "CustomerId": "@triggerBody()?['customerId']"
        },
        "connectionString": "@body('Get_Database_Credentials')?['value']"
      }
    },
    "runAfter": {
      "Get_Database_Credentials": ["Succeeded"]
    }
  }
}
```

### 高级身份和访问控制

1. **细粒度访问控制**：
   - 为 Logic Apps 管理实施自定义角色
   - 对连接应用最小权限原则
   - 对所有 Azure 服务访问使用托管标识

2. **访问审查和治理**：
   - 对 Logic Apps 资源实施定期访问审查
   - 对管理操作实施即时访问
   - 审计所有访问和配置更改

3. **网络安全**：
   - 使用专用端点实施网络隔离
   - 为触发器端点应用 IP 限制
   - 对 Logic Apps Standard 使用虚拟网络集成

```json
{
  "resources": [
    {
      "type": "Microsoft.Logic/workflows",
      "apiVersion": "2019-05-01",
      "name": "[parameters('logicAppName')]",
      "location": "[parameters('location')]",
      "identity": {
        "type": "SystemAssigned"
      },
      "properties": {
        "accessControl": {
          "triggers": {
            "allowedCallerIpAddresses": [
              {
                "addressRange": "13.91.0.0/16"
              },
              {
                "addressRange": "40.112.0.0/13"
              }
            ]
          },
          "contents": {
            "allowedCallerIpAddresses": [
              {
                "addressRange": "13.91.0.0/16"
              },
              {
                "addressRange": "40.112.0.0/13"
              }
            ]
          },
          "actions": {
            "allowedCallerIpAddresses": [
              {
                "addressRange": "13.91.0.0/16"
              },
              {
                "addressRange": "40.112.0.0/13"
              }
            ]
          }
        },
        "definition": {}
      }
    }
  ]
}
```

## 其他资源

- [Azure Logic Apps 文档](https://docs.microsoft.com/en-us/azure/logic-apps/)
- [Power Automate 文档](https://docs.microsoft.com/en-us/power-automate/)
- [工作流定义语言模式](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-workflow-definition-language)
- [Power Automate 与 Logic Apps 比较](https://docs.microsoft.com/en-us/azure/azure-functions/functions-compare-logic-apps-ms-flow-webjobs)
- [企业集成模式](https://docs.microsoft.com/en-us/azure/logic-apps/enterprise-integration-overview)
- [Logic Apps B2B 文档](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-enterprise-integration-b2b)
- [Azure Logic Apps 限制和配置](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-limits-and-config)
- [Logic Apps 性能优化](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-performance-optimization)
- [Logic Apps 安全概述](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-securing-a-logic-app)
- [API 管理和 Logic Apps 集成](https://docs.microsoft.com/en-us/azure/api-management/api-management-create-api-logic-app)
- [Logic Apps 标准网络](https://docs.microsoft.com/en-us/azure/logic-apps/connect-virtual-network-vnet-isolated-environment)