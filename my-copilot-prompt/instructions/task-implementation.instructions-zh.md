---
applyTo: '**/.copilot-tracking/changes/*.md'
描述：“通过渐进式跟踪和更改记录实施任务计划的说明 - 由 microsoft/edge-ai 为您提供”
---

# 任务计划实施说明

您将实施位于 `.copilot-tracking/plans/**` 和 `.copilot-tracking/details/**` 中的特定任务计划。您的目标是逐步、完整地实施计划文件中的每个步骤，以创建满足所有指定要求的高质量、可工作的软件。

必须在位于 `.copilot-tracking/changes/**` 的相应更改文件中跟踪实施进度。

## 核心实施流程

### 1. 方案分析与准备

**必须在开始实施之前完成：**
- **强制**：阅读并充分理解完整的计划文件，包括范围、目标、所有阶段和每个清单项目
- **强制**：完全阅读并完全理解相应的更改文件 - 如果上下文中缺少任何部分，请使用 `read_file` 读回整个文件
- **强制**：识别计划中提到的所有引用文件并检查它们的上下文
- **强制**：了解当前的项目结构和惯例

### 2. 系统化的实施流程

**系统地执行计划中的每项任务：**

1. **按顺序处理任务** - 严格遵循计划顺序，一次一项任务
2. **执行任何任务之前必须执行：**
   - **始终确保实施与计划中的特定任务相关联**
   - **始终从 `.copilot-tracking/details/**`** 中的关联详细信息 Markdown 文件中读取该任务的整个详细信息部分
   - **在继续之前充分了解所有实施细节**
   - 根据需要收集任何其他所需的上下文

3. **使用工作代码完全实现任务：**
   - 遵循工作区中的现有代码模式和约定
   - 创建满足详细信息中指定的所有任务要求的工作功能
   - 包括正确的错误处理、文档并遵循最佳实践

4. **标记任务完成并更新更改跟踪：**
   - 更新计划文件：将已完成任务的 `[ ]` 更改为 `[x]`
   - **完成每项任务后必须**：通过附加到相应的“已添加”、“已修改”或“已删除”部分以及相关文件路径和已实现内容的一句话摘要来更新更改文件
   - **强制**：如果任何更改与任务计划和详细信息存在差异，请在相关部分中明确指出更改是在计划之外进行的，并包括具体原因
   - 如果阶段中的所有任务均已完成 `[x]`，则将阶段标头标记为已完成 `[x]`

### 3. 执行质量标准

**每个实施必须：**
- 遵循现有的工作区模式和约定（检查 `copilot/` 文件夹中的标准）
- 实现满足所有任务要求的完整、有效的功能
- 包括适当的错误处理和验证
- 使用工作区中一致的命名约定和代码结构
- 为复杂的逻辑添加必要的文档和注释
- 确保与现有系统和依赖项的兼容性

### 4. 持续进步和验证

**执行每项任务后：**
1. 验证根据详细信息文件中的任务要求所做的更改
2. 在进行下一个任务之前解决任何问题
3. **强制**：更新计划文件以标记已完成的任务 `[x]`
4. **每项任务完成后都必须**：通过附加到“已添加”、“已修改”或“已删除”部分以及相关文件路径和已实现内容的一句话摘要来更新更改文件
5. 继续执行下一个未选中的任务

**继续直到：**
- 计划中的所有任务都标记为完成 `[x]`
- 所有指定的文件均已使用工作代码创建或更新
- 该计划的所有成功标准均已得到验证

### 5. 参考资料收集指南

**收集外部参考资料时：**
- 注重实际实施示例而不是理论文档
- 验证外部源包含实际可用的模式
- 调整外部模式以匹配工作空间惯例和标准

**根据参考实施时：**
- 首先遵循工作空间模式和约定，其次遵循外部模式
- 实现完整、有效的功能而不仅仅是示例
- 确保所有依赖项和配置都正确集成
- 确保实施工作在现有项目结构内进行

### 6. 完成和文件记录

**实施完成时：**
- 所有计划任务均标记为完成 `[x]`
- 所有指定的文件都与工作代码一起存在
- 计划中的所有成功标准均已验证
- 不存在任何实施错误

**最后一步 - 使用发布摘要更新更改文件：**
- 仅在所有阶段都标记为完成后添加发布摘要部分 `[x]`
- 记录完整的文件清单和发布文档的总体实施摘要

### 7. 问题解决

**遇到实施问题时：**
- 清楚地记录具体问题
- 尝试其他方法或搜索词
- 当外部引用失败时，使用工作区模式作为后备
- 继续使用现有信息而不是完全停止
- 在计划文件中记下任何未解决的问题以供将来参考

## 实施工作流程

```
1. Read and fully understand plan file and all checklists completely
2. Read and fully understand changes file completely (re-read entire file if missing context)
3. For each unchecked task:
   a. Read entire details section for that task from details markdown file
   b. Fully understand all implementation requirements
   c. Implement task with working code following workspace patterns
   d. Validate implementation meets task requirements
   e. Mark task complete [x] in plan file
   f. Update changes file with Added, Modified, or Removed entries
   g. Call out any divergences from plan/details within relevant sections with specific reasons
4. Repeat until all tasks complete
5. Only after ALL phases are complete [x]: Add final Release Summary to changes file
```

## 成功标准

当满足以下条件时，实施完成：
- ✅ 所有计划任务都标记为完成 `[x]`
- ✅ 所有指定的文件都包含工作代码
- ✅ 代码遵循工作区模式和约定
- ✅ 项目中的所有功能均按预期运行
- ✅ 每次任务完成后都会更新更改文件，其中包含添加、修改或删除的条目
- ✅ 更改文件记录所有阶段，并提供详细的发布就绪文档和最终发布摘要

## 模板更改文件

使用以下内容作为跟踪版本实施进度的更改文件的模板。
将 `{{ }}` 替换为适当的值。在 `./.copilot-tracking/changes/` 中创建此文件，文件名：`YYYYMMDD-task-description-changes.md`

**重要**：在每个任务完成后通过附加到“已添加”、“已修改”或“已删除”部分来更新此文件。
**强制**：始终在更改文件的顶部包含以下内容：`<!-- markdownlint-disable-file -->`

<!-- <更改模板> -->
```markdown
<!-- markdownlint-disable-file -->
# Release Changes: {{task name}}

**Related Plan**: {{plan-file-name}}
**Implementation Date**: {{YYYY-MM-DD}}

## Summary

{{Brief description of the overall changes made for this release}}

## Changes

### Added

- {{relative-file-path}} - {{one sentence summary of what was implemented}}

### Modified

- {{relative-file-path}} - {{one sentence summary of what was changed}}

### Removed

- {{relative-file-path}} - {{one sentence summary of what was removed}}

## Release Summary

**Total Files Affected**: {{number}}

### Files Created ({{count}})

- {{file-path}} - {{purpose}}

### Files Modified ({{count}})

- {{file-path}} - {{changes-made}}

### Files Removed ({{count}})

- {{file-path}} - {{reason}}

### Dependencies & Infrastructure

- **New Dependencies**: {{list-of-new-dependencies}}
- **Updated Dependencies**: {{list-of-updated-dependencies}}
- **Infrastructure Changes**: {{infrastructure-updates}}
- **Configuration Updates**: {{configuration-changes}}

### Deployment Notes

{{Any specific deployment considerations or steps}}
```
<!-- </changes-template> -->
