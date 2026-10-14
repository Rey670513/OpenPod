from openpod import Preset
from openpod.editor import Amp, Block, Cab, PresetEditor


def test_public_api():
    assert Preset is not None


def test_editor_exports_typed_blocks():
    from openpod.editor.amp import Amp as AmpImplementation
    from openpod.editor.block import Block as BlockImplementation
    from openpod.editor.cab import Cab as CabImplementation

    assert Amp is AmpImplementation
    assert Block is BlockImplementation
    assert Cab is CabImplementation
    assert PresetEditor is not None
