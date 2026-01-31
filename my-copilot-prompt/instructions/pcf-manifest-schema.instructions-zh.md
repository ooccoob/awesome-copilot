---
描述：“PCF 组件的完整清单架构参考，包含所有可用的 XML 元素”
applyTo: '**/*.xml'
---

# 清单架构参考

清单文件 (`ControlManifest.Input.xml`) 是定义代码组件的元数据文档。此参考列出了所有可用的清单元素及其用途。

## 根元素

### 明显的

包含整个组件定义的根元素。

## 核心要素

### 代码

指实现组件逻辑的资源文件。

**属性：**
- `path`：TypeScript/JavaScript 实现文件的路径
- `order`：加载顺序（通常为“1”）

**可用性：** 模型驱动应用程序、画布应用程序、门户

### 控制

定义组件本身，包括命名空间、版本和显示信息。

**关键属性：**
- `namespace`：组件的命名空间
- `constructor`：构造函数名称
- `version`：语义版本（例如“1.0.0”）
- `display-name-key`：显示名称的资源键
- `description-key`：描述的资源密钥
- `control-type`：控制类型（“标准”或“虚拟”）

**可用性：** 模型驱动应用程序、画布应用程序、门户

## 属性元素

### 财产

定义组件的输入或输出属性。

**关键属性：**
- `name`：属性名称
- `display-name-key`：显示名称的资源键
- `description-key`：描述的资源密钥
- `of-type`：数据类型（例如，“SingleLine.Text”、“Whole.None”、“TwoOptions”、“DateAndTime.DateOnly”）
- `usage`：属性用法（“绑定”或“输入”）
- `required`：是否需要属性（true/false）
- `of-type-group`：对类型组的引用
- `default-value`：属性的默认值

**可用性：** 模型驱动应用程序、画布应用程序、门户

### 类型组

定义属性可以接受的一组类型。

**用法：** 允许属性接受多种数据类型

**可用性：** 模型驱动应用程序、画布应用程序、门户

## 数据集元素

### 数据集

定义用于处理表格数据的数据集属性。

**关键属性：**
- `name`：数据集名称
- `display-name-key`：显示名称的资源键
- `description-key`：描述的资源密钥

**可用性：** 模型驱动应用程序（有限制的画布应用程序）

## 资源元素

### 资源

所有资源定义（代码、CSS、图像、本地化）的容器。

**可用性：** 模型驱动应用程序、画布应用程序、门户

### CSS

引用 CSS 样式表文件。

**属性：**
- `path`：CSS 文件的路径
- `order`：加载顺序

**可用性：** 模型驱动应用程序、画布应用程序、门户

### 图像

引用图像资源。

**属性：**
- `path`：图像文件的路径

**可用性：** 模型驱动应用程序、画布应用程序、门户

### 资源

引用资源文件进行本地化。

**属性：**
- `path`：.resx 文件的路径
- `version`：版本号

**可用性：** 模型驱动应用程序、画布应用程序、门户

## 功能使用元素

### 使用功能

声明该组件使用特定的平台功能。

**关键属性：**
- `name`：功能名称（例如“Device.captureImage”、“Device.getCurrentPosition”、“Utility.lookupObjects”、“WebAPI”）
- `required`：是否需要该功能（true/false）

**共同特点：**
- 设备.captureAudio
- 设备.captureImage
- 设备.captureVideo
- 设备.getBarcodeValue
- 设备.getCurrentPosition
- 设备.pickFile
- 实用程序.lookupObjects
- 网络应用程序接口

**可用性：** 因功能和平台而异

### 功能使用

功能声明的容器。

**可用性：** 模型驱动应用程序、画布应用程序

## 依赖元素

### 依赖性

声明组件所需的外部依赖项。

**可用性：** 模型驱动应用程序、画布应用程序

### 外部服务使用

声明组件使用的外部服务。

**关键属性：**
- `enabled`：是否启用外部服务使用（true/false）

**可用性：** 模型驱动应用程序、画布应用程序

## 图书馆元素

### 平台库

