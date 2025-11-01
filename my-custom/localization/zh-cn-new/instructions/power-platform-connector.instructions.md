---
title: Power Platform 连接器架构开发指令
description: '使用 JSON 架构定义的 Power Platform 自定义连接器综合开发指南。涵盖 API 定义 (Swagger 2.0)、API 属性和带有 Microsoft 扩展的设置配置。'
applyTo: '**/*.{json,md}'
---

# Power Platform 连接器架构开发指令

## 项目概述
此工作空间包含 Power Platform 自定义连接器的 JSON 架构定义，专门用于 `paconn`（Power Apps 连接器）工具。这些架构为以下内容提供验证和 IntelliSense：

- **API 定义**（Swagger 2.0 格式）
- **API 属性**（连接器元数据和配置）
- **设置**（环境和部署配置）

## 文件结构理解

### 1. apiDefinition.swagger.json
- **目的**：此文件包含带有 Power Platform 扩展的 Swagger 2.0 API 定义。
- **主要特性**：
  - 标准 Swagger 2.0 属性，包括 info、paths、definitions 等。
  - 以 `x-ms-*` 前缀开头的 Microsoft 特定扩展。
  - 专为 Power Platform 设计的自定义格式类型，如 `date-no-tz` 和 `html`。
  - 提供运行时灵活性的动态架构支持。
  - 支持 OAuth2、API 密钥和基本身份验证方法的安全定义。

### 2. apiProperties.json
- **目的**：此文件定义连接器元数据、身份验证配置和策略配置。
- **关键组件**：
  - **连接参数**：支持各种身份验证类型，包括 OAuth、API 密钥和网关配置。
  - **策略模板实例**：处理连接器的数据转换和路由策略。
  - **连接器元数据**：包括发布者信息、功能和品牌元素。

### 3. settings.json
- **目的**：此文件为 paconn 工具提供环境和部署配置设置。
- **配置选项**：
  - 针对特定 Power Platform 环境的环境 GUID 定位。
  - 连接器资源和配置文件的文件路径映射。
  - 生产和测试环境（PROD/TIP1）的 API 端点 URL。
  - API 版本规范以确保与 Power Platform 服务的兼容性。

## 开发指南

### 处理 API 定义时（Swagger）
1. **始终根据 Swagger 2.0 规范验证** - 架构强制执行严格的 Swagger 2.0 合规性

2. **操作的 Microsoft 扩展**：
   - `x-ms-summary`：使用此功能提供用户友好的显示名称，确保使用标题格式。
   - `x-ms-visibility`：使用此功能通过 `important`、`advanced` 或 `internal` 值控制参数可见性。
   - `x-ms-trigger`：使用此功能通过 `batch` 或 `single` 值将操作标记为触发器。
   - `x-ms-trigger-hint`：使用此功能提供有用的提示文本，指导用户使用触发器。
   - `x-ms-trigger-metadata`：使用此功能定义触发器配置设置，包括 kind 和 mode 属性。
   - `x-ms-notification`：使用此功能配置 webhook 操作以进行实时通知。
   - `x-ms-pageable`：使用此功能通过指定 `nextLinkName` 属性启用分页功能。
   - `x-ms-safe-operation`：使用此功能将没有副作用的 POST 操作标记为安全。
   - `x-ms-no-generic-test`：使用此功能禁用特定操作的自动测试。
   - `x-ms-operation-context`：使用此功能配置操作模拟设置以进行测试。

3. **参数的 Microsoft 扩展**：
   - `x-ms-dynamic-list`：使用此功能启用从 API 调用填充的动态下拉列表。
   - `x-ms-dynamic-values`：使用此功能配置填充参数选项的动态值源。
   - `x-ms-dynamic-tree`：使用此功能为嵌套数据结构创建分层选择器。
   - `x-ms-dynamic-schema`：使用此功能允许基于用户选择进行运行时架构更改。
   - `x-ms-dynamic-properties`：使用此功能进行适应上下文的动态属性配置。
   - `x-ms-enum-values`：使用此功能提供增强的枚举定义和显示名称以获得更好的用户体验。
   - `x-ms-test-value`：使用此功能提供测试样本值，但绝不要包含机密或敏感数据。
   - `x-ms-trigger-value`：使用此功能为带有 `value-collection` 和 `value-path` 属性的触发器参数指定值。
   - `x-ms-url-encoding`：使用此功能将 URL 编码样式指定为 `single` 或 `double`（默认为 `single`）。
   - `x-ms-parameter-location`：使用此功能为 API 提供参数位置提示（AutoRest 扩展 - Power Platform 忽略）。
   - `x-ms-localizeDefaultValue`：使用此功能为默认参数值启用本地化。
   - `x-ms-skip-url-encoding`：使用此功能跳过路径参数的 URL 编码（AutoRest 扩展 - Power Platform 忽略）。

