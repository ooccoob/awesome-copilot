---
description: '基于 Microsoft 指导的 Power BI 数据建模最佳实践，用于使用星型模式原则创建高效、可扩展和可维护的语义模型。'
applyTo: '**/*.{pbix,md,json,txt}'
---

# Power BI 数据建模最佳实践

## 概述
本文档提供了基于 Microsoft 官方指导和维度建模最佳实践，设计高效、可扩展和可维护的 Power BI 语义模型的综合指导。

## 星型模式设计原则

### 1. 基本表类型
**维度表** - 存储描述性业务实体：
- 产品、客户、地理、时间、员工
- 包含唯一键列（最好是代理键）
- 相对较少的行数
- 用于过滤、分组和提供上下文
- 支持分层向下钻取场景

**事实表** - 存储可测量的业务事件：
- 销售交易、网站点击、制造事件
- 包含指向维度表的外键
- 用于聚合的数字度量
- 大量行数（通常随时间增长）
- 表示特定的粒度/详细级别

```
示例星型模式结构：

DimProduct (维度)          FactSales (事实)              DimCustomer (维度)
├── ProductKey (PK)             ├── SalesKey (PK)             ├── CustomerKey (PK)
├── ProductName                 ├── ProductKey (FK)           ├── CustomerName
├── Category                    ├── CustomerKey (FK)          ├── CustomerType
├── SubCategory                 ├── DateKey (FK)              ├── Region
└── UnitPrice                   ├── SalesAmount               └── RegistrationDate
                               ├── Quantity
DimDate (维度)             └── DiscountAmount
├── DateKey (PK)
├── Date
├── Year
├── Quarter
├── Month
└── DayOfWeek
```

### 2. 表设计最佳实践

#### 维度表设计
```
✅ 应该做：
- 使用代理键（自动递增整数）作为主键
- 包含业务键用于集成目的
- 创建分层属性（类别 > 子类别 > 产品）
- 使用描述性名称和适当的数据类型
- 为缺失维度数据包含"未知"记录
- 保持维度表相对窄（专注属性）

❌ 不应该做：
- 在大型模型中使用自然业务键作为主键
- 在同一表中混合事实和维度特征
- 创建不必要的宽维度表
- 对缺失值不做适当处理
```

#### 事实表设计
```
✅ 应该做：
- 以所需的最详细级别存储数据
- 使用与维度表键匹配的外键
- 仅包含数字、可测量的列
- 在所有事实表行中保持一致的粒度
- 使用适当的数据类型（货币使用小数，计数使用整数）

❌ 不应该做：
- 包含描述性文本列（这些属于维度）
- 在同一事实表中混合不同粒度
- 存储可以在查询时计算的计算值
- 使用组合键，当代理键更简单时
```

## 关系设计和管理

### 1. 关系类型和最佳实践

#### 一对多关系（标准模式）
```
配置：
- 从维度（一端）到事实（多端）
- 单向过滤（维度过滤事实）
- 对于 DirectQuery 性能，标记为"假设引用完整性"

示例：
DimProduct (1) ← ProductKey → (*) FactSales
DimCustomer (1) ← CustomerKey → (*) FactSales
DimDate (1) ← DateKey → (*) FactSales
```

#### 多对多关系（谨慎使用）
```
何时使用：
✅ 真正的多对多业务关系
✅ 当桥接表模式不可行时
✅ 用于高级分析场景

最佳实践：
- 在可能时创建显式桥接表
- 使用低基数关系列
- 仔细监控性能影响
- 清晰记录业务规则

带桥接表示例：
DimCustomer (1) ← CustomerKey → (*) BridgeCustomerAccount (*) ← AccountKey → (1) DimAccount
```

#### 一对一关系（罕见）
```
何时使用：
- 使用附加属性扩展维度表
- 退化维度场景
- 将 PII 与操作数据分离

实施：
- 如果可能，考虑合并到单个表中
- 用于安全/隐私分离
- 维护引用完整性
```

### 2. 关系配置指南
```
过滤方向：
✅ 单向：默认选择，最佳性能
✅ 双向：仅当业务逻辑需要交叉过滤时
❌ 避免：循环关系路径

交叉过滤方向：
- 维度到事实：始终单向
- 事实到事实：避免直接关系，使用共享维度
- 维度到维度：仅当业务逻辑需要时

引用完整性：
✅ 当数据质量有保证时，为 DirectQuery 源启用
✅ 通过使用 INNER JOIN 提高查询性能
❌ 如果源数据有孤立记录，则不要启用
```

## 存储模式优化

### 1. 导入模式最佳实践
```
何时使用导入模式：
✅ 数据大小符合容量限制
✅ 需要复杂的分析计算
✅ 具有稳定数据集的历史数据分析
✅ 需要最佳查询性能

优化策略：
- 移除不必要的列和行
- 使用适当的数据类型
- 在可能时预聚合数据
- 对大型数据集实施增量刷新
- 优化 Power Query 转换
```

