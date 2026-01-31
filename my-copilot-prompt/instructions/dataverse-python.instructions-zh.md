---
适用于：'**'
---
# 适用于 Python 的 Dataverse SDK — 入门

- 安装 Dataverse Python SDK 和先决条件。
- 为 Dataverse 租户、客户端 ID、密钥和资源 URL 配置环境变量。
- 使用SDK通过OAuth进行身份验证并执行CRUD操作。

## 设置
- Python 3.10+
- 推荐：虚拟环境

## 安装
```bash
pip install dataverse-sdk
```

## 身份验证基础知识
- 将 OAuth 与 Azure AD 应用程序注册结合使用。
- 将机密存储在 `.env` 中并通过 `python-dotenv` 加载。

## 常见任务
- 查询表
- 创建/更新行
- 批量操作
- 处理分页和限制

## 温馨提示
- 重用客户端；避免频繁的重新验证。
- 添加针对暂时性故障的重试。
- 记录故障排除请求。
