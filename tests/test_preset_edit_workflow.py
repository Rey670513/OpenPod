from openpod.editor import PresetEditor


def test_editing_preset_name_amp_cab_and_snapshot_survives_save_as(tmp_path):
    preset = PresetEditor("Richie Sambora.pgp")
    original_name = preset.name
    output = tmp_path / "soul-blues.pgp"

    preset.name = "Soul Blues"
    preset.amp.drive = 4.25
    preset.cab.level = -3.5
    preset.snapshots[1].name = "Lead"
    preset.save(output)

    reloaded = PresetEditor(output)

    assert reloaded.name == "Soul Blues"
    assert reloaded.amp.drive == 4.25
    assert reloaded.cab.level == -3.5
    assert reloaded.snapshots[1].name == "Lead"
    assert PresetEditor("Richie Sambora.pgp").name == original_name
