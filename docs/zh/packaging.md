---
icon: lucide/box
title: 打包与分发
description: 独立应用打包、PyApp 引导器与分发指南。
---

# 打包与分发

VSView 使用 [PyApp](https://github.com/Varde-s-Forks/pyapp) 为 Windows、Linux 与 macOS 构建独立、自安装的可执行文件。

项目提供了一个自定义命令行工具 `vsapp`，用于简化 wheel 生成、离线 Python 分发打包、图标生成以及 macOS 应用打包。

## 前置条件

要构建独立应用，需要安装以下工具并确保它们位于 `PATH` 中：

- <strong>Python 3.14</strong> 或更高版本。
- <strong>[Rust 与 Cargo](https://rustup.rs/)</strong>：编译 `PyApp` 引导器所需。
- <strong>Git 子模块</strong>：PyApp 源码位于 `submodules/pyapp`。请确保子模块已初始化：
  ```bash
  git submodule update --init --recursive submodules/pyapp
  ```
- <strong>[ImageMagick 7](https://imagemagick.org/)</strong>（可选）：`vsapp icon` 命令生成跨平台图标集时需要。
- <strong>[iconutil](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/DrawingWithQuartz2D/dq_images/dq_images.html)</strong>：（<strong>仅 macOS</strong>）创建 App Bundle（`.app`）与 Macintosh 图标（`.icns`）时需要。

---

## `vsapp` 命令行工具

打包逻辑位于 `vsview-pyapp` 包中（`src/pyapp`）。请确保你的工作区环境已同步：

```bash
uv sync
```

随后即可通过 `uv` 运行该命令行工具：

```bash
uv run vsapp --help
```

### 1. 生成图标

`vsapp icon` 命令会处理一张源图片，并生成适用于 Windows、macOS 与 Linux 的图标格式。

```bash
uv run vsapp icon [OPTIONS] [SOURCE_IMAGE]
```

- <strong>格式</strong>：
    - <strong>Windows</strong>：`vsview.ico`（多尺寸图标）
    - <strong>macOS</strong>：`vsview.iconset/`（供 `iconutil` 转换）
    - <strong>Linux</strong>：标准尺寸的 PNG（`16x16`、`32x32` 等）

!!! info "预生成图标"

    仓库中已包含预生成的图标，位于 [`src/pyapp/icons/`](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/pyapp/icons/)。

### 2. 构建可执行文件

`vsapp build` 命令会自动打包工作区的 wheel、配置 PyApp 环境并编译 Rust 引导器。

```bash
uv run vsapp build [OPTIONS]
```

#### 构建模式

`vsapp` 支持两种不同的构建模式：

=== "在线（轻量）"

    构建一个轻量的 `VSView` 可执行文件。
    首次运行时，可执行文件会使用 `uv` 从 PyPI / 索引服务器动态获取并安装 `vsview` 及其依赖。

    ```bash
    uv run vsapp build
    ```

=== "离线（自包含）"

    构建完全自包含的 `VSView-offline` 可执行文件，内嵌 Python 3.14 运行时与预装的工作区 wheel。
    运行时无需联网，也无需本地安装 Python。

    ```bash
    uv run vsapp build --offline
    ```

### 3. macOS 应用打包与磁盘映像

在 macOS 上，应用以 `.app` bundle 或磁盘映像（`.dmg`）形式分发。

#### 生成 App Bundle

`vsapp bundle` 命令会构建标准 macOS bundle 结构，并使用 `iconutil` 将 `.iconset` 转换为 `.icns` 文件。

```bash
uv run vsapp bundle SOURCE VERSION [OPTIONS]
```

- 使用 `iconutil` 将 `vsapp icon` 生成的 iconset 转换为 `.icns` 文件。
- 创建标准 macOS bundle 结构（`Contents/MacOS`、`Contents/Resources`）。
- 生成有效的 `Info.plist`。

#### 创建 DMG 安装包

要把构建好的 `.app` bundle 打包为带有 `/Applications` 快捷方式的可分发的磁盘映像：

```bash
mkdir dmg_staging
ditto dist/AppBundle dmg_staging/VSView.app
ln -s /Applications dmg_staging/Applications

hdiutil create -volname VSView -srcfolder dmg_staging -ov -format UDZO dist/VSView.dmg
```

---

## 配置

`vsapp` 工具会从 `--env` 指定的 `.env` 文件读取配置（默认使用 [`src/pyapp/.env.example`](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/pyapp/.env.example)）。
