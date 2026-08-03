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
        