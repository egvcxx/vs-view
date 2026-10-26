---
icon: lucide/file-pen
title: Visual Studio Code 集成
description: 直接在 Visual Studio Code 中对当前文件运行 VSView。
---

# Visual Studio Code 集成

可配置 Visual Studio Code 任务，对正在编辑的文件启动 VSView。
这对快速预览 VapourSynth 脚本非常有用。

## 任务配置

在项目中创建（或追加）`.vscode/tasks.json`：

```json title=".vscode/tasks.json"
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "VSView",
      "type": "shell",
      "command": {
        "value": "${command:python.interpreterPath}",
        "quoting": "strong"
      },
      "args": [
        "-m",
        "vsview",
        { "value": "${file}", "quoting": "strong" }
      ],
      "group": {
        "kind": "none",
        "isDefault": true
      },
      "presentation": {
        "reveal": "always",
        "panel": "shared"
      }
    }
  ]
}
```

`${command:python.interpreterPath}` 会解析为 Visual Studio Code 中当前选中的
Python 解释器（通过
[Python 扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python)），
因此无论虚拟环境位于何处、使用哪种平台，该任务都能正常工作。
请确保 VSView 已安装在对应解释器的环境中。

打开脚本后，通过 <strong>Terminal → Run Task… → VSView</strong> 运行该任务，
或为 `workbench.action.tasks.runTask` 添加带 `"args": "VSView"` 的快捷键绑定。

!!! warning "避免使用 `launch.json` / debugpy"

    请优先使用任务，而不是调试启动配置（`launch.json` 中的 `type: "debugpy"`）。
    在调试器下运行 VSView 会降低性能，并可能导致死锁，设置断点时尤其明显。
