---
标题：电源平台连接器架构开发说明
描述：'使用 JSON 架构定义的 Power Platform 自定义连接器的综合开发指南。涵盖 API 定义 (Swagger 2.0)、API 属性和 Microsoft 扩展的设置配置。
applyTo: '**/*.{json,md}'
---

# 电源平台连接器架构开发说明

## 项目概况
此工作区包含 Power Platform 自定义连接器的 JSON 架构定义，特别是针对 `paconn` (Power Apps 连接器) 工具。该架构验证并提供 IntelliSense：

- **API 定义**（Swagger 2.0 格式）
- **API 属性**（连接器元数据和配置）
- **设置**（环境和部署配置）

## 文件结构理解

### 1. apiDefinition.swagger.json
- **用途**：此文件包含带有 Power Platform 扩展的 Swagger 2.0 API 定义。
- **主要特点**：
  - 标准 Swagger 2.0 属性，包括信息、路径、定义等。
  - 以 `x-ms-*` 前缀开头的 Microsoft 特定扩展。
  - 专为 Power Platform 设计的自定义格式类型，例如 `date-no-tz` 和 `html`。
  - 动态模式支持提供运行时灵活性。
  - 支持 OAuth2、API Key 和 Basic Auth 身份验证方法的安全定义。

### 2. apiProperties.json
- **用途**：此文件定义连接器元数据、身份验证配置和策略配置。
- **关键组件**：
  - **连接参数**：这些支持各种身份验证类型，包括 OAuth、API 密钥和网关配置。
  - **策略模板实例**：这些实例处理连接器的数据转换和路由策略。
  - **连接器元数据**：这包括发布商信息、功能和品牌元素。

### 3.设置.json
- **用途**：该文件提供 paconn 工具的环境和部署配置设置。
- **配置选项**：
  - 针对特定 Power Platform 环境的环境 GUID。
  - 连接器资产和配置文件的文件路径映射。
  - 生产和测试环境 (PROD/TIP1) 的 API 端点 URL。
  - API 版本规范，以确保与 Power Platform 服务的兼容性。

## 开发指南

### 使用 API 定义时 (Swagger)
1. **始终根据 Swagger 2.0 规范进行验证** - 该架构强制执行严格的 Swagger 2.0 合规性

2. **Microsoft 操作扩展**：
   - `x-ms-summary`：使用它来提供用户友好的显示名称并确保您使用标题大小写格式。
   - `x-ms-visibility`：使用它来控制值为 `important`、`advanced` 或 `internal` 的参数可见性。
   - `x-ms-trigger`：使用它来将操作标记为值为 `batch` 或 `single` 的触发器。
   - `x-ms-trigger-hint`：使用它来提供有用的提示文本，指导用户使用触发器。
   - `x-ms-trigger-metadata`：使用它来定义触发器配置设置，包括种类和模式属性。
   - `x-ms-notification`：使用它来配置实时通知的 Webhook 操作。
   - `x-ms-pageable`：通过指定 `nextLinkName` 属性，使用它来启用分页功能。
   - `x-ms-safe-operation`：当 POST 操作没有副作用时，使用此标记将其标记为安全。
   - `x-ms-no-generic-test`：使用它来禁用特定操作的自动测试。
   - `x-ms-operation-context`：使用它来配置用于测试目的的操作模拟设置。

3. **Microsoft 参数扩展**：
   - `x-ms-dynamic-list`：使用它来启用从 API 调用填充的动态下拉列表。
   - `x-ms-dynamic-values`：使用它来配置填充参数选项的动态值源。
   - `x-ms-dynamic-tree`：使用它为嵌套数据结构创建分层选择器。
   - `x-ms-dynamic-schema`：使用它允许运行时架构根据用户选择进行更改。
   - `x-ms-dynamic-properties`：使用它来适应上下文的动态属性配置。
   - `x-ms-enum-values`：使用它来提供增强的枚举定义和显示名称，以获得更好的用户体验。
   - `x-ms-test-value`：使用它来提供用于测试的示例值，但切勿包含机密或敏感数据。
   - `x-ms-trigger-value`：使用它专门为具有 `value-collection` 和 `value-path` 属性的触发器参数指定值。
   - `x-ms-url-encoding`：使用它将 URL 编码样式指定为 `single` 或 `double`（默认为 `single`）。
   - `x-ms-parameter-location`：使用它为 API 提供参数位置提示（AutoRest 扩展 - 被 Power Platform 忽略）。
   - `x-ms-localizeDefaultValue`：使用它来启用默认参数值的本地化。
   - `x-ms-skip-url-encoding`：使用它可以跳过路径参数的 URL 编码（AutoRest 扩展 - 被 Power Platform 忽略）。

