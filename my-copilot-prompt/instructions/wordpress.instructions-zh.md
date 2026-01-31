---
applyTo: 'wp-content/plugins/**,wp-content/themes/**,**/*.php,**/*.inc,**/*.js,**/*.jsx,**/*.ts,**/*.tsx,**/*.css,**/*.scss,**/*.json'
描述：“WordPress 插件和主题的编码、安全性和测试规则”
---

# WordPress 开发 — Copilot 说明

**目标：** 生成安全、高性能、可测试且符合官方 WordPress 实践的 WordPress 代码。更喜欢钩子、小函数、依赖注入（如果合理）和清晰的关注点分离。

## 1）核心原则
- 切勿修改 WordPress 核心。通过**操作**和**过滤器**进行扩展。
- 对于插件，始终在入口 PHP 文件中包含标头并保护直接执行。
- 使用唯一的前缀或 PHP 命名空间来避免全局冲突。
- 排队资产；切勿在 PHP 模板中内联原始 `<script>`/`<style>` 。
- 使面向用户的字符串可翻译并加载正确的文本域。

### 最小插件头和防护
```php
<?php
defined('ABSPATH') || exit;
/**
 * Plugin Name: Awesome Feature
 * Description: Example plugin scaffold.
 * Version: 0.1.0
 * Author: Example
 * License: GPL-2.0-or-later
 * Text Domain: awesome-feature
 * Domain Path: /languages
 */
```

## 2) 编码标准（PHP、JS、CSS、HTML）
- 遵循 **WordPress 编码标准 (WPCS)** 并为公共 API 编写 DocBlock。
- PHP：在适当的情况下更喜欢严格比较（`===`，`!==`）。与 WPCS 中的数组语法和间距保持一致。
- JS：匹配WordPress JS风格；对于块/编辑器代码更喜欢 `@wordpress/*` 包。
- CSS：有用时使用类似 BEM 的类命名；避免过于具体的选择器。
- PHP 7.4+ 兼容模式，除非项目指定更高版本。避免使用目标 WP/PHP 版本不支持的功能。

### Linting 设置建议
```xml
<!-- phpcs.xml -->
<?xml version="1.0"?>
<ruleset name="Project WPCS">
  <description>WordPress Coding Standards for this project.</description>
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
// composer.json (snippet)
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
// package.json (snippet)
{
  "devDependencies": {
    "@wordpress/eslint-plugin": "^x.y.z"
  },
  "scripts": {
    "lint:js": "eslint ."
  }
}
```

## 3) 安全和数据处理
- **输出转义，输入清理。**
  - 转义：`esc_html()`、`esc_attr()`、`esc_url()`、`wp_kses_post()`。
  - 清理：`sanitize_text_field()`、`sanitize_email()`、`sanitize_key()`、`absint()`、`intval()`。
- **表单、AJAX、REST 的功能和随机数**：
  - 使用 `wp_nonce_field()` 添加随机数并通过 `check_admin_referer()` / `wp_verify_nonce()` 进行验证。
  - 使用 `current_user_can( 'manage_options' /* or specific cap */ )` 限制突变。
- **数据库：**始终使用 `$wpdb->prepare()` 和占位符；切勿连接不受信任的输入。
- **上传：** 验证 MIME/类型并使用 `wp_handle_upload()`/`media_handle_upload()`。

## 4）国际化（i18n）
- 使用文本域用翻译函数包装用户可见的字符串：
  - __代码0__、__代码1__、__代码2__。
- 使用 `load_plugin_textdomain()` 或 `load_theme_textdomain()` 加载翻译。
- 在 `/languages` 中保留 `.pot` 并确保一致的域使用。

## 5）性能
- 将繁重的逻辑推迟到特定的钩子上；除非必要，否则避免在 `init`/`wp_loaded` 上进行昂贵的工作。
- 对昂贵的查询使用瞬态或对象缓存；计划失效。
- 仅将您需要的内容和有条件地排队（前端与管理；特定屏幕/路线）。
- 优先选择分页/参数化查询而不是无界循环。

## 6) 管理用户界面和设置
- 对选项页面使用 **Settings API**；为每个设置提供 `sanitize_callback`。
- 对于表，请遵循 `WP_List_Table` 模式。对于通知，请使用管理通知 API。
- 避免复杂 UI 的直接 HTML 回显；更喜欢带有转义的模板或小视图助手。

## 7) 休息API
- 使用 `register_rest_route()` 注册；始终设置 `permission_callback`。
- 通过 `args` 模式验证/清理请求参数。
- 返回 `WP_REST_Response` 或干净映射到 JSON 的数组/对象。

## 8）块和编辑器（古腾堡）
- 使用 `block.json` + `register_block_type()`；依赖 `@wordpress/*` 包。
- 需要时提供服务器渲染回调（动态块）。
- E2E测试应涵盖：插入块→编辑→保存→前端渲染。

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
- 如果多个组件依赖于相同的资产，请先使用 `wp_register_style/script` 进行注册。
- 对于管理屏幕，连接到 `admin_enqueue_scripts` 并检查屏幕 ID。

## 10) 测试
### PHP 单元/集成
- 将 **WordPress 测试套件** 与 `PHPUnit` 和 `WP_UnitTestCase` 结合使用。
- 测试：清理、功能检查、REST 权限、数据库查询、挂钩。
- 优先选择工厂（`self::factory()->post->create()` 等）来设置固定装置。

```xml
<!-- phpunit.xml.dist (minimal) -->
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
// tests/bootstrap.php (minimal sketch)
<?php
$_tests_dir = getenv('WP_TESTS_DIR') ?: '/tmp/wordpress-tests-lib';
require_once $_tests_dir . '/includes/functions.php';
tests_add_filter( 'muplugins_loaded', function () {
  require dirname(__DIR__) . '/awesome-feature.php';
} );
require $_tests_dir . '/includes/bootstrap.php';
```
### 端到端
- 使用 Playwright（或 Puppeteer）进行编辑器/前端流程。
- 涵盖基本的用户旅程和回归（块插入、设置保存、前端渲染）。

## 11) 文档和提交
- 使 `README.md` 保持最新：安装、使用、功能、挂钩/过滤器和测试说明。
- 使用清晰、命令式的提交消息；参考问题/票证并总结影响。

## 12) 副驾驶必须确保什么（清单）
- ✅ 独特的前缀/命名空间；没有意外的全局变量。  
- ✅ Nonce + 任何写入操作（AJAX/REST/forms）的能力检查。  
- ✅ 输入已净化；输出逃逸。  
- ✅ 用户可见的字符串用正确的文本域封装在 i18n 中。  
- ✅ 通过 API 排队的资产（无内联脚本/样式）。  
- ✅ 添加/更新新行为的测试。  
- ✅ 代码通过 PHPCS (WPCS) 和 ESLint（如果适用）。  
- ✅ 避免直接DB串联；始终准备查询。
