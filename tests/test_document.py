from data.document import Document


def test_document_creation():
    document = Document(
        id="1185869",
        text="भारत में परमाणु ऊर्जा का विकास हुआ।",
        metadata={
            "query_id": 1185869,
            "query_type": "DESCRIPTION",
        },
    )

    assert document.id == "1185869"
    assert document.text == "भारत में परमाणु ऊर्जा का विकास हुआ।"
    assert document.metadata["query_id"] == 1185869


def test_document_metadata_is_preserved():
    metadata = {
        "query_id": 123,
        "query_type": "DESCRIPTION",
    }

    document = Document(
        id="123",
        text="test text",
        metadata=metadata,
    )

    assert document.metadata == metadata