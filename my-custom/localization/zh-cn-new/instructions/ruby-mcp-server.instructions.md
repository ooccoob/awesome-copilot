---
description: '使用官方 MCP Ruby SDK gem 在 Ruby 中构建模型上下文协议 (MCP) 服务器的最佳实践和模式。'
applyTo: "**/*.rb, **/Gemfile, **/*.gemspec, **/Rakefile"
---

# Ruby MCP 服务器开发指南

在 Ruby 中构建 MCP 服务器时，遵循这些使用官方 Ruby SDK 的最佳实践和模式。

## 安装

将 MCP gem 添加到您的 Gemfile：

```ruby
gem 'mcp'
```

然后运行：

```bash
bundle install
```

## 服务器设置

创建 MCP 服务器实例：

```ruby
require 'mcp'

server = MCP::Server.new(
  name: 'my_server',
  version: '1.0.0'
)
```

## 添加工具

使用类或代码块定义工具：

### 工具作为类

```ruby
class GreetTool < MCP::Tool
  tool_name 'greet'
  description '生成问候消息'

  input_schema(
    properties: {
      name: { type: 'string', description: '要问候的名字' }
    },
    required: ['name']
  )

  output_schema(
    properties: {
      message: { type: 'string' },
      timestamp: { type: 'string', format: 'date-time' }
    },
    required: ['message']
  )

  annotations(
    read_only_hint: true,
    idempotent_hint: true
  )

  def self.call(name:, server_context:)
    MCP::Tool::Response.new([{
      type: 'text',
      text: "你好，#{name}！欢迎使用 MCP。"
    }], structured_content: {
      message: "你好，#{name}！",
      timestamp: Time.now.iso8601
    })
  end
end

server = MCP::Server.new(
  name: 'my_server',
  tools: [GreetTool]
)
```

### 使用代码块的工具

```ruby
server.define_tool(
  name: 'calculate',
  description: '执行数学计算',
  input_schema: {
    properties: {
      operation: { type: 'string', enum: ['add', 'subtract', 'multiply', 'divide'] },
      a: { type: 'number' },
      b: { type: 'number' }
    },
    required: ['operation', 'a', 'b']
  },
  annotations: {
    read_only_hint: true,
    idempotent_hint: true
  }
) do |operation:, a:, b:, server_context:|
  result = case operation
           when 'add'
             a + b
           when 'subtract'
             a - b
           when 'multiply'
             a * b
           when 'divide'
             raise '除零错误' if b == 0
             a / b
           else
             raise "未知操作：#{operation}"
           end

  MCP::Tool::Response.new([{
    type: 'text',
    text: "#{a} #{operation} #{b} = #{result}"
  }], structured_content: {
    operation: operation,
    operands: [a, b],
    result: result
  })
end
```

## 添加资源

定义资源处理器：

```ruby
class DataResource < MCP::Resource
  resource_name 'data_file'
  description '访问数据文件'
  uri 'data://example/file.txt'
  mime_type 'text/plain'

  def self.read(server_context:)
    content = File.read('/path/to/data.txt')
    MCP::Resource::Response.new([{
      type: 'text',
      text: content,
      uri: 'data://example/file.txt'
    }])
  end
end

server = MCP::Server.new(
  name: 'my_server',
  resources: [DataResource]
)
```

## 添加提示

定义提示模板：

```ruby
class CodeReviewPrompt < MCP::Prompt
  prompt_name 'code_review'
  description '为代码提供审查反馈'

  arguments([
    {
      name: 'code',
      description: '要审查的代码',
      required: true
    },
    {
      name: 'language',
      description: '编程语言',
      required: false
    }
  ])

  def self.get(code:, language: 'unknown', server_context:)
    messages = [
      {
        role: 'user',
        content: {
          type: 'text',
          text: "请审查以下 #{language} 代码并提供反馈：\n\n#{code}"
        }
      }
    ]

    MCP::Prompt::Response.new(
      description: "#{language} 代码审查",
      messages: messages
    )
  end
end

server = MCP::Server.new(
  name: 'my_server',
  prompts: [CodeReviewPrompt]
)
```

