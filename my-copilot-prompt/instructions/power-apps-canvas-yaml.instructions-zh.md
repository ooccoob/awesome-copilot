---
描述：“使用基于 Microsoft Power Apps YAML 架构 v3.0 的 Power Apps Canvas Apps YAML 结构的综合指南。涵盖 Power Fx 公式、控制结构、数据类型和源代码控制最佳实践。
applyTo: '**/*.{yaml,yml,md,pa.yaml}'
---

# Power Apps Canvas Apps YAML 结构指南

## 概述
本文档根据官方 Microsoft Power Apps YAML 架构 (v3.0) 和 Power Fx 文档，提供有关使用 Power Apps 画布应用的 YAML 代码的全面说明。

**官方架构来源**：https://raw.githubusercontent.com/microsoft/PowerApps-Tooling/refs/heads/master/schemas/pa-yaml/v3.0/pa.schema.yaml

## Power Fx 设计原则
Power Fx 是整个 Power Apps 画布应用程序中使用的公式语言。它遵循以下核心原则：

### 设计原则
- **简单**：使用 Excel 公式中的熟悉概念
- **Excel 一致性**：与 Excel 公式语法和行为保持一致
- **声明式**：描述你想要什么，而不是如何实现它
- **功能性**：避免副作用；大多数函数都是纯函数
- **组合**：通过组合更简单的函数构建复杂的逻辑
- **强类型**：类型系统确保数据完整性
- **集成**：跨 Power Platform 无缝工作

### 语言哲学
Power Fx 提倡：
- 通过熟悉的类似 Excel 的公式进行低代码开发
- 当依赖关系发生变化时自动重新计算
- 具有编译时检查的类型安全
- 函数式编程模式

## 根结构
每个 Power Apps YAML 文件都遵循以下顶级结构：

```yaml
App:
  Properties:
    # App-level properties and formulas
    StartScreen: =Screen1

Screens:
  # Screen definitions

ComponentDefinitions:
  # Custom component definitions

DataSources:
  # Data source configurations

EditorState:
  # Editor metadata (screen order, etc.)
```

## 1. 应用程序部分
`App` 部分定义应用程序级属性和配置。

```yaml
App:
  Properties:
    StartScreen: =Screen1
    BackEnabled: =false
    # Other app properties with Power Fx formulas
```

### 要点：
- 包含应用程序范围的设置
- 属性使用 Power Fx 公式（前缀为 `=`）
- 通常指定 `StartScreen` 属性

## 2. 屏幕部分
将应用程序中的所有屏幕定义为无序地图。

```yaml
Screens:
  Screen1:
    Properties:
      # Screen properties
    Children:
      - Label1:
          Control: Label
          Properties:
            Text: ="Hello World"
            X: =10
            Y: =10
      - Button1:
          Control: Button
          Properties:
            Text: ="Click Me"
            X: =10
            Y: =100
```

### 屏幕结构：
- **属性**：屏幕级属性和公式
- **Children**：屏幕上的控件数组（按 z 索引排序）

### 控件定义格式：
```yaml
ControlName:
  Control: ControlType      # Required: Control type identifier
  Properties:
    PropertyName: =PowerFxFormula
  # Optional properties:
  Group: GroupName          # For organizing controls in Studio
  Variant: VariantName      # Control variant (affects default properties)
  MetadataKey: Key          # Metadata identifier for control
  Layout: LayoutName        # Layout configuration
  IsLocked: true/false      # Whether control is locked in editor
  Children: []              # For container controls (ordered by z-index)
```

### 控制版本控制：
您可以使用 `@` 运算符指定控件版本：
```yaml
MyButton:
  Control: Button@2.1.0     # Specific version
  Properties:
    Text: ="Click Me"

MyLabel:
  Control: Label            # Uses latest version by default
  Properties:
    Text: ="Hello World"
```

## 3. 控制类型

