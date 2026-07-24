from dataclasses import dataclass


@dataclass(slots=True)
class Metadata:
    """Metadata of a POD Go preset."""

    name: str
    application: str
    app_version: int
    build_sha: str
    modified_date: int
    