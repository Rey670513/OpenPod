import math
from numbers import Real

from .parameter import Parameter

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

        self.validate_parameter_value(parameter, value)
        self._block[parameter] = value

    def validate_parameter_value(self, parameter, value):
        """Reject non-finite numbers; subclasses may enforce known limits."""
        if isinstance(value, Real) and not math.isfinite(value):
            raise ValueError(f"{parameter} must be a finite number")

    def __getitem__(self, parameter):
        return self.get(parameter)

    def __setitem__(self, parameter, value):
        self.set(parameter, value)

    def parameter(self, name):
        if name not in self.parameters:
            raise KeyError(name)

        return Parameter(self, name)
