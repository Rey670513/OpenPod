from dataclasses import dataclass

from .binary import BinaryReader


@dataclass
class Header:
    magic: bytes
    version: int


class HeaderParser:

    def __init__(self, reader: BinaryReader):
        self.reader = reader

    def parse(self) -> Header:
        magic = self.reader.read_bytes(4)
        version = self.reader.read_u32()

        return Header(
            magic=magic,
            version=version,
        )
    from openpod.models.header import Header
from openpod.parser.binary import BinaryReader


class HeaderParser:
    def __init__(self, reader: BinaryReader):
        self.reader = reader

    def parse(self) -> Header:
        return Header(
            magic=self.reader.read_bytes(4),
            version=self.reader.read_u32(),
        )
    