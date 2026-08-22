import pyarrow.parquet as pq


DATASET_PATH = (
    "hf://datasets/ai4bharat/MSMARCO-XI/"
    "train/hintrain.parquet"
)


class DatasetLoader:
    """Read MSMARCO-XI remotely in small Parquet batches."""

    def __init__(self, dataset_path: str = DATASET_PATH):
        self.dataset_path = dataset_path

    def iter_records(self, max_records: int = 5):
        if max_records <= 0:
            return

        columns = [
            "query_id",
            "query_type",
            "query",
            "Answer",
            "Eng_Query",
            "Eng_Answer",
        ]

        parquet_file = pq.ParquetFile(self.dataset_path)

        records_read = 0

        for batch in parquet_file.iter_batches(
            batch_size=min(max_records, 5),
            columns=columns,
            use_threads=False,
        ):
            for record in batch.to_pylist():
                yield record

                records_read += 1

                if records_read >= max_records:
                    return