---
description: '使用官方 PHP SDK 构建模型上下文协议服务器的最佳实践，具有基于属性的发现和多种传输选项'
applyTo: '**/*.php'
---

# PHP MCP 服务器开发最佳实践

本指南提供了使用与 PHP Foundation 协作维护的官方 PHP SDK 构建模型上下文协议 (MCP) 服务器的最佳实践。

## 安装和设置

### 通过 Composer 安装

```bash
composer require mcp/sdk
```

### 项目结构

组织您的 PHP MCP 服务器项目：

```
my-mcp-server/
├── composer.json
├── src/
│   ├── Tools/
│   │   ├── Calculator.php
│   │   └── FileManager.php
│   ├── Resources/
│   │   ├── ConfigProvider.php
│   │   └── DataProvider.php
│   ├── Prompts/
│   │   └── PromptGenerator.php
│   └── Server.php
├── server.php           # 服务器入口点
└── tests/
    └── ToolsTest.php
```

### Composer 配置

```json
{
    "name": "your-org/mcp-server",
    "description": "用于...的 MCP 服务器",
    "type": "project",
    "require": {
        "php": "^8.2",
        "mcp/sdk": "^0.1"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}
```

## 服务器实现

### 具有属性发现的基本服务器

创建您的服务器入口点：

```php
#!/usr/bin/env php
<?php

declare(strict_types=1);

require_once __DIR__ . '/vendor/autoload.php';

use Mcp\Server;
use Mcp\Server\Transport\StdioTransport;

$server = Server::builder()
    ->setServerInfo('My MCP Server', '1.0.0')
    ->setDiscovery(__DIR__, ['.'])
    ->build();

$transport = new StdioTransport();

$server->run($transport);
```

### 具有缓存的服务器

使用 PSR-16 缓存以获得更好的性能：

```php
use Symfony\Component\Cache\Adapter\FilesystemAdapter;
use Symfony\Component\Cache\Psr16Cache;

$cache = new Psr16Cache(new FilesystemAdapter('mcp-discovery'));

$server = Server::builder()
    ->setServerInfo('My MCP Server', '1.0.0')
    ->setDiscovery(__DIR__, ['.'], $cache)
    ->build();
```

## 工具开发

### 使用属性定义工具

```php
<?php

declare(strict_types=1);

namespace App\Tools;

use Mcp\Server\Attributes\AsTool;
use Mcp\Server\Attributes\Description;
use Mcp\Server\Attributes\Name;
use Mcp\Server\Attributes\InputSchema;
use Mcp\Server\Attributes\Required;
use Mcp\Server\ToolResponse;

#[AsTool]
#[Name('calculator')]
#[Description('执行数学运算')]
class Calculator
{
    #[InputSchema(
        properties: [
            'operation' => [
                'type' => 'string',
                'enum' => ['add', 'subtract', 'multiply', 'divide'],
                'description' => '要执行的运算'
            ],
            'a' => [
                'type' => 'number',
                'description' => '第一个操作数'
            ],
            'b' => [
                'type' => 'number',
                'description' => '第二个操作数'
            ]
        ],
        required: ['operation', 'a', 'b']
    )]
    public function calculate(
        #[Name('operation')] string $operation,
        #[Name('a')] float $a,
        #[Name('b')] float $b
    ): ToolResponse {
        $result = match ($operation) {
            'add' => $a + $b,
            'subtract' => $a - $b,
            'multiply' => $a * $b,
            'divide' => $b === 0.0 ? throw new \InvalidArgumentException('除零错误') : $a / $b,
            default => throw new \InvalidArgumentException("未知运算：{$operation}")
        };

        $message = "{$a} {$operation} {$b} = {$result}";

        return new ToolResponse([
            [
                'type' => 'text',
                'text' => $message
            ]
        ], [
            'operation' => $operation,
            'operands' => [$a, $b],
            'result' => $result,
            'message' => $message
        ]);
    }
}
```

### 异步工具实现

