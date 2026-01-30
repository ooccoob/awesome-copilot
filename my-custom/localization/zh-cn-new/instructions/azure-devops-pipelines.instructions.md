---
description: 'Azure DevOps Pipeline YAML文件最佳实践'
applyTo: '**/azure-pipelines.yml, **/azure-pipelines*.yml, **/*.pipeline.yml'
---

# Azure DevOps Pipeline YAML最佳实践

## 通用指导原则

- 一致地使用YAML语法并采用适当的缩进（2个空格）
- 始终为管道、阶段、作业和步骤包含有意义的名称和显示名称
- 实施适当的错误处理和条件执行
- 使用变量和参数使管道可重用和可维护
- 遵循服务连接和权限的最小权限原则
- 包含全面的日志记录和诊断以便故障排除

## 管道结构

- 使用阶段组织复杂管道以获得更好的可视化和控制
- 使用作业对相关步骤进行分组，并在可能时启用并行执行
- 在阶段和作业之间实施适当的依赖关系
- 为可重用的管道组件使用模板
- 保持管道文件专注和模块化 - 将大型管道拆分为多个文件

## 构建最佳实践

- 使用特定的代理池版本和VM镜像以确保一致性
- 缓存依赖项（npm、NuGet、Maven等）以提高构建性能
- 实施适当的构件管理，使用有意义的名称和保留策略
- 使用构建变量表示版本号和构建元数据
- 包含代码质量门控（代码检查、测试、安全扫描）
- 确保构建是可重现的且与环境无关

## 测试集成

- 将单元测试作为构建过程的一部分运行
- 以标准格式发布测试结果（JUnit、VSTest等）
- 包含代码覆盖率报告和质量门控
- 在适当阶段实施集成和端到端测试
- 在可用时使用测试影响分析以优化测试执行
- 在测试失败时快速失败以提供快速反馈

## 安全考虑

- 使用Azure Key Vault处理敏感配置和机密
- 使用变量组实施适当的机密管理
- 使用具有最小所需权限的服务连接
- 启用安全扫描（依赖项漏洞、静态分析）
- 为生产部署实施审批门控
- 尽可能使用托管身份而不是服务主体

## 部署策略

- 实施适当的环境提升（开发 → 预发布 → 生产）
- 使用具有适当环境目标的部署作业
- 在适当时实施蓝绿或金丝雀部署策略
- 包含回滚机制和健康检查
- 使用基础设施即代码（ARM、Bicep、Terraform）以确保部署一致性
- 为每个环境实施适当的配置管理

## 变量和参数管理

- 使用变量组实现跨管道的共享配置
- 实施运行时参数以实现灵活的管道执行
- 基于分支或环境使用条件变量
- 保护敏感变量并将其标记为机密
- 记录变量用途和预期值
- 使用变量模板处理复杂的变量逻辑

## 性能优化

- 在适当时使用并行作业和矩阵策略
- 为依赖项和构建输出实施适当的缓存策略
- 在不需要完整历史时使用Git浅克隆
- 使用多阶段构建和层缓存优化Docker镜像构建
- 监控管道性能并优化瓶颈
- 高效使用管道资源触发器

## 监控和可观察性

- 在整个管道中包含全面的日志记录
- 使用Azure Monitor和Application Insights进行部署跟踪
- 为失败和成功实施适当的通知策略
- 包含部署健康检查和自动回滚触发器
- 使用管道分析识别改进机会
- 记录管道行为和故障排除步骤

## 模板和可重用性

- 为常见模式创建管道模板
- 使用extends模板实现完整的管道继承
- 为可重用的任务序列实施步骤模板
- 使用变量模板处理复杂的变量逻辑
- 适当版本化模板以确保稳定性
- 记录模板参数和使用示例

## 分支和触发器策略

- 为不同分支类型实施适当的触发器
- 使用路径过滤器仅在相关文件更改时触发构建
- 为主/主分支配置适当的CI/CD触发器
- 使用拉取请求触发器进行代码验证
- 为维护任务实施计划触发器
- 考虑多仓库场景的资源触发器

## 示例结构

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
      - main
      - develop
  paths:
    exclude:
      - docs/*
      - README.md

variables:
  - group: shared-variables
  - name: buildConfiguration
    value: 'Release'

stages:
  - stage: Build
    displayName: '构建和测试'
    jobs:
      - job: Build
        displayName: '构建应用程序'
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: UseDotNet@2
            displayName: '使用.NET SDK'
            inputs:
              version: '8.x'

          - task: DotNetCoreCLI@2
            displayName: '恢复依赖项'
            inputs:
              command: 'restore'
              projects: '**/*.csproj'

          - task: DotNetCoreCLI@2
            displayName: '构建应用程序'
            inputs:
              command: 'build'
              projects: '**/*.csproj'
              arguments: '--configuration $(buildConfiguration) --no-restore'

  - stage: Deploy
    displayName: '部署到预发布环境'
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployToStaging
        displayName: '部署到预发布环境'
        environment: 'staging'
        strategy:
          runOnce:
            deploy:
              steps:
                - download: current
                  displayName: '下载drop构件'
                  artifact: drop
                - task: AzureWebApp@1
                  displayName: '部署到Azure Web应用'
                  inputs:
                    azureSubscription: 'staging-service-connection'
                    appType: 'webApp'
                    appName: 'myapp-staging'
                    package: '$(Pipeline.Workspace)/drop/**/*.zip'
```

## 要避免的常见反模式

- 直接在YAML文件中硬编码敏感值
- 使用过于宽泛的触发器导致不必要的构建
- 在单个阶段混合构建和部署逻辑
- 不实施适当的错误处理和清理
- 使用已弃用的任务版本而没有升级计划
- 创建难以维护的单体管道
- 不使用适当的命名约定以确保清晰性
- 忽略管道安全最佳实践