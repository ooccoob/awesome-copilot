---
description: 'Complete PCF API reference with all interfaces and their availability in model-driven and canvas apps'
applyTo: '**/*.{ts,tsx,js}'
---

# Power Apps 组件框架 API 参考

Power Apps 组件框架提供了一组丰富的 API，使您能够创建功能强大的代码组件。此参考列出了所有可用的接口及其在不同应用程序类型中的可用性。

## API 可用性

下表显示了 Power Apps 组件框架中可用的所有 API 接口，以及它们在模型驱动应用程序和画布应用程序中的可用性。

|应用程序接口 |模型驱动的应用程序 |画布应用程序 |
|-----|------------------|-------------|
|属性元数据 |是的 |没有 |
|客户|是的 |是的 |
|专栏 |是的 |是的 |
|条件表达式 |是的 |是的 |
|背景 |是的 |是的 |
|数据集|是的 |是的 |
|设备|是的 |是的 |
|实体|是的 |是的 |
|活动 |是的 |是的 |
|工厂|是的 |是的 |
|过滤|是的 |是的 |
|格式化|是的 |是的 |
|图像对象 |是的 |是的 |
|链接|是的 |是的 |
|模式|是的 |是的 |
|导航 |是的 |是的 |
|数字格式信息 |是的 |是的 |
|寻呼 |是的 |是的 |
|弹出窗口 |是的 |是的 |
|弹出服务|是的 |是的 |
|物业帮手 |是的 |是的 |
|资源 |是的 |是的 |
|排序状态 |是的 |是的 |
|标准控制|是的 |是的 |
|用户设置 |是的 |是的 |
|实用程序|是的 |是的 |
|网页API |是的 |是的 |

## 关键 API 命名空间

### 上下文 API

`Context` 对象提供对所有框架功能的访问，并传递给组件的生命周期方法。它包含：

- **客户端**：有关客户端的信息（外形尺寸、网络状态）
- **设备**：设备功能（摄像头、位置、麦克风）
- **工厂**：用于创建框架对象的工厂方法
- **格式**：数字和日期格式
- **模式**：组件模式和跟踪
- **导航**：导航方法
- **资源**：访问资源（图像、字符串）
- **UserSettings**：用户设置（区域设置、数字格式、安全角色）
- **Utils**：实用方法（getEntityMetadata、hasEntityPrivilege、lookupObjects）
- **WebApi**：Dataverse Web API 方法

### 数据API

- **数据集**：处理表格数据
- **列**：访问列元数据和数据
- **实体**：访问记录数据
- **过滤**：定义数据过滤
- **链接**：定义关系
- **分页**：处理数据分页
- **SortStatus**：管理排序

### 用户界面API

- **弹出**：创建弹出对话框
- **PopupService**：管理弹出生命周期
- **Mode**：获取组件渲染模式

### 元数据 API

- **AttributeMetadata**：列元数据（仅限模型驱动）
- **PropertyHelper**：属性元数据助手

### 标准控制

- **StandardControl**：具有生命周期方法的所有代码组件的基本接口：
  - `init()`：初始化组件
  - `updateView()`：更新组件 UI
  - `destroy()`：清理资源
  - `getOutputs()`：返回输出值

## 使用指南

### 模型驱动与画布应用程序

由于平台差异，某些 API 仅在模型驱动应用程序中可用：

- **AttributeMetadata**：仅模型驱动 - 提供详细的列元数据
- 大多数其他 API 在两个平台上均可用

### API版本兼容性

- 始终检查目标平台（模型驱动或画布）的 API 可用性
- 某些 API 可能在不同平台上有不同的行为
- 在目标环境中测试组件以确保兼容性

### 常见模式

1. **访问上下文 API**
   ```typescript
   // In init or updateView
   const userLocale = context.userSettings.locale;
   const isOffline = context.client.isOffline();
   ```

2. **使用数据集**
   ```typescript
   // Access dataset records
   const records = context.parameters.dataset.records;
   
   // Get sorted columns
   const sortedColumns = context.parameters.dataset.sorting;
   ```

3. **使用WebApi**
   ```typescript
   // Retrieve records
   context.webAPI.retrieveMultipleRecords("account", "?$select=name");
   
   // Create record
   context.webAPI.createRecord("contact", data);
   ```

4. **设备功能**
   ```typescript
   // Capture image
   context.device.captureImage();
   
   // Get current position
   context.device.getCurrentPosition();
   ```

5. **格式化**
   ```typescript
   // Format date
   context.formatting.formatDateLong(date);
   
   // Format number
   context.formatting.formatDecimal(value);
   ```

## 最佳实践

1. **类型安全**：使用 TypeScript 进行类型检查和 IntelliSense
2. **空检查**：在访问 API 对象之前始终检查空/未定义
3. **错误处理**：将 API 调用包装在 try-catch 块中
4. **平台检测**：检查 `context.client.getFormFactor()` 以适应行为
5. **API 可用性**：使用前验证目标平台的 API 可用性
6. **性能**：适当时缓存 API 结果以避免重复调用

## 其他资源

- 有关每个 API 的详细文档，请参阅 [Power Apps 组件框架 API 参考](https://learn.microsoft.com/power-apps/developer/component-framework/reference/)
- 每个 API 的示例代码可在 [PowerApps-Samples 存储库](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework) 中找到
