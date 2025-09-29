import os
import shutil
import sys
from importlib.resources import as_file, files
from logging import getLogger
from pathlib import Path

log = getLogger(__name__)


def require_java():
    if shutil.which("java"):
        return

    sys.exit(
        "Error: Java runtime not found on PATH. Please install Java (e.g., OpenJDK) and retry."
    )


def _get_cache_dir() -> Path:
    cache_dir = (
        Path(os.getenv("XDG_CACHE_HOME", Path.home() / ".cache")) / "dash-license-scan"
    )
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


def get_jar() -> Path:
    res = files("dash_license_scan.resources") / "org.eclipse.dash.licenses-1.1.0.jar"
    with as_file(res) as p:
        return p

