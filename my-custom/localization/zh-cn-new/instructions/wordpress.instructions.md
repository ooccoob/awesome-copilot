---
applyTo: 'wp-content/plugins/**,wp-content/themes/**,**/*.php,**/*.inc,**/*.js,**/*.jsx,**/*.ts,**/*.tsx,**/*.css,**/*.scss,**/*.json'
description: 'WordPress 插件和主题的编码、安全和测试规则'
---

# WordPress 开发 — Copilot 指令

**目标：**生成安全、高性能、可测试且符合官方 WordPress 实践的 WordPress 代码。优先使用钩子、小型函数、依赖注入（在合理的地方）和清晰的关注点分离。

## 1) 核心原则
- 永不修改 WordPress 核心。通过**操作**和**过滤器**扩展。
- 对于插件，总是在入口 PHP 文件中包含标头并防止直接执行。
- 使用唯一前缀或 PHP 命名空间避免全局冲突。
- 排队资源；永远不要在 PHP 模板中内联原始 `<script>`/`<style>`。
- 使用户面向的字符串可翻译并加载正确的文本域。

### 最小插件标头和防护
```php
<?php
defined('ABSPATH') || exit;
/**
 * Plugin Name: Awesome Feature
 * Description: 示例插件脚手架。
 * Version: 0.1.0
 * Author: Example
 * License: GPL-2.0-or-later
 * Text Domain: awesome-feature
 * Domain Path: /languages
 */
```

## 2) 编码标准（PHP、JS、CSS、HTML）
- 遵循 **WordPress 编码标准（WPCS）** 并为公共 API 编写 DocBlocks。
- PHP：在适当的地方优先使用严格比较（`===`、`!==`）。保持数组语法和间距与 WPCS 一致。
- JS：匹配 WordPress JS 风格；对于块/编辑器代码优先使用 `@wordpress/*` 包。
- CSS：在有帮助时使用类似 BEM 的类命名；避免过于具体的选择器。
- PHP 7.4+ 兼容模式，除非项目指定更高版本。避免使用目标 WP/PHP 版本不支持的功能。

### 代码检查设置建议
```xml
<!-- phpcs.xml -->
<?xml version="1.0"?>
<ruleset name="Project WPCS">
  <description>此项目的 WordPress 编码标准。</description>
  <file>./</file>
  <exclude-pattern>vendor/*</exclude-pattern>
  <exclude-pattern>node_modules/*</exclude-pattern>
  <rule ref="WordPress"/>
  <rule ref="WordPress-Docs"/>
  <rule ref="WordPress-Extra"/>
  <rule ref="PHPCompatibility"/>
  <config name="testVersion" value="7.4-"/>
</ruleset>
```

```json
// composer.json（片段）
{
  "require-dev": {
    "dealerdirect/phpcodesniffer-composer-installer": "^1.0",
    "wp-coding-standards/wpcs": "^3.0",
    "phpcompatibility/php-compatibility": "^9.0"
  },
  "scripts": {
    "lint:php": "phpcs -p",
    "fix:php": "phpcbf -p"
  }
}
```

```json
// package.json（片段）
{
  "devDependencies": {
    "@wordpress/eslint-plugin": "^x.y.z"
  },
  "scripts": {
    "lint:js": "eslint ."
  }
}
```

## 3) 安全性和数据处理
- **输出时转义，输入时清理。**
  - 转义：`esc_html()`、`esc_attr()`、`esc_url()`、`wp_kses_post()`。
  - 清理：`sanitize_text_field()`、`sanitize_email()`、`sanitize_key()`、`absint()`、`intval()`。
- **功能权限和非ces**用于表单、AJAX、REST：
  - 使用 `wp_nonce_field()` 添加非ces并通过 `check_admin_referer()` / `wp_verify_nonce()` 验证。
  - 使用 `current_user_can( 'manage_options' /* 或特定功能权限 */ )` 限制修改。
- **数据库：**始终使用带有占位符的 `$wpdb->prepare()`；永不连接不受信任的输入。
- **上传：**验证 MIME/类型并使用 `wp_handle_upload()`/`media_handle_upload()`。

## 4) 国际化（i18n）
- 使用您的文本域将用户可见的字符串包装在翻译函数中：
  - `__( 'Text', 'awesome-feature' )`、`_x()`、`esc_html__()`。
