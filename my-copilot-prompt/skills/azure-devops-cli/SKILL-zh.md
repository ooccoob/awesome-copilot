---
名称：azure-devops-cli
描述：通过 CLI 管理 Azure DevOps 资源，包括项目、存储库、管道、构建、拉取请求、工作项、工件和服务端点。使用 Azure DevOps、az 命令、devops 自动化、CI/CD 或用户提及 Azure DevOps CLI 时使用。
---

# Azure DevOps CLI

此技能有助于使用 Azure CLI 和 Azure DevOps 扩展来管理 Azure DevOps 资源。

**CLI 版本：** 2.81.0（截至 2025 年当前）

## 先决条件

安装 Azure CLI 和 Azure DevOps 扩展：

```bash
# Install Azure CLI
brew install azure-cli  # macOS
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash  # Linux
pip install azure-cli  # via pip

# Verify installation
az --version

# Install Azure DevOps extension
az extension add --name azure-devops
az extension show --name azure-devops
```

## CLI结构

```
az devops          # Main DevOps commands
├── admin          # Administration (banner)
├── extension      # Extension management
├── project        # Team projects
├── security       # Security operations
│   ├── group      # Security groups
│   └── permission # Security permissions
├── service-endpoint # Service connections
├── team           # Teams
├── user           # Users
├── wiki           # Wikis
├── configure      # Set defaults
├── invoke         # Invoke REST API
├── login          # Authenticate
└── logout         # Clear credentials

az pipelines       # Azure Pipelines
├── agent          # Agents
├── build          # Builds
├── folder         # Pipeline folders
├── pool           # Agent pools
├── queue          # Agent queues
├── release        # Releases
├── runs           # Pipeline runs
├── variable       # Pipeline variables
└── variable-group # Variable groups

az boards          # Azure Boards
├── area           # Area paths
├── iteration      # Iterations
└── work-item      # Work items

az repos           # Azure Repos
├── import         # Git imports
├── policy         # Branch policies
├── pr             # Pull requests
└── ref            # Git references

az artifacts       # Azure Artifacts
└── universal      # Universal Packages
    ├── download   # Download packages
    └── publish    # Publish packages
```

## 认证

### 登录 Azure DevOps

```bash
# Interactive login (prompts for PAT)
az devops login --organization https://dev.azure.com/{org}

# Login with PAT token
az devops login --organization https://dev.azure.com/{org} --token YOUR_PAT_TOKEN

# Logout
az devops logout --organization https://dev.azure.com/{org}
```

### 配置默认值

```bash
# Set default organization and project
az devops configure --defaults organization=https://dev.azure.com/{org} project={project}

# List current configuration
az devops configure --list

# Enable Git aliases
az devops configure --use-git-aliases true
```

## 扩展管理

### 列表扩展

```bash
# List available extensions
az extension list-available --output table

# List installed extensions
az extension list --output table
```

### 管理 Azure DevOps 扩展

```bash
# Install Azure DevOps extension
az extension add --name azure-devops

# Update Azure DevOps extension
az extension update --name azure-devops

# Remove extension
az extension remove --name azure-devops

# Install from local path
az extension add --source ~/extensions/azure-devops.whl
```

## 项目

### 列出项目

```bash
az devops project list --organization https://dev.azure.com/{org}
az devops project list --top 10 --output table
```

### 创建项目

```bash
az devops project create \
  --name myNewProject \
  --organization https://dev.azure.com/{org} \
  --description "My new DevOps project" \
  --source-control git \
  --visibility private
```

### 显示项目详情

```bash
az devops project show --project {project-name} --org https://dev.azure.com/{org}
```

### 删除项目

```bash
az devops project delete --id {project-id} --org https://dev.azure.com/{org} --yes
```

## 存储库

### 列出存储库

```bash
az repos list --org https://dev.azure.com/{org} --project {project}
az repos list --output table
```

### 显示存储库详细信息

```bash
az repos show --repository {repo-name} --project {project}
```

### 创建存储库

```bash
az repos create --name {repo-name} --project {project}
```

### 删除存储库

```bash
az repos delete --id {repo-id} --project {project} --yes
```

### 更新存储库

```bash
az repos update --id {repo-id} --name {new-name} --project {project}
```

## 存储库导入

### 导入 Git 存储库

```bash
# Import from public Git repository
az repos import create \
  --git-source-url https://github.com/user/repo \
  --repository {repo-name}

# Import with authentication
az repos import create \
  --git-source-url https://github.com/user/private-repo \
  --repository {repo-name} \
  --user {username} \
  --password {password-or-pat}
```

## 请求请求

### 创建拉取请求

```bash
# Basic PR creation
az repos pr create \
  --repository {repo} \
  --source-branch {source-branch} \
  --target-branch {target-branch} \
  --title "PR Title" \
  --description "PR description" \
  --open

# PR with work items
az repos pr create \
  --repository {repo} \
  --source-branch {source-branch} \
  --work-items 63 64

# Draft PR with reviewers
az repos pr create \
  --repository {repo} \
  --source-branch feature/new-feature \
  --target-branch main \
  --title "Feature: New functionality" \
  --draft true \
  --reviewers user1@example.com user2@example.com \
  --required-reviewers lead@example.com \
  --labels "enhancement" "backlog"
```

### 列出拉取请求

```bash
# All PRs
az repos pr list --repository {repo}

# Filter by status
az repos pr list --repository {repo} --status active

# Filter by creator
az repos pr list --repository {repo} --creator {email}

# Output as table
az repos pr list --repository {repo} --output table
```

### 显示公关详情

```bash
az repos pr show --id {pr-id}
az repos pr show --id {pr-id} --open  # Open in browser
```

### 更新 PR（完成/放弃/草稿）

```bash
# Complete PR
az repos pr update --id {pr-id} --status completed

# Abandon PR
az repos pr update --id {pr-id} --status abandoned

# Set to draft
az repos pr update --id {pr-id} --draft true

# Publish draft PR
az repos pr update --id {pr-id} --draft false

# Auto-complete when policies pass
az repos pr update --id {pr-id} --auto-complete true

# Set title and description
az repos pr update --id {pr-id} --title "New title" --description "New description"
```

### 本地查看 PR

```bash
# Checkout PR branch
az repos pr checkout --id {pr-id}

# Checkout with specific remote
az repos pr checkout --id {pr-id} --remote-name upstream
```

### 公关投票

```bash
az repos pr set-vote --id {pr-id} --vote approve
az repos pr set-vote --id {pr-id} --vote approve-with-suggestions
az repos pr set-vote --id {pr-id} --vote reject
az repos pr set-vote --id {pr-id} --vote wait-for-author
az repos pr set-vote --id {pr-id} --vote reset
```

### 公关评论员

```bash
# Add reviewers
az repos pr reviewer add --id {pr-id} --reviewers user1@example.com user2@example.com

# List reviewers
az repos pr reviewer list --id {pr-id}

# Remove reviewers
az repos pr reviewer remove --id {pr-id} --reviewers user1@example.com
```

