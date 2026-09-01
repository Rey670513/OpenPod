from openpod.editor import PresetEditor


def test_block_parameter_getitem():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    assert delay["Mix"] == delay.get("Mix")


def test_block_parameter_setitem():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    original = delay["Mix"]

    delay["Mix"] = original

    assert delay["Mix"] == original


def test_block_metadata_getitem_is_allowed():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    assert delay["@model"] == "HD2_DelayElephantManStereo"


def test_block_metadata_setitem_is_rejected():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    try:
        delay["@model"] = "BROKEN_MODEL"
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError")