4. **架构的 Microsoft 扩展**：
   - `x-ms-notification-url`：使用此功能将架构属性标记为 webhook 配置的通知 URL。
   - `x-ms-media-kind`：使用此功能指定内容的媒体类型，支持的值为 `image` 或 `audio`。
   - `x-ms-enum`：使用此功能提供增强的枚举元数据（AutoRest 扩展 - Power Platform 忽略）。
   - 注意，上面列出的所有参数扩展也适用于架构属性，可以在架构定义中使用。

5. **根级扩展**：
   - `x-ms-capabilities`：使用此功能定义连接器功能，如文件选择器和 testConnection 功能。
   - `x-ms-connector-metadata`：使用此功能提供除标准属性之外的额外连接器元数据。
   - `x-ms-docs`：使用此功能配置连接器的文档设置和引用。
   - `x-ms-deployment-version`：使用此功能跟踪版本信息以进行部署管理。
   - `x-ms-api-annotation`：使用此功能添加 API 级注释以增强功能。

6. **路径级扩展**：
   - `x-ms-notification-content`：使用此功能为 webhook 路径项定义通知内容架构。

7. **操作级功能**：
   - `x-ms-capabilities`（在操作级别）：使用此功能启用操作特定功能，如用于大文件传输的 `chunkTransfer`。

8. **安全注意事项**：
   - 您应该为 API 定义适当的 `securityDefinitions` 以确保正确的身份验证。
   - **允许多个安全定义** - 您可以定义最多两种身份验证方法（例如，oauth2 + apiKey，basic + apiKey）。
   - **例外**：如果使用"无"身份验证，则同一连接器中不能存在其他安全定义。
   - 您应该对现代 API 使用 `oauth2`，对简单令牌身份验证使用 `apiKey`，仅对内部/遗留系统考虑 `basic` 身份验证。
   - 每个安全定义必须只是一种类型（此约束由 oneOf 验证强制执行）。

9. **参数最佳实践**：
   - 您应该使用描述性的 `description` 字段来帮助用户理解每个参数的用途。
   - 您应该实现 `x-ms-summary` 以获得更好的用户体验（需要标题格式）。
   - 您必须正确标记必需参数以确保适当的验证。
   - 您应该使用适当的 `format` 值（包括 Power Platform 扩展）以启用正确的数据处理。
   - 您应该利用动态扩展以获得更好的用户体验和数据验证。

10. **Power Platform 格式扩展**：
    - `date-no-tz`：表示没有时间偏移信息的日期时间。
    - `html`：此格式告诉客户端在编辑时发出 HTML 编辑器，在查看内容时发出 HTML 查看器。
    - 标准格式包括：`int32`、`int64`、`float`、`double`、`byte`、`binary`、`date`、`date-time`、`password`、`email`、`uri`、`uuid`。

### 处理 API 属性时
1. **连接参数**：
   - 您应该选择适当的参数类型，如 `string`、`securestring` 或 `oauthSetting`。
   - 您应该使用正确的身份提供者配置 OAuth 设置。
   - 您应该在适当时对下拉选项使用 `allowedValues`。
   - 您应该在需要时为条件参数实现参数依赖关系。

2. **策略模板**：
   - 您应该使用 `routerequesttoendpoint` 进行到不同 API 端点的后端路由。
   - 您应该实现 `setqueryparameter` 为查询参数设置默认值。
   - 您应该使用 `updatenextlink` 处理分页场景以正确处理分页。
   - 您应该对需要轮询行为的触发器操作应用 `pollingtrigger`。

3. **品牌和元数据**：
   - 您必须始终指定 `iconBrandColor`，因为此属性是所有连接器所必需的。
   - 您应该定义适当的 `capabilities` 以指定连接器是否支持操作或触发器。
   - 您应该设置有意义的 `publisher` 和 `stackOwner` 值以标识连接器的所有权。

### 处理设置时
1. **环境配置**：
   - 您应该为 `environment` 使用与验证模式匹配的正确 GUID 格式。
   - 您应该为目标环境设置正确的 `powerAppsUrl` 和 `flowUrl`。
   - 您应该将 API 版本匹配到您的特定要求。

2. **文件引用**：
   - 您应该保持与 `apiProperties.json` 和 `apiDefinition.swagger.json` 默认值一致的文件命名。
   - 您应该对本地开发环境使用相对路径。
   - 您应该确保图标文件存在并在配置中正确引用。

## 架构验证规则

### 必需属性
- **API 定义**：`swagger: "2.0"`、`info`（包含 `title` 和 `version`）、`paths`
- **API 属性**：带有 `iconBrandColor` 的 `properties`
- **设置**：无必需属性（全部可选，具有默认值）

