````prompt
---
mode: 'agent'
tools: ['changes', 'search/codebase', 'edit/editFiles', 'problems']
description: 'Add Adaptive Card response templates to MCP-based API plugins for visual data presentation in Microsoft 365 Copilot'
model: 'gpt-4.1'
tags: [mcp, adaptive-cards, m365-copilot, api-plugin, response-templates]
---

# Create Adaptive Cards for MCP Plugins

Add Adaptive Card response templates to MCP-based API plugins to enhance how data is presented visually in Microsoft 365 Copilot.

## Adaptive Card Types

### Static Response Templates
Use when API always returns items of the same type and format doesn't change often.

Define in `response_semantics.static_template` in ai-plugin.json:

```json
{
  “功能”：[
    {
      "name": "获取预算",
      "description": "返回预算详细信息，包括名称和可用资金",
      “能力”：{
        “响应语义”：{
          “数据路径”：“$”，
          “属性”：{
            "标题": "$.name",
            "副标题": "$.availableFunds"
          },
          “静态模板”：{
            “类型”：“自适应卡”，
            “$schema”：“http://adaptivecards.io/schemas/adaptive-card.json”，
            “版本”：“1.5”，
            “身体”：[
              {
                “类型”：“容器”，
                "$data": "${$root}",
                “项目”：[
                  {
                    “类型”：“文本块”，
                    "text": "姓名：${if(name, name, 'N/A')}",
                    “换行”：正确
                  },
                  {
                    “类型”：“文本块”，
                    "text": "可用资金：${if(availableFunds, formatNumber(availableFunds, 2), 'N/A')}",
                    “换行”：正确
                  }
                ]
              }
            ]
          }
        }
      }
    }
  ]
}
```

### Dynamic Response Templates
Use when API returns multiple types and each item needs a different template.

**ai-plugin.json configuration:**
```json
{
  "name": "获取交易",
  "description": "使用动态模板返回交易详细信息",
  “能力”：{
    “响应语义”：{
      "data_path": "$.transactions",
      “属性”：{
        "template_selector": "$.displayTemplate"
      }
    }
  }
}
```

**API Response with Embedded Templates:**
```json
{
  “交易”：[
    {
      "budgetName": "第四咖啡大堂装修",
      “金额”：-2000，
      "description": "申请许可证所需的财产调查",
      "expenseCategory": "许可",
      "displayTemplate": "$.templates.debit"
    },
    {
      "budgetName": "第四咖啡大堂装修",
      “金额”：5000，
      "description": "额外资金以弥补成本超支",
      “费用类别”：空，
      "displayTemplate": "$.templates.credit"
    }
  ],
  “模板”：{
    “借方”：{
      “类型”：“自适应卡”，
      “版本”：“1.5”，
      “身体”：[
        {
          “类型”：“文本块”，
“尺寸”：“中”，
          “重量”：“更大胆”，
          “颜色”：“注意”，
          “文本”：“借方”
        },
        {
          “类型”：“事实集”，
          “事实”：[
            {
              "title": "预算",
              “值”：“${预算名称}”
            },
            {
              "title": "金额",
              "值": "${formatNumber(金额, 2)}"
            },
            {
              "标题": "类别",
              “价值”：“$ {if（费用类别，费用类别，'不适用'）}”
            },
            {
              "标题": "描述",
              "值": "${if(描述, 描述, 'N/A')}"
            }
          ]
        }
      ],
      “$schema”：“http://adaptivecards.io/schemas/adaptive-card.json”
    },
    “信用”：{
      “类型”：“自适应卡”，
      “版本”：“1.5”，
      “身体”：[
        {
          “类型”：“文本块”，
“尺寸”：“中”，
          “重量”：“更大胆”，
          “颜色”：“好”，
          “文本”：“信用”
        },
        {
          “类型”：“事实集”，
          “事实”：[
            {
              "title": "预算",
              “值”：“${预算名称}”
            },
            {
              "title": "金额",
              "值": "${formatNumber(金额, 2)}"
            },
            {
              "标题": "描述",
              "值": "${if(描述, 描述, 'N/A')}"
            }
          ]
        }
      ],
      “$schema”：“http://adaptivecards.io/schemas/adaptive-card.json”
    }
  }
}
```

