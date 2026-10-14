import pytest

from openpod.models.metadata import Metadata
from openpod.parser import MetadataParser


def test_metadata_model():
    metadata = Metadata(
        name="Test",
        application="POD Go Edit",
        app_version=1,
        build_sha="abc123",
        modified_date=0,
    )

    assert metadata.name == "Test"


def test_metadata_parser_maps_preset_json_fields():
    parser = MetadataParser(
        {
            "name": "Richie Sambora",
            "application": "POD Go Edit",
            "appversion": 38797312,
            "build_sha": "v2.01-19-g6e98447",
            "modifieddate": 1785679028,
        }
    )

    metadata = parser.parse()

    assert metadata == Metadata(
        name="Richie Sambora",
        application="POD Go Edit",
        app_version=38797312,
        build_sha="v2.01-19-g6e98447",
        modified_date=1785679028,
    )


def test_metadata_parser_reports_missing_field():
    parser = MetadataParser({"name": "Incomplete"})

    with pytest.raises(KeyError, match="application"):
        parser.parse()
