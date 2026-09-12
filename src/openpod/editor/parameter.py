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

    @value.setter
    def value(self, value):
        self._block.set(self.name, value)

    @property
    def type(self):
        return type(self.value)
