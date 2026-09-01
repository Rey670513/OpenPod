class Block:
    """
    Base editor for POD Go DSP blocks.
    """

    def __init__(self, block):
        self._block = block

    @property
    def model(self):
        return self._block.get("@model")

    @property
    def enabled(self):
        return self._block.get("@enabled", True)

    @enabled.setter
    def enabled(self, value):
        self._block["@enabled"] = bool(value)

    @property
    def data(self):
        return self._block

    @property
    def parameters(self):
        return [
            key
            for key in self._block
            if not key.startswith("@")
        ]

    def get(self, parameter):
        return self._block[parameter]

    def set(self, parameter, value):
        if parameter.startswith("@"):
            raise KeyError(parameter)

        self._block[parameter] = value