```php
<?php

declare(strict_types=1);

namespace App\Tools;

use Mcp\Server\Attributes\AsTool;
use Mcp\Server\Attributes\Name;
use Mcp\Server\Attributes\Description;
use Mcp\Server\ToolResponse;

#[AsTool]
#[Name('async_processor')]
#[Description('异步处理数据')]
class AsyncProcessor
{
    public function process(
        #[Name('data')] array $data,
        #[Name('operation')] string $operation
    ): ToolResponse {
        // 使用 ReactPHP 进行异步处理
        $deferred = new \React\Promise\Deferred();

        // 模拟异步操作
        \React\Async\delay(0.1)->then(function () use ($deferred, $data, $operation) {
            $result = $this->performOperation($data, $operation);
            $deferred->resolve($result);
        });

        return new ToolResponse([
            [
                'type' => 'text',
                'text' => '异步处理已开始'
            ]
        ]);
    }

    private function performOperation(array $data, string $operation): array
    {
        return match ($operation) {
            'sum' => ['result' => array_sum($data)],
            'average' => ['result' => array_sum($data) / count($data)],
            'max' => ['result' => max($data)],
            'min' => ['result' => min($data)],
            default => throw new \InvalidArgumentException("未知操作：{$operation}")
        };
    }
}
```

## 资源开发

### 资源提供者实现

```php
<?php

declare(strict_types=1);

namespace App\Resources;

use Mcp\Server\Attributes\AsResource;
use Mcp\Server\Attributes\Name;
use Mcp\Server\Attributes\Description;
use Mcp\Server\Attributes\Uri;
use Mcp\Server\ResourceResponse;

#[AsResource]
#[Name('config')]
#[Description('提供配置数据')]
#[Uri('config://app/settings')]
class ConfigProvider
{
    private array $config;

    public function __construct()
    {
        $this->config = $this->loadConfig();
    }

    public function read(): ResourceResponse
    {
        return new ResourceResponse([
            [
                'type' => 'text',
                'text' => json_encode($this->config, JSON_PRETTY_PRINT),
                'uri' => 'config://app/settings'
            ]
        ]);
    }

    public function watch(): \Generator
    {
        // 实现文件监视功能
        while (true) {
            $currentConfig = $this->loadConfig();
            if ($currentConfig !== $this->config) {
                $this->config = $currentConfig;
                yield new ResourceResponse([
                    [
                        'type' => 'text',
                        'text' => '配置已更新',
                        'uri' => 'config://app/settings'
                    ]
                ]);
            }
            sleep(5);
        }
    }

    private function loadConfig(): array
    {
        $configFile = __DIR__ . '/../../config/app.json';
        if (!file_exists($configFile)) {
            return [];
        }

        return json_decode(file_get_contents($configFile), true);
    }
}
```

### 数据库资源

```php
<?php

declare(strict_types=1);

namespace App\Resources;

use Mcp\Server\Attributes\AsResource;
use Mcp\Server\Attributes\Name;
use Mcp\Server\Attributes\Description;
use Mcp\Server\Attributes\Uri;
use Mcp\Server\ResourceResponse;
use PDO;

#[AsResource]
#[Name('database_query')]
#[Description('执行数据库查询')]
#[Uri('db://users')]
class DatabaseProvider
{
    private PDO $pdo;

    public function __construct(PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    public function read(): ResourceResponse
    {
        $stmt = $this->pdo->query('SELECT id, name, email FROM users LIMIT 100');
        $users = $stmt->fetchAll(PDO::FETCH_ASSOC);

        return new ResourceResponse([
            [
                'type' => 'text',
                'text' => json_encode($users, JSON_PRETTY_PRINT),
                'uri' => 'db://users'
            ]
        ]);
    }

    public function readWithParams(array $params): ResourceResponse
    {
        $limit = $params['limit'] ?? 100;
        $offset = $params['offset'] ?? 0;

        $stmt = $this->pdo->prepare('SELECT id, name, email FROM users LIMIT :limit OFFSET :offset');
        $stmt->bindValue(':limit', $limit, PDO::PARAM_INT);
        $stmt->bindValue(':offset', $offset, PDO::PARAM_INT);
        $stmt->execute();

        $users = $stmt->fetchAll(PDO::FETCH_ASSOC);

        return new ResourceResponse([
            [
                'type' => 'text',
                'text' => json_encode($users, JSON_PRETTY_PRINT),
                'uri' => 'db://users'
            ]
        ]);
    }
}
```

## 提示开发

### 提示生成器

