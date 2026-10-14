from openpod.editor import Amp, Block, Cab, PresetEditor
from openpod.parser.block import BlockParser


def test_block_parser_maps_preset_slots_to_typed_editors():
    preset = PresetEditor("Richie Sambora.pgp")
    parser = BlockParser(preset.data["data"]["tone"]["dsp0"])

    blocks = parser.parse()

    assert len(blocks) == len(preset.blocks)
    assert isinstance(blocks[0], Block)
    assert isinstance(blocks[3], Amp)
    assert isinstance(blocks[4], Cab)
    assert blocks[3].model == preset.amp.model
    assert blocks[4].model == preset.cab.model


def test_block_parser_skips_non_block_dsp_entries():
    blocks = BlockParser(
        {
            "tempo": 120,
            "block0": {"@model": "Delay", "@enabled": True},
            "metadata": {"name": "test"},
        }
    ).parse()

    assert len(blocks) == 1
    assert blocks[0].model == "Delay"
