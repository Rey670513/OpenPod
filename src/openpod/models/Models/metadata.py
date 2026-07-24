from dataclasses import dataclass

@dataclass(slots=True)
class Metadata:
    name: str
    application: str
    app_version: int
    build_sha: str
    modified_date: int
    