```php
<?php

declare(strict_types=1);

namespace App\Prompts;

use Mcp\Server\Attributes\AsPrompt;
use Mcp\Server\Attributes\Name;
use Mcp\Server\Attributes\Description;
use Mcp\Server\Attributes\Argument;
use Mcp\Server\PromptResponse;

#[AsPrompt]
#[Name('code_review')]
#[Description('生成代码审查提示')]
class PromptGenerator
{
    #[Argument(
        name: 'code',
        description: '要审查的代码',
        required: true
    )]
    #[Argument(
        name: 'language',
        description: '编程语言',
        required: false
    )]
    #[Argument(
        name: 'focus',
        description: '审查重点',
        required: false
    )]
    public function generate(
        string $code,
        ?string $language = null,
        ?string $focus = null
    ): PromptResponse {
        $language = $language ?? 'unknown';
        $focus = $focus ?? 'general';

        $systemMessage = $this->buildSystemMessage($language, $focus);
        $userMessage = $this->buildUserMessage($code);

        return new PromptResponse(
            description: "审查 {$language} 代码",
            messages: [
                [
                    'role' => 'system',
                    'content' => [
                        'type' => 'text',
                        'text' => $systemMessage
                    ]
                ],
                [
                    'role' => 'user',
                    'content' => [
                        'type' => 'text',
                        'text' => $userMessage
                    ]
                ]
            ]
        );
    }

    private function buildSystemMessage(string $language, string $focus): string
    {
        $baseMessage = "你是一个专业的代码审查者。请审查以下 {$language} 代码。";

        return match ($focus) {
            'security' => $baseMessage . "特别关注安全漏洞和潜在风险。",
            'performance' => $baseMessage . "特别关注性能优化和效率问题。",
            'readability' => $baseMessage . "特别关注代码可读性和维护性。",
            'best_practices' => $baseMessage . "特别关注最佳实践和设计模式。",
            default => $baseMessage . "进行全面的代码审查。"
        };
    }

    private function buildUserMessage(string $code): string
    {
        return "请审查以下代码：\n\n```{$language}\n{$code}\n```";
    }
}
```

## 错误处理

### 自定义异常处理

```php
<?php

declare(strict_types=1);

namespace App\Exception;

use Mcp\Server\McpError;

class ToolException extends McpError
{
    public static function invalidParams(string $message): self
    {
        return new self($message, -32602);
    }

    public static function toolNotFound(string $toolName): self
    {
        return new self("工具未找到：{$toolName}", -32601);
    }

    public static function executionFailed(string $message, \Throwable $previous = null): self
    {
        return new self($message, -32603, $previous);
    }
}

class ResourceException extends McpError
{
    public static function notFound(string $uri): self
    {
        return new self("资源未找到：{$uri}", -32602);
    }

    public static function accessDenied(string $uri): self
    {
        return new self("访问被拒绝：{$uri}", -32603);
    }
}
```

### 全局错误处理器

```php
<?php

declare(strict_types=1);

namespace App\Handler;

use Mcp\Server\ErrorHandlerInterface;
use Mcp\Server\Request;
use Mcp\Server\Response;
use Psr\Log\LoggerInterface;

class GlobalErrorHandler implements ErrorHandlerInterface
{
    public function __construct(
        private LoggerInterface $logger
    ) {
    }

    public function handle(\Throwable $error, Request $request): Response
    {
        $this->logger->error('MCP 服务器错误', [
            'error' => $error->getMessage(),
            'file' => $error->getFile(),
            'line' => $error->getLine(),
            'trace' => $error->getTraceAsString()
        ]);

        if ($error instanceof Mcp\Server\McpError) {
            return new Response([
                'jsonrpc' => '2.0',
                'id' => $request->getId(),
                'error' => [
                    'code' => $error->getCode(),
                    'message' => $error->getMessage()
                ]
            ]);
        }

        return new Response([
            'jsonrpc' => '2.0',
            'id' => $request->getId(),
            'error' => [
                'code' => -32603,
                'message' => '内部错误'
            ]
        ]);
    }
}
```

## 日志记录

### PSR-3 日志实现

