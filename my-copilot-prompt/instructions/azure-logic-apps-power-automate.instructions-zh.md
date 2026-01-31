---
描述：“使用工作流定义语言 (WDL)、集成模式和企业自动化的最佳实践开发 Azure 逻辑应用和 Power Automate 工作流的指南”
applyTo: "**/*.json,**/*.logicapp.json,**/workflow.json,**/*-definition.json,**/*.flow.json"
---

# Azure 逻辑应用和 Power Automate 说明

## 概述

这些说明将指导你使用基于 JSON 的工作流定义语言 (WDL) 编写高质量的 Azure 逻辑应用和 Microsoft Power Automate 工作流定义。 Azure 逻辑应用是基于云的集成平台即服务 (iPaaS)，提供 1,400 多个连接器来简化跨服务和协议的集成。请遵循这些准则来创建强大、高效且可维护的云工作流自动化解决方案。

## 工作流程定义语言结构

使用逻辑应用或 Power Automate 流 JSON 文件时，请确保您的工作流遵循以下标准结构：

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

## Azure 逻辑应用和 Power 自动化开发的最佳实践

### 1. 触发器

- **根据您的场景使用适当的触发器类型**：
  - **请求触发器**：用于类似 API 的同步工作流程
  - **重复触发器**：用于计划操作
  - **基于事件的触发器**：适用于反应模式（服务总线、事件网格等）
- **配置正确的触发设置**：
  - 设置合理的超时时间
  - 对大容量数据源使用分页设置
  - 实施适当的身份验证

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

### 2. 行动

- **描述性地命名操作**以表明其目的
- **使用范围进行逻辑分组来组织复杂的工作流程**
- **针对不同的操作使用适当的操作类型**：
  - API 调用的 HTTP 操作
  - 内置集成的连接器操作
  - 转换的数据操作动作

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

- **实施稳健的错误处理**：
  - 使用“runAfter”配置来处理故障
  - 配置针对暂时性错误的重试策略
  - 对错误分支使用具有“runAfter”条件的范围
- **针对关键操作实施后备机制**
- **为外部服务调用添加超时**
- **使用 runAfter 条件**用于复杂的错误处理场景

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

- **使用内置表达式函数**来转换数据
- **保持表达式简洁易读**
- **用注释记录复杂的表达式**

常见的表达模式：
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

Power Automate 支持条件中的高级表达式来检查多个值。处理复杂的逻辑条件时，请使用以下模式：

- 要比较单个值：使用基本条件设计器界面
- 对于多个条件：在高级模式下使用高级表达式

Power Automate 中条件的常见逻辑表达式函数：

|表达 |描述 |示例|
|------------|-------------|---------|
| __代码0__ |如果两个参数都为 true，则返回 true | __代码1__ |
| __代码0__ |如果任一参数为 true，则返回 true | __代码1__ |
| __代码0__ |检查值是否相等 | __代码1__ |
| __代码0__ |检查第一个值是否大于第二个 | __代码1__ |
| __代码0__ |检查第一个值是否小于第二个 | __代码1__ |
| __代码0__ |检查对象、数组或字符串是否为空 | __代码1__ |
| __代码0__ |返回布尔值的相反值 | __代码1__ |

示例：检查状态是否为“已完成”或“不必要”：
```
@or(equals(item()?['Status'], 'completed'), equals(item()?['Status'], 'unnecessary'))
```

示例：检查状态是否为“阻止”并分配给特定人员：
```
@and(equals(item()?['Status'], 'blocked'), equals(item()?['Assigned'], 'John Wonder'))
```

示例：检查付款是否逾期且不完整：
```
@and(greater(item()?['Due'], item()?['Paid']), less(item()?['dueDate'], utcNow()))
```

**注意：** 在 Power Automate 中，在表达式中访问先前步骤中的动态值时，请使用语法 `item()?['PropertyName']` 安全地访问集合中的属性。

### 5. 参数和变量

- **参数化您的工作流程**以实现跨环境的可重用性
- **在工作流程中使用变量作为临时值**
- **使用默认值和描述定义清晰的参数模式**

```json
"parameters": {
  "apiEndpoint": {
    "type": "string",
    "defaultValue": "https://api.dev.example.com",
    "metadata": {
      "description": "The base URL for the API endpoint"
    }
  }
},
"variables": {
  "requestId": "@{guid()}",
  "processedItems": []
}
```

### 6. 控制流程

- **使用条件**进行分支逻辑
- **实现并行分支**以进行独立操作
- **使用 foreach 循环**和合理的批量大小进行集合
- **应用直到循环**并具有适当的退出条件

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
- **实施正确的内容类型处理**
- **使用解析 JSON 操作**来处理结构化数据

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

