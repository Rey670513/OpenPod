from openpod.editor.block import Block


def test_block_model():
    data = {
        "@model": "HD2_TestModel",
        "@enabled": True,
        "Mix": 0.5,
    }

    block = Block(data)

    assert block.model == "HD2_TestModel"


def test_block_enabled():
    data = {
        "@model": "HD2_TestModel",
        "@enabled": True,
    }

    block = Block(data)

    assert block.enabled is True

    block.enabled = False

    assert block.enabled is False


def test_block_data():
    data = {
        "@model": "HD2_TestModel",
        "@enabled": True,
        "Mix": 0.5,
    }

    block = Block(data)

    assert block.data is data
    assert block.data["Mix"] == 0.5
