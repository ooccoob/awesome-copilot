---
description: '基于 Microsoft Power Apps YAML 架构 v3.0 的 Power Apps 画布应用 YAML 结构综合指南。涵盖 Power Fx 公式、控件结构、数据类型和源代码控制最佳实践。'
applyTo: '**/*.{yaml,yml,md,pa.yaml}'
---

# Power Apps 画布应用 YAML 结构指南

## 概述
本文档提供了基于 Microsoft 官方 Power Apps YAML 架构 (v3.0) 和 Power Fx 文档的 Power Apps 画布应用 YAML 代码综合指令。

**官方架构源**: https://raw.githubusercontent.com/microsoft/PowerApps-Tooling/refs/heads/master/schemas/pa-yaml/v3.0/pa.schema.yaml

## Power Fx 设计原则
Power Fx 是 Power Apps 画布应用中使用的公式语言。它遵循这些核心原则：

### 设计原则
- **简单性**: 使用 Excel 公式中熟悉的概念
- **Excel 一致性**: 与 Excel 公式语法和行为保持一致
- **声明式**: 描述您想要什么，而不是如何实现它
- **函数式**: 避免副作用；大多数函数是纯函数
- **组合性**: 通过组合更简单的函数构建复杂逻辑
- **强类型**: 类型系统确保数据完整性
- **集成性**: 在 Power Platform 中无缝工作

### 语言哲学
Power Fx 促进：
- 通过类似 Excel 的熟悉公式进行低代码开发
- 当依赖项更改时自动重新计算
- 编译时检查的类型安全
- 函数式编程模式

## 根结构
每个 Power Apps YAML 文件都遵循这个顶级结构：

```yaml
App:
  Properties:
    # 应用级属性和公式
    StartScreen: =Screen1

Screens:
  # 屏幕定义

ComponentDefinitions:
  # 自定义组件定义

DataSources:
  # 数据源配置

EditorState:
  # 编辑器元数据（屏幕顺序等）
```

## 1. App 部分
`App` 部分定义应用程序级属性和配置。

```yaml
App:
  Properties:
    StartScreen: =Screen1
    BackEnabled: =false
    # 其他带有 Power Fx 公式的应用属性
```

### 关键点：
- 包含应用程序范围的设置
- 属性使用 Power Fx 公式（以 `=` 为前缀）
- 通常会指定 `StartScreen` 属性

## 2. Screens 部分
将应用程序中的所有屏幕定义为无序映射。

```yaml
Screens:
  Screen1:
    Properties:
      # 屏幕属性
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
- **Properties**: 屏幕级属性和公式
- **Children**: 屏幕上的控件数组（按 z-index 排序）

### 控件定义格式：
```yaml
ControlName:
  Control: ControlType      # 必需：控件类型标识符
  Properties:
    PropertyName: =PowerFxFormula
  # 可选属性：
  Group: GroupName          # 用于在 Studio 中组织控件
  Variant: VariantName      # 控件变体（影响默认属性）
  MetadataKey: Key          # 控件的元数据标识符
  Layout: LayoutName        # 布局配置
  IsLocked: true/false      # 控件在编辑器中是否锁定
  Children: []              # 用于容器控件（按 z-index 排序）
```

### 控件版本控制：
您可以使用 `@` 运算符指定控件版本：
```yaml
MyButton:
  Control: Button@2.1.0     # 特定版本
  Properties:
    Text: ="Click Me"

MyLabel:
  Control: Label            # 默认使用最新版本
  Properties:
    Text: ="Hello World"
```

## 3. 控件类型

### 标准控件
常见的第一方控件包括：
- **基本控件**: `Label`, `Button`, `TextInput`, `HTMLText`
- **输入控件**: `Slider`, `Toggle`, `Checkbox`, `Radio`, `Dropdown`, `Combobox`, `DatePicker`, `ListBox`
- **显示控件**: `Image`, `Icon`, `Video`, `Audio`, `PDF 查看器`, `条形码扫描器`
- **布局控件**: `Container`, `Rectangle`, `Circle`, `Gallery`, `DataTable`, `Form`
- **图表控件**: `柱状图`, `折线图`, `饼图`
- **高级控件**: `Timer`, `Camera`, `Microphone`, `添加图片`, `导入`, `导出`

### 容器和布局控件
特别关注容器控件及其子控件：
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
          X: =10         # 相对于容器
          Y: =10         # 相对于容器
    - Button1:
        Control: Button
        Properties:
          Text: ="Container Button"
          X: =10
          Y: =50
```

