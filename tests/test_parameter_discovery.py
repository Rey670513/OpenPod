from openpod.editor import PresetEditor


def test_parameters_are_list():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    assert isinstance(delay.parameters, list)


def test_parameters_exclude_metadata():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    assert all(not name.startswith("@") for name in delay.parameters)


def test_parameters_are_readable():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    for name in delay.parameters:
        assert delay.get(name) == delay[name]


def test_parameters_returns_independent_list():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    parameters = delay.parameters
    parameters.clear()

    assert delay.parameters
