---
icon: lucide/git-pull-request
---

# 贡献指南

## 开发环境安装

### 环境要求

- <strong>[uv](https://github.com/astral-sh/uv)</strong> 是本仓库默认使用的开发工具。
- 构建 [`vspackrgb`](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/vspackrgb) 与 [`vsview-histogram`](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/plugins/histogram) 需要 [Cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html)。
- 构建 [`vsview-editor`](https://github.com/Jaded-Encoding-Thaumaturgy/vs-view/tree/main/src/workspaces/editor) 需要 [npm](https://www.npmjs.com/)。
---

克隆仓库并同步所有包：

```bash
git clone --recurse-submodules https://github.com/Jaded-Encoding-Thaumaturgy/vs-view.git
cd vs-view
uv sync --all-packages --all-groups --all-extras
```

运行开发版本：

```bash
uv run vsview
```

---

## 打包与分发

VSView 可以使用 [PyApp](https://github.com/Varde-s-Forks/pyapp) 与自定义的 `vsapp` 命令行工具打包为独立可执行文件。

详见 <strong>[打包与分发](packaging.md)</strong> 指南。

---

## 推荐的编辑器设置

### VSCode / VSCodium

下列设置可在整个代码库中统一格式化、类型检查与文件关联行为。

请将以下内容复制到 `vsview/.vscode/settings.json`：

```json title="vsview/.vscode/settings.json"
{
  "[github-actions-workflow]": {
    "editor.defaultFormatter": "oxc.oxc-vscode"
  },
  "[json]": {
    "editor.defaultFormatter": "oxc.oxc-vscode",
    "editor.formatOnSave": true,
    "editor.tabSize": 2
  },
  "[python]": {
    "editor.codeActionsOnSave": {
      "source.organizeImports.ruff": "explicit"
    },
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true
  },
  "[rust]": {
    "editor.defaultFormatter": "rust-lang.rust-analyzer",
    "editor.formatOnSave": true
  },
  "[toml]": {
    "editor.defaultFormatter": "tamasfe.even-better-toml",
    "editor.formatOnSave": true
  },
  "editor.formatOnSave": true,
  "files.associations": {
    "*.vpy": "python",
    "**/.github/actions/**/action.yml": "github-actions-workflow",
    "**/.github/workflows/*.yml": "github-actions-workflow"
  },
  "mypy-type-checker.importStrategy": "fromEnvironment",
  "oxc.enable.oxfmt": true,
  "oxc.enable.oxlint": true,
  "python.analysis.autoFormatStrings": true,
  "python.analysis.autoImportCompletions": true,
  "python.analysis.packageIndexDepths": [
    {
      "depth": 2,
      "name": "PySide6"
    }
  ],
  "python.analysis.stubPath": "stubs",
  "python.analysis.typeCheckingMode": "standard",
  "python.analysis.typeEvaluation.deprecateTypingAliases": true,
  "python.analysis.typeEvaluation.enableReachabilityAnalysis": true,
  "python.testing.pytestArgs": ["."],
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "rust-analyzer.check.command": "clippy",
  "rust-analyzer.linkedProjects": [
    "src/vspackrgb/Cargo.toml",
    "src/plugins/histogram/src/rust/Cargo.toml"
  ],
  "search.exclude": {
    "**/submodules": true
  },
  "vitest.debugExclude": ["submodules:**", "<node_internals>/**"],
  "vitest.rootConfig": "src/workspaces/editor",
  "vsstubs.watchPlugins": false,
  "yaml.schemas": {
    "https://www.schemastore.org/github-action.json": "**/.github/actions/**/*.yml"
  }
}
```