- **尽可能使用托管身份**
- **将机密存储在 Key Vault 中**
- **对连接实施最小权限访问**
- **通过身份验证保护 API 端点**
- **对 HTTP 触发器实施 IP 限制**
- **对参数和消息中的敏感数据应用数据加密**
- **使用 Azure RBAC** 控制对逻辑应用资源的访问
- **对工作流程和连接进行定期安全审查**

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

- **减少不必要的行动**
- **使用批处理操作**（如果可用）
- **优化表达式**以降低复杂性
- **配置适当的超时值**
- **对大型数据集实施分页**
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

### 工作流程设计最佳实践

- **将工作流程限制为 50 项或更少**，以获得最佳设计性能
- **必要时将复杂的业务逻辑**分解为多个较小的工作流程
- **将部署槽用于需要零停机部署的关键任务逻辑应用程序
- **避免在触发器和操作定义中使用硬编码属性**
- **添加描述性注释**以提供有关触发器和操作定义的上下文
- **使用可用的内置操作**而不是共享连接器以获得更好的性能
- **使用集成帐户**进行 B2B 场景和 EDI 消息处理
- **重复使用工作流程模板**以实现整个组织的标准模式
- **避免范围和操作的深度嵌套**以保持可读性

### 监控和可观察性

- **配置诊断设置**以捕获工作流程运行和指标
- **添加跟踪 ID** 以关联相关的工作流程运行
- **实施具有适当详细级别的全面日志记录**
- **针对工作流程失败和性能下降设置警报**
- **使用 Application Insights** 进行端到端跟踪和监控

## 平台类型和注意事项

### Azure 逻辑应用与 Power Automate

虽然 Azure 逻辑应用和 Power Automate 共享相同的底层工作流引擎和语言，但它们具有不同的目标受众和功能：

- **电源自动化**： 
  - 适合商业用户的用户友好界面
  - Power Platform 生态系统的一部分
  - 与 Microsoft 365 和 Dynamics 365 集成
  - 用于 UI 自动化的桌面流程功能

- **Azure 逻辑应用**：
  - 企业级集成平台
  - 以开发人员为中心，具有先进的功能
  - 更深入的 Azure 服务集成
  - 更广泛的监控和运营能力

### 逻辑应用程序类型

#### 消费逻辑应用
- 按执行付费定价模型
- 无服务器架构
- 适用于可变或不可预测的工作负载

#### 标准逻辑应用程序
- 基于应用服务计划的固定定价
- 可预测的性能
- 当地发展支持
- 与 VNet 集成

#### 集成服务环境 (ISE)
- 专用部署环境
- 更高的吞吐量和更长的执行持续时间
- 直接访问 VNet 资源
- 隔离的运行环境

### Power Automate 许可证类型
- **Power Automate 每用户计划**：针对个人用户
- **每个流程计划的 Power Automate**：适用于特定工作流程
- **Power Automate 流程计划**：针对 RPA 功能
- **Office 365 附带的 Power Automate**：Office 365 用户的功能有限

## 常见的集成模式

### 建筑模式
- **中介模式**：使用逻辑应用/Power Automate 作为系统之间的编排层
- **基于内容的路由**：根据内容将消息路由到不同的目的地
- **消息转换**：在格式（JSON、XML、EDI 等）之间转换消息
- **分散-聚集**：并行分配工作并聚合结果
- **协议桥接**：使用不同协议（REST、SOAP、FTP 等）连接系统
- **声明检查**：将大型有效负载存储在外部 blob 存储或数据库中
- **Saga 模式**：通过失败补偿操作来管理分布式事务
- **编排模式**：在没有中央编排器的情况下协调多个服务

### 行动模式
- **异步处理模式**：适用于长时间运行的操作
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
- **集成帐户**：用于存储和管理 B2B 工件（协议、模式、地图）
- **规则引擎**：使用 Azure 逻辑应用规则引擎实施复杂的业务规则
- **消息验证**：根据模式验证消息的合规性和数据完整性
- **事务处理**：处理业务事务并补偿事务回滚

## 逻辑应用程序的 DevOps 和 CI/CD

### 源代码控制和版本控制

- **将逻辑应用定义存储在源代码管理中**（Git、Azure DevOps、GitHub）
- **使用 ARM 模板**部署到多个环境
- **实施适合您的发布节奏的分支策略**
- **使用标签或版本属性对逻辑应用进行版本控制**

### 自动化部署

