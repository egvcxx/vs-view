---
icon: lucide/settings
title: 配置与命令行
description: VSView 的命令行选项与环境变量。
---

# 配置与命令行

VSView 可通过<strong>命令行参数</strong>与<strong>环境变量</strong>配置。

!!! note

    应用设置（外观、时间轴、播放等）通过菜单栏中的内置 <strong>Settings 对话框</strong>管理。

---

## 用法


在桌面预览器中预览 VapourSynth 脚本、视频、图片与音频。
直接打开一个或多个输入文件，或不带文件启动以打开默认工作区。

```bash
vsview [OPTIONS] [FILE]...
vsview COMMAND [OPTIONS] [ARGS...]
```

`[FILE]...`
:   输入文件路径；可以是视频、图片或脚本。VSView 会自动识别类型：

    - `.py` / `.vpy` 文件作为 VapourSynth 脚本打开
    - 其余文件作为视频或图片打开

    若省略，VSView 将以默认工作区启动。

---

## 选项

#### `--arg` / `-a` `KEY=VALUE`
:   向脚本环境传入一个参数。可重复指定多次。

    这与 `vspipe --arg` 的约定一致。

    ```bash
    vsview script.vpy --arg myparam=hello --arg dryrun=true --arg width=1920
    ```

    脚本中随后可通过 `#!python globals()` 访问它们：

    ```pycon title="script.vpy"
    >>> globals()
    {
        ...
        'myparam': 'hello',
        'dryrun': 'true'
        'width': '1920',
        ...
    }
    ```

    !!! info

        所有值都以<strong>字符串</strong>形式传入。
        类型转换由脚本自行负责。

#### `--qt-arg` / `-q` `ARG`
:   将参数直接传给底层的 Qt（PySide6）应用。

    可以重复该选项，或使用一个带引号的字符串来传入多个参数。

    ```bash
    # 单个带引号的字符串（推荐）
    vsview --qt-arg "-platform offscreen -geometry 1920x1080"

    # 多次使用选项
    vsview -q -platform -q offscreen -q -geometry -q 1920x1080
    ```

#### `--hdr`
:   启用高动态范围（HDR）支持，并配置目标图形 API（Direct3D12、Vulkan、Metal）。

    <strong>环境变量：</strong> `VSVIEW_HDR`

#### `--verbose` / `-v`
:   启用详细输出。重复使用以提高详细程度（`-vv`、`-vvv`）。

#### `--help`
:   打印帮助信息。

#### `--version`
:   显示已安装的 vsview 版本并退出（也可使用 `vsview version` 命令）。

---

## 工作区选项

#### `--workspace` / `-w` `WORKSPACE`
:   启动时打开指定工作区。可重复指定以同时打开多个。

    取值为<strong>工作区标识（slug）</strong>，即工作区标题转为小写并将空格替换为连字符。内置标识：

    | 标识           | 工作区                  |
    | :------------- | :---------------------- |
    | `script`       | Python 脚本工作区       |
    | `file`         | 视频文件工作区          |
    | `quick-script` | 快速脚本工作区          |

    若已安装相应插件，也接受插件提供的工作区标识。

    ```bash
    # 启动时打开两个工作区
    vsview --workspace script --workspace file
    ```

#### `--no-default-workspace`
:   启动应用时不打开任何工作区。

    这会抑制三个默认工作区（Python 脚本、视频文件、快速脚本），
    它们通常在没有提供文件或 `--workspace` 参数时自动打开。

    <strong>环境变量：</strong> `VSVIEW_NO_DEFAULT_WORKSPACE`

---

## 设置选项

这些选项控制 VSView 如何处理其配置文件。

#### `--no-settings`
:   本次会话不加载也不保存任何设置。

    <strong>环境变量：</strong> `VSVIEW_NO_SETTINGS`

