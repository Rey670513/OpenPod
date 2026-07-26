from openpod.models.metadata import Metadata


def test_metadata_model():
    metadata = Metadata(
        name="Test",
        application="POD Go Edit",
        app_version=1,
        build_sha="abc123",
        modified_date=0,
    )

    assert metadata.name == "Test"
    