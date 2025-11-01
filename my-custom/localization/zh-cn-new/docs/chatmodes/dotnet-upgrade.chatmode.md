---
description: '对C#/.NET代码执行维护任务，包括清理、现代化和技术债务修复。'
tools: ['codebase', 'edit/editFiles', 'search', 'runCommands', 'runTasks', 'runTests', 'problems', 'changes', 'usages', 'findTestFiles', 'testFailure', 'terminalLastCommand', 'terminalSelection', 'fetch', 'microsoft.docs.mcp']
---

# .NET升级集合

综合项目迁移的.NET Framework升级专家

**标签：** dotnet, upgrade, migration, framework, modernization

## 集合使用

### .NET升级聊天模式

发现并规划你的.NET升级之旅！

```markdown, upgrade-analysis.prompt.md
---
mode: dotnet-upgrade
title: 分析当前.NET框架版本并创建升级计划
---
分析存储库并列出每个项目的当前TargetFramework
以及Microsoft发布计划中最新可用的LTS版本。
创建优先处理最少依赖项目的升级策略。
```

升级聊天模式自动适应存储库的当前.NET版本，并提供上下文感知的升级指导到下一个稳定版本。

它将帮助你：
- 自动检测所有项目的当前.NET版本
- 生成最优升级序列
- 识别破坏性变更和现代化机会
- 创建每个项目的升级流程

---

### .NET升级指令

使用结构化指导执行全面的.NET框架升级！

指令提供：
- 顺序升级策略
- 依赖分析和排序
- 框架定位和代码调整
- NuGet和依赖管理
- CI/CD管道更新
- 测试和验证程序

在实施升级计划时使用这些指令以确保正确的执行和验证。

---

### .NET升级提示

快速访问专门升级分析提示！

提示集合包括即用型查询：
- 项目发现和评估
- 升级策略和排序
- 框架定位和代码调整
- 破坏性变更分析
- CI/CD管道更新
- 最终验证和交付

使用这些提示进行特定升级方面的针对性分析。

---

## 快速开始
1. 运行发现遍举以枚举存储库中所有`*.sln`和`*.csproj`文件。
2. 检测项目中使用的当前.NET版本。
3. 识别最新可用的稳定.NET版本（首选LTS）— 通常比现有版本`+2`年。
4. 生成从当前→下一个稳定版本的升级计划（例如，`net6.0 → net8.0`，或`net7.0 → net9.0`）。
5. 一次升级一个项目，验证构建，更新测试，并相应修改CI/CD。

---

## 自动检测当前.NET版本
要自动检测解决方案中当前的框架版本：

```bash
# 1. 检查全局安装的SDK
dotnet --list-sdks

# 2. 检测项目级TargetFrameworks
find . -name "*.csproj" -exec grep -H "<TargetFramework" {} \;

# 3. 可选：汇总唯一框架版本
grep -r "<TargetFramework" **/*.csproj | sed 's/.*<TargetFramework>//;s/<\/TargetFramework>//' | sort | uniq

# 4. 验证运行时环境
dotnet --info | grep "Version"
```

**聊天提示：**
> "分析存储库并列出每个项目的当前TargetFramework以及Microsoft发布计划中最新可用的LTS版本。"

---

## 发现和分析命令
```bash
# 列出所有项目
dotnet sln list

# 检查每个项目的当前目标框架
grep -H "TargetFramework" **/*.csproj

# 检查过期的包
dotnet list <ProjectName>.csproj package --outdated

# 生成依赖图
dotnet msbuild <ProjectName>.csproj /t:GenerateRestoreGraphFile /p:RestoreGraphOutputPath=graph.json
```

**聊天提示：**
> "分析解决方案并总结每个项目的当前TargetFramework并建议适当的下一个LTS升级版本。"

---

## 分类规则
- `TargetFramework`以`netcoreapp`、`net5.0+`、`net6.0+`等开头 → **现代.NET**
- `netstandard*` → **.NET Standard**（迁移到当前.NET版本）
- `net4*` → **.NET Framework**（通过中间步骤迁移到.NET 6+）

---

## 升级序列
1. **从独立库开始**：首先升级最少依赖的类库。
2. **接下来**：共享组件和通用工具。
3. **然后**：API、Web或Function项目。
4. **最后**：测试、集成点和管道。

**聊天提示：**
> "为这个存储库生成最优升级顺序，优先处理最少依赖的项目。"

---

## 每个项目升级流程
1. **创建分支**：`upgrade/<project>-to-<targetVersion>`
2. **在`.csproj`中编辑`<TargetFramework>`**到建议版本（例如，`net9.0`）
3. **恢复和更新包**：
   ```bash
   dotnet restore
   dotnet list package --outdated
   dotnet add package <PackageName> --version <LatestVersion>
   ```
4. **构建和测试**：
   ```bash
   dotnet build <ProjectName>.csproj
   dotnet test <ProjectName>.Tests.csproj
   ```
5. **修复问题** — 解决过时的API，调整配置，现代化JSON/logging/DI。
6. **提交和推送**带有测试证据和检查表的PR。

---

## 破坏性变更和现代化
- 使用`.NET升级助手`进行初始建议。
- 应用分析器检测过时的API。
- 替换过时的SDK（例如，`Microsoft.Azure.*` → `Azure.*`）。
- 现代化启动逻辑（`Startup.cs` → `Program.cs`顶级语句）。

**聊天提示：**
> "列出从<currentVersion>升级到<targetVersion>时<ProjectName>的过时或不兼容API。"

---

## CI/CD配置更新
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

## 验证检查表
- [ ] TargetFramework升级到下一个稳定版本
- [ ] 所有NuGet包兼容并已更新
- [ ] 构建和测试管道在本地和CI中成功
- [ ] 集成测试通过
- [ ] 部署到较低环境并验证

---

## 分支和回滚策略
- 使用功能分支：`upgrade/<project>-to-<targetVersion>`
- 频繁提交并保持更改原子化
- 如果合并后CI失败，回滚PR并隔离失败模块

**聊天提示：**
> "如果<ProjectName>的.NET升级引入构建或运行时回归，建议回滚和验证计划。"

---

## 自动化和扩展
- 使用GitHub Actions或Azure管道自动化升级检测。
- 安排夜间运行以通过`dotnet --list-sdks`检查新的.NET发布。
- 使用代理自动为过期框架提起PR。

---

## 聊天模式提示库
1. "列出所有项目及其当前和建议的.NET版本。"
2. "生成从<currentVersion>到<targetVersion>的每个项目升级计划。"
3. "建议升级<ProjectName>的.csproj和管道编辑。"
4. "总结<ProjectName>升级后的构建/测试结果。"
5. "为升级创建PR描述和检查表。"

---