### 公关工作项目

```bash
# Add work items to PR
az repos pr work-item add --id {pr-id} --work-items {id1} {id2}

# List PR work items
az repos pr work-item list --id {pr-id}

# Remove work items from PR
az repos pr work-item remove --id {pr-id} --work-items {id1}
```

### 公关政策

```bash
# List policies for a PR
az repos pr policy list --id {pr-id}

# Queue policy evaluation for a PR
az repos pr policy queue --id {pr-id} --evaluation-id {evaluation-id}
```

## 管道

### 列出管道

```bash
az pipelines list --output table
az pipelines list --query "[?name=='myPipeline']"
az pipelines list --folder-path 'folder/subfolder'
```

### 创建管道

```bash
# From local repository context (auto-detects settings)
az pipelines create --name 'ContosoBuild' --description 'Pipeline for contoso project'

# With specific branch and YAML path
az pipelines create \
  --name {pipeline-name} \
  --repository {repo} \
  --branch main \
  --yaml-path azure-pipelines.yml \
  --description "My CI/CD pipeline"

# For GitHub repository
az pipelines create \
  --name 'GitHubPipeline' \
  --repository https://github.com/Org/Repo \
  --branch main \
  --repository-type github

# Skip first run
az pipelines create --name 'MyPipeline' --skip-run true
```

### 显示管道

```bash
az pipelines show --id {pipeline-id}
az pipelines show --name {pipeline-name}
```

### 更新管道

```bash
az pipelines update --id {pipeline-id} --name "New name" --description "Updated description"
```

### 删除管道

```bash
az pipelines delete --id {pipeline-id} --yes
```

### 运行管道

```bash
# Run by name
az pipelines run --name {pipeline-name} --branch main

# Run by ID
az pipelines run --id {pipeline-id} --branch refs/heads/main

# With parameters
az pipelines run --name {pipeline-name} --parameters version=1.0.0 environment=prod

# With variables
az pipelines run --name {pipeline-name} --variables buildId=123 configuration=release

# Open results in browser
az pipelines run --name {pipeline-name} --open
```

## 管道运行

### 列表运行

```bash
az pipelines runs list --pipeline {pipeline-id}
az pipelines runs list --name {pipeline-name} --top 10
az pipelines runs list --branch main --status completed
```

### 显示运行详细信息

```bash
az pipelines runs show --run-id {run-id}
az pipelines runs show --run-id {run-id} --open
```

### 管道工件

```bash
# List artifacts for a run
az pipelines runs artifact list --run-id {run-id}

# Download artifact
az pipelines runs artifact download \
  --artifact-name '{artifact-name}' \
  --path {local-path} \
  --run-id {run-id}

# Upload artifact
az pipelines runs artifact upload \
  --artifact-name '{artifact-name}' \
  --path {local-path} \
  --run-id {run-id}
```

### 管道运行标签

```bash
# Add tag to run
az pipelines runs tag add --run-id {run-id} --tags production v1.0

# List run tags
az pipelines runs tag list --run-id {run-id} --output table
```

## 构建

### 列表构建

```bash
az pipelines build list
az pipelines build list --definition {build-definition-id}
az pipelines build list --status completed --result succeeded
```

### 队列构建

```bash
az pipelines build queue --definition {build-definition-id} --branch main
az pipelines build queue --definition {build-definition-id} --parameters version=1.0.0
```

### 显示构建详细信息

```bash
az pipelines build show --id {build-id}
```

### 取消构建

```bash
az pipelines build cancel --id {build-id}
```

### 构建标签

```bash
# Add tag to build
az pipelines build tag add --build-id {build-id} --tags prod release

# Delete tag from build
az pipelines build tag delete --build-id {build-id} --tag prod
```

## 构建定义

### 列出构建定义

```bash
az pipelines build definition list
az pipelines build definition list --name {definition-name}
```

### 显示构建定义

```bash
az pipelines build definition show --id {definition-id}
```

## 发布

### 列表发布

```bash
az pipelines release list
az pipelines release list --definition {release-definition-id}
```

### 创建发布

```bash
az pipelines release create --definition {release-definition-id}
az pipelines release create --definition {release-definition-id} --description "Release v1.0"
```

### 展会发布

```bash
az pipelines release show --id {release-id}
```

## 发布定义

### 列出发布定义

```bash
az pipelines release definition list
```

### 显示发布定义

```bash
az pipelines release definition show --id {definition-id}
```

## 管道变量

### 列出变量

```bash
az pipelines variable list --pipeline-id {pipeline-id}
```

### 创建变量

```bash
# Non-secret variable
az pipelines variable create \
  --name {var-name} \
  --value {var-value} \
  --pipeline-id {pipeline-id}

# Secret variable
az pipelines variable create \
  --name {var-name} \
  --secret true \
  --pipeline-id {pipeline-id}

# Secret with prompt
az pipelines variable create \
  --name {var-name} \
  --secret true \
  --prompt true \
  --pipeline-id {pipeline-id}
```

### 更新变量

```bash
az pipelines variable update \
  --name {var-name} \
  --value {new-value} \
  --pipeline-id {pipeline-id}

# Update secret variable
az pipelines variable update \
  --name {var-name} \
  --secret true \
  --value "{new-secret-value}" \
  --pipeline-id {pipeline-id}
```

### 删除变量

```bash
az pipelines variable delete --name {var-name} --pipeline-id {pipeline-id} --yes
```

## 变量组

### 列出变量组

```bash
az pipelines variable-group list
az pipelines variable-group list --output table
```

### 显示变量组

```bash
az pipelines variable-group show --id {group-id}
```

### 创建变量组

```bash
az pipelines variable-group create \
  --name {group-name} \
  --variables key1=value1 key2=value2 \
  --authorize true
```

### 更新变量组

```bash
az pipelines variable-group update \
  --id {group-id} \
  --name {new-name} \
  --description "Updated description"
```

### 删除变量组

```bash
az pipelines variable-group delete --id {group-id} --yes
```

### 变量组变量

#### 列出变量

```bash
az pipelines variable-group variable list --group-id {group-id}
```

#### 创建变量

```bash
# Non-secret variable
az pipelines variable-group variable create \
  --group-id {group-id} \
  --name {var-name} \
  --value {var-value}

# Secret variable (will prompt for value if not provided)
az pipelines variable-group variable create \
  --group-id {group-id} \
  --name {var-name} \
  --secret true

# Secret with environment variable
export AZURE_DEVOPS_EXT_PIPELINE_VAR_MySecret=secretvalue
az pipelines variable-group variable create \
  --group-id {group-id} \
  --name MySecret \
  --secret true
```

#### 更新变量

```bash
az pipelines variable-group variable update \
  --group-id {group-id} \
  --name {var-name} \
  --value {new-value} \
  --secret false
```

