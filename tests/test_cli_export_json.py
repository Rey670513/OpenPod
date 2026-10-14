import json
from pathlib import Path

from openpod.__main__ import main


SAMPLE = Path(__file__).parents[1] / "src" / "openpod" / "templates" / "richie_sambora.pgp"


def test_export_json_writes_preset_data_without_modifying_source(
    monkeypatch, tmp_path
):
    output = tmp_path / "preset.json"
    source_before = SAMPLE.read_bytes()
    monkeypatch.setattr(
        "sys.argv", ["openpod", "export-json", str(SAMPLE), str(output)]
    )

    main()

    assert json.loads(output.read_text()) == json.loads(source_before)
    assert SAMPLE.read_bytes() == source_before
