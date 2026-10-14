from openpod.editor import PresetEditor
from openpod.editor.amp import Amp
from openpod.editor.block import Block


def test_preset_amp_is_a_block():
    preset = PresetEditor("Richie Sambora.pgp")

    assert isinstance(preset.amp, Amp)
    assert isinstance(preset.amp, Block)
