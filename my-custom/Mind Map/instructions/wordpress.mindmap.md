## What

- WordPress 主题/插件开发规范：钩子扩展、安全与数据处理、i18n、性能、REST、区块、资源加载、测试与文档

## When

- 开发新插件/主题或改造现有功能时

## Why

- 与官方最佳实践对齐，提升安全性、可维护性与可测试性

## How

- 原则
  - 绝不改 WP Core；用 actions/filters 扩展；入口 PHP 有 header 与 ABSPATH guard
  - 前缀/命名空间避免全局冲突；通过 enqueue 加载资源；字符串可翻译并加载 text domain
- 代码规范
  - 遵循 WPCS；DocBlocks；PHP 严格比较；JS 用 @wordpress/*；CSS 采用 BEM；保持 PHP7.4+ 兼容
  - PHPCS/ESLint 脚手架与 composer/package 脚本
- 安全
  - 输入 sanitize、输出 escape；Nonce+capabilities 校验；$wpdb->prepare() 防注入；上传用 WP API
- i18n
  - __/_x/esc_html__ 包装；load_plugin_textdomain/load_theme_textdomain；/languages 下放 .pot
- 性能
  - 重逻辑归位特定 hook；使用 transients/object cache；按需/按屏加载资源；分页/参数化查询
- 管理端
  - Settings API + sanitize_callback；WP_List_Table；模板/助手函数输出转义
- REST
  - register_rest_route + permission_callback；args 校验；返回 WP_REST_Response
- 区块
  - block.json + register_block_type；@wordpress/*；动态块 server render；E2E 覆盖插入/编辑/保存/前端渲染
- 资源加载
  - wp_enqueue_style/script；按 admin_enqueue_scripts 分场景；可先 register 再 enqueue
- 测试
  - WP test suite + PHPUnit；覆盖 sanitize/权限/REST/DB/hooks；fixtures 用 factories
  - E2E 用 Playwright；覆盖关键用户旅程
- 文档/提交
  - README 说明安装/用法/钩子/测试；清晰提交信息，指向 issue
- 清单
  - 前缀/命名空间✔  Nonce+cap✔  输入/输出校验✔  i18n✔  资源加载✔  测试✔  PHPCS/ESLint✔  预处理查询✔

## Key Points

- “输入净化 + 输出转义 + 能力/Nonce”是三件套
- 所有资源走 enqueue；REST 必有 permission_callback

## Compact Map

- 原则: 钩子/前缀/enqueue
- 安全: sanitize/escape/nonce/caps/prepare
- i18n: domain/.pot
- 性能: 缓存/按需
- REST: 路由/权限
- 区块: block.json/动态
- 测试: PHPUnit/E2E

## Example Questions

1) 某个写操作需要哪些 Nonce 与能力校验？
2) 这段输出应使用哪个 esc_* 函数？
3) 该 REST 路由的 permission_callback 如何设计？
4) 何时适合用 transients，如何失效？
5) block.json 与 register_block_type 如何配合？
6) 资源应在前台还是后台加载，挂在哪个 hook？
7) 如何配置 PHPCS 与 PHPCompatibility？
8) 表单/上传如何做 sanitize 与校验？
9) 多语言文本的 text domain 如何管理？
10) E2E 用例应覆盖哪些编辑器/前端场景？
11) $wpdb 查询的 prepare 占位符如何编写？

Source: d:\mycode\awesome-copilot\instructions\wordpress.instructions.md | Generated: 2025-10-17