- **使用 Azure DevOps 管道**或 GitHub Actions 进行自动化部署
- **针对特定于环境的值实施参数化**
- **使用部署槽**进行零停机部署
- **在 CI/CD 管道中包含部署后验证**测试

```yaml
# Example Azure DevOps YAML pipeline for Logic App deployment
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

同时使用 Azure 逻辑应用和 Power Automate 时：

- **导出/导入兼容性**：可以从 Power Automate 导出流并导入到逻辑应用中，但可能需要进行一些修改
- **连接器差异**：某些连接器在一个平台上可用，但在另一个平台上不可用
- **环境隔离**：Power Automate 环境提供隔离并可能具有不同的策略
- **ALM 实践**：考虑将 Azure DevOps 用于 Power Automate 的逻辑应用和解决方案

### 迁移策略

- **评估**：评估迁移的复杂性和适用性
- **连接器映射**：映射平台之间的连接器并识别间隙
- **测试策略**：割接前实施并行测试
- **文档**：记录所有配置更改以供参考

```json
// Example Power Platform solution structure for Power Automate flows
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
            // Actions would be defined here
          }
        }
      }
    }
  ]
}
```

## 实用逻辑应用示例

### 具有 API 集成的 HTTP 请求处理程序

此示例演示一个逻辑应用，它接受 HTTP 请求、验证输入数据、调用外部 API、转换响应并返回格式化结果。

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

### 具有错误处理功能的事件驱动流程

此示例演示了一个逻辑应用程序，该逻辑应用程序处理来自 Azure 服务总线的事件，通过强大的错误处理来处理消息，并实现重试模式以实现弹性。

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

实施多层异常处理方法以实现稳健的工作流程：

1. **预防措施**：
   - 对所有传入消息使用模式验证
   - 使用 `coalesce()` 和 `?` 运算符实现防御性表达式求值
   - 在关键操作之前添加前置条件检查

2. **运行时错误处理**：
   - 使用带有嵌套 try/catch 模式的结构化错误处理范围
   - 为外部依赖项实现断路器模式
   - 以不同的方式捕获和处理特定的错误类型

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

3. **集中错误记录**：
   - 创建一个专用逻辑应用程序用于其他工作流可以调用的错误处理
   - 使用相关 ID 记录错误，以实现跨系统的可追溯性
   - 按类型和严重性对错误进行分类，以便更好地分析

### 先进的监控架构

实施全面的监测策略，其中包括：

1. **运行监控**：
   - **运行状况探针**：创建专用的运行状况检查工作流程
   - **心跳模式**：实施定期检查以验证系统运行状况
   - **死信处理**：处理和分析失败的消息

2. **业务流程监控**：
   - **业务指标**：跟踪关键业务 KPI（订单处理时间、批准率）
   - **SLA 监控**：根据服务级别协议衡量性能
   - **相关追踪**：实施端到端交易追踪

3. **警报策略**：
   - **多渠道警报**：将警报配置到适当的渠道（电子邮件、短信、团队）
   - **基于严重性的路由**：根据业务影响路由警报
   - **警报关联**：对相关警报进行分组，以防止警报疲劳

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

## API管理集成

将逻辑应用与 Azure API 管理集成以增强安全性、治理和管理：

### API管理前端

- **通过 API 管理公开逻辑应用程序**：
  - 为逻辑应用 HTTP 触发器创建 API 定义
  - 应用一致的 URL 结构和版本控制
  - 实施 API 政策以实现安全和转型

### 逻辑应用的策略模板

```xml
<!-- Logic App API Policy Example -->
<policies>
  <inbound>
    <!-- Authentication -->
    <validate-jwt header-name="Authorization" failed-validation-httpcode="401" failed-validation-error-message="Unauthorized">
      <openid-config url="https://login.microsoftonline.com/{tenant-id}/.well-known/openid-configuration" />
      <required-claims>
        <claim name="aud" match="any">
          <value>api://mylogicapp</value>
        </claim>
      </required-claims>
    </validate-jwt>
    
    <!-- Rate limiting -->
    <rate-limit calls="5" renewal-period="60" />
    
    <!-- Request transformation -->
    <set-header name="Correlation-Id" exists-action="override">
      <value>@(context.RequestId)</value>
    </set-header>
    
    <!-- Logging -->
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
    <!-- Response transformation -->
    <set-header name="X-Powered-By" exists-action="delete" />
  </outbound>
  <on-error>
    <base />
  </on-error>
