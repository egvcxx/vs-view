#!/usr/bin/env python3
"""Build the English documentation and the Simplified Chinese translation.

Zensical has no per-page i18n: a site has exactly one canonical language, and
other languages are linked through ``[project.extra].alternate``. The Chinese
docs therefore live in ``docs/zh`` and are built as a second site into
``site/zh`` so that the combined output can be served from a single domain.

Shared, non-translated assets (images, stylesheets, JS, template overrides) are
copied from ``docs`` into ``docs/zh`` before the second build; those copies are
git-ignored.

Usage:
    python scripts/build_docs_i18n.py            # build en + zh
    python scripts/build_docs_i18n.py --serve    # build, then serve site/
    python scripts/build_docs_i18n.py --zh-only  # skip the english build
"""

from __future__ import annotations

import argparse
import http.server
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
ZH_DOCS = DOCS / "zh"
EN_SITE = ROOT / "site"
ZH_SITE = EN_SITE / "zh"
SHARED_DIRS = ("assets", "stylesheets", "javascripts", "overrides")
SHARED_FILES = ("vs_fixed.inv",)


def zensical() -> str:
    """Return the zensical executable, preferring the local docs venv."""
    candidates = [
        ROOT / ".venv-docs" / ("Scripts/zensical.exe" if sys.platform == "win32" else "bin/zensical"),
        ROOT / ".venv" / ("Scripts/zensical.exe" if sys.platform == "win32" else "bin/zensical"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)

    found = shutil.which("zensical")
    if found is None:
        sys.exit("zensical not found: install it with `uv pip install zensical 'mkdocstrings[python]'`")

    return found


def copy_shared_assets() -> None:
    """Mirror non-translated doc assets into docs/zh."""
    for name in SHARED_DIRS:
        src = DOCS / name
        if not src.exists():
            continue
        dst = ZH_DOCS / name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)

    for name in SHARED_FILES:
        src = DOCS / name
        if src.exists():
            shutil.copy2(src, ZH_DOCS / name)


def build(config: Path, clean: bool) -> None:
    cmd = [zensical(), "build", "-f", str(config)]
    if clean:
        cmd.append("--clean")
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=ROOT, check=True)


def check() -> None:
    """Fail if the expected output trees are missing."""
    expected = [EN_SITE / "index.html", EN_SITE / "zh" / "index.html"]
    overview = ZH_SITE / "usage" / "overview.html"
    if not overview.exists():
        overview = ZH_SITE / "usage" / "overview" / "index.html"
    expected.append(overview)
    missing = [str(p.relative_to(ROOT)) for p in expected if not p.exists()]
    if missing:
        sys.exit(f"missing build output: {', '.join(missing)}")
    print(f"ok: {EN_SITE.relative_to(ROOT)}/ (en) + {ZH_SITE.relative_to(ROOT)}/ (zh)")


def serve(port: int) -> None:
    handler = http.server.SimpleHTTPRequestHandler
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), lambda *a, **kw: handler(*a, directory=str(EN_SITE), **kw)) as httpd:
        print(f"serving http://127.0.0.1:{port}/  (中文: /zh/)")
        httpd.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serve", action="store_true", help="serve site/ after building")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--zh-only", action="store_true", help="only build the chinese site")
    args = parser.parse_args()

    copy_shared_assets()

    if not args.zh_only:
        build(ROOT / "zensical.toml", clean=True)
    build(ROOT / "zensical.zh.toml", clean=True)

    check()

    if args.serve:
        serve(args.port)


if __name__ == "__main__":
    main()
