---
模式：“代理”
工具：['更改'、'搜索/代码库'、'编辑/编辑文件'、'问题']
描述：“使用适当的路由、参数和自适应卡将 GET、POST、PATCH 和 DELETE 操作添加到 TypeSpec API 插件”
型号：'gpt-4.1'
标签：[typespec、m365-copilot、api 插件、休息操作、crud]
---

# 添加 TypeSpec API 操作

将 RESTful 操作添加到 Microsoft 365 Copilot 的现有 TypeSpec API 插件。

## 添加 GET 操作

### 简单 GET - 列出所有项目
```typescript
/**
 * List all items.
 */
@route("/items")
@get op listItems(): Item[];
```

### 带查询参数的 GET - 过滤结果
```typescript
/**
 * List items filtered by criteria.
 * @param userId Optional user ID to filter items
 */
@route("/items")
@get op listItems(@query userId?: integer): Item[];
```

### 带路径参数的 GET - 获取单个项目
```typescript
/**
 * Get a specific item by ID.
 * @param id The ID of the item to retrieve
 */
@route("/items/{id}")
@get op getItem(@path id: integer): Item;
```

### 使用自适应卡获取
```typescript
/**
 * List items with adaptive card visualization.
 */
@route("/items")
@card(#{
  dataPath: "$",
  title: "$.title",
  file: "item-card.json"
})
@get op listItems(): Item[];
```

**创建自适应卡** (`appPackage/item-card.json`)：
```json
{
  "type": "AdaptiveCard",
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.5",
  "body": [
    {
      "type": "Container",
      "$data": "${$root}",
      "items": [
        {
          "type": "TextBlock",
          "text": "**${if(title, title, 'N/A')}**",
          "wrap": true
        },
        {
          "type": "TextBlock",
          "text": "${if(description, description, 'N/A')}",
          "wrap": true
        }
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.OpenUrl",
      "title": "View Details",
      "url": "https://example.com/items/${id}"
    }
  ]
}
```

## 添加 POST 操作

### 简单的 POST - 创建项目
```typescript
/**
 * Create a new item.
 * @param item The item to create
 */
@route("/items")
@post op createItem(@body item: CreateItemRequest): Item;

model CreateItemRequest {
  title: string;
  description?: string;
  userId: integer;
}
```

### 发布并确认
```typescript
/**
 * Create a new item with confirmation.
 */
@route("/items")
@post
@capabilities(#{
  confirmation: #{
    type: "AdaptiveCard",
    title: "Create Item",
    body: """
    Are you sure you want to create this item?
      * **Title**: {{ function.parameters.item.title }}
      * **User ID**: {{ function.parameters.item.userId }}
    """
  }
})
op createItem(@body item: CreateItemRequest): Item;
```

## 添加 PATCH 操作

### 简单补丁 - 更新项目
```typescript
/**
 * Update an existing item.
 * @param id The ID of the item to update
 * @param item The updated item data
 */
@route("/items/{id}")
@patch op updateItem(
  @path id: integer,
  @body item: UpdateItemRequest
): Item;

model UpdateItemRequest {
  title?: string;
  description?: string;
  status?: "active" | "completed" | "archived";
}
```

### 补丁并确认
```typescript
/**
 * Update an item with confirmation.
 */
@route("/items/{id}")
@patch
@capabilities(#{
  confirmation: #{
    type: "AdaptiveCard",
    title: "Update Item",
    body: """
    Updating item #{{ function.parameters.id }}:
      * **Title**: {{ function.parameters.item.title }}
      * **Status**: {{ function.parameters.item.status }}
    """
  }
})
op updateItem(
  @path id: integer,
  @body item: UpdateItemRequest
): Item;
```

## 添加删除操作

### 简单删除
```typescript
/**
 * Delete an item.
 * @param id The ID of the item to delete
 */
@route("/items/{id}")
@delete op deleteItem(@path id: integer): void;
```

### 确认删除
```typescript
/**
 * Delete an item with confirmation.
 */
@route("/items/{id}")
@delete
@capabilities(#{
  confirmation: #{
    type: "AdaptiveCard",
    title: "Delete Item",
    body: """
    ⚠️ Are you sure you want to delete item #{{ function.parameters.id }}?
    This action cannot be undone.
    """
  }
})
op deleteItem(@path id: integer): void;
```

## 完整的 CRUD 示例

