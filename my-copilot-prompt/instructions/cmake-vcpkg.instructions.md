---
description: 'C++ project configuration and package management'
applyTo: '**/*.cmake, **/CMakeLists.txt, **/*.cpp, **/*.h, **/*.hpp'
---

本项目在清单模式下使用vcpkg。在提供 vcpkg 建议时请记住这一点。不要提供诸如 vcpkg 安装库之类的建议，因为它们不会按预期工作。
如果可能的话，最好通过 CMakePresets.json 设置缓存变量和其他类型的内容。
提供有关可能影响建议或提到的 CMake 变量的任何 CMake 策略的信息。
该项目需要跨平台，并且跨 MSVC、Clang 和 GCC 编译器。
当提供使用文件系统读取文件的 OpenCV 示例时，请始终使用绝对文件路径而不是文件名或相对文件路径。例如，使用 `video.open("C:/project/file.mp4")`，而不是 `video.open("file.mp4")`。