#### 删除变量

```bash
az pipelines variable-group variable delete \
  --group-id {group-id} \
  --name {var-name}
```

## 管道文件夹

### 列出文件夹

```bash
az pipelines folder list
```

### 创建文件夹

```bash
az pipelines folder create --path 'folder/subfolder' --description "My folder"
```

### 删除文件夹

```bash
az pipelines folder delete --path 'folder/subfolder'
```

### 更新文件夹

```bash
az pipelines folder update --path 'old-folder' --new-path 'new-folder'
```

## 代理池

### 列出代理池

```bash
az pipelines pool list
az pipelines pool list --pool-type automation
az pipelines pool list --pool-type deployment
```

### 显示代理池

```bash
az pipelines pool show --pool-id {pool-id}
```

## 座席队列

### 列出代理队列

```bash
az pipelines queue list
az pipelines queue list --pool-name {pool-name}
```

### 显示代理队列

```bash
az pipelines queue show --id {queue-id}
```

## 工作项目（板）

### 查询工作项

```bash
# WIQL query
az boards query \
  --wiql "SELECT [System.Id], [System.Title], [System.State] FROM WorkItems WHERE [System.AssignedTo] = @Me AND [System.State] = 'Active'"

# Query with output format
az boards query --wiql "SELECT * FROM WorkItems" --output table
```

### 显示工作项

```bash
az boards work-item show --id {work-item-id}
az boards work-item show --id {work-item-id} --open
```

### 创建工作项

```bash
# Basic work item
az boards work-item create \
  --title "Fix login bug" \
  --type Bug \
  --assigned-to user@example.com \
  --description "Users cannot login with SSO"

# With area and iteration
az boards work-item create \
  --title "New feature" \
  --type "User Story" \
  --area "Project\\Area1" \
  --iteration "Project\\Sprint 1"

# With custom fields
az boards work-item create \
  --title "Task" \
  --type Task \
  --fields "Priority=1" "Severity=2"

# With discussion comment
az boards work-item create \
  --title "Issue" \
  --type Bug \
  --discussion "Initial investigation completed"

# Open in browser after creation
az boards work-item create --title "Bug" --type Bug --open
```

### 更新工作项

```bash
# Update state, title, and assignee
az boards work-item update \
  --id {work-item-id} \
  --state "Active" \
  --title "Updated title" \
  --assigned-to user@example.com

# Move to different area
az boards work-item update \
  --id {work-item-id} \
  --area "{ProjectName}\\{Team}\\{Area}"

# Change iteration
az boards work-item update \
  --id {work-item-id} \
  --iteration "{ProjectName}\\Sprint 5"

# Add comment/discussion
az boards work-item update \
  --id {work-item-id} \
  --discussion "Work in progress"

# Update with custom fields
az boards work-item update \
  --id {work-item-id} \
  --fields "Priority=1" "StoryPoints=5"
```

### 删除工作项

```bash
# Soft delete (can be restored)
az boards work-item delete --id {work-item-id} --yes

# Permanent delete
az boards work-item delete --id {work-item-id} --destroy --yes
```

### 工作项关系

```bash
# List relations
az boards work-item relation list --id {work-item-id}

# List supported relation types
az boards work-item relation list-type

# Add relation
az boards work-item relation add --id {work-item-id} --relation-type parent --target-id {parent-id}

# Remove relation
az boards work-item relation remove --id {work-item-id} --relation-id {relation-id}
```

## 区域路径

### 列出项目区域

```bash
az boards area project list --project {project}
az boards area project show --path "Project\\Area1" --project {project}
```

### 创建区域

```bash
az boards area project create --path "Project\\NewArea" --project {project}
```

### 更新区

```bash
az boards area project update \
  --path "Project\\OldArea" \
  --new-path "Project\\UpdatedArea" \
  --project {project}
```

### 删除区域

```bash
az boards area project delete --path "Project\\AreaToDelete" --project {project} --yes
```

### 区域团队管理

```bash
# List areas for team
az boards area team list --team {team-name} --project {project}

# Add area to team
az boards area team add \
  --team {team-name} \
  --path "Project\\NewArea" \
  --project {project}

# Remove area from team
az boards area team remove \
  --team {team-name} \
  --path "Project\\AreaToRemove" \
  --project {project}

# Update team area
az boards area team update \
  --team {team-name} \
  --path "Project\\Area" \
  --project {project} \
  --include-sub-areas true
```

## 迭代

### 列出项目的迭代

```bash
az boards iteration project list --project {project}
az boards iteration project show --path "Project\\Sprint 1" --project {project}
```

### 创建迭代

```bash
az boards iteration project create --path "Project\\Sprint 1" --project {project}
```

### 更新迭代

```bash
az boards iteration project update \
  --path "Project\\OldSprint" \
  --new-path "Project\\NewSprint" \
  --project {project}
```

### 删除迭代

```bash
az boards iteration project delete --path "Project\\OldSprint" --project {project} --yes
```

### 列出团队的迭代

```bash
az boards iteration team list --team {team-name} --project {project}
```

### 将迭代添加到团队

```bash
az boards iteration team add \
  --team {team-name} \
  --path "Project\\Sprint 1" \
  --project {project}
```

### 从团队中删除迭代

```bash
az boards iteration team remove \
  --team {team-name} \
  --path "Project\\Sprint 1" \
  --project {project}
```

### 列出迭代中的工作项

```bash
az boards iteration team list-work-items \
  --team {team-name} \
  --path "Project\\Sprint 1" \
  --project {project}
```

### 为团队设置默认迭代

```bash
az boards iteration team set-default-iteration \
  --team {team-name} \
  --path "Project\\Sprint 1" \
  --project {project}
```

### 显示默认迭代

```bash
az boards iteration team show-default-iteration \
  --team {team-name} \
  --project {project}
```

### 为团队设置待办事项列表迭代

```bash
az boards iteration team set-backlog-iteration \
  --team {team-name} \
  --path "Project\\Sprint 1" \
  --project {project}
```

### 显示积压迭代

```bash
az boards iteration team show-backlog-iteration \
  --team {team-name} \
  --project {project}
```

### 显示当前迭代

```bash
az boards iteration team show --team {team-name} --project {project} --timeframe current
```

## Git 参考资料

### 列出参考文献（分支）

```bash
az repos ref list --repository {repo}
az repos ref list --repository {repo} --query "[?name=='refs/heads/main']"
```

### 创建参考（分支）

```bash
az repos ref create --name refs/heads/new-branch --object-type commit --object {commit-sha}
```

### 删除参考（分支）

```bash
az repos ref delete --name refs/heads/old-branch --repository {repo} --project {project}
```

### 锁科

```bash
az repos ref lock --name refs/heads/main --repository {repo} --project {project}
```

### 解锁分支

```bash
az repos ref unlock --name refs/heads/main --repository {repo} --project {project}
```

