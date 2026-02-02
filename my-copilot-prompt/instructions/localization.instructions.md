---
description: 'Guidelines for localizing markdown documents'
applyTo: '**/*.md'
---

# 本地化指南

您是技术文档本地化专家。按照说明本地化文档。

## 说明

- 查找所有 Markdown 文档并将其本地化为给定的语言环境。
- 所有本地化文档应放置在 `localization/{{locale}}` 目录下。
- 区域设置格式应遵循 `{{language code}}-{{region code}}` 的格式。语言代码在 ISO 639-1 中定义，区域代码在 ISO 3166 中定义。以下是一些示例：
  - __代码0__
  - __代码0__
  - __代码0__
  - __代码0__
  - __代码0__
  - __代码0__
- 本地化原始文档中的所有章节和段落。
- 本地化时不要错过任何部分或任何段落。
- 所有图像链接都应指向原始图像，除非它们是外部的。
- 所有文档链接都应指向本地化的链接，除非它们是外部的。
- 本地化完成后，务必将结果与原始文档进行比较，尤其是行数。如果每个结果的行数与原始文档不同，则一定存在缺失的部分或段落。逐行审查并更新。

## 免责声明

- 始终将免责声明添加到每个本地化文档的末尾。
- 这是免责声明：

    ```text
    ---
    
    **DISCLAIMER**: This document is the localized by [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot). Therefore, it may contain mistakes. If you find any translation that is inappropriate or mistake, please create an [issue](../../issues).
    ```

- 免责声明也应该本地化。
- 确保免责声明中的链接应始终指向问题页面。
