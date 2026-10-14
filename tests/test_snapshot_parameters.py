import pytest

from openpod.editor import PresetEditor


def test_snapshot_parameter_values_are_independent_and_persist(tmp_path):
    preset = PresetEditor("Richie Sambora.pgp")
    output = tmp_path / "snapshot-amp.pgp"
    amp = preset.amp
    original_drive = amp.drive

    preset.snapshots[0].set_parameter(amp, "Drive", 0.4)
    preset.snapshots[1].set_parameter(amp, "Drive", 0.8)
    preset.save(output)

    reloaded = PresetEditor(output)
    reloaded_amp = reloaded.amp

    assert reloaded.snapshots[0].get_parameter(reloaded_amp, "Drive") == 0.4
    assert reloaded.snapshots[1].get_parameter(reloaded_amp, "Drive") == 0.8
    assert reloaded_amp.drive == original_drive


def test_snapshot_parameter_assignment_uses_pod_go_controller():
    preset = PresetEditor("Richie Sambora.pgp")

    preset.snapshots[1].set_parameter(preset.amp, "Drive", 0.85)

    assignment = preset.data["data"]["tone"]["controller"]["dsp0"]["block3"]["Drive"]
    assert assignment["@controller"] == 11
    assert assignment["@min"] <= 0.85 <= assignment["@max"]
    assert preset.data["data"]["tone"]["snapshot1"]["@valid"] is True


def test_snapshot_rejects_unknown_block_parameter():
    preset = PresetEditor("Richie Sambora.pgp")

    with pytest.raises(KeyError):
        preset.snapshots[0].set_parameter(preset.amp, "NotAParameter", 1.0)
