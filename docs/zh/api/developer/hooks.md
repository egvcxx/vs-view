---
icon: lucide/webhook
---

# 钩子规范

VSView 的插件系统基于 `pluggy`。使用此处定义的标记注册实现。

!!! note "以下内容为英文原文"

    本页 API 由源码 docstring 自动生成，故保持英文，以便与代码和参数名对照。

---

[:lucide-layout-panel-left:{ .middle } <strong>UI 钩子</strong>](#ui-hooks)

[:lucide-layers:{ .middle } <strong>处理钩子</strong>](#processing-hooks)

[:lucide-webhook:{ .middle } <strong>钩子标记</strong>](#hook)

---

## UI 钩子（Hooks）
::: vsview.app.plugins.specs
    options:
        heading_level: 3
        members:
           - vsview_register_tooldock
           - vsview_register_toolpanel

## 处理钩子（Processing Hooks）
::: vsview.app.plugins.specs
    options:
        heading_level: 3
        members:
           - vsview_get_video_processor
           - vsview_get_audio_processor


## 钩子标记（Hook）
::: vsview.app.plugins.specs
    options:
        heading_level: 3
        members:
           - hookimpl