#### `--settings-roaming`
:   <strong>仅限 Windows。</strong> 将全局设置保存在 `%APPDATA%\vsview\`，而非 `%LOCALAPPDATA%\vsview\`。

    <strong>环境变量：</strong> `VSVIEW_GLOBAL_SETTINGS_ROAMING`

#### `--settings-env`
:   将设置限定到当前 Python 环境。

    每个环境拥有独立子目录，避免不同虚拟环境之间产生冲突。

    <strong>环境变量：</strong> `VSVIEW_GLOBAL_SETTINGS_ENVIRONMENT`

#### `--settings-env-copy`
:   若已设置 `--settings-env`，且限定后的文件尚不存在，则从基础 `global_settings.json` 复制一份作为初始内容。

    <strong>环境变量：</strong> `VSVIEW_GLOBAL_SETTINGS_ENVIRONMENT_COPY`

---

## 日志选项

这些选项控制应用日志的详细程度。

#### `--file-log`
:   在平台的标准日志目录中启用文件日志。

    - Windows：`%LOCALAPPDATA%\vsview\Logs`
    - Linux：`~/.local/state/vsview/log`
    - macOS：`~/Library/Logs/vsview`

    <strong>环境变量：</strong> `VSVIEW_FILE_LOG`

#### `--vapoursynth-log-level` / `-vs-ll` `LEVEL`
:   设置 VapourSynth 核心环境的日志级别。
    可用级别：`critical`、`fatal`、`error`、`warn`、`warning`、`info`、`debug`、`notset`。

    默认为 `INFO`，或在使用 `--verbose` 时跟随详细程度。

    <strong>环境变量：</strong> `VSVIEW_VS_LOG_LEVEL`

#### `--vsengine-log-level` / `-vse-ll` `LEVEL`
:   设置 VSEngine 子系统的日志级别。
    可用级别：`critical`、`fatal`、`error`、`warn`、`warning`、`info`、`debug`、`notset`。

    默认为 `INFO`。

    <strong>环境变量：</strong> `VSVIEW_VSENGINE_LOG_LEVEL`

#### `--qt-log-level` / `-qt-ll` `LEVEL`
:   设置 Qt / PySide6 系统消息的日志级别。
    可用级别：`critical`、`fatal`、`error`、`warn`、`warning`、`info`、`debug`、`notset`。

    默认为 `INFO`，或在使用 `--verbose` 时跟随详细程度。

    <strong>环境变量：</strong> `VSVIEW_QT_LOG_LEVEL`

---

## 命令

### `vsview help`

打印帮助信息，或指定子命令的帮助。

### `vsview config`

通过命令行管理配置目录。

#### `vsview config help`
:   打印本信息或 config 子命令的帮助。

#### `vsview config path`
:   将解析后的配置路径输出到标准输出并退出。

    默认基础目录：

    - Windows：`%LOCALAPPDATA%\vsview\`
    - Linux：`~/.config/vsview/`
    - macOS：`~/Library/Application Support/vsview/`

#### `vsview config wipe`
:   删除配置目录（即 `vsview config path` 显示的路径）并退出。

### `vsview settings`

通过命令行管理应用设置。

#### `vsview settings help`
:   打印本信息或 settings 子命令的帮助。

#### `vsview settings path`
:   将解析后的 `global_settings.json` 路径输出到标准输出并退出。

    若 `--settings-env` 生效，解析结果会遵循环境限定。

    默认基础目录：

    - Windows：`%LOCALAPPDATA%\vsview\`
    - Linux：`~/.config/vsview/`
    - macOS：`~/Library/Application Support/vsview/`

#### `vsview settings wipe`
:   删除 `global_settings.json` 文件（即 `vsview settings path` 显示的路径）并退出。

### `vsview version`

显示已安装的 vsview 版本并退出（`--version` 的替代方式）。

---

## 独立环境管理（Standalone Environment Management env）
预编译的独立可执行文件内置 Python 运行时，由 `vsview env` 命令行命名空间管理。

### 子命令

#### `vsview env pip` `[ARGS]...`
:   使用独立可执行文件内置的 Python 运行时直接调用 `pip`。

    可用此命令安装 VapourSynth 插件或其他 Python 依赖：

    === "PowerShell (Windows)"

        ```powershell
        # 安装额外的插件或依赖包集合
        .\VSView.exe env pip install vsjetpack[full,nvidia] --extra-index-url https://pypi.nvidia.com/

        # 列出可执行文件环境中已安装的包
        .\VSView.exe env pip list

        # 卸载某个包
        .\VSView.exe env pip uninstall <package_name>
        ```

    === "Bash / Zsh (macOS & Linux)"

        ```bash
        # 安装额外的插件或依赖包集合
        ./VSView env pip install "vsjetpack[full,gpu,cl,vulkan]" 

        # 列出可执行文件环境中已安装的包
        ./VSView env pip list

        # 卸载某个包
        ./VSView env pip uninstall <package_name>
        ```

#### `vsview env python` `[ARGS]...`
:   直接调用独立可执行文件内置的 Python 解释器。

    === "PowerShell (Windows)"

        ```powershell
        # 在内置 Python 中验证已安装的模块
        .\VSView.exe env python -c "import vapoursynth; print(vapoursynth.__version__)"
        ```

    === "Bash / Zsh (macOS & Linux)"

        ```bash
        # 在内置 Python 中验证已安装的模块
        ./VSView env python -c "import vapoursynth; print(vapoursynth.__version__)"
        ```

#### `vsview env python-path`
:   输出驱动独立应用的嵌入式 Python 可执行文件绝对路径并退出。

    === "PowerShell (Windows)"

        ```powershell
        .\VSView.exe env python-path
        ```

    === "Bash / Zsh (macOS & Linux)"

        ```bash
        ./VSView env python-path
        ```

#### `vsview env update`
:   在独立可执行文件环境中将 VSView 升级到最新版本。

    这会就地升级 `vsview` 及其直接依赖，同时保留自行安装的包与插件。

    <strong>选项：</strong>

    - `--pre`：允许升级到预发布与开发版本。
    - `--restore` / `-r`：先清空环境，再以完整构建附加项（如 `vsview[all]`）干净重装。

    === "PowerShell (Windows)"

        ```powershell
        # 标准更新
        .\VSView.exe env update

        # 包含预发布版本
        .\VSView.exe env update --pre

        # 清空并以默认构建附加项干净重装
        .\VSView.exe env update --restore
        ```

    === "Bash / Zsh (macOS & Linux)"

        ```bash
        # 标准更新
        ./VSView env update

        # 包含预发布版本
        ./VSView env update --pre

        # 清空并以默认构建附加项干净重装
        ./VSView env update --restore
        ```

#### `vsview env restore`
:   将嵌入式 Python 环境重置并重装为最初的干净状态。

    === "PowerShell (Windows)"

        ```powershell
        .\VSView.exe env restore
        ```

    === "Bash / Zsh (macOS & Linux)"

        ```bash
        ./VSView env restore
        ```

#### `vsview env remove`
:   从磁盘删除独立可执行文件的环境目录。

    === "PowerShell (Windows)"

        ```powershell
        .\VSView.exe env remove
        ```

    === "Bash / Zsh (macOS & Linux)"

        ```bash
        ./VSView env remove
        ```

#### `vsview env cache` `[dist|pip|uv]`
:   查看或管理独立可执行文件启动器使用的分发压缩包、pip wheel 或 uv 缓存资源。

    可用缓存目标：

    * `dist`：缓存的 Python 运行时压缩包。
    * `pip`：缓存的 `pip` wheel 与包下载产物。
    * `uv`：缓存的 `uv` 安装器二进制与解析数据。

    !!! tip "安全的磁盘清理"

        删除任何缓存资源（`--remove` 或 `-r`）都是完全安全的，可回收磁盘空间，且不会影响你当前使用的 VSView 环境。
        之后如有需要（例如执行 `restore` 时），压缩包会自动重建或重新下载。

    传入 `-r` / `--remove` 可清除指定的缓存资源：

    === "PowerShell (Windows)"

        ```powershell
        # 显示 Python 分发缓存位置
        .\VSView.exe env cache dist

        # 安全删除 Python 分发压缩包以释放空间
        .\VSView.exe env cache dist --remove
        ```

    === "Bash / Zsh (macOS & Linux)"

        ```bash
        # 显示 Python 分发缓存位置
        ./VSView env cache dist

        # 安全删除 Python 分发压缩包以释放空间
        ./VSView env cache dist --remove
        ```

---
## 环境文件（.env）

VSView 启动时会自动查找并加载 `.env` 文件。

查找从<strong>当前工作目录</strong>开始，逐级向上遍历父目录，直到找到 `.env` 文件为止。

设置 `VSVIEW_NO_DOTENV` 可禁用 .env 文件加载。
