import pyarrow.parquet as pq


DATASET_PATH = (
    "hf://datasets/ai4bharat/MSMARCO-XI/"
    "train/hintrain.parquet"
)


print("Connecting to MSMARCO-XI Hindi train data...")


with pq.ParquetFile(DATASET_PATH) as parquet_file:

    metadata = parquet_file.metadata

    print("\n==============================")
    print("DATASET INFORMATION")
    print("==============================")

    print("Rows:", metadata.num_rows)
    print("Row groups:", metadata.num_row_groups)

    print("\nColumns:")
    print(parquet_file.schema_arrow.names)

    print("\n==============================")
    print("COLUMN SIZES")
    print("==============================")

    row_group = metadata.row_group(0)

    for i in range(row_group.num_columns):

        column = row_group.column(i)

        print(
            f"{column.path_in_schema}: "
            f"{column.total_compressed_size / (1024 * 1024):.2f} MB"
        )

    print("\nMetadata inspection complete.")