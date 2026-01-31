---
描述：“TypeScript、React 和 Power Platform 集成的 Power Apps 代码应用开发标准和最佳实践”
applyTo: '**/*.{ts,tsx,js,jsx}, **/vite.config.*, **/package.json, **/tsconfig.json, **/power.config.json'
---

# Power Apps 代码应用开发说明

遵循 Microsoft 官方最佳实践和预览功能，使用 TypeScript、React 和 Power Platform SDK 生成高质量 Power Apps 代码应用的说明。

## 项目背景

- **Power Apps 代码应用程序（预览版）**：通过 Power Platform 集成进行代码优先 Web 应用程序开发
- **TypeScript + React**：推荐使用 Vite 捆绑器的前端堆栈
- **Power Platform SDK**：@microsoft/power-apps（当前版本 ^0.3.1）用于连接器集成
- **PAC CLI**：用于项目管理和部署的 Power Platform CLI
- **端口 3000**：使用 Power Platform SDK 进行本地开发所需
- **Power Apps Premium**：生产使用的最终用户许可要求

## 开发标准

### 项目结构

- 使用组织良好的文件夹结构并明确关注点分离：
  ```
  src/
  ├── components/          # Reusable UI components
  ├── hooks/              # Custom React hooks for Power Platform
  ├── services/           # Generated connector services (PAC CLI)
  ├── models/            # Generated TypeScript models (PAC CLI)
  ├── utils/             # Utility functions and helpers
  ├── types/             # TypeScript type definitions
  ├── PowerProvider.tsx  # Power Platform initialization
  └── main.tsx          # Application entry point
  ```
- 将生成的文件（`services/`、`models/`）与自定义代码分开
- 使用一致的命名约定（文件采用短横线命名法，组件采用 PascalCase 命名法）

### TypeScript 配置

- 在 tsconfig.json 中设置 `verbatimModuleSyntax: false` 以实现 Power Apps SDK 兼容性
- 使用推荐的 tsconfig.json 启用严格模式以实现类型安全：
  ```json
  {
    "compilerOptions": {
      "target": "ES2020",
      "useDefineForClassFields": true,
      "lib": ["ES2020", "DOM", "DOM.Iterable"],
      "module": "ESNext",
      "skipLibCheck": true,
      "verbatimModuleSyntax": false,
      "moduleResolution": "bundler",
      "allowImportingTsExtensions": true,
      "resolveJsonModule": true,
      "isolatedModules": true,
      "noEmit": true,
      "jsx": "react-jsx",
      "strict": true,
      "noUnusedLocals": true,
      "noUnusedParameters": true,
      "noFallthroughCasesInSwitch": true,
      "baseUrl": ".",
      "paths": {
        "@/*": ["./src/*"]
      }
    }
  }
  ```
- 对 Power Platform 连接器响应使用正确的类型
- 使用 `"@": path.resolve(__dirname, "./src")` 配置路径别名以实现更清晰的导入
- 为特定于应用程序的数据结构定义接口
- 实施错误边界和正确的错误处理类型

### 先进的电源平台集成

#### 自定义控制框架（PCF 控件）
- **集成 PCF 控件**：在 Code Apps 中嵌入 Power Apps 组件框架控件
  ```typescript
  // Example: Using custom PCF control for data visualization
  import { PCFControlWrapper } from './components/PCFControlWrapper';
  
  const MyComponent = () => {
    return (
      <PCFControlWrapper
        controlName="CustomChartControl"
        dataset={chartData}
        configuration={chartConfig}
      />
    );
  };
  ```
- **PCF控制通信**：处理PCF和React之间的事件和数据绑定
- **自定义控件部署**：使用 Code Apps 打包和部署 PCF 控件

#### Power BI 嵌入式分析
- **嵌入 Power BI 报告**：集成交互式仪表板和报告
  ```typescript
  import { PowerBIEmbed } from 'powerbi-client-react';
  
  const DashboardComponent = () => {
    return (
      <PowerBIEmbed
        embedConfig={{
          type: 'report',
          id: reportId,
          embedUrl: embedUrl,
          accessToken: accessToken,
          tokenType: models.TokenType.Aad,
          settings: {
            panes: { filters: { expanded: false, visible: false } }
          }
        }}
      />
    );
  };
  ```
