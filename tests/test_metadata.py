from openpod.models.metadata import Metadata


def test_metadata():
    metadata = Metadata(
        name="Test",
        application="POD Go Edit",
        app_version=1,
        build_sha="abc123",
        modified_date=0,
    )

    assert metadata.name == "Test"
    assert metadata.application == "POD Go Edit"
    assert metadata.app_version == 1
    assert metadata.build_sha == "abc123"
    