import pytest

from openpod.editor import PresetEditor


def test_missing_parameter_raises_key_error():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    with pytest.raises(KeyError):
        delay.parameter("DoesNotExist").value


def test_metadata_is_not_a_parameter():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")

    with pytest.raises(KeyError):
        delay.parameter("@model")


def test_parameter_type_updates_after_value_change():
    preset = PresetEditor("Richie Sambora.pgp")

    delay = preset.find_model("HD2_DelayElephantManStereo")
    parameter = delay.parameter("Mix")

    assert parameter.type is float

    parameter.value = 1

    assert parameter.value == 1
    assert parameter.type is int