## 存储库策略

### 列出所有政策

```bash
az repos policy list --repository {repo-id} --branch main
```

### 使用配置文件创建策略

```bash
az repos policy create --config policy.json
```

### 更新/删除策略

```bash
# Update
az repos policy update --id {policy-id} --config updated-policy.json

# Delete
az repos policy delete --id {policy-id} --yes
```

### 保单类型

#### 批准者计数策略

```bash
az repos policy approver-count create \
  --blocking true \
  --enabled true \
  --branch main \
  --repository-id {repo-id} \
  --minimum-approver-count 2 \
  --creator-vote-counts true
```

#### 制定政策

```bash
az repos policy build create \
  --blocking true \
  --enabled true \
  --branch main \
  --repository-id {repo-id} \
  --build-definition-id {definition-id} \
  --queue-on-source-update-only true \
  --valid-duration 720
```

#### 工作项链接策略

```bash
az repos policy work-item-linking create \
  --blocking true \
  --branch main \
  --enabled true \
  --repository-id {repo-id}
```

#### 所需审稿人政策

```bash
az repos policy required-reviewer create \
  --blocking true \
  --enabled true \
  --branch main \
  --repository-id {repo-id} \
  --required-reviewers user@example.com
```

#### 合并策略政策

```bash
az repos policy merge-strategy create \
  --blocking true \
  --enabled true \
  --branch main \
  --repository-id {repo-id} \
  --allow-squash true \
  --allow-rebase true \
  --allow-no-fast-forward true
```

#### 案件执行政策

```bash
az repos policy case-enforcement create \
  --blocking true \
  --enabled true \
  --branch main \
  --repository-id {repo-id}
```

#### 需要评论的政策

```bash
az repos policy comment-required create \
  --blocking true \
  --enabled true \
  --branch main \
  --repository-id {repo-id}
```

#### 文件大小政策

```bash
az repos policy file-size create \
  --blocking true \
  --enabled true \
  --branch main \
  --repository-id {repo-id} \
  --maximum-file-size 10485760  # 10MB in bytes
```

## 服务端点

### 列出服务端点

```bash
az devops service-endpoint list --project {project}
az devops service-endpoint list --project {project} --output table
```

### 显示服务端点

```bash
az devops service-endpoint show --id {endpoint-id} --project {project}
```

### 创建服务端点

```bash
# Using configuration file
az devops service-endpoint create --service-endpoint-configuration endpoint.json --project {project}
```

### 删除服务端点

```bash
az devops service-endpoint delete --id {endpoint-id} --project {project} --yes
```

## 团队

### 列出团队

```bash
az devops team list --project {project}
```

### 表演团队

```bash
az devops team show --team {team-name} --project {project}
```

### 创建团队

```bash
az devops team create \
  --name {team-name} \
  --description "Team description" \
  --project {project}
```

### 更新团队

```bash
az devops team update \
  --team {team-name} \
  --project {project} \
  --name "{new-team-name}" \
  --description "Updated description"
```

### 删除团队

```bash
az devops team delete --team {team-name} --project {project} --yes
```

### 显示团队成员

```bash
az devops team list-member --team {team-name} --project {project}
```

## 用户

### 列出用户

```bash
az devops user list --org https://dev.azure.com/{org}
az devops user list --top 10 --output table
```

### 显示用户

```bash
az devops user show --user {user-id-or-email} --org https://dev.azure.com/{org}
```

### 添加用户

```bash
az devops user add \
  --email user@example.com \
  --license-type express \
  --org https://dev.azure.com/{org}
```

### 更新用户

```bash
az devops user update \
  --user {user-id-or-email} \
  --license-type advanced \
  --org https://dev.azure.com/{org}
```

### 删除用户

```bash
az devops user remove --user {user-id-or-email} --org https://dev.azure.com/{org} --yes
```

## 安全组

### 列出组

```bash
# List all groups in project
az devops security group list --project {project}

# List all groups in organization
az devops security group list --scope organization

# List with filtering
az devops security group list --project {project} --subject-types vstsgroup
```

### 显示组详细信息

```bash
az devops security group show --group-id {group-id}
```

### 创建群组

```bash
az devops security group create \
  --name {group-name} \
  --description "Group description" \
  --project {project}
```

### 更新组

```bash
az devops security group update \
  --group-id {group-id} \
  --name "{new-group-name}" \
  --description "Updated description"
```

### 删除组

```bash
az devops security group delete --group-id {group-id} --yes
```

### 团体会员资格

```bash
# List memberships
az devops security group membership list --id {group-id}

# Add member
az devops security group membership add \
  --group-id {group-id} \
  --member-id {member-id}

# Remove member
az devops security group membership remove \
  --group-id {group-id} \
  --member-id {member-id} --yes
```

## 安全权限

### 列出命名空间

```bash
az devops security permission namespace list
```

### 显示命名空间详细信息

```bash
# Show permissions available in a namespace
az devops security permission namespace show --namespace "GitRepositories"
```

### 列出权限

```bash
# List permissions for user/group and namespace
az devops security permission list \
  --id {user-or-group-id} \
  --namespace "GitRepositories" \
  --project {project}

# List for specific token (repository)
az devops security permission list \
  --id {user-or-group-id} \
  --namespace "GitRepositories" \
  --project {project} \
  --token "repoV2/{project}/{repository-id}"
```

### 显示权限

```bash
az devops security permission show \
  --id {user-or-group-id} \
  --namespace "GitRepositories" \
  --project {project} \
  --token "repoV2/{project}/{repository-id}"
```

### 更新权限

```bash
# Grant permission
az devops security permission update \
  --id {user-or-group-id} \
  --namespace "GitRepositories" \
  --project {project} \
  --token "repoV2/{project}/{repository-id}" \
  --permission-mask "Pull,Contribute"

# Deny permission
az devops security permission update \
  --id {user-or-group-id} \
  --namespace "GitRepositories" \
  --project {project} \
  --token "repoV2/{project}/{repository-id}" \
  --permission-mask 0
```

### 重置权限

```bash
# Reset specific permission bits
az devops security permission reset \
  --id {user-or-group-id} \
  --namespace "GitRepositories" \
  --project {project} \
  --token "repoV2/{project}/{repository-id}" \
  --permission-mask "Pull,Contribute"

# Reset all permissions
az devops security permission reset-all \
  --id {user-or-group-id} \
  --namespace "GitRepositories" \
  --project {project} \
  --token "repoV2/{project}/{repository-id}" --yes
```

## 维基百科

### 列出维基百科

```bash
# List all wikis in project
az devops wiki list --project {project}

# List all wikis in organization
az devops wiki list
```

### 显示维基

```bash
az devops wiki show --wiki {wiki-name} --project {project}
az devops wiki show --wiki {wiki-name} --project {project} --open
```

### 创建维基

