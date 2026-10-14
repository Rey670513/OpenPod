from openpod.editor import PresetEditor
from openpod.editor.amp import Amp
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


def test_find_amp_model_returns_typed_amp():
    preset = PresetEditor("Richie Sambora.pgp")

    amp = preset.find_model(preset.amp.model)

    assert isinstance(amp, Amp)
    assert amp.data is preset.amp.data
    assert amp.model == preset.amp.model