### 定义服务和模型
```typescript
@service
@server("https://api.example.com")
@actions(#{
  nameForHuman: "Items API",
  descriptionForHuman: "Manage items",
  descriptionForModel: "Read, create, update, and delete items"
})
namespace ItemsAPI {
  
  // Models
  model Item {
    @visibility(Lifecycle.Read)
    id: integer;
    
    userId: integer;
    title: string;
    description?: string;
    status: "active" | "completed" | "archived";
    
    @format("date-time")
    createdAt: utcDateTime;
    
    @format("date-time")
    updatedAt?: utcDateTime;
  }

  model CreateItemRequest {
    userId: integer;
    title: string;
    description?: string;
  }

  model UpdateItemRequest {
    title?: string;
    description?: string;
    status?: "active" | "completed" | "archived";
  }

  // Operations
  @route("/items")
  @card(#{ dataPath: "$", title: "$.title", file: "item-card.json" })
  @get op listItems(@query userId?: integer): Item[];

  @route("/items/{id}")
  @card(#{ dataPath: "$", title: "$.title", file: "item-card.json" })
  @get op getItem(@path id: integer): Item;

  @route("/items")
  @post
  @capabilities(#{
    confirmation: #{
      type: "AdaptiveCard",
      title: "Create Item",
      body: "Creating: **{{ function.parameters.item.title }}**"
    }
  })
  op createItem(@body item: CreateItemRequest): Item;

  @route("/items/{id}")
  @patch
  @capabilities(#{
    confirmation: #{
      type: "AdaptiveCard",
      title: "Update Item",
      body: "Updating item #{{ function.parameters.id }}"
    }
  })
  op updateItem(@path id: integer, @body item: UpdateItemRequest): Item;

  @route("/items/{id}")
  @delete
  @capabilities(#{
    confirmation: #{
      type: "AdaptiveCard",
      title: "Delete Item",
      body: "⚠️ Delete item #{{ function.parameters.id }}?"
    }
  })
  op deleteItem(@path id: integer): void;
}
```

## 高级功能

### 多个查询参数
```typescript
@route("/items")
@get op listItems(
  @query userId?: integer,
  @query status?: "active" | "completed" | "archived",
  @query limit?: integer,
  @query offset?: integer
): ItemList;

model ItemList {
  items: Item[];
  total: integer;
  hasMore: boolean;
}
```

### 标头参数
```typescript
@route("/items")
@get op listItems(
  @header("X-API-Version") apiVersion?: string,
  @query userId?: integer
): Item[];
```

### 自定义响应模型
```typescript
@route("/items/{id}")
@delete op deleteItem(@path id: integer): DeleteResponse;

model DeleteResponse {
  success: boolean;
  message: string;
  deletedId: integer;
}
```

### 错误响应
```typescript
model ErrorResponse {
  error: {
    code: string;
    message: string;
    details?: string[];
  };
}

@route("/items/{id}")
@get op getItem(@path id: integer): Item | ErrorResponse;
```

## 测试提示

添加操作后，使用以下提示进行测试：

**获取操作：**
- “列出所有项目并将其显示在表格中”
- “显示用户 ID 1 的项目”
- “获取第42项的详细信息”

**邮政操作：**
- “为用户 1 创建一个标题为‘我的任务’的新项目”
- “添加项目：标题‘新功能’，描述‘添加登录’”

**补丁操作：**
- “将第 10 项更新为标题‘更新的标题’”
- “将第 5 项的状态更改为已完成”

**删除操作：**
- “删除第99项”
- “删除 ID 为 15 的项目”

## 最佳实践

### 参数命名
- 使用描述性参数名称：`userId` 而不是 `uid`
- 跨操作保持一致
- 对过滤器使用可选参数 (`?`)

### 文档
- 为所有操作添加 JSDoc 注释
- 描述每个参数的作用
- 记录预期的反应

### 型号
- 将 `@visibility(Lifecycle.Read)` 用于只读字段，例如 `id`
- 对日期字段使用 `@format("date-time")`
- 对枚举使用联合类型：`"active" | "completed"`
- 使用 `?` 使可选字段显式化

### 确认信息
- 始终为破坏性操作添加确认（DELETE、PATCH）
- 在确认正文中显示关键详细信息
- 使用警告表情符号 (⚠️) 进行不可逆转的操作

### 自适应卡
- 保持卡片简单且重点突出
- 使用条件渲染与 `${if(..., ..., 'N/A')}`
- 包括常见后续步骤的操作按钮
- 测试数据与实际 API 响应的绑定

### 路由
- 使用 RESTful 约定：
  - `GET /items` - 列表
  - `GET /items/{id}` - 获取一个
  - `POST /items` - 创建
  - `PATCH /items/{id}` - 更新
  - `DELETE /items/{id}` - 删除
- 将相关操作分组到同一命名空间中
- 对分层资源使用嵌套路由

## 常见问题

### 问题：Copilot 中未显示参数
**解决方案**：检查参数是否用 `@query`、`@path` 或 `@body` 正确修饰

### 问题：自适应卡未渲染
**解决方案**：验证 `@card` 装饰器中的文件路径并检查 JSON 语法

### 问题：未出现确认信息
**解决方案**：确保 `@capabilities` 装饰器使用确认对象正确格式化

### 问题：模型属性未出现在响应中
**解决方案**：检查属性是否需要 `@visibility(Lifecycle.Read)` 或将其删除（如果它应该是可写的）
