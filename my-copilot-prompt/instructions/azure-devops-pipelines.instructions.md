---
description: 'Best practices for Azure DevOps Pipeline YAML files'
applyTo: '**/azure-pipelines.yml, **/azure-pipelines*.yml, **/*.pipeline.yml'
---

# Azure DevOps 管道 YAML 最佳实践

## 一般准则

- 使用与正确缩进一致的 YAML 语法（2 个空格）
- 始终包含管道、阶段、作业和步骤的有意义的名称和显示名称
- 实施适当的错误处理和条件执行
- 使用变量和参数使管道可重用和可维护
- 服务连接和权限遵循最小特权原则
- 包括用于故障排除的全面日志记录和诊断

## 管道结构

- 使用阶段组织复杂的管道，以实现更好的可视化和控制
- 使用作业对相关步骤进行分组并在可能的情况下启用并行执行
- 在阶段和作业之间实现适当的依赖关系
- 使用可重用管道组件的模板
- 保持管道文件集中和模块化 - 将大型管道拆分为多个文件

## 构建最佳实践

- 使用特定代理池版本和 VM 映像以保持一致性
- 缓存依赖项（npm、NuGet、Maven 等）以提高构建性能
- 使用有意义的名称和保留策略实施适当的工件管理
- 使用版本号和构建元数据的构建变量
- 包括代码质量关卡（linting、测试、安全扫描）
- 确保构建可重复且独立于环境

## 测试集成

- 作为构建过程的一部分运行单元测试
- 以标准格式（JUnit、VSTest 等）发布测试结果
- 包括代码覆盖率报告和质量门
- 在适当的阶段实施集成和端到端测试
- 在可用时使用测试影响分析来优化测试执行
- 测试失败时快速失败以提供快速反馈

## 安全考虑

- 使用 Azure Key Vault 进行敏感配置和机密
- 使用可变组实施适当的秘密管理
- 使用具有最少所需权限的服务连接
- 启用安全扫描（依赖漏洞、静态分析）
- 实施生产部署审批门
- 尽可能使用托管身份而不是服务主体

## 部署策略

- 实施适当的环境升级（开发→登台→生产）
- 使用具有适当环境目标的部署作业
- 适当时实施蓝绿或金丝雀部署策略
- 包括回滚机制和健康检查
- 使用基础设施即代码（ARM、Bicep、Terraform）来实现一致的部署
- 每个环境实施适当的配置管理

## 变量和参数管理

- 使用变量组跨管道共享配置
- 实现运行时参数以实现灵活的管道执行
- 根据分支或环境使用条件变量
- 保护敏感变量并将其标记为秘密
- 记录变量的用途和期望值
- 使用变量模板来实现复杂的变量逻辑

## 性能优化

- 适当时使用并行作业和矩阵策略
- 为依赖项和构建输出实施适当的缓存策略
- 当不需要完整历史记录时，使用浅克隆进行 Git 操作
- 通过多阶段构建和层缓存优化 Docker 镜像构建
- 监控管道性能并优化瓶颈
- 高效使用管道资源触发器

## 监控和可观察性

- 包括整个管道的全面日志记录
- 使用 Azure Monitor 和 Application Insights 进行部署跟踪
- 针对失败和成功实施适当的通知策略
- 包括部署运行状况检查和自动回滚触发器
- 使用管道分析来识别改进机会
- 记录管道行为和故障排除步骤

## 模板和可重用性

- 为常见模式创建管道模板
- 使用扩展模板实现完整的管道继承
- 实施可重用任务序列的步骤模板
- 使用变量模板来实现复杂的变量逻辑
- 适当的版本模板以确保稳定性
- 文档模板参数及使用示例

## 分支和触发策略

- 为不同的分支类型实施适当的触发器
- 使用路径过滤器仅在相关文件发生更改时触发构建
- 为主/主分支配置适当的 CI/CD 触发器
- 使用拉取请求触发器进行代码验证
- 实施维护任务的计划触发器
- 考虑多存储库场景的资源触发器

## 结构示例

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
    displayName: 'Build and Test'
    jobs:
      - job: Build
        displayName: 'Build Application'
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: UseDotNet@2
            displayName: 'Use .NET SDK'
            inputs:
              version: '8.x'
          
          - task: DotNetCoreCLI@2
            displayName: 'Restore dependencies'
            inputs:
              command: 'restore'
              projects: '**/*.csproj'
          
          - task: DotNetCoreCLI@2
            displayName: 'Build application'
            inputs:
              command: 'build'
              projects: '**/*.csproj'
              arguments: '--configuration $(buildConfiguration) --no-restore'

  - stage: Deploy
    displayName: 'Deploy to Staging'
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployToStaging
        displayName: 'Deploy to Staging Environment'
        environment: 'staging'
        strategy:
          runOnce:
            deploy:
              steps:
                - download: current
                  displayName: 'Download drop artifact'
                  artifact: drop
                - task: AzureWebApp@1
                  displayName: 'Deploy to Azure Web App'
                  inputs:
                    azureSubscription: 'staging-service-connection'
                    appType: 'webApp'
                    appName: 'myapp-staging'
                    package: '$(Pipeline.Workspace)/drop/**/*.zip'
```

## 要避免的常见反模式

- 直接在 YAML 文件中对敏感值进行硬编码
- 使用过于广泛的触发器会导致不必要的构建
- 在单个阶段中混合构建和部署逻辑
- 没有实施正确的错误处理和清理
- 在没有升级计划的情况下使用已弃用的任务版本
- 创建难以维护的整体管道
- 为了清晰起见，未使用正确的命名约定
- 忽略管道安全最佳实践