## 服务器配置

### 基本配置

```ruby
server = MCP::Server.new(
  name: 'my_ruby_server',
  version: '1.0.0',
  capabilities: {
    tools: { listChanged: true },
    resources: { subscribe: true, listChanged: true },
    prompts: { listChanged: true }
  }
)
```

### 自定义传输层

```ruby
# 使用自定义传输层
class CustomTransport
  def initialize
    @running = false
  end

  def start
    @running = true
    puts "自定义传输层已启动"

    while @running
      message = receive_message
      handle_message(message) if message
    end
  end

  def stop
    @running = false
    puts "自定义传输层已停止"
  end

  private

  def receive_message
    # 实现消息接收逻辑
    nil
  end

  def handle_message(message)
    # 实现消息处理逻辑
  end
end

server = MCP::Server.new(
  name: 'my_server',
  transport: CustomTransport.new
)
```

## 错误处理

### 自定义异常

```ruby
class MCPServerError < StandardError
  attr_reader :code, :data

  def initialize(message, code: nil, data: nil)
    super(message)
    @code = code
    @data = data
  end
end

class ToolNotFoundError < MCPServerError
  def initialize(tool_name)
    super("工具未找到：#{tool_name}", code: -32601)
  end
end

class InvalidParamsError < MCPServerError
  def initialize(message)
    super(message, code: -32602)
  end
end
```

### 错误处理模式

```ruby
server.define_tool(
  name: 'risky_operation',
  description: '可能失败的操作',
  input_schema: {
    properties: {
      input: { type: 'string' }
    },
    required: ['input']
  }
) do |input:, server_context:|
  begin
    # 执行风险操作
    result = perform_risky_operation(input)

    MCP::Tool::Response.new([{
      type: 'text',
      text: "操作成功：#{result}"
    }], isError: false)
  rescue ToolNotFoundError => e
    MCP::Tool::Response.new([{
      type: 'text',
      text: e.message
    }], isError: true, error: {
      code: e.code,
      message: e.message
    })
  rescue StandardError => e
    server_context.logger.error("操作失败：#{e.message}")
    MCP::Tool::Response.new([{
      type: 'text',
      text: "操作失败：#{e.message}"
    }], isError: true)
  end
end
```

## 日志记录

### 配置日志记录

```ruby
require 'logger'

# 自定义日志记录器
logger = Logger.new(STDOUT)
logger.level = Logger::INFO
logger.formatter = proc do |severity, datetime, progname, msg|
  "[#{datetime}] #{severity}: #{msg}\n"
end

server = MCP::Server.new(
  name: 'my_server',
  logger: logger
)
```

### 结构化日志记录

```ruby
require 'json'

class StructuredLogger
  def initialize(output = STDOUT)
    @logger = Logger.new(output)
  end

  def info(message, metadata = {})
    log('INFO', message, metadata)
  end

  def warn(message, metadata = {})
    log('WARN', message, metadata)
  end

  def error(message, metadata = {})
    log('ERROR', message, metadata)
  end

  private

  def log(level, message, metadata)
    log_entry = {
      timestamp: Time.now.iso8601,
      level: level,
      message: message,
      metadata: metadata
    }.to_json

    @logger.info(log_entry)
  end
end

server = MCP::Server.new(
  name: 'my_server',
  logger: StructuredLogger.new
)
```

## 测试

### 单元测试工具

```ruby
require 'test_helper'

class GreetToolTest < Minitest::Test
  def setup
    @server_context = OpenStruct.new(logger: Logger.new(STDOUT))
  end

  def test_greet_tool_with_name
    result = GreetTool.call(name: '世界', server_context: @server_context)

    assert_equal false, result.is_error
    assert_equal 1, result.content.length
    assert_includes result.content.first['text'], '你好，世界！'
    assert_equal '你好，世界！', result.structured_content[:message]
  end

  def test_greet_tool_without_name
    assert_raises(ArgumentError) do
      GreetTool.call(server_context: @server_context)
    end
  end
end
```