#### 导入的数据减少技术
```
垂直过滤（列减少）：
✅ 移除报告中或关系中未使用的列
✅ 移除可以在 DAX 中计算的计算列
✅ 移除仅在 Power Query 中使用的中间列
✅ 优化数据类型（整数 vs 小数，日期 vs 日期时间）

水平过滤（行减少）：
✅ 过滤到相关时间段（例如，最近 3 年的数据）
✅ 过滤到相关业务实体（活跃客户、特定区域）
✅ 移除测试、无效或已取消的交易
✅ 实施适当的数据归档策略

数据类型优化：
文本 → 数字：尽可能将代码转换为整数
日期时间 → 日期：当不需要时间时使用日期类型
小数 → 整数：对整数度量使用整数
高精度 → 低精度：匹配业务需求
```

### 2. DirectQuery 模式最佳实践
```
何时使用 DirectQuery 模式：
✅ 数据超出导入容量限制
✅ 实时数据要求
✅ 安全/合规性要求数据保留在源
✅ 与操作系统集成

优化要求：
- 优化源数据库性能
- 在源表上创建适当的索引
- 最小化复杂的 DAX 计算
- 使用简单的度量和聚合
- 限制每个报表页面的可视化数量
- 实施查询减少技术
```

#### DirectQuery 性能优化
```
数据库优化：
✅ 在经常过滤的列上创建索引
✅ 在关系键列上创建索引
✅ 对复杂连接使用物化视图
✅ 实施适当的数据库维护
✅ 对分析工作负载考虑列存储索引

DirectQuery 的模型设计：
✅ 保持 DAX 度量简单
✅ 避免在大型表上创建计算列
✅ 严格使用星型模式设计
✅ 最小化跨表操作
✅ 在可能时在源中预聚合数据

查询性能：
✅ 在报表设计中尽早应用过滤器
✅ 使用适当的可视化类型
✅ 限制高基数过滤
✅ 监控和优化慢查询
```

### 3. 复合模型设计
```
何时使用复合模型：
✅ 结合历史（导入）与实时（DirectQuery）数据
✅ 使用附加数据源扩展现有模型
✅ 平衡性能与数据新鲜度要求
✅ 集成多个 DirectQuery 源

存储模式选择：
导入：小型维度表、历史聚合事实
DirectQuery：大型事实表、实时操作数据
Dual：需要与导入和 DirectQuery 事实一起工作的维度表
Hybrid：结合历史（导入）与最近（DirectQuery）数据的事实表
```

#### 双存储模式策略
```
对以下情况使用双模式：
✅ 与导入和 DirectQuery 事实相关的维度表
✅ 小型、缓慢变化的参考表
✅ 需要灵活查询的查找表

配置：
- 将维度表设置为双模式
- Power BI 自动选择最佳查询路径
- 维护维度数据的单一副本
- 启用高效的跨源关系
```

## 高级建模模式

### 1. 日期表设计
```
基本日期表属性：
✅ 连续日期范围（无间隔）
✅ 在 Power BI 中标记为日期表
✅ 包含标准层次结构（年 > 季度 > 月 > 日）
✅ 添加特定于业务的列（FiscalYear、WorkingDay、Holiday）
✅ 对日期列使用日期数据类型

日期表实施：
DateKey（整数）：20240315（YYYYMMDD 格式）
Date（日期）：2024-03-15
Year（整数）：2024
Quarter（文本）：Q1 2024
Month（文本）：2024 年 3 月
MonthNumber（整数）：3
DayOfWeek（文本）：星期五
IsWorkingDay（布尔值）：TRUE
FiscalYear（整数）：2024
FiscalQuarter（文本）：FY2024 Q3
```

### 2. 缓慢变化维度（SCD）
```
类型 1 SCD（覆盖）：
- 用新值更新现有记录
- 失去历史上下文
- 简单实施和维护
- 用于非关键属性更改

类型 2 SCD（历史保存）：
- 为更改创建新记录
- 维护完整历史
- 包含生效日期范围
- 使用代理键进行唯一标识

实施模式：
CustomerKey（代理）：1、2、3、4
CustomerID（业务）：101、101、102、103
CustomerName："John Doe"、"John Smith"、"Jane Doe"、"Bob Johnson"
EffectiveDate：2023-01-01、2024-01-01、2023-01-01、2023-01-01
ExpirationDate：2023-12-31、9999-12-31、9999-12-31、9999-12-31
IsCurrent：FALSE、TRUE、TRUE、TRUE
```

