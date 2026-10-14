"""
Cab editor.
"""

from .block import Block


class Cab(Block):
    def __init__(self, block):
        super().__init__(block)

    @property
    def low_cut(self):
        return self._block["LowCut"]

    @low_cut.setter
    def low_cut(self, value):
        self._block["LowCut"] = float(value)

    @property
    def high_cut(self):
        return self._block["HighCut"]

    @high_cut.setter
    def high_cut(self, value):
        self._block["HighCut"] = float(value)

    @property
    def distance(self):
        return self._block["Distance"]

    @distance.setter
    def distance(self, value):
        self._block["Distance"] = float(value)

    @property
    def level(self):
        return self._block["Level"]

    @level.setter
    def level(self, value):
        self._block["Level"] = float(value)

