## What/When/Why/How

- What: CMake + vcpkg(manifest) 项目规范：跨平台(MSVC/Clang/GCC)、Presets 配置、策略提示、路径与样例。
- When: 配置/构建/依赖管理、示例给出、OpenCV 文件访问时。
- Why: 可移植与可复现；避免错误安装指令；提高可读性与维护性。
- How: 使用 vcpkg manifest；通过 CMakePresets.json 设缓存变量；提供影响变量的 CMake Policy 背景；文件访问用绝对路径。

## Key Points

- vcpkg: Manifest 模式；不要建议 vcpkg install <lib> 直接命令。
- Presets: 优先用 CMakePresets.json 设定 cache/options。
- Policies: 给出相关 CMake Policies 影响说明。
- Cross-Compiler: MSVC/Clang/GCC 兼容目标。
- I/O 示例: OpenCV 读文件统一绝对路径，如 C:/project/file.mp4。

## Compact Map

- vcpkg(manifest) → 可复现
- Presets → 集中配置
- Policies → 变量/行为影响
- Cross-Platform → MSVC/Clang/GCC
- Paths → 绝对路径示例

## Example Questions (10+)

1) Manifest 模式下如何新增依赖并锁定版本？
2) CMakePresets 如何切分 Debug/Release 配置？
3) 哪些 CMake Policies 会影响变量展开或查找？
4) MSVC 与 Clang/GCC 的编译选项如何统一？
5) OpenCV 样例中为何必须绝对路径？
6) vcpkg triplet 的选择策略？
7) 跨平台路径/分隔符如何在 CMake 中处理？
8) 外部项目/工具链文件与 Presets 的配合？
9) CI 环境如何复用 Presets？
10) 生成器差异(Ninja/MSBuild)对缓存变量的影响？

---
Source: d:\mycode\awesome-copilot\instructions\cmake-vcpkg.instructions.md | Generated: 2025-10-17