```bash
# Create project wiki
az devops wiki create \
  --name {wiki-name} \
  --project {project} \
  --type projectWiki

# Create code wiki from repository
az devops wiki create \
  --name {wiki-name} \
  --project {project} \
  --type codeWiki \
  --repository {repo-name} \
  --mapped-path /wiki
```

### 删除维基

```bash
az devops wiki delete --wiki {wiki-id} --project {project} --yes
```

### 维基页面

```bash
# List pages
az devops wiki page list --wiki {wiki-name} --project {project}

# Show page
az devops wiki page show \
  --wiki {wiki-name} \
  --path "/page-name" \
  --project {project}

# Create page
az devops wiki page create \
  --wiki {wiki-name} \
  --path "/new-page" \
  --content "# New Page\n\nPage content here..." \
  --project {project}

# Update page
az devops wiki page update \
  --wiki {wiki-name} \
  --path "/existing-page" \
  --content "# Updated Page\n\nNew content..." \
  --project {project}

# Delete page
az devops wiki page delete \
  --wiki {wiki-name} \
  --path "/old-page" \
  --project {project} --yes
```

## 行政管理

### 横幅管理

```bash
# List banners
az devops admin banner list

# Show banner details
az devops admin banner show --id {banner-id}

# Add new banner
az devops admin banner add \
  --message "System maintenance scheduled" \
  --level info  # info, warning, error

# Update banner
az devops admin banner update \
  --id {banner-id} \
  --message "Updated message" \
  --level warning \
  --expiration-date "2025-12-31T23:59:59Z"

# Remove banner
az devops admin banner remove --id {banner-id}
```

## 开发运营扩展

管理安装在 Azure DevOps 组织中的扩展（与 CLI 扩展不同）。

```bash
# List installed extensions
az devops extension list --org https://dev.azure.com/{org}

# Search marketplace extensions
az devops extension search --search-query "docker"

# Show extension details
az devops extension show --ext-id {extension-id} --org https://dev.azure.com/{org}

# Install extension
az devops extension install \
  --ext-id {extension-id} \
  --org https://dev.azure.com/{org} \
  --publisher {publisher-id}

# Enable extension
az devops extension enable \
  --ext-id {extension-id} \
  --org https://dev.azure.com/{org}

# Disable extension
az devops extension disable \
  --ext-id {extension-id} \
  --org https://dev.azure.com/{org}

# Uninstall extension
az devops extension uninstall \
  --ext-id {extension-id} \
  --org https://dev.azure.com/{org} --yes
```

## 通用包

### 发布包

```bash
az artifacts universal publish \
  --feed {feed-name} \
  --name {package-name} \
  --version {version} \
  --path {package-path} \
  --project {project}
```

### 下载包

```bash
az artifacts universal download \
  --feed {feed-name} \
  --name {package-name} \
  --version {version} \
  --path {download-path} \
  --project {project}
```

## 代理商

### 列出池中的代理

```bash
az pipelines agent list --pool-id {pool-id}
```

### 显示代理详细信息

```bash
az pipelines agent show --agent-id {agent-id} --pool-id {pool-id}
```

## Git 别名

启用 git 别名后：

```bash
# Enable Git aliases
az devops configure --use-git-aliases true

# Use Git commands for DevOps operations
git pr create --target-branch main
git pr list
git pr checkout 123
```

## 输出格式

所有命令都支持多种输出格式：

```bash
# Table format (human-readable)
az pipelines list --output table

# JSON format (default, machine-readable)
az pipelines list --output json

# JSONC (colored JSON)
az pipelines list --output jsonc

# YAML format
az pipelines list --output yaml

# YAMLC (colored YAML)
az pipelines list --output yamlc

# TSV format (tab-separated values)
az pipelines list --output tsv

# None (no output)
az pipelines list --output none
```

## JMES路径查询

过滤和转换输出：

```bash
# Filter by name
az pipelines list --query "[?name=='myPipeline']"

# Get specific fields
az pipelines list --query "[].{Name:name, ID:id}"

# Chain queries
az pipelines list --query "[?name.contains('CI')].{Name:name, ID:id}" --output table

# Get first result
az pipelines list --query "[0]"

# Get top N
az pipelines list --query "[0:5]"
```

## 全球争论

适用于所有命令：

- `--help` / `-h`：显示帮助
- `--output` / `-o`：输出格式（json、jsonc、none、table、tsv、yaml、yamlc）
- `--query`：JMESPath 查询字符串
- `--verbose`：增加日志记录的详细程度
- `--debug`：显示所有调试日志
- `--only-show-errors`：仅显示错误，抑制警告
- `--subscription`：订阅名称或ID

## 常用参数

|参数|描述 |
| -------------------------- | ------------------------------------------------------------------- |
| __代码0__ / __代码1__ | Azure DevOps 组织 URL（例如 `https://dev.azure.com/{org}`）|
| __代码0__ / __代码1__ |项目名称或ID |
| __代码0__ |从 git config 自动检测组织 |
| __代码0__ / __代码1__ |跳过确认提示 |
| __代码0__ |在网络浏览器中打开 |

## 通用工作流程

### 从当前分支创建 PR

```bash
CURRENT_BRANCH=$(git branch --show-current)
az repos pr create \
  --source-branch $CURRENT_BRANCH \
  --target-branch main \
  --title "Feature: $(git log -1 --pretty=%B)" \
  --open
```

### 创建有关管道故障的工作项

```bash
az boards work-item create \
  --title "Build $BUILD_BUILDNUMBER failed" \
  --type bug \
  --org $SYSTEM_TEAMFOUNDATIONCOLLECTIONURI \
  --project $SYSTEM_TEAMPROJECT
```

### 下载最新的管道工件

```bash
RUN_ID=$(az pipelines runs list --pipeline {pipeline-id} --top 1 --query "[0].id" -o tsv)
az pipelines runs artifact download \
  --artifact-name 'webapp' \
  --path ./output \
  --run-id $RUN_ID
```

### 批准并完成 PR

```bash
# Vote approve
az repos pr set-vote --id {pr-id} --vote approve

# Complete PR
az repos pr update --id {pr-id} --status completed
```

### 从本地存储库创建管道

```bash
# From local git repository (auto-detects repo, branch, etc.)
az pipelines create --name 'CI-Pipeline' --description 'Continuous Integration'
```

### 批量更新工作项

```bash
# Query items and update in loop
for id in $(az boards query --wiql "SELECT ID FROM WorkItems WHERE State='New'" -o tsv); do
  az boards work-item update --id $id --state "Active"
done
```

## 最佳实践

### 身份验证和安全

```bash
# Use PAT from environment variable (most secure)
export AZURE_DEVOPS_EXT_PAT=$MY_PAT
az devops login --organization $ORG_URL

# Pipe PAT securely (avoids shell history)
echo $MY_PAT | az devops login --organization $ORG_URL

# Set defaults to avoid repetition
az devops configure --defaults organization=$ORG_URL project=$PROJECT

# Clear credentials after use
az devops logout --organization $ORG_URL
```

