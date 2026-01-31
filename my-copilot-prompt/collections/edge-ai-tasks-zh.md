# microsoft/edge-ai 的任务

适用于中级到专家用户和大型代码库的任务研究员和任务规划器 - 由 microsoft/edge-ai 为您提供

**标签：** 架构、规划、研究、任务、实施

## 该系列中的项目

|标题 |类型 |描述 | MCP 服务器 |
| ----- | ---- | ----------- | ----------- |
| [任务计划执行说明](../instructions/task-implementation.instructions-zh.md)<br />[![在VS中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Ftask-implementation.instructions.md)<br />[![安装在 VS 代码中内部人员](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/instructions?url=vscode-insiders%3Achat-instructions%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Finstructions%2Ftask-implementation.instructions.md) |说明 |通过渐进式跟踪和更改记录实施任务计划的说明 - 由 microsoft/edge-ai 为您提供 [请参阅用法](#task-plan-implementation-instructions) |  |
| [任务计划器说明](../agents/task-planner.agent-zh.md)<br />[![在 VS 中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Ftask-planner.agent.md)<br />[![在 VS Code 中安装业内人士](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode-insiders%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Ftask-planner.agent.md) |代理|用于创建可操作实施计划的任务规划器 - 由 microsoft/edge-ai 为您提供 [查看用法](#task-planner-instructions) |  |
| [任务研究员说明](../agents/task-researcher.agent-zh.md)<br />[![在VS中安装代码](https://img.shields.io/badge/VS_Code-Install-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Ftask-researcher.agent.md)<br />[![在 VS Code 中安装内部人士](https://img.shields.io/badge/VS_Code_Insiders-Install-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://aka.ms/awesome-copilot/install/agent?url=vscode-insiders%3Achat-agent%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fagents%2Ftask-researcher.agent.md) |代理|用于综合项目分析的任务研究专家 - 由 microsoft/edge-ai 为您提供 [查看用法](#task-researcher-instructions) |  |

## 集合用途

### 任务计划实施说明

继续使用 `task-planner` 迭代该计划，直到您完全完成您想要对代码库执行的操作。

当您准备好实施该计划时，**创建一个新的聊天**并切换到 `Agent` 模式，然后触发新生成的提示。

```markdown, implement-fabric-rti-changes.prompt.md
---
mode: agent
title: Implement microsoft fabric realtime intelligence terraform support
---
/implement-fabric-rti-blueprint-modification phaseStop=true
```

此提示的另一个好处是可以将计划作为说明附加，这有助于在整个对话中保持计划的上下文。

**专家警告** ->>使用 `phaseStop=false` 让 Copilot 不间断地执行整个计划。此外，您可以使用 `taskStop=true` 让 Copilot 在每次任务执行后停止，以实现更精细的细节控制。

要使用这些生成的说明和提示，您需要相应地更新您的 `settings.json` ：

```json
    "chat.instructionsFilesLocations": {
        // Existing instructions folders...
        ".copilot-tracking/plans": true
    },
    "chat.promptFilesLocations": {
        // Existing prompts folders...
        ".copilot-tracking/prompts": true
    },
```

---

### 任务计划说明

此外，任务研究员将提供额外的实施想法，您可以与 GitHub Copilot 合作选择合适的重点。

```markdown, task-plan.prompt.md
---
mode: task-planner
title: Plan microsoft fabric realtime intelligence terraform support
---
#file: .copilot-tracking/research/*-fabric-rti-blueprint-modification-research.md
Build a plan to support adding fabric rti to this project
```

`task-planner` 将帮助您制定实施任务的计划。它将使用您充分研究的想法或建立新的研究（如果尚未提供）。

`task-planner` 将生成三 (3) 个由 `task-implementation.instructions.md` 使用的文件。

* __代码0__

  * 新生成的说明文件，其中包含作为阶段和任务清单的计划。
* __代码0__

  * 实施的细节，计划文件请参阅此文件以了解具体细节（如果您有一个大计划，这一点很重要）。
* __代码0__

  * 新生成的提示文件将创建 `.copilot-tracking/changes/*-changes.md` 文件并继续实施更改。

继续使用 `task-planner` 迭代该计划，直到您完全完成您想要对代码库执行的操作。

---

### 任务研究员指示

现在您可以针对您的任务迭代研究！

```markdown, research.prompt.md
---
mode: task-researcher
title: Research microsoft fabric realtime intelligence terraform support
---
Review the microsoft documentation for fabric realtime intelligence
and come up with ideas on how to implement this support into our terraform components.
```

研究被转储到 .copilot-tracking/research/*-research.md 文件中，并将包括 GHCP 的发现以及在实施过程中有用的示例和模式。

此外，任务研究员将提供额外的实施想法，您可以与 GitHub Copilot 合作选择合适的重点。

---