```php
<?php

declare(strict_types=1);

namespace App\Logging;

use Psr\Log\AbstractLogger;
use Psr\Log\LogLevel;

class FileLogger extends AbstractLogger
{
    private string $logFile;

    public function __construct(string $logFile)
    {
        $this->logFile = $logFile;
    }

    public function log($level, $message, array $context = []): void
    {
        $timestamp = date('Y-m-d H:i:s');
        $contextStr = empty($context) ? '' : ' ' . json_encode($context);
        $logEntry = "[{$timestamp}] {$level}: {$message}{$contextStr}" . PHP_EOL;

        file_put_contents($this->logFile, $logEntry, FILE_APPEND | LOCK_EX);
    }
}

// 使用示例
$logger = new FileLogger(__DIR__ . '/logs/mcp.log');

$server = Server::builder()
    ->setServerInfo('My MCP Server', '1.0.0')
    ->setLogger($logger)
    ->setDiscovery(__DIR__, ['.'])
    ->build();
```

### 结构化日志记录

```php
<?php

declare(strict_types=1);

namespace App\Logging;

use Monolog\Logger;
use Monolog\Handler\StreamHandler;
use Monolog\Processor\ProcessIdProcessor;
use Monolog\Processor\MemoryUsageProcessor;

class StructuredLoggerFactory
{
    public static function create(string $name, string $logFile): Logger
    {
        $logger = new Logger($name);

        $handler = new StreamHandler($logFile, Logger::DEBUG);
        $handler->setFormatter(new \Monolog\Formatter\JsonFormatter());

        $logger->pushHandler($handler);
        $logger->pushProcessor(new ProcessIdProcessor());
        $logger->pushProcessor(new MemoryUsageProcessor());

        return $logger;
    }
}

// 在工具中使用
$logger = StructuredLoggerFactory::create('mcp-server', __DIR__ . '/logs/mcp.json');

#[AsTool]
#[Name('data_processor')]
class DataProcessor
{
    public function __construct(
        private LoggerInterface $logger
    ) {
    }

    public function process(array $data): ToolResponse
    {
        $this->logger->info('开始数据处理', [
            'data_size' => count($data),
            'memory_usage' => memory_get_usage(true)
        ]);

        try {
            $result = $this->performProcessing($data);

            $this->logger->info('数据处理完成', [
                'result_size' => count($result),
                'execution_time' => microtime(true) - $startTime
            ]);

            return new ToolResponse([[...]]);
        } catch (\Exception $e) {
            $this->logger->error('数据处理失败', [
                'error' => $e->getMessage(),
                'trace' => $e->getTraceAsString()
            ]);

            throw $e;
        }
    }
}
```

## 测试

### PHPUnit 测试示例

```php
<?php

declare(strict_types=1);

namespace Tests\Tools;

use PHPUnit\Framework\TestCase;
use App\Tools\Calculator;
use Mcp\Server\ToolResponse;

class CalculatorTest extends TestCase
{
    private Calculator $calculator;

    protected function setUp(): void
    {
        $this->calculator = new Calculator();
    }

    public function testAddition(): void
    {
        $response = $this->calculator->calculate('add', 5.0, 3.0);

        $this->assertInstanceOf(ToolResponse::class, $response);
        $this->assertStringContainsString('5 add 3 = 8', $response->getContent()[0]['text']);
        $this->assertEquals(8.0, $response->getStructuredContent()['result']);
    }

    public function testDivisionByZero(): void
    {
        $this->expectException(\InvalidArgumentException::class);
        $this->expectExceptionMessage('除零错误');

        $this->calculator->calculate('divide', 5.0, 0.0);
    }

    public function testInvalidOperation(): void
    {
        $this->expectException(\InvalidArgumentException::class);
        $this->expectExceptionMessage('未知运算：invalid');

        $this->calculator->calculate('invalid', 5.0, 3.0);
    }

    /**
     * @dataProvider calculationProvider
     */
    public function testCalculations(string $operation, float $a, float $b, float $expected): void
    {
        $response = $this->calculator->calculate($operation, $a, $b);

        $this->assertEquals($expected, $response->getStructuredContent()['result']);
    }

    public static function calculationProvider(): array
    {
        return [
            ['add', 2.0, 3.0, 5.0],
            ['subtract', 10.0, 4.0, 6.0],
            ['multiply', 3.0, 4.0, 12.0],
            ['divide', 8.0, 2.0, 4.0],
        ];
    }
}
```

