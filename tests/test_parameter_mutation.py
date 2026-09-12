from openpod.editor import PresetEditor


def test_parameter_value_can_be_changed():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")
    parameter = delay.parameter("Mix")

    original = parameter.value
    parameter.value = 0.50

    assert parameter.value == 0.50
    assert parameter.value != original
    assert delay["Mix"] == 0.50


def test_parameter_change_updates_block_data():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")
    parameter = delay.parameter("Time")

    parameter.value = 0.75

    assert delay.get("Time") == 0.75
    assert delay.data["Time"] == 0.75
