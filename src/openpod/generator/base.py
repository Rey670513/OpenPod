from importlib.resources import files

from openpod.editor import PresetEditor


class BaseGenerator(PresetEditor):

    def __init__(self, template_name):
        template = files("openpod.templates").joinpath(template_name)
        super().__init__(str(template))
        