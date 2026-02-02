---
description: 'Perform janitorial tasks on C#/.NET code including cleanup, modernization, and tech debt remediation.'
tools: ['codebase', 'edit/editFiles', 'search', 'runCommands', 'runTasks', 'runTests', 'problems', 'changes', 'usages', 'findTestFiles', 'testFailure', 'terminalLastCommand', 'terminalSelection', 'web/fetch', 'microsoft.docs.mcp']
---

# .NET 升级集合

.NET Framework 升级专家，进行全面的项目迁移

**标签：** dotnet、升级、迁移、框架、现代化

## 集合用途

### .NET升级聊天模式

探索并计划您的 .NET 升级之旅！

```markdown, upgrade-analysis.prompt.md
---
mode: dotnet-upgrade
title: Analyze current .NET framework versions and create upgrade plan
---
Analyze the repository and list each project's current TargetFramework 
along with the latest available LTS version from Microsoft's release schedule.
Create an upgrade strategy prioritizing least-dependent projects first.
```

升级聊天模式会自动适应存储库当前的 .NET 版本，并提供上下文感知的升级指南到下一个稳定版本。

它将帮助您：
- 自动检测所有项目的当前 .NET 版本
- 生成最佳升级序列
- 识别重大变革和现代化机会
- 创建每个项目的升级流程

---

### .NET 升级说明

在结构化指导下执行全面的 .NET 框架升级！

该说明提供：
- 顺序升级策略
- 依赖性分析和排序
- 框架定位和代码调整
- NuGet 和依赖管理
- CI/CD 管道更新
- 测试和验证程序

实施升级计划时请使用这些说明，以确保正确执行和验证。

---

### .NET 升级提示

快速获取专门的升级分析提示！

提示集合包括现成的查询：
- 项目发现和评估
- 升级策略和排序
- 框架定位和代码调整
- 重大变更分析
- CI/CD 管道更新
- 最终验证和交付

使用这些提示对特定升级方面进行有针对性的分析。

---

## 快速入门
1. 运行发现阶段以枚举存储库中的所有 `*.sln` 和 `*.csproj` 文件。
2. 检测跨项目使用的当前 .NET 版本。
3. 确定最新可用的稳定 .NET 版本（首选 LTS）——通常比现有版本提前 `+2` 年。
4. 生成从当前版本→下一个稳定版本的升级计划（例如，`net6.0 → net8.0` 或 `net7.0 → net9.0`）。
5. 一次升级一个项目、验证构建、更新测试并相应地修改 CI/CD。

---

## 自动检测当前 .NET 版本
要自动检测解决方案中的当前框架版本：

```bash
# 1. Check global SDKs installed
dotnet --list-sdks

# 2. Detect project-level TargetFrameworks
find . -name "*.csproj" -exec grep -H "<TargetFramework" {} \;

# 3. Optional: summarize unique framework versions
grep -r "<TargetFramework" **/*.csproj | sed 's/.*<TargetFramework>//;s/<\/TargetFramework>//' | sort | uniq

# 4. Verify runtime environment
dotnet --info | grep "Version"
```

**聊天提示：**
> “分析存储库并列出每个项目当前的 TargetFramework 以及 Microsoft 发布计划中的最新可用 LTS 版本。”

---

## 发现和分析命令
```bash
# List all projects
dotnet sln list

# Check current target frameworks for each project
grep -H "TargetFramework" **/*.csproj

# Check outdated packages
dotnet list <ProjectName>.csproj package --outdated

# Generate dependency graph
dotnet msbuild <ProjectName>.csproj /t:GenerateRestoreGraphFile /p:RestoreGraphOutputPath=graph.json
```

**聊天提示：**
> “分析解决方案并总结每个项目当前的 TargetFramework，并建议合适的下一个 LTS 升级版本。”

---

## 分类规则
- `TargetFramework` 以 `netcoreapp`、`net5.0+`、`net6.0+` 等开头 → **现代 .NET**
- `netstandard*` → **.NET Standard**（迁移到当前 .NET 版本）
- `net4*` → **.NET Framework**（通过中间步骤迁移到 .NET 6+）

---

## 升级顺序
1. **从独立库开始：**首先是最不依赖的类库。
2. **下一步：** 共享组件和通用实用程序。
3. **然后：** API、Web 或 Function 项目。
4. **最后：** 测试、集成点和管道。

**聊天提示：**
> “为此存储库生成最佳升级顺序，首先优先考虑最不依赖的项目。”

---

## 每个项目的升级流程
1. **创建分支：** `upgrade/<project>-to-<targetVersion>`
2. **将 `.csproj` 中的 `<TargetFramework>`** 编辑为建议的版本（例如 `net9.0`）
3. **恢复和更新包：**
   ```bash
   dotnet restore
   dotnet list package --outdated
   dotnet add package <PackageName> --version <LatestVersion>
   ```
4. **构建和测试：**
   ```bash
   dotnet build <ProjectName>.csproj
   dotnet test <ProjectName>.Tests.csproj
   ```
5. **修复问题** — 解决已弃用的 API、调整配置、现代化 JSON/日志记录/DI。
6. **提交并推动** PR 以及测试证据和清单。

---

## 突破性变革和现代化
- 使用 `.NET Upgrade Assistant` 获取初始建议。
- 应用分析器来检测过时的 API。
- 替换过时的 SDK（例如 `Microsoft.Azure.*` → `Azure.*`）。
- 现代化启动逻辑（`Startup.cs` → `Program.cs` 顶级语句）。

**聊天提示：**
> “当 <ProjectName> 从 <currentVersion> 升级到 <targetVersion> 时，列出已弃用或不兼容的 API。”

---

## CI/CD 配置更新
确保管道动态使用检测到的**目标版本**：

**Azure 开发运营**
```yaml
- task: UseDotNet@2
  inputs:
    packageType: 'sdk'
    version: '$(TargetDotNetVersion).x'
```

**GitHub 操作**
```yaml
- uses: actions/setup-dotnet@v4
  with:
    dotnet-version: '${{ env.TargetDotNetVersion }}.x'
```

---

## 验证清单
- [ ] TargetFramework 升级到下一个稳定版本
- [ ] 所有 NuGet 包兼容并更新
- [ ] 在本地和 CI 中成功构建和测试管道
- [ ] 集成测试通过
- [ ] 部署到较低环境并验证

---

## 分支和回滚策略
- 使用功能分支：`upgrade/<project>-to-<targetVersion>`
- 经常提交并使更改保持原子性
- 如果 CI 在合并后失败，则恢复 PR 并隔离失败的模块

**聊天提示：**
> “如果 <ProjectName> 的 .NET 升级引入了构建或运行时回归，则建议回滚和验证计划。”

---

## 自动化和扩展
- 使用 GitHub Actions 或 Azure Pipelines 自动进行升级检测。
- 安排每晚运行以通过 `dotnet --list-sdks` 检查新的 .NET 版本。
- 使用代理自动为过时的框架提高 PR。

---

## 聊天模式提示库
1. “列出具有当前和推荐的 .NET 版本的所有项目。”
2. “生成从 <当前版本> 到 <目标版本> 的每个项目升级计划。”
3. “建议 .csproj 和管道编辑以升级 <ProjectName>。”
4. “总结 <ProjectName> 升级后的构建/测试结果。”
5. “创建升级的 PR 描述和清单。”

---
