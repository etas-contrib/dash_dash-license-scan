
from collections.abc import Sequence
from pathlib import Path
import sys


def parse_pypi(files: Sequence[Path]):

    deps: list[str] = []

    for file in files:
        assert isinstance(file, Path), f"Expected Path, got <{type(file)}> {file}"

        if not file.exists():
            sys.exit(f"pip requirements file not found: {file}")
        
        for line in file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if "==" in line:
                name, _, version = line.strip("\\ ").partition("==")
                deps.append(f"pypi/pypi/-/{name}/{version}")

    return deps

def parse_crate(files: Sequence[Path]):
    deps: list[str] = []
    for file in files:
        assert isinstance(file, Path), f"Expected Path, got <{type(file)}> {file}"

        if not file.exists():
            sys.exit(f"crate lockfile not found: {file}")

        text = file.read_text(encoding="utf-8")

        # Split into [[package]] blocks and parse simple key=value lines into a dict.
        for block in text.split("[[package]]"):
            block = block.strip()
            if not block:
                continue

            fields: dict[str, str] = {}
            for line in block.splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                fields[k.strip()] = v.strip().strip('"')

            name = fields.get("name")
            version = fields.get("version")
            source = fields.get("source")

            if not (name and version):
                continue

            # Only crates.io is supported today; detect via presence of 'crates' in source.
            if source and "crates" not in source.lower():
                raise ValueError(f"Unknown crate registry source: {source}")

            deps.append(f"crate/cratesio/-/{name}/{version}")

    return deps