### Combined Static and Dynamic Templates
Use static template as default when item doesn't have template_selector or when value doesn't resolve.

```json
{
  “能力”：{
    “响应语义”：{
      "data_path": "$.items",
      “属性”：{
        "标题": "$.name",
        "template_selector": "$.templateId"
      },
      “静态模板”：{
        “类型”：“自适应卡”，
        “版本”：“1.5”，
        “身体”：[
          {
            “类型”：“文本块”，
            "text": "默认值：${name}",
            “换行”：正确
          }
        ]
      }
    }
  }
}
```

## Response Semantics Properties

### data_path
JSONPath query indicating where data resides in API response:
```json
"data_path": "$" // 响应根
"data_path": "$.results" // 在结果属性中
"data_path": "$.data.items"//嵌套路径
```

### properties
Map response fields for Copilot citations:
```json
“属性”：{
  "title": "$.name", // 引文标题
  "subtitle": "$.description", // 引文副标题
  "url": "$.link" // 引用链接
}
```

### template_selector
Property on each item indicating which template to use:
```json
"template_selector": "$.displayTemplate"
```

## Adaptive Card Template Language

### Conditional Rendering
```json
{
  “类型”：“文本块”，
  "text": "${if(field, field, 'N/A')}" // 显示字段或 'N/A'
}
```

### Number Formatting
```json
{
  “类型”：“文本块”，
  "text": "${formatNumber(amount, 2)}" // 两位小数
}
```

### Data Binding
```json
{
  “类型”：“容器”，
  "$data": "${$root}", // 中断到根上下文
  “项目”：[...]
}
```

### Conditional Display
```json
{
  “类型”：“图像”，
  "url": "${imageUrl}",
  "$when": "${imageUrl != null}" // 仅显示 imageUrl 是否存在
}
```

## Card Elements

### TextBlock
```json
{
  “类型”：“文本块”，
  "text": "文本内容",
  "size": "medium", // 小、默认、中、大、超大
  "weight": "bolder", // 更轻，默认，更粗
  "color": "attention", // 默认、深色、浅色、重音、良好、警告、注意
  “换行”：正确
}
```

### FactSet
```json
{
  “类型”：“事实集”，
  “事实”：[
    {
      “标题”：“标签”，
      “价值”：“价值”
    }
  ]
}
```

### Image
```json
{
  “类型”：“图像”，
  "url": "https://example.com/image.png",
  "size": "medium", // 自动、拉伸、小、中、大
  "style": "default" // 默认，人物
}
```

### Container
```json
{
  “类型”：“容器”，
  "$data": "${items}", // 迭代数组
  “项目”：[
    {
      “类型”：“文本块”，
      “文本”：“${名称}”
    }
  ]
}
```

### ColumnSet
```json
{
  "type": "列集",
  “列”：[
    {
      “类型”：“列”，
      “宽度”：“自动”，
      “项目”：[...]
    },
    {
      “类型”：“列”，
      “宽度”：“拉伸”，
      “项目”：[...]
    }
  ]
}
```

### Actions
```json
{
  "type": "Action.OpenUrl",
  "title": "查看详情",
“url”：“https://example.com/item/${id}”
}
```

## Responsive Design Best Practices

### Single-Column Layouts
- Use single columns for narrow viewports
- Avoid multi-column layouts when possible
- Ensure cards work at minimum viewport width

### Flexible Widths
- Don't assign fixed widths to elements
- Use "auto" or "stretch" for width properties
- Allow elements to resize with viewport
- Fixed widths OK for icons/avatars only

### Text and Images
- Avoid placing text and images in same row
- Exception: Small icons or avatars
- Use "wrap": true for text content
- Test at various viewport widths