### 标准控制
常见的第一方控件包括：
- **基本控制**：`Label`、`Button`、`TextInput`、`HTMLText`
- **输入控件**：`Slider`、`Toggle`、`Checkbox`、`Radio`、`Dropdown`、`Combobox`、`DatePicker`、`ListBox`
- **显示控件**：`Image`、`Icon`、`Video`、`Audio`、`PDF viewer`、`Barcode scanner`
- **布局控件**：`Container`、`Rectangle`、`Circle`、`Gallery`、`DataTable`、`Form`
- **图表控件**：`Column chart`、`Line chart`、`Pie chart`
- **高级控制**：`Timer`、`Camera`、`Microphone`、`Add picture`、`Import`、`Export`

### 容器和布局控件
特别注意容器控件及其子控件：
```yaml
MyContainer:
  Control: Container
  Properties:
    Width: =300
    Height: =200
    Fill: =RGBA(240, 240, 240, 1)
  Children:
    - Label1:
        Control: Label
        Properties:
          Text: ="Inside Container"
          X: =10         # Relative to container
          Y: =10         # Relative to container
    - Button1:
        Control: Button
        Properties:
          Text: ="Container Button"
          X: =10
          Y: =50
```

### 定制组件
```yaml
MyCustomControl:
  Control: Component
  ComponentName: MyComponent
  Properties:
    X: =10
    Y: =10
    # Custom component properties
```

### 代码组件 (PCF)
```yaml
MyPCFControl:
  Control: CodeComponent
  ComponentName: publisherprefix_namespace.classname
  Properties:
    X: =10
    Y: =10
```

## 4. 组件定义
定义可重用的自定义组件：

```yaml
ComponentDefinitions:
  MyComponent:
    DefinitionType: CanvasComponent
    Description: "A reusable component"
    AllowCustomization: true
    AccessAppScope: false
    CustomProperties:
      InputText:
        PropertyKind: Input
        DataType: Text
        Description: "Input text property"
        Default: ="Default Value"
      OutputValue:
        PropertyKind: Output
        DataType: Number
        Description: "Output number value"
    Properties:
      Fill: =RGBA(255, 255, 255, 1)
      Height: =100
      Width: =200
    Children:
      - Label1:
          Control: Label
          Properties:
            Text: =Parent.InputText
```

### 自定义属性类型：
- **输入**：从父级接收值
- **输出**：将值发送给父级
- **InputFunction**：父级调用的函数
- **OutputFunction**：组件中定义的函数
- **事件**：向父级触发事件
- **操作**：有副作用的函数

### 数据类型：
- __代码0__、__代码1__、__代码2__
- __代码0__、__代码1__、__代码2__
- __代码0__、__代码1__、__代码2__
- __代码0__，__代码1__

## 5. 数据来源
配置数据连接：

```yaml
DataSources:
  MyTable:
    Type: Table
    Parameters:
      TableLogicalName: account

  MyActions:
    Type: Actions
    ConnectorId: shared_office365users
    Parameters:
      # Additional connector parameters
```

### 数据源类型：
- **表格**：Dataverse 表格或其他表格数据
- **操作**：连接器操作和流程

## 6. 编辑器状态
维护编辑组织：

```yaml
EditorState:
  ScreensOrder:
    - Screen1
    - Screen2
    - Screen3
  ComponentDefinitionsOrder:
    - MyComponent
    - AnotherComponent
```

## Power Fx 公式指南

### 公式语法：
- 所有公式必须以 `=` 开头
- 对表达式使用 Power Fx 语法
- 空值可以表示为 `null` （不带引号）
- 示例：
  ```yaml
  Text: ="Hello World"
  X: =10
  Visible: =Toggle1.Value
  OnSelect: =Navigate(Screen2, ScreenTransition.Fade)
  OptionalProperty: null    # Represents no value
  ```

