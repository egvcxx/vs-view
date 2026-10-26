---
icon: lucide/terminal
title: 插件开发
---

# 插件开发

本指南介绍如何为 VSView 创建插件，从搭建基本结构，到接入应用的生命周期与渲染循环。

!!! tip "插件模板"
    有一个模板仓库，包含标准的项目结构与起步代码：

    [:fontawesome-brands-github: Ichunjo/vs-view-plugin-template](https://github.com/Ichunjo/vs-view-plugin-template)

## 插件架构

VSView 的插件系统基于 [pluggy](https://pluggy.readthedocs.io/)。插件通过 Python 入口点（entry points）被发现。应用定义了若干规范（钩子），插件可实现这些钩子来注入组件或响应事件。

### 入口点注册

要让插件可被发现，请在 `pyproject.toml` 的 `project.entry-points."vsview"` 分组中注册它：

```toml
[project.entry-points."vsview"]
my_plugin = "my_package.plugin:MyPluginHooks"
```

VSView 启动时会查找该入口点并加载注册的钩子。

## 创建控件插件

最常见的插件类型是控件插件，它向工作区添加自定义 UI 面板。这通过继承 `WidgetPluginBase` 实现。

### 基本结构

一个最小插件需要一个唯一标识符、一个显示名称，并且必须通过 `vsview_register_toolpanel` 和/或 `vsview_register_tooldock` 钩子注册：

```python title="plugin.py"
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from vsview.api import PluginAPI, WidgetPluginBase, hookimpl


class MyPlugin(WidgetPluginBase):
    identifier = "jet_vsview_myplugin"
    display_name = "My Plugin"

    def __init__(self, parent: QWidget, api: PluginAPI) -> None:
        super().__init__(parent, api)
        layout = QVBoxLayout(self)
        self.label = QLabel("Hello from my plugin!")
        layout.addWidget(self.label)


class MyPluginHooks:
    @hookimpl
    def vsview_register_toolpanel(self) -> type[WidgetPluginBase]:
        return MyPlugin
```

## 钩子系统

`WidgetPluginBase` 提供事件钩子系统，使插件可以响应 VSView 内的交互与状态变化。在派生类中重写相应方法即可。

以下只是 `WidgetPluginBase` 中最常用的一部分钩子。完整列表与全部钩子的详细规范，见 [API 参考](../api/developer/index.md#vsview.api.WidgetPluginBase)。

- `on_current_voutput_changed(...)`：用户切换到其他视频输出标签页时触发。
- `on_current_frame_changed(...)`：用户拖动时间轴或播放期间持续触发。
- `on_playback_started()` / `on_playback_stopped()`：视频播放开始或暂停时触发。

## 公共 API

每个 `WidgetPluginBase` 实例在初始化时都会收到一个 `PluginAPI` 对象，可通过 `self.api` 属性访问。该 API 是访问应用其余部分的入口。

通过它可以读取当前状态、操作时间轴并访问 VapourSynth 环境：

```py
class MyPlugin(WidgetPluginBase):
    # ...

    def on_current_voutput_changed(self, voutput: VideoOutputProxy, tab_index: int) -> None:
        # 超过第 2000 帧后不再执行后续逻辑
        if self.api.current_frame > 2000:
            return

        # 访问当前时间轴模式
        if self.api.timeline.mode == "frame":
            print("Viewing by frame!")
```

完整能力列表见 [API 参考](../api/developer/#vsview.api.PluginAPI) 页面。

## 设置管理

插件可以定义持久化设置，它们会自动出现在用户的设置面板中。VSView 原生集成 [Pydantic](https://docs.pydantic.dev/) 模型来定义与校验这些配置。

```python
from typing import Annotated

from jetpytools import fallback
from pydantic import BaseModel
from vsview.api import LocalSettingsModel, PluginSettings, Dropdown


class GlobalSettings(BaseModel):
    mode: Annotated[  # (1)!
        str,
        Dropdown(
            label="Mode",
            items=[("Horizontal", "h"), ("Vertical", "v")],
            tooltip="Stacking direction",
        ),
    ] = "h"
    threshold: int = 50


class LocalSettings(LocalSettingsModel):
    enabled: bool = True
    threshold: int | None = None  # (2)!


class MyPlugin(WidgetPluginBase[GlobalSettings, LocalSettings]):  # (3)!
    def setup_ui(self) -> None:
        if self.settings.global_.mode == "h":
            ...

        self.threshold = fallback(self.settings.local_.threshold, self.settings.global_.threshold)
```

1.  `#!python Annotated` 类型用于在设置面板中注册支持的控件。不同受支持的控件见[参考 API](../api/developer/#ui-settings)。
2. 通过继承 `#!python LocalSettingsModel` 并将 `threshold=None`，我们得到一个会回退到上方全局值的局部阈值。
3. 为了访问设置并把模型注册到 VSView 设置中，必须在这里把类作为泛型参数传入。

### 将设置组织为分区

设置模型（顶层模型或嵌套的 `BaseModel` 类）可以定义 `#!python __section__` 类属性，以把字段分组到不同的 UI 折叠面板中。

UI 中所有插件设置分区都会自动带上 `Plugin - <display_name>` 前缀：

- **设置了 `#!python __section__ = "Custom Section"`**：显示为 `Plugin - <display_name> - Custom Section`。
- **未设置 `#!python __section__`**：默认为 `Plugin - <display_name>`（若为嵌套模型，则继承父模型的分区）。

```python
class AdvancedSettings(BaseModel):
    __section__ = "Advanced"  # (1)!
    debug_logging: Annotated[bool, Checkbox(label="Debug Logging")] = False


class GlobalSettings(BaseModel):
    __section__ = "General"  # (2)!
    mode: Annotated[str, Dropdown(label="Mode", items=[("Horizontal", "h")])] = "h"
    advanced: AdvancedSettings = AdvancedSettings()  # (3)!
```

1. 嵌套模型的分区会渲染为 `Plugin - My Plugin - Advanced`。
2. 顶层模型的分区会渲染为 `Plugin - My Plugin - General`。
3. 嵌套模型的属性会自动继承分区逻辑。

## 键盘快捷键

插件可以向 VSView 的中央快捷键管理器注册自定义快捷键。快捷键始终可由用户配置，并支持热重载。

首先，使用 `ActionDefinition` 定义快捷键。为了可读性与类型安全，建议把它们放进 `Enum` 或 `StrEnum` 中分组：

```python
from enum import StrEnum
from typing import Self

from vsview.api import ActionDefinition


class ShortcutDefinition(StrEnum):
    definition: ActionDefinition

    REMOVE_ITEM = "remove_item", "Remove selected item", "Delete"
    TOGGLE_PLAYBACK = "toggle_playback", "Toggle Playback", "Space"

    def __new__(cls, value: str, label: str, default_key: str = "") -> Self:
        obj = str.__new__(cls, value)
        obj._value_ = value
        # 动作 ID 必须以你的插件标识符为前缀
        obj.definition = ActionDefinition(f"my_plugin.{value}", label, default_key)
        return obj
```

接下来，在 `WidgetPluginBase` 子类中声明 `shortcuts` 属性，把定义注册到设置面板。
然后使用 `self.api.register_action` 或 `self.api.register_shortcut` 将定义映射到你的动作或函数：

```python hl_lines="8 9 18 19 20 21 22 23 24 25"
from PySide6.QtWidgets import QWidget
from vsview.api import PluginAPI, WidgetPluginBase


class MyPlugin(WidgetPluginBase):
    identifier = "my_plugin"
    display_name = "My Plugin"

    # 注册快捷键定义，使其可由用户配置
    shortcuts = tuple(s.definition for s in ShortcutDefinition)

    def __init__(self, parent: QWidget, api: PluginAPI) -> None:
        super().__init__(parent, api)
        # ... setup UI ...
        self.setup_shortcuts()

    def setup_shortcuts(self) -> None:
        # 注册一个简单的函数回调
        self.api.register_shortcut(
            ShortcutDefinition.REMOVE_ITEM.definition,
            self.on_remove_item_triggered,
            self.view_widget,  # 父控件
        )

        # 注册一个已有的 QAction
        self.api.register_action(ShortcutDefinition.TOGGLE_PLAYBACK.definition, self.my_play_action)

    def on_remove_item_triggered(self) -> None: ...  # 你的逻辑
```

1. **`shortcuts` 属性**：把快捷键暴露到用户的应用设置面板中，使其可以修改默认按键。
2. **`register_shortcut`**：把 `ActionDefinition` 直接绑定到 Python 可调用对象。
3. **`register_action`**：把 `ActionDefinition` 绑定到已有的 `QAction`，并自动保持其工具提示与当前按键序列同步。

## 示例：帧计数器

把以上内容组合起来，下面是一个完整的插件：显示当前帧号，通过钩子系统自动更新，集成用户设置，并注册自定义快捷键：

```python title="plugin.py"
from enum import StrEnum
from typing import Annotated, Any, Self

from jetpytools import fallback
from pydantic import BaseModel
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from vsview.api import (
    ActionDefinition,
    Dropdown,
    LocalSettingsModel,
    PluginAPI,
    WidgetPluginBase,
    hookimpl,
    run_in_loop,
)


class GlobalSettings(BaseModel):
    font_size: int = 16
    font_weight: Annotated[
        str,
        Dropdown(
            label="Font Weight",
            items=[("Normal", "normal"), ("Bold", "bold")],
            tooltip="The weight of the font",
        ),
    ] = "bold"


class LocalSettings(LocalSettingsModel):
    font_size: int | None = None


class ShortcutDefinition(StrEnum):
    definition: ActionDefinition

    RESET_TEXT = "reset_text", "Reset Display Text", "Ctrl+Alt+R"

    def __new__(cls, value: str, label: str, default_key: str = "") -> Self:
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.definition = ActionDefinition(f"jet_vsview_framecounter.{value}", label, default_key)
        return obj


class FrameCounterPlugin(WidgetPluginBase[GlobalSettings, LocalSettings]):
    identifier = "jet_vsview_framecounter"
    display_name = "Frame Counter"

    # 注册快捷键定义，使其可由用户配置
    shortcuts = tuple(s.definition for s in ShortcutDefinition)

    def __init__(self, parent: QWidget, api: PluginAPI) -> None:
        super().__init__(parent, api)
        layout = QVBoxLayout(self)

        # 读取当前设置
        font_size = fallback(self.settings.local_.font_size, self.settings.global_.font_size)
        font_weight = self.settings.global_.font_weight

        # 初始化 UI 状态
        self.label = QLabel(f"Frame: {self.api.current_frame}", self)
        self.label.setStyleSheet(f"font-size: {font_size}px; font-weight: {font_weight};")

        layout.addWidget(self.label)

        # 设置快捷键
        self.api.register_shortcut(
            ShortcutDefinition.RESET_TEXT.definition,
            self.on_reset_text,
            self.view_widget,
        )

    def on_reset_text(self) -> None:
        self.update_label(0)

    # 接入钩子系统以响应帧变化
    def on_current_frame_changed(self, n: int) -> None:
        self.update_label(n)

    @run_in_loop  # (1)!
    def update_label(self, n: int) -> None:
        self.label.setText(f"Frame: {n}")


class FrameCounterHooks:
    @hookimpl
    def vsview_register_toolpanel(self) -> type[WidgetPluginBase[Any, Any]]:
        return FrameCounterPlugin
```

1. `@run_in_loop` 装饰器确保 `update_label` 方法在 Qt 主事件循环中调用，这是更新 UI 元素所必需的。
