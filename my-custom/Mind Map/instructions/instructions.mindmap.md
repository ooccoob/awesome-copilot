## What/When/Why/How
- What: 如何编写高质量 *.instructions.md（前言、结构、内容、示例、验证）
- When: 新增/维护自定义指令以指导 Copilot 生成领域代码
- Why: 让 Copilot 在特定工程/语言中更合规、更有上下文
- How: 标准化 frontmatter、章节模板、写作风格与验证流程

## Key Points
- Frontmatter: description(单引号)、applyTo(glob，可多项)
- 结构: 标题/Overview → General/Best Practices/Code Standards/Architecture/Security/Performance/Testing → 示例
- 写作: 祈使句、具体可执行、示例优先、保持当前版本、给出链接
- 示例: Good/Bad 对比、表格、代码块（标注语言）
- 验证: 构建/格式/测试/路径匹配；先本地试用再提交
- 维护: 框架/依赖升级时同步更新；移除过时内容

## Compact Map
Frontmatter→章节→写作风格→示例→验证→维护

## Example Questions (10+)
1) 生成一个面向 React 的 instructions 初稿（含 frontmatter）
2) 将 applyTo 扩展为多种后缀的 glob 写法
3) 写一个“Good/Bad”代码对比的 TypeScript 片段
4) 给出“Security Best Practices”表格化示例
5) 如何为团队约定命名/导入顺序/注释规范？
6) 把验证步骤集成到 CI 并输出校验报告
7) 为大型仓库拆分指令文件并维持链接目录
8) 编写“Conditional Guidance”段落的示例
9) 将旧版内容升级到新框架主版本的步骤
10) 在 VS Code 中验证 Copilot 是否正确遵循此文件

Source: d:\mycode\awesome-copilot\instructions\instructions.instructions.md | Generated: 2025-10-17T00:00:00Z
