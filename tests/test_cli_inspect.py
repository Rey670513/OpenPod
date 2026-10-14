import json
from pathlib import Path

import pytest

from openpod.__main__ import main


SAMPLE = Path(__file__).parents[1] / "src" / "openpod" / "templates" / "richie_sambora.pgp"


def test_inspect_shows_preset_blocks_and_snapshots(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["openpod", "inspect", str(SAMPLE)])

    main()

    output = capsys.readouterr().out
    assert "Preset: Richie Sambora" in output
    assert "Blocks:" in output
    assert "HD2_DistScream808Mono" in output
    assert "Snapshots:" in output
    assert "SNAPSHOT 4" in output


def test_inspect_reports_missing_file(monkeypatch, capsys, tmp_path):
    missing = tmp_path / "missing.pgp"
    monkeypatch.setattr("sys.argv", ["openpod", "inspect", str(missing)])

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2
    assert "tidak ditemukan" in capsys.readouterr().err


def test_inspect_reports_invalid_preset_json(monkeypatch, capsys, tmp_path):
    invalid = tmp_path / "invalid.pgp"
    invalid.write_text("not a preset")
    monkeypatch.setattr("sys.argv", ["openpod", "inspect", str(invalid)])

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2
    assert "JSON preset tidak valid" in capsys.readouterr().err
