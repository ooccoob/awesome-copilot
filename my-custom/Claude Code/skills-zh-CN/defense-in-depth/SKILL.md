---
name: defense-in-depth
description: 当无效数据在执行深处导致失败，需要在多个系统层进行验证时使用 - 在数据通过的每一层进行验证，使错误在结构上不可能发生
---

# 纵深防御验证

## 概述

当您修复由无效数据引起的错误时，在一个地方添加验证感觉足够了。但单一检查可能被不同的代码路径、重构或模拟绕过。

**核心原则：** 在数据通过的每一层进行验证。使错误在结构上不可能发生。

## 为什么需要多层

单一验证："我们修复了错误"
多层验证："我们使错误不可能发生"

不同层捕获不同情况：
- 入口验证捕获大多数错误
- 业务逻辑捕获边界情况
- 环境防护防止特定上下文的危险
- 调试日志在其他层失败时提供帮助

## 四层结构

### 第1层：入口点验证
**目的：** 在API边界拒绝明显无效的输入

```typescript
function createProject(name: string, workingDirectory: string) {
  if (!workingDirectory || workingDirectory.trim() === '') {
    throw new Error('workingDirectory不能为空');
  }
  if (!existsSync(workingDirectory)) {
    throw new Error(`workingDirectory不存在：${workingDirectory}`);
  }
  if (!statSync(workingDirectory).isDirectory()) {
    throw new Error(`workingDirectory不是目录：${workingDirectory}`);
  }
  // ...继续
}
```

### 第2层：业务逻辑验证
**目的：** 确保数据对此操作有意义

```typescript
function initializeWorkspace(projectDir: string, sessionId: string) {
  if (!projectDir) {
    throw new Error('工作区初始化需要projectDir');
  }
  // ...继续
}
```

### 第3层：环境防护
**目的：** 在特定上下文中防止危险操作

```typescript
async function gitInit(directory: string) {
  // 在测试中，拒绝在临时目录外进行git init
  if (process.env.NODE_ENV === 'test') {
    const normalized = normalize(resolve(directory));
    const tmpDir = normalize(resolve(tmpdir()));

    if (!normalized.startsWith(tmpDir)) {
      throw new Error(
        `在测试期间拒绝在临时目录外进行git init：${directory}`
      );
    }
  }
  // ...继续
}
```

### 第4层：调试工具
**目的：** 捕获上下文用于取证

```typescript
async function gitInit(directory: string) {
  const stack = new Error().stack;
  logger.debug('即将进行git init', {
    directory,
    cwd: process.cwd(),
    stack,
  });
  // ...继续
}
```

## 应用模式

当您发现错误时：

1. **追踪数据流** - 坏值起源于哪里？在哪里使用？
2. **映射所有检查点** - 列出数据通过的每个点
3. **在每层添加验证** - 入口、业务、环境、调试
4. **测试每层** - 尝试绕过第1层，验证第2层捕获它

## 会话中的示例

错误：空的`projectDir`导致在源代码中进行`git init`

**数据流：**
1. 测试设置 → 空字符串
2. `Project.create(name, '')`
3. `WorkspaceManager.createWorkspace('')`
4. `git init`在`process.cwd()`中运行

**添加的四层：**
- 第1层：`Project.create()`验证非空/存在/可写
- 第2层：`WorkspaceManager`验证projectDir非空
- 第3层：`WorktreeManager`拒绝在测试中在tmpdir外进行git init
- 第4层：在git init前进行堆栈跟踪日志记录

**结果：** 所有1847个测试通过，错误不可能重现

## 关键洞察

所有四层都是必要的。在测试期间，每层都捕获了其他层错过的错误：
- 不同的代码路径绕过了入口验证
- 模拟绕过了业务逻辑检查
- 不同平台上的边界情况需要环境防护
- 调试日志识别了结构性误用

**不要在一个验证点停止。** 在每一层都添加检查。