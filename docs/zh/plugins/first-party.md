---
icon: lucide/package-check
title: 第一方插件
---

# 第一方插件

第一方插件是直接集成在 <strong>VSView</strong> 源码中的官方组件，随每次发布一同分发。

<div class="grid cards" markdown>

- :lucide-audio-lines: <strong>Audio Convert</strong>

    ---

    一个 [AudioNode](https://www.vapoursynth.com/doc/pythonreference.html#vapoursynth.AudioNode) 处理器，用于转换音频采样类型并为播放重采样音频片段。

    [:lucide-move-right: 详情](#audio-convert)

- :lucide-pipette: <strong>Color Picker</strong>

    ---

    直接在视口中查看精确的像素值。实时对比渲染后的 RGB 值与源数值。

    [:lucide-move-right: 了解 Color Picker](#color-picker)

- :lucide-list-video: <strong>Frame Properties</strong>

    ---

    查看 VapourSynth 滤镜附加的帧属性。

    [:lucide-move-right: 了解 Frame Properties](#frame-properties)

- :lucide-clapperboard: <strong>Scening</strong>

    ---

    创建、管理并导出场景区间或视频片段。支持自定义解析器与序列化器。

    [:lucide-move-right: 了解 Scening](#scening)
    
- :lucide-scan: <strong>Region Selector</strong>

    ---

    在视口中选取并微调精确区域，用于裁剪与检查。

    [:lucide-move-right: 了解 Region Selector](#region-selector)


</div>

---

## Audio Convert

Audio Convert 插件将一个专用的 [AudioNode](https://www.vapoursynth.com/doc/pythonreference.html#vapoursynth.AudioNode) 处理器集成到 <strong>VSView</strong> 管线中，用于协调脚本音频与系统播放能力之间的差异。

在 <strong>Settings</strong> 菜单的 <strong>Plugin - Audio Convert</strong> 分区中配置目标位深、采样类型、采样率与抖动类型。

---

## Color Picker

Color Picker 停靠工具可用于检查画面中任意位置的精确像素值。

<figure markdown="span">
    ![Color Picker 停靠面板，显示源数值与渲染后的像素值](../assets/colorpicker_dock.png){ loading=lazy }
</figure>

### 使用方法

1.  点击工具栏中的<strong>吸管图标</strong>以激活该工具。
2.  将鼠标<strong>悬停在视口上</strong>即可查看实时像素数据。
3.  <strong>右键点击</strong>或再次点击工具图标即可停用。

### 提供的数据
检查器会为所选像素提供两组数值：

- <strong>Rendered Values（渲染值）</strong>：经过 <strong>VSView</strong> 内部渲染管线之后呈现的 RGB 值。
- <strong>Source Values（源值）</strong>：直接来自 VapourSynth 片段的原始底层采样值。

---

## Frame Properties

Frame Properties 面板显示 VapourSynth 滤镜为每一帧附加的元数据。

<figure markdown="span">
    ![Frame Properties 面板，显示当前帧的元数据](../assets/frameprops_panel.png){ loading=lazy }
</figure>

### 功能
- <strong>分类</strong>：属性按逻辑类别分组（例如 Video、Metrics、Field）。
- <strong>格式化器</strong>：数值会根据其类型自动格式化为可读字符串。
- <strong>右键菜单</strong>：右键点击某个属性，可打开包含“复制属性值”或“复制属性键”选项的菜单。

!!! Abstract "扩展功能"
    如需更多属性类别与格式化器，见 [FrameProps Extended](second-party.md#frameprops-extended)。

!!! warning "性能与显示限制"
    - 过大的属性值（例如超长字符串、字节缓冲区或大型列表）会自动截断后再显示。
    - 如果一帧包含超过 100 个属性，则会完全跳过加载，以保持界面响应速度。

---

## Scening

Scening 停靠工具用于创建、管理并导出场景区间。

<figure markdown="span">
    ![Scening 停靠面板，显示场景区间](../assets/scening_dock.png){ loading=lazy }
</figure>

### 场景管理

上方面板管理<strong>场景（scenes）</strong>，即区间的命名容器。每个场景都有可自定义的颜色，可以绑定到特定输出，并带有一个控制时间轴可见性的显示开关。

- <strong>:lucide-plus: Create new scene</strong> 添加新场景。
- <strong>:lucide-x: Delete</strong> 删除场景。
- <strong>Color</strong> 色块用于修改场景颜色。
- <strong>Outputs</strong> 列用于将场景限制到特定的视频输出。
- <strong>Display</strong> 复选框用于切换场景在时间轴上的可见性。

### 添加区间

下方面板显示属于所选场景的区间。你可以通过 <strong>Mark in / Mark out</strong> 流程构建区间，也可以直接把当前帧添加为单帧区间。

当你需要一段跨帧的区间时，使用标准区间流程：

1. 在时间轴上定位到期望的起始帧。
2. 按 ++q++（或点击 <strong>Mark in</strong>）设置起点。
3. 定位到期望的结束帧。
4. 按 ++w++（或点击 <strong>Mark out</strong>）设置终点。
5. 按 ++e++（或点击 <strong>Add range</strong>）将区间提交到所选的场景。

当区间应当起止于同一帧时，使用单帧流程：

1. 在时间轴上定位到目标帧。
2. 按 ++r++（或点击 <strong>Add frame</strong>），将该帧作为区间添加到所选场景。

每个区间会显示其 <strong>Start Frame</strong>、<strong>End Frame</strong>、<strong>Start Time</strong>、<strong>End Time</strong> 以及可选的 <strong>Label</strong>。

### 快捷键

| 快捷键               | 操作                             |
| :------------------- | :------------------------------- |
| ++q++                | 切换区间起点（Mark in）          |
| ++w++                | 切换区间终点（Mark out）         |
| ++e++                | 校验/添加待提交的区间            |
| ++r++                | 将当前帧添加为区间               |
| ++del++              | 删除选中的区间或场景             |
| ++ctrl+left++        | 跳转到上一个区间边界             |
| ++ctrl+right++       | 跳转到下一个区间边界             |
| ++ctrl+shift+left++  | 跳转到上一个区间                 |
| ++ctrl+shift+right++ | 跳转到下一个区间                 |

每个快捷键都可以在 <strong>Settings</strong> 菜单中自定义。

### 时间轴集成

启用某个场景的 <strong>Display</strong> 复选框后，其区间会以彩色刻度直接绘制在时间轴上。
将鼠标悬停在刻度上会显示带有区间标签（若已设置）的工具提示。
场景可以按输出过滤，因此只有与当前视频标签页相关的区间会被显示。

### 导入与导出

工具栏提供 <strong>Import scene...</strong> 与 <strong>Export scene...</strong> 按钮，用于处理外部文件。

#### 支持的导入格式

| 格式                     | 扩展名         |
| :----------------------- | :------------- |
| Aegisub Advanced SSA     | `.ass`         |
| OGM Chapters             | `.txt`         |
| Matroska XML Chapters    | `.xml`         |
| XviD Log                 | `.txt`、`.log` |
| QP File                  | `.qp`、`.txt`  |
| Wobbly File              | `.wob`         |
| Python List (Frames)     | `.txt`         |
| Python List (Timestamps) | `.txt`         |

#### 支持的导出格式

| 格式                     | 扩展名  |
| :----------------------- | :------ |
| OGM Chapters             | `.txt`  |
| QP File                  | `.qp`   |
| Python List (Frames)     | `.txt`  |
| Python List (Timestamps) | `.txt`  |

#### 导出视频片段

你可以把选中的区间直接导出为视频文件：

1. 在下方面板中选中一个或多个区间。
2. <strong>右键点击</strong>并选择 <strong>Export</strong> -> <strong>H.264 (8-bit YUV)</strong>（`.mp4`）或 <strong>Lossless FFV1</strong>（`.mkv`）。
3. 选择目标文件（单个区间）或基础文件名（批量导出）。

导出会通过 FFmpeg 在后台异步执行（FFmpeg 路径可在 <strong>Settings</strong> -> <strong>Plugin - Scening</strong> 中配置）。

!!! Abstract "扩展功能"
    开发者可以通过插件钩子系统注册自定义解析器与序列化器。
    详见 [Scening 工具 API](../api/developer/tools/scening.md)。

---

## Region Selector

Region Selector 工具用于在画面中定义矩形区域，主要用于生成 VapourSynth 裁剪参数。

<figure markdown="span">
    ![Region Selector 停靠面板](../assets/region_selector_dock.png){ loading=lazy }
</figure>

### 功能

- <strong>边界微调</strong>：通过数值框直接控制 Left、Right、Top、Bottom、Width 与 Height。
- <strong>按模数吸附</strong>：选区边界会吸附到设置中定义的 `mod` 值（例如 mod 2、mod 4）。
- <strong>代码生成</strong>：根据当前选区生成 VapourSynth 代码片段（例如 `std.Crop`）。
- <strong>交互式叠加层</strong>：可调整大小、可移动的区域叠加层，带有角点与边缘手柄。

### 使用方法

1.  点击 <strong>Frame Corners</strong> 图标或按 ++c++。
2.  在视口中<strong>左键拖动</strong>以定义初始区域。
3.  使用<strong>手柄</strong>或<strong>数值框</strong>调整边界。
4.  点击<strong>剪贴板图标</strong>复制生成的代码。
5.  点击 <strong>X-Circle</strong> 图标或按 ++c++ 停用。

### 快捷键

| 快捷键  | 操作                 |
| :------ | :------------------- |
| ++c++   | 切换 Region Selector |
| ++esc++ | 清除当前选区         |

快捷键、`mod` 与代码片段均可在 <strong>Settings</strong> 菜单中配置。
