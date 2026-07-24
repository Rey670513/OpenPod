import json

from openpod.models.metadata import Metadata


class MetadataParser:

    @staticmethod
    def parse(data: bytes) -> Metadata:
        document = json.loads(data.decode("utf-8"))
        meta = document["data"]["meta"]

        return Metadata(
            name=meta["name"],
            application=meta["application"],
            app_version=meta["appversion"],
            build_sha=meta["build_sha"],
            modified_date=meta["modifieddate"],
        )
    