</policies>
```

### 工作流作为 API 模式

- **将工作流程实施为 API 模式**：
  - 专门将逻辑应用程序设计为 API 后端
  - 将请求触发器与 OpenAPI 架构结合使用
  - 应用一致的响应模式
  - 实施正确的状态代码和错误处理

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
            "description": "The unique identifier for the customer"
          },
          "requestType": {
            "type": "string",
            "enum": ["Profile", "OrderSummary"],
            "description": "The type of request to process"
          }
        },
        "required": ["customerId", "requestType"]
      },
      "method": "POST"
    }
  }
}
```

## 版本控制策略

为逻辑应用和 Power Automate 流程实施强大的版本控制方法：

### 版本控制模式

1. **URI 路径版本控制**：
   - 在 HTTP 触发器路径 (/api/v1/resource) 中包含版本
   - 为每个主要版本维护单独的逻辑应用

2. **参数版本控制**：
   - 将版本参数添加到工作流定义中
   - 使用基于版本参数的条件逻辑

3. **并行版本控制**：
   - 将新版本与现有版本一起部署
   - 实现版本之间的流量路由

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

### 不同版本ARM模板部署

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "logicAppName": {
      "type": "string",
      "metadata": {
        "description": "Base name of the Logic App"
      }
    },
    "version": {
      "type": "string",
      "metadata": {
        "description": "Version of the Logic App to deploy"
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

实施策略来优化逻辑应用和 Power Automate 解决方案的成本：

### 逻辑应用消耗优化

1. **触发优化**：
   - 在触发器中使用批处理在一次运行中处理多个项目
   - 实施适当的重复间隔（避免过度轮询）
   - 使用基于 Webhook 的触发器而不是轮询触发器

2. **动作优化**：
   - 通过组合相关操作来减少操作数量
   - 使用内置函数而不是自定义操作
   - 为 foreach 循环实施适当的并发设置

3. **数据传输优化**：
   - 最小化 HTTP 请求/响应中的负载大小
   - 使用本地文件操作而不是重复的API调用
   - 对大负载实施数据压缩

### 逻辑应用标准（工作流）成本优化

1. **应用程序服务计划选择**：
   - 适合工作负载需求的应用服务计划
   - 根据负载模式实现自动缩放
   - 考虑为可预测的工作负载保留实例

2. **资源共享**：
   - 整合共享应用服务计划中的工作流程
   - 实施共享连接和集成资源
   - 有效使用集成账户

### 电源自动化许可优化

1. **许可证类型选择**：
   - 根据工作流程复杂性选择合适的许可证类型
   - 为每用户计划实施正确的用户分配
   - 考虑高级连接器的使用要求

2. **API 调用减少**：
   - 缓存经常访问的数据
   - 实现多条记录的批处理
   - 降低计划流的触发频率

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

## 增强的安全实践

为逻辑应用和 Power Automate 工作流程实施全面的安全措施：

### 敏感数据处理

1. **数据分类和保护**：
   - 识别工作流程中的敏感数据并对其进行分类
   - 对日志和监控中的敏感数据实施屏蔽
   - 对静态和传输中的数据应用加密

2. **安全参数处理**：
   - 使用 Azure Key Vault 保存所有机密和凭据
   - 在运行时实现动态参数解析
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
   - 实施逻辑应用管理的自定义角色
   - 对连接应用最小权限原则
   - 对所有 Azure 服务访问使用托管标识

2. **访问审查和治理**：
   - 对逻辑应用资源实施定期访问审查
   - 对管理操作应用即时访问
   - 审核所有访问和配置更改

3. **网络安全**：
   - 使用专用端点实施网络隔离
   - 对触发端点应用 IP 限制
   - 使用逻辑应用标准的虚拟网络集成

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

- [Azure 逻辑应用文档](https://docs.microsoft.com/en-us/azure/logic-apps/)
- [Power Automate 文档](https://docs.microsoft.com/en-us/power-automate/)
- [工作流定义语言架构](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-workflow-definition-language)
- [Power Automate 与逻辑应用比较](https://docs.microsoft.com/en-us/azure/azure-functions/functions-compare-logic-apps-ms-flow-webjobs)
- [企业集成模式](https://docs.microsoft.com/en-us/azure/logic-apps/enterprise-integration-overview)
- [逻辑应用 B2B 文档](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-enterprise-integration-b2b)
- [Azure 逻辑应用限制和配置](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-limits-and-config)
- [逻辑应用性能优化](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-performance-optimization)
- [逻辑应用安全概述](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-securing-a-logic-app)
- [API 管理和逻辑应用集成](https://docs.microsoft.com/en-us/azure/api-management/api-management-create-api-logic-app)
- [逻辑应用标准网络](https://docs.microsoft.com/en-us/azure/logic-apps/connect-virtual-network-vnet-isolated-environment)
