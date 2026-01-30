---
description: 'Power Apps 代码应用开发标准和 TypeScript、React 及 Power Platform 集成的最佳实践'
applyTo: '**/*.{ts,tsx,js,jsx}, **/vite.config.*, **/package.json, **/tsconfig.json, **/power.config.json'
---

# Power Apps 代码应用开发指令

使用 TypeScript、React 和 Power Platform SDK 生成高质量 Power Apps 代码应用的指令，遵循 Microsoft 官方最佳实践和预览功能。

## 项目背景

- **Power Apps 代码应用（预览版）**：代码优先的 Web 应用开发，具有 Power Platform 集成
- **TypeScript + React**：推荐的前端技术栈，使用 Vite 打包器
- **Power Platform SDK**：@microsoft/power-apps（当前版本 ^0.3.1）用于连接器集成
- **PAC CLI**：Power Platform CLI 用于项目管理和部署
- **端口 3000**：Power Platform SDK 本地开发必需
- **Power Apps Premium**：生产使用的最终用户许可要求

## 开发标准

### 项目结构

- 使用组织良好的文件夹结构，具有清晰的关注点分离：
  ```
  src/
  ├── components/          # 可重用的 UI 组件
  ├── hooks/              # Power Platform 的自定义 React hooks
  ├── services/           # 生成的连接器服务（PAC CLI）
  ├── models/            # 生成的 TypeScript 模型（PAC CLI）
  ├── utils/             # 实用函数和帮助器
  ├── types/             # TypeScript 类型定义
  ├── PowerProvider.tsx  # Power Platform 初始化
  └── main.tsx          # 应用程序入口点
  ```
- 保持生成的文件（`services/`、`models/`）与自定义代码分离
- 使用一致的命名约定（文件使用 kebab-case，组件使用 PascalCase）

### TypeScript 配置

- 在 tsconfig.json 中设置 `verbatimModuleSyntax: false` 以兼容 Power Apps SDK
- 启用严格模式以确保类型安全，使用推荐的 tsconfig.json：
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
- 为 Power Platform 连接器响应使用适当的类型
- 使用 `"@": path.resolve(__dirname, "./src")` 配置路径别名以获得更清晰的导入
- 为应用特定的数据结构定义接口
- 实现错误边界和适当的错误处理类型

### 高级 Power Platform 集成

#### 自定义控件框架（PCF 控件）
- **集成 PCF 控件**：在代码应用中嵌入 Power Apps 组件框架控件
  ```typescript
  // 示例：使用自定义 PCF 控件进行数据可视化
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
- **PCF 控件通信**：处理 PCF 和 React 之间的事件和数据绑定
- **自定义控件部署**：将 PCF 控件与代码应用一起打包和部署

#### Power BI 嵌入式分析
- **嵌入 Power BI 报告**：集成交互式仪表板和报告
  ```typescript
  import { PowerBIEmbed } from 'powerbi-client-react';

  const DashboardComponent = () => {
    return (
      <PowerBIEmbed
        embedConfig={{
          type: 'report',
          id: 'your-report-id',
          embedUrl: 'https://app.powerbi.com/reportEmbed',
          accessToken: 'your-access-token',
          tokenType: models.TokenType.Embed,
          settings: {
            panes: {
              filters: { expanded: false, visible: true },
              pageNavigation: { visible: false }
            }
          }
        }}
        cssClassName="embed-container"
        getEmbeddedComponent={(embeddedReport) => {
          console.log('报告已嵌入', embeddedReport);
        }}
      />
    );
  };
  ```

#### Power Virtual Agents 集成
- **聊天机器人集成**：嵌入 Power Virtual Agents 聊天机器人
  ```typescript
  import { ChatWidget } from '@microsoft/power-virtual-agents';

  const SupportChat = () => {
    return (
      <ChatWidget
        botId="your-bot-id"
        tokenProvider={async () => {
          const response = await fetch('/api/chat-token');
          const data = await response.json();
          return data.token;
        }}
        directLine={{
          secret: 'your-direct-line-secret'
        }}
        styleOptions={{
          botAvatarInitials: 'Support',
          userAvatarInitials: 'You',
          backgroundColor: '#f0f0f0'
        }}
      />
    );
  };
  ```

### React 组件开发

#### 组件最佳实践
- **函数组件优先**：使用函数组件和 hooks 而不是类组件
- **类型安全组件**：使用 TypeScript 接口定义 props
  ```typescript
  interface DataTableProps {
    data: PowerPlatformData[];
    columns: ColumnDefinition[];
    loading?: boolean;
    onRowClick?: (row: PowerPlatformData) => void;
  }

  export const DataTable: React.FC<DataTableProps> = ({
    data,
    columns,
    loading = false,
    onRowClick
  }) => {
    // 组件实现
  };
  ```
- **可访问性**：实现 ARIA 属性和键盘导航
- **响应式设计**：使用 CSS Grid 和 Flexbox 进行响应式布局
- **性能优化**：使用 React.memo、useMemo 和 useCallback

#### 自定义 Hooks
```typescript
// Power Platform 数据获取 hook
export const usePowerPlatformData = <T>(
  serviceName: string,
  functionName: string,
  params?: Record<string, any>
) => {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const service = getPowerPlatformService(serviceName);
        const result = await service[functionName](params);
        setData(result);
      } catch (err) {
        setError(err instanceof Error ? err.message : '未知错误');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [serviceName, functionName, JSON.stringify(params)]);

  return { data, loading, error, refetch: fetchData };
};