### 3. 角色扮演维度
```
场景：日期表用于订单日期、发货日期、交货日期

实施选项：

选项 1：多重关系（推荐）
- 具有到事实的多个关系的单一日期表
- 一个活动关系（订单日期）
- 发货日期和交货日期的非活动关系
- 在 DAX 度量中使用 USERELATIONSHIP

选项 2：多个日期表
- 分离表：OrderDate、ShipDate、DeliveryDate
- 每个都有专用关系
- 对报表作者更直观
- 由于重复，模型大小更大

DAX 实施：
按订单日期的销售额 = [总销售额]  // 使用活动关系
按发货日期的销售额 = CALCULATE([总销售额], USERELATIONSHIP(FactSales[ShipDate], DimDate[Date]))
按交货日期的销售额 = CALCULATE([总销售额], USERELATIONSHIP(FactSales[DeliveryDate], DimDate[Date]))
```

### 4. 多对多桥接表
```
场景：学生可以参加多个课程，课程可以有多个学生

桥接表设计：
DimStudent (1) ← StudentKey → (*) BridgeStudentCourse (*) ← CourseKey → (1) DimCourse

桥接表结构：
StudentCourseKey（PK）：代理键
StudentKey（FK）：引用 DimStudent
CourseKey（FK）：引用 DimCourse
EnrollmentDate：附加上下文
Grade：附加上下文
Status：Active、Completed、Dropped

关系配置：
- DimStudent 到 BridgeStudentCourse：一对多
- BridgeStudentCourse 到 DimCourse：多对一
- 将一个关系设置为双向以进行过滤器传播
- 从报表视图隐藏桥接表
```

## 性能优化策略

### 1. 模型大小优化
```
列优化：
✅ 完全移除未使用的列
✅ 使用最小的适当数据类型
✅ 将高基数文本转换为带查找表的整数
✅ 移除冗余的计算列

行优化：
✅ 过滤到业务相关时间段
✅ 移除无效、测试或已取消的交易
✅ 适当归档历史数据
✅ 对增长的数据集使用增量刷新

聚合策略：
✅ 预计算常见聚合
✅ 对高级报告使用汇总表
✅ 在 Premium 中实施自动聚合
✅ 对复杂分析要求考虑 OLAP 多维数据集
```

### 2. 关系性能
```
键选择：
✅ 整数键优于文本键
✅ 代理键优于自然键
✅ 确保源数据中的引用完整性
✅ 在键列上创建适当的索引

基数优化：
✅ 设置正确的关系基数
✅ 在适当时使用"假设引用完整性"
✅ 最小化双向关系
✅ 在可能时避免多对多关系

交叉过滤策略：
✅ 默认使用单向过滤
✅ 仅在需要时启用双向
✅ 测试交叉过滤的性能影响
✅ 记录双向关系的业务原因
```

### 3. 查询性能模式
```
高效模型模式：
✅ 适当的星型模式实施
✅ 规范化维度表
✅ 非规范化事实表
✅ 相关表间的一致粒度
✅ 适当使用计算表和列

查询优化：
✅ 预过滤大型数据集
✅ 为数据使用适当的可视化类型
✅ 最小化报告中的复杂 DAX
✅ 有效利用模型关系
✅ 对大型、实时数据集考虑 DirectQuery
```

## 安全和治理

### 1. 行级安全性（RLS）
```
实施模式：

基于用户的安全性：
[UserEmail] = USERPRINCIPALNAME()

基于角色的安全性：
VAR UserRole =
    LOOKUPVALUE(
        UserRoles[Role],
        UserRoles[Email],
        USERPRINCIPALNAME()
    )
RETURN
    Customers[Region] = UserRole

动态安全性：
LOOKUPVALUE(
    UserRegions[Region],
    UserRegions[Email],
    USERPRINCIPALNAME()
) = Customers[Region]

最佳实践：
✅ 使用不同用户帐户进行测试
✅ 保持安全逻辑简单和高性能
✅ 清晰记录安全要求
✅ 使用安全角色，而不是单个用户过滤器
✅ 考虑复杂 RLS 的性能影响
```

### 2. 数据治理
```
文档要求：
✅ 所有度量的业务定义
✅ 数据血缘和源系统映射
✅ 刷新计划和依赖项
✅ 安全和访问控制文档
✅ 变更管理程序

数据质量：
✅ 实施数据验证规则
✅ 监控数据完整性
✅ 适当处理缺失值
✅ 验证业务规则实施
✅ 定期数据质量评估

版本控制：
✅ Power BI 文件的源代码控制
✅ 环境推广程序
✅ 变更跟踪和批准流程
✅ 备份和恢复程序
```

## 测试和验证框架

