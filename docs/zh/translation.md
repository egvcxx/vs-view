---
icon: lucide/languages
title: 关于本翻译
---

# 关于本翻译

本页说明这份简体中文文档的范围、约定、同步方式与许可。

!!! warning "非官方翻译"

    本翻译由社区维护，<strong>不是</strong> VSView 官方文档。

    上游项目：[Jaded-Encoding-Thaumaturgy/vs-view](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view) ·
    英文原文：[jaded-encoding-thaumaturgy.github.io/vs-view](https://jaded-encoding-thaumaturgy.github.io/vs-view/)

    遇到与英文原文不一致之处，<strong>以英文原文为准</strong>。

## 翻译基线

- 对应上游提交：[`f30eb89`](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/commit/f30eb89)（`cli: add config path management commands`）
- 对应上游分支：`main`
- 基线日期：2026-10-21

文档更新频繁，本翻译不承诺与上游实时同步。

## 翻译范围

| 内容 | 是否翻译 | 说明 |
| :--- | :------- | :--- |
| 使用文档、安装、配置、插件介绍 | 是 | 全部页面 |
| 导航与页面标题 | 是 | `zensical.zh.toml` 中的 `nav` |
| 页面内截图 | 否 | 沿用英文截图，图中界面为英文 |
| API 参考页正文 | 否 | 由 `mkdocstrings` 从源码 docstring 生成，保留英文更利于对照 |
| API 参考页的标题与说明 | 是 | 仅翻译页面标题与引导语，`:::` 指令与成员列表不动 |
| 代码块、命令、路径、配置键、标识符 | 否 | 原样保留；注释在不影响复制粘贴的前提下可译为中文 |
| 应用界面文本 | 部分 | 见下文“应用内汉化” |
| 命令行 `--help` 输出 | 否 | 见下文 |
| 日志与异常信息 | 否 | 见下文 |

## 应用内汉化

上游代码目前<strong>没有任何 i18n 基础设施</strong>（无 `QTranslator`、无 `.ts/.qm`、无 `tr()` 包裹、无语言设置项），界面字符串硬编码在 Python 源码中。

本分支因此新增了一个最小化、可选、默认关闭的翻译层：

- `src/vsview/i18n.py`：基于英文原文键的查表翻译，未命中时原样返回英文。
- `src/vsview/locales/zh_CN.json`：翻译目录。
- 语言通过环境变量 `VSVIEW_LANG=zh_CN` 选择；默认仍为英文，因此不改变上游行为。

!!! note "为什么用环境变量而不是设置项"

    新增“语言”设置项需要改动设置模型、默认值、迁移逻辑与设置 UI，属于独立议题。
    在维护者确认方向前，环境变量可以最小化改动面，也便于 A/B 对照。

### 刻意不翻译的部分

- <strong>命令行帮助文本</strong>：`--help` 由 `cyclopts` 从 docstring 与参数声明生成，翻译需要重构 CLI 元数据。开发者在终端中通常也需要与英文文档/issue 中的选项名对照。
- <strong>日志与异常</strong>：保持英文，便于向上游提交 issue、搜索已有报告，也避免翻译破坏日志解析。
- <strong>第三方插件界面</strong>：其字符串不在本仓库中，无法在本分支翻译。
- **`vspackrgb` / `histogram` 的 Rust 部分**：不涉及用户界面文本。

## 术语表

| 英文 | 中文 | 备注 |
| :--- | :--- | :--- |
| workspace | 工作区 | |
| tool dock | 工具停靠面板 | 可停靠窗口 |
| tool panel | 工具面板 | 标签式侧栏 |
| output | 输出 | `set_output` 注册的节点 |
| clip | 片段 | VapourSynth 节点 |
| frame | 帧 | |
| frame properties / frameprops | 帧属性 | |
| timeline | 时间轴 | |
| playhead | 播放头 | |
| notch | 刻度 | 时间轴标记 |
| scening | 场景标记 | 工具名保留原样 |
| region selector | 区域选择器 | 工具名保留原样 |
| color picker | 取色器 | 工具名保留原样 |
| plane | 平面 | 如 Y/U/V 平面 |
| chroma | 色度 | |
| luma | 亮度 | |
| primaries | 原色 | 色彩管理语境 |
| transfer (characteristics) | 传递特性 | |
| matrix | 矩阵 | 色彩矩阵 |
| range | 范围 / 区间 | 视频范围用“范围”，时间轴用“区间” |
| tone mapping | 色调映射 | |
| descale | 反缩放 | |
| kernel | 内核 | 缩放内核 |
| dither | 抖动 | |
| sample type | 采样类型 | |
| shortcut | 快捷键 | |
| settings dialog | Settings 对话框 | 界面名保留英文 |
| bundle (recommended/full) | 合集 | pip extra |

界面元素名（如 `Settings`、`Mark in`、`Levels`）在正文中保留英文，避免与截图不一致。启用中文界面后，应用内会显示对应中文文本（例如 `Settings` 显示为“设置”），对照时请以英文原文与上方术语表为准。

## 同步与维护

1. 拉取上游 `main`，对比 `docs/` 的变更：

    ```bash
    git fetch upstream
    git diff --stat upstream/main -- docs/
    ```

2. 对发生变更的英文页面，更新 `docs/zh/` 中对应文件。
3. 更新本页“翻译基线”中的提交号与日期。
4. 重新构建并检查：

    ```bash
    python scripts/build_docs_i18n.py
    ```

## 许可

本翻译与上游一致，采用 <strong>EUPL-1.2</strong> 许可。原始文档版权归 Jaded Encoding Thaumaturgy 所有。

## 已知的上游文档问题

翻译时发现但<strong>未擅自修改</strong>的原文问题，供上游参考：

- `docs/usage/workspaces/workspace.md` 列出四种工作区，但正文写 “applies to all three”。
- `docs/plugins/first-party.md` 中 Audio Convert 一节写 “target bidepth”，应为 “bit depth”。
- `docs/installation.md` 的 Linux 示例命令写作 `/VSView env pip install ...`，缺少可执行文件的相对路径前缀（同一页其他示例使用 `./VSView`）。

## 反馈

- 文档翻译问题：请在本仓库提交 issue。
- VSView 本身的问题：请提交到[上游仓库](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/issues)。