// 环境上下文 hook
export const useEnvironmentContext = () => {
  const context = useContext(EnvironmentContext);
  if (!context) {
    throw new Error('useEnvironmentContext 必须在 PowerProvider 内使用');
  }
  return context;
};
```

### 状态管理

#### Context API 实现
```typescript
// Power Platform 上下文
interface PowerPlatformContextType {
  environment: PowerPlatformEnvironment;
  currentUser: UserInfo;
  connectors: ConnectorMap;
  notifications: Notification[];
  addNotification: (notification: Notification) => void;
  removeNotification: (id: string) => void;
}

export const PowerPlatformContext = createContext<PowerPlatformContextType | null>(null);

export const PowerProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [environment, setEnvironment] = useState<PowerPlatformEnvironment | null>(null);
  const [currentUser, setCurrentUser] = useState<UserInfo | null>(null);
  const [notifications, setNotifications] = useState<Notification[]>([]);

  useEffect(() => {
    // 初始化 Power Platform 连接
    const initializePowerPlatform = async () => {
      try {
        const env = await PowerApps.getEnvironmentInfo();
        const user = await PowerApps.getCurrentUserInfo();
        setEnvironment(env);
        setCurrentUser(user);
      } catch (error) {
        console.error('Power Platform 初始化失败:', error);
      }
    };

    initializePowerPlatform();
  }, []);

  const addNotification = useCallback((notification: Notification) => {
    setNotifications(prev => [...prev, notification]);
  }, []);

  const removeNotification = useCallback((id: string) => {
    setNotifications(prev => prev.filter(n => n.id !== id));
  }, []);

  const value: PowerPlatformContextType = {
    environment: environment!,
    currentUser: currentUser!,
    connectors: {},
    notifications,
    addNotification,
    removeNotification
  };

  return (
    <PowerPlatformContext.Provider value={value}>
      {children}
    </PowerPlatformContext.Provider>
  );
};
```

### 错误处理和日志记录

#### 错误边界组件
```typescript
interface ErrorBoundaryState {
  hasError: boolean;
  error: Error | null;
  errorInfo: ErrorInfo | null;
}

export class ErrorBoundary extends React.Component<
  React.PropsWithChildren<{}>,
  ErrorBoundaryState
> {
  constructor(props: React.PropsWithChildren<{}>) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error, errorInfo: null };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    this.setState({ error, errorInfo });

    // 记录错误到 Power Platform 或外部服务
    this.logErrorToPowerPlatform(error, errorInfo);
  }

  private async logErrorToPowerPlatform(error: Error, errorInfo: ErrorInfo) {
    try {
      const errorService = getPowerPlatformService('ErrorLoggingService');
      await errorService.logError({
        message: error.message,
        stack: error.stack,
        componentStack: errorInfo.componentStack,
        timestamp: new Date().toISOString(),
        userAgent: navigator.userAgent
      });
    } catch (loggingError) {
      console.error('记录错误失败:', loggingError);
    }
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary">
          <h2>应用程序遇到错误</h2>
          <details>
            <summary>错误详情</summary>
            <pre>{this.state.error?.message}</pre>
          </details>
          <button onClick={() => window.location.reload()}>
            重新加载应用程序
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}
```

#### 全局错误处理
```typescript
// 全局错误处理设置
export const setupGlobalErrorHandling = () => {
  window.addEventListener('error', (event) => {
    console.error('全局错误:', event.error);
    // 报告错误到 Power Platform
    reportErrorToPowerPlatform(event.error);
  });

  window.addEventListener('unhandledrejection', (event) => {
    console.error('未处理的 Promise 拒绝:', event.reason);
    // 报告错误到 Power Platform
    reportErrorToPowerPlatform(event.reason);
  });
};

