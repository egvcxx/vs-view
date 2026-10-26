# VSView 简体中文本地化（审阅版）

本目录是对 [Jaded-Encoding-Thaumaturgy/vs-view](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view) 的**本地**简体中文翻译工作区，用于在提交上游之前审阅翻译质量与实现方式。

- 基线提交：`f30eb89`（`cli: add config path management commands`），分支 `main`
- 当前状态：**全部改动均未提交、未推送到任何远程仓库**
- 许可：跟随上游 **EUPL-1.2**；译文为非官方社区翻译

---

## 1. 快速预览

### 文档站点

```bash
# 需要在仓库根目录执行；.venv-docs 内已安装 zensical 与 mkdocstrings
python scripts/build_docs_i18n.py
```

产物：

- 英文站：`site/`
- 中文站：`site/zh/`
- 两个站点互相提供语言切换入口（`alternate`）

本地预览（英文 + 中文一起构建并启动服务）：

```bash
python scripts/build_docs_i18n.py --serve
```

只构建中文站（调试用）：

```bash
python scripts/build_docs_i18n.py --zh-only
```

### 中文界面

应用内翻译是**可选、默认关闭**的，通过环境变量启用：

```powershell
$env:VSVIEW_LANG = "zh_CN"
vsview path\to\script.vpy
```

```bash
VSVIEW_LANG=zh_CN vsview path/to/script.vpy
```

不设置该变量时行为与上游完全一致（英文）。

---

## 2. 分层落地

| 层 | 范围 | 状态 | 说明 |
| :--- | :--- | :--- | :--- |
| 文档 | `docs/zh/**`（25 个上游页面 + 1 个说明页） | 全部翻译 | 与 `docs/` 目录结构一一对应 |
| 站点配置 | `zensical.zh.toml`、`zensical.toml` | 完成 | 独立 `docs_dir`/`site_dir`/`language`/`nav`，并加语言切换 |
| 构建脚本 | `scripts/build_docs_i18n.py` | 完成 | 复制共享静态资源，先英文后中文 |
| 应用界面 | 菜单、状态栏、时间轴、设置对话框、工具面板、第一方插件 | 主要可见文本 | 约 180 处调用点，398 条词条 |
| CLI / 日志 / 异常 | `--help`、日志、报错文本 | 不翻译 | 便于与上游文档、issue 对照 |
| API 文档正文 | `:::` mkdocstrings 生成内容 | 不翻译 | 仅翻译页面标题与引导语 |
| 第三方插件 | 不在本仓库 | 不翻译 | 词条缺失时自动回退英文 |

---

## 3. 文档翻译

- 目录：`docs/zh/` 与上游 `docs/` 完全对齐，包含安装、使用、配置、插件、开发、贡献等页面。
- 导航：由 `zensical.zh.toml` 的 `nav` 提供中文标题，`language = "zh"`。
- 语言切换：两个配置都使用 `alternate` 链接（中文站 → `/`，英文站 → `/zh/`）。
- 共享资源：图片、样式等通过构建脚本复制到 `docs/zh/`，并由 `docs/zh/.gitignore` 排除复制产物。
- 锚点：Zensical 0.0.71 的标题 ID 只保留 ASCII 词，因此被链接引用的标题保留英文括注，例如
  `## 安装（Installation）` → `#installation`。
- 说明页：`docs/zh/translation.md` 记录了翻译范围、术语表、同步流程、上游文档的已知问题与许可信息。

### 构建验证

`python scripts/build_docs_i18n.py` 对英文与中文均输出 `No issues found`。
（该命令的进度信息写入 stderr，PowerShell 中即使成功也可能显示退出码 1，以输出内容为准。）

---

## 4. 应用内汉化

上游目前**没有任何 i18n 基础设施**（无 `QTranslator`、无 `.ts/.qm`、无 `tr()`、无语言设置项）。本分支添加了一个最小化、无第三方依赖的翻译层：

| 文件 | 作用 |
| :--- | :--- |
| `src/vsview/i18n.py` | `tr()` / `set_language()` / `get_language()`，英文原文作为键，缺失时回退英文 |
| `src/vsview/locales/zh_CN.json` | 398 条词条 |
| `src/vsview/cli.py` | 在 `main_meta()` 中于任何窗口/插件导入之前调用 `set_language()` |
| `tests/i18n/test_i18n.py` | 14 项测试：默认英文、别名解析、词条完整性、占位符一致性、`tr()` 字面量覆盖率 |

