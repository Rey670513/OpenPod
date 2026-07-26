from dataclasses import dataclass


@dataclass(slots=True)
class Header:
    magic: bytes
    version: int
    