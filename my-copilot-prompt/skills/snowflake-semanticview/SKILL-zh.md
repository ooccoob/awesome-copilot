---
名称： 雪花语义视图
描述：使用 Snowflake CLI (snow) 创建、更改和验证 Snowflake 语义视图。当要求使用 CREATE/ALTER SEMANTIC VIEW 构建语义视图/语义层定义或对其进行故障排除时使用，通过 CLI 针对 Snowflake 验证语义视图 DDL，或指导 Snowflake CLI 安装和连接设置。
---

# 雪花语义视图

## 一次性设置

- 通过打开新终端并运行 `snow --help` 来验证 Snowflake CLI 安装。
- 如果 Snowflake CLI 丢失或用户无法安装，请引导他们访问 https://docs.snowflake.com/en/developer-guide/snowflake-cli/installation/installation。
- 根据 https://docs.snowflake.com/en/developer-guide/snowflake-cli/connecting/configure-connections#add-a-connection 配置 Snowflake 连接。
- 将配置的连接用于所有验证和执行步骤。

## 每个语义视图请求的工作流程

1. 确认目标数据库、模式、角色、仓库和最终语义视图名称。
2. 确认模型遵循星型模式（具有一致维度的事实）。
3. 使用官方语法起草语义视图DDL：
   - https://docs.snowflake.com/en/sql-reference/sql/create-semantic-view
4. 填充每个维度、事实和指标的同义词和注释：
   - 首先阅读 Snowflake 表/视图/列注释（首选来源）：
     - https://docs.snowflake.com/en/sql-reference/sql/comment
   - 如果缺少注释或同义词，请询问您是否可以创建它们，用户是否想要提供文本，或者您是否应该起草建议以供批准。
5. 使用带有 DISTINCT 和 LIMIT（最多 1000 行）的 SELECT 语句来发现事实表和维度表之间的关系，识别列数据类型，并为列创建更有意义的注释和同义词。
6. 创建临时验证名称（例如，附加 `__tmp_validate`），同时保留相同的数据库和架构。
7. 在最终确定之前，始终通过 Snowflake CLI 将 DDL 发送到 Snowflake 进行验证：
   - 使用 `snow sql` 通过配置的连接执行语句。
   - 如果标志因版本而异，请检查 `snow sql --help` 并使用此处显示的连接选项。
8. 如果验证失败，则迭代 DDL 并重新运行验证步骤，直到成功。
9. 使用真实语义视图名称应用最终的 DDL（创建或更改）。
10. 针对最终语义视图运行示例查询以确认其按预期工作。它具有不同的 SQL 语法，如下所示：https://docs.snowflake.com/en/user-guide/views-semantic/querying#querying-a-semantic-view
示例：

```SQL
SELECT * FROM SEMANTIC_VIEW(
    my_semview_name
    DIMENSIONS customer.customer_market_segment
    METRICS orders.order_average_value
)
ORDER BY customer_market_segment;
```

11. 清理验证期间创建的任何临时语义视图。

## 同义词和注释（必填）

- 对同义词和注释使用语义视图语法：

```
WITH SYNONYMS [ = ] ( 'synonym' [ , ... ] )
COMMENT = 'comment_about_dim_fact_or_metric'
```

- 将同义词视为仅供参考；不要使用它们来引用其他地方的维度、事实或指标。
- 使用 Snowflake 注释作为同义词和注释的首选和第一个来源：
  - https://docs.snowflake.com/en/sql-reference/sql/comment
- 如果缺少雪花评论，请询问您是否可以创建它们，用户是否想要提供文本，或者您是否应该起草建议以供批准。
- 未经用户批准，请勿发明同义词或注释。

## 验证模式（必填）

- 切勿跳过验证。在将其呈现为最终版本之前，始终使用 Snowflake CLI 针对 Snowflake 执行 DDL。
- 最好使用临时名称进行验证，以避免破坏真实视图。

## CLI 验证示例（模板）

```bash
# Replace placeholders with real values.
snow sql -q "<CREATE OR ALTER SEMANTIC VIEW ...>" --connection <connection_name>
```

如果 CLI 在您的版本中使用不同的连接标志，请运行：

```bash
snow sql --help
```

## 注释

- 将安装和连接设置视为一次性步骤，但请确认它们在第一次验证之前已完成。
- 保持最终语义视图定义与已验证的临时定义相同（名称除外）。
- 不要省略同义词或注释；即使它们在语法上是可选的，也应考虑完整性所必需的。
