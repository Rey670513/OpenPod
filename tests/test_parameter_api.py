from openpod.editor import PresetEditor


def test_block_get_parameter():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    value = delay.get("Mix")

    assert value is not None


def test_block_set_parameter():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    original = delay.get("Mix")

    delay.set("Mix", 0.25)

    assert delay.get("Mix") == 0.25

    delay.set("Mix", original)


def test_block_get_missing_parameter():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    try:
        delay.get("DOES_NOT_EXIST")
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError")


def test_block_set_metadata_is_rejected():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    try:
        delay.set("@model", "BROKEN_MODEL")
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError")
