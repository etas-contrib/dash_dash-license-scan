from __future__ import annotations

import logging
import sys

from dash_license_scan import jar
from dash_license_scan.cli import parse_args
from dash_license_scan.parsers import parse_crate, parse_pypi

log = logging.getLogger(__name__)

# FIXME
logging.basicConfig(level=logging.DEBUG)

# ----------------------------------------------------------------------------------


def real_main(argv: list[str] | None = None) -> None:
    log.debug("Starting dash_license_scan.main(%s)", argv)
    args = parse_args(argv)
    log.debug("Parsed args: %s", args)

    jar_path = jar.get_jar()
    log.debug(f"Using dash-licenses JAR at {jar_path}")

    deps = []

    if args.pypi:
        deps.extend(parse_pypi(args.pypi))

    if args.crate:
        deps.extend(parse_crate(args.crate))

    if args.dry_run:
        print("Detected dependencies:")
        print("\n".join(deps))
        return
    else:
        # TODO: should we cache the results? Forever? For some minutes? Configurable?

        cmd = ["java", "-jar", str(jar_path)] + args.passthrough
        ...  # subprocess.run(cmd, check=True)


def main(argv: list[str] | None = None) -> None:
    # Catch SystemExit to return an int exit code.
    # This makes it easier to call from tests:
    # - normal exit: return None
    # - error exit: raise SystemExit with code
    try:
        real_main(argv)
    except SystemExit as e:
        if isinstance(e.code, int):
            if e.code != 0:
                print(f"Exiting with code {e.code}", file=sys.stderr)
                raise
            else:
                return  # normal exit
        else:
            print(f"Exiting with message: {e.code}", file=sys.stderr)
            raise


if __name__ == "__main__":
    main()
