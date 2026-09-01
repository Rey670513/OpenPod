class Parameter:
    """
    Represents a single POD Go block parameter.
    """

    def __init__(self, block, name):
        self._block = block
        self.name = name

    @property
    def value(self):
        return self._block.get(self.name)

    @property
    def type(self):
        return type(self.value)