4. **微软架构扩展**：
   - `x-ms-notification-url`：使用它将架构属性标记为 Webhook 配置的通知 URL。
   - `x-ms-media-kind`：使用它来指定内容的媒体类型，支持的值为 `image` 或 `audio`。
   - `x-ms-enum`：使用它来提供增强的枚举元数据（AutoRest 扩展 - 被 Power Platform 忽略）。
   - 请注意，上面列出的所有参数扩展也适用于模式属性，并且可以在模式定义中使用。

5. **根级扩展**：
   - `x-ms-capabilities`：使用它来定义连接器功能，例如文件选择器和 testConnection 功能。
   - `x-ms-connector-metadata`：使用它来提供标准属性之外的其他连接器元数据。
   - `x-ms-docs`：使用它来配置连接器的文档设置和参考。
   - `x-ms-deployment-version`：使用它来跟踪部署管理的版本信息。
   - `x-ms-api-annotation`：使用它来添加 API 级注释以增强功能。

6. **路径级扩展**：
   - `x-ms-notification-content`：使用它来定义 Webhook 路径项的通知内容架构。

7. **操作级能力**：
   - `x-ms-capabilities`（在操作级别）：使用它来启用特定于操作的功能，例如用于大文件传输的 `chunkTransfer`。

8. **安全考虑**：
   - 您应该为您的 API 定义适当的 `securityDefinitions` 以确保正确的身份验证。
   - **允许多个安全定义** - 您最多可以定义两个身份验证方法（例如，oauth2 + apiKey、basic + apiKey）。
   - **例外**：如果使用“无”身份验证，则同一连接器中不能存在其他安全定义。
   - 您应该对现代 API 使用 `oauth2`，对简单令牌身份验证使用 `apiKey`，并仅针对内部/旧系统考虑使用 `basic` 身份验证。
   - 每个安全定义必须恰好是一种类型（此约束由 oneOf 验证强制执行）。

9. **参数最佳实践**：
   - 您应该使用描述性 `description` 字段来帮助用户理解每个参数的用途。
   - 您应该实现 `x-ms-summary` 以获得更好的用户体验（需要标题大小写）。
   - 您必须正确标记所需参数以确保正确验证。
   - 您应该使用适当的 `format` 值（包括 Power Platform 扩展）来启用正确的数据处理。
   - 您应该利用动态扩展来获得更好的用户体验和数据验证。

10. **Power Platform 格式扩展**：
   - `date-no-tz`：这表示没有时间偏移信息的日期时间。
   - `html`：此格式告诉客户端在编辑时发出 HTML 编辑器，在查看内容时发出 HTML 查看器。
   - 标准格式包括：`int32`、`int64`、`float`、`double`、`byte`、`binary`、`date`、`date-time`、`password`、`email`、`uri`、`uuid`。

### 使用 API 属性时
1. **连接参数**：
   - 您应该选择适当的参数类型，例如 `string`、`securestring` 或 `oauthSetting`。
   - 您应该使用正确的身份提供商配置 OAuth 设置。
   - 在适当的情况下，您应该使用 `allowedValues` 作为下拉选项。
   - 您应该在需要条件参数时实现参数依赖关系。

2. **政策模板**：
   - 您应该使用 `routerequesttoendpoint` 进行到不同 API 端点的后端路由。
   - 您应该实现 `setqueryparameter` 来设置查询参数的默认值。
   - 您应该在分页场景中使用 `updatenextlink` 来正确处理分页。
   - 您应该为需要轮询行为的触发器操作应用 `pollingtrigger`。

3. **品牌和元数据**：
   - 您必须始终指定 `iconBrandColor`，因为所有连接器都需要此属性。
   - 您应该定义适当的 `capabilities` 来指定您的连接器是否支持操作或触发器。
   - 您应该设置有意义的 `publisher` 和 `stackOwner` 值来标识连接器的所有权。

### 使用设置时
1. **环境配置**：
   - 您应该为 `environment` 使用与验证模式匹配的正确 GUID 格式。
   - 您应该为您的目标环境设置正确的 `powerAppsUrl` 和 `flowUrl` 。
   - 您应该将 API 版本与您的具体要求相匹配。

2. **文件参考**：
   - 您应该保持与默认值 `apiProperties.json` 和 `apiDefinition.swagger.json` 一致的文件命名。
   - 您应该对本地开发环境使用相对路径。
   - 您应该确保图标文件存在并且在您的配置中正确引用。

## 模式验证规则

### 所需属性
- **API 定义**：`swagger: "2.0"`、`info`（带有 `title` 和 `version`）、`paths`
- **API 属性**：`properties` 和 `iconBrandColor`
- **设置**：没有必需的属性（所有属性都是可选的，默认值）

