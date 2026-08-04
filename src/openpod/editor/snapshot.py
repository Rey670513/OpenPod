"""
Snapshot editor.
"""


class Snapshot:
    def __init__(self, data):
        self._data = data

    @property
    def name(self):
        return self._data["@name"]

    @name.setter
    def name(self, value):
        self._data["@name"] = str(value)
        