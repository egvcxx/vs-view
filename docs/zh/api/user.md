---
icon: lucide/user
---

# 用户 API

面向用户的 API 主要在 VapourSynth 脚本中使用，用于注册需要预览的节点。

!!! note "以下内容为英文原文"

    本页 API 由源码 docstring 自动生成，故保持英文，以便与代码和参数名对照。

::: vsview.api
    options:
        heading_level: 3
        members:
           - set_output
           - catch_output
           - is_preview
           - is_reload
           - get_reload_count
           - get_state
           - get_cached
           - on_workspace_destroy