### 模式验证
- **供应商扩展**：必须与非 Microsoft 扩展的 `^x-(?!ms-)` 模式匹配
- **路径项**：API 路径必须以 `/` 开头
- **环境 GUID**：必须与 UUID 格式模式 `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` 匹配
- **URL**：必须是端点配置的有效 URI
- **主机模式**：必须匹配 `^[^{}/ :\\\\]+(?::\\d+)?$` （无空格、协议或路径）

### 类型约束
- **安全定义**：
  - `securityDefinitions` 对象中最多允许两个安全定义
  - 每个单独的安全定义必须恰好是一种类型（oneOf 验证：`basic`、`apiKey`、`oauth2`）
  - **例外**：“无”身份验证不能与其他安全定义共存
- **参数类型**：仅限于特定枚举值（`string`、`number`、`integer`、`boolean`、`array`、`file`）
- **策略模板**：特定于类型的参数要求
- **格式值**：包括 Power Platform 格式的扩展集
- **可见性值**：必须是 `important`、`advanced` 或 `internal` 之一
- **触发器类型**：必须是 `batch` 或 `single`

### 附加验证规则
- **$ref 引用**：应仅指向 `#/definitions/`、`#/parameters/` 或 `#/responses/`
- **路径参数**：必须标记为 `required: true`
- **信息对象**：描述应与标题不同
- **联系对象**：电子邮件必须是有效的电子邮件格式，URL 必须是有效的 URI
- **许可证对象**：名称为必填项，URL 必须是有效的 URI（如果提供）
- **外部文档**：URL 为必填项，并且必须是有效的 URI
- **标签**：数组中必须具有唯一的名称
- **方案**：必须是有效的 HTTP 方案（`http`、`https`、`ws`、`wss`）
- **MIME 类型**：必须遵循 `consumes` 和 `produces` 中的有效 MIME 类型格式

## 常见模式和示例

### API定义示例

#### Microsoft 扩展的基本操作
```json
{
  "get": {
    "operationId": "GetItems",
    "summary": "Get items",
    "x-ms-summary": "Get Items",
    "x-ms-visibility": "important",
    "description": "Retrieves a list of items from the API",
    "parameters": [
      {
        "name": "category",
        "in": "query",
        "type": "string",
        "x-ms-summary": "Category",
        "x-ms-visibility": "important",
        "x-ms-dynamic-values": {
          "operationId": "GetCategories",
          "value-path": "id",
          "value-title": "name"
        }
      }
    ],
    "responses": {
      "200": {
        "description": "Success",
        "x-ms-summary": "Success",
        "schema": {
          "type": "object",
          "properties": {
            "items": {
              "type": "array",
              "x-ms-summary": "Items",
              "items": {
                "$ref": "#/definitions/Item"
              }
            }
          }
        }
      }
    }
  }
}
```

#### 触发操作配置
```json
{
  "get": {
    "operationId": "WhenItemCreated",
    "x-ms-summary": "When an Item is Created",
    "x-ms-trigger": "batch",
    "x-ms-trigger-hint": "To see it work now, create an item",
    "x-ms-trigger-metadata": {
      "kind": "query",
      "mode": "polling"
    },
    "x-ms-pageable": {
      "nextLinkName": "@odata.nextLink"
    }
  }
}
```

#### 动态模式示例
```json
{
  "name": "dynamicSchema",
  "in": "body",
  "schema": {
    "x-ms-dynamic-schema": {
      "operationId": "GetSchema",
      "parameters": {
        "table": {
          "parameter": "table"
        }
      },
      "value-path": "schema"
    }
  }
}
```

#### 文件选择器功能
```json
{
  "x-ms-capabilities": {
    "file-picker": {
      "open": {
        "operationId": "OneDriveFilePickerOpen",
        "parameters": {
          "dataset": {
            "value-property": "dataset"
          }
        }
      },
      "browse": {
        "operationId": "OneDriveFilePickerBrowse",
        "parameters": {
          "dataset": {
            "value-property": "dataset"
          }
        }
      },
      "value-title": "DisplayName",
      "value-collection": "value",
      "value-folder-property": "IsFolder",
      "value-media-property": "MediaType"
    }
  }
}
```

#### 测试连接能力（注意：不支持自定义连接器）
```json
{
  "x-ms-capabilities": {
    "testConnection": {
      "operationId": "TestConnection",
      "parameters": {
        "param1": "literal-value"
      }
    }
  }
}
```

#### 模拟操作上下文
```json
{
  "x-ms-operation-context": {
    "simulate": {
      "operationId": "SimulateOperation",
      "parameters": {
        "param1": {
          "parameter": "inputParam"
        }
      }
    }
  }
}
```