### 集成测试

```php
<?php

declare(strict_types=1);

namespace Tests\Integration;

use PHPUnit\Framework\TestCase;
use Mcp\Server;
use Mcp\Server\Transport\InMemoryTransport;
use App\Server;

class ServerIntegrationTest extends TestCase
{
    private Server $server;
    private InMemoryTransport $transport;

    protected function setUp(): void
    {
        $this->server = Server::builder()
            ->setServerInfo('Test Server', '1.0.0')
            ->setDiscovery(__DIR__ . '/../src', ['App'])
            ->build();

        $this->transport = new InMemoryTransport();
    }

    public function testToolList(): void
    {
        $request = [
            'jsonrpc' => '2.0',
            'id' => 1,
            'method' => 'tools/list',
            'params' => []
        ];

        $this->transport->sendRequest(json_encode($request));
        $response = $this->server->runOnce($this->transport);

        $responseData = json_decode($response, true);

        $this->assertArrayHasKey('result', $responseData);
        $this->assertArrayHasKey('tools', $responseData['result']);
        $this->assertNotEmpty($responseData['result']['tools']);
    }

    public function testToolCall(): void
    {
        $request = [
            'jsonrpc' => '2.0',
            'id' => 2,
            'method' => 'tools/call',
            'params' => [
                'name' => 'calculator',
                'arguments' => [
                    'operation' => 'add',
                    'a' => 5.0,
                    'b' => 3.0
                ]
            ]
        ];

        $this->transport->sendRequest(json_encode($request));
        $response = $this->server->runOnce($this->transport);

        $responseData = json_decode($response, true);

        $this->assertArrayHasKey('result', $responseData);
        $this->assertArrayHasKey('content', $responseData['result']);
        $this->assertStringContainsString('8', $responseData['result']['content'][0]['text']);
    }
}
```

## 部署

### Docker 配置

```dockerfile
FROM php:8.2-cli

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 安装 Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY composer.json composer.lock ./

# 安装依赖
RUN composer install --no-dev --optimize-autoloader

# 复制应用代码
COPY . .

# 设置权限
RUN chmod +x server.php

# 暴露端口
EXPOSE 8080

# 启动命令
CMD ["php", "server.php"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  mcp-server:
    build: .
    ports:
      - "8080:8080"
    environment:
      - APP_ENV=production
      - LOG_LEVEL=info
    volumes:
      - ./logs:/app/logs
      - ./config:/app/config
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    restart: unless-stopped

  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: mcp_db
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
    restart: unless-stopped

volumes:
  mysql_data:
```

## 性能优化

### 缓存实现

```php
<?php

declare(strict_types=1);

namespace App\Cache;

use Psr\SimpleCache\CacheInterface;

class ToolResultCache
{
    public function __construct(
        private CacheInterface $cache,
        private int $ttl = 3600
    ) {
    }

    public function get(string $key, callable $callback): mixed
    {
        if ($this->cache->has($key)) {
            return $this->cache->get($key);
        }

        $result = $callback();
        $this->cache->set($key, $result, $this->ttl);

        return $result;
    }

    public function generateKey(string $toolName, array $arguments): string
    {
        return md5($toolName . serialize($arguments));
    }
}

// 在工具中使用
#[AsTool]
#[Name('cached_calculator')]
class CachedCalculator
{
    public function __construct(
        private ToolResultCache $cache
    ) {
    }

    public function calculate(string $operation, float $a, float $b): ToolResponse
    {
        $key = $this->cache->generateKey('calculator', [
            'operation' => $operation,
            'a' => $a,
            'b' => $b
        ]);

        return $this->cache->get($key, function () use ($operation, $a, $b) {
            return $this->performCalculation($operation, $a, $b);
        });
    }

    private function performCalculation(string $operation, float $a, float $b): ToolResponse
    {
        // 实际计算逻辑
        return new ToolResponse([[...]]);
    }
}
```

## 总结

使用 PHP 构建 MCP 服务器提供了：
- 丰富的框架和包生态系统
- 强大的类型安全和现代化特性
- 灵活的属性发现机制
- 优秀的工具和 IDE 支持
- 成熟的测试和部署解决方案

遵循这些最佳实践将帮助您构建可靠、高性能的 PHP MCP 服务器。