### Test Across Hubs
Validate cards in:
- Teams (desktop and mobile)
- Word
- PowerPoint
- Various viewport widths (contract/expand UI)

## Complete Example

**ai-plugin.json:**
```json
{
  “功能”：[
    {
      "name": "搜索项目",
      "description": "搜索具有状态和详细信息的项目",
      “能力”：{
        “响应语义”：{
          "data_path": "$.projects",
          “属性”：{
            "标题": "$.name",
            "副标题": "$.status",
            "url": "$.projectUrl"
          },
          “静态模板”：{
            “类型”：“自适应卡”，
            “$schema”：“http://adaptivecards.io/schemas/adaptive-card.json”，
            “版本”：“1.5”，
            “身体”：[
              {
                “类型”：“容器”，
                "$data": "${$root}",
                “项目”：[
                  {
                    “类型”：“文本块”，
                    “尺寸”：“中”，
                    “重量”：“更大胆”，
                    "text": "${if(name, name, '无标题项目')}",
                    “换行”：正确
                  },
                  {
                    “类型”：“事实集”，
                    “事实”：[
                      {
                        "标题": "状态",
                        “值”：“${状态}”
                      },
                      {
                        “标题”：“所有者”，
                        "value": "${if(所有者, 所有者, '未分配')}"
                      },
                      {
                        "title": "截止日期",
                        "value": "${if(dueDate, dueDate, '未设置')}"
                      },
                      {
                        "title": "预算",
                        "value": "${if(预算, formatNumber(预算, 2), 'N/A')}"
                      }
                    ]
                  },
                  {
                    “类型”：“文本块”，
                    "text": "${if(描述, 描述, '无描述')}",
                    “包裹”：真实，
                    “分隔符”：正确
                  }
                ]
              }
            ],
            “行动”：[
              {
                "type": "Action.OpenUrl",
                "title": "查看项目",
                "url": "${projectUrl}"
              }
            ]
          }
        }
      }
    }
  ]
}
```

## Workflow

Ask the user:
1. What type of data does the API return?
2. Are all items the same type (static) or different types (dynamic)?
3. What fields should appear in the card?
4. Should there be actions (e.g., "View Details")?
5. Are there multiple states or categories requiring different templates?

Then generate:
- Appropriate response_semantics configuration
- Static template, dynamic templates, or both
- Proper data binding with conditional rendering
- Responsive single-column layout
- Test scenarios for validation

## Resources

- [Adaptive Card Designer](https://adaptivecards.microsoft.com/designer) - Visual design tool
- [Adaptive Card Schema](https://adaptivecards.io/schemas/adaptive-card.json) - Full schema reference
- [Template Language](https://learn.microsoft.com/en-us/adaptive-cards/templating/language) - Binding syntax guide
- [JSONPath](https://www.rfc-editor.org/rfc/rfc9535) - Path query syntax

## Common Patterns

### List with Images
```json
{
  “类型”：“容器”，
  "$data": "${items}",
  “项目”：[
    {
      "type": "列集",
      “列”：[
        {
          “类型”：“列”，
          “宽度”：“自动”，
          “项目”：[
            {
              “类型”：“图像”，
              "url": "${thumbnailUrl}",
              “尺寸”：“小”，
              "$when": "${thumbnailUrl != null}"
            }
          ]
        },
        {
          “类型”：“列”，
          “宽度”：“拉伸”，
          “项目”：[
            {
              “类型”：“文本块”，
              "文本": "${标题}",
              “重量”：“更大胆”，
              “换行”：正确
            }
          ]
        }
      ]
    }
  ]
}
```

### Status Indicators
```json
{
  “类型”：“文本块”，
  "文本": "${状态}",
  "color": "${if(status == '已完成', '良好', if(status == '进行中', '注意', '默认'))}"
}
```

### Currency Formatting
```json
{
  “类型”：“文本块”，
  "text": "$${formatNumber(金额, 2)}"
}
```

````