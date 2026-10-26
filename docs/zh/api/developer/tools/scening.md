---
icon: lucide/clapperboard
---

# Scening 工具 API

用于通过自定义解析器与序列化器扩展 Scening 工具的 API。

!!! note "以下内容为英文原文"

    本页 API 由源码 docstring 自动生成，故保持英文，以便与代码和参数名对照。

---

[:lucide-box:{ .middle } <strong>核心类</strong>](#core-classes)

[:lucide-database:{ .middle } <strong>数据模型</strong>](#models)

[:lucide-wrench:{ .middle } <strong>工具与钩子</strong>](#utility-hook)

---

## 核心类（Core Classes）
::: vsview.app.tools.scening.api
    options:
        heading_level: 3
        members:
           - Parser
           - Serializer
           - FileFilter

## 数据模型（Models）
::: vsview.app.tools.scening.api
    options:
        heading_level: 3
        members:
           - RangeFrame
           - RangeTime
           - SceneRow
           - UnifiedRange

## 工具与钩子（Utility & Hook）
::: vsview.app.tools.scening.api
    options:
        heading_level: 3
        members:
           - borrowed_text_wrapper
           - hookimpl