- **动态报告过滤**：根据代码应用上下文过滤 Power BI 报告
- **报告导出功能**：启用 PDF、Excel 和图像导出

#### 人工智能生成器集成
- **认知服务集成**：使用 AI Builder 模型进行表单处理、对象检测
  ```typescript
  // Example: Document processing with AI Builder
  const processDocument = async (file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    
    const result = await AIBuilderService.ProcessDocument({
      modelId: 'document-processing-model-id',
      document: formData
    });
    
    return result.extractedFields;
  };
  ```
- **预测模型**：集成自定义 AI 模型以进行业务预测
- **情感分析**：使用 AI Builder 分析文本情感
- **物体检测**：实现图像分析和物体识别

#### 强大的虚拟代理集成
- **聊天机器人嵌入**：将 Power Virtual Agents 机器人集成到代码应用程序中
  ```typescript
  import { DirectLine } from 'botframework-directlinejs';
  import { WebChat } from 'botframework-webchat';
  
  const ChatbotComponent = () => {
    const directLine = new DirectLine({
      token: chatbotToken
    });
    
    return (
      <div style={{ height: '400px', width: '100%' }}>
        <WebChat directLine={directLine} />
      </div>
    );
  };
  ```
- **上下文传递**：与聊天机器人对话共享代码应用程序上下文
- **自定义机器人操作**：通过机器人交互触发代码应用程序功能
- 使用 PAC CLI 生成的 TypeScript 服务进行连接器操作
- 使用 Microsoft Entra ID 实施正确的身份验证流程
- 处理连接器同意对话框和权限管理
- PowerProvider实现模式：
  ```typescript
  import { initialize } from "@microsoft/power-apps/app";
  import { useEffect, type ReactNode } from "react";

  export default function PowerProvider({ children }: { children: ReactNode }) {
    useEffect(() => {
      const initApp = async () => {
        try {
          await initialize();
          console.log('Power Platform SDK initialized successfully');
        } catch (error) {
          console.error('Failed to initialize Power Platform SDK:', error);
        }
      };
      initApp();
    }, []);
    return <>{children}</>;
  }
  ```
- 遵循官方支持的连接器模式：
  - SQL Server（包括 Azure SQL）
  - 共享点
  - Office 365 用户/组
  - Azure 数据资源管理器
  - OneDrive 商业版
  - 微软团队
  - 数据空间（CRUD 操作）

### 反应模式

- 使用带钩子的功能组件进行所有新开发
- 为连接器操作实现正确的加载和错误状态
- 考虑 Fluent UI React 组件（如官方示例中使用的）
- 在适当的时候使用 React Query 或 SWR 进行数据获取和缓存
- 遵循 React 组件组合最佳实践
- 使用移动优先方法实施响应式设计
- 按照官方示例安装关键依赖项：
  - Power Platform SDK 的 `@microsoft/power-apps`
  - UI 组件的 `@fluentui/react-components`
  - `concurrently` 用于并行脚本执行（开发依赖）

### 数据管理

- 将敏感数据存储在数据源中，而不是应用程序代码中
- 使用生成的模型进行类型安全的连接器操作
- 实施适当的数据验证和清理
- 尽可能优雅地处理离线场景
- 适当缓存经常访问的数据

#### 高级数据宇宙关系
- **多对多关系**：实现联结表和关系服务
  ```typescript
  // Example: User-to-Role many-to-many relationship
  const userRoles = await UserRoleService.getall();
  const filteredRoles = userRoles.filter(ur => ur.userId === currentUser.id);
  ```
- **多态查找**：处理可以引用多个实体类型的客户字段
  ```typescript
  // Handle polymorphic customer lookup (Account or Contact)
  const customerType = record.customerType; // 'account' or 'contact'
  const customerId = record.customerId;
  const customer = customerType === 'account' 
    ? await AccountService.get(customerId)
    : await ContactService.get(customerId);
  ```
- **复杂关系查询**：使用$expand和$filter进行高效的数据检索
- **关系验证**：实施关系约束的业务规则

### 性能优化

