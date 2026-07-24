from openpod.parser.hexdump import hexdump


def test_hexdump():
    text = hexdump(b"OpenPod")

    assert "4F 70 65 6E" in text
    assert "OpenPod" in text
    