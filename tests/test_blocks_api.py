from openpod.editor import PresetEditor
from openpod.editor.amp import Amp


def test_preset_blocks():
    preset = PresetEditor("Richie Sambora.pgp")

    blocks = preset.blocks

    assert isinstance(blocks, list)
    assert len(blocks) > 0


def test_preset_blocks_models():
    preset = PresetEditor("Richie Sambora.pgp")

    models = [block.model for block in preset.blocks]

    assert "HD2_AmpBrit2204" in models
    assert "HD2_Cab4x12Blackback30" in models


def test_preset_blocks_uses_typed_amp():
    preset = PresetEditor("Richie Sambora.pgp")

    amp = next(block for block in preset.blocks if block.model == preset.amp.model)

    assert isinstance(amp, Amp)
