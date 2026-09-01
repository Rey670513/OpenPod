from openpod.editor import PresetEditor


def test_parameter_object_name_and_value():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")
    parameter = delay.parameter("Mix")

    assert parameter.name == "Mix"
    assert parameter.value == delay["Mix"]
    assert parameter.type is float


def test_parameter_object_boolean_type():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")
    parameter = delay.parameter("TempoSync1")

    assert parameter.name == "TempoSync1"
    assert parameter.value is True
    assert parameter.type is bool
