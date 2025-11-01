---
description: '对 C#/.NET 代码执行清理任务，包括清理、现代化和技术债务修复。'
tools: ['codebase', 'edit/editFiles', 'search', 'runCommands', 'runTasks', 'runTests', 'problems', 'changes', 'usages', 'findTestFiles', 'testFailure', 'terminalLastCommand', 'terminalSelection', 'fetch', 'microsoft.docs.mcp']
---

# .NET 升级集合

用于综合项目迁移的 .NET Framework 升级专家

**标签：** dotnet, upgrade, migration, framework, modernization

## 集合使用

### .NET 升级聊天模式

发现并规划您的 .NET 升级之旅！

```markdown, upgrade-analysis.prompt.md
---
mode: dotnet-upgrade
title: 分析当前 .NET 框架版本并创建升级计划
---
分析存储库并列出每个项目的当前 TargetFramework
以及 Microsoft 发布计划中的最新可用 LTS 版本。
创建升级策略，优先升级最少依赖的项目。
```

升级聊天模式会自动适应您存储库的当前 .NET 版本，并提供针对下一稳定版本的上下文感知升级指导。

它将帮助您：
- 自动检测所有项目的当前 .NET 版本
- 生成最佳升级序列
- 识别破坏性更改和现代化机会
- 创建每个项目的升级流程

---

### .NET 升级指令

通过结构化指导执行全面的 .NET 框架升级！

指令提供：
- 顺序升级策略
- 依赖分析和排序
- 框架定位和代码调整
- NuGet 和依赖管理
- CI/CD 管道更新
- 测试和验证程序

在实施升级计划时使用这些指令以确保正确的执行和验证。

---

### .NET 升级提示

快速访问专业升级分析提示！

提示集合包含即用型查询：
- 项目发现和评估
- 升级策略和排序
- 框架定位和代码调整
- 破坏性更改分析
- CI/CD 管道更新
- 最终验证和交付

使用这些提示对特定升级方面进行针对性分析。

---

## 快速开始
1. 运行发现过程以枚举存储库中的所有 `*.sln` 和 `*.csproj` 文件。
2. 检测项目中使用的当前 .NET 版本。
3. 识别最新可用的稳定 .NET 版本（首选 LTS）——通常比现有版本领先 `+2` 年。
4. 生成从当前 → 下一稳定版本的升级计划（例如，`net6.0 → net8.0` 或 `net7.0 → net9.0`）。
5. 一次升级一个项目，验证构建，更新测试，并相应地修改 CI/CD。

---

## 自动检测当前 .NET 版本
自动检测解决方案中当前的框架版本：

```bash
# 1. 检查安装的全局 SDK
dotnet --list-sdks

# 2. 检测项目级 TargetFrameworks
find . -name "*.csproj" -exec grep -H "<TargetFramework" {} \;

# 3. 可选：总结唯一的框架版本
grep -r "<TargetFramework" **/*.csproj | sed 's/.*<TargetFramework>//;s/<\/TargetFramework>//' | sort | uniq

# 4. 验证运行时环境
dotnet --info | grep "Version"
```

**聊天提示：**
> "分析存储库并列出每个项目的当前 TargetFramework 以及 Microsoft 发布计划中的最新可用 LTS 版本。"

---

## 发现和分析命令
```bash
# 列出所有项目
dotnet sln list

# 检查每个项目的当前目标框架
grep -H "TargetFramework" **/*.csproj

# 检查过期包
dotnet list <ProjectName>.csproj package --outdated

# 生成依赖图
dotnet msbuild <ProjectName>.csproj /t:GenerateRestoreGraphFile /p:RestoreGraphOutputPath=graph.json
```

**聊天提示：**
> "分析解决方案并总结每个项目的当前 TargetFramework，并建议适当的下一 LTS 升级版本。"

---

## 分类规则
- `TargetFramework` 以 `netcoreapp`、`net5.0+`、`net6.0+` 等开头 → **现代 .NET**
- `netstandard*` → **.NET Standard**（迁移到当前 .NET 版本）
- `net4*` → **.NET Framework**（通过中间步骤迁移到 .NET 6+）

---

## 升级序列
1. **从独立库开始：** 首先升级最少依赖的类库。
2. **接下来：** 共享组件和通用工具。
3. **然后：** API、Web 或 Function 项目。
4. **最后：** 测试、集成点和管道。

**聊天提示：**
> "为此存储库生成最佳升级顺序，优先升级最少依赖的项目。"

---

## 每个项目升级流程
1. **创建分支：** `upgrade/<project>-to-<targetVersion>`
2. **编辑 `.csproj` 中的 `<TargetFramework>`** 到建议版本（例如，`net9.0`）
3. **恢复并更新包：**
   ```bash
   dotnet restore
   dotnet list package --outdated
   dotnet add package <PackageName> --version <LatestVersion>
   ```
4. **构建并测试：**
   ```bash
   dotnet build <ProjectName>.csproj
   dotnet test <ProjectName>.Tests.csproj
   ```
5. **修复问题** —— 解决过时的 API、调整配置、现代化 JSON/日志/DI。
6. **提交并推送** 带有测试证据和检查清单的 PR。

---

## 破坏性更改和现代化
- 使用 `.NET Upgrade Assistant` 获得初步建议。
- 应用分析器检测过时的 API。
- 替换过时的 SDK（例如，`Microsoft.Azure.*` → `Azure.*`）。
- 现代化启动逻辑（`Startup.cs` → `Program.cs` 顶级语句）。

**聊天提示：**
> "列出从 <currentVersion> 升级到 <targetVersion> 时 <ProjectName> 的过时或不兼容的 API。"

---

## CI/CD 配置更新
确保管道动态使用检测到的**目标版本**：

**Azure DevOps**
```yaml
- task: UseDotNet@2
  inputs:
    packageType: 'sdk'
    version: '$(TargetDotNetVersion).x'
```

**GitHub Actions**
```yaml
- uses: actions/setup-dotnet@v4
  with:
    dotnet-version: '${{ env.TargetDotNetVersion }}.x'
```

---

## 验证检查清单
- [ ] TargetFramework 升级到下一稳定版本
- [ ] 所有 NuGet 包兼容并已更新
- [ ] 构建和测试管道在本地和 CI 中成功
- [ ] 集成测试通过
- [ ] 部署到低级环境并验证

---

## 分支和回滚策略
- 使用功能分支：`upgrade/<project>-to-<targetVersion>`
- 频繁提交并保持更改原子性
- 如果合并后 CI 失败，还原 PR 并隔离失败的模块

**聊天提示：**
> "如果 <ProjectName> 的 .NET 升级引入构建或运行时回归，建议回滚和验证计划。"

---

## 自动化和扩展
- 使用 GitHub Actions 或 Azure Pipelines 自动化升级检测。
- 安排夜间运行通过 `dotnet --list-sdks` 检查新的 .NET 版本。
- 使用代理自动为过时的框架创建 PR。

---

## 聊天模式提示库
1. "列出所有项目及其当前和建议的 .NET 版本。"
2. "生成从 <currentVersion> 到 <targetVersion> 的每个项目升级计划。"
3. "建议升级 <ProjectName> 的 .csproj 和管道编辑。"
4. "总结 <ProjectName> 升级后的构建/测试结果。"
5. "为升级创建 PR 描述和检查清单。"

---