- 使用 React.memo 和 useMemo 进行昂贵的计算
- 为大型应用程序实现代码分割和延迟加载
- 通过 Tree Shaking 优化捆绑包大小
- 使用高效的连接器查询模式来最大限度地减少 API 调用
- 为大型数据集实施正确的分页

#### 具有同步模式的离线优先架构
- **Service Worker 实现**：启用离线功能
  ```typescript
  // Example: Service worker registration
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js')
        .then(registration => console.log('SW registered:', registration))
        .catch(error => console.log('SW registration failed:', error));
    });
  }
  ```
- **本地数据存储**：使用IndexedDB进行离线数据持久化
  ```typescript
  // Example: IndexedDB wrapper for offline storage
  class OfflineDataStore {
    async saveData(key: string, data: any) {
      const db = await this.openDB();
      const transaction = db.transaction(['data'], 'readwrite');
      transaction.objectStore('data').put({ id: key, data, timestamp: Date.now() });
    }
    
    async loadData(key: string) {
      const db = await this.openDB();
      const transaction = db.transaction(['data'], 'readonly');
      return transaction.objectStore('data').get(key);
    }
  }
  ```
- **同步冲突解决**：重新上线时处理数据冲突
- **后台同步**：实现周期性数据同步
- **渐进式 Web 应用程序 (PWA)**：启用应用程序安装和离线功能

### 安全最佳实践

- 切勿在代码中存储机密或敏感配置
- 使用 Power Platform 的内置身份验证和授权
- 实施适当的输入验证和清理
- 遵循 Web 应用程序的 OWASP 安全指南
- 尊重 Power Platform 数据丢失防护政策
- 实施仅 HTTPS 通信

### 错误处理

- 在 React 中实现全面的错误边界
- 优雅地处理连接器特定的错误
- 向用户提供有意义的错误消息
- 适当记录错误而不暴露敏感信息
- 实现暂时性故障的重试逻辑
- 处理网络连接问题

### 测试策略

- 为业务逻辑和实用程序编写单元测试
- 使用 React 测试库测试 React 组件
- 测试中的模拟电源平台连接器
- 对关键用户流程实施集成测试
- 使用 TypeScript 提高测试安全性
- 测试错误场景和边缘情况

### 开发流程

- 使用 PAC CLI 进行项目初始化和连接器管理
- 遵循适合团队规模的 git 分支策略
- 实施适当的代码审查流程
- 使用 linting 和格式化工具（ESLint、Prettier）
- 同时使用以下方式配置开发脚本：
  - __代码0__
  - __代码0__
- 在 CI/CD 管道中实施自动化测试
- 遵循发布的语义版本控制

### 部署和 DevOps

- 使用 `npm run build` 后跟 `pac code push` 进行部署
- 实施适当的环境管理（开发、测试、生产）
- 使用特定于环境的配置文件
- 尽可能实施蓝绿或金丝雀部署策略
- 监控生产中的应用程序性能和错误
- 实施适当的备份和灾难恢复程序

#### 多环境部署管道
- **特定于环境的配置**：管理开发/测试/登台/生产环境
  ```json
  // Example: environment-specific config files
  // config/development.json
  {
    "powerPlatform": {
      "environmentUrl": "https://dev-env.crm.dynamics.com",
      "apiVersion": "9.2"
    },
    "features": {
      "enableDebugMode": true,
      "enableAnalytics": false
    }
  }
  ```
- **自动化部署管道**：使用 Azure DevOps 或 GitHub Actions
  ```yaml
  # Example Azure DevOps pipeline step
  - task: PowerPlatformToolInstaller@2
  - task: PowerPlatformSetConnectionVariables@2
    inputs:
      authenticationType: 'PowerPlatformSPN'
      applicationId: '$(AppId)'
      clientSecret: '$(ClientSecret)'
      tenantId: '$(TenantId)'
  - task: PowerPlatformPublishCustomizations@2
  ```
- **环境升级**：从开发→测试→暂存→生产的自动升级
- **回滚策略**：部署失败时实现自动回滚
- **配置管理**：使用 Azure Key Vault 存储特定于环境的机密

## 代码质量指南

### 组件开发

