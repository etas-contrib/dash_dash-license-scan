from pathlib import Path

import pytest
from dash_license_scan.main import main


def _data_files():
    data_dir = Path(__file__).parent / "data"
    for p in sorted(data_dir.iterdir()):
        if p.is_dir():
            # skip directories like __pycache__
            continue
        if p.name.endswith("_expected.txt"):
            continue
        yield p


@pytest.mark.parametrize("input_path", list(_data_files()), ids=lambda p: p.stem)
def test_file_based(input_path, capsys):
    # Each input has a matching *_expected.txt file
    expected_path = input_path.with_name(input_path.stem + "_expected.txt")
    assert expected_path.exists(), f"expected file missing: {expected_path}"

    package_manager: str = input_path.stem.partition("_")[0]

    # Run main with a relative path as tests expect
    main(["--dry-run", "--" + package_manager, str(input_path)])

    captured = capsys.readouterr()
    assert not captured.err, f"Unexpected stderr: {captured.err}"

    expected = expected_path.read_text()
    assert expected in captured.out
