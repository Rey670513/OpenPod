"""
Amp editor.
"""

import math
from numbers import Real

from .block import Block


class Amp(Block):
    NORMALIZED_PARAMETERS = frozenset({
        "Bass",
        "Bias",
        "BiasX",
        "ChVol",
        "Drive",
        "Hum",
        "Master",
        "Mid",
        "Presence",
        "Ripple",
        "Sag",
        "Treble",
    })

    def __init__(self, block):
        super().__init__(block)

    def validate_parameter_value(self, parameter, value):
        if parameter not in self.NORMALIZED_PARAMETERS:
            return

        if (
            isinstance(value, bool)
            or not isinstance(value, Real)
            or not math.isfinite(value)
            or not 0.0 <= value <= 1.0
        ):
            raise ValueError(
                f"{parameter} must be a finite number between 0.0 and 1.0"
            )

    @property
    def model(self):
        return self._block["@model"]

    @property
    def drive(self):
        return self._block["Drive"]

    @drive.setter
    def drive(self, value):
        self.set("Drive", float(value))

    @property
    def bass(self):
        return self._block["Bass"]

    @bass.setter
    def bass(self, value):
        self.set("Bass", float(value))

    @property
    def mid(self):
        return self._block["Mid"]

    @mid.setter
    def mid(self, value):
        self.set("Mid", float(value))

    @property
    def treble(self):
        return self._block["Treble"]

    @treble.setter
    def treble(self, value):
        self.set("Treble", float(value))

    @property
    def presence(self):
        return self._block["Presence"]

    @presence.setter
    def presence(self, value):
        self.set("Presence", float(value))

    @property
    def master(self):
        return self._block["Master"]

    @master.setter
    def master(self, value):
        self.set("Master", float(value))