设计要点：

- **默认英文**：不设置 `VSVIEW_LANG` 时行为不变，便于上游评估。
- **原文键**：不引入消息 ID，避免维护两套键；重复英文共享同一条译文。
- **显示层收口**：设置项标签与提示集中在 `settings/dialog.py` 与 `settings/metadata.py` 翻译，而不是逐条修改 `label=`/`tooltip=` 定义，减少与上游冲突。
- **运行时切换**：语言在查找时生效，测试中可反复切换。

---

## 5. 未翻译 / 已知缺口

| 项目 | 原因 |
| :--- | :--- |
| `--help` 与 CLI 参数说明 | 由 cyclopts + docstring 生成，翻译需重写 CLI 元数据；开发者也需与英文选项名对照 |
| 日志、异常回溯 | 便于搜索上游 issue、保持日志可解析 |
| API 参考页正文 | mkdocstrings 直接读取英文 docstring |
| 第三方插件字符串 | 不在本仓库 |
| Qt 内置文本（文件对话框、标准按钮） | 依赖 Qt 自带翻译；设置对话框的 OK/Cancel/Apply 已显式翻译 |
| 快捷键分组名（如 `appearance`） | 由 action ID 推导，属于内部标识；如需翻译需引入映射表 |
| 部分多行拼接的工具提示 | 少数跨行字符串尚未包裹，回退英文 |
| 截图 | 沿用上游英文截图 |
| 应用内插件自带属性名（如帧属性分类名） | 已接入 `tr()`，但未提供词条，回退英文 |

文档正文中引用的界面元素名保留英文（如 `Settings`、`Mark in`、`Levels`），以便与截图对照；启用中文界面后应用内会显示中文，例如 `Settings` → “设置”。

---

## 6. 与上游协作的建议

若维护者接受文档翻译，需要先确认采用哪种形态：

- **方案 A：上游内置中文站** —— 合并 `docs/zh/**`、`zensical.zh.toml` 与构建脚本，加入语言切换。
- **方案 B：社区独立站点** —— 本仓库只保留译文，由社区部署，并在页首标注“非官方翻译”。

需要在 issue 中说明的限制：

1. Zensical 0.0.71 没有逐页 i18n，只能整站复制一套 `docs/zh`。
2. mkdocstrings 生成的 API 页面正文保持英文。
3. 译文存在滞后，需要约定每页的“基线提交”。
4. 上游 Pages 工作流带有 `if: github.repository_owner == 'Jaded-Encoding-Thaumaturgy'` 守卫，fork 不会自动部署，需要改 `site_url` 与部署条件。
5. 应用内 i18n 是否接受“环境变量 + 原文键”的最小方案，或希望改为 Qt `QTranslator`。

---

## 7. 验证记录

| 检查 | 结果 |
| :--- | :--- |
| `python scripts/build_docs_i18n.py` | 英文、中文均 `No issues found` |
| `python -m compileall src` | 通过 |
| `ruff check src tests/i18n` | `All checks passed!` |
| `pytest tests/i18n` | 14 passed |
| 词条占位符一致性 | `{}` 数量逐条比对通过 |
| `tr()` 字面量覆盖 | 所有单行字面量均在词条表中 |

图形界面无法在当前环境无头运行（缺少 VapourSynth 运行时），界面验证为静态检查：导入、编译、词条覆盖与测试。

---

## 8. 审阅清单

建议重点审阅：

1. **术语一致性**：工作区 / 输出 / 片段 / 平面 / 色度 / 亮度 / 刻度 等译法是否统一。
2. **标签长度**：设置面板与时间轴菜单中的中文是否过长（截图或本地运行确认）。
3. **技术模式名**：`Density`、`Chroma Wheel`、`Pixel Color` 等已译为“密度 / 色度轮 / 像素颜色”，是否需要保留英文。
4. **语气**：提示文本采用简洁书面语，是否需要更口语化。
5. **是否接受环境变量开关**，还是希望增加“设置 → 语言”选项。
6. **文档页脚与许可声明**是否符合预期。

审阅通过后，再决定是否 fork、提交 issue 或发起 PR。