引用平台提供的库（例如 React、Fluent UI）。

**关键属性：**
- `name`：库名称（例如“React”、“Fluent”）
- `version`：库版本

**可用性：** 模型驱动应用程序、画布应用程序

## 事件元素

### 事件

定义组件可以引发的自定义事件。

**关键属性：**
- `name`：事件名称
- `display-name-key`：显示名称的资源键
- `description-key`：描述的资源密钥

**可用性：** 模型驱动应用程序、画布应用程序

## 动作元素

### 平台行动

定义组件可以调用的平台操作。

**可用性：** 模型驱动应用程序

## 清单结构示例

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleNamespace" 
           constructor="SampleControl" 
           version="1.0.0" 
           display-name-key="Sample_Display_Key" 
           description-key="Sample_Desc_Key" 
           control-type="standard">
    
    <!-- Properties -->
    <property name="sampleProperty" 
              display-name-key="Property_Display_Key" 
              description-key="Property_Desc_Key" 
              of-type="SingleLine.Text" 
              usage="bound" 
              required="true" />
    
    <!-- Type Group Example -->
    <type-group name="numbers">
      <type>Whole.None</type>
      <type>Currency</type>
      <type>FP</type>
      <type>Decimal</type>
    </type-group>
    
    <property name="numericProperty"
              display-name-key="Numeric_Display_Key"
              of-type-group="numbers"
              usage="bound" />
    
    <!-- Data Set Example -->
    <data-set name="dataSetProperty" 
              display-name-key="Dataset_Display_Key">
    </data-set>
    
    <!-- Events -->
    <event name="onCustomEvent"
           display-name-key="Event_Display_Key"
           description-key="Event_Desc_Key" />
    
    <!-- Resources -->
    <resources>
      <code path="index.ts" order="1" />
      <css path="css/SampleControl.css" order="1" />
      <img path="img/icon.png" />
      <resx path="strings/SampleControl.1033.resx" version="1.0.0" />
    </resources>
    
    <!-- Feature Usage -->
    <feature-usage>
      <uses-feature name="WebAPI" required="true" />
      <uses-feature name="Device.captureImage" required="false" />
    </feature-usage>
    
    <!-- Platform Library -->
    <platform-library name="React" version="16.8.6" />
    <platform-library name="Fluent" version="8.29.0" />
    
  </control>
</manifest>
```

## 舱单验证

清单架构在构建过程中进行验证：
- 缺少必需的元素将导致构建错误
- 无效的属性值将被标记
- 使用 `pac pcf` 命令验证清单结构

## 最佳实践

1. **语义版本控制**：对组件版本使用语义版本控制 (major.minor.patch)
2. **本地化键**：始终使用资源键而不是硬编码字符串
3. **功能声明**：声明您的组件使用的所有功能
4. **必需与可选**：仅在真正必要时将属性和功能标记为必需
5. **类型组**：对接受多个数字类型的属性使用类型组
6. **数据类型**：选择符合您要求的最具体的数据类型
7. **CSS 作用域**：作用域 CSS 以避免与主机应用程序发生冲突
8. **资源组织**：将资源组织在单独的文件夹中（css/、img/、strings/）

## 数据类型参考

属性的常见 `of-type` 值：

- **文本**：SingleLine.Text、多个、SingleLine.TextArea、SingleLine.Email、SingleLine.Phone、SingleLine.Url、SingleLine.Ticker
- **数字**：整数、无、货币、FP、小数
- **日期/时间**：DateAndTime.DateAndTime、DateAndTime.DateOnly
- **布尔**：两个选项
- **查找**：查找。简单
- **选项集**：选项集、多选选项集
- **其他**：枚举

## 平台可用性图例

- ✅ **模型驱动应用程序**：完全支持
- ✅ **画布应用程序**：支持（可能有限制）
- ✅ **门户**：在 Power Pages 中受支持

大多数清单元素在所有平台上都可用，但某些功能（例如某些设备 API 或平台操作）可能是特定于平台的。始终在目标环境中进行测试。
