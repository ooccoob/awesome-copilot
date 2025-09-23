---
description: "C++ 项目配置与包管理"
applyTo: "**/*.cmake, **/CMakeLists.txt, **/*.cpp, **/*.h, **/*.hpp"
---

本项目采用 vcpkg manifest 模式。请在给出 vcpkg 相关建议时务必注意，不要建议使用 `vcpkg install library` 这类命令，否则无法达到预期效果。

如有可能，建议通过 CMakePresets.json 设置缓存变量及相关配置。

如涉及 CMake 变量建议，请说明可能影响这些变量的 CMake Policies。

本项目需支持 MSVC、Clang、GCC 等多平台多编译器。

如提供 OpenCV 文件读写示例，务必使用绝对路径（如 `video.open("C:/project/file.mp4")`），不要用文件名或相对路径（如 `video.open("file.mp4")`）。

---

**免责声明**：本文档由 [GitHub Copilot](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot) 本地化。如有错误或不当之处，欢迎通过 [issues](../../issues) 反馈。
