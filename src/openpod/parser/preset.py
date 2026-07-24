from .binary import BinaryReader


class Preset:
    """Represents a POD Go preset."""

    def __init__(self, data: bytes):
        self._data = data

    @classmethod
    def load(cls, filename: str) -> "Preset":
        """Load a preset from a .pgp file."""
        reader = BinaryReader(filename)
        return cls(reader.read())

    @property
    def size(self) -> int:
        """Return the preset size in bytes."""
        return len(self._data)

    @property
    def raw(self) -> bytes:
        """Return the raw preset bytes."""
        return self._data
    