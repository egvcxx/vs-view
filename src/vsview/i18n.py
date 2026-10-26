"""Minimal, opt-in translation layer for VSView's user interface.

The upstream project has no i18n infrastructure: user-facing strings are hardcoded
in the source. This module adds a small, dependency-free lookup layer that is keyed
by the English source string, in the spirit of ``gettext``::

    from vsview.i18n import tr

    button.setText(tr("Load Script..."))

Untranslated or missing entries fall back to the English source string, so a
partial catalog is always safe to ship.

Language selection
------------------
The active language is read from the ``VSVIEW_LANG`` environment variable when
:func:`set_language` is called::

    VSVIEW_LANG=zh_CN vsview script.vpy

Accepted values are catalog codes (``zh_CN``) plus a few aliases (``zh``,
``zh-Hans``, ...). The default is ``en``, which keeps upstream behavior unchanged.

Adding a language
-----------------
Drop a JSON file into ``vsview/locales/`` named after the language code, mapping
English source strings to translations::

    {
        "Load Script...": "载入脚本…"
    }

Then extend :data:`_LANGUAGE_ALIASES` if the code has common short forms.

Notes
-----
* Lookups are exact-match on the English text; duplicated English strings share
  one translation.
* Strings containing ``{}`` placeholders are formatted by the caller after
  translation, so keep the same number of placeholders in the value.
* Language is applied at lookup time, so it can be changed at runtime; call
  :func:`set_language` again after switching.
"""

from __future__ import annotations

import json
import os
from functools import cache
from typing import Final

__all__ = ["available_languages", "get_language", "set_language", "tr"]

DEFAULT_LANGUAGE: Final = "en"
CATALOG_DIR: Final = os.path.join(os.path.dirname(__file__), "locales")
ENV_VAR: Final = "VSVIEW_LANG"

#: Alternative spellings mapped to a catalog code.
_LANGUAGE_ALIASES: Final[dict[str, str]] = {
    "zh": "zh_CN",
    "zh_cn": "zh_CN",
    "zh_hans": "zh_CN",
    "zh-hans": "zh_CN",
    "zh_sg": "zh_CN",
    "zh-sg": "zh_CN",
}

_current_language: str = DEFAULT_LANGUAGE
_catalog: dict[str, str] = {}


@cache
def available_languages() -> tuple[str, ...]:
    """Return the default language plus every language with a catalog."""
    try:
        codes = sorted(
            name[:-5] for name in os.listdir(CATALOG_DIR) if name.endswith(".json") and name != "en.json"
        )
    except OSError:
        codes = []

    return (DEFAULT_LANGUAGE, *codes)


def normalize_language(code: str | None) -> str:
    """Normalize a language code to a catalog code, falling back to the default."""
    if not code:
        return DEFAULT_LANGUAGE

    key = code.strip().replace("-", "_").lower()
    key = _LANGUAGE_ALIASES.get(key, key)

    return key if key in available_languages() else DEFAULT_LANGUAGE


@cache
def _load_catalog(language: str) -> dict[str, str]:
    if language == DEFAULT_LANGUAGE:
        return {}

    path = os.path.join(CATALOG_DIR, f"{language}.json")
    try:
        with open(path, encoding="utf-8") as file:
            catalog = json.load(file)
    except (OSError, ValueError):
        return {}

    if not isinstance(catalog, dict):
        return {}

    return {str(key): str(value) for key, value in catalog.items() if isinstance(value, str) and value}


def get_language() -> str:
    """Return the currently active language code."""
    return _current_language


def set_language(code: str | None = None) -> str:
    """
    Activate a language and return the resolved code.

    If *code* is ``None``, the ``VSVIEW_LANG`` environment variable is used.
    Unknown or missing catalogs fall back to English.
    """
    global _catalog, _current_language

    if code is None:
        code = os.environ.get(ENV_VAR)

    _current_language = normalize_language(code)
    _catalog = _load_catalog(_current_language)

    return _current_language


def tr(text: str) -> str:
    """Translate an English UI string to the active language."""
    return _catalog.get(text, text)