### 常见的公式模式：
```yaml
# Static values
Text: ="Static Text"
X: =50
Visible: =true

# Control references
Text: =TextInput1.Text
Visible: =Toggle1.Value

# Parent references (for controls in containers/galleries)
Width: =Parent.Width - 20
Height: =Parent.TemplateHeight    # In gallery templates

# Functions
OnSelect: =Navigate(NextScreen, ScreenTransition.Slide)
Text: =Concatenate("Hello ", User().FullName)

# Conditional logic
Visible: =If(Toggle1.Value, true, false)
Fill: =If(Button1.Pressed, RGBA(255,0,0,1), RGBA(0,255,0,1))

# Data operations
Items: =Filter(DataSource, Status = "Active")
Text: =LookUp(Users, ID = 123).Name
```

### Z 索引和控制排序：
- `Children` 数组中的控件按 z 索引排序
- 数组中的第一个控件 = 底层（z-index 1）
- 数组中的最后一个控件 = 顶层（最高 z 索引）
- 所有控件都使用从 1 开始的升序

## 命名约定

### 实体名称：
- 屏幕名称：具有描述性且独特
- 控件名称：类型名称 + 数字（例如 `Button1`、`Label2`）
- 组件名称：PascalCase

### 属性名称：
- 标准属性：使用模式中的精确大小写
- 自定义属性：推荐 PascalCase

## 最佳实践

### 1、结构组织：
- 保持屏幕逻辑有序
- 使用 `Group` 属性对相关控件进行分组
- 为所有实体使用有意义的名称

### 2、公式书写：
- 保持公式可读且格式良好
- 尽可能在复杂的公式中使用注释
- 避免过于复杂的嵌套表达式

### 3. 组件设计：
- 设计可重复使用的组件
- 为自定义属性提供清晰的描述
- 使用适当的属性类型（输入/输出）

### 4、数据源管理：
- 对数据源使用描述性名称
- 文档连接要求
- 保持最少的数据源配置

## 验证规则

### 所需属性：
- 所有控件都必须具有 `Control` 属性
- 组件定义必须具有 `DefinitionType`
- 数据源必须具有 `Type`

### 命名模式：
- 实体名称：至少 1 个字符，字母数字
- 控制类型 ID：遵循模式 `^([A-Z][a-zA-Z0-9]*/)?[A-Z][a-zA-Z0-9]*(@\d+\.\d+\.\d+)?$`
- 代码组件名称：遵循模式 `^([a-z][a-z0-9]{1,7})_([a-zA-Z0-9]\.)+[a-zA-Z0-9]+$`

## 常见问题及解决方案

### 1. 无效的控件类型：
- 确保控件类型拼写正确
- 检查外壳是否正确
- 验证架构支持控件类型

### 2、公式错误：
- 所有公式必须以 `=` 开头
- 使用正确的 Power Fx 语法
- 检查正确的属性引用

### 3.结构验证：
- 保持正确的 YAML 缩进
- 确保存在所需的属性
- 严格遵循模式结构

### 4. 自定义组件问题：
- 验证 `ComponentName` 与定义匹配
- 确保正确定义自定义属性
- 检查财产种类是否合适
- 如果使用外部组件，请验证组件库引用

### 5. 性能考虑：
- 避免在 YAML 中深度嵌套公式
- 使用高效的数据源查询
- 考虑大型数据集的可委托公式
- 最大限度地减少频繁更新的属性中的复杂计算

## 高级主题

### 1. 组件库集成：
```yaml
ComponentDefinitions:
  MyLibraryComponent:
    DefinitionType: CanvasComponent
    AllowCustomization: true
    ComponentLibraryUniqueName: "pub_MyComponentLibrary"
    # Component definition details
```

### 2.响应式设计注意事项：
- 使用 `Parent.Width` 和 `Parent.Height` 进行响应式大小调整
- 考虑复杂 UI 的基于容器的布局
- 使用公式进行动态定位和调整大小

### 3.图库模板：
```yaml
MyGallery:
  Control: Gallery
  Properties:
    Items: =DataSource
    TemplateSize: =100
  Children:
    - GalleryTemplate:  # Template for each gallery item
        Children:
          - TitleLabel:
              Control: Label
              Properties:
                Text: =ThisItem.Title
                Width: =Parent.TemplateWidth - 20
```

