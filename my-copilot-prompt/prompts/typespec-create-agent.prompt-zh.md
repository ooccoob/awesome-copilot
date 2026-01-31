---
模式：“代理”
工具：['更改'、'搜索/代码库'、'编辑/编辑文件'、'问题']
描述：“为 Microsoft 365 Copilot 生成完整的 TypeSpec 声明性代理，其中包含说明、功能和对话启动器”
型号：'gpt-4.1'
标签：[typespec、m365-copilot、声明性代理、代理开发]
---

# 创建 TypeSpec 声明性代理

使用以下结构为 Microsoft 365 Copilot 创建完整的 TypeSpec 声明性代理：

## 要求

使用以下命令生成 `main.tsp` 文件：

1. **代理声明**
   - 使用带有描述性名称和描述的 `@agent` 装饰器
   - 名称不得超过 100 个字符
   - 描述不得超过 1,000 个字符

2. **说明**
   - 使用具有明确行为准则的 `@instructions` 装饰器
   - 定义代理的角色、专业知识和个性
   - 指定代理应该做什么和不应该做什么
   - 保持在 8,000 个字符以内

3. **对话开始者**
   - 包含 2-4 个 `@conversationStarter` 装饰器
   - 每个都有标题和示例查询
   - 使他们多样化并展示不同的能力

4. **功能**（基于用户需求）
   - `WebSearch` - 用于具有可选网站范围的 Web 内容
   - `OneDriveAndSharePoint` - 用于通过 URL 过滤进行文档访问
   - `TeamsMessages` - 用于团队频道/聊天访问
   - `Email` - 用于通过文件夹过滤进行电子邮件访问
   - `People` - 用于组织人员搜索
   - `CodeInterpreter` - 用于Python代码执行
   - `GraphicArt` - 用于图像生成
   - `GraphConnectors` - 用于 Copilot 连接器内容
   - `Dataverse` - 用于 Dataverse 数据访问
   - `Meetings` - 用于会议内容访问

## 模板结构

```typescript
import "@typespec/http";
import "@typespec/openapi3";
import "@microsoft/typespec-m365-copilot";

using TypeSpec.Http;
using TypeSpec.M365.Copilot.Agents;

@agent({
  name: "[Agent Name]",
  description: "[Agent Description]"
})
@instructions("""
  [Detailed instructions about agent behavior, role, and guidelines]
""")
@conversationStarter(#{
  title: "[Starter Title 1]",
  text: "[Example query 1]"
})
@conversationStarter(#{
  title: "[Starter Title 2]",
  text: "[Example query 2]"
})
namespace [AgentName] {
  // Add capabilities as operations here
  op capabilityName is AgentCapabilities.[CapabilityType]<[Parameters]>;
}
```

## 最佳实践

- 使用描述性的、基于角色的代理名称（例如“客户支持助理”、“研究助手”）
- 用第二人称写指令（“你是……”）
- 具体说明代理人的专业知识和局限性
- 包括展示不同功能的多样化对话开头
- 仅包含代理实际需要的功能
- 尽可能扩大范围功能（URL、文件夹等）以获得更好的性能
- 对多行指令使用三引号字符串

## 示例

询问用户：
1. 代理人的目的和作用是什么？
2. 它需要什么能力？
3. 它应该访问哪些知识源？
4. 典型的用户交互是什么？

然后生成完整的 TypeSpec 代理定义。
