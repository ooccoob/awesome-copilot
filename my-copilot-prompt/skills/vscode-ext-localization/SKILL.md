---
name: vscode-ext-localization
description: 'Guidelines for proper localization of VS Code extensions, following VS Code extension development guidelines, libraries and good practices'
---

# VS Code 扩展本地化

此技能可帮助您本地化 VS Code 扩展的各个方面

## 何时使用该技能

当您需要执行以下操作时，请使用此技能：
- 本地化新的或现有的贡献配置（设置）、命令、菜单、视图或演练
- 本地化向最终用户显示的扩展源代码中包含的新消息或现有消息或其他字符串资源

# 使用说明

VS Code 本地化由三种不同的方法组成，具体取决于要本地化的资源。创建或更新新的可本地化资源时，必须创建/更新所有当前可用语言的相应本地化。

1. 设置、命令、菜单、视图、ViewsWelcome、演练标题和描述等配置，在 `package.json` 中定义
  -> 独有的 `package.nls.LANGID.json` 文件，例如巴西葡萄牙语 (`pt-br`) 本地化的 `package.nls.pt-br.json`
2. 演练内容（在其自己的 `Markdown` 文件中定义）
  -> 用于巴西葡萄牙语本地化的专有 `Markdown` 文件，例如 `walkthrough/someStep.pt-br.md`
3. 位于扩展源代码（JavaScript 或 TypeScript 文件）中的消息和字符串
  -> 用于巴西葡萄牙语本地化的专有 `bundle.l10n.pt-br.json`
