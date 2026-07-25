from openpod.parser.binary import BinaryReader


def test_read_u8():
    reader = BinaryReader(b"\x2A")
    assert reader.read_u8() == 42


def test_read_u16():
    reader = BinaryReader(b"\x34\x12")
    assert reader.read_u16() == 0x1234


def test_read_u32():
    reader = BinaryReader(b"\x78\x56\x34\x12")
    assert reader.read_u32() == 0x12345678


def test_read_string():
    reader = BinaryReader(b"OpenPod\x00Extra")
    assert reader.read_string(8) == "OpenPod"


def test_remaining():
    reader = BinaryReader(b"\x01\x02\x03")

    reader.read_u8()

    assert reader.remaining() == 2
    