- 使用 `load_plugin_textdomain()` 或 `load_theme_textdomain()` 加载翻译。
- 在 `/languages` 中保留 `.pot` 文件并确保一致的域使用。

## 5) 性能
- 将重型逻辑推迟到特定钩子；除非必要，避免在 `init`/`wp_loaded` 上进行昂贵的工作。
- 对昂贵的查询使用瞬态或对象缓存；计划失效。
- 仅排队您需要的内容并有条件地（前端 vs 管理员；特定屏幕/路由）。
- 优先使用分页/参数化查询而不是无界循环。

## 6) 管理员 UI 和设置
- 对选项页面使用**设置 API**；为每个设置提供 `sanitize_callback`。
- 对于表格，遵循 `WP_List_Table` 模式。对于通知，使用管理员通知 API。
- 避免为复杂 UI 直接回显 HTML；优先使用带有转义的模板或小型视图助手。

## 7) REST API
- 使用 `register_rest_route()` 注册；始终设置 `permission_callback`。
- 通过 `args` 模式验证/清理请求参数。
- 返回 `WP_REST_Response` 或能干净映射到 JSON 的数组/对象。

## 8) 块和编辑器（Gutenberg）
- 使用 `block.json` + `register_block_type()`；依赖 `@wordpress/*` 包。
- 在需要时提供服务器渲染回调（动态块）。
- E2E 测试应覆盖：插入块 → 编辑 → 保存 → 前端渲染。

## 9) 资源加载
```php
add_action('wp_enqueue_scripts', function () {
  wp_enqueue_style(
    'af-frontend',
    plugins_url('assets/frontend.css', __FILE__),
    [],
    '0.1.0'
  );

  wp_enqueue_script(
    'af-frontend',
    plugins_url('assets/frontend.js', __FILE__),
    [ 'wp-i18n', 'wp-element' ],
    '0.1.0',
    true
  );
});
```
- 如果多个组件依赖相同的资源，首先使用 `wp_register_style/script` 注册。
- 对于管理员屏幕，钩入 `admin_enqueue_scripts` 并检查屏幕 ID。

## 10) 测试
### PHP 单元/集成测试
- 使用带有 `PHPUnit` 和 `WP_UnitTestCase` 的 **WordPress 测试套件**。
- 测试：清理、功能权限检查、REST 权限、数据库查询、钩子。
- 优先使用工厂（`self::factory()->post->create()` 等）设置 fixtures。

```xml
<!-- phpunit.xml.dist（最小） -->
<?xml version="1.0" encoding="UTF-8"?>
<phpunit bootstrap="tests/bootstrap.php" colors="true">
  <testsuites>
    <testsuite name="Plugin Test Suite">
      <directory suffix="Test.php">tests/</directory>
    </testsuite>
  </testsuites>
</phpunit>
```

```php
// tests/bootstrap.php（最小草图）
<?php
$_tests_dir = getenv('WP_TESTS_DIR') ?: '/tmp/wordpress-tests-lib';
require_once $_tests_dir . '/includes/functions.php';
tests_add_filter( 'muplugins_loaded', function () {
  require dirname(__DIR__) . '/awesome-feature.php';
} );
require $_tests_dir . '/includes/bootstrap.php';
```
### E2E
- 使用 Playwright（或 Puppeteer）进行编辑器/前端流程。
- 覆盖基本用户旅程和回归（块插入、设置保存、前端渲染）。

## 11) 文档和提交
- 保持 `README.md` 最新：安装、使用、功能、钩子/过滤器和测试说明。
- 使用清晰、命令式的提交消息；引用问题/工单并总结影响。

## 12) Copilot 必须确保的事项（检查清单）
- ✅ 唯一前缀/命名空间；没有意外的全局变量。
- ✅ 对任何写入操作（AJAX/REST/表单）进行非ces + 功能权限检查。
- ✅ 输入已清理；输出已转义。
- ✅ 用户可见的字符串使用正确的文本域包装在 i18n 中。
- ✅ 资源通过 API 排队（无内联脚本/样式）。
- ✅ 为新行为添加/更新测试。
- ✅ 代码通过 PHPCS（WPCS）和适用的 ESLint。
- ✅ 避免直接数据库连接；始终准备查询。