- 创建具有清晰 props 接口的可重用组件
- 使用组合而不是继承
- 使用 TypeScript 实现正确的 prop 验证
- 遵循单一职责原则
- 编写具有清晰命名的自文档代码

### 状态管理

- 对于简单场景使用 React 的内置状态管理
- 考虑使用 Redux Toolkit 进行复杂的状态管理
- 实施适当的状态正常化
- 避免使用上下文或状态管理库进行道具钻探
- 有效地使用派生状态和计算值

### API集成

- 使用 PAC CLI 生成的服务以保持一致性
- 实施适当的请求/响应拦截器
- 处理身份验证令牌管理
- 实施请求重复数据删除和缓存
- 使用正确的 HTTP 状态代码处理

### 样式和用户界面

- 使用一致的设计系统或组件库
- 使用 CSS Grid/Flexbox 实现响应式设计
- 遵循无障碍指南 (WCAG 2.1)
- 使用 CSS-in-JS 或 CSS 模块进行组件样式设置
- 适当时实现深色模式支持
- 确保移动友好的用户界面

#### 高级 UI/UX 模式

##### 使用组件库实现设计系统
- **组件库结构**：构建可复用的组件系统
  ```typescript
  // Example: Design system button component
  interface ButtonProps {
    variant: 'primary' | 'secondary' | 'danger';
    size: 'small' | 'medium' | 'large';
    disabled?: boolean;
    onClick: () => void;
    children: React.ReactNode;
  }
  
  export const Button: React.FC<ButtonProps> = ({ 
    variant, size, disabled, onClick, children 
  }) => {
    const classes = `btn btn-${variant} btn-${size} ${disabled ? 'btn-disabled' : ''}`;
    return <button className={classes} onClick={onClick} disabled={disabled}>{children}</button>;
  };
  ```
- **设计标记**：实现一致的间距、颜色、版式
- **组件文档**：使用 Storybook 进行组件文档

##### 深色模式和主题系统
- **主题提供者实现**：支持多个主题
  ```typescript
  // Example: Theme context and provider
  const ThemeContext = createContext({
    theme: 'light',
    toggleTheme: () => {}
  });
  
  export const ThemeProvider: React.FC<{children: ReactNode}> = ({ children }) => {
    const [theme, setTheme] = useState<'light' | 'dark'>('light');
    
    const toggleTheme = () => {
      setTheme(prev => prev === 'light' ? 'dark' : 'light');
    };
    
    return (
      <ThemeContext.Provider value={{ theme, toggleTheme }}>
        <div className={`theme-${theme}`}>{children}</div>
      </ThemeContext.Provider>
    );
  };
  ```
- **CSS 自定义属性**：使用 CSS 变量进行动态主题设置
- **系统偏好检测**：尊重用户的操作系统主题偏好

##### 响应式设计高级模式
- **容器查询**：使用基于容器的响应式设计
  ```css
  /* Example: Container query for responsive components */
  .card-container {
    container-type: inline-size;
  }
  
  @container (min-width: 400px) {
    .card {
      display: grid;
      grid-template-columns: 1fr 1fr;
    }
  }
  ```
- **流体排版**：实现响应式字体缩放
- **自适应布局**：根据屏幕尺寸和上下文更改布局模式

##### 动画和微交互
- **Framer Motion 集成**：平滑的动画和过渡
  ```typescript
  import { motion, AnimatePresence } from 'framer-motion';
  
  const AnimatedCard = () => {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -20 }}
        transition={{ duration: 0.3 }}
        whileHover={{ scale: 1.02 }}
        className="card"
      >
        Card content
      </motion.div>
    );
  };
  ```
- **加载状态**：动画骨架和进度指示器
- **手势识别**：滑动、捏合和触摸交互
- **性能优化**：使用 CSS 变换和 will-change 属性

##### 辅助功能自动化和测试
- **ARIA 实现**：正确的语义标记和 ARIA 属性
  ```typescript
  // Example: Accessible modal component
  const Modal: React.FC<{isOpen: boolean, onClose: () => void, children: ReactNode}> = ({ 
    isOpen, onClose, children 
  }) => {
    useEffect(() => {
      if (isOpen) {
        document.body.style.overflow = 'hidden';
        const focusableElement = document.querySelector('[data-autofocus]') as HTMLElement;
        focusableElement?.focus();
      }
      return () => { document.body.style.overflow = 'unset'; };
    }, [isOpen]);
    
    return (
      <div 
        role="dialog" 
        aria-modal="true" 
        aria-labelledby="modal-title"
        className={isOpen ? 'modal-open' : 'modal-hidden'}
      >
        {children}
      </div>
    );
  };
  ```
