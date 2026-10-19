import json
from pathlib import Path

import pytest

from openpod.editor import PresetEditor


def test_failed_save_preserves_original_file_and_cleans_temp(
    tmp_path, monkeypatch
):
    source = tmp_path / "source.pgp"
    original_content = (
        '{\n "data": {"meta": {"name": "Original"}}\n}\n'
    )
    source.write_text(original_content)

    preset = PresetEditor(source)
    preset.name = "Edited"

    def fail_replace(self, target, *args, **kwargs):
        raise OSError("Simulated replacement failure")

    monkeypatch.setattr(Path, "replace", fail_replace)

    with pytest.raises(OSError, match="Simulated replacement failure"):
        preset.save()

    assert source.read_text() == original_content
    assert sorted(path.name for path in tmp_path.iterdir()) == [
        "source.pgp"
    ]