### 4.表单控件和数据卡：
```yaml
MyForm:
  Control: Form
  Properties:
    DataSource: =DataSource
    DefaultMode: =FormMode.New
  Children:
    - DataCard1:
        Control: DataCard
        Properties:
          DataField: ="Title"
        Children:
          - DataCardValue1:
              Control: TextInput
              Properties:
                Default: =Parent.Default
```

### 5. 公式中的错误处理：
```yaml
Properties:
  Text: =IfError(LookUp(DataSource, ID = 123).Name, "Not Found")
  Visible: =!IsError(DataSource)
  OnSelect: =IfError(
    Navigate(DetailScreen, ScreenTransition.Cover),
    Notify("Navigation failed", NotificationType.Error)
  )
```

## Power Apps 源代码管理

### 访问源代码文件：
可以通过多种方法获取 Power Apps YAML 文件：

1. **Power 平台 CLI**：
   ```powershell
   # List canvas apps in environment
   pac canvas list

   # Download and extract YAML files
   pac canvas download --name "MyApp" --extract-to-directory "C:\path\to\destination"
   ```

2. **从 .msapp 手动提取**：
   ```powershell
   # Extract .msapp file using PowerShell
   Expand-Archive -Path "C:\path\to\yourFile.msapp" -DestinationPath "C:\path\to\destination"
   ```

3. **Dataverse Git 集成**：直接访问源文件，无需 .msapp 文件

### .msapp 中的文件结构：
- `\src\App.pa.yaml` - 代表主应用程序配置
- `\src\[ScreenName].pa.yaml` - 每个屏幕一个文件
- `\src\Component\[ComponentName].pa.yaml` - 组件定义

**重要说明**：
- 仅 `\src` 文件夹中的文件适用于源代码控制
- .pa.yaml 文件是**只读**且仅用于审核目的
- 不支持外部编辑、合并和冲突解决
- .msapp 中的 JSON 文件对于源代码控制不稳定

### 架构版本演变：
1. **实验格式** (*.fx.yaml)：不再开发
2. **早期预览**：临时格式，不再使用
3. **源代码** (*.pa.yaml)：支持版本控制的当前活动格式

## Power Fx 公式参考

### 公式类别：

#### **函数**：获取参数、执行操作、返回值
```yaml
Properties:
  Text: =Concatenate("Hello ", User().FullName)
  X: =Sum(10, 20, 30)
  Items: =Filter(DataSource, Status = "Active")
```

#### **Signals**：返回环境信息（无参数）
```yaml
Properties:
  Text: =Location.Latitude & ", " & Location.Longitude
  Visible: =Connection.Connected
  Color: =If(Acceleration.X > 5, Color.Red, Color.Blue)
```

#### **枚举**：预定义的常量值
```yaml
Properties:
  Fill: =Color.Blue
  Transition: =ScreenTransition.Fade
  Align: =Align.Center
```

#### **命名操作员**：访问容器信息
```yaml
Properties:
  Text: =ThisItem.Title        # In galleries
  Width: =Parent.Width - 20    # In containers
  Height: =Self.Height / 2     # Self-reference
```

### YAML 的基本 Power Fx 函数：

#### **导航和应用程序控制**：
```yaml
OnSelect: =Navigate(NextScreen, ScreenTransition.Cover)
OnSelect: =Back()
OnSelect: =Exit()
OnSelect: =Launch("https://example.com")
```

#### **数据操作**：
```yaml
Items: =Filter(DataSource, Category = "Active")
Text: =LookUp(Users, ID = 123).Name
OnSelect: =Patch(DataSource, ThisItem, {Status: "Complete"})
OnSelect: =Collect(LocalCollection, {Name: TextInput1.Text})
```

#### **条件逻辑**：
```yaml
Visible: =If(Toggle1.Value, true, false)
Text: =Switch(Status, "New", "🆕", "Complete", "✅", "❓")
Fill: =If(Value < 0, Color.Red, Color.Green)
```