### 基本 OAuth 配置
```json
{
  "type": "oauthSetting",
  "oAuthSettings": {
    "identityProvider": "oauth2",
    "clientId": "your-client-id",
    "scopes": ["scope1", "scope2"],
    "redirectMode": "Global"
  }
}
```

#### 多重安全定义示例
```json
{
  "securityDefinitions": {
    "oauth2": {
      "type": "oauth2",
      "flow": "accessCode",
      "authorizationUrl": "https://api.example.com/oauth/authorize",
      "tokenUrl": "https://api.example.com/oauth/token",
      "scopes": {
        "read": "Read access",
        "write": "Write access"
      }
    },
    "apiKey": {
      "type": "apiKey",
      "name": "X-API-Key",
      "in": "header"
    }
  }
}
```

**注意**：最多可以共存两个安全定义，但“无”身份验证不能与其他方法结合使用。

### 动态参数设置
```json
{
  "x-ms-dynamic-values": {
    "operationId": "GetItems",
    "value-path": "id",
    "value-title": "name"
  }
}
```

### 路由策略模板
```json
{
  "templateId": "routerequesttoendpoint",
  "title": "Route to backend",
  "parameters": {
    "x-ms-apimTemplate-operationName": ["GetData"],
    "x-ms-apimTemplateParameter.newPath": "/api/v2/data"
  }
}
```

## 最佳实践

1. **使用 IntelliSense**：这些架构提供了丰富的自动完成和验证功能，可在开发过程中提供帮助。
2. **遵循命名约定**：对操作和参数使用描述性名称以提高代码可读性。
3. **实施错误处理**：定义适当的响应模式和错误代码以正确处理故障场景。
4. **彻底测试**：在部署之前验证架构，以便在开发过程的早期发现问题。
5. **文档扩展**：注释 Microsoft 特定的扩展，以便团队理解和未来维护。
6. **版本管理**：使用 API 信息中的语义版本控制来跟踪更改和兼容性。
7. **安全第一**：始终实施适当的身份验证机制来保护您的 API 端点。

## 故障排除

### 常见的架构违规
- **缺少必需的属性**：`swagger: "2.0"`、`info.title`、`info.version`、`paths`
- **无效的模式格式**：
  - GUID 必须与精确格式 `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` 匹配
  - URL 必须是具有正确方案的有效 URI
  - 路径必须以 `/` 开头
  - 主机不得包含协议、路径或空格
- **不正确的供应商扩展命名**：对于 Microsoft 扩展使用 `x-ms-*`，对于其他扩展使用 `^x-(?!ms-)`
- **不匹配的安全定义类型**：每个安全定义必须恰好是一种类型
- **无效的枚举值**：检查 `x-ms-visibility`、`x-ms-trigger`、参数类型的允许值
- **$ref 指向无效位置**：必须指向 `#/definitions/`、`#/parameters/` 或 `#/responses/`
- **路径参数未标记为必填**：所有路径参数必须具有 `required: true`
- **在错误的上下文中键入“文件”**：仅允许在 `formData` 参数中使用，不允许在模式中使用

### API 定义特定问题
- **动态架构冲突**：无法将 `x-ms-dynamic-schema` 与固定架构属性一起使用
- **触发配置错误**：`x-ms-trigger-metadata` 需要 `kind` 和 `mode`
- **分页设置**：`x-ms-pageable` 需要 `nextLinkName` 属性
- **文件选择器配置错误**：必须包含 `open` 操作和所需属性
- **功能冲突**：某些功能可能与某些参数类型冲突
- **测试值安全性**：切勿在 `x-ms-test-value` 中包含机密或 PII
- **操作上下文设置**：`x-ms-operation-context` 需要一个带有 `operationId` 的 `simulate` 对象
- **通知内容架构**：路径级别 `x-ms-notification-content` 必须定义正确的架构结构
- **媒体种类限制**：`x-ms-media-kind` 仅支持 `image` 或 `audio` 值
- **触发值配置**：`x-ms-trigger-value` 必须至少有一个属性（`value-collection` 或 `value-path`）

### 验证工具
- 使用 JSON 架构验证器检查架构定义的合规性。
- 利用 VS Code 的内置架构验证来捕获开发过程中的错误。
- 在部署之前使用 paconn CLI 进行测试：`paconn validate --api-def apiDefinition.swagger.json`
- 根据 Power Platform 连接器要求进行验证以确保兼容性。
- 使用 Power Platform 连接器门户在目标环境中进行验证和测试。
- 检查操作响应是否与预期模式匹配，以防止运行时错误。

请记住：这些架构可确保您的 Power Platform 连接器格式正确，并且可以在 Power Platform 生态系统中正常工作。
