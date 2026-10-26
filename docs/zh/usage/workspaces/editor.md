---
icon: lucide/code
title: 编辑器工作区
description: 基于 Monaco 的编辑器工作区，可在 VSView 中编辑并执行 VapourSynth 脚本。
---

# 编辑器工作区

<strong>编辑器工作区</strong>在 <strong>VSView</strong> 中内嵌了基于 Monaco 的代码编辑器与集成 Python 环境。

它在视频帧预览之外，同时提供脚本编辑、语言服务器实时诊断、多标签页文件管理以及执行输出控制台。

通用工作区布局与查看器控件请参阅[工作区概览](workspace.md)。

---

## 安装

=== "pip"
    ```bash title="安装编辑器"
    pip install vsview-editor
    ```
=== "uv"
    ```bash title="添加编辑器"
    uv add vsview-editor
    ```

---

## 工作区布局

编辑器工作区由两个主要的可停靠面板组成：

1. <strong>代码编辑面板（左侧）</strong>：包含工具栏、多标签栏、Monaco 编辑器视口、输出控制台与状态栏。
2. <strong>预览堆栈面板（右侧）</strong>：显示渲染后的视频帧与播放控制。通用工作区布局与查看器控件请参阅[工作区概览](workspace.md)。

<figure markdown="span">
    ![](../../assets/workspace_editor_layout.png){ .lightboxOn }
</figure>

---

## 工具栏控件

编辑器工具栏提供脚本管理、格式化与执行相关的控件：

| 图标                      | 控件                  | 默认快捷键       | 操作                                                                    |
| :------------------------ | :-------------------- | :--------------- | :---------------------------------------------------------------------- |
| :lucide-file-plus:        | <strong>New Script</strong>        | ++ctrl+n++       | 打开一个新的未命名脚本标签页（`untitled_<id>.py`）。                    |
| :lucide-file-down:        | <strong>Open Script</strong>       | ++ctrl+o++       | 显示文件选择器，打开已有脚本。                                          |
| :lucide-save:             | <strong>Save Script</strong>       | ++ctrl+s++       | 将当前标签页的缓冲区保存到磁盘。                                        |
| :lucide-file-up:          | <strong>Save Script As...</strong> | ++ctrl+shift+s++ | 显示文件选择器，将当前缓冲区另存到新路径。                              |
| :lucide-code:             | <strong>Format Code</strong>       | ++shift+alt+f++  | 使用 Ruff 格式化当前标签页的代码。                                       |
| :lucide-text-align-start: | <strong>Toggle Word Wrap</strong>  | ++alt+z++        | 切换编辑器中的自动换行。                                                |
| :lucide-square-terminal:  | <strong>Toggle Console</strong>    | ++ctrl+grave++   | 显示或隐藏集成输出控制台。                                              |
| :lucide-play:             | <strong>Run Script</strong>        | ++f5++           | 重新加载并在预览引擎中执行指定的主脚本。                                 |

---

## 界面组件

### 多标签页系统

标签栏用于管理已打开的脚本缓冲区。

执行目标由标签页上的 `MAIN` 徽标标识。无论当前显示哪个标签页，点击 <strong>Run Script</strong>（++f5++）都会执行 `MAIN` 脚本。

右键点击任意标签页并选择 <strong>Set as Main Script</strong>，即可将其指定为执行目标。

### Monaco 编辑器视口

代码视口由 [Monaco Editor](https://github.com/microsoft/monaco-editor) 驱动，这与 VS Code 使用的是同一个代码编辑器。

- <strong>自动补全与 IntelliSense</strong>：按 ++ctrl+space++ 触发代码建议。
- <strong>悬停与诊断</strong>：将鼠标悬停在符号上会显示文档字符串与类型签名。语法与类型错误会在行内以下划线标出。
- <strong>速览定义</strong>：按 ++ctrl+left-button++ 速览定义。
- <strong>配色主题</strong>：使用内置的 Light、Dark、High Contrast、Visual Studio 与 GitHub 配色主题自定义编辑器外观。

### 输出控制台

集成的 xterm.js 终端面板用于显示执行日志。

### 状态栏

编辑器停靠面板左下角的状态栏显示当前光标所在的行与列（`Ln X, Col Y`）。

---

## 语言服务器（Basedpyright）

该工作区会在后台运行 [Basedpyright Language Server](https://github.com/detachhead/basedpyright) 的嵌入实例。

工作区启动时会自动生成 VapourSynth 存根（stubs）。
你也可以按 ++f1++ 或 ++ctrl+shift+p++ 打开 Monaco 的 <strong>Show All Commands</strong> 面板，
选择 “VapourSynth: Generate Stubs” 强制重新生成。

与其他插件一样，语言服务器可以通过 <strong>Settings</strong> 菜单进行配置。

---

## 配置项

编辑器工作区的设置可在 VSView 设置的 `Plugin - Editor` 插件分区中配置。
