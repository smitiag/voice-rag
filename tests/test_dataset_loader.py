from data.dataset_loader import DatasetLoader


def test_dataset_loader_structure():
    loader = DatasetLoader()

    assert hasattr(loader, "iter_records")


def test_dataset_loader_limit_validation():
    loader = DatasetLoader()

    records = list(loader.iter_records(max_records=0))

    assert records == []


def test_dataset_loader_reads_records():
    loader = DatasetLoader()

    records = list(loader.iter_records(max_records=5))

    assert len(records) == 5

    for record in records:
        assert "query_id" in record
        assert "query" in record
        assert "Answer" in record