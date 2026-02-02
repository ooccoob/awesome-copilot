---
name: vscode-ext-commands
description: 'Guidelines for contributing commands in VS Code extensions. Indicates naming convention, visibility, localization and other relevant attributes, following VS Code extension development guidelines, libraries and good practices'
---

# VS Code 扩展命令贡献

此技能可帮助您在 VS Code 扩展中贡献命令

## 何时使用该技能

当您需要执行以下操作时，请使用此技能：
- 向 VS Code 扩展添加或更新命令

# 使用说明

VS Code 命令必须始终定义 `title`，与其类别、可见性或位置无关。我们对每种“类型”的命令使用一些模式，并具有一些特征，如下所述：

* 常规命令：默认情况下，所有命令都应可在命令面板中访问，必须定义 `category`，并且不需要 `icon`，除非该命令将在侧栏中使用。

* 侧边栏命令：其名称遵循特殊模式，以下划线 (`_`) 开头，后缀为 `#sideBar`，例如 `_extensionId.someCommand#sideBar`。必须定义 `icon`，并且可能有也可能没有 `enablement` 的某些规则。侧栏独占命令不应在命令面板中可见。将其贡献给 `view/title` 或 `view/item/context`，我们必须通知 _order/position_ 它将被显示，并且我们可以使用“相对于其他命令/按钮”的术语，以便您识别要使用的正确 `group`。另外，定义新命令可见的条件 (`when`) 是一个很好的做法。
