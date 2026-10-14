"""Build the docs into site/, leaving out sections disabled in settings.yml."""

import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml

root = Path(__file__).resolve().parent
abschnitte = yaml.safe_load((root / "settings.yml").read_text())["abschnitte"]

# Build in a copy so the sources stay untouched
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    for name in ["zensical.toml", "settings.yml", "overrides", "docs"]:
        src = root / name
        if src.is_dir():
            shutil.copytree(src, tmp / name)
        else:
            shutil.copy(src, tmp / name)

    index = tmp / "docs" / "index.md"
    for name, aktiv in abschnitte.items():
        if not aktiv:
            shutil.rmtree(tmp / "docs" / name)
            # Drop start page links into the removed section
            zeilen = index.read_text().splitlines(keepends=True)
            index.write_text("".join(z for z in zeilen if f"]({name}/" not in z))

    subprocess.run(["zensical", "build", "--strict"], cwd=tmp, check=True)
    shutil.rmtree(root / "site", ignore_errors=True)
    shutil.move(tmp / "site", root / "site")
