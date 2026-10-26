---
icon: lucide/book-open
---

# 使用概览

本页概述 <strong>VSView</strong> 的界面及其核心组成部分。

## 启动 VSView

### 命令行界面

<strong>VSView</strong> 会根据文件扩展名自动识别输入类型。

| 扩展名                               | 类型            |
| ------------------------------------ | --------------- |
| `.py`、`.vpy`                        | VapourSynth 脚本 |
| `.mkv`、`.mp4`、`.png`、`.jpg` 等    | 视频与图片文件   |

```bash
# 打开 VSView
vsview

# 打开指定文件
vsview script.vpy video.mkv
```

!!! tip "进阶命令行选项与环境变量"

    VSView 还支持用于设置管理与环境作用域的额外参数。
    完整参见[配置与命令行](configuration.md)。

### 在脚本中注册输出

在 VapourSynth 脚本中使用 `set_output()` 注册片段（clip）：

```python title="example.vpy"
import vapoursynth as vs
from vsview import set_output

core = vs.core
clip = core.bs.VideoSource("video.mkv")

set_output(clip, "Source")
set_output(clip.std.Invert(), "Inverted")
```


## 界面速览

<strong>VSView</strong> 采用工作区（workspace）布局来组织脚本与文件，并提供集成工具的入口。

<figure markdown="span">
    ![](../assets/app_overview.png){ .lightboxOn }
</figure>

---

## 1. 侧边栏

左侧边栏是主导航区域。每个已打开的工作区由一个图标表示。
如果内容区域需要更多空间，可以通过 <strong>View</strong> 菜单显示或隐藏侧边栏。

### 导航与管理
- <strong>切换工作区</strong>：点击图标即可将主内容区域切换到对应工作区。
- <strong>排序</strong>：可以按住图标拖动，上下调整顺序。
- <strong>右键菜单</strong>：右键点击任意侧边栏图标，可访问该工作区专属操作：
    - <strong>Reload</strong>：重新加载当前工作区。

        !!! info "热重载"
            重新加载时，只会刷新<strong>本地</strong> Python 模块。

            标准库模块与已安装的包（即位于 `site-packages` 中的模块）会被跳过，以保证环境稳定。

    - <strong>Clear</strong>：将工作区重置为默认状态。
    - <strong>Delete</strong>：关闭工作区并释放其占用的资源。

---

## 2. 菜单栏

顶部菜单栏提供影响整个应用的全局控制项。

### `New` 菜单
向 <strong>VSView</strong> 中载入新内容：

- **`Load Script...`**：打开 VapourSynth（`.vpy`）或 Python（`.py`）脚本。
- **`Load File...`**：打开视频或图片文件。
- <strong>Workspace 子菜单</strong>：手动创建一个指定类型的空工作区。

### `View` 菜单
管理工作区环境：

- **`Sidebar`**：显示或隐藏主导航侧边栏。
- **`Tool Docks`**：显示或隐藏常驻的停靠工具。
- **`Tool Panels`**：显示或隐藏以标签页形式呈现的工具面板。

### `Settings`
打开 <strong>Settings 对话框</strong>，可在其中自定义快捷键、应用设置与插件设置。

---

## 3. 主内容区域

主区域显示当前工作区的内容。
更多信息参见[工作区](workspaces/workspace.md)。