#### **文本操作**：
```yaml
Text: =Concatenate("Hello ", User().FullName)
Text: =Upper(TextInput1.Text)
Text: =Substitute(Label1.Text, "old", "new")
Text: =Left(Title, 10) & "..."
```

#### **数学运算**：
```yaml
Text: =Sum(Sales[Amount])
Text: =Average(Ratings[Score])
Text: =Round(Calculation, 2)
Text: =Max(Values[Number])
```

#### **日期和时间函数**：
```yaml
Text: =Text(Now(), "mm/dd/yyyy")
Text: =DateDiff(StartDate, EndDate, Days)
Text: =Text(Today(), "dddd, mmmm dd, yyyy")
Visible: =IsToday(DueDate)
```

### 公式语法指南：

#### **基本语法规则**：
- 所有公式均以 `=` 开头
- 前面没有 `+` 或 `=` 符号（与 Excel 不同）
- 文本字符串的双引号：`="Hello World"`
- 属性参考：`ControlName.PropertyName`
- YAML 上下文中不支持注释

#### **公式元素**：
```yaml
# Literal values
Text: ="Static Text"
X: =42
Visible: =true

# Control property references
Text: =TextInput1.Text
Visible: =Checkbox1.Value

# Function calls
Text: =Upper(TextInput1.Text)
Items: =Sort(DataSource, Title)

# Complex expressions
Text: =If(IsBlank(TextInput1.Text), "Enter text", Upper(TextInput1.Text))
```

#### **行为与属性公式**：
```yaml
# Property formulas (calculate values)
Properties:
  Text: =Concatenate("Hello ", User().FullName)
  Visible: =Toggle1.Value

# Behavior formulas (perform actions - use semicolon for multiple actions)
Properties:
  OnSelect: =Set(MyVar, true); Navigate(NextScreen); Notify("Done!")
```

### 高级公式模式：

#### **使用集合**：
```yaml
Properties:
  Items: =Filter(MyCollection, Status = "Active")
  OnSelect: =ClearCollect(MyCollection, DataSource)
  OnSelect: =Collect(MyCollection, {Name: "New Item", Status: "Active"})
```

#### **错误处理**：
```yaml
Properties:
  Text: =IfError(Value(TextInput1.Text), 0)
  OnSelect: =IfError(
    Patch(DataSource, ThisItem, {Field: Value}),
    Notify("Error updating record", NotificationType.Error)
  )
```

#### **动态属性设置**：
```yaml
Properties:
  Fill: =ColorValue("#" & HexInput.Text)
  Height: =Parent.Height * (Slider1.Value / 100)
  X: =If(Alignment = "Center", (Parent.Width - Self.Width) / 2, 0)
```

## 使用公式最佳实践

### 公式组织：
- 将复杂的公式分解为更小的、可读的部分
- 使用变量来存储中间计算
- 使用描述性控件名称注释复杂逻辑
- 将相关计算分组在一起

### 性能优化：
- 处理大型数据集时使用委托友好的函数
- 避免在频繁更新的属性中嵌套函数调用
- 使用集合进行复杂的数据转换
- 最大限度地减少对外部数据源的调用

## Power Fx 数据类型和操作

### 数据类型类别：

#### **原始类型**：
- **布尔值**：`=true`、`=false`
- **数字**：`=123`、`=45.67`
- **文本**：`="Hello World"`
- **日期**：`=Date(2024, 12, 25)`
- **时间**：`=Time(14, 30, 0)`
- **日期时间**：`=Now()`

#### **复杂类型**：
- **颜色**：`=Color.Red`、`=RGBA(255, 128, 0, 1)`
- **记录**：`={Name: "John", Age: 30}`
- **表**：`=Table({Name: "John"}, {Name: "Jane"})`
- **GUID**：__代码0__

#### **类型转换**：
```yaml
Properties:
  Text: =Text(123.45, "#,##0.00")        # Number to text
  Text: =Value("123.45")                 # Text to number
  Text: =DateValue("12/25/2024")         # Text to date
  Visible: =Boolean("true")              # Text to boolean
```

