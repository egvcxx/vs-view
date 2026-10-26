---
icon: lucide/palette
title: 色彩管理
description: VSView 如何处理色彩空间转换与帧属性。
---

# 色彩管理

显示 VapourSynth 片段时，<strong>VSView</strong> 必须先将输出转换为 packed RGB 才能渲染到屏幕上。

默认情况下，这一转换以 <strong>BT.709</strong> 色彩空间（原色与传递特性）为目标，用于标准动态范围（SDR）渲染，
但你可以全局配置，也可以按片段分别覆盖。

处理高动态范围（HDR）内容时，VSView 可在支持 HDR 的显示器上实现原生端到端 HDR 渲染。

!!! info "不做色调映射"

    VSView 在 SDR 与 HDR 模式下都不对 HDR 内容做任何色调映射。

    - <strong>在 SDR 模式下</strong>：HDR 内容与超范围数值会被裁剪到目标 SDR 色域（默认为 BT.709）。
    - <strong>在 HDR 模式下</strong>：原生线性 PQ 值会被直接转换为线性 scRGB 并交给操作系统合成器。

        任何色调映射或亮度映射（以适配显示器峰值亮度）完全由操作系统与显示硬件处理。

    该行为只影响预览，不会改变脚本中的源片段。

## SDR 输出目标

配置 SDR 渲染的目标色彩空间。

### 全局设置

位于 <strong>Settings</strong> > <strong>View</strong> 下：

- <strong>Output Transfer</strong>：目标传递特性（默认：`BT709`）。
- <strong>Output Primaries</strong>：目标原色（默认：`BT709`）。

### 脚本覆盖

向 `set_output()` 传入 `transfer` 和/或 `primaries`，即可按片段覆盖设置：

```python title="script.vpy"
import vapoursynth as vs
from vsview import set_output

set_output(clip, transfer=vs.TRANSFER_BT2020_10, primaries=vs.PRIMARIES_BT2020)
```

## 必需的帧属性

VSView 依赖 VapourSynth 帧属性 [`_Matrix`](https://www.vapoursynth.com/doc/apireference.html#reserved-frame-properties)、
[`_Primaries`](https://www.vapoursynth.com/doc/apireference.html#reserved-frame-properties)
与 [`_Transfer`](https://www.vapoursynth.com/doc/apireference.html#reserved-frame-properties)
来在转换期间正确解释片段的色彩空间。

如果缺少这些属性，转换可能失败，或颜色显示不正确。

!!! info "显式处理"

    VSView 不会推断或“猜测”缺失的属性。

    你必须确保片段设置了正确的属性，或配置一个回退策略。

## 帧属性策略

你可以通过 <strong>Settings 对话框</strong>控制 VSView 对缺失属性的反应方式。

!!! danger "YUV 转换"

    如果片段的色彩家族为 `YUV` 且 `_Matrix` 未知或未指定，VSView 一定无法将输出转换为 RGB。

- <strong>Error（默认）</strong>

    如果缺少 `_Transfer` 或 `_Primaries`，VSView 会停止渲染并显示一张失败提示图，
    因为 VapourSynth 没有足够的信息在色彩空间之间转换。

-  <strong>Warn</strong>

    如果缺少 `_Transfer` 或 `_Primaries`，则不执行传递特性或原色转换，改为记录一条警告日志。

-  <strong>Ignore</strong>

    执行与 <strong>Warn</strong> 相同的步骤，但不向日志输出警告。


## 高动态范围（HDR）

VSView 通过高位深色彩转换与硬件加速，支持原生 HDR 显示输出。

要以 HDR 预览内容，必须满足以下条件：

1. <strong>系统与显示器</strong>：已连接支持 HDR 的显示器，并在操作系统设置中启用了 HDR。
2. <strong>命令行参数</strong>：使用 [`--hdr` 命令行选项](configuration.md#-hdr) 启动 VSView（或设置环境变量 `VSVIEW_HDR=true`）。

### 脚本配置

默认情况下，启用 `--hdr` 后，所有输出都会尝试 HDR 转换。
你可以在 VapourSynth 脚本中向 `set_output()` 传入 `hdr=False`，显式覆盖该行为，或按输出禁用 HDR。

```python title="script.vpy"
from vsview import set_output

# 为该输出禁用 HDR
set_output(clip, hdr=False)
```
