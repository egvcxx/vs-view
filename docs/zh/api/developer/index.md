---
icon: lucide/code
---

# 开发者 API 概览

本节介绍用于开发插件与扩展 VSView 的 API。

为方便使用，其中大部分符号都通过顶层 `vsview.api` 模块重新导出。

!!! note "以下内容为英文原文"

    本页 API 由源码 docstring 自动生成，故保持英文，以便与代码和参数名对照。

---

[:lucide-cpu:{ .middle } <strong>核心与代理（Core & Proxies）</strong>](#core-proxies)

[:lucide-layout-template:{ .middle } <strong>自定义控件</strong>](#custom-widgets)

[:lucide-settings:{ .middle } <strong>UI 设置</strong>](#ui-settings)

[:lucide-play-circle:{ .middle } <strong>时间轴与播放</strong>](#timeline-playback)

[:lucide-wrench:{ .middle } <strong>工具函数</strong>](#utilities)

---

## 核心与代理（Core & Proxies）
::: vsview.api
    options:
        heading_level: 3
        members:
           - PluginAPI
           - VideoOutputProxy
           - AudioOutputProxy
           - GraphicsViewProxy
           - TimelineProxy
           - PlaybackProxy
           - PluginSettings
           - WidgetPluginBase
           - NodeProcessor
           - ActionDefinition
           - LocalSettingsModel
           - WorkspaceBlocker


## 自定义控件（Custom Widgets）
::: vsview.api
    options:
        heading_level: 3
        members:
           - Accordion
           - AnimatedToggle
           - SegmentedControl
           - FrameEdit
           - TimeEdit
           - BaseGraphicsView
           - CustomSpinBox
           - PluginGraphicsView
           - ListEditWidget
           - LoginCredentialsInput
           - ColorPickerInput
           - FilePickerWidget
           - PathListEditWidget

## UI 设置（Settings）
::: vsview.api
    options:
        heading_level: 3
        members:
           - WidgetMetadata 
           - Checkbox
           - Dropdown
           - Spin
           - DoubleSpin
           - PlainTextEdit
           - ListEdit
           - WidgetTimeEdit
           - Login
           - SecretLineEdit
           - ColorPicker
           - FilePicker
           - PathListEdit


## 时间轴与播放（Timeline & Playback）
::: vsview.api
    options:
        heading_level: 3
        members:
           - Frame
           - Time


## 工具函数（Utilities）
::: vsview.api
    options:
        heading_level: 3
        members:
           - hookimpl
           - Packer 
           - run_in_background
           - run_in_loop
           - IconName
           - IconReloadMixin
           - load_icon
           - ObjectType
           - QObjectCounter
           - QObjectSet
           - cache_clip
           - path_to_hash
           - get_console_level