### 1. 模型测试检查清单
```
功能测试：
□ 所有关系正常运行
□ 度量计算预期值
□ 过滤器适当传播
□ 安全规则按设计工作
□ 数据刷新成功完成

性能测试：
□ 模型在可接受时间内加载
□ 查询在 SLA 要求内执行
□ 可视化交互响应迅速
□ 内存使用在容量限制内
□ 并发用户负载测试完成

数据质量测试：
□ 没有缺失的外键关系
□ 度量总计与源系统匹配
□ 日期范围完整且连续
□ 安全过滤产生正确结果
□ 业务规则正确实施
```

### 2. 验证程序
```
业务验证：
✅ 与源系统比较报告总计
✅ 与业务用户验证复杂计算
✅ 测试边缘情况和边界条件
✅ 确认业务逻辑实施
✅ 验证不同过滤器下的报告准确性

技术验证：
✅ 使用真实数据量进行性能测试
✅ 并发用户测试
✅ 使用不同用户角色进行安全测试
✅ 数据刷新测试和监控
✅ 灾难恢复测试
```

## 要避免的常见反模式

### 1. 模式反模式
```
❌ 雪花模式（除非必要）：
- 多个规范化维度表
- 复杂的关系链
- 降低查询性能
- 对业务用户更复杂

❌ 单一大表：
- 混合事实和维度
- 极度非规范化
- 难以维护和扩展
- 分析查询性能差

❌ 具有直接关系的多个事实表：
- 事实间的多对多关系
- 复杂的过滤器传播
- 难以维护一致性
- 最好使用共享维度
```

### 2. 关系反模式
```
❌ 到处都是双向关系：
- 性能影响
- 不可预测的过滤器行为
- 维护复杂性
- 应该是例外，而不是规则

❌ 没有业务理由的多对多关系：
- 通常表示缺少维度
- 可能隐藏数据质量问题
- 复杂的调试和维护
- 桥接表通常是更好的解决方案

❌ 循环关系：
- 模糊的过滤器路径
- 不可预测的结果
- 调试困难
- 通过适当设计始终避免
```

## 高级数据建模模式

### 1. 缓慢变化维度实施
```powerquery
// 类型 1 SCD：基于哈希变更检测的 Power Query 实施
let
    Source = Source,

    #"添加自定义" = Table.TransformColumnTypes(
        Table.AddColumn(Source, "Hash", each Binary.ToText(
            Text.ToBinary(
                Text.Combine(
                    List.Transform({[FirstName],[LastName],[Region]}, each if _ = null then "" else _),
                "|")),
            BinaryEncoding.Hex)
        ),
        {{"Hash", type text}}
    ),

    #"标记键列" = Table.AddKey(#"添加自定义", {"Hash"}, false),

    #"合并查询" = Table.NestedJoin(
        #"标记键列",
        {"Hash"},
        ExistingDimRecords,
        {"Hash"},
        "ExistingDimRecords",
        JoinKind.LeftOuter
    ),

    #"展开 ExistingDimRecords" = Table.ExpandTableColumn(
        #"合并查询",
        "ExistingDimRecords",
        {"Count"},
        {"Count"}
    ),

    #"筛选行" = Table.SelectRows(#"展开 ExistingDimRecords", each ([Count] = null)),

    #"移除列" = Table.RemoveColumns(#"筛选行", {"Count"})
in
    #"移除列"
```

### 2. 具有查询折叠的增量刷新
```powerquery
// 优化的增量刷新模式
let
  Source = Sql.Database("server","database"),
  Data  = Source{[Schema="dbo",Item="FactInternetSales"]}[Data],
  FilteredByStart = Table.SelectRows(Data, each [OrderDateKey] >= Int32.From(DateTime.ToText(RangeStart,[Format="yyyyMMdd"]))),
  FilteredByEnd = Table.SelectRows(FilteredByStart, each [OrderDateKey] < Int32.From(DateTime.ToText(RangeEnd,[Format="yyyyMMdd"])))
in
  FilteredByEnd
```

### 3. 语义链接集成
```python
# 在 Python 中使用 Power BI 语义模型
import sempy.fabric as fabric
from sempy.relationships import plot_relationship_metadata

relationships = fabric.list_relationships("my_dataset")
plot_relationship_metadata(relationships)
```

### 4. 高级分区策略
```json
// 具有基于时间过滤的 TMSL 分区
"partition": {
      "name": "Sales2019",
      "mode": "import",
      "source": {
        "type": "m",
        "expression": [
          "let",
          "    Source = SqlDatabase,",
          "    dbo_Sales = Source{[Schema=\"dbo\",Item=\"Sales\"]}[Data],",
          "    FilteredRows = Table.SelectRows(dbo_Sales, each [OrderDateKey] >= 20190101 and [OrderDateKey] <= 20191231)",
          "in",
          "    FilteredRows"
        ]
      }
}
```

记住：始终与业务用户验证模型设计，并使用真实数据量和使用模式进行测试。使用 Power BI 的内置工具，如性能分析器和 DAX Studio 进行优化和调试。