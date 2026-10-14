import pytest

from openpod.editor import PresetEditor


def test_snapshot_parameter_values_are_independent_and_persist(tmp_path):
    preset = PresetEditor("Richie Sambora.pgp")
    output = tmp_path / "snapshot-amp.pgp"
    amp = preset.amp
    original_drive = amp.drive

    preset.snapshots[0].set_parameter(amp, "Drive", 0.4)
    preset.snapshots[1].set_parameter(amp, "Drive", 0.8)
    preset.snapshots[2].set_parameter(amp, "Drive", 0.2)
    preset.snapshots[3].set_parameter(amp, "Drive", 0.6)
    preset.snapshots[1].name = "Lead"
    preset.snapshots[2].name = "Rhythm"
    preset.snapshots[3].name = "Clean"
    preset.save(output)

    reloaded = PresetEditor(output)
    reloaded_amp = reloaded.amp

    assert reloaded.snapshots[0].get_parameter(reloaded_amp, "Drive") == 0.4
    assert reloaded.snapshots[1].get_parameter(reloaded_amp, "Drive") == 0.8
    assert reloaded.snapshots[2].get_parameter(reloaded_amp, "Drive") == 0.2
    assert reloaded.snapshots[3].get_parameter(reloaded_amp, "Drive") == 0.6
    assert all(snapshot._data["@valid"] for snapshot in reloaded.snapshots)
    assert reloaded_amp.drive == original_drive


def test_snapshot_parameter_assignment_uses_pod_go_controller():
    preset = PresetEditor("Richie Sambora.pgp")

    preset.snapshots[1].set_parameter(preset.amp, "Drive", 0.85)

    assignment = preset.data["data"]["tone"]["controller"]["dsp0"]["block3"]["Drive"]
    assert assignment["@controller"] == 11
    assert assignment["@min"] <= 0.85 <= assignment["@max"]
    assert preset.data["data"]["tone"]["snapshot1"]["@valid"] is True


def test_activating_unused_snapshot_inherits_base_block_bypass_states():
    preset = PresetEditor("Richie Sambora.pgp")
    tone = preset.data["data"]["tone"]

    preset.snapshots[1].set_parameter(preset.amp, "Drive", 0.85)

    snapshot_blocks = tone["snapshot1"]["blocks"]["dsp0"]
    for key, block in tone["dsp0"].items():
        if key.startswith("block"):
            assert snapshot_blocks[key] is block["@enabled"]

    # This preset's FX Loop block is off in its base state; an unused snapshot
    # must not silently turn it on when the snapshot is first activated.
    assert snapshot_blocks["block2"] is False


def test_snapshot_block_enabled_state_is_independent_and_persists(tmp_path):
    preset = PresetEditor("Richie Sambora.pgp")
    distortion = preset.find_model("HD2_DistScream808Mono")
    output = tmp_path / "snapshot-bypass.pgp"

    preset.snapshots[1].set_block_enabled(distortion, False)
    preset.snapshots[2].set_block_enabled(distortion, True)
    preset.save(output)

    reloaded = PresetEditor(output)
    reloaded_distortion = reloaded.find_model("HD2_DistScream808Mono")

    assert reloaded.snapshots[1].get_block_enabled(reloaded_distortion) is False
    assert reloaded.snapshots[2].get_block_enabled(reloaded_distortion) is True
    assert reloaded_distortion.enabled is True
    assert reloaded.snapshots[1]._data["@valid"] is True


def test_unused_snapshot_block_state_reads_from_preset_base():
    preset = PresetEditor("Richie Sambora.pgp")
    fx_loop = preset.find_model("HD2_FXLoopMono1")

    assert preset.snapshots[1].get_block_enabled(fx_loop) is False


def test_snapshot_rejects_unknown_block_parameter():
    preset = PresetEditor("Richie Sambora.pgp")

    with pytest.raises(KeyError):
        preset.snapshots[0].set_parameter(preset.amp, "NotAParameter", 1.0)


def test_snapshot_rejects_out_of_range_amp_value_without_mutating_preset():
    preset = PresetEditor("Richie Sambora.pgp")
    snapshot = preset.snapshots[1]
    original = preset.data["data"]["tone"]
    original_drive = preset.amp.drive

    with pytest.raises(ValueError, match="between 0.0 and 1.0"):
        snapshot.set_parameter(preset.amp, "Drive", 3.5)

    assert preset.amp.drive == original_drive
    assert snapshot._data["@valid"] is False
    assert "controller" in original
    assert "block3" not in original["controller"]["dsp0"]


def test_snapshot_allows_generic_parameter_values_above_one():
    preset = PresetEditor("Richie Sambora.pgp")
    cab = preset.cab

    preset.snapshots[1].set_parameter(cab, "HighCut", 12000.0)

    assert preset.snapshots[1].get_parameter(cab, "HighCut") == 12000.0