const reportErrorToPowerPlatform = async (error: any) => {
  try {
    const service = getPowerPlatformService('ErrorReportingService');
    await service.reportError({
      message: error?.message || '未知错误',
      stack: error?.stack,
      url: window.location.href,
      timestamp: new Date().toISOString()
    });
  } catch (reportingError) {
    console.error('报告错误失败:', reportingError);
  }
};
```

### 性能优化

#### 代码分割和懒加载
```typescript
import { lazy, Suspense } from 'react';
import { Spin } from 'antd';

// 懒加载组件
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Reports = lazy(() => import('./pages/Reports'));
const Settings = lazy(() => import('./pages/Settings'));

const AppRouter = () => {
  return (
    <Router>
      <Suspense fallback={<Spin size="large" />}>
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/reports" element={<Reports />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </Suspense>
    </Router>
  );
};
```

#### 虚拟滚动
```typescript
import { FixedSizeList as List } from 'react-window';

interface VirtualizedListProps {
  items: PowerPlatformData[];
  itemHeight: number;
  height: number;
}

export const VirtualizedList: React.FC<VirtualizedListProps> = ({
  items,
  itemHeight,
  height
}) => {
  const Row = ({ index, style }: { index: number; style: React.CSSProperties }) => (
    <div style={style}>
      <DataItem item={items[index]} />
    </div>
  );

  return (
    <List
      height={height}
      itemCount={items.length}
      itemSize={itemHeight}
      width="100%"
    >
      {Row}
    </List>
  );
};
```

### 测试

#### 单元测试
```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { PowerProvider } from './PowerProvider';
import { DataComponent } from './DataComponent';

// Mock Power Platform SDK
jest.mock('@microsoft/power-apps', () => ({
  PowerApps: {
    getEnvironmentInfo: jest.fn().mockResolvedValue({
      id: 'env-id',
      name: 'Test Environment'
    }),
    getCurrentUserInfo: jest.fn().mockResolvedValue({
      id: 'user-id',
      displayName: 'Test User'
    })
  }
}));

describe('DataComponent', () => {
  const renderWithProvider = (component: React.ReactElement) => {
    return render(
      <PowerProvider>
        {component}
      </PowerProvider>
    );
  };

  it('应该显示加载状态', () => {
    renderWithProvider(<DataComponent />);
    expect(screen.getByText('加载中...')).toBeInTheDocument();
  });

  it('应该成功加载数据', async () => {
    renderWithProvider(<DataComponent />);

    await waitFor(() => {
      expect(screen.getByText('数据加载完成')).toBeInTheDocument();
    });
  });

  it('应该处理数据加载错误', async () => {
    // 模拟错误
    jest.spyOn(console, 'error').mockImplementation(() => {});

    renderWithProvider(<DataComponent />);

    await waitFor(() => {
      expect(screen.getByText('数据加载失败')).toBeInTheDocument();
    });
  });
});
```

#### 集成测试
```typescript
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { PowerProvider } from './PowerProvider';
import { MainForm } from './MainForm';

