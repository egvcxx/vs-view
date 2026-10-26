---
icon: lucide/brush
title: 外观
description: 配置配色方案、控件样式、调色板主题、自定义样式表与图标。
---

# 外观

外观设置用于配置应用的配色方案、控件样式、图标集与自定义样式。

## Settings 对话框

从菜单栏打开外观设置：

- <strong>Settings</strong> > <strong>Appearance</strong>（或按 <kbd>Ctrl</kbd> + <kbd>,</kbd> / <kbd>Cmd</kbd> + <kbd>,</kbd>）

设置会保存到 `global_settings.json`。

<figure markdown="span">
    ![](../assets/appearance_settings.png){ .lightboxOn }
</figure>

---

## 选项

### Color Scheme（配色方案）

设置操作系统级别的配色方案。

-  <strong>System Default</strong>：跟随操作系统主题。
-  <strong>Light</strong>：强制窗口装饰与菜单使用浅色模式。
-  <strong>Dark</strong>：强制窗口装饰与菜单使用深色模式。

选择 <strong>Light</strong> 或 <strong>Dark</strong> 后，<strong>Palette Theme</strong> 下拉列表会筛选出与之匹配的主题。

---

### Widget Style（控件样式）

设置 Qt 控件样式（例如 `Fusion`、`Windows`）。

!!! tip "推荐样式"

    在使用自定义控件样式时，推荐选择 <strong>Fusion</strong>，
    因为它在所有控件上提供最一致的外观。

---

### Palette Theme（调色板主题）

为整个界面应用一套配色。以下示例均使用 Fusion 控件样式。

=== "Stock（默认）"

    <figure markdown="span">
        ![](../assets/palette_theme/stock_light.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/stock_dark.png#only-dark){ .lightboxOn }
    </figure>

=== "Adwaita"

    <figure markdown="span">
        ![](../assets/palette_theme/adwaita_light.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/adwaita_dark.png#only-dark){ .lightboxOn }
    </figure>

=== "Atom One Dark"

    <figure markdown="span">
        ![](../assets/palette_theme/atom_one.png){ .lightboxOn }
    </figure>

=== "Ayu"

    <figure markdown="span">
        ![](../assets/palette_theme/ayu_light.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/ayu_dark.png#only-dark){ .lightboxOn }
    </figure>

=== "Ayu Mirage"

    <figure markdown="span">
        ![](../assets/palette_theme/ayu_mirage.png){ .lightboxOn }
    </figure>

=== "Blender Dark"

    <figure markdown="span">
        ![](../assets/palette_theme/blender.png){ .lightboxOn }
    </figure>

=== "Breeze"

    <figure markdown="span">
        ![](../assets/palette_theme/breeze_light.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/breeze_dark.png#only-dark){ .lightboxOn }
    </figure>

=== "Catppuccin Frappé"

    <figure markdown="span">
        ![](../assets/palette_theme/catppuccin_frappe.png){ .lightboxOn }
    </figure>

=== "Catppuccin Macchiato"

    <figure markdown="span">
        ![](../assets/palette_theme/catppuccin_macchiato.png){ .lightboxOn }
    </figure>

=== "Catppuccin Mocha"

    <figure markdown="span">
        ![](../assets/palette_theme/catppuccin_latte.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/catppuccin_mocha.png#only-dark){ .lightboxOn }
    </figure>

=== "Dracula"

    <figure markdown="span">
        ![](../assets/palette_theme/dracula.png){ .lightboxOn }
    </figure>

=== "Everforest"

    <figure markdown="span">
        ![](../assets/palette_theme/everforest_light.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/everforest_dark.png#only-dark){ .lightboxOn }
    </figure>

=== "GitHub"

    <figure markdown="span">
        ![](../assets/palette_theme/github_light.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/github_dark.png#only-dark){ .lightboxOn }
    </figure>

=== "Gruvbox"

    <figure markdown="span">
        ![](../assets/palette_theme/gruvbox_light.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/gruvbox_dark.png#only-dark){ .lightboxOn }
    </figure>

=== "Kanagawa"

    <figure markdown="span">
        ![](../assets/palette_theme/kanagawa_lotus.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/kanagawa_wave.png#only-dark){ .lightboxOn }
    </figure>

=== "Kanagawa Dragon"

    <figure markdown="span">
        ![](../assets/palette_theme/kanagawa_dragon.png){ .lightboxOn }
    </figure>

=== "Modern"

    <figure markdown="span">
        ![](../assets/palette_theme/modern_light.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/modern_dark.png#only-dark){ .lightboxOn }
    </figure>

=== "Monokai"

    <figure markdown="span">
        ![](../assets/palette_theme/monokai.png){ .lightboxOn }
    </figure>

=== "Nord"

    <figure markdown="span">
        ![](../assets/palette_theme/nord.png){ .lightboxOn }
    </figure>

=== "One Dark Two"

    <figure markdown="span">
        ![](../assets/palette_theme/one_dark_two.png){ .lightboxOn }
    </figure>

=== "Rosé Pine"

    <figure markdown="span">
        ![](../assets/palette_theme/rose_pine_dawn.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/rose_pine.png#only-dark){ .lightboxOn }
    </figure>

=== "Rosé Pine Moon"

    <figure markdown="span">
        ![](../assets/palette_theme/rose_pine_moon.png){ .lightboxOn }
    </figure>

=== "Solarized"

    <figure markdown="span">
        ![](../assets/palette_theme/solarized_light.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/solarized_dark.png#only-dark){ .lightboxOn }
    </figure>

=== "Tokyo Night"

    <figure markdown="span">
        ![](../assets/palette_theme/tokyo_night_day.png#only-light){ .lightboxOn }
        ![](../assets/palette_theme/tokyo_night.png#only-dark){ .lightboxOn }
    </figure>

=== "Tokyo Night Storm"

    <figure markdown="span">
        ![](../assets/palette_theme/tokyo_night_storm.png){ .lightboxOn }
    </figure>

---

### Custom Stylesheet（自定义样式表）

在当前样式与调色板之上应用自定义 Qt 样式表（`.qss`）文件。留空表示禁用。

---

### Icons（图标）

- <strong>Icon Provider</strong>：选择图标集。
- <strong>Icon Weight</strong>：设置描边粗细。可选粗细取决于所选的图标提供方。

---

## 自定义主题

自定义 JSON 主题可以放在设置目录下的 `themes` 目录中：

=== "Windows"

    ```text
    %LOCALAPPDATA%\vsview\themes\
    ```

=== "Linux"

    ```text
    ~/.config/vsview/themes/
    ```

=== "macOS"

    ```text
    ~/Library/Application Support/vsview/themes/
    ```

运行 `vsview config path` 可打印当前生效的设置目录。

### 格式

```json title="custom_theme.json"
{
  "id": "custom_dark",
  "name": "Custom Dark",
  "scheme": "dark",
  "palette": {
    "base": "#1e1e2e",
    "mantle": "#181825",
    "crust": "#11111b",
    "surface0": "#313244",
    "surface1": "#45475a",
    "surface2": "#585b70",
    "overlay0": "#6c7086",
    "overlay1": "#7f849c",
    "overlay2": "#9399b2",
    "text": "#cdd6f4",
    "primary": "#89b4fa",
    "secondary": "#f5c2e7",
    "tertiary": "#94e2d5",
    "info": "#89dceb",
    "success": "#a6e3a1",
    "warning": "#f9e2af",
    "danger": "#f38ba8"
  }
}
```

该目录中的主题会在启动时自动加载。