### 幂等操作

```bash
# Always use --detect for auto-detection
az devops configure --defaults organization=$ORG_URL project=$PROJECT

# Check existence before creation
if ! az pipelines show --id $PIPELINE_ID 2>/dev/null; then
  az pipelines create --name "$PIPELINE_NAME" --yaml-path azure-pipelines.yml
fi

# Use --output tsv for shell parsing
PIPELINE_ID=$(az pipelines list --query "[?name=='MyPipeline'].id" --output tsv)

# Use --output json for programmatic access
BUILD_STATUS=$(az pipelines build show --id $BUILD_ID --query "status" --output json)
```

### 脚本安全输出

```bash
# Suppress warnings and errors
az pipelines list --only-show-errors

# No output (useful for commands that only need to execute)
az pipelines run --name "$PIPELINE_NAME" --output none

# TSV format for shell scripts (clean, no formatting)
az repos pr list --output tsv --query "[].{ID:pullRequestId,Title:title}"

# JSON with specific fields
az pipelines list --output json --query "[].{Name:name, ID:id, URL:url}"
```

### 管道编排

```bash
# Run pipeline and wait for completion
RUN_ID=$(az pipelines run --name "$PIPELINE_NAME" --query "id" -o tsv)

while true; do
  STATUS=$(az pipelines runs show --run-id $RUN_ID --query "status" -o tsv)
  if [[ "$STATUS" != "inProgress" && "$STATUS" != "notStarted" ]]; then
    break
  fi
  sleep 10
done

# Check result
RESULT=$(az pipelines runs show --run-id $RUN_ID --query "result" -o tsv)
if [[ "$RESULT" == "succeeded" ]]; then
  echo "Pipeline succeeded"
else
  echo "Pipeline failed with result: $RESULT"
  exit 1
fi
```

### 变量组管理

```bash
# Create variable group idempotently
VG_NAME="production-variables"
VG_ID=$(az pipelines variable-group list --query "[?name=='$VG_NAME'].id" -o tsv)

if [[ -z "$VG_ID" ]]; then
  VG_ID=$(az pipelines variable-group create \
    --name "$VG_NAME" \
    --variables API_URL=$API_URL API_KEY=$API_KEY \
    --authorize true \
    --query "id" -o tsv)
  echo "Created variable group with ID: $VG_ID"
else
  echo "Variable group already exists with ID: $VG_ID"
fi
```

### 服务连接自动化

```bash
# Create service connection using configuration file
cat > service-connection.json <<'EOF'
{
  "data": {
    "subscriptionId": "$SUBSCRIPTION_ID",
    "subscriptionName": "My Subscription",
    "creationMode": "Manual",
    "serviceEndpointId": "$SERVICE_ENDPOINT_ID"
  },
  "url": "https://management.azure.com/",
  "authorization": {
    "parameters": {
      "tenantid": "$TENANT_ID",
      "serviceprincipalid": "$SP_ID",
      "authenticationType": "spnKey",
      "serviceprincipalkey": "$SP_KEY"
    },
    "scheme": "ServicePrincipal"
  },
  "type": "azurerm",
  "isShared": false,
  "isReady": true
}
EOF

az devops service-endpoint create \
  --service-endpoint-configuration service-connection.json \
  --project "$PROJECT"
```

### 拉取请求自动化

```bash
# Create PR with work items and reviewers
PR_ID=$(az repos pr create \
  --repository "$REPO_NAME" \
  --source-branch "$FEATURE_BRANCH" \
  --target-branch main \
  --title "Feature: $(git log -1 --pretty=%B)" \
  --description "$(git log -1 --pretty=%B)" \
  --work-items $WORK_ITEM_1 $WORK_ITEM_2 \
  --reviewers "$REVIEWER_1" "$REVIEWER_2" \
  --required-reviewers "$LEAD_EMAIL" \
  --labels "enhancement" "backlog" \
  --open \
  --query "pullRequestId" -o tsv)

# Set auto-complete when policies pass
az repos pr update --id $PR_ID --auto-complete true
```

## 错误处理和重试模式

### 短暂故障的重试逻辑

```bash
# Retry function for network operations
retry_command() {
  local max_attempts=3
  local attempt=1
  local delay=5

  while [[ $attempt -le $max_attempts ]]; do
    if "$@"; then
      return 0
    fi
    echo "Attempt $attempt failed. Retrying in ${delay}s..."
    sleep $delay
    ((attempt++))
    delay=$((delay * 2))
  done

  echo "All $max_attempts attempts failed"
  return 1
}

# Usage
retry_command az pipelines run --name "$PIPELINE_NAME"
```

### 检查并处理错误

```bash
# Check if pipeline exists before operations
PIPELINE_ID=$(az pipelines list --query "[?name=='$PIPELINE_NAME'].id" -o tsv)

if [[ -z "$PIPELINE_ID" ]]; then
  echo "Pipeline not found. Creating..."
  az pipelines create --name "$PIPELINE_NAME" --yaml-path azure-pipelines.yml
else
  echo "Pipeline exists with ID: $PIPELINE_ID"
fi
```

### 验证输入

```bash
# Validate required parameters
if [[ -z "$PROJECT" || -z "$REPO" ]]; then
  echo "Error: PROJECT and REPO must be set"
  exit 1
fi

# Check if branch exists
if ! az repos ref list --repository "$REPO" --query "[?name=='refs/heads/$BRANCH']" -o tsv | grep -q .; then
  echo "Error: Branch $BRANCH does not exist"
  exit 1
fi
```

### 处理权限错误

```bash
# Try operation, handle permission errors
if az devops security permission update \
  --id "$USER_ID" \
  --namespace "GitRepositories" \
  --project "$PROJECT" \
  --token "repoV2/$PROJECT/$REPO_ID" \
  --allow-bit 2 \
  --deny-bit 0 2>&1 | grep -q "unauthorized"; then
  echo "Error: Insufficient permissions to update repository permissions"
  exit 1
fi
```

### 管道故障通知

```bash
# Run pipeline and check result
RUN_ID=$(az pipelines run --name "$PIPELINE_NAME" --query "id" -o tsv)

# Wait for completion
while true; do
  STATUS=$(az pipelines runs show --run-id $RUN_ID --query "status" -o tsv)
  if [[ "$STATUS" != "inProgress" && "$STATUS" != "notStarted" ]]; then
    break
  fi
  sleep 10
done

# Check result and create work item on failure
RESULT=$(az pipelines runs show --run-id $RUN_ID --query "result" -o tsv)
if [[ "$RESULT" != "succeeded" ]]; then
  BUILD_NUMBER=$(az pipelines runs show --run-id $RUN_ID --query "buildNumber" -o tsv)

  az boards work-item create \
    --title "Build $BUILD_NUMBER failed" \
    --type Bug \
    --description "Pipeline run $RUN_ID failed with result: $RESULT\n\nURL: $ORG_URL/$PROJECT/_build/results?buildId=$RUN_ID"
fi
```