### 集成测试

```ruby
require 'test_helper'

class ServerIntegrationTest < Minitest::Test
  def setup
    @server = MCP::Server.new(
      name: 'test_server',
      tools: [GreetTool]
    )
  end

  def test_list_tools
    tools = @server.list_tools
    assert_equal 1, tools.length
    assert_equal 'greet', tools.first['name']
  end

  def test_call_greet_tool
    result = @server.call_tool('greet', { name: 'Ruby' })

    assert_equal false, result[:isError]
    assert_includes result[:content].first[:text], '你好，Ruby！'
  end

  def test_call_unknown_tool
    result = @server.call_tool('unknown_tool', {})

    assert_equal true, result[:isError]
    assert_includes result[:content].first[:text], '未找到工具'
  end
end
```

## 性能优化

### 缓存机制

```ruby
require 'digest'

class CachedTool < MCP::Tool
  def initialize(name, description, cache = {})
    super(name, description)
    @cache = cache
    @cache_ttl = 3600 # 1小时
  end

  def call_with_cache(**args)
    cache_key = generate_cache_key(args)

    # 检查缓存
    if cached_result = @cache[cache_key]
      if Time.now - cached_result[:timestamp] < @cache_ttl
        return cached_result[:result]
      end
    end

    # 执行工具
    result = call(**args)

    # 更新缓存
    @cache[cache_key] = {
      result: result,
      timestamp: Time.now
    }

    result
  end

  private

  def generate_cache_key(args)
    args_hash = args.to_s
    Digest::SHA256.hexdigest(args_hash)
  end
end
```

### 并发处理

```ruby
require 'concurrent-ruby'

class ConcurrentServer < MCP::Server
  def initialize(name:, tools: [], **options)
    super(name: name, tools: tools, **options)
    @executor = Concurrent::ThreadPoolExecutor.new(
      min_threads: 2,
      max_threads: 10
    )
  end

  def call_tool_async(tool_name, arguments, &block)
    future = Concurrent::Future.execute(executor: @executor) do
      call_tool(tool_name, arguments)
    end

    future.then(&block) if block
    future
  end

  def shutdown
    @executor.shutdown
    @executor.wait_for_termination(30)
  end
end
```

## 部署

### 使用 Rack

```ruby
# config.ru
require 'my_mcp_server'

class MCPHandler
  def call(env)
    request = Rack::Request.new(env)

    case request.path_info
    when '/mcp'
      handle_mcp_request(request)
    else
      [404, {}, ['Not Found']]
    end
  end

  private

  def handle_mcp_request(request)
    begin
      body = JSON.parse(request.body.read)

      case body['method']
      when 'tools/list'
        response = server.list_tools
      when 'tools/call'
        response = server.call_tool(
          body['params']['name'],
          body['params']['arguments']
        )
      else
        response = { error: { code: -32601, message: 'Method not found' } }
      end

      [200, { 'Content-Type' => 'application/json' }, [response.to_json]]
    rescue StandardError => e
      [500, { 'Content-Type' => 'application/json' }, [{
        error: { code: -32603, message: e.message }
      }.to_json]]
    end
  end
end

run MCPHandler.new
```

### 系统服务配置

```yaml
# mcp-server.service (systemd)
[Unit]
Description=Ruby MCP Server
After=network.target

[Service]
Type=simple
User=mcp
Group=mcp
WorkingDirectory=/opt/mcp-server
ExecStart=/usr/bin/bundle exec ruby server.rb
Restart=always
RestartSec=10
Environment=RACK_ENV=production

[Install]
WantedBy=multi-user.target
```

## 最佳实践

### 1. 模块化设计

