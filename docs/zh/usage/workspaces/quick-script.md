---
icon: lucide/file-code
---

# 快速脚本

<strong>快速脚本</strong>工作区用于测试与实验。它无需创建脚本文件，即可编写并执行 VapourSynth 代码。

通用工作区布局与查看器控件请参阅[工作区概览](workspace.md)。

## 内置代码编辑器

编辑器是一个<strong>可停靠控件</strong>，可以移动、浮动，或停靠到工作区的不同侧边。

### 工具栏操作

- :lucide-play: <strong>Run script</strong>（++f5++ 或 ++ctrl+r++）：执行代码。如果脚本已在运行，则会触发重新加载。
- :lucide-save: <strong>Save script to file</strong>：将当前代码导出为 `.vpy` 文件。

### 主题与自定义

编辑器的外观可在设置的 <strong>Appearance</strong> 部分配置：

- <strong>Editor Themes</strong>：直接取自 <strong>Pygments</strong>。向环境中添加更多 Pygments 样式即可扩展可用主题。
- <strong>UI Elements</strong>：语法高亮、行号与当前行指示会随所选主题自动调整。

### 快捷键

| 操作             | 快捷键               | 说明                 |
| :--------------- | :------------------- | :------------------- |
| <strong>Run / Reload</strong> | ++f5++ 或 ++ctrl+r++ | 执行代码。           |
| <strong>Zoom In/Out</strong>  | ++ctrl++ + <strong>Wheel</strong> | 调整字体大小。       |
