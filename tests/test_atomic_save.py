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


def test_failed_temp_write_preserves_original_file(
    tmp_path, monkeypatch
):
    source = tmp_path / "source.pgp"
    original_content = (
        '{"data": {"meta": {"name": "Original"}}}'
    )
    source.write_text(original_content)

    preset = PresetEditor(source)
    preset.name = "Edited"

    class FailingWriter:
        def __init__(self, wrapped):
            self.wrapped = wrapped

        def __enter__(self):
            self.wrapped.__enter__()
            return self

        def __exit__(self, *args):
            return self.wrapped.__exit__(*args)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def write(self, content):
            raise OSError("Simulated write failure")

    import openpod.editor.preset as preset_module

    real_temp_file = preset_module.tempfile.NamedTemporaryFile

    def failing_temp_file(*args, **kwargs):
        return FailingWriter(real_temp_file(*args, **kwargs))

    monkeypatch.setattr(
        preset_module.tempfile,
        "NamedTemporaryFile",
        failing_temp_file,
    )

    with pytest.raises(OSError, match="Simulated write failure"):
        preset.save()

    assert source.read_text() == original_content
    assert list(tmp_path.iterdir()) == [source]


def test_save_as_creates_valid_preset_without_changing_source(
    tmp_path,
):
    source = tmp_path / "source.pgp"
    original_content = (
        '{"data": {"meta": {"name": "Original"}}}'
    )
    source.write_text(original_content)

    preset = PresetEditor(source)
    preset.name = "New Preset"
    output = tmp_path / "new-preset.pgp"

    preset.save(output)

    assert json.loads(output.read_text())["data"]["meta"]["name"] == (
        "New Preset"
    )
    assert source.read_text() == original_content
