# Create LLMs File from Repository Structure - 思维导图

## 📋 文档摘要 (What / When / Why / How)

**What（文档作用）**: 从仓库结构生成符合 llms.txt 规范的 `llms.txt`，为 LLM 提供高效的导航入口。

**When（适用场景）**: 在需要让大模型快速理解和导航代码库、生成自动化文档索引或为代码搜索/审查提供上下文时使用。

**Why（核心价值）**: 帮助 LLM 和开发者快速找到关键文档与规范，提升自动化助手（如 Copilot）对仓库的理解深度与准确性。

**How（使用指引）**: 分析仓库结构，挑选关键文件，按 llms.txt 规范组织为 H1、blockquote、无标题段落与若干 H2 列表节，并验证链接有效性。

---

## 🎯 实际使用说明与示例问题（场景化问题）

- 如何根据仓库生成一份遵循 https://llmstxt.org/ 的 `llms.txt`？
- 哪些文件应被视为“关键文件”（Documentation / Specs / Examples / Configuration）并列入优先级？
- 如何为每个文件生成简短、明晰的描述，既供人阅读也利于 LLM 索引？
- 如何验证相对链接在仓库根路径下是否有效？

---

## 📊 结构化要点（中英对照）

- Project Name (项目名称)
  - H1 header: repository / project name
- Summary (摘要)
  - blockquote: concise description of purpose & scope
- Additional Context (附加上下文)
  - optional paragraphs without headings
- Documentation (文档)
  - README, CONTRIBUTING, docs/
- Specifications (规范)
  - spec/, API 文档, blueprint
- Examples (示例)
  - examples/, sample code
- Configuration (配置)
  - CI/CD, Dockerfile, env files
- Optional (可选)
  - architecture, decisions, historical notes

---

## 🧭 输出格式模板（llms.txt 格式要求）

# [Repository Name]

> [Concise description of the repository's purpose and scope]

[Optional additional context paragraphs without headings]

## Documentation

- [Main README](README.md): Primary project documentation and getting started guide

## Specifications

- [Technical Specification](spec/technical-spec.md): Detailed technical requirements and constraints

## Examples

- [Basic Example](examples/basic-usage.md): Simple usage demonstration

## Configuration

- [Setup Guide](docs/setup.md): Installation and configuration instructions

---

## 🧠 思维导图格式（Markdown 列表）

- Create LLMs File from Repository Structure
  - 文档摘要
    - What: 从仓库生成 llms.txt
    - When: 需要 LLM 快速理解仓库时
    - Why: 提升 LLM 导航效率与准确性
    - How: 分析结构并按规范组织
  - 实际使用说明
    - 生成步骤: 分析 -> 计划 -> 生成 -> 验证
    - 验证要点: 链接有效性、格式合规、优先级合理
  - 结构化要点 (中英对照)
    - Project Name / 项目名称
    - Summary / 摘要
    - Documentation / 文档
    - Specifications / 规范
    - Examples / 示例
    - Configuration / 配置
  - 输出模板
    - H1, blockquote, sections

---

**源文件**: d:\mycode\awesome-copilot\prompts\create-llms.prompt.md
**生成时间**: 2025-10-17T00:00:00+08:00
