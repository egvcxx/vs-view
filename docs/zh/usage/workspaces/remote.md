---
icon: lucide/monitor-up
title: 远程工作区
description: 在 VSView 中借助 vsremote 远程执行 VapourSynth 的工作区。
---

# 远程工作区

<strong>远程工作区</strong>借助 [vsremote](https://github.com/Ichunjo/vs-remote) 实现远程脚本执行。
它从客户端载入本地脚本，把代码发送到远程服务器执行，再把产生的视频输出流式传回客户端以供预览与检查。

通用工作区布局与查看器控件请参阅[工作区概览](workspace.md)。

---

## 安装

=== "uv"
    ```bash title="添加远程工作区"
    uv add vsview-remote
    ```
=== "pip"
    ```bash title="安装远程工作区"
    pip install vsview-remote
    ```

---

## 用法

### 1. 启动远程服务器

服务器必须以 `--allow-eval` 启动，以允许动态执行脚本：

```bash
vsremote serve --allow-eval
```

!!! danger
    使用 `--allow-eval` 运行意味着允许在服务器上执行任意 Python 代码。
    关于如何保护连接（SSH 隧道、CurveZMQ 加密、客户端白名单），请参阅
    [vsremote 的安全说明](https://github.com/Ichunjo/vs-remote#security)。

### 2. 在 VSView 中打开脚本

通过 <strong>New &rarr; Workspace &rarr; Remote</strong> 打开本地的 `.vpy` 或 `.py` 脚本。

执行脚本前会弹出连接对话框，要求填写服务器连接信息。
随时可以按 ++ctrl+alt+r++ 重新打开该对话框，修改连接参数并重新加载当前脚本

---

## 配置项

插件偏好可在 VSView 设置的 <strong>Plugin &rarr; Remote</strong> 中调整。敏感值（auth token、Curve 密钥）会保存在加密的插件密钥存储中。

---

## 在服务器上编写脚本（Shim）

如果你直接在服务器上编写并托管脚本（例如 `vsremote serve script.vpy`），则不需要 `--allow-eval`。
此时可以从标准的脚本工作区或编辑器工作区，通过一个本地 shim 连接：

```python title="shim.vpy"
import vsremote
import vsview


def setup_client() -> vsremote.RemoteClient:
    # 连接到远程服务器
    client = vsremote.RemoteClient("tcp://127.0.0.1:5555")
    client.start()
    # 注册回调，在工作区销毁时关闭客户端
    vsview.register_on_workspace_destroy(client.close)
    # 测试连接
    assert client.ping().result(timeout=10.0)
    return client


# 使用缓存的客户端，避免每次重新加载都新建客户端
client = vsview.get_cached("remote_client", setup_client)

# 如果脚本正在重新加载，向服务器发送重载信号
if vsview.is_reload():
    client.reload().result()

# 获取远程脚本的输出，并设为 VSView 中的输出
for idx, clip in client.get_outputs().items():
    name = client.get_clip_info(idx).result().name
    vsview.set_output(clip, idx, name)
```