#### **类型检查**：
```yaml
Properties:
  Visible: =Not(IsBlank(OptionalField))
  Visible: =Not(IsError(Value(TextInput1.Text)))
  Visible: =IsNumeric(TextInput1.Text)
```

### 表操作：

#### **创建表**：
```yaml
Properties:
  Items: =Table(
    {Name: "Product A", Price: 10.99},
    {Name: "Product B", Price: 15.99}
  )
  Items: =["Option 1", "Option 2", "Option 3"]  # Single-column table
```

#### **过滤和排序**：
```yaml
Properties:
  Items: =Filter(Products, Price > 10)
  Items: =Sort(Products, Name, Ascending)
  Items: =SortByColumns(Products, "Price", Descending, "Name", Ascending)
```

#### **数据转换**：
```yaml
Properties:
  Items: =AddColumns(Products, "Total", Price * Quantity)
  Items: =RenameColumns(Products, "Price", "Cost")
  Items: =ShowColumns(Products, "Name", "Price")
  Items: =DropColumns(Products, "InternalID")
```

#### **聚合**：
```yaml
Properties:
  Text: =Sum(Products, Price)
  Text: =Average(Products, Rating)
  Text: =Max(Products, Price)
  Text: =CountRows(Products)
```

### 变量和状态管理：

#### **全局变量**：
```yaml
Properties:
  OnSelect: =Set(MyGlobalVar, "Hello World")
  Text: =MyGlobalVar
```

#### **上下文变量**：
```yaml
Properties:
  OnSelect: =UpdateContext({LocalVar: "Screen Specific"})
  OnSelect: =Navigate(NextScreen, None, {PassedValue: 42})
```

#### **收藏**：
```yaml
Properties:
  OnSelect: =ClearCollect(MyCollection, DataSource)
  OnSelect: =Collect(MyCollection, {Name: "New Item"})
  Items: =MyCollection
```

## Power Fx 增强型连接器和外部数据

### 连接器集成：
```yaml
DataSources:
  SharePointList:
    Type: Table
    Parameters:
      TableLogicalName: "Custom List"

  Office365Users:
    Type: Actions
    ConnectorId: shared_office365users
```

### 使用外部数据：
```yaml
Properties:
  Items: =Filter(SharePointList, Status = "Active")
  OnSelect: =Office365Users.SearchUser({searchTerm: SearchInput.Text})
```

### 委派注意事项：
```yaml
Properties:
  # Delegable operations (executed server-side)
  Items: =Filter(LargeTable, Status = "Active")    # Efficient

  # Non-delegable operations (may download all records)
  Items: =Filter(LargeTable, Len(Description) > 100)  # Warning issued
```

## 故障排除和常见模式

### 常见错误模式：
```yaml
# Handle blank values
Properties:
  Text: =If(IsBlank(OptionalText), "Default", OptionalText)

# Handle errors gracefully
Properties:
  Text: =IfError(RiskyOperation(), "Fallback Value")

# Validate input
Properties:
  Visible: =And(
    Not(IsBlank(NameInput.Text)),
    IsNumeric(AgeInput.Text),
    IsMatch(EmailInput.Text, Email)
  )
```

### 性能优化：
```yaml
# Efficient data loading
Properties:
  Items: =Filter(LargeDataSource, Status = "Active")    # Server-side filtering

# Use delegation-friendly operations
Properties:
  Items: =Sort(Filter(DataSource, Active), Name)        # Delegable
  # Avoid: Sort(DataSource, If(Active, Name, ""))       # Not delegable
```

### 内存管理：
```yaml
# Clear unused collections
Properties:
  OnSelect: =Clear(TempCollection)

# Limit data retrieval
Properties:
  Items: =FirstN(Filter(DataSource, Status = "Active"), 50)
```

请记住：本指南全面介绍了 Power Apps Canvas Apps YAML 结构和 Power Fx 公式。始终根据 Power Apps Studio 环境中的官方架构和测试公式验证您的 YAML。
