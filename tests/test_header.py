from openpod.parser.binary import BinaryReader
from openpod.parser.header import HeaderParser


def test_parse_header():
    data = b"PODG" + (2).to_bytes(4, "little")

    reader = BinaryReader(data)

    header = HeaderParser(reader).parse()

    assert header.magic == b"PODG"
    assert header.version == 2


def test_parse_header_rejects_truncated_data():
    import pytest

    reader = BinaryReader(b"PODG\x02")

    with pytest.raises(EOFError, match="Unexpected end of file"):
        HeaderParser(reader).parse()
