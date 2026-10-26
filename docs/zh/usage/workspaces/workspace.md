---
icon: lucide/file-stack
---

# 工作区

<strong>VSView</strong> 目前提供三种内置工作区类型，以及一种插件工作区类型：

- [<strong>脚本工作区</strong>](script.md)：用于 VapourSynth 脚本开发与预览的主要环境。
- [<strong>文件工作区</strong>](file.md)：无需脚本，直接预览媒体文件。
- [<strong>快速脚本</strong>](quick-script.md)：借助内置代码编辑器进行一次性测试与实验的工作区。
- [<strong>编辑器工作区</strong>](editor.md)：借助内置代码编辑器与 Python 环境进行 VapourSynth 脚本开发的工作区。

这些工作区共享同一套核心界面。下文中除特别说明外，描述的行为适用于所有工作区。

## 概览

将脚本或文件载入工作区后，界面分为以下几个区域：

<figure markdown="span">
    ![](../../assets/workspace_overview.png){ .lightboxOn }
</figure>

1. [<strong>工作区标签页</strong>](#1-workspace-tabs)：当前载入的脚本或文件所提供的输出标签页。
2. [<strong>帧查看器</strong>](#2-frame-viewer)：显示当前输出的当前帧。
3. [<strong>播放控制</strong>](#3-playback-controls)：视频与音频的播放操作控件。
4. [<strong>时间轴</strong>](#4-timeline)：当前输出的帧/时间导航。
5. [<strong>工具停靠面板</strong>](#5-tool-docks)：以可停靠窗口形式呈现的插件工具。
6. [<strong>工具面板</strong>](#6-tool-panels)：以侧边标签面板形式呈现的插件工具。
7. [<strong>状态栏</strong>](#7-status-bar)：工作区状态、媒体信息与运行时消息。

## 1. 工作区标签页（Workspace Tabs）
工作区标签页对应当前载入源提供的每个输出。

- 在<strong>脚本工作区</strong>与<strong>快速脚本</strong>中，可以暴露多个输出并通过标签页切换。
- 在<strong>文件工作区</strong>中，只有一个输出标签页。
- 切换标签页时，帧查看器、时间轴以及相关工具都会同步切换到该输出。

此外，标签栏右上角有一组按钮，用于控制跨标签页行为与面板可见性：
<figure markdown="span">
    ![](../../assets/workspace_tab_buttons.png){ loading=lazy }
</figure>
- <strong>Toggle Plugin Tool Docks</strong>：显示或隐藏插件工具使用的侧边工具停靠面板区域。
- <strong>Sync playhead</strong>：在四种跨标签页时间轴同步模式间循环：
    - <strong>Adaptive link</strong>：跟随当前时间轴的显示模式（时间或帧）。
    - <strong>Link by time</strong>：将所有标签页定位到相同时间戳。
    - <strong>Link by frame</strong>：将所有标签页定位到相同帧号。
    - <strong>Unlink</strong>：关闭跨标签页播放头同步。
    工具提示会实时更新，显示当前生效的模式。
- <strong>Sync zoom</strong>：联动各输出的缩放级别。在任一标签页缩放，所有标签页都会应用相同缩放。
- <strong>Sync scroll</strong>：联动各输出的平移/滚动位置。在任一标签页平移，所有标签页都会更新查看区域。
- <strong>Autofit all views</strong>：启用后自动将每个输出适配到帧查看器视口。
- <strong>Toggle Plugin Tool Panel</strong>：显示或隐藏插件工具使用的侧边工具面板区域。


## 2. 帧查看器（Frame Viewer）
帧查看器是主要的预览区域。
它显示当前输出标签页的当前帧。
任何播放操作（播放、拖动、单帧前进/后退）都会实时刷新该视图。

在显示的帧上点击右键，会打开以下上下文菜单：

<figure markdown="span">
    ![](../../assets/frame_viewer_context_menu.png){ loading=lazy }
</figure>

- <strong>Zoom</strong>：放大与缩小。也可通过 <strong>++ctrl++</strong> + <strong>鼠标滚轮</strong> 操作。
- <strong>Autofit</strong>：将当前输出适配到帧查看器视口。
- <strong>Toggle SAR</strong>：切换当前输出的采样宽高比（SAR）校正显示（仅当 SAR 不为 1:1 时可用）。
- <strong>Save Current Image</strong>：打开保存对话框，将当前显示的帧写入磁盘。
- <strong>Copy Image to Clipboard</strong>：将当前显示的帧复制到系统剪贴板。

## 3. 播放控制（Playback Controls）
播放控制区集合了播放按钮、直接跳转输入框与音频控制。

<figure markdown="span">
    ![](../../assets/playback_controls.png){ loading=lazy }
</figure>

- <strong>Seek N Backward / Forward</strong>：按配置的跳转步长前后跳转。
- <strong>Seek 1 Backward / Forward</strong>：精确移动一帧。
- <strong>Play / Pause</strong>：开始或停止播放。播放期间，跳转按钮与时间/帧输入框会被禁用，但 Play / Pause 仍可用于停止播放。
- <strong>时间输入框</strong>：直接跳转到指定时间戳。
- <strong>帧输入框</strong>：直接跳转到指定帧号。
- <strong>Mute + Volume</strong>：切换静音并调整播放音量（仅在存在音频输出时可用）。

在播放控制区域点击右键可打开进阶设置：

<figure markdown="span">
    ![](../../assets/playback_controls_context_menu.png){ loading=lazy }
</figure>

- <strong>Seek Step</strong>：设置 N 帧的跳转步长，并提供 <strong>Reset to Global</strong> 以恢复全局设置中的默认值。
- <strong>Speed Limit</strong>：设置 0.25x 至 8.00x 的播放速度，步进为 0.25x，并提供恢复 1.00x 的重置按钮。
- <strong>Uncap FPS</strong>：取消速度上限。
- <strong>Zone Playback</strong>：按时间/帧定义区间，然后播放该区间，可选 <strong>Loop</strong> 以及可配置的 <strong>Play Step</strong>（允许负值！）。
- <strong>Audio Output / Delay</strong>：选择音频输出并调整同步延迟（-10000 ms 至 +10000 ms），并提供 <strong>Reset to Global</strong> 以恢复全局设置中的默认值。

## 4. 时间轴（Timeline）
时间轴为当前输出提供精确导航与可视化参考标记。

- <strong>左键按住拖动</strong>时间轴条即可交互式跳转。
- <strong>悬停预览</strong>：鼠标移过时间轴时，会以帧/时间形式显示当前悬停位置；可在时间轴设置中启用悬停放大。
- <strong>帧/时间显示模式</strong>：刻度与标签可以按帧号或时间戳显示。
- <strong>自定义标记/刻度（notches）</strong>：插件与工具可以向时间轴添加标记（例如书签、类似关键帧的标记），并支持可选区间。

在时间轴上点击右键可切换显示模式：

- <strong>Frame</strong>：显示基于帧的刻度标签。
- <strong>Time</strong>：显示基于时间戳的刻度标签。


## 5. 工具停靠面板（Tool Docks）
工具停靠面板是附着在工作区布局中的可移动插件窗口。
你可以拖动标题栏重新定位、将其停靠到边缘、与其他停靠面板堆叠，或将其浮动为独立窗口。

也可以使用[工作区标签页](#1-workspace-tabs)中的 <strong>Toggle Plugin Tool Docks</strong> 按钮切换其可见性。

<figure markdown="span">
    <video controls width="100%" style="border-radius: 8px;">
        <source src="../../assets/tool_dock_showoff.mp4" type="video/mp4">
        你的浏览器不支持 video 标签。
    </video>
</figure>

更多信息参见[插件](../../plugins/overview.md)。

## 6. 工具面板（Tool Panels）
工具面板以位于工作区右侧的紧凑标签面板形式，提供相同的插件工具。

该面板属于一个<strong>水平分隔器</strong>，因此你可以拖动主内容区与面板之间的手柄来调整其大小。

也可以将其拖到边缘，或使用[工作区标签页](#1-workspace-tabs)中的 <strong>Toggle Plugin Tool Panel</strong> 按钮来隐藏面板。

<figure markdown="span">
    <video controls width="100%" style="border-radius: 8px;">
        <source src="../../assets/tool_panel_showoff.mp4" type="video/mp4">
        你的浏览器不支持 video 标签。
    </video>
</figure>

更多信息参见[插件](../../plugins/overview.md)。

## 7. 状态栏（Status Bar）
状态栏实时显示当前工作区/输出的信息

- 工作区及其关联插件的运行时/日志消息。
- 所选输出的上下文媒体信息。
