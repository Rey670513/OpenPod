from openpod.editor import PresetEditor
from openpod.editor.block import Block


def test_find_existing_model():
    preset = PresetEditor("Richie Sambora.pgp")

    block = preset.find_model("HD2_DelayElephantManStereo")

    assert isinstance(block, Block)
    assert block.model == "HD2_DelayElephantManStereo"


def test_find_missing_model():
    preset = PresetEditor("Richie Sambora.pgp")

    try:
        preset.find_model("DOES_NOT_EXIST")
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError")