### 优雅的降级

```bash
# Try to download artifact, fallback to alternative source
if ! az pipelines runs artifact download \
  --artifact-name 'webapp' \
  --path ./output \
  --run-id $RUN_ID 2>/dev/null; then
  echo "Warning: Failed to download from pipeline run. Falling back to backup source..."

  # Alternative download method
  curl -L "$BACKUP_URL" -o ./output/backup.zip
fi
```

## 高级 JMESPath 查询

### 过滤和排序

```bash
# Filter by multiple conditions
az pipelines list --query "[?name.contains('CI') && enabled==true]"

# Filter by status and result
az pipelines runs list --query "[?status=='completed' && result=='succeeded']"

# Sort by date (descending)
az pipelines runs list --query "sort_by([?status=='completed'], &finishTime | reverse(@))"

# Get top N items after filtering
az pipelines runs list --query "[?result=='succeeded'] | [0:5]"
```

### 嵌套查询

```bash
# Extract nested properties
az pipelines show --id $PIPELINE_ID --query "{Name:name, Repo:repository.{Name:name, Type:type}, Folder:folder}"

# Query build details
az pipelines build show --id $BUILD_ID --query "{ID:id, Number:buildNumber, Status:status, Result:result, Requested:requestedFor.displayName}"
```

### 复杂过滤

```bash
# Find pipelines with specific YAML path
az pipelines list --query "[?process.type.name=='yaml' && process.yamlFilename=='azure-pipelines.yml']"

# Find PRs from specific reviewer
az repos pr list --query "[?contains(reviewers[?displayName=='John Doe'].displayName, 'John Doe')]"

# Find work items with specific iteration and state
az boards work-item show --id $WI_ID --query "{Title:fields['System.Title'], State:fields['System.State'], Iteration:fields['System.IterationPath']}"
```

### 聚合

```bash
# Count items by status
az pipelines runs list --query "groupBy([?status=='completed'], &[result]) | {Succeeded: [?key=='succeeded'][0].count, Failed: [?key=='failed'][0].count}"

# Get unique reviewers
az repos pr list --query "unique_by(reviewers[], &displayName)"

# Sum values
az pipelines runs list --query "[?result=='succeeded'] | [].{Duration:duration} | [0].Duration"
```

### 条件变换

```bash
# Format dates
az pipelines runs list --query "[].{ID:id, Date:createdDate, Formatted:createdDate | format_datetime(@, 'yyyy-MM-dd HH:mm')}"

# Conditional output
az pipelines list --query "[].{Name:name, Status:(enabled ? 'Enabled' : 'Disabled')}"

# Extract with defaults
az pipelines show --id $PIPELINE_ID --query "{Name:name, Folder:folder || 'Root', Description:description || 'No description'}"
```

### 复杂的工作流程

```bash
# Find longest running builds
az pipelines build list --query "sort_by([?result=='succeeded'], &queueTime) | reverse(@) | [0:3].{ID:id, Number:buildNumber, Duration:duration}"

# Get PR statistics per reviewer
az repos pr list --query "groupBy([], &reviewers[].displayName) | [].{Reviewer:@.key, Count:length(@)}"

# Find work items with multiple child items
az boards work-item relation list --id $PARENT_ID --query "[?rel=='System.LinkTypes.Hierarchy-Forward'] | [].{ChildID:url | split('/', @) | [-1]}"
```

## 幂等操作的脚本模式

### 创建或更新模式

```bash
# Ensure pipeline exists, update if different
ensure_pipeline() {
  local name=$1
  local yaml_path=$2

  PIPELINE=$(az pipelines list --query "[?name=='$name']" -o json)

  if [[ -z "$PIPELINE" ]]; then
    echo "Creating pipeline: $name"
    az pipelines create --name "$name" --yaml-path "$yaml_path"
  else
    echo "Pipeline exists: $name"
  fi
}
```

### 确保变量组

```bash
# Create variable group with idempotent updates
ensure_variable_group() {
  local vg_name=$1
  shift
  local variables=("$@")

  VG_ID=$(az pipelines variable-group list --query "[?name=='$vg_name'].id" -o tsv)

  if [[ -z "$VG_ID" ]]; then
    echo "Creating variable group: $vg_name"
    VG_ID=$(az pipelines variable-group create \
      --name "$vg_name" \
      --variables "${variables[@]}" \
      --authorize true \
      --query "id" -o tsv)
  else
    echo "Variable group exists: $vg_name (ID: $VG_ID)"
  fi

  echo "$VG_ID"
}
```

### 确保服务连接

```bash
# Check if service connection exists, create if not
ensure_service_connection() {
  local name=$1
  local project=$2

  SC_ID=$(az devops service-endpoint list \
    --project "$project" \
    --query "[?name=='$name'].id" \
    -o tsv)

  if [[ -z "$SC_ID" ]]; then
    echo "Service connection not found. Creating..."
    # Create logic here
  else
    echo "Service connection exists: $name"
    echo "$SC_ID"
  fi
}
```

### 幂等工作项创建

```bash
# Create work item only if doesn't exist with same title
create_work_item_if_new() {
  local title=$1
  local type=$2

  WI_ID=$(az boards query \
    --wiql "SELECT ID FROM WorkItems WHERE [System.WorkItemType]='$type' AND [System.Title]='$title'" \
    --query "[0].id" -o tsv)

  if [[ -z "$WI_ID" ]]; then
    echo "Creating work item: $title"
    WI_ID=$(az boards work-item create --title "$title" --type "$type" --query "id" -o tsv)
  else
    echo "Work item exists: $title (ID: $WI_ID)"
  fi

  echo "$WI_ID"
}
```

### 批量幂等操作

```bash
# Ensure multiple pipelines exist
declare -a PIPELINES=(
  "ci-pipeline:azure-pipelines.yml"
  "deploy-pipeline:deploy.yml"
  "test-pipeline:test.yml"
)

for pipeline in "${PIPELINES[@]}"; do
  IFS=':' read -r name yaml <<< "$pipeline"
  ensure_pipeline "$name" "$yaml"
done
```

### 配置同步

```bash
# Sync variable groups from config file
sync_variable_groups() {
  local config_file=$1

  while IFS=',' read -r vg_name variables; do
    ensure_variable_group "$vg_name" "$variables"
  done < "$config_file"
}

# config.csv format:
# prod-vars,API_URL=prod.com,API_KEY=secret123
# dev-vars,API_URL=dev.com,API_KEY=secret456
```

## 现实世界的工作流程

### CI/CD 管道设置

