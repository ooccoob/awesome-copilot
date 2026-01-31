---
描述：“使用 Fluent UI 设置具有现代主题的样式组件”
applyTo: '**/*.{ts,tsx,js,json,xml,pcfproj,csproj}'
---

# 具有现代主题的样式组件（预览）

[本主题是预发布文档，可能会发生变化。]

开发人员需要能够对其组件进行样式设置，以便它们看起来像它们所包含的应用程序的其余部分一样。当现代主题对画布应用程序（通过[现代控件和主题](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/overview-modern-controls)功能）或模型驱动应用程序（通过[新的刷新外观](https://learn.microsoft.com/en-us/power-apps/user/modern-fluent-design)）生效时，他们可以这样做。

使用基于 [Fluent UI React v9](https://react.fluentui.dev/) 的现代主题来设置组件的样式。建议使用此方法以获得组件的最佳性能和主题体验。

## 应用现代主题的四种方法

1. **流畅的 UI v9 控件**
2. **流畅的 UI v8 控件**
3. **不流畅的 UI 控件**
4. **自定义主题提供商**

## Fluent UI v9 控件

将 Fluent UI v9 控件包装为组件是利用现代主题的最简单方法，因为现代主题会自动应用于这些控件。唯一的先决条件是确保您的组件添加对 [React 控件和平台库](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/react-controls-platform-libraries) 的依赖项。

这种方法允许您的组件使用与平台相同的 React 和 Fluent 库，因此共享将主题令牌传递给组件的相同 React 上下文。

```xml
<resources>
  <code path="index.ts" order="1"/>
  <!-- Dependency on React controls & platform libraries -->
  <platform-library name="React" version="16.14.0" />
  <platform-library name="Fluent" version="9.46.2" />
</resources>
```

## 流畅的 UI v8 控件

当您在组件中使用 Fluent UI v8 控件时，Fluent 提供了应用 v9 主题构造的迁移路径。使用 [Fluent 的 v8 到 v9 迁移包](https://www.npmjs.com/package/@fluentui/react-migration-v8-v9) 中包含的 `createV8Theme` 函数基于 v9 主题令牌创建 v8 主题：

```typescript
const theme = createV8Theme(
  context.fluentDesignLanguage.brand,
  context.fluentDesignLanguage.theme
);
return <ThemeProvider theme={theme}></ThemeProvider>;
```

## 不流畅的 UI 控件

如果您的组件不使用 Fluent UI，您可以通过 `fluentDesignLanguage` 上下文参数直接获取可用的 v9 主题令牌的依赖项。使用此参数可以访问所有 [theme](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/theming) 标记，以便它可以引用主题的任何方面来设置自身样式。

```typescript
<span style={{ fontSize: context.fluentDesignLanguage.theme.fontSizeBase300 }}>
  {"Stylizing HTML with platform provided theme."}
</span>
```

## 自定义主题提供商

当您的组件需要与应用程序当前主题不同的样式时，请创建您自己的 `FluentProvider` 并传递您自己的一组主题标记以供组件使用。

```typescript
<FluentProvider theme={context.fluentDesignLanguage.tokenTheme}>
  {/* your control */}
</FluentProvider>
```

## 样品对照

每个用例的示例可在 [现代主题 API 控件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/sample-controls/modern-theming-api-control) 中找到。

## 常见问题解答

### 问：我的控件使用 Fluent UI v9 并依赖于平台库，但我不想使用现代主题。如何为我的组件禁用它？

答：您可以通过两种不同的方式执行此操作：

**选项 1**：创建您自己的组件级 `FluentProvider`

```typescript
<FluentProvider theme={customFluentV9Theme}>
  {/* your control */}
</FluentProvider>
```

**选项 2**：将控件包装在 `IdPrefixContext.Provider` 内并设置您自己的 `idPrefix` 值。这可以防止您的组件从平台获取主题令牌。

```typescript
<IdPrefixProvider value="custom-control-prefix">
  <Label weight="semibold">This label is not getting Modern Theming</Label>
</IdPrefixProvider>
```

### 问：我的一些 Fluent UI v9 控件没有获取样式

答：依赖于 React Portal 的 Fluent v9 控件需要在主题提供程序中重新包装，以确保正确应用样式。您可以使用 `FluentProvider`。

### 问：如何检查现代主题是否已启用？

答：您可以检查令牌是否可用：`context.fluentDesignLanguage?.tokenTheme`。或者在模型驱动应用程序中，您可以检查应用程序设置：`context.appSettings.getIsFluentThemingEnabled()`。

## 相关文章

- [主题（Power Apps 组件框架 API 参考）](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/theming)
- [现代主题 API 控件](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/sample-controls/modern-theming-api-control)
- [在画布应用程序中使用现代主题（预览）](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/modern-controls/modern-theming)
