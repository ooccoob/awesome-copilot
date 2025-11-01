## What/When/Why/How

- What: awesome-copilot collections 编写/校验规范与生成流程。
- When: 新建/修改 collections/*.collection.yml 时。
- Why: 确保清单正确、可发现、自动生成文档成功。
- How: 遵循必填字段(id/name/description/items)、校验脚本、ID/路径/标签规则；运行 update-readme.js 生成文档。

## Key Points

- 结构: 必填 id/name/description/items；可选 tags/display。
- 规则: id 唯一、小写/数字/连字符；1-50 items；描述 1-500 字符；路径存在且 kind 与扩展匹配；标签字符集受限。
- 最佳实践: 3-10 相关条目/清晰命名/互补性验证/添加标签。
- 校验: node validate-collections.js；仅引用仓库存在文件。
- 文档: update-readme.js 自动生成概览与页面；VS Code 安装 badges 自动创建。

## Compact Map

- Fields → id/name/description/items
- Rules → id 唯一/路径存在/标签规范
- Validate → validate-collections.js
- Generate → update-readme.js
- Practice → 小而专/互补/可用

## Example Questions (10+)

1) collection id 冲突如何定位与修复？
2) items 的 kind 与扩展不匹配怎么处理？
3) 标签命名不合规会触发哪些校验错误？
4) 如何让集合条目形成完整工作流？
5) 生成的 README.collections.md 包含哪些信息？
6) 如何在 PR 中集成自动校验？
7) 跨目录引用路径的相对写法？
8) 大于 50 条目的拆分策略？
9) display.ordering 的可选值与用途？
10) 校验通过但条目失效的排查步骤？

---
Source: d:\mycode\awesome-copilot\instructions\collections.instructions.md | Generated: 2025-10-17
