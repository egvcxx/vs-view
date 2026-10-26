---
icon: lucide/blocks
title: 第二方插件
---

# 第二方插件

第二方插件由官方维护，但以独立包的形式分发，以保持核心安装轻量。

## 概览

<div class="grid cards" markdown>

- :lucide-split-square-horizontal: <strong>Comparison</strong>

    ---

    选择、提取对比帧并上传到 Slow.pics，支持 TMDB 元数据集成。

    [:lucide-move-right: 详情](#comparison) · [:fontawesome-brands-github: 源码](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/comp)

- :lucide-code: <strong>Editor</strong>

    ---

    面向 VapourSynth 脚本的 Monaco 代码编辑器工作区。

    [:lucide-move-right: 详情](../usage/workspaces/editor.md) · [:fontawesome-brands-github: 源码](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/workspaces/editor)


- :lucide-activity: <strong>FFT Spectrum</strong>

    ---

    显示视频片段各平面的快速傅里叶变换（FFT）频谱。

    [:lucide-move-right: 详情](#fft-spectrum) · [:fontawesome-brands-github: 源码](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/fftspectrum)

- :lucide-list-plus: <strong>FrameProps Extended</strong>

    ---

    为内置的 [Frame Properties](first-party.md#frame-properties) 工具扩展专用类别与格式化器。

    [:lucide-move-right: 详情](#frameprops-extended) · [:fontawesome-brands-github: 源码](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/frameprops-extended)

- :lucide-bar-chart-2: <strong>Histogram</strong>

    ---

    逐帧视频示波器：Levels、Luma、Vectorscope 与 Waveform。

    [:lucide-move-right: 详情](#histogram) · [:fontawesome-brands-github: 源码](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/histogram)

- :lucide-monitor-up: <strong>Remote</strong>

    ---

    由 [vsremote](https://github.com/Ichunjo/vs-remote) 驱动的远程 VapourSynth 执行与帧流式传输工作区。

    [:lucide-move-right: 详情](../usage/workspaces/remote.md) · [:fontawesome-brands-github: 源码](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/workspaces/remote)

- :lucide-layers-2: <strong>Split Planes</strong>

    ---

    单独查看视频片段的各个平面（例如 Y、U、V），以检查通道特有的伪影。

    [:lucide-move-right: 详情](#split-planes) · [:fontawesome-brands-github: 源码](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/split-planes)

</div>

---

## 安装（Installation）
第二方插件由官方维护，但以独立 Python 包形式分发。注意其中许多插件还需要在 VapourSynth 环境中安装特定的<strong>原生 VapourSynth 插件</strong>。

你可以单独安装插件，也可以选择预配置的合集。

!!! tip "可选：recommended 与 full 合集"
    * <strong>recommended</strong> 合集包含 <strong>Split Planes</strong>、<strong>FrameProps Extended</strong> 与 <strong>Comparison</strong>。
    * <strong>full</strong> 合集包含 <strong>recommended</strong> 中的全部插件，另加 <strong>Histogram</strong>、<strong>Editor</strong> 以及第三方 [<strong>Native Resolution</strong>](third-party.md#native-resolution) 插件。

    === "pip"
        ```bash title="安装 recommended 合集"
        pip install vsview[recommended]
        ```

        ```bash title="安装 full 合集"
        pip install vsview[full]
        ```
    === "uv"
        ```bash title="添加 recommended 合集"
        uv add vsview --extra recommended
        ```

        ```bash title="添加 full 合集"
        uv add vsview --extra full
        ```

各独立包的详细安装方式见下文对应用户章节。

---

## Comparison [ :fontawesome-brands-github: ](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/comp){ title="Source Code" }

=== "pip"
    ```bash title="安装 Comparison"
    pip install vsview-comp
    ```
=== "uv"
    ```bash title="添加 Comparison"
    uv add vsview-comp
    ```

Comparison 插件提供了一套完整流程：提取帧并直接上传到 [Slow.pics](https://slow.pics/)。

它具备自动选帧、按画面类型过滤以及与 TMDB 集成的能力。

### 功能
- <strong>选帧</strong>：
    - 按帧数与时间范围手动或自动选择帧。
    - 按画面类型（I/P/B 帧）与混合帧（combed）过滤。
    - 使用非对称高斯亮度评分选出最暗和/或最亮的帧。
- <strong>概率曲线</strong>：
    - 通过交互式曲线编辑器，调整随机帧在时间轴上的抽取偏向。
    - 点击随机帧数旁的 <strong>Curve...</strong> 打开编辑器。
- <strong>TMDB 集成</strong>：
    - 从 TMDB 搜索并获取元数据，自动填充合集名称。
    - 在插件 <strong>Settings</strong> 中自定义命名格式。
- <strong>直接上传</strong>：
    - 将提取的帧上传到 [Slow.pics](https://slow.pics/)。
    - 在插件 <strong>Settings</strong> 中配置登录信息后即可直接上传。

### 设置

| 设置项                      | 默认值   | 说明                                                                                            |
| :-------------------------- | :------- | :---------------------------------------------------------------------------------------------- |
| <strong>Browser ID</strong>              | 自动     | 每次上传时发送给 Slow.pics 的 UUID。（见 [Browser ID](#browser-id)）                             |
| <strong>Allowed frame searches</strong>  | 150      | 每个帧位在放弃前的最大尝试次数。                                                                |
| <strong>Brightness candidates</strong>   | 0（自动）| 用于暗/亮帧选择的候选帧数量。`0` 表示根据片段长度与 FPS 自动缩放。                              |

### 帧列表右键菜单

在已选帧列表中右键点击任意缩略图，会打开用于管理与复制帧数据的菜单。支持多选（++ctrl++ 点击或 ++shift++ 点击）：

| 操作                     | 说明                                                                       |
| :----------------------- | :------------------------------------------------------------------------- |
| <strong>Copy timestamp(s)</strong>    | 将时间戳（`HH:MM:SS.mmm`）或时间戳列表复制到剪贴板。                       |
| <strong>Copy frame number(s)</strong> | 将帧号或帧号列表复制到剪贴板。                                             |
| <strong>Remove frame(s)</strong>      | 从列表中移除所选帧（也支持 ++delete++）。                                  |

双击列表中的任意缩略图，可将播放直接跳转到该帧。

### 概率曲线编辑器

点击 <strong>Curve...</strong>（位于随机帧数旁）打开曲线编辑器，调整随机帧在时间轴上的采样偏向。

| 操作                                     | 效果                                |
| :--------------------------------------- | :---------------------------------- |
| 在图表上双击                             | 添加一个控制点                      |
| 拖动控制点                               | 调整其位置与权重（Y 轴，0 – 5）     |
| 在控制点上双击                           | 打开浮层以精确设置帧号与权重        |
| 右键 / ++delete++ / ++backspace++        | 删除该控制点                        |
| <strong>Reset</strong>                                | 恢复为扁平均匀分布                  |

边界点（起始帧/结束帧）在水平方向固定，但权重可编辑。各处 Y = 1 即为均匀采样。

### 暗帧 / 亮帧选择

候选帧会针对其平均亮度（`PlaneStatsAverage`）使用<strong>非对称高斯</strong>评分：

- <strong>暗帧</strong>：峰值 ≈ 6.5 %（左侧 σ = 0.015，右侧 σ = 0.15）
- <strong>亮帧</strong>：峰值 ≈ 75 %（左侧 σ = 0.45，右侧 σ = 0.90）

### Browser ID

每次上传都会带上一枚持久化的 <strong>Browser ID</strong> UUID，以便 Slow.pics 将其与你的浏览器会话关联。

!!! tip "认领匿名上传"
    如果你在未登录状态下上传，事后仍可认领该对比：

    1. 从插件 <strong>Settings</strong> 中复制你的 <strong>Browser ID</strong>（点击剪贴板按钮）。
    2. 在浏览器开发者工具（++f12++）中进入 **Application → Cookies → `slow.pics`**，把 `BROWSER-ID` 设为该值。
    3. 刷新对比页面，并从页面菜单中认领。

    若在上传时已登录，Slow.pics 会返回它自己的 `BROWSER-ID`，插件会自动采用它。

### 脚本集成

默认情况下，所有 `set_output` 输出都是可用的。传入 `allow_comp` 可显式排除特定输出。

### VapourSynth 依赖
- [<strong>fpng</strong>](https://github.com/Mikewando/vsfpng)（可选）：可略微加快帧提取速度。

---

## FFT Spectrum [ :fontawesome-brands-github: ](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/fftspectrum){ title="Source Code" }

=== "pip"
    ```bash title="安装 FFT Spectrum"
    pip install vsview-fftspectrum
    ```
=== "uv"
    ```bash title="添加 FFT Spectrum"
    uv add vsview-fftspectrum
    ```

FFT Spectrum 工具可将视频片段各平面的快速傅里叶变换（FFT）频谱可视化。

---

## Histogram [ :fontawesome-brands-github: ](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/histogram){ title="Source Code" }

=== "pip"
    ```bash title="安装 Histogram"
    pip install vsview-histogram
    ```
=== "uv"
    ```bash title="添加 Histogram"
    uv add vsview-histogram
    ```

在单个面板中以标签页形式提供逐帧视频示波器。

- 播放期间暂停更新，播放停止后恢复当前活动标签页的更新。
- 右键点击任意图表可复制或保存视图。

!!! note
    Luma 标签页使用 [Numba](https://numba.pydata.org/) JIT 编译。启动时会在后台预热；预热完成前该标签页不可用。

### Levels

绘制当前帧按平面统计的像素值直方图。

| 控件                  | 选项                 | 说明                                                                                    |
| :-------------------- | :------------------- | :-------------------------------------------------------------------------------------- |
| <strong>Bin resolution</strong>    | Auto、256、512、1024 | 直方图的分箱数量。Auto 会根据面板宽度缩放。                                             |
| <strong>Clamp factor</strong>      | 0.001 % – 100 %      | 将峰值分箱计数裁剪到总像素的这一百分比，使较小的峰值也能显示。                          |
| <strong>Show unsafe zones</strong> | 开 / 关              | 高亮广播非法范围（仅 YUV 有限范围）。                                                   |

### Luma

使用 VapourSynth 的 `ModifyFrame` 节点显示亮度示波器，并通过标准图形视图渲染。

| 控件                  | 选项                          | 说明                                                        |
| :-------------------- | :---------------------------- | :---------------------------------------------------------- |
| <strong>Frequency (Shift)</strong> | 2 – 256 周期（shift 1 – 8）   | 控制示波器上显示的亮度周期数量。                            |
| <strong>Sawtooth style</strong>    | 开 / 关                       | 将渲染风格从类正弦波形切换为锯齿波形。                      |

仅支持 GRAY 与 YUV 输入。RGB 输入会显示错误提示层。

### Vectorscope

在二维平面上绘制色度（U/V）分布。

示波网格显示 75 % 与 100 % 饱和度圆、肤色参考线，以及会自动根据片段色彩矩阵调整的主/次色目标点
（支持 Rec. 601、Rec. 709、Rec. 2020 与 ST 240M）。

| 控件           | 选项                                   | 说明                                                                                                                                                    |
| :------------- | :------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <strong>Mode</strong>       | Density、Chroma Wheel、Pixel Color     | <strong>Density</strong>：带荧光色表的对数热力图。<br><strong>Chroma Wheel</strong>：在全彩 UV 背景轮上绘制密度图。<br><strong>Pixel Color</strong>：每个像素以其实际转换后的 RGB 颜色绘制。   |
| <strong>Resolution</strong> | Auto、256、512、1024                   | 内部示波图像（正方形）的尺寸。Auto 会以位深上限为界。                                                                                                   |
| <strong>Matrix</strong>     | Auto、BT.709、BT.601、BT.2020、ST 240M | 用于目标网格与信号转换的色彩矩阵系数。Auto 会根据片段属性或分辨率自动识别。                                                                             |
| <strong>Luma</strong>       | 0.01 – 2.00                            | 应用于点云/辉光的亮度缩放系数。仅在 `Chroma Wheel` 模式下生效。                                                                                        |

不支持 RGB 输入，会显示警告。GRAY 输入会将所有像素绘制在中性色度位置。

### Waveform

按列绘制像素值，形成波形图。每一列都会应用对数密度缩放。

| 控件             | 选项                 | 说明                                                                                                                    |
| :--------------- | :------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| <strong>Mode</strong>         | Luma、RGB/YUV Parade | <strong>Luma</strong>：单条 Y 平面波形。<br><strong>Parade</strong>：每个平面并排显示一条波形（取决于色彩家族，为 R/G/B 或 Y/U/V）。              |
| <strong>Resolution</strong>   | Auto、256、512、1024 | 示波器的垂直分辨率。Auto 会以位深上限为界。                                                                             |
| <strong>Show zones</strong>   | 开 / 关              | 叠加中性线与广播限制线（亮度为 16/235，色度为 16/240），并标出阴影化的非法区域。                                        |
| <strong>Dynamic gain</strong> | 开 / 关              | 开启时按最密集的列缩放亮度；关闭时按帧高缩放。                                                                          |
| <strong>Gain</strong>         | 0.1x – 10.0x         | 在对数刻度之上再乘的倍数。                                                                                              |

### CIE Chromaticity

将帧像素的色度坐标绘制到标准 CIE 色度图上（CIE 1931 xy 或 CIE 1976 u'v'）。借此可以直观看到视频的色域覆盖与颜色分布。

示波网格显示常见色域的边界三角形（<strong>Rec. 709</strong>、<strong>Rec. 601</strong>、<strong>DCI-P3</strong> 与 <strong>Rec. 2020</strong>），以及 <strong>D65</strong> 白点参考十字线。

| 控件            | 选项                                  | 说明                                                                                                                                                                                                                                                        |
| :-------------- | :------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <strong>CIE Mode</strong>    | CIE 1931 (xy)、CIE 1976 (u'v')        | 在 CIE 1931 标准色彩空间表示与 CIE 1976 均匀色度标度（UCS）表示之间切换。                                                                                                                                                                                   |
| <strong>Render Mode</strong> | Density、Chroma Wheel、Pixel Color    | <strong>Density</strong>：使用荧光色表显示像素密度的对数热力图。<br><strong>Chroma Wheel</strong>：在全彩背景色度图上以白色辉光绘制密度图。<br><strong>Pixel Color</strong>：每个像素以其实际 RGB 颜色绘制，并按密度与亮度设置缩放。                                                               |
| <strong>Resolution</strong>  | Native、256x256、512x512、1024x1024   | 内部示波图像的尺寸。`Native` 使用帧的高度。                                                                                                                                                                                                                |
| <strong>Luma</strong>        | 0.01 – 2.00                           | 应用于点云/辉光的亮度缩放系数。仅在 `Pixel Color` 与 `Chroma Wheel` 模式下生效。                                                                                                                                                                           |
| <strong>Gamuts</strong>      | Rec. 709、Rec. 601、DCI-P3、Rec. 2020 | 用于切换色度图上目标色域边界三角形与标签显示的复选框。                                                                                                                                                                                                      |

仅支持 RGB 输入。其他格式，或缺少有效 `_Primaries` 帧属性的片段，会显示错误提示层。

---

## FrameProps Extended [ :fontawesome-brands-github: ](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/frameprops-extended){ title="Source Code" }

=== "pip"
    ```bash title="安装 FrameProps Extended"
    pip install vsview-frameprops-extended
    ```
=== "uv"
    ```bash title="添加 FrameProps Extended"
    uv add vsview-frameprops-extended
    ```
该插件为内置的 [Frame Properties](first-party.md#frame-properties) 面板增加更多类别与格式化器。

---

## Split Planes [ :fontawesome-brands-github: ](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/split-planes){ title="Source Code" }

=== "pip"
    ```bash title="安装 Split Planes"
    pip install vsview-split-planes
    ```
=== "uv"
    ```bash title="添加 Split Planes"
    uv add vsview-split-planes
    ```

Split Planes 将视频片段拆分为各个独立平面以便检查。

### 功能
- 扩展图形视图的默认右键菜单，提供偏移色度平面数值的方式。
