---
description: 'C++项目配置和包管理'
applyTo: '**/*.cmake, **/CMakeLists.txt, **/*.cpp, **/*.h, **/*.hpp'
---

此项目在清单模式下使用vcpkg。在提供vcpkg建议时请记住这一点。不要提供像vcpkg install library这样的建议，因为它们不会按预期工作。
如果可能，优先通过CMakePresets.json设置缓存变量和其他类型的东西。
提供有关可能影响建议或提及的CMake变量的任何CMake策略的信息。
此项目需要跨平台和跨编译器，支持MSVC、Clang和GCC。
当提供使用文件系统读取文件的OpenCV示例时，请始终使用绝对文件路径而不是文件名或相对文件路径。例如，使用`video.open("C:/project/file.mp4")`，而不是`video.open("file.mp4")`。