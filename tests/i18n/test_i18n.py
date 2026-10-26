from __future__ import annotations

import ast
import json
import os
import re
from pathlib import Path

import pytest

from vsview.i18n import available_languages, get_language, normalize_language, set_language, tr

SRC_ROOT = Path(__file__).resolve().parents[2] / "src"
CATALOG_PATH = SRC_ROOT / "vsview" / "locales" / "zh_CN.json"
PLACEHOLDER = re.compile(r"\{\}")
#: Terms of art that are intentionally kept as-is in Chinese UIs.
ALLOW_IDENTICAL = {"NSFW"}


@pytest.fixture(autouse=True)
def _reset_language() -> None:
    set_language("en")


def test_default_language_is_english() -> None:
    assert get_language() == "en"
    assert tr("Settings") == "Settings"
    assert tr("Not in the catalog") == "Not in the catalog"


def test_chinese_catalog_loads(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("VSVIEW_LANG", "zh_CN")

    assert set_language() == "zh_CN"
    assert get_language() == "zh_CN"
    assert tr("Settings") == "设置"
    assert tr("This string is not translated") == "This string is not translated"


@pytest.mark.parametrize("code", ["zh", "zh-Hans", "zh-hans", "ZH_cn"])
def test_language_aliases(code: str) -> None:
    assert set_language(code) == "zh_CN"


@pytest.mark.parametrize("code", ["en", "de", "", "klingon"])
def test_unknown_languages_fall_back_to_english(code: str) -> None:
    assert normalize_language(code) == "en"
    assert set_language(code) == "en"


def test_catalog_discovery() -> None:
    assert "en" in available_languages()
    assert "zh_CN" in available_languages()


def test_catalog_values_are_translated() -> None:
    catalog: dict[str, str] = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))

    assert catalog, "catalog is empty"

    for source, target in catalog.items():
        assert source, "empty source key"
        assert target.strip(), f"empty translation for {source!r}"
        assert target != source or source in ALLOW_IDENTICAL, f"untranslated entry for {source!r}"
        assert len(PLACEHOLDER.findall(target)) == len(PLACEHOLDER.findall(source)), (
            f"placeholder mismatch for {source!r}: {target!r}"
        )


def test_every_tr_literal_is_in_the_catalog() -> None:
    """Guard against wrapping a string without adding it to the catalog."""
    catalog: dict[str, str] = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))

    def is_untranslated_tr_call(node: ast.AST) -> bool:
        return (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "tr"
            and len(node.args) == 1
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
            and node.args[0].value not in catalog
        )

    missing = [
        f"{path.relative_to(SRC_ROOT)}:{node.lineno}: {node.args[0].value!r}"  # type: ignore[attr-defined]
        for path in SRC_ROOT.rglob("*.py")
        if path.name != "i18n.py"
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"), filename=str(path)))
        if is_untranslated_tr_call(node)
    ]

    assert not missing, "missing catalog entries:\n" + "\n".join(missing)


def test_env_var_reads_at_startup(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("VSVIEW_LANG", "zh")
    set_language()
    assert get_language() == "zh_CN"

    del os.environ["VSVIEW_LANG"]
    set_language()
    assert get_language() == "en"
