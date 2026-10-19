from openpod.models.header import Header
from openpod.parser.binary import BinaryReader


class HeaderParser:
    """Parse the fixed-size header fields from a binary reader."""

    def __init__(self, reader: BinaryReader):
        self.reader = reader

    def parse(self) -> Header:
        return Header(
            magic=self.reader.read_bytes(4),
            version=self.reader.read_u32(),
        )
