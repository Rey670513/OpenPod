import pytest

from openpod.editor import PresetEditor
from openpod.editor.amp import Amp
from openpod.editor.block import Block


def test_preset_amp_is_a_block():
    preset = PresetEditor("Richie Sambora.pgp")

    assert isinstance(preset.amp, Amp)
    assert isinstance(preset.amp, Block)


@pytest.mark.parametrize(
    "value",
    [-0.1, 1.01, float("nan"), float("inf")],
)
def test_amp_rejects_drive_outside_normalized_range(value):
    preset = PresetEditor("Richie Sambora.pgp")
    original_drive = preset.amp.drive

    with pytest.raises(ValueError):
        preset.amp.drive = value

    assert preset.amp.drive == original_drive