describe('MainForm 集成测试', () => {
  const user = userEvent.setup();

  beforeEach(() => {
    // 清除所有模拟
    jest.clearAllMocks();
  });

  it('应该成功提交表单', async () => {
    render(
      <PowerProvider>
        <MainForm />
      </PowerProvider>
    );

    // 填写表单
    await user.type(screen.getByLabelText('姓名'), 'John Doe');
    await user.type(screen.getByLabelText('邮箱'), 'john@example.com');

    // 提交表单
    await user.click(screen.getByRole('button', { name: '提交' }));

    // 验证成功消息
    await expect(screen.getByText('表单提交成功')).toBeInTheDocument();
  });

  it('应该显示验证错误', async () => {
    render(
      <PowerProvider>
        <MainForm />
      </PowerProvider>
    );

    // 提交空表单
    await user.click(screen.getByRole('button', { name: '提交' }));

    // 验证错误消息
    await expect(screen.getByText('姓名是必需的')).toBeInTheDocument();
    await expect(screen.getByText('邮箱是必需的')).toBeInTheDocument();
  });
});
```

### 部署和 CI/CD

#### GitHub Actions 工作流
```yaml
name: Power Apps Code App CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: 设置 Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'

    - name: 安装依赖
      run: npm ci

    - name: 运行测试
      run: npm test

    - name: 构建应用
      run: npm run build

    - name: 上传构建产物
      uses: actions/upload-artifact@v3
      with:
        name: build-files
        path: dist/

  deploy:
    needs: build-and-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
    - uses: actions/checkout@v3

    - name: 下载构建产物
      uses: actions/download-artifact@v3
      with:
        name: build-files
        path: dist/

    - name: 设置 Power Platform CLI
      run: |
        wget -q https://aka.ms/PowerAppsCLI -O powerapps-cli.tar.gz
        tar -xzf powerapps-cli.tar.gz
        sudo mv powerapps-cli /usr/local/bin/

    - name: 部署到 Power Apps
      env:
        POWER_APPS_URL: ${{ secrets.POWER_APPS_URL }}
        POWER_APPS_USERNAME: ${{ secrets.POWER_APPS_USERNAME }}
        POWER_APPS_PASSWORD: ${{ secrets.POWER_APPS_PASSWORD }}
      run: |
        pac auth create --url $POWER_APPS_URL --username $POWER_APPS_USERNAME --password $POWER_APPS_PASSWORD
        pac canvas publish --app-path ./dist
```

### 安全最佳实践

#### API 密钥管理
```typescript
// 环境变量配置
export const config = {
  powerApps: {
    environmentId: process.env.REACT_APP_POWER_APPS_ENVIRONMENT_ID,
    apiUrl: process.env.REACT_APP_POWER_APPS_API_URL,
    clientId: process.env.REACT_APP_CLIENT_ID
  },
  logging: {
    level: process.env.REACT_APP_LOG_LEVEL || 'info'
  }
};

// 安全的服务调用
export const secureApiCall = async (endpoint: string, data: any) => {
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': process.env.REACT_APP_API_KEY || '',
    },
    body: JSON.stringify(data)
  });

  if (!response.ok) {
    throw new Error(`API 调用失败: ${response.statusText}`);
  }

  return response.json();
};
```

### 监控和分析

#### 应用程序性能监控
```typescript
import { getPowerAppsService } from './services/powerPlatformService';

export class PerformanceMonitor {
  private static instance: PerformanceMonitor;

  static getInstance(): PerformanceMonitor {
    if (!PerformanceMonitor.instance) {
      PerformanceMonitor.instance = new PerformanceMonitor();
    }
    return PerformanceMonitor.instance;
  }

  async trackPageView(pageName: string) {
    const startTime = performance.now();

    // 发送页面视图数据到 Power Platform
    try {
      const analyticsService = getPowerAppsService('AnalyticsService');
      await analyticsService.trackPageView({
        pageName,
        timestamp: new Date().toISOString(),
        loadTime: startTime
      });
    } catch (error) {
      console.error('跟踪页面视图失败:', error);
    }
  }

  async trackUserAction(action: string, properties?: Record<string, any>) {
    try {
      const analyticsService = getPowerAppsService('AnalyticsService');
      await analyticsService.trackEvent({
        action,
        properties,
        timestamp: new Date().toISOString()
      });
    } catch (error) {
      console.error('跟踪用户操作失败:', error);
    }
  }
}
```

## 总结

Power Apps 代码应用开发需要：
- 遵循 React 和 TypeScript 最佳实践
- 充分利用 Power Platform SDK 功能
- 实现强大的错误处理和性能优化
- 确保安全性和可访问性
- 建立全面的测试策略
- 配置适当的 CI/CD 管道

通过遵循这些标准，您可以构建高质量、可维护的 Power Apps 代码应用。