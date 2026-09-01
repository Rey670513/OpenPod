from openpod.editor import PresetEditor


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
