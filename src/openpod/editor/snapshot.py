"""
Snapshot editor.
"""

from .block import Block


SNAPSHOT_CONTROLLER = 11


class Snapshot:
    def __init__(self, data, tone=None, key=None):
        self._data = data
        self._tone = tone
        self._key = key

    @property
    def name(self):
        return self._data["@name"]

    @name.setter
    def name(self, value):
        self._data["@name"] = str(value)

    def get_parameter(self, block, name):
        self._validate_parameter(block, name)
        block_key = self._block_key(block)
        value = (
            self._data.get("controllers", {})
            .get("dsp0", {})
            .get(block_key, {})
            .get(name)
        )

        if value is not None and "@value" in value:
            return value["@value"]

        return block.get(name)

    def get_block_enabled(self, block):
        self._validate_block(block)
        block_key = self._block_key(block)

        if not self._data.get("@valid", False):
            return block.enabled

        return (
            self._data.get("blocks", {})
            .get("dsp0", {})
            .get(block_key, block.enabled)
        )

    def set_block_enabled(self, block, enabled):
        self._validate_block(block)
        block_key = self._block_key(block)
        self._initialize_block_states()

        snapshot_blocks = self._data.setdefault("blocks", {}).setdefault("dsp0", {})
        snapshot_blocks[block_key] = bool(enabled)
        self._data["@valid"] = True

    def set_parameter(self, block, name, value):
        self._validate_parameter(block, name)
        block.validate_parameter_value(name, value)
        block_key = self._block_key(block)
        self._initialize_block_states()

        # A parameter assigned to snapshots needs a value entry in every slot.
        # Unset slots inherit the block's current value until explicitly changed.
        snapshot_values = []
        for index in range(4):
            snapshot_key = f"snapshot{index}"
            snapshot = self._tone[snapshot_key]
            controllers = snapshot.setdefault("controllers", {}).setdefault("dsp0", {})
            block_controllers = controllers.setdefault(block_key, {})
            parameter = block_controllers.setdefault(
                name,
                {"@fs_enabled": False, "@value": block.get(name)},
            )
            if "@value" not in parameter:
                parameter["@value"] = block.get(name)
            parameter.setdefault("@fs_enabled", False)
            snapshot_values.append(parameter["@value"])

        target_parameter = self._data["controllers"]["dsp0"][block_key][name]
        target_parameter["@value"] = value
        self._data["@valid"] = True
        snapshot_values[self._index()] = value

        assignment = (
            self._tone.setdefault("controller", {})
            .setdefault("dsp0", {})
            .setdefault(block_key, {})
        )
        assignment[name] = {
            "@min": min(snapshot_values),
            "@max": max(snapshot_values),
            "@controller": SNAPSHOT_CONTROLLER,
        }

    def _validate_parameter(self, block, name):
        self._validate_block(block)
        if name not in block.parameters:
            raise KeyError(name)

    def _validate_block(self, block):
        if not isinstance(block, Block):
            raise TypeError("block must be a Block instance")

    def _initialize_block_states(self):
        if self._data.get("@valid", False):
            return

        snapshot_blocks = self._data.setdefault("blocks", {}).setdefault("dsp0", {})
        for key, block_data in self._tone["dsp0"].items():
            if key.startswith("block") and "@enabled" in block_data:
                snapshot_blocks[key] = block_data["@enabled"]

    def _block_key(self, block):
        if self._tone is None:
            raise RuntimeError("snapshot parameter access requires a preset context")

        for key, data in self._tone["dsp0"].items():
            if key.startswith("block") and data is block.data:
                return key

        raise ValueError("block does not belong to this preset")

    def _index(self):
        if self._tone is None or self._key is None:
            raise RuntimeError("snapshot parameter access requires a preset context")
        return int(self._key.removeprefix("snapshot"))
