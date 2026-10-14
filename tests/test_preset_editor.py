from pathlib import Path

from openpod.editor import PresetEditor


def test_preset_name_can_be_changed():
    preset = PresetEditor("Richie Sambora.pgp")

    preset.name = "Soul Blues"

    assert preset.name == "Soul Blues"


def test_preset_name_change_survives_save_and_reload(tmp_path):
    preset = PresetEditor("Richie Sambora.pgp")
    output = tmp_path / "renamed-preset.pgp"

    preset.name = 42
    preset.save(output)

    reloaded = PresetEditor(output)

    assert reloaded.name == "42"


def test_save_without_filename_overwrites_loaded_preset(tmp_path):
    source = tmp_path / "source.pgp"
    source.write_bytes(Path("Richie Sambora.pgp").read_bytes())
    preset = PresetEditor(source)

    preset.name = "Saved in place"
    preset.save()

    reloaded = PresetEditor(source)

    assert reloaded.name == "Saved in place"