### 自定义组件
```yaml
MyCustomControl:
  Control: Component
  ComponentName: MyComponent
  Properties:
    X: =10
    Y: =10
    # 自定义组件属性
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
    Description: "一个可重用的组件"
    AllowCustomization: true
    AccessAppScope: false
    CustomProperties:
      InputText:
        PropertyKind: Input
        DataType: Text
        Description: "输入文本属性"
        Default: ="Default Value"
      OutputValue:
        PropertyKind: Output
        DataType: Number
        Description: "输出数值"
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
- **Input**: 从父级接收值
- **Output**: 向父级发送值
- **InputFunction**: 由父级调用的函数
- **OutputFunction**: 在组件中定义的函数
- **Event**: 向父级触发事件
- **Action**: 具有副作用的函数

### 数据类型：
- `Text`, `Number`, `Boolean`
- `DateAndTime`, `Color`, `Currency`
- `Record`, `Table`, `Image`
- `VideoOrAudio`, `Screen`

## 5. 数据源
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
      # 附加连接器参数
```

### 数据源类型：
- **Table**: Dataverse 表或其他表格数据
- **Actions**: 连接器操作和流

## 6. 编辑器状态
维护编辑器组织：

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
- 空值可以表示为 `null`（不带引号）
- 示例：
  ```yaml
  Text: ="Hello World"
  X: =10
  Visible: =Toggle1.Value
  OnSelect: =Navigate(Screen2, ScreenTransition.Fade)
  OptionalProperty: null    # 表示无值
  ```

### 常见公式模式：
```yaml
# 静态值
Text: ="Static Text"
X: =50
Visible: =true

# 控件引用
Text: =TextInput1.Text
Visible: =Toggle1.Value

# 父级引用（用于容器/库中的控件）
Width: =Parent.Width - 20
Height: =Parent.TemplateHeight    # 在库模板中

# 函数
OnSelect: =Navigate(NextScreen, ScreenTransition.Slide)
Text: =Concatenate("Hello ", User().FullName)

# 条件逻辑
Visible: =If(Toggle1.Value, true, false)
Fill: =If(Button1.Pressed, RGBA(255,0,0,1), RGBA(0,255,0,1))

# 数据操作
Items: =Filter(DataSource, Status = "Active")
Text: =LookUp(Users, ID = 123).Name
```

### Z-Index 和控件排序：
- `Children` 数组中的控件按 z-index 排序
- 数组中的第一个控件 = 底层（z-index 1）
- 数组中的最后一个控件 = 顶层（最高 z-index）
- 所有控件都使用从 1 开始的升序

## 命名约定

### 实体名称：
- 屏幕名称：描述性且唯一
- 控件名称：TypeName + Number（例如：`Button1`, `Label2`）
- 组件名称：PascalCase

### 属性名称：
- 标准属性：使用架构中的确切大小写
- 自定义属性：建议使用 PascalCase

## 最佳实践

### 1. 结构组织：
- 保持屏幕逻辑组织
- 使用 `Group` 属性对相关控件进行分组
- 为所有实体使用有意义的名称

### 2. 公式编写：
- 保持公式可读性和良好格式
- 在复杂公式中尽可能使用注释
- 避免过于复杂的嵌套表达式

### 3. 组件设计：
- 设计可重用的组件
- 为自定义属性提供清晰的描述
- 使用适当的属性类型（Input/Output）

### 4. 数据源管理：
- 为数据源使用描述性名称
- 文档化连接要求
- 保持数据源配置最小化

## 验证规则

### 必需属性：
- 所有控件都必须有 `Control` 属性
- 组件定义必须有 `DefinitionType`
- 数据源必须有 `Type`

