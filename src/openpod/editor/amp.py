"""
Amp editor.
"""


class Amp:
    def __init__(self, block):
        self._block = block

    @property
    def model(self):
        return self._block["@model"]

    @property
    def drive(self):
        return self._block["Drive"]

    @drive.setter
    def drive(self, value):
        self._block["Drive"] = float(value)

    @property
    def bass(self):
        return self._block["Bass"]

    @bass.setter
    def bass(self, value):
        self._block["Bass"] = float(value)

    @property
    def mid(self):
        return self._block["Mid"]

    @mid.setter
    def mid(self, value):
        self._block["Mid"] = float(value)

    @property
    def treble(self):
        return self._block["Treble"]

    @treble.setter
    def treble(self, value):
        self._block["Treble"] = float(value)

    @property
    def presence(self):
        return self._block["Presence"]

    @presence.setter
    def presence(self, value):
        self._block["Presence"] = float(value)

    @property
    def master(self):
        return self._block["Master"]

    @master.setter
    def master(self, value):
        self._block["Master"] = float(value)
        