```bash
# Setup complete CI/CD pipeline
setup_cicd_pipeline() {
  local project=$1
  local repo=$2
  local branch=$3

  # Create variable groups
  VG_DEV=$(ensure_variable_group "dev-vars" "ENV=dev API_URL=api-dev.com")
  VG_PROD=$(ensure_variable_group "prod-vars" "ENV=prod API_URL=api-prod.com")

  # Create CI pipeline
  az pipelines create \
    --name "$repo-CI" \
    --repository "$repo" \
    --branch "$branch" \
    --yaml-path .azure/pipelines/ci.yml \
    --skip-run true

  # Create CD pipeline
  az pipelines create \
    --name "$repo-CD" \
    --repository "$repo" \
    --branch "$branch" \
    --yaml-path .azure/pipelines/cd.yml \
    --skip-run true

  echo "CI/CD pipeline setup complete"
}
```

### 自动公关创建

```bash
# Create PR from feature branch with automation
create_automated_pr() {
  local branch=$1
  local title=$2

  # Get branch info
  LAST_COMMIT=$(git log -1 --pretty=%B "$branch")
  COMMIT_SHA=$(git rev-parse "$branch")

  # Find related work items
  WORK_ITEMS=$(az boards query \
    --wiql "SELECT ID FROM WorkItems WHERE [System.ChangedBy] = @Me AND [System.State] = 'Active'" \
    --query "[].id" -o tsv)

  # Create PR
  PR_ID=$(az repos pr create \
    --source-branch "$branch" \
    --target-branch main \
    --title "$title" \
    --description "$LAST_COMMIT" \
    --work-items $WORK_ITEMS \
    --auto-complete true \
    --query "pullRequestId" -o tsv)

  # Set required reviewers
  az repos pr reviewer add \
    --id $PR_ID \
    --reviewers $(git log -1 --pretty=format:'%ae' "$branch") \
    --required true

  echo "Created PR #$PR_ID"
}
```

### 管道监控和警报

```bash
# Monitor pipeline and alert on failure
monitor_pipeline() {
  local pipeline_name=$1
  local slack_webhook=$2

  while true; do
    # Get latest run
    RUN_ID=$(az pipelines list --query "[?name=='$pipeline_name'] | [0].id" -o tsv)
    RUNS=$(az pipelines runs list --pipeline $RUN_ID --top 1)

    LATEST_RUN_ID=$(echo "$RUNS" | jq -r '.[0].id')
    RESULT=$(echo "$RUNS" | jq -r '.[0].result')

    # Check if failed and not already processed
    if [[ "$RESULT" == "failed" ]]; then
      # Send Slack alert
      curl -X POST "$slack_webhook" \
        -H 'Content-Type: application/json' \
        -d "{\"text\": \"Pipeline $pipeline_name failed! Run ID: $LATEST_RUN_ID\"}"
    fi

    sleep 300 # Check every 5 minutes
  done
}
```

### 批量工作项管理

```bash
# Bulk update work items based on query
bulk_update_work_items() {
  local wiql=$1
  local updates=("$@")

  # Query work items
  WI_IDS=$(az boards query --wiql "$wiql" --query "[].id" -o tsv)

  # Update each work item
  for wi_id in $WI_IDS; do
    az boards work-item update --id $wi_id "${updates[@]}"
    echo "Updated work item: $wi_id"
  done
}

# Usage: bulk_update_work_items "SELECT ID FROM WorkItems WHERE State='New'" --state "Active" --assigned-to "user@example.com"
```

### 分支机构策略自动化

```bash
# Apply branch policies to all repositories
apply_branch_policies() {
  local branch=$1
  local project=$2

  # Get all repositories
  REPOS=$(az repos list --project "$project" --query "[].id" -o tsv)

  for repo_id in $REPOS; do
    echo "Applying policies to repo: $repo_id"

    # Require minimum approvers
    az repos policy approver-count create \
      --blocking true \
      --enabled true \
      --branch "$branch" \
      --repository-id "$repo_id" \
      --minimum-approver-count 2 \
      --creator-vote-counts true

    # Require work item linking
    az repos policy work-item-linking create \
      --blocking true \
      --branch "$branch" \
      --enabled true \
      --repository-id "$repo_id"

    # Require build validation
    BUILD_ID=$(az pipelines list --query "[?name=='CI'].id" -o tsv | head -1)
    az repos policy build create \
      --blocking true \
      --enabled true \
      --branch "$branch" \
      --repository-id "$repo_id" \
      --build-definition-id "$BUILD_ID" \
      --queue-on-source-update-only true
  done
}
```

### 多环境部署

```bash
# Deploy across multiple environments
deploy_to_environments() {
  local run_id=$1
  shift
  local environments=("$@")

  # Download artifacts
  ARTIFACT_NAME=$(az pipelines runs artifact list --run-id $run_id --query "[0].name" -o tsv)
  az pipelines runs artifact download \
    --artifact-name "$ARTIFACT_NAME" \
    --path ./artifacts \
    --run-id $run_id

  # Deploy to each environment
  for env in "${environments[@]}"; do
    echo "Deploying to: $env"

    # Get environment-specific variables
    VG_ID=$(az pipelines variable-group list --query "[?name=='$env-vars'].id" -o tsv)

    # Run deployment pipeline
    DEPLOY_RUN_ID=$(az pipelines run \
      --name "Deploy-$env" \
      --variables ARTIFACT_PATH=./artifacts ENV="$env" \
      --query "id" -o tsv)

    # Wait for deployment
    while true; do
      STATUS=$(az pipelines runs show --run-id $DEPLOY_RUN_ID --query "status" -o tsv)
      if [[ "$STATUS" != "inProgress" ]]; then
        break
      fi
      sleep 10
    done
  done
}
```

## 增强的全球论点

|参数|描述 |
| -------------------- | ---------------------------------------------------------- |
| __代码0__ / __代码1__ |显示命令帮助 |
| __代码0__ / __代码1__ |输出格式（json、jsonc、none、table、tsv、yaml、yamlc）|
| __代码0__ |用于过滤输出的 JMESPath 查询字符串 |
| __代码0__ |增加日志记录的详细程度 |
| __代码0__ |显示所有调试日志 |
| __代码0__ |只显示错误，抑制警告 |
| __代码0__ |订阅名称或 ID |
| __代码0__ / __代码1__ |跳过确认提示 |

## 增强通用参数

|参数|描述 |
| -------------------------- | ------------------------------------------------------------------- |
| __代码0__ / __代码1__ | Azure DevOps 组织 URL（例如 `https://dev.azure.com/{org}`）|
| __代码0__ / __代码1__ |项目名称或ID |
| __代码0__ |从 git config 自动检测组织 |
| __代码0__ / __代码1__ |跳过确认提示 |
| __代码0__ |在网络浏览器中打开资源 |
| __代码0__ | Azure 订阅（适用于 Azure 资源） |

## 寻求帮助

```bash
# General help
az devops --help

# Help for specific command group
az pipelines --help
az repos pr --help

# Help for specific command
az repos pr create --help

# Search for examples
az find "az repos pr create"
```
