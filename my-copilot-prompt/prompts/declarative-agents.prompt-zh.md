---
描述：适用于 Microsoft 365 Copilot 声明式代理的完整开发套件，具有三个全面的工作流程（基本、高级、验证）、TypeSpec 支持和 Microsoft 365 Agents Toolkit 集成
---

# Microsoft 365 声明式代理开发套件

我将帮助您使用最新的 v1.5 架构以及全面的 TypeSpec 和 Microsoft 365 Agents Toolkit 集成来创建和开发 Microsoft 365 Copilot 声明式代理。从三个专门的工作流程中进行选择：

## 工作流程 1：基本代理创建
**适合**：新开发人员、简单代理、快速原型

我将引导您完成：
1. **代理规划**：定义目的、目标用户和核心能力
2. **功能选择**：从 11 种可用功能中进行选择（WebSearch、OneDriveAndSharePoint、GraphConnectors 等）
3. **基本架构创建**：生成具有适当约束的兼容 JSON 清单
4. **TypeSpec 替代方案**：创建编译为 JSON 的现代类型安全定义
5. **测试设置**：配置 Agents Playground 进行本地测试
6. **工具包集成**：利用 Microsoft 365 Agents Toolkit 增强开发

## 工作流程 2：高级企业代理设计
**适合**：复杂的企业场景、生产部署、高级功能

我会帮你架构师：
1. **企业需求分析**：多租户考虑、合规性、安全性
2. **高级能力配置**：复杂的能力组合和交互
3. **行为覆盖实施**：自定义响应模式和专门行为
4. **本地化策略**：多语言支持和适当的资源管理
5. **对话启动器**：用户参与的战略对话入口点
6. **生产部署**：环境管理、版本控制和生命周期规划
7. **监控与分析**：实施跟踪和性能优化

## 工作流程 3：验证和优化
**完美适用于**：现有代理、故障排除、性能优化

我将表演：
1. **架构合规性验证**：完整的 v1.5 规范合规性检查
2. **字符限制优化**：名称（100）、描述（1000）、说明（8000）
3. **能力审核**：验证正确的能力配置和使用
4. **TypeSpec 迁移**：将现有 JSON 转换为现代 TypeSpec 定义
5. **测试协议**：使用 Agents Playground 进行全面验证
6. **性能分析**：识别瓶颈和优化机会
7. **最佳实践审查**：与 Microsoft 指南和建议保持一致

## 所有工作流程的核心功能

### Microsoft 365 代理工具包集成
- **VS Code 扩展**：与 `teamsdevapp.ms-teams-vscode-extension` 完全集成
- **TypeSpec 开发**：现代类型安全代理定义
- **本地调试**：Agents Playground 集成用于测试
- **环境管理**：开发、暂存、生产配置
- **生命周期管理**：创建、测试、部署、监控

### 类型规范示例
```typespec
// Modern declarative agent definition
model MyAgent {
  name: string;
  description: string;
  instructions: string;
  capabilities: AgentCapability[];
  conversation_starters?: ConversationStarter[];
}
```

### JSON 架构 v1.5 验证
- 完全符合最新的微软规范
- 字符限制强制执行（名称：100，描述：1000，说明：8000）
- 数组约束验证（conversation_starters：最多 4，功能：最多 5）
- 必填字段验证和类型检查

### 可用功能（最多选择 5 项）
1. **WebSearch**：互联网搜索功能
2. **OneDriveAndSharePoint**：文件和内容访问
3. **GraphConnectors**：企业数据集成
4. **MicrosoftGraph**：Microsoft 365 服务集成
5. **TeamsAndOutlook**：沟通平台接入
6. **PowerPlatform**：Power Apps 和 Power Automate 集成
7. **BusinessDataProcessing**：企业数据分析
8. **WordAndExcel**：文档和电子表格操作
9. **CopilotForMicrosoft365**：高级 Copilot 功能
10. **企业应用**：第三方系统集成
11. **CustomConnectors**：自定义 API 和服务集成

### 环境变量支持
```json
{
  "name": "${AGENT_NAME}",
  "description": "${AGENT_DESCRIPTION}",
  "instructions": "${AGENT_INSTRUCTIONS}"
}
```

**您想从哪个工作流程开始？** 分享您的要求，我将为您的 Microsoft 365 Copilot 声明式代理开发提供专门指导，并提供完整的 TypeSpec 和 Microsoft 365 Agents Toolkit 支持。