from openpod.editor import PresetEditor


def test_preset_exposes_four_snapshots():
    preset = PresetEditor("Richie Sambora.pgp")

    assert len(preset.snapshots) == 4
    assert [snapshot.name for snapshot in preset.snapshots] == [
        "SNAPSHOT 1",
        "SNAPSHOT 2",
        "SNAPSHOT 3",
        "SNAPSHOT 4",
    ]


def test_snapshot_name_change_survives_save_and_reload(tmp_path):
    preset = PresetEditor("Richie Sambora.pgp")
    output = tmp_path / "renamed-snapshot.pgp"

    preset.snapshots[1].name = 42
    preset.save(output)

    reloaded = PresetEditor(output)

    assert reloaded.snapshots[1].name == "42"