```ruby
module MyMCPTools
  class BaseTool < MCP::Tool
    def initialize(name, description)
      super(name, description)
      @logger = Logger.new(STDOUT)
    end

    protected

    def log_info(message)
      @logger.info("[#{self.class.name}] #{message}")
    end

    def log_error(message)
      @logger.error("[#{self.class.name}] #{message}")
    end
  end

  class CalculatorTool < BaseTool
    def initialize
      super('calculator', '执行数学计算')
    end

    def call(operation:, a:, b:, server_context:)
      log_info("执行计算：#{a} #{operation} #{b}")

      result = perform_calculation(operation, a, b)

      log_info("计算结果：#{result}")
      MCP::Tool::Response.new([{
        type: 'text',
        text: "#{a} #{operation} #{b} = #{result}"
      }])
    end

    private

    def perform_calculation(operation, a, b)
      case operation
      when 'add' then a + b
      when 'subtract' then a - b
      when 'multiply' then a * b
      when 'divide'
        raise '除零错误' if b == 0
        a / b
      else
        raise "未知操作：#{operation}"
      end
    end
  end
end
```

### 2. 配置管理

```ruby
require 'yaml'

class ServerConfig
  def self.load(file_path = 'config/mcp.yml')
    config_file = File.exist?(file_path) ? file_path : 'config/mcp.yml.default'
    YAML.load_file(config_file)
  end

  def self.from_env
    {
      'server' => {
        'host' => ENV['MCP_HOST'] || 'localhost',
        'port' => (ENV['MCP_PORT'] || '3000').to_i,
        'log_level' => ENV['MCP_LOG_LEVEL'] || 'info'
      },
      'tools' => {
        'cache_enabled' => ENV['MCP_CACHE_ENABLED'] != 'false',
        'cache_ttl' => (ENV['MCP_CACHE_TTL'] || '3600').to_i
      }
    }
  end
end

# 使用配置
config = if File.exist?('config/mcp.yml')
            ServerConfig.load
          else
            ServerConfig.from_env
          end

server = MCP::Server.new(
  name: config['server']['name'] || 'my_server',
  logger: create_logger(config['server']['log_level'])
)
```

### 3. 健康检查

```ruby
class HealthCheck < MCP::Tool
  tool_name 'health_check'
  description '检查服务器健康状态'

  def self.call(server_context:)
    start_time = Time.now

    # 执行健康检查
    checks = {
      database: check_database,
      memory: check_memory,
      disk_space: check_disk_space
    }

    end_time = Time.now
    duration = ((end_time - start_time) * 1000).round(2)

    all_healthy = checks.values.all? { |check| check[:status] == 'ok' }

    response = {
      status: all_healthy ? 'healthy' : 'unhealthy',
      timestamp: Time.now.iso8601,
      duration_ms: duration,
      checks: checks
    }

    MCP::Tool::Response.new([{
      type: 'text',
      text: "服务器状态：#{response[:status]} (#{duration}ms)"
    }], structured_content: response)
  end

  private

  def self.check_database
    # 实现数据库健康检查
    { status: 'ok', message: '数据库连接正常' }
  rescue StandardError => e
    { status: 'error', message: e.message }
  end

  def self.check_memory
    memory_usage = `ps -o pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 2 | tail -n 1`
    { status: 'ok', usage: memory_usage.strip }
  rescue StandardError => e
    { status: 'error', message: e.message }
  end

  def self.check_disk_space
    disk_usage = `df -h / | tail -n 1`
    { status: 'ok', usage: disk_usage.strip }
  rescue StandardError => e
    { status: 'error', message: e.message }
  end
end
```

## 总结

使用 Ruby 构建 MCP 服务器提供了：
- 简洁优雅的语法
- 丰富的 gem 生态系统
- 灵活的元编程能力
- 强大的测试框架
- 易于部署和维护

遵循这些最佳实践将帮助您构建可靠、高效的 Ruby MCP 服务器。