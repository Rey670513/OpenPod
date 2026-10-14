"""Parse metadata fields from a JSON-formatted POD Go preset."""

from collections.abc import Mapping

from openpod.models.metadata import Metadata


class MetadataParser:
    """Convert the preset's ``data.meta`` object into a Metadata model."""

    def __init__(self, data: Mapping):
        self.data = data

    def parse(self) -> Metadata:
        return Metadata(
            name=self.data["name"],
            application=self.data["application"],
            app_version=self.data["appversion"],
            build_sha=self.data["build_sha"],
            modified_date=self.data["modifieddate"],
        )