### 命名模式：
- 实体名称：最少 1 个字符，字母数字
- 控件类型 ID：遵循模式 `^([A-Z][a-zA-Z0-9]*/)?[A-Z][a-zA-Z0-9]*(@\d+\.\d+\.\d+)?$`
- 代码组件名称：遵循模式 `^([a-z][a-z0-9]{1,7})_([a-zA-Z0-9]\.)+[a-zA-Z0-9]+$`

## 常见问题和解决方案

### 1. 无效控件类型：
- 确保控件类型拼写正确
- 检查正确的大小写
- 验证控件类型在架构中受支持

### 2. 公式错误：
- 所有公式必须以 `=` 开头
- 使用正确的 Power Fx 语法
- 检查正确的属性引用

### 3. 结构验证：
- 保持正确的 YAML 缩进
- 确保存在必需属性
- 严格遵循架构结构

### 4. 自定义组件问题：
- 验证 `ComponentName` 与定义匹配
- 确保自定义属性正确定义
- 检查属性类型是否合适
- 如果使用外部组件，验证组件库引用

### 5. 性能考虑：
- 避免在 YAML 中深度嵌套公式
- 使用高效的数据源查询
- 考虑对大型数据集使用可委托公式
- 最小化频繁更新属性中的复杂计算

## 高级主题

### 1. 组件库集成：
```yaml
ComponentDefinitions:
  MyLibraryComponent:
    DefinitionType: CanvasComponent
    AllowCustomization: true
    ComponentLibraryUniqueName: "pub_MyComponentLibrary"
    # 组件定义详细信息
```

### 2. 响应式设计考虑：
- 使用 `Parent.Width` 和 `Parent.Height` 进行响应式大小调整
- 考虑基于容器的布局用于复杂 UI
- 使用公式进行动态定位和大小调整

### 3. 库模板：
```yaml
MyGallery:
  Control: Gallery
  Properties:
    Items: =DataSource
    TemplateSize: =100
  Children:
    - GalleryTemplate:  # 每个库项的模板
        Children:
          - TitleLabel:
              Control: Label
              Properties:
                Text: =ThisItem.Title
                Width: =Parent.TemplateWidth - 20
```

### 4. 表单控件和数据卡：
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
Power Apps YAML 文件可以通过几种方法获得：

1. **Power Platform CLI**：
   ```powershell
   # 列出环境中的画布应用
   pac canvas list

   # 下载并提取 YAML 文件
   pac canvas download --name "MyApp" --extract-to-directory "C:\path\to\destination"
   ```

2. **从 .msapp 手动提取**：
   ```powershell
   # 使用 PowerShell 提取 .msapp 文件
   Expand-Archive -Path "C:\path\to\yourFile.msapp" -DestinationPath "C:\path\to\destination"
   ```

3. **Dataverse Git 集成**：无需 .msapp 文件直接访问源文件

### .msapp 中的文件结构：
- `\src\App.pa.yaml` - 表示主要应用配置
- `\src\[ScreenName].pa.yaml` - 每个屏幕一个文件
- `\src\Component\[ComponentName].pa.yaml` - 组件定义

**重要说明**：
- 只有 `\src` 文件夹中的文件用于源代码控制
- .pa.yaml 文件是**只读的**，仅供审查目的
- 不支持外部编辑、合并和冲突解决
- .msapp 中的 JSON 文件对于源代码控制不稳定

### 架构版本演进：
1. **实验格式** (*.fx.yaml)：不再开发
2. **早期预览**：临时格式，不再使用
3. **源代码** (*.pa.yaml)：当前支持版本控制的活跃格式

## Power Fx 公式参考

### 公式类别：

#### **函数**：接受参数，执行操作，返回值
```yaml
Properties:
  Text: =Concatenate("Hello ", User().FullName)
  X: =Sum(10, 20, 30)
  Items: =Filter(DataSource, Status = "Active")
```

#### **信号**：返回环境信息（无参数）
```yaml
Properties:
  Text: =User().FullName
  Color: =RGBA(255, 255, 255, 1)
  CurrentTime: =Now()
```

#### **枚举**：预定义常量值
```yaml
Properties:
  Transition: =ScreenTransition.Fade
  NotificationType: =NotificationType.Information
  FormMode: =FormMode.Edit
```

#### **操作**：执行具有副作用的操作
```yaml
Properties:
  OnSelect: =Navigate(Screen2, ScreenTransition.Cover)
  OnChange: =Reset(TextInput1)
  OnSuccess: =Notify("保存成功", NotificationType.Success)
```

### 表达式类型：

#### 文本操作
```yaml
Text: =Concatenate("Hello", " ", "World")
Substring: =Mid(Text, 1, 5)
Upper: =Upper(Text)
Lower: =Lower(Text)
Length: =Len(Text)
```

#### 数值计算
```yaml
Sum: =10 + 20
Product: =5 * 3
Division: =15 / 3
Modulo: =10 % 3
Power: =2 ^ 3
```

#### 日期和时间
```yaml
CurrentDate: =Today()
CurrentDateTime: =Now()
DateAdd: =DateAdd(Today(), 7, Days)
DateDiff: =DateDiff(Today(), DueDate, Days)
Year: =Year(Now())
Month: =Month(Now())
Day: =Day(Now())
```

#### 逻辑操作
```yaml
And: =And(Toggle1.Value, Checkbox1.Value)
Or: =Or(Dropdown1.Selected.Value = "A", Dropdown1.Selected.Value = "B")
Not: =Not(Toggle1.Value)
If: =If(Score > 80, "Excellent", "Good")
```

#### 数据操作
```yaml
Filter: =Filter(DataSource, Status = "Active")
Search: =Search(DataSource, TextInput1.Text, "Name")
Sort: =Sort(DataSource, CreatedDate, SortOrder.Descending)
LookUp: =LookUp(DataSource, ID = 123, Name)
Distinct: =Distinct(DataSource, ColumnName)
```

### 记录和表操作

#### 记录操作
```yaml
# 创建记录
NewRecord: = { Name: "John", Age: 30, Active: true }

# 更新记录
UpdatedRecord: =Patch(DataSource, LookUp(DataSource, ID = 123), { Name: "Jane" })

# 合并记录
MergedRecord: = { Record1: existingRecord, Record2: { Active: false } }
```

#### 表操作
```yaml
# 创建表
NewTable: =Table({ Name: "Item1" }, { Name: "Item2" })

# 添加行
AddRow: =Collect(Collection1, { Name: "NewItem" })

# 清除表
ClearTable: =Clear(Collection1)

# 表函数
FirstRow: =First(DataSource)
LastRow: =Last(DataSource)
Count: =CountRows(DataSource)
```

### 错误处理函数
```yaml
# IfError - 处理错误
SafeValue: =IfError(Divide(10, 0), "Error occurred")

# IsError - 检查错误
HasError: =IsError(Divide(10, 0))

# Error - 创建错误对象
CustomError: =Error("Custom error message")
```

### 数据类型转换
```yaml
# 文本转换
TextToNumber: =Value("123")
NumberToText: =Text(123)
DateToText: =Text(Now())

# 类型检查
IsText: =IsType(Value, TextType)
IsNumber: =IsType(Value, NumberType)
IsDate: =IsType(Value, DateType)
```

## 调试和故障排除

### 调试技巧：
1. **使用 Label 控件**显示变量值进行调试
2. **Notify 函数**显示调试信息
3. **Trace 函数**在控制台记录信息
4. **分步执行**复杂公式

### 常见调试模式：
```yaml
# 调试变量
DebugLabel:
  Control: Label
  Properties:
    Text: =Concatenate("Current Value: ", TextVariable)

# 调试条件
OnSelect: =If(DebugMode,
  Notify("Debug: Button clicked", NotificationType.Information),
  Navigate(NextScreen)
)
```

## 性能优化

### 公式优化：
- 避免在 `Items` 属性中使用复杂的嵌套函数
- 使用 `With` 函数简化重复引用
- 考虑使用变量存储计算结果
- 对大型数据集使用可委托函数

### 数据源优化：
- 限制检索的数据量
- 使用适当的索引和筛选条件
- 考虑数据分页
- 缓存频繁访问的数据

### 控件优化：
- 最小化不必要的控件重新计算
- 使用 `DelayOutput` 属性避免频繁更新
- 考虑使用 `Screen.Transition` 优化用户体验

通过遵循这些指南和最佳实践，您可以创建高效、可维护且功能强大的 Power Apps 画布应用 YAML 结构。