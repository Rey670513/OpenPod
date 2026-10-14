from openpod.editor import PresetEditor


def test_typed_amp_and_cab_changes_survive_save_and_reload(tmp_path):
    preset = PresetEditor("Richie Sambora.pgp")
    output = tmp_path / "edited.pgp"

    preset.amp.drive = 4.25
    preset.cab.level = -3.5
    preset.save(output)

    reloaded = PresetEditor(output)

    assert reloaded.amp.drive == 4.25
    assert reloaded.cab.level == -3.5
