---
icon: lucide/download
title: 安装
---

# 安装

VSView 既可以通过 `pip` 或 `uv` 作为 Python 包安装，也可以直接使用预编译的独立可执行文件。

## Python 包

请选择你惯用的包管理器，将 `vsview` 安装到现有的 Python 环境中。

对大多数用户，建议安装 <strong>[推荐包](plugins/second-party.md#installation)</strong> 或 <strong>[完整包](plugins/second-party.md#installation)</strong>，以获得开箱即用的体验。

=== "pip"

    ```bash title="最小安装"
    pip install vsview
    ```

    ```bash title="安装并启用推荐插件"
    pip install vsview[recommended]
    ```

    ```bash title="安装全部插件"
    pip install vsview[full]
    ```

=== "uv"

    ```bash title="最小安装"
    uv add vsview
    ```

    ```bash title="安装并启用推荐插件"
    uv add vsview --extra recommended
    ```

    ```bash title="安装全部插件"
    uv add vsview --extra full
    ```

---

## 独立可执行文件

面向 Windows x86-64 与 Linux x86-64 的预编译二进制包发布在 [GitHub Releases](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/releases)。

发布的可执行文件提供两种变体：

- <strong>在线版（推荐）</strong>：下载体积小，首次启动时动态获取依赖。
- <strong>离线版</strong>：内置 Python 运行时与预装的工作区包，无需外部 Python 环境，也无需联网。

!!! note "网络环境"

    在线版首次启动需要联网下载依赖。中国大陆用户请先确认网络环境可以访问 PyPI、GitHub 等服务；
    无法访问时请改用离线版。

=== "Windows"

    - 从 [GitHub Releases](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/releases) 下载 `VSView.exe`（或 `VSView-offline.exe`），
    随后直接运行。

=== "Linux"

    1. 从 [GitHub Releases](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/releases) 下载并解压 Linux 发布包
    （`vsview-pyapp-linux-x86_64.tar.gz` 或离线变体）。
    2. 在解压后的目录中运行随附的安装脚本：

        ```bash
        bash install.sh
        ```

    该脚本会将可执行文件安装到 `~/.local/bin/VSView`，在 `~/.local/share/icons` 注册标准 hicolor 图标，
    并创建 `.desktop` 菜单启动项。

### 扩展独立可执行文件

独立可执行文件自带一个隔离的 Python 环境，无需全局 Python，即可在其中安装内容。

!!! tip "安装插件与依赖包"

    使用 `vsview env pip` 可以把额外的 Python 包或插件直接安装到独立版的环境中：

    === "Windows"

        ```powershell
        .\VSView.exe env pip install vsjetpack[full]
        ```

    === "Linux"

        ```bash
        /VSView env pip install vsjetpack[full]
        ```

关于独立环境的更多管理与扩展说明，详见[配置](usage/configuration.md#standalone-environment-management-env)。

---

## 开发环境安装

如果你要参与贡献、从源码构建或在本地开发，请参阅[贡献指南](contributing.md)与[打包与分发](packaging.md)。