### 模式验证
- **供应商扩展**：非 Microsoft 扩展必须匹配 `^x-(?!ms-)` 模式
- **路径项**：API 路径必须以 `/` 开头
- **环境 GUID**：必须匹配 UUID 格式模式 `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

### 类型约束
- **安全定义**：
  - `securityDefinitions` 对象中最多允许两个安全定义
  - 每个单独的安全定义必须只是一种类型（oneOf 验证：`basic`、`apiKey`、`oauth2`）
  - **例外**："无"身份验证不能与其他安全定义共存
- **参数类型**：限制为特定枚举值（`string`、`number`、`integer`、`boolean`、`array`、`file`）
- **策略模板**：类型特定的参数要求
- **格式值**：包括 Power Platform 格式的扩展集
- **可见性值**：必须是 `important`、`advanced` 或 `internal` 之一
- **触发器类型**：必须是 `batch` 或 `single`

### 附加验证规则
- **$ref 引用**：应仅指向 `#/definitions/`、`#/parameters/` 或 `#/responses/`
- **路径参数**：必须标记为 `required: true`
- **信息对象**：描述应与标题不同
- **联系对象**：电子邮件必须是有效的电子邮件格式，URL 必须是有效的 URI
- **许可证对象**：名称是必需的，如果提供 URL 必须是有效的 URI
- **外部文档**：URL 是必需的，必须是有效的 URI
- **标签**：数组中必须有唯一的名称
- **方案**：必须是有效的 HTTP 方案（`http`、`https`、`ws`、`wss`）
- **MIME 类型**：在 `consumes` 和 `produces` 中必须遵循有效的 MIME 类型格式

## 常见模式和示例

### API 定义示例

#### 带有 Microsoft 扩展的基本操作
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

#### 触发器操作配置
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

#### 动态架构示例
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

#### 测试连接功能（注意：自定义连接器不支持）
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

#### 用于模拟的操作上下文
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

#### 多个安全定义示例
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

**注意**：最多可以有两个安全定义共存，但"无"身份验证不能与其他方法组合。

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

1. **使用 IntelliSense**：这些架构提供丰富的自动完成和验证功能，有助于开发过程。
2. **遵循命名约定**：为操作和参数使用描述性名称以提高代码可读性。
3. **实现错误处理**：定义适当的响应架构和错误代码以正确处理失败场景。
4. **彻底测试**：在部署前验证架构，以便在开发过程中及早发现问题。
5. **记录扩展**：为 Microsoft 特定扩展添加注释以便团队理解和未来维护。
6. **版本管理**：在 API 信息中使用语义版本控制来跟踪更改和兼容性。
7. **安全第一**：始终实施适当的身份验证机制以保护您的 API 端点。

## 故障排除

### 常见架构违规
- **缺少必需属性**：`swagger: "2.0"`、`info.title`、`info.version`、`paths`
- **无效模式格式**：
  - GUID 必须匹配精确格式 `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
  - URL 必须是带有适当方案的有效 URI
  - 路径必须以 `/` 开头
  - 主机不得包含协议、路径或空格
- **不正确的供应商扩展命名**：对 Microsoft 扩展使用 `x-ms-*`，对其他扩展使用 `^x-(?!ms-)`
- **安全定义类型不匹配**：每个安全定义必须只是一种类型
- **无效枚举值**：检查 `x-ms-visibility`、`x-ms-trigger`、参数类型的允许值
- **$ref 指向无效位置**：必须指向 `#/definitions/`、`#/parameters/` 或 `#/responses/`
- **路径参数未标记为必需**：所有路径参数必须具有 `required: true`
- **类型 'file' 在错误上下文中**：仅允许在 `formData` 参数中，不允许在架构中

### API 定义特定问题
- **动态架构冲突**：不能将 `x-ms-dynamic-schema` 与固定架构属性一起使用
- **触发器配置错误**：`x-ms-trigger-metadata` 需要同时具有 `kind` 和 `mode`
- **分页设置**：`x-ms-pageable` 需要 `nextLinkName` 属性
- **文件选择器配置错误**：必须同时包含 `open` 操作和必需属性
- **功能冲突**：某些功能可能与某些参数类型冲突
- **测试值安全**：绝不要在 `x-ms-test-value` 中包含机密或 PII
- **操作上下文设置**：`x-ms-operation-context` 需要带有 `operationId` 的 `simulate` 对象
- **通知内容架构**：路径级 `x-ms-notification-content` 必须定义适当的架构结构
- **媒体种类限制**：`x-ms-media-kind` 仅支持 `image` 或 `audio` 值
- **触发器值配置**：`x-ms-trigger-value` 必须至少有一个属性（`value-collection` 或 `value-path`）

### 验证工具
- 使用 JSON 架构验证器检查架构定义是否符合规范。
- 利用 VS Code 的内置架构验证在开发过程中捕获错误。
- 在部署前使用 paconn CLI 测试：`paconn validate --api-def apiDefinition.swagger.json`
- 根据 Power Platform 连接器要求进行验证以确保兼容性。
- 使用 Power Platform 连接器门户在目标环境中进行验证和测试。
- 检查操作响应是否与预期架构匹配以防止运行时错误。

记住：这些架构确保您的 Power Platform 连接器格式正确，并且将在 Power Platform 生态系统中正常工作。