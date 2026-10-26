---
icon: lucide/home
---

# VSView

<div align="center" markdown>

![vsview Logo](assets/loading.png){ width="300" }

<strong>下一代 VapourSynth 预览器</strong>

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view)
[![Discord](https://img.shields.io/discord/856381934052704266?label=Discord&logo=discord&logoColor=7F71FF)](https://discord.gg/XTpc6Fa9eB)

</div>

---

!!! note "非官方翻译"

    本页是社区维护的简体中文翻译，可能滞后于[英文原文](https://jaded-encoding-thaumaturgy.github.io/vs-view/)。

    为便于对照，界面元素名、命令、配置项与 API 名称均保留英文原文。详见[关于本翻译](translation.md)。

---

## 为什么选择 VSView

<strong>VSView</strong> 是为 [VapourSynth](https://www.vapoursynth.com/) 打造的现代化、可扩展预览器。
在同一界面中预览、检查并对比脚本、视频或图片，无需来回切换工具。

它旨在成为 [VSPreview](https://github.com/Jaded-Encoding-Thaumaturgy/vs-preview) 的现代替代品，
注重更整洁、更易维护的代码，并通过清晰的 API 提供直接的插件集成，
使官方与社区扩展更易于开发、维护和采用。

## 快速开始

直接在终端中安装并启动：

=== "pip"
    ```bash title="安装并运行"
    pip install vsview
    vsview
    ```

    ```bash title="安装并启用推荐插件"
    pip install vsview[recommended]
    ```

    ```bash title="安装全部插件（完整版）"
    pip install vsview[full]
    ```

    ```bash title="直接打开文件："
    vsview script.vpy video.mkv
    ```
=== "uv"
    ```bash title="安装并运行"
    uv add vsview
    vsview
    ```

    ```bash title="安装并启用推荐插件"
    uv add vsview --extra recommended
    ```

    ```bash title="安装全部插件（完整版）"
    uv add vsview --extra full
    ```

    ```bash title="直接打开文件："
    uv run vsview script.vpy video.mkv
    ```

也可以从 [GitHub Releases](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/releases) 下载预编译的二进制包。

## 文档目录

- [安装](installation.md)：系统要求、`pip`/`uv` 安装方式与开发环境配置。
- [贡献指南](contributing.md)：开发环境搭建与编辑器推荐配置。
- [使用](usage/overview.md)：命令行用法、文件类型识别、工作区与快捷键。
- [插件](plugins/overview.md)：内置工具、官方插件与插件开发。
- [用户 API](api/user.md)：`set_output` 及脚本侧 API 用法。
- [开发者 API](api/developer/index.md)：面向插件的类、钩子与工具函数。

## 社区与支持

加入 [JET Discord](https://discord.gg/XTpc6Fa9eB) 获取支持、提出功能请求并参与讨论。

