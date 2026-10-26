---
icon: lucide/globe
title: 第三方插件
---

# 第三方插件

第三方插件由独立开发者维护。

## 概览

<div class="grid cards" markdown>

- :lucide-box: <strong>Native Resolution</strong>

    ---

    面向 VSView 的反缩放（descale）分析套件，提供 `Get Native`、`Get Scaler` 与 `Get Frequencies`。

    [:lucide-move-right: 详情](#native-resolution) · [:fontawesome-brands-github: 源码](https://github.com/Jaded-Encoding-Thaumaturgy/native-res)

</div>

---

## Native Resolution [ :fontawesome-brands-github: ](https://github.com/Jaded-Encoding-Thaumaturgy/native-res){ title="Source Code" }

=== "pip"
    ```bash
    pip install vsview-nativeres
    ```
=== "uv"
    ```bash
    uv add vsview-nativeres
    ```

!!! tip "通过合集安装"
    `vsview-nativeres` 也包含在 <strong>full</strong> 合集中。你可以连同所有其他插件一起安装：

    === "pip"
        ```bash
        pip install vsview[full]
        ```
    === "uv"
        ```bash
        uv add vsview --extra full
        ```

`vsview-nativeres` 为 [nativeres](https://github.com/Jaded-Encoding-Thaumaturgy/nativeres) 提供前端，可在 VSView 内分析分辨率。

### 功能

- <strong>Get Native</strong>：在指定的尺寸范围内绘制反缩放误差曲线。
- <strong>Get Scaler</strong>：针对目标尺寸对各个内核（kernel）进行排名。
- <strong>Get Frequencies</strong>：可视化基于 DCT 的频率分布。

更多信息见 [nativeres 文档](https://github.com/Jaded-Encoding-Thaumaturgy/nativeres)与
[vsview-nativeres 文档](https://github.com/Jaded-Encoding-Thaumaturgy/nativeres/blob/master/src/plugin/README.md)。

### 依赖

- [<strong>nativeres</strong>](https://github.com/Jaded-Encoding-Thaumaturgy/nativeres)