- **自动化可访问性测试**：集成 axe-core 进行可访问性测试
- **键盘导航**：实现完整的键盘辅助功能
- **屏幕阅读器优化**：使用 NVDA、JAWS 和 VoiceOver 进行测试

##### 国际化 (i18n) 和本地化
- **React-intl集成**：多语言支持
  ```typescript
  import { FormattedMessage, useIntl } from 'react-intl';
  
  const WelcomeMessage = ({ userName }: { userName: string }) => {
    const intl = useIntl();
    
    return (
      <h1>
        <FormattedMessage
          id="welcome.title"
          defaultMessage="Welcome, {userName}!"
          values={{ userName }}
        />
      </h1>
    );
  };
  ```
- **语言检测**：自动语言检测和切换
- **RTL 支持**：从右到左的阿拉伯语、希伯来语语言支持
- **日期和数字格式**：特定于区域设置的格式
- **翻译管理**：与翻译服务集成

## 当前的限制和解决方法

### 已知限制

- 尚不支持内容安全策略 (CSP)
- 不支持存储 SAS IP 限制
- 没有 Power Platform Git 集成
- 不支持 Dataverse 解决方案
- 没有本机 Azure Application Insights 集成

### 解决方法

- 如果需要，使用替代错误跟踪解决方案
- 实施手动部署工作流程
- 使用外部工具进行高级分析
- 规划未来迁移到支持的功能

## 文件标准

- 维护包含设置说明的全面 README.md
- 记录所有自定义组件和挂钩
- 包括常见问题的故障排除指南
- 记录部署过程和要求
- 维护版本更新的变更日志
- 包括主要选择的架构决策记录

## 常见问题故障排除

### 发展问题

- **端口 3000 冲突**：使用 `netstat -ano | findstr :3000` 终止现有进程，然后使用 `taskkill /PID {PID} /F`
- **身份验证失败**：使用 `pac auth list` 验证环境设置和用户权限
- **软件包安装失败**：使用 `npm cache clean --force` 清除 npm 缓存并重新安装
- **TypeScript 编译错误**：检查 verbatimModuleSyntax 设置和 SDK 兼容性
- **连接器权限错误**：确保正确的同意流程和管理权限
- **PowerProvider 初始化错误**：检查控制台是否有 SDK 初始化失败
- **Vite 开发服务器问题**：确保主机和端口配置符合要求

### 部署问题

- **构建失败**：使用 `npm audit` 验证所有依赖项并检查构建配置
- **身份验证错误**：使用 `pac auth clear` 然后使用 `pac auth create` 重新验证 PAC CLI
- **连接器不可用**：验证 Power Platform 中的连接器设置和连接状态
- **性能问题**：使用 `npm run build --report` 优化包大小并实现缓存
- **环境不匹配**：使用 `pac env list` 确认正确的环境选择
- **应用程序超时错误**：检查 PowerProvider.tsx 实施和网络连接

### 运行时问题

- **“应用程序超时”错误**：验证 npm run build 已执行并且 PowerProvider 没有错误
- **连接器身份验证提示**：确保正确的同意流程实施
- **数据加载失败**：检查网络请求和连接器权限
- **UI渲染问题**：验证Fluent UI兼容性和响应式设计实现

## 最佳实践总结

1. **遵循微软官方文档和最佳实践**
2. **使用 TypeScript 实现类型安全和更好的开发人员体验**
3. **实施适当的错误处理和用户反馈**
4. **针对性能和用户体验进行优化**
5. **遵循安全最佳实践和 Power Platform 政策**
6. **编写可维护、可测试且文档齐全的代码**
7. **使用 PAC CLI 生成的服务和模型**
8. **规划未来的功能更新和迁移**
9. **实施全面的测试策略**

10. **遵循正确的 DevOps